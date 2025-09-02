from django.db import models


class BlogPost(models.Model):
    title = models.CharField(verbose_name='სათაური', max_length=255)
    text = models.TextField(verbose_name='ტექსტი')

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title
