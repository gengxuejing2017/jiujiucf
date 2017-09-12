#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(1, 10):
    for j in range(1, i + 1):
        m = j * i
        print '%d x %d = %d' % (j, i, m),
    print '\n'