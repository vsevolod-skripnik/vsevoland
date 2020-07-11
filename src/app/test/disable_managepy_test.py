from django.core.management.base import CommandError


class DisableTestCommandRunner:
    def __init__(self, *args, **kwargs):
        pass

    def run_tests(self, *args):
        raise CommandError('Pytest, motherfucker, do you speak it?')
