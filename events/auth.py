from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
	def create_user(self, email, password, **kwargs):
		if not email:
			raise ValueError('Invalid Email Provided')

		elif not password:
			raise ValueError('Invalid Password Provided')

		if  not kwargs.get('username'):
			raise ValueError('Invalid Username Provided')
		
		user = self.model(email=self.normalize_email(email), username = kwargs.get('username'))

		user.set_password(password)

		user.save()

		return user

