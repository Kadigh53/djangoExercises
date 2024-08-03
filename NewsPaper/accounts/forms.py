from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostumUser

class CostumUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model=CostumUser
        fields=('username' ,'email', 'age',)

class CostumUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model=CostumUser
        fields=('username' ,'email', 'age',)
