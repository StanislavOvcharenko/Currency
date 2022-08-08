from django.contrib import admin
from django.urls import path

from currency.views import contact_us_table, rate_table, contact_us_list, source, index, rate_list, rate_create,\
    rate_update, rate_details, rate_delete, source_create, source_update, source_details, source_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactus/table/', contact_us_table),
    path('rate/table/', rate_table),
    path('contactus/', contact_us_list),
    path('source/list/', source),
    path('', index),
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:rate_id>/', rate_update),
    path('rate/details/<int:rate_id>/', rate_details),
    path('rate/delete/<int:rate_id>/', rate_delete),
    path('source/create/', source_create),
    path('source/update/<int:source_id>/', source_update),
    path('source/details/<int:source_id>/', source_details),
    path('source/delete/<int:source_id>/', source_delete)
]
