from django.urls import path,include
from .views import *

urlpatterns = [
    path("",index,name="index.html"),
    path("contact/",contact,name="contact.html"),
]