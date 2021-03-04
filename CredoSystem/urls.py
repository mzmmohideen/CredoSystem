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
from .views import index
# from CredoSystem.settings import STATIC_URL, STATIC_ROOT
# from django.conf.urls.static import static
from CourseApp.views import CourseView, UserReg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', CourseView),
    path('user_reg/', UserReg),
    # path('user_reg/', UserRegForm)
    # path('', index)
]

# urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

