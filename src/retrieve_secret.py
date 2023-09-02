import boto3
from botocore.exceptions import ParamValidationError
import json
from pprint import pprint


def retrieve_secret():
    try:
        user_secret = input('Specify secret to retrieve: \n')
        secretm = boto3.client('secretsmanager')
        secret = secretm.get_secret_value(SecretId=user_secret)
        user_data = secret['SecretString']
        user_data_object = json.loads(user_data)

        with open('data_files/secrets.txt', 'w') as outfile:
            outfile.write(
                f'UserId: {user_data_object["username"]}\nPassword: {user_data_object["password"]}\n')

        print('Secrets stored in local file secrets.txt')
    except ParamValidationError as e:
        raise AttributeError('Please enter a valid secret...')
    except Exception as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise TypeError(
                'Secrets Manager can\'t find the specified secret.')
