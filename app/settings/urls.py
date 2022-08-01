from django.contrib import admin
from django.urls import path

from currency.views import contact_us_table, rate_table, contact_us_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactus/table/', contact_us_table),
    path('rate/table/', rate_table),
    path('contactus/', contact_us_list),
]
