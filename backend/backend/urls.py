from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # user
    path('api/user/', include('user.urls')),

    # employee
    path('api/employee/', include('employee.urls')),

    # manager
    path('api/manager/', include('manager.urls')),

    # rnd
    path('api/rnd/', include('developer.urls')),

    # admin
    path('admin/', admin.site.urls),
]
