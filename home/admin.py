from django.contrib import admin

from home.models import MultiSite


@admin.register(MultiSite)
class MultiSiteAdmin(admin.ModelAdmin):

    list_display = ["site", "background_color"]
