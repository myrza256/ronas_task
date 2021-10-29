from django.db import models
from django.utils.translation import ugettext_lazy as _


class TrackableDate(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
        
    class Meta:
        abstract = True


class Weather(TrackableDate):
    city = models.CharField(max_length=255)
    main = models.CharField(_('main'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    temp_c = models.FloatField(_('temp_c'), default=0)
    temp_f = models.FloatField(_('temp_f'), default=0)
    humidity = models.PositiveIntegerField(_('humidity'), default=0)
    wind_speed = models.PositiveIntegerField(_('wind speed'), default=0)
    wind_deg = models.IntegerField(_('wind degree'), default=0)

    class Meta:
        verbose_name = _('weather')
        verbose_name_plural = _('weather')

    def __str__(self):
        return '[{}] {}'.format(self.pk, self.main)

