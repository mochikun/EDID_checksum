###Copyright (c) 2013 Kenta Ueda
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

from struct import *
import sys
import os

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
    print("please input edid binary file path for argument")
    quit()

size = os.path.getsize(argvs[1])
if size >= 127:
    f = open(argvs[1],'rb')
    sum = 0
    for i in range(127):
        tmp = unpack('B',f.read(1))[0]
    #	print('read:%d' % tmp)
        sum = sum + tmp

    m = 256 - (sum % 256)
    print('Calced: %x' % m)
    if size >= 128:
        csum = unpack('B',f.read(1))[0]
        print('Actual: %x' % csum)
        if (csum == m):
            print('Match!')
        else:
            print('Un-match...')
else:
    print("Please input binary size > 127 Bytes")
