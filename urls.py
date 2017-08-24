from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf.urls.static import static
from django.conf import settings
from pavelstanlley.sitemaps import PavelSitemap
sitemaps= {'pavelsitemap': PavelSitemap()}
urlpatterns =[
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

