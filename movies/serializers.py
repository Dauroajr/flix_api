from django.db.models import Avg
from rest_framework import serializers

from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
# from genres.models import Genre
# from actors.models import Actor


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1920:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1920')
        return value

    def validate_summary(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O campo "Summary" não pode ter mais que 200 caracteres')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):

    cast = ActorSerializer(many=True)
    genre = GenreSerializer()
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'genre',
            'cast',
            'release_date',
            'rating',
            'summary',
        ]

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rating:
            return round(rating, 1)
        return None


# Formato de Serializer genérico:

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset = Genre.objects.all(),
#     )
#     release_date = serializers.DateField()
#     cast = serializers.PrimaryKeyRelatedField(
#         queryset = Actor.objects.all(),
#         many = True,
#     )
#     summary = serializers.CharField()


# The code below returns the same result as the block of code before
# 1st function in MovieModelSerializer, except it's "hard code" written.

        # reviews = obj.reviews.all()
        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()
        #     reviews_mean = sum_reviews / reviews_count

        #     return round(reviews_mean, 1)
        # return None
