import os
from config.settings import PHOTOALBUM_BASE_DIR, PHOTOALBUM_REWRITE
from django.views.generic.base import TemplateView

class PhotosView(TemplateView):

    template_name = 'pages/photos.html'

    def get_context_data(self, **kwargs):
        context = super(PhotosView, self).get_context_data(**kwargs)
        photo_dirs = os.listdir(PHOTOALBUM_BASE_DIR)
        context['photo_dirs'] = photo_dirs
        return context

class PhotosDirView(TemplateView):

    template_name = 'pages/photos_dir.html'

    def get_context_data(self, **kwargs):
        context = super(PhotosDirView, self).get_context_data(**kwargs)
        photo_filenames = os.listdir(os.path.join(PHOTOALBUM_BASE_DIR,
                                                  context['photo_dir']))
        photo_dir = context['photo_dir']
        photos = [create_photo(photo_dir, filename) for filename in
                photo_filenames if 'thumb' not in filename]
        context['photos'] = photos
        return context

class Photo:
    def __init__(self, thumb_path, image_path):
        self.thumb_path = thumb_path
        self.image_path = image_path

def create_photo(photo_dir, filename):
    pieces = os.path.splitext(filename)
    thumb_file = pieces[0] + '.thumb' + pieces[1]
    return Photo(os.path.join(PHOTOALBUM_REWRITE, photo_dir, thumb_file),
                 os.path.join(PHOTOALBUM_REWRITE, photo_dir, filename))
