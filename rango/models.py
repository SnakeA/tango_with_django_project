from django.db import models

class Category (models.Model):
    name = models.CharField(max_length=128, unique=True)

    #method is therefore used to provide a unicode representation of a model instance
    def __unicode__(self):
        return self.name


class Page(models.Model):
    category=models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

# Whenever you add to existing database models, you will have to delete the database
# file and then re-sync the database by running python manage.py syncb again.