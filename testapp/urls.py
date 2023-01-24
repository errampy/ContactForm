from django.urls import path
from testapp import views
urlpatterns=[
    path('contact-us/',views.contact_us,name='contact_us'),
    path('verification/',views.verification, name='verification'),
    path('success/',views.success,name='success'),
]