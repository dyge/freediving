from django import forms
from . import models

class EventForm(forms.ModelForm):
    class Meta():
        model = models.Event
        fields = ('name','location','datum','desc')
        widgets = {
            'datum':forms.SelectDateWidget(),
            'name':forms.TextInput(attrs={'placeholder': ''}),
        }
        labels = {
            'desc':"Description",
        }

class ShopForm(forms.ModelForm):
    class Meta():
        model = models.Shop
        fields = ('name','location','desc')
        labels = {
            'desc':"Description",
        }

class VereinForm(forms.ModelForm):
    class Meta():
        model = models.Verein
        fields = ('name','location','desc')
        labels = {
            'desc':"Description",
        }

class BuddyForm(forms.ModelForm):
    class Meta():
        model = models.Buddy
        fields = ('fname','lname','ort','desc')
        labels = {
            'desc':"Description",
            'fname':"First Name",
            'lname':"Last Name",
            'ort':"Location",
        }
