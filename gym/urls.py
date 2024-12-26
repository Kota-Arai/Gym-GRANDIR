from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ルートURLにhomeビューを割り当て
    path('about/',views.about, name='about'),  # /about/にaboutビューを割り当て
    path('contact/',views.contact, name='contact'),  # /contact/にcontactビューを割り当て 
]
