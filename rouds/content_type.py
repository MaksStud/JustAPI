from enum import StrEnum


class ContentType(StrEnum):
    """
    Content types for HTTP responses
    """
    TEXT_HTML = 'text/html'
    TEXT_PLAIN = 'text/plain'
    APPLICATION_JSON = 'application/json'
    APPLICATION_XML = 'application/xml'
    APPLICATION_XHTML = 'application/xhtml+xml'
    APPLICATION_JAVASCRIPT = 'application/javascript'
    APPLICATION_JAVASCRIPT_TYPE = 'application/javascript; charset=utf-8'
    APPLICATION_JAVASCRIPT_TYPE_UTF_8 = 'application/javascript; charset=utf-8'
