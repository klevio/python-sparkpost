import sparkpost

from .exceptions import SparkPostAPIException
from .base import TornadoTransport
from .transmissions import Transmissions
from .. import Metrics, RecipientLists, SuppressionList, Templates
from ..events import Events

__all__ = ["SparkPost", "TornadoTransport", "SparkPostAPIException",
           "Transmissions"]


class SparkPost(sparkpost.SparkPost):
    TRANSPORT_CLASS = TornadoTransport

    def __init__(self, *args, **kwargs):
        super(SparkPost, self).__init__(*args, **kwargs)
        self.metrics = Metrics(self.base_uri, self.api_key,
                               self.TRANSPORT_CLASS)
        self.recipient_lists = RecipientLists(self.base_uri, self.api_key,
                                              self.TRANSPORT_CLASS)
        self.suppression_list = SuppressionList(self.base_uri, self.api_key,
                                                self.TRANSPORT_CLASS)
        self.templates = Templates(self.base_uri, self.api_key,
                                   self.TRANSPORT_CLASS)
        self.transmissions = Transmissions(self.base_uri, self.api_key,
                                           self.TRANSPORT_CLASS)
        self.events = Events(self.base_uri, self.api_key,
                             self.TRANSPORT_CLASS)
        # Keeping self.transmission for backwards compatibility.
        # Will be removed in a future release.
        self.transmission = self.transmissions
