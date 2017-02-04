#FIFTH VERSION BEFORE I STARTED UDACITY STYLE CODING
import webapp2
import cgi
import re
form="""
<html>
<head>
</head>
<body style="background-color:white;">
<h1>Signup</h1>

    <form method="post">
        <label type="text" style="display:inline-block;width:150px;color:black">Username</label>
        <input type="text" name="username">%(username_error)s<br><br>
        <label type="text" style="display:inline-block;width:150px;color:black">Password</label>
        <input type="password" name="password">%(password_error)s<br><br>
        <label type="text" style="display:inline-block;width:150px;color:black">Verify Password</label>
        <input type="password" name="Vpassword">%(Vpassword_error)s<br><br>
        <label type="text" style="display:inline-block;width:150px;color:black">Email Optional</label>
        <input type="text" name="email">%(email_error)s<br><br>
    <input type="submit" value="Submit Query">
    </form>
</body>
</html>
"""


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        inputinfo = dict(username_error = "",
                             password_error="",
                             Vpassword_error="",
                             email_error="")# to preserve the data user typed in Username box

        global form# to declare that form is the global variable declared in hTMl above and
                    #it is being assigned to a local variable form which replaces username_error etc
                    # with new values in the " "
        form= form % inputinfo
        self.response.out.write(form)
    def post(self):
        user =self.request.get("username")
        faulty_form=False
#        validuser = cgi. escaped(user)
        passw = self.request.get("password")
        VerifiedPassword = self.request.get("Vpassword")
        Email = self.request.get("email")
        userwarn = ""
        pwdwarn = ""
        vpwdwarn = ""
        emailwarn = ""
        if not valid_username(user):#If you supply "user" as this parameter, then it is not the same as user = self.request.get("username")
            userwarn = "This is not valid username."
            faulty_form = True
        if not valid_password(passw):
            pwdwarn = "This is not a valid password"
            faulty_form = True
        elif VerifiedPassword !=passw:
            vpwdwarn = "Passwords do not match."
            faulty_form = True
        if not valid_email(Email):
            emailwarn = "This is not a valid email."
            faulty_form = True
        inputinfo = dict(username_error = userwarn,
                         password_error=pwdwarn,
                         Vpassword_error=vpwdwarn,
                         email_error=emailwarn)
        self.response.write( form % inputinfo)
        if faulty_form == False:
            self.redirect('/welcome' )
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        user = self.request.get("username")
        content = "Welcome," +user +"!"
        self.response.write(content)
app = webapp2.WSGIApplication([ ('/',MainHandler),
    ('/welcome',WelcomeHandler)
    ],debug=True)
