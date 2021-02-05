from default.testing import register


@register
def comic(self, **kwargs):
    return self.mixer.blend('comics.Comic', **kwargs)
