from django.db import models


class Country(models.Model):
    """
    Represents a Person's country in the system
    Example: Israel, Brazil
    """
    country_id = models.AutoField(primary_key=True)         #: ID
    country_name = models.CharField('Name', max_length=70)  #: Name
    country_code = models.CharField('ISO Code', max_length=10, blank=True, null=True)  #: ISO Code

    class Meta:
        ordering = ['country_name',]
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        app_label = 'common'

    def __str__(self):
        return self.country_name
