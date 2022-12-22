from django.db import models


class PhotoCategory(models.Model):
    name = models.CharField(max_length=100)
    category_image = models.ImageField()

    def __str__(self):
        return self.name


class PhotoSets(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    category = models.ForeignKey(PhotoCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']