#!/usr/bin/env python

from __future__ import division
from sstv import SSTV, byte_to_freq


class GrayscaleSSTV(SSTV):

    def gen_image_tuples(self):
        for line in xrange(self.HEIGHT):
            for item in self.horizontal_sync():
                yield item
            for item in self.encode_line(line):
                yield item

    def encode_line(self, line):
        msec_pixel = self.SCAN / self.WIDTH
        image = self.image.load()
        pixlen = len(image[0, line])
        for col in xrange(self.WIDTH):
            pixel = image[col, line]
            freq_pixel = byte_to_freq(sum(pixel) / pixlen)
            yield freq_pixel, msec_pixel


class Robot8BW(GrayscaleSSTV):
    VIS_CODE = 0x02
    WIDTH = 160
    HEIGHT = 120
    SYNC = 7
    SCAN = 60


class Robot24BW(GrayscaleSSTV):
    VIS_CODE = 0x0A
    WIDTH = 320
    HEIGHT = 240
    SYNC = 12
    SCAN = 93

MODES = (Robot8BW, Robot24BW)
