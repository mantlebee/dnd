from django.db import models


# Create your models here.
class CastingTime(models.Model):
    name = models.CharField(max_length=100)


class Component(models.Model):
    name = models.CharField(max_length=100)


class Duration(models.Model):
    name = models.CharField(max_length=100)


class Range(models.Model):
    name = models.CharField(max_length=100)


class School(models.Model):
    name = models.CharField(max_length=100)


class Spell(models.Model):
    casting_time = models.ForeignKey(CastingTime, on_delete=models.CASCADE)
    components = models.ManyToManyField(Component)
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE)
    level = models.IntegerField()
    name = models.CharField(max_length=100)
    range = models.ForeignKey(Range, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
