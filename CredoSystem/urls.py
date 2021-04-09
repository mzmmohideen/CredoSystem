"""CredoSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import index, LoginCheck, LoginView #ApiLoginView
# from CredoSystem.settings import STATIC_URL, STATIC_ROOT
# from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from CourseApp.views import CourseView, UserReg
from CourseApp.urls import CourseRouter

urlpatterns = [
    path('login/', LoginView),
    path('login_check/', LoginCheck),
    path('admin/', admin.site.urls),
    path('api/', include(CourseRouter.urls)),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('courses/', CourseView),
    path('user_reg/', UserReg, name='reg'),
    path('', index, name='home'),    
    # DRF URLS
    # path('api/login/', ApiLoginView),
    path('api-auth/', include('rest_framework.urls')),
    # path('user_reg/', UserRegForm)
]

# urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

