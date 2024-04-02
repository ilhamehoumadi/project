from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    #path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('signup',views.signup, name='signup'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('association',views.association, name='account_association'),

    #path('about',views.about, name='about'),

]
