from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    class Meta:
        fields = ("fname","lname","username", "email", "password1", "password2")
        model = User
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email address"
        self.fields["fname"].label = "First name"
        self.fields["lname"].label = "Last name"
