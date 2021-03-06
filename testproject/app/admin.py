from django.contrib import admin
from models import Normal, SimpleRelated
from nani.admin import TranslatableAdmin, TranslatableTabularInline

class SimpleRelatedInline(TranslatableTabularInline):
    model = SimpleRelated

class NormalAdmin(TranslatableAdmin):
    inlines = [SimpleRelatedInline,]

admin.site.register(Normal, NormalAdmin)
admin.site.register(SimpleRelated, TranslatableAdmin)