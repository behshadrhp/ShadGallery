from django.db import models
from django.contrib.sites.models import Site


class MultiSite(models.Model):
    """
    Set Custom config --> multi website,
    """
    
    # initial fields
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return self.site.name
