from rest_framework.renderers import JSONRenderer


class DefaultJSONRenderer(JSONRenderer):
    charset = 'utf-8'  # force DRF to add charset header to the content-type
