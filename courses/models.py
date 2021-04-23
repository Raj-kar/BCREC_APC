from django.db import models

# Create your models here.

class Course(models.Model):
    slug = models.CharField(max_length=50, default="", primary_key=True)
    title = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="courses/images", default="")
    description = models.CharField(max_length=100, default="")
    yearsOfCourse = models.IntegerField(default=3)
    pdfs = models.FileField(upload_to="pdfs", default="")

    def __str__(self):
        return self.description
