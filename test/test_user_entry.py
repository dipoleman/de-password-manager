import boto3
from moto import mock_secretsmanager
from unittest.mock import patch
from src.user_entry import user_entry
import pytest


@mock_secretsmanager
def test_secret_manager():
    with patch('builtins.input', side_effect=['test-secret', 'test-user']), patch('src.user_entry.password', return_value='test-password'):

        user_entry()

    test_secret = boto3.client('secretsmanager')
    res = test_secret.get_secret_value(SecretId='test-secret')

    assert res['SecretString'] == '{"username": "test-user", "password": "test-password"}'


@mock_secretsmanager
def test_secret_manager_has_unique_id():
    with patch('builtins.input', side_effect=['test-secret', 'test-user']), patch('src.user_entry.password', return_value='test-password'):
        user_entry()
        with pytest.raises(TypeError, match='A secret with the specified name already exists'):
            with patch('builtins.input', side_effect=['test-secret', 'test-user', 'test-password']):
                user_entry()


@mock_secretsmanager
def test_secret_manager_has_no_empty_input_values():
    with patch('builtins.input', side_effect=['test-secret', 'test-user']), patch('src.user_entry.password', return_value='test-password'):

        user_entry()

    test_secret = boto3.client('secretsmanager')
    res = test_secret.get_secret_value(SecretId='test-secret')

    assert res['SecretString'] == '{"username": "test-user", "password": "test-password"}'


@mock_secretsmanager
def test_secret_manager_does_not_allow_spaces_or_invalid_chars_for_SecretId():
    with patch('builtins.input', side_effect=['test-secret', 'test user']), patch('src.user_entry.password', return_value='test password'):
        user_entry()

        test_secret = boto3.client('secretsmanager')
        res = test_secret.get_secret_value(SecretId='test-secret')

        assert res['SecretString'] == '{"username": "test user", "password": "test password"}'
