from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from .models.models import Blog


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return "/Blog/" + str(obj.id)

    @staticmethod
    def lastmod(obj):
        return obj.pub_date

