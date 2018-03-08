'''
Grant Tremblay's (very) slight modification of code by Jeremy Sanders
'''

import sys
import os
import argparse

from astropy.io import fits
import scipy.ndimage
import numpy as np

def run(infile, outfile, scale):
    f = fits.open(infile)
    img = f[0].data

    # convert to float if required
    if issubclass(img.dtype.type, np.integer):
        img = img.astype(np.float32)

    proc = scipy.ndimage.gaussian_gradient_magnitude(img, scale)

    f[0].data = proc

    try:
        os.unlink(outfile)
    except OSError:
        pass

    f.writeto(outfile)

def main():
    parser = argparse.ArgumentParser(
        description="Gaussian gradient magnitude")
    parser.add_argument('inimage', help='input image')
    parser.add_argument('outimage', help='output image')
    parser.add_argument('scale', type=float, help='gaussian sigma (pixels)')
    args = parser.parse_args()

    run(args.inimage, args.outimage, args.scale)

if __name__ == '__main__':
    main()
