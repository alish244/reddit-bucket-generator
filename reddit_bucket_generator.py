import boto3
from botocore.exceptions import ClientError

# ألوان للطباعة
class bcolors:
    OK = '\033[92m'    # أخضر
    FAIL = '\033[91m'  # أحمر
    END = '\033[0m'    # نهاية اللون

bucket_name = input("Enter bucket name: ")

s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

# فحص إمكانية القراءة
try:
    s3.list_objects_v2(Bucket=bucket_name)
    print(f"{bcolors.OK}[SUCCESS]{bcolors.END} Bucket '{bucket_name}' is readable")
except ClientError:
    print(f"{bcolors.FAIL}[FAIL]{bcolors.END} Bucket '{bucket_name}' is not readable")

# محاولة رفع ملف صغير
try:
    s3.put_object(Bucket=bucket_name, Key='test.txt', Body='This is a test.')
    print(f"{bcolors.OK}[SUCCESS]{bcolors.END} Able to write to '{bucket_name}'")
except ClientError:
    print(f"{bcolors.FAIL}[FAIL]{bcolors.END} Cannot write to '{bucket_name}'")
