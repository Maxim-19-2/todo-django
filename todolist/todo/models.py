from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=160)
    date = models.CharField(max_length=100, default='10. Mai 2022')
    progress = models.IntegerField(default='50')

    def _str_(self):
        return self.title + self.date + str(self.progress)