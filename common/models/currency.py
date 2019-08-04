from django.db import models


class Currency(models.Model):
    """
    Represents a Person's salry Currency in the system
    Example: Euro, Dolar
    """
    
    currency_id = models.AutoField(primary_key=True)        #: ID
    currency_name = models.CharField('Name', max_length=70) #: Name
    currency_symbol = models.CharField('Symbol', max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['currency_name',]
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return self.currency_name
