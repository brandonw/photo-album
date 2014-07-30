import os
from config.settings import PHOTOALBUM_BASE_DIR, PHOTOALBUM_REWRITE
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
    context_object_name = 'photos'
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
        context['start'] = 1
        context['end'] = 35
        context['total'] = len(self.photos)
        context['photo_dir'] = self.photo_dir
        return context

class Photo:
    def __init__(self, thumb_path, image_path):
        self.thumb_path = thumb_path
        self.image_path = image_path

def create_photo(photo_dir, filename):
    pieces = os.path.splitext(filename)
    thumb_file = pieces[0] + '.thumb' + pieces[1]
    name = filename
    return Photo(os.path.join(PHOTOALBUM_REWRITE, photo_dir, thumb_file),
                 os.path.join(PHOTOALBUM_REWRITE, photo_dir, filename))
