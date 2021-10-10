from django.contrib.auth.forms import UserCreationForm

from app.models import user


class RegistrationForm(UserCreationForm):
    class Meta:
        model = user.User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  )
