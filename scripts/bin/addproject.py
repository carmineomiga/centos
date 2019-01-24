#!/usr/bin/env python
import sys
import os

p = "project"
name = sys.argv[1]

os.makedirs("/%s/%s/asset/char" % (p, name))
os.makedirs("/%s/%s/asset/shader" % (p, name))
os.makedirs("/%s/%s/config/ocio" % (p, name))
os.makedirs("/%s/%s/config/thumbnail" % (p, name))
os.makedirs("/%s/%s/doc/concept" % (p, name))
os.makedirs("/%s/%s/edit" % (p, name))
os.makedirs("/%s/%s/in" % (p, name))
os.makedirs("/%s/%s/out" % (p, name))
os.makedirs("/%s/%s/shot" % (p, name))
