from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import User, Event, Venue

#user serializer for converting user data to JSON
class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(required=True, write_only=False)
	confirm_password = serializers.CharField(required=True, write_only=False)

	#metadata for User file conversion
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'confirm_password',
	 	'first_name', 'last_name')

		#for conversition of user data to python
		#compatible from JSON
		def create(self, validated_data):
			return User.objects.create(**validated_data)

  	#convert JSON user data to python compatible on data update 
  	def update(self, instance, validated_data):
  		instance.username = validated_data.get('username', instance.username)
  		instance.username = validated_data.get('first_name', instance.first_name)
  		instance.username = validated_data.get('last_name', instance.last_name)
  		instance.tagline = validated_data.get('email', instance.email)
  	
  		instance.save()
  		#verify password if provided
  		password = validated_data.get('password', None)
  		confirm_password = validated_data.get('confirm_password', None)

  		if password and confirm_password and password == confirm_password:
  			instance.set_password(password)

  		instance.save()

  		update_session_auth_hash(self.context.get('request'), instance)

  		return instance
    	




#event serializer for converting event data to JSON
class EventSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = ('Host', 'Venue', 'Date', 'Time')

		#convert JSON event data to python compatible on event creation	
		def create(self, validated_data):
			return Event.objects.create(**validated_data)

  	#convert JSON event data to python compatible on data update
  	def update(self, instance, validated_data):
  		instance.username = validated_data.get('Time', instance.Time)
  		instance.username = validated_data.get('Date', instance.Date)

  		instance.save()

  		return instance


#venue serializer for converting event data to JSON
class VenueSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = ('name', 'address', 'state')

		#convert JSON venue data to python compatible on venue creation
		def create(self, validated_data):
			return Event.objects.create(**validated_data)

  	#convert JSON venue data to python compatible on data update
  	def update(self, instance, validated_data):
  		instance.username = validated_data.get('name', instance.name)
  		instance.username = validated_data.get('address', instance.address)
  		instance.username = validated_data.get('state', instance.state)

  		instance.save()

  		return instance