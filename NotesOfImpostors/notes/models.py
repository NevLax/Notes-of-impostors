from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=80)
    main = models.TextField()
    likes = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title