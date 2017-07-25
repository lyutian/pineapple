from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    abstract = models.TextField(blank = True, null = True)
    content = RichTextField()
  
    def __str__(self):
        return self.title
  
    class Meta:
        ordering = ['-date_time']

