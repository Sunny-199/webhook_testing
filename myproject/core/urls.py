from django.urls import path
from myproject.core.views import Index

app_name = 'core'

urlpatterns = [
    path('webhook/', Index.as_view(), name='index'),
]
