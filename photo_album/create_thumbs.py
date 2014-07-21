import os, sys
from PIL import Image

size = (128, 128)

for infile in os.listdir(sys.argv[1]):
    inpath = os.path.join(sys.argv[1], infile)
    pieces = os.path.splitext(inpath)
    outpath = pieces[0] + ".thumb" + pieces[1]
    if inpath != outpath and not os.path.exists(outpath):
        try:
            im = Image.open(inpath)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outpath, 'JPEG')
        except IOError as ex:
            print('cannot create thumbnail for ' + infile + ' -- ' + ex.strerror)
