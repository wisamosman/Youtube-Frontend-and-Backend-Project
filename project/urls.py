"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from viedeos.views import post_list , post_detail , new_post , edit_post , VideoList , VideoDetail , VideoCreate , VideoDelete , VideoEdit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    #path('viedeos/' , post_list),
    #path('viedeos/new' , new_post),
    #path('viedeos/<int:video_id>' , post_detail),
    #path('viedeos/<int:video_id>/edit' , edit_post),
    path('viedeos/' , VideoList.as_view()),
    path('viedeos/new' , VideoCreate.as_view()),
    path('viedeos/<int:pk>' , VideoDetail.as_view()),
    path('viedeos/<int:pk>/edit' , VideoEdit.as_view()),
    path('viedeos/<int:pk>/delete' , VideoDelete.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
