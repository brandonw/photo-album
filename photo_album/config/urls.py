# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

import views

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^photos/$',
        views.PhotosView.as_view(),
        name="photos"),
    url(r'^photos/(?P<photo_dir>[^/]*)$',
        views.PhotosDirView.as_view(),
        name="photos_dir"),
    url(r'^photos/(?P<photo_dir>[^/]*)/(?P<photo_file>[^/]*)$',
        views.PhotoView.as_view(),
        name="photo"),
    url(r'^videos/$',
        TemplateView.as_view(template_name='pages/videos.html'),
        name="videos"),
    url(r'^videos/([^/]*)$',
        TemplateView.as_view(template_name='pages/videos_dir.html'),
        name="videos_dir"),
    #url(r'^videos/([^/]*)/([^/]*)$',
        #TemplateView.as_view(template_name='pages/video.html'),
        #name="video"),

    # Your stuff: custom urls go here

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
