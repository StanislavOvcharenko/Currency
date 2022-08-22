from django.contrib import admin
from django.urls import path, include
from currency import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view()),
    path('silk/', include('silk.urls', namespace='silk')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('currency/', include('currency.urls')),


]
