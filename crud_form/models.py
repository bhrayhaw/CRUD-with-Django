from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length=254)
    instrument = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class AlbumModel(models.Model):
    artist = models.ForeignKey(MusicianModel, on_delete = models.CASCADE)
    album_name = models.CharField(max_length = 40)
    release_date = models.DateField()

    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Good"),
        (4, "Excellent")
    )

    number_stars = models.IntegerField(choices = rating)
    def __str__(self) -> str:
        return self.album_name + " " + str(self.number_stars)