
from django.urls import path

from shared.views import home_page_view

app_name = 'shared'

urlpatterns = [
    path('', home_page_view, name='home')
]
