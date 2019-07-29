import warnings

from django.db import models
from django.utils.translation import ugettext_lazy as _


class PizzaType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "pizza_types"

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    pizza_type = models.ForeignKey(PizzaType, on_delete=models.CASCADE)


class Transactions(models.Model):
    price = models.DecimalField(max_digits=13, decimal_places=2)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
