#!/usr/bin/env python
#coding:utf8

# === my way ===

# import sys
# import os

# p = "project"
# name = sys.argv[1]

# os.makedirs("/%s/%s/asset/char" % (p, name))
# os.makedirs("/%s/%s/asset/shader" % (p, name))
# os.makedirs("/%s/%s/config/ocio" % (p, name))
# os.makedirs("/%s/%s/config/thumbnail" % (p, name))
# os.makedirs("/%s/%s/doc/concept" % (p, name))
# os.makedirs("/%s/%s/edit" % (p, name))
# os.makedirs("/%s/%s/in" % (p, name))
# os.makedirs("/%s/%s/out" % (p, name))
# os.makedirs("/%s/%s/shot" % (p, name))

# === other way ===

import os
import sys

def addProject(name):
	"""
	프로젝트 하위 경로를 생성하는 함수입니다.
	"""
	root = "/project"
	subDirs = ["asset",
			"asset/char",
			"asset/shader",
			"config",
			"config/ocio",
			"config/thumbnail",
			"doc",
			"doc/concept",
			"edit",
			"in",
			"out",
			"shot"]
	for s in subDirs:
		p = "/".join([root, name, s])
		os.makedirs(p)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "How to use:"
		print "$ addproject projectname"
		sys.exit()
	name = sys.argv[1]
	addProject(name)

