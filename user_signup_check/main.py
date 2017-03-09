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
import webapp2
import jinja2
import os
import core.core as core

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment( loader = jinja2.FileSystemLoader(template_dir),
									autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kwargs):
        self.response.write(*a, **kwargs)
    def render_string(self, template, **params):
    	temp = jinja_env.get_template(template)
    	return temp.render(params)
    def render(self, template, **params):
    	self.write(self.render_string(template, **params))
    def get_from_request(self, valName):
    	return self.request.get(valName)

class MainHandler(Handler):
	def get(self):
		page = {
			"title": "Please Signup To Use Our Services!",
			"errors": {

			}
		}
		self.render("maintemplate.html", page = page)
	def post(self):
		page = {
			"title": "Please Check the Errors In the Form",
			"errors": {},
			"hasErrors": False
		}
		userName = self.get_from_request("userName")
		password = self.get_from_request("password")
		rePass = self.get_from_request("rePassword")
		email = self.get_from_request("email")

		if not (userName and core.validate_user(userName) ):
			page["errors"]["userName"] = True
			page["hasErrors"] = True

		if not (password and core.validate_password(password)):
			page["errors"]["password"] = True
			page["hasErrors"] = True
		else:
			if not (rePass and rePass == password):
				page["errors"]["rePass"] = True
				page["hasErrors"] = True

		if email and not core.validate_email(email):
			page["errors"]["email"] = True
			page["hasErrors"] = True
 	
 		if page["hasErrors"]:
			self.render("maintemplate.html", page = page)
		else:
			self.redirect("/welcome?userName=" + userName)
class WelcomeHandler(Handler):
	def get(self):
		user = self.request.get("userName")
		self.render("welcomeTemplate.html", userName = user)

app = webapp2.WSGIApplication([
    ('/', MainHandler), ("/welcome", WelcomeHandler)
], debug=True)
