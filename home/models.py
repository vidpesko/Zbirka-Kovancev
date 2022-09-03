from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    pass
    # user = models.ForeignKey(User)
    # name = models.CharField(max_length=50)
    # release_date
    # country
    # value
    # collection
    # unit
    # item_type
    # description