import json

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class ApiClient(APIClient):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            self.user = user
            token = Token.objects.create(user=self.user)
            self.credentials(
                HTTP_AUTHORIZATION=f'Token {token}',
                HTTP_X_CLIENT='testing',
            )

    def get(self, *args, **kwargs):
        status = kwargs.get('status', 200)
        return self._request('get', status, *args, **kwargs)

    def patch(self, *args, **kwargs):
        status = kwargs.get('status', 200)
        return self._request('patch', status, *args, **kwargs)

    def post(self, *args, **kwargs):
        status = kwargs.get('status', 201)
        return self._request('post', status, *args, **kwargs)

    def put(self, *args, **kwargs):
        status = kwargs.get('status', 200)
        return self._request('put', status, *args, **kwargs)

    def delete(self, *args, **kwargs):
        status = kwargs.get('status', 204)
        return self._request('delete', status, *args, **kwargs)

    def _request(self, method, status, *args, **kwargs):
        kwargs['format'] = kwargs.get('format', 'json')
        as_response = kwargs.pop('as_response', False)
        method = getattr(super(), method)

        response = method(*args, **kwargs)
        assert response.status_code == status
        return response if as_response else self._decode(response)

    def _decode(self, response):
        content = response.content.decode('utf-8', errors='ignore')
        content_type = response._headers['content-type']
        if 'application/json' in content_type[1]:
            return json.loads(content)
        else:
            return content
