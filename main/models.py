from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    psevdonim = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.psevdonim if self.psevdonim \
            else f'{self.first_name} {self.last_name}'

    def get_all(self):
        return self.id, self.first_name, self.last_name, self.psevdonim

    class Meta:
        verbose_name = 'Музыкант'
        verbose_name_plural = 'Музыканты'


class Song(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Musician,
                               on_delete=models.SET('Deleted'),
                               related_name='songs')
    feat = models.ForeignKey(Musician, null=True, blank=True,
                             on_delete=models.SET_NULL,
                             related_name='feats')
    poster = models.ImageField(upload_to='images', blank=True)
    date = models.DateField()

    def __str__(self):
        if self.feat:
            return f'{self.author} - {self.title} ft. {self.feat}'
        return f'{self.author} - {self.title}'

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Песни'


class Award(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
    year = models.DateField()

    def __str__(self):
        return f'{self.song} - Award {self.year}'

