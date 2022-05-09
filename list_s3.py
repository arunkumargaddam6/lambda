import boto3

aws_con_mng=boto3.session.Session(profile_name='root')
s3_console=aws_con_mng.resource('s3')
for each_s3 in s3_console.buckets.all():
    print(each_s3.name)