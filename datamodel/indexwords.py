#!/usr/bin/env python

import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp :
    for line_no, line in enumerate(fp, 1) :
        for match in WORD_RE.finditer(line) :
            word = match.group()
            col = match.start() + 1
            loc = (line_no, col)

            occurences = index.get(word, [])
            occurences.append(loc)
            index[word] = occurences

for word in sorted(index, key=str.upper) :
    print (word, index[word])
