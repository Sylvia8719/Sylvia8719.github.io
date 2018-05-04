from django.urls import path

from . import views as calc_views

urlpatterns = [
    path('add/<int:a>/<int:b>/<int:c>', calc_views.add, name='add'),
    path('product/<int:a>/<int:b>/<int:c>', calc_views.product, name='product'),
    path('minus/<int:a>/<int:b>/<int:c>', calc_views.minus, name='minus'),
    path('divide/<int:a>/<int:b>/<int:c>', calc_views.divide, name='divide'),
    path('',calc_views.calc,name='calc')
]
