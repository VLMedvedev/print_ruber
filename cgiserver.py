#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Demo CGI Server
"""
import logging
import dbSqliteAlpameter as db

on = db.get_startedLoadVideo()
if on == 1:
    db.set_startedLoadVideo(0)

try:
    import BaseHTTPServer
    import CGIHTTPServer
except ImportError:
    import http.server as BaseHTTPServer
    import http.server as CGIHTTPServer
import cgitb

logging.basicConfig(level=logging.INFO)

cgitb.enable()  # This line enables CGI error reporting

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
handler.have_fork = 0 # debug
server_address = ("", 8000)
handler.cgi_directories = ["/cgi-bin", "/wsgi"]
#handler.cgi_directories = ["/cgi-bin", "/"]

#CGIHTTPRequestHandler.have_fork = 0
#httpd = HTTPServer(('', port), CGIHTTPRequestHandler)

httpd = server(server_address, handler)
httpd.serve_forever()
