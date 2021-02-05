from django.contrib.auth.models import AnonymousUser

from default.testing import register


@register
def user(self, **kwargs):
    return self.mixer.blend('users.User', **kwargs)


@register
def anon(self, **kwargs):
    return AnonymousUser()
