from django.db import models
from .utlis import cover_directory_path
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class News(models.Model):
    title   = models.CharField(max_length=100)
    cover   = models.ImageField(upload_to=cover_directory_path)
    body    = RichTextUploadingField()
    ad      = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def save(self, *args, **kwargs):
        if self.pk:
            this_record = News.objects.get(id=self.id)
            if this_record.cover != self.cover:
                this_record.cover.delete(save=False)
        super(News, self).save(*args, **kwargs)
