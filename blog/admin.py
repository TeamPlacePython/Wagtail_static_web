from django.contrib import admin

from . import models

admin.site.register(models.BlogPageCategories)
admin.site.register(models.BlogIndexPage)
admin.site.register(models.BlogPage)


@admin.register(models.BlogSubscriber)
class BlogSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
