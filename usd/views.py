from django.http import JsonResponse

from usd.models import Rate


def get_current_rate(request):
    last_rate = Rate.objects.order_by('-date_time')[:10]

    serialized_last_rate = [
        {
            'usd_rate': req.usd_rate, 'date_time': req.date_time
        } for req in last_rate
    ]
    return JsonResponse({
        'last 10 request usd rate': serialized_last_rate,
    })
