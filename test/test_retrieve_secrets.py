from src.retrieve_secret import retrieve_secret
from unittest.mock import patch, Mock
import datetime
import pytest
from moto import mock_secretsmanager

mock_res = {'ARN': 'arn:aws:secretsmanager:eu-west-2:027026634773:secret:a-IueujH',
            'CreatedDate': datetime.datetime(2023, 7, 20, 10, 27, 5, 315000),
            'Name': 'test_secret',
            'ResponseMetadata': {'HTTPHeaders': {'content-length': '255',
                                                 'content-type': 'application/x-amz-json-1.1',
                                                 'date': 'Fri, 21 Jul 2023 09:40:59 GMT',
                                                 'x-amzn-requestid': '491bdd7f-e0c2-4379-a51d-a983dba03cb9'},
                                 'HTTPStatusCode': 200,
                                 'RequestId': '491bdd7f-e0c2-4379-a51d-a983dba03cb9',
                                 'RetryAttempts': 0},
            'SecretString': '{"username": "test_user", "password": "test_password"}',
            'VersionId': '7d83a4e9-eb50-43bd-940f-4a583f0300b0',
            'VersionStages': ['AWSCURRENT']}


def test_retrieve_secrets_outputs_data_to_a_file():
    with patch('src.retrieve_secret.boto3.client') as mock_client, patch('builtins.input', side_effect=['test_secret']):

        mock_secrets = Mock()
        mock_secrets.get_secret_value.return_value = mock_res
        mock_client.return_value = mock_secrets

        retrieve_secret()

        with open('data_files/secrets.txt') as f:
            secret = f.readlines()
        assert secret == ['UserId: test_user\n', 'Password: test_password\n']


@mock_secretsmanager
def test_retrieve_secrets_catches_error_when_no_secret_exists():
    with patch('builtins.input', side_effect=['no_secret']):

        with pytest.raises(TypeError, match='Secrets Manager can\'t find the specified secret.'):
            retrieve_secret()


@mock_secretsmanager
def test_retrieve_secrets_catches_error_when_passed_empty_string():
    with patch('builtins.input', side_effect=['']):

        with pytest.raises(AttributeError, match='Please enter a valid secret...'):
            retrieve_secret()
