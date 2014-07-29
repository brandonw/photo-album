import os, sys
from PIL import Image, ExifTags

size = (128, 128)

for infile in os.listdir(sys.argv[1]):
    inpath = os.path.join(sys.argv[1], infile)
    pieces = os.path.splitext(inpath)
    outpath = pieces[0] + ".thumb" + pieces[1]
    if (inpath != outpath and not os.path.exists(outpath) and
        'thumb' not in infile):
        try:
            image = Image.open(inpath)
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break

            e = image._getexif()
            if e is not None:
                exif = dict(e.items())
                if orientation in exif:
                    if exif[orientation] == 3:
                        image=image.transpose(Image.ROTATE_180)
                    elif exif[orientation] == 6:
                        image = image.transpose(Image.ROTATE_270)
                    elif exif[orientation] == 8:
                        image = image.transpose(Image.ROTATE_90)

            image.save(inpath)
            image.thumbnail(size, Image.ANTIALIAS)
            image.save(outpath, 'JPEG')
        except IOError as ex:
            print('cannot create thumbnail for ' + infile + ' -- ' + ex.strerror)
