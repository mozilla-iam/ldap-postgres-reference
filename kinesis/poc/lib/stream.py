#!/usr/bin/python
import boto3

"""
    Class of objects that dictate PoC interactions with kinesis stream.
    Can be integrated into lambda functions later.
"""

class Stream(object):
    def __init__(self):
        self.client = self.__connect()
        self.stream_name = 'ChangeIntegrationStream' #Fix this later to come from config

    def __connect(self):
        """Return a kinesis client."""
        session = self.__boto_session()
        client = session.client('kinesis', region_name='us-west-2')
        return client

    def __boto_session(self):
        try:
            session = boto3.Session(profile_name='cis-dev')
        except Exception as e:
            try:
                session = boto3.Session()
            except Exception as e:
                raise e
        return session

    def shards(self):
        response = self.client.describe_stream(
            StreamName=self.stream_name,
        )

        return response['StreamDescription']['Shards']

class Publish(Stream):
    def __init__(self):
        Stream.__init__(self)

    def put_message(self, data):
        """Adds a message to the change data input stream."""
        response = self.client.put_record(
            StreamName=self.stream_name,
            Data=data, #1 MB MAX message size
            PartitionKey='change_data_input' #Arbitrary value same a kafka channel
            #ExplicitHashKey='string', #Not required
            #SequenceNumberForOrdering='string'#Not required
        )
        return response


"""
This is just for test.  Really we would use the parallel record
processor https://github.com/awslabs/amazon-kinesis-client-python.
"""
class Subscribe(Stream):
    def __init__(self):
        Stream.__init__(self)

    def nearest_shard(self):
        """Find the nearest kinesis shard to this script."""
        return self.shards()[0]['ShardId']

    def shard_iterator(self):
        """Returns the shard iterator.  This is a fancy way of saying
        the serial number of the message to start reading forward from."""
        response = self.client.get_shard_iterator(
            StreamName=self.stream_name,
            ShardId=self.nearest_shard(),
            ShardIteratorType='LATEST' #For now return all records can be more elegant later
            #StartingSequenceNumber='string', #Optional
            #Timestamp=datetime(2015, 1, 1) #Optional
        )
        return response['ShardIterator']

    def messages(self):
        """This actually goes out and fetches the records to do stuff with."""
        response = self.client.get_records(
            ShardIterator=self.shard_iterator()
        )
        return response['Records']
