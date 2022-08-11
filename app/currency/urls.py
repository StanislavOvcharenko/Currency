from django.urls import path
from currency.views import contact_us_table, rate_table, contact_us_list
from currency import views

app_name = 'currency'

urlpatterns = [
    path('contactus/table/', contact_us_table),
    path('rate/table/', rate_table),
    path('contactus/', contact_us_list),
    path('rate/list/', views.RateListView.as_view(), name='rate_list'),
    path('rate/create/', views.RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', views.RateUpdateView.as_view(), name='rate_update'),
    path('rate/delete/<int:pk>/', views.RateDeleteView.as_view(), name='rate_delete'),
    path('rate/details/<int:pk>/', views.RateDetailsView.as_view(), name='rate_details'),
    path('source/list/', views.SourceListView.as_view(), name='source_list'),
    path('source/create/', views.SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', views.SourceUpdateView.as_view(), name='source_update'),
    path('source/details/<int:pk>/', views.SourceDetailsView.as_view(), name='source_details'),
    path('source/delete/<int:pk>/', views.SourceDeleteView.as_view(), name='source_delete'),



]
