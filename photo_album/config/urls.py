# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^photos/$',
        TemplateView.as_view(template_name='pages/photos.html'),
        name="photos"),
    url(r'^videos/$',
        TemplateView.as_view(template_name='pages/videos.html'),
        name="videos"),

    # Your stuff: custom urls go here

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
