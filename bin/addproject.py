#!/usr/bin/env python
#coding:utf8

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

