from django.db import models
from django.utils.timezone import now
from .base_model import BaseModel

class LandingPage(BaseModel):
    shortDesc = models.TextField(max_length=500, default=None, null=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True,
                            default=None, width_field=1920, height_field=1080)


class SkillCat(BaseModel):
    name = models.CharField(default=None, null=True, max_length=500)


class Skill(BaseModel):
    name = models.CharField(default=None, null=True, max_length=500)
    rate = models.IntegerField(default=None, null=True)
    icon = models.CharField(default=None, null=True, max_length=500)
    SkillCatFK = models.ForeignKey(SkillCat, on_delete=models.CASCADE)


class Education(BaseModel):
    title = models.CharField(default=None, null=True, max_length=500)
    shortDesc = models.TextField(default=None, null=True)
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)


class Experience(BaseModel):
    title = models.CharField(default=None, null=True, max_length=500)
    shortDesc = models.TextField(default=None, null=True)
    longDesc = models.TextField(default=None, null=True)
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    usedTech = models.TextField(null=True, blank=True)
    companyLogo = models.ImageField(upload_to='images/', null=True, blank=True,
                                    default=None, width_field=200, height_field=200)


class BlogCat(BaseModel):
    title = models.CharField(default=None, null=True, max_length=500)


class Blog(BaseModel):
    title = models.TextField(default=None, null=True)
    blogReadingTime = models.IntegerField(default=None, null=True)
    body = models.TextField(default=None, null=True)
    tags = models.TextField(null=True, blank=True)
    BlogCatFK = models.ForeignKey(BlogCat, on_delete=models.CASCADE)


class Gallery(BaseModel):
    legend = models.CharField(default=None, null=True, max_length=500)
    imgThumbnail = models.ImageField(upload_to='images/', null=True, blank=True,
                                     default=None, width_field=200, height_field=200)
    img = models.ImageField(upload_to='images/', null=True, blank=True,
                            default=None)
