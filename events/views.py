from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import viewsets, permissions, status, views
from rest_framework.response import Response
import json
from .models import User, Venue, Event
from .serializer import UserSerializer, EventSerializer, VenueSerializer

# Create your views here.

class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        if request.user:
            return user == request.user
        return False


class UserView(viewsets.ModelViewSet):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsUser(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        else:
        	return Response({
        		'status': 'Error',
        		'message': serializer.errors
        	}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
	def post(self, request, format=None):
		data = json.loads(request.body)
		email = data.get('email', None)
		password = data.get('password', None)

		user = authenticate(email=email, password=password)
	
		if user is not None:
			login(request, user)

			serialized = UserSerializer(user)

			return Response(serialized.data)

		else:
			return Response({
        		'status': 'Unauthorized',
        		'message': 'Invalid email/password'
        	}, status=status.HTTP_401_UNAUTHORIZED)


def index(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'eventslist.view.html')

def error404(request):
		return render(request, '404.view.html')

def error500(request):
		return render(request, '500.view.html')
