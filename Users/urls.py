from django.urls import path
from django.conf.urls import url

from Users import views


urlpatterns = [
    #path('register/', views.RegistrationView.as_view(), name="register"),
    #path('username-validtion/', views.UsenameValidationView.as_view(), name="username-validation"),
    url(r'^$', views.home, name='home'),
    #url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
