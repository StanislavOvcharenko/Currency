from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views


app_name = 'api'

router = DefaultRouter()
router.register('rates', views.RatesViewSet, basename='rate')

urlpatterns = [
    # path('rates/', views.RatesView.as_view(), name='rates'),
    # path('rates/<int:pk>/', views.RateDetails.as_view(), name='rate-details'),
    path('sources/', views.SourcesView.as_view(), name='sources'),
    path('contactus/create/', views.ContactUsCreateView.as_view(), name='contactuscreate'),
    path('contactus/<int:pk>/', views.ContactUsDetails.as_view(), name='contactus'),
    path('contactus/list/', views.ContactUsList.as_view(), name='contactuslist')
]

urlpatterns += router.urls
