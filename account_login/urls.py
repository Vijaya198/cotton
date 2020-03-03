from django.urls import path, include
from django.conf.urls import url

from .forms import EmailValidationOnForgotPassword
from . import views
from .views import SignUpView, ActivateAccount
from .forms import EmailValidationOnForgotPassword
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', views.home, name='home'),
    path('', views.user_login, name='user_login'),

    path('success', views.user_success, name='user_success'),
    path('user_details', views.user_details, name='user_details'),
    path('account/logout', views.user_logout, name='user_logout'),
    # path('logout',views.user_logout,name='user_logout'),
    # path('signup',views.user_signup,name='user_signup'),
    path('signup/', SignUpView.as_view()),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

    path('register', views.user_register, name='user_register'),
    path('profile', views.user_profile, name='user_profile'),

    path('password_reset/',
       PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name = 'registration/password_reset_email.html', form_class= EmailValidationOnForgotPassword ),
       name="password_reset")


]