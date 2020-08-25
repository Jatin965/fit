from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('methods/', views.MethodView.as_view(), name='methods'),
    path('about/', views.AboutView.as_view(), name='abt'),
]
