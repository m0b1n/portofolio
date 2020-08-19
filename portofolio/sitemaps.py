from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from icc.models import News, Category


class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return News.objects.all()

    def location(self, obj):
        return "/news/" + str(obj.id)

    @staticmethod
    def lastmod(obj):
        return obj.pub_date


class AboutUsViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return ['about']

    def location(self, obj):
        return "/aboutus"


class CatsViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return ['all_cats']

    def location(self, obj):
        return "/categories"


class AllCatsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return "/categories/" + str(obj.title_en)
