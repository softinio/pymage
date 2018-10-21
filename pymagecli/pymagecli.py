import click

from pymagecli.s3 import S3
from pymagecli.utils import get_file_and_resize


@click.group()
def cli():
    pass


@cli.command()
@click.argument('bucket_name')
def list(bucket_name):
    """Lists contents of a given bucket"""
    print("Bucket: {}".format(bucket_name))
    s3 = S3()
    bucket_list = s3.list_objects(bucket_name)
    [print(key.key) for key in bucket_list]


@cli.command()
@click.argument('bucket_name')
@click.option('--width', default=600, help='Image width')
def resize(bucket_name, width):
    """Resize all files in a bucket"""
    s3 = S3()
    bucket_list = s3.list_objects(bucket_name)
    [get_file_and_resize(bucket_name=bucket_name, file_name=key.key, width=width) for key in bucket_list]


@cli.command()
@click.argument('bucket_name')
@click.argument('file_name')
@click.option('--width', default=600, help='Image width')
def file(bucket_name, file_name, width):
    """resize a given file"""
    get_file_and_resize(
        bucket_name=bucket_name,
        file_name=file_name,
        width=width
    )

