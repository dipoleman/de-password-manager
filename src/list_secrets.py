import boto3


def list_user_secrets():

    secretm = boto3.client('secretsmanager')
    secrets = secretm.list_secrets()
    print(f'\n{len(secrets["SecretList"])} secret(s) available')
    result = [secret['Name'] for secret in secrets['SecretList']]
    [print(f'Secret {i+1}: ', secret['Name'])
     for i, secret in enumerate(secrets['SecretList'])]
    return result
