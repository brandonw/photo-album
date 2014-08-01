import os
from config.settings import PHOTOALBUM_BASE_DIR, PHOTOALBUM_REWRITE
from django.views.generic.base import TemplateView
from django.views.generic import ListView

class PhotosView(ListView):

    template_name = 'pages/photos.html'
    context_object_name = 'photo_dirs'

    def get_queryset(self):
        photo_dirs = os.listdir(PHOTOALBUM_BASE_DIR)
        photo_dirs.sort()
        return photo_dirs

class PhotosDirView(ListView):

    template_name = 'pages/photos_dir.html'
    paginate_by = 35

    def get_queryset(self):
        self.photo_dir = self.kwargs['photo_dir']
        photo_filenames = os.listdir(os.path.join(PHOTOALBUM_BASE_DIR,
                                                  self.photo_dir))
        photo_filenames.sort()
        self.photos = [create_photo(self.photo_dir, filename) for filename in
                       photo_filenames if 'thumb' not in filename]
        return self.photos

    def get_context_data(self, **kwargs):
        context = super(PhotosDirView, self).get_context_data(**kwargs)
        context['photo_dir'] = self.photo_dir
        return context

class PhotoView(TemplateView):

    template_name = 'pages/photo.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        # has_previous, previous_link (just image file name)
        # has_next, next_link (just image file name)
        context['photo_dir'] = kwargs['photo_dir']
        context['photo_file'] = kwargs['photo_file']
        context['photo_path'] = os.path.join(PHOTOALBUM_REWRITE,
                                             context['photo_dir'],
                                             context['photo_file'])
        return context

class Photo:
    def __init__(self, name, thumb_path):
        self.name = name
        self.thumb_path = thumb_path

def create_photo(photo_dir, filename):
    pieces = os.path.splitext(filename)
    thumb_file = pieces[0] + '.thumb' + pieces[1]
    return Photo(filename, os.path.join(PHOTOALBUM_REWRITE,
                                        photo_dir, thumb_file))
