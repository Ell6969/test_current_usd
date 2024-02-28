
import requests
from celery import shared_task

from usd.models import Rate

API_KEY = 'a7479e37bf913d9385a96d94'
URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'


@shared_task(name='get_usd')
def get_usd():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        usd_rate = data['conversion_rates']['RUB']
        Rate.objects.create(usd_rate=usd_rate)
    else:
        Rate.objects.create(errors='Не удалось получить курс доллара')
