import click

from s3 import S3

@click.group()
def cli():
    pass


@cli.command()
@click.argument('bucket_name')
def list(bucket_name):
    """Lists contents of a given bucket"""
    s3 = S3()
    s3.list_objects(bucket_name)


@cli.command()
@click.argument('bucket_name')
def resize(bucket_name):
    """Resize all files in a bucket"""
    s3 = S3()
    #TODO


@cli.command()
@click.argument('bucket_name')
@click.argument('file_name')
def file(bucket_name, file_name):
    """resize a given file"""
    s3 = S3()
    #TODO


if __name__ == '__main__':
    cli()
