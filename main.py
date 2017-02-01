#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import webapp2
'''
def valid_user(username):
    if username :
        if username.isdigit:
            warning="This is not a valid user name."
            return warning
#        if " " not in username:
'''

def build_signup():
            message = "I still need to validate and display the warnings !"
            textarea = "<textarea type='text' style='width:500px'>"+message+"</textarea>"
            body = "<body style='background-color:white'>.<br><br></body>"
    #        header = "<h2 style='background-color:rgb(0,180,200);color:white;text-align:center'>USER SIGN-UP</h2>"
    #        body = "<body style='background-color:rgb(0,180,200)'>Please note that, the first three fields ar required.<br><br></body>"
            submit="<input type='submit' value='Submit Query'/>"
            form= ("<form method = 'post'>"+
            display_field("Username")+"<br><br>"+
            display_field("Password")+"<br><br>"+
            display_field("Verify Password")+"<br><br>"+
            display_field("Email(optional)")+"<br><br>"+
            textarea+"<br><br>"+submit+
            "</form>")
            return body + form

def display_field(fieldname):
            textarea_label ="<label style='font-size:16px;background-color:white;display:inline-block;width:150px'>"+fieldname+ "</label>"
            textarea =  "<input type ='text' name = 'fieldname'>"
            return textarea_label+ textarea
# def valid_Username(textarea):
#     for i in textarea :
#         if i !=" " :
#             return True

# def display_errmessage(fieldname):
#     errmessage = "That's not a valid username."
#     errmessage_label ="<label style='font-size:16px;color:red;display:inline-block;width:150px'>"+errmessage+ "</label>"
#     return errmessage_label
class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h2 style='font-family: 'Times New Roman';color:black' > Signup</h2>"
        content = build_signup()
        self.response.out.write(header + content)

    def post(self):
        #if (valid_Username and valid_password and valid_VerifyPassword) :
        correctinfoheader = "<h2 style='font-family: 'Times New Roman';color:black' > Thankyou !</h2>"
        content = build_signup()
        self.response.write(correctinfoheader +  content)

        # if valid_Username(Username) :
        #     self.response.write(correctinfoheader + content)
        # else:
        #     errorheader = "<h2 style='font-family: 'Times New Roman';color:black' > Please signup again !</h2>"
        #     errormessage = " !"
        #     self.response.write(errorheader + errormessage + content)

app = webapp2.WSGIApplication([
    ('/',MainHandler)
    ],debug=True)
