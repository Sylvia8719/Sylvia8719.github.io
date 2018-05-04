from django.urls import path

from . import views as dis_view

urlpatterns = [
    path('<str:a>',dis_view.displayname , name='displayname')
]
