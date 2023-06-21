from django.db import models

# Create your models here.
class file(models.Model):
    file = models.FileField(upload_to='css',null=True,blank=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)