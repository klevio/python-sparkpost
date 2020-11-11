from .base import Resource, RequestsTransport


class Events(object):
    """
    Wrapper for sub-resources
    """

    def __init__(self, base_uri, api_key, transport_class=RequestsTransport):
        self.base_uri = "%s/%s" % (base_uri, 'events')
        self.message = Message(self.base_uri, api_key, transport_class)
        self.ingest = Ingest(self.base_uri, api_key, transport_class)


class Message(Resource):
    """
    Message class used to list and search message events.
    For details see the `Events API documentation
    <https://developers.sparkpost.com/api/events>`_.
    """

    key = 'message'

    def list(self, **kwargs):
        """
        Get a list of message events. For search parameters see the `Search
        for Message Events API documentation
        <https://developers.sparkpost.com/api/events/#events-get-search-for
        -message-events>`_.

        :returns: list of message events
        :raises: :exc:`SparkPostAPIException` if API call fails
        """

        results = self.request('GET', self.uri, params=kwargs)
        return results


class Ingest(Resource):
    """
    Ingest class used to list and search ingest events.
    For details see the `Events API documentation
    <https://developers.sparkpost.com/api/events>`_.
    """

    key = 'ingest'

    def list(self, **kwargs):
        """
        Get a list of ingest events. For search parameters see the `Search
        for Ingest Events API documentation
        <https://developers.sparkpost.com/api/events/#events-get-search-for
        -ingest-events>`_.

        :returns: list of message events
        :raises: :exc:`SparkPostAPIException` if API call fails
        """
        results = self.request('GET', self.uri, params=kwargs)
        return results
