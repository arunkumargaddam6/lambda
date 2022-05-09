import boto3

aws_mng_con=boto3.session.Session(profile_name='root')
aws_cli_users=aws_mng_con.client(service_name='iam',region_name='us-east-1')

for each in aws_cli_users.list_users()['Users']:
    print(each['UserName'])