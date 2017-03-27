#!/usr/bin/python

from lib import stream

def test_stream_object_init():
    s = stream.Stream()
    assert s.client is not None
    assert s is not None

def test_publish_object_init():
    s = stream.Publish()
    assert s.client is not None
    assert s is not None

def test_publish_object_init():
    s = stream.Subscribe()
    assert s.client is not None
    assert s is not None

def test_message_publishing():
    s = stream.Publish()
    result = s.put_message("{'foo': 'bar'}")
    assert result['ResponseMetadata']['HTTPStatusCode'] is 200

def test_fetching_messages():
    s = stream.Publish()
    result = s.put_message("{'foo': 'bar'}")
    p = stream.Subscribe()
    shard_iterator = p.shard_iterator()

    records = p.messages()
    assert len(records) > 0
    assert shard_iterator is not None
