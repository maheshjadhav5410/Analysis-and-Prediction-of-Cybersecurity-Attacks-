# cyberthreat\cyberthreat\urls.py

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from analysis import views as analysis_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', analysis_views.home_redirect, name='home_redirect'),  # Redirect based on authentication
    path('signup/', analysis_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='analysis/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='analysis/logout.html'), name='logout'),
    path('analysis/', include('analysis.urls')),
]
