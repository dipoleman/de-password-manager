from src.delete_secret import delete_secret
import boto3
import datetime
import json
from moto import mock_secretsmanager
from unittest.mock import patch
import pytest

mock_res = {'ARN': 'arn:aws:secretsmanager:eu-west-2:358070591655:secret:top-M8wMVD',
            'DeletionDate': datetime.datetime(2023, 8, 20, 11, 54, 46, 362000),
            'Name': 'test_secret',
            'ResponseMetadata': {'HTTPHeaders': {'content-length': '118',
                                                 'content-type': 'application/x-amz-json-1.1',
                                                 'date': 'Fri, 21 Jul 2023 10:54:45 GMT',
                                                 'x-amzn-requestid': 'a6972639-9a08-4f0e-a2e8-e3d59fe5dbe8'},
                                 'HTTPStatusCode': 200,
                                 'RequestId': 'a6972639-9a08-4f0e-a2e8-e3d59fe5dbe8',
                                 'RetryAttempts': 0}}


@mock_secretsmanager
def test_delete_secret_deletes_a_saved_secret():

    mock_secretm = boto3.client('secretsmanager')
    mock_secretm.create_secret(Name='test_secret', SecretString=json.dumps(
        {"username": "test_user", "password": "test_password"}))

    with patch('builtins.input', side_effect=['test_secret']):
        result = delete_secret()

    assert result['Name'] == mock_res['Name']


@mock_secretsmanager
def test_delete_secret_that_does_not_exist():

    with patch('builtins.input', side_effect=['no_secret']):
        with pytest.raises(TypeError, match='SecretsManager cannot find the specified secret'):
            delete_secret()


@mock_secretsmanager
def test_delete_secret_passed_an_empty_string():

    with patch('builtins.input', side_effect=['']):
        with pytest.raises(AttributeError, match='Please enter a valid secret...'):
            delete_secret()
