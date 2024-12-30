from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ルートURLにhomeビューを割り当て
    path('about/',views.about, name='about'),  # /about/にaboutビューを割り当て
    path('contact/',views.contact, name='contact'),  # /contact/にcontactビューを割り当て 

    # 各ページのurlを追加
    path('access/', views.access, name='access'),   # /access/にaccessビューを割り当て
    path('training/', views.training, name='training'),   # /training/にtrainingビューを割り当て
    path('equipment/', views.equipment, name='equipment'),   # /equipment/にequipmentビューを割り当て
    path('rental/', views.rental, name='rental'),   # /rental/にrentalビューを割り当て
    path('oatmeal/',views.oatmeal, name='oatmeal'),  # /oatmeal/にoatmealビューを割り当て
    path('smoothie/',views.smoothie, name='smoothie'),  # /smoothie/にsmoothieビューを割り当て
]
