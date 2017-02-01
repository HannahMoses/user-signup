#!/usr/bin/env python## Copyright 2007 Google Inc.## Licensed under the Apache License, Version 2.0 (the "License");# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at#http://www.apache.org/licenses/LICENSE-2.0# Unless required by applicable law or agreed to in writing, software# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.# See the License for the specific language governing permissions and# limitations under the License.
import webapp2
import cgi
def display(fieldname):
    textarea_label = "<label type='text' style='display:inline-block;width:150px;font-size:16px'>"+fieldname+ "</label>"
#if fieldname == Password info = "Mypassword"
    textarea = "<input type='text' style='width:150px'/>"
    warning = " "+fieldname + " warning appears here."
    return textarea_label + textarea + warning

def build_signup():
    body = "<body style='background-color:white'>Hi.</body>"
    submit="<input type ='submit' value='Submit Query' />"
    form =("<form method='post'>" +
            display("Username")+"<br><br>"+
            display("Password")+"<br><br>"+
            display("Verify Password")+"<br><br>"+
            display("Email(optional)")+"<br><br>"+
            submit+
            "</form>")
    return body + form
class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1 style='color:black;'>Signup</h1>"
        content = build_signup()  #build_signup("signup")
        self.response.out.write(header + content)
    def post(self):
#        header = "<h1 style='color:red;'>"+ Sorry signup again. +"</h1>"
        content = build_signup()   #build_signup("Sorry")
        self.response.out.write(content)
app = webapp2.WSGIApplication( [
    ('/', MainHandler)
    ],debug=True)
#class Welcome(bighead):
#     def get(self):
#         user = self.request.get("Username")
#         # if valid_Username(Username):
#         #     self.render("<h1 style='font-family: 'Times New Roman';color:black' > Welcome, "   +user +"! </h1>",user=Username)
#         # else:
#         #     self.redirect('/')
#         self.response.write("Fix errors in form.")
# app = webapp2.WSGIApplication([
#     ('/',MainHandler),
# #    ('/welcome',Welcome)
#     ],debug=True)
