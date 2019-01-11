#!/usr/bin/env python
import sys
import csv
import re
i = 0
for line in sys.stdin:
    i = i + 1
    if i != "DATE":
            line = re.sub(r'".*"','',line)
            words = line.split(',')

            for word in words:
                word = word.strip()
                if word:
                        if i >= 25:
                                print '%s\t%s' %(word,1)
