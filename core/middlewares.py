from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware


class PersonalSessionMiddleware(SessionMiddleware):
  pass

class PersonalAuthenticationMiddleware(AuthenticationMiddleware):
  pass

