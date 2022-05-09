#manual steps to see all I am users

# step1: Get AWS management CONSOLE
#step2: Get I am console

import boto3

aws_mng_con=boto3.session.Session(profile_name="root")
Iam_cons=aws_mng_con.resource('iam')

for each_user in Iam_cons.users.all():
    print(each_user.name)



