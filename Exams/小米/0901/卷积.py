#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re
import numpy as np

# 5 5, 1 1 1 1 1 1 2 2 2 1 1 2 4 2 1 1 2 2 2 1 1 1 1 1 1
# 5 5, 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 2


class Solution:
    def padding(self, image, hei, wid):
        h, w = image.size()
        out = None
        out = np.zeros((h+2*hei, w+2*wid))
        out[hei:hei+h, wid:wid+w] = image
        return out

    def conv2d(self, kernel, image, stride):
        # Write Code Here
        kernel = kernel.split(', ')
        ksize = kernel[0].split(' ')
        kernel = kernel[1].split(' ')

        image = image.split(', ')
        isize = image[0].split(' ')
        image = image[1].split(' ')

        tmp=np.zeros((isize[0],isize[1]))
        for i in range(isize[0]):
            tmp[i]=image[i*isize[1]:(i+1)*isize[1]]
        image=tmp
        self.padding(image,stride,stride)
        out=np.zeros((isize[0],isize[1]))


try:
    _kernel = input()
except:
    _kernel = None

try:
    _image = input()
except:
    _image = None

_stride = int(input())


s = Solution()
res = s.conv2d(_kernel, _image, _stride)

print(res + "\n")
