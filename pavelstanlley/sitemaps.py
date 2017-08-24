from django.contrib.sitemaps import Sitemap
from .models import Post, Projects
class PavelSitemap(Sitemap):
     changefreq = "weekly"
     priority= 0.5
     def Post(self):
        return Post.objects.all()

