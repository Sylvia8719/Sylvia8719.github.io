from django.contrib import admin
from django.urls import include, path
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('displayname/',include('displayname.urls')),
    path('calc/',include('calc.urls'))
]
