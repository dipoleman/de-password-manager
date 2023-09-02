from src.list_secrets import list_user_secrets
from unittest.mock import patch, Mock
import datetime
from moto import mock_secretsmanager


mock_res = {'ResponseMetadata': {'HTTPHeaders': {'content-length': '511',
                                                 'content-type': 'application/x-amz-json-1.1',
                                                 'date': 'Thu, 20 Jul 2023 11:27:10 GMT',
                                                 'x-amzn-requestid': 'a45d3df1-7efd-4139-a5e4-2c872d734f10'},
                                 'HTTPStatusCode': 200,
                                 'RequestId': 'a45d3df1-7efd-4139-a5e4-2c872d734f10',
                                 'RetryAttempts': 0},
            'SecretList': [{'ARN': 'arn:aws:secretsmanager:eu-west-2:027026634773:secret:a-IueujH',
                            'CreatedDate': datetime.datetime(2023, 7, 20, 10, 27, 5, 77000),
                            'LastAccessedDate': datetime.datetime(2023, 7, 20, 1, 0),
                            'LastChangedDate': datetime.datetime(2023, 7, 20, 10, 27, 5, 319000),
                            'Name': 'a',
                            'SecretVersionsToStages': {'7d83a4e9-eb50-43bd-940f-4a583f0300b0': ['AWSCURRENT']}},
                           {'ARN': 'arn:aws:secretsmanager:eu-west-2:027026634773:secret:xyz-smutF3',
                            'CreatedDate': datetime.datetime(2023, 7, 20, 12, 7, 9, 804000),
                            'LastChangedDate': datetime.datetime(2023, 7, 20, 12, 7, 9, 847000),
                            'Name': 'xyz',
                            'SecretVersionsToStages': {'e5d1b4d4-4ce9-4e54-9751-c021b210ab49': ['AWSCURRENT']}}]}


def test_list_user_secrets():
    with patch('src.list_secrets.boto3.client') as mock_client:

        mock_secrets = Mock()
        mock_secrets.list_secrets.return_value = mock_res

        mock_client.return_value = mock_secrets

        list_user_secrets()

        assert list_user_secrets() == ['a', 'xyz']


@mock_secretsmanager
def test_list_objects_returns_an_empty_array_with_no_secrets():

    assert list_user_secrets() == []
