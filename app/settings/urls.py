from django.contrib import admin
from django.urls import path

from currency.views import contact_us_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactus/', contact_us_list)
]
