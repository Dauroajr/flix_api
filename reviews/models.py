from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from movies.models import Movie


class Review(models.Model):

    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Can't be less than 0 (zero) stars."),
            MaxValueValidator(5, "Can't be greater than 5 (five) stars.")
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie
