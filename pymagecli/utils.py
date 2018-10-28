from os import path

from pymagecli.image import Image
from pymagecli.s3 import S3


def check_extension(key):
    """
    Verifies if the file extension is valid.
    Valid formats are JPG and PNG.
    :param key: Name of the file
    :return: string file extension
    """
    extension = path.splitext(key)[1].lower()

    if 'pymage_archive' not in key and extension.lower() in [
        '.jpg',
        '.jpeg',
        '.png',
    ]:
        return extension
    else:
        print("skipping, wrong ext: for {}".format(key))


def get_file_and_resize(bucket_name, file_name, width=600):
    image = Image()
    s3 = S3()
    obj = s3.get_object(bucket_name, file_name)
    body = obj.get()['Body'].read()
    file_ext = check_extension(file_name)
    if not file_ext:
        return None
    new_body = image.resize_image(
        body=body,
        extension=file_ext,
        width=width
    )
    if new_body:
        s3.copy_to_archive(bucket_name=bucket_name, key=file_name)
        s3.put_object(
            bucket_name=bucket_name,
            key=file_name,
            body=new_body
        )
