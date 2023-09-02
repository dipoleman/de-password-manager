import boto3
from botocore.exceptions import ClientError
import json
import re
from pwinput import pwinput

pattern = r'^[a-zA-Z0-9\-_+=.@!]+$'


def identifier():
    secret_identifier = input('Secret identifier: \n')
    if secret_identifier == '':
        print('Please enter a valid identifier')
        return identifier()
    elif not re.fullmatch(pattern, secret_identifier):
        print('Please enter a string using alphanumerical characters and - _ + = . @ !')
        return identifier()
    return secret_identifier


def userId():
    user_id = input('UserId: \n')
    if user_id == '':
        print('Please enter a valid UserId')
        return userId()
    return user_id


def password():
    user_password = pwinput('Password: \n', mask="*")
    if user_password == '':
        print('Please enter a valid password')
        return password()
    return user_password


def user_entry():
    try:

        secret_identifier = identifier()
        user_id = userId()
        user_password = password()

        print(
            f'\nSecret Identifier: {secret_identifier}\nUserId: {user_id} \nPassword: {"*" * len(user_password)}')

        secretm = boto3.client('secretsmanager')

        secretm.create_secret(Name=secret_identifier, SecretString=json.dumps(
            {"username": user_id, "password": user_password}))
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceExistsException':
            raise TypeError('A secret with the specified name already exists')
        else:
            raise TypeError
