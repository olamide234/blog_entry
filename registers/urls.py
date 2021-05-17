from django.urls import path
from registers import views

urlpatterns=[
    path('register/', views.register_view, name='register_user'),
    path('login/', views.login_view, name='login_user'),
    path('logout/', views.logout_view, name='logout_user'),
]