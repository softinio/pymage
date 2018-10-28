import click

from pymagecli.markdown_parser import move_all_photos, move_all_photos_file
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


@cli.command()
@click.argument('bucket_name')
@click.argument('directory_path')
@click.argument('base_url')
def migrate(bucket_name, directory_path, base_url):
    """Migrate photos from a given url to s3 and replace url in markdown doc for all md files in a directory"""
    move_all_photos(
        bucket_name=bucket_name,
        directory_path=directory_path,
        base_url=base_url
    )

@cli.command()
@click.argument('bucket_name')
@click.argument('file_path')
@click.argument('base_url')
def migratefile(bucket_name, file_path, base_url):
    """Migrate photos from a given url to s3 and replace url in markdown doc for given file"""
    move_all_photos_file(
        bucket_name=bucket_name,
        file_name=file_path,
        base_url=base_url
    )
