from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
  name = models.CharField(max_length=150)

  def __str__(self):
    return self.name


class Article(models.Model):
  title = models.CharField(max_length=150)
  date_posted = models.DateTimeField(default=timezone.now)
  description = models.TextField()
  link = models.CharField(max_length=150)
  category = models.ManyToManyField(Category)
  channel = models.CharField(max_length=100, default="channel")

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})
