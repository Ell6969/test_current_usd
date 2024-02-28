from django.urls import path
from .views import get_current_rate

app_name = "usd"

urlpatterns = [
    path("", get_current_rate, name='get-current-rate'),
]