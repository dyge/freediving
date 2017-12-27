from django.conf.urls import url, include
from . import views

app_name = 'spots'

urlpatterns = [
    url(r"add_event/$", views.CreateEvent.as_view(), name="newevent"),
    url(r"add_shop/$", views.CreateShop.as_view(), name="newshop"),
    url(r"add_verein/$", views.CreateVerein.as_view(), name="newverein"),
    url(r"add_buddy/$", views.CreateBuddy.as_view(), name="newbuddy"),
]
