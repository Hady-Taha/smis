from django.db import models
from django.contrib.auth.models import User
from news.utlis import slugify
# Create your models here.


class Department (models.Model):
    title   = models.CharField(max_length=150)
    slug    = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_professor(self):
        return self.professor_set.all()

class Professor(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName   = models.CharField(max_length=50, blank=True, null=True)
    photo      = models.ImageField(upload_to='professorPhoto', default='user.png')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    bio        = models.TextField(max_length=200, blank=True, null=True)
    slug       = models.SlugField(blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True)
    created    = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.user))
        super(Professor, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)
