from django.db import models


class City(models.Model):
    """
    Represents a Person's City in the system
    Example: Lisboa, Porto
    """

    city_id = models.AutoField(primary_key=True)        #: ID
    city_name = models.CharField('Name', max_length=70) #: Name

    class Meta:
        ordering = ['city_name',]
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city_name
