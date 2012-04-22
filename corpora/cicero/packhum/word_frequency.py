#!/usr/bin/env python
# -*- coding: utf-8 -*-
# caio begotti <caio1982@gmail.com>
# this is under public domain

from nltk import Text
from nltk import FreqDist

from nltk.tokenize import word_tokenize
from nltk.corpus import cicero

from CatXMLReader import CategorizedXMLCorpusReader

fileids = cicero.abspaths()
reader = CategorizedXMLCorpusReader('/', fileids, cat_file='categories.txt')
tokens = Text(reader.words(fileids))
dist = FreqDist(tokens)
print dist.tabulate()
