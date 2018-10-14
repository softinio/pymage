import boto3


class S3(object):
    def __init__(self):
        self.s3 = boto3.resource('s3')

    def get_object(self, bucket, key):
        """

        :param bucket: Name of the S3 Bucket
        :param key: Object name to return
        :return:
        """
        return self.s3.Object(bucket_name=bucket, key=key)

    def put_object(self, bucket_name, key, body):
        obj = self.s3.Object(
            bucket_name=bucket_name,
            key=key,
        )
        obj.put(ACL='public-read', Body=body)

    def delete_object(self, bucket_name, key):
        obj = self.s3.Object(
            bucket_name=bucket_name,
            key=key,
        )
        obj.delete()

    def list_objects(self, bucket):
        return self.s3.Bucket(bucket).objects.all()

