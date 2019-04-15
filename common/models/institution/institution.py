from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=200, unique=True)
    short_name = models.CharField(max_length=10, blank=True)
    people = models.ManyToManyField(
        to='humanresources.Person',
        through='InstitutionAffiliation',
        related_name='institutions',
    )

    class Meta:
        ordering = ('name', )
        app_label = 'common'

    def __str__(self):
        return self.name

