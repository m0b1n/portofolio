from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    createDate = models.DateTimeField(null=False, default=now)
    deleteDate = models.DateTimeField(null=True, blank=True)
    isDeleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return "{}, {}, {}".format(self.createDate, self.deleteDate, self.isDeleted)


class LandingPage(BaseModel):
    shortDesc = models.TextField(max_length=500, default=None, null=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True,
                            default=None, width_field=1920, height_field=1080)


class SkillCat(BaseModel):
    name = models.CharField(default=None, null=True)


class Skill(BaseModel):
    name = models.CharField(default=None, null=True)
    rate = models.IntegerField(default=None, null=True, max_length=100)
    icon = models.CharField(default=None, null=True)
    SkillCatFK = models.ForeignKey(SkillCat, on_delete=models.CASCADE)


class Education(BaseModel):
    title = models.CharField(default=None, null=True)
    shortDesc = models.TextField(default=None, null=True)
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)


class Experience(BaseModel):
    title = models.CharField(default=None, null=True)
    shortDesc = models.TextField(default=None, null=True)
    longDesc = models.TextField(default=None, null=True)
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    usedTech = models.TextField(null=True, blank=True)
    companyLogo = models.ImageField(upload_to='images/', null=True, blank=True,
                                    default=None, width_field=200, height_field=200)


class BlogCat(BaseModel):
    title = models.CharField(default=None, null=True)


class Blog(BaseModel):
    title = models.CharField(default=None, null=True)
    blogReadingTime = models.IntegerField(default=None, null=True)
    body = models.TextField(default=None, null=True)
    tags = models.TextField(null=True, blank=True)
    BlogCatFK = models.ForeignKey(BlogCat, on_delete=models.CASCADE)


class Gallery(BaseModel):
    legend = models.CharField(default=None, null=True)
    imgThumbnail = models.ImageField(upload_to='images/', null=True, blank=True,
                                     default=None, width_field=200, height_field=200)
    img = models.ImageField(upload_to='images/', null=True, blank=True,
                            default=None)
