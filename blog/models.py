from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/', blank=True)
    published_date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def summary(self):
        return self.content[:100] + "..."

    def pub_date(self):
        return self.published_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
