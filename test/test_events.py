import pytest
import responses

from sparkpost import SparkPost
from sparkpost.exceptions import SparkPostAPIException


@responses.activate
def test_success_events_message():
    responses.add(
        responses.GET,
        'https://api.sparkpost.com/api/v1/events/message',
        status=200,
        content_type='application/json',
        body='{"results": []}'
    )
    sp = SparkPost('fake-key')
    results = sp.events.message.list()
    assert results == []


@responses.activate
def test_fail_events_message():
    responses.add(
        responses.GET,
        'https://api.sparkpost.com/api/v1/events/message',
        status=500,
        content_type='application/json',
        body="""
        {"errors": [{"message": "You failed", "description": "More Info"}]}
        """
    )
    with pytest.raises(SparkPostAPIException):
        sp = SparkPost('fake-key')
        sp.events.message.list()


@responses.activate
def test_success_events_ingest():
    responses.add(
        responses.GET,
        'https://api.sparkpost.com/api/v1/events/ingest',
        status=200,
        content_type='application/json',
        body='{"results": []}'
    )
    sp = SparkPost('fake-key')
    results = sp.events.ingest.list()
    assert results == []


@responses.activate
def test_fail_events_ingest():
    responses.add(
        responses.GET,
        'https://api.sparkpost.com/api/v1/events/ingest',
        status=500,
        content_type='application/json',
        body="""
        {"errors": [{"message": "You failed", "description": "More Info"}]}
        """
    )
    with pytest.raises(SparkPostAPIException):
        sp = SparkPost('fake-key')
        sp.events.ingest.list()
