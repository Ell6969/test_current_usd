from django.db import models


class Rate(models.Model):

    usd_rate = models.FloatField(default=0.00)
    date_time = models.DateTimeField(auto_now_add=True)
    errors = models.CharField(max_length=155, blank=True, default='ALL OK')
