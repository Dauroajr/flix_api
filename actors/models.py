from django.db import models

import pycountry


NATIONALITY_CHOICES = [
    (country.alpha_3, country.name) for country in pycountry.countries
]


class Actor(models.Model):

    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', 'name', 'nationality',)
