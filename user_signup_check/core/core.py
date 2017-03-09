import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def validate_user(text):
	return USER_RE.match(text)
def validate_password(passwod):
	return PASSWORD_RE.match(passwod)
def validate_email(email):
	return EMAIL_RE.match(email)
