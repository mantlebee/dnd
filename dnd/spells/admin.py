from django.contrib import admin
from . import models


@admin.register(models.CastingTime)
class CastingTimeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Component)
class ComponentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Duration)
class DurationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Range)
class RangeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Spell)
class SpellAdmin(admin.ModelAdmin):
    pass