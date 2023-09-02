import boto3
from botocore.exceptions import ClientError, ParamValidationError


def delete_secret():
    try:
        to_delete = input('Specify secret to delete:\n')

        secretm = boto3.client('secretsmanager')

        deleted = secretm.delete_secret(SecretId=to_delete)
        print('Deleted')

        return deleted
    except ClientError as e:

        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise TypeError('SecretsManager cannot find the specified secret')

    except ParamValidationError as e:
        raise AttributeError('Please enter a valid secret...')
