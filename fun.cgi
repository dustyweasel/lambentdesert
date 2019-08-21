#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from fun import app

CGIHandler().run(app)
