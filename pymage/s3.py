import boto3


class S3(object):
    def __init__(self):
        self.s3 = boto3.resource('s3')

    def get_object(self, bucket, key):
        """
        GET S3 Object
        :param bucket: Name of the S3 Bucket
        :param key: Object name to return
        :return: S3 Object
        """
        return self.s3.Object(bucket_name=bucket, key=key)

    def put_object(self, bucket_name, key, body):
        """
        SAVE S3 Object
        :param bucket: Name of the S3 Bucket
        :param key: Object name
        :return: S3 Object
        """
        obj = self.s3.Object(
          bucket_name=bucket_name,
          key=key,
        )
        obj.put(
            ACL='public-read',
            Metadata={'pymage': 'true'},
            Body=body
        )

    def delete_object(self, bucket_name, key):
        """
        DELETE S3 Object
        :param bucket: Name of the S3 Bucket
        :param key: Object name to return
        :return: S3 Object
        """
        obj = self.s3.Object(
            bucket_name=bucket_name,
            key=key,
        )
        obj.delete()

    def list_objects(self, bucket):
        """
        GET list S3 Objects in a bucket
        :param bucket: Name of the S3 Bucket
        :return: List of S3 ObjectSummary resources
        """
        return self.s3.Bucket(bucket).objects.all()

    def copy_to_archive(self, bucket_name, key):
        """
        Copy file to archive sub folder
        :param bucket: Name of the S3 Bucket
        :param key: Object name to copy
        :return: S3 Object
        """
        source = {
            "Bucket": bucket_name,
            "Key": key,
        }
        destination = 'archive/{}'.format(key)
        self.s3.meta.client.copy(source, bucket_name, destination)
