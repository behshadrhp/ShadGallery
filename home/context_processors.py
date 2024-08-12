from django.contrib.sites.shortcuts import get_current_site
from home.models import MultiSite  


def site_info(request):
    current_site = get_current_site(request)
    try:
        site_settings = MultiSite.objects.get(site=current_site)
    except MultiSite.DoesNotExist:
        site_settings = None

    return {
        'background_color': site_settings.background_color if site_settings else '#FFFFFF',
        'site_name': site_settings.site if site_settings else 'Default Site Name',
    }
