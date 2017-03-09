#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment( loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kwargs):
		self.response.write(*a, **kwargs);
	def render_string(self, template, **params):
		template = jinja_env.get_template(template)
		return template.render(params)
	def render(self, template, **params):
		self.write(self.render_string(template, **params))

class MainHandler(Handler):
    def get(self):
        self.render("rot13Main.html")
    def post(self):
    	text_to_rot13 = self.request.get("rot13text")
    	rot13_val = text_to_rot13 and len(text_to_rot13) and text_to_rot13.encode("rot13")
    	self.render("rot13Main.html", rot_13_val = rot13_val)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
