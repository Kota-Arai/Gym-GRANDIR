from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ルートURLにhomeビューを割り当て
]
