from __future__ import print_function

from urllib.parse import unquote_plus

from pymagecli.utils import get_file_and_resize


def lambda_handler(event, context):
    """
    AWS Lambda handler to resize uploaded images to 600px
    """
    print("Incoming event: {}".format(event))
    for object in event.get("Records"):
        key = unquote_plus(object["s3"]["object"]["key"])
        bucket_name = unquote_plus(object["s3"]["object"]["bucket_name"])
        print("Pymage: Resizing {} in bucket: {}".format(key, bucket_name))
        get_file_and_resize(bucket_name=bucket_name, file_name=key)
