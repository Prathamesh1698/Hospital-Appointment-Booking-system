from django.urls import path
from app import views

urlpatterns = [

    path('index', views.index),
    path('footer', views.footer),
    path('header', views.header),
    path('base', views.base),
    path('apt', views.apt),
    path('about', views.about),
    path('contact', views.contact),
    path('services', views.services),
    path('dept', views.dept),
    path('edit/<rid>', views.edit),
    path('delete/<rid>', views.delete),
    path('docfilter/<value>', views.docfilter),
    path('dform', views.djangoform),
    path('dmodelform', views.djangomodelform),
    path('register', views.user_register),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('setcookies', views.setcookie),
    path('getcookies', views.getcookie),
    path('setsession', views.setsession),
    path('getsession', views.getsession),
]
