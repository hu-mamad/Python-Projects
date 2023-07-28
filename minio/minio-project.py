import requests
from minio import Minio
from minio.error import S3Error

# Minio server configuration
MINIO_ENDPOINT = "https://miinioapi.duckdns.org"
MINIO_ACCESS_KEY = "python-test"
MINIO_SECRET_KEY = "11236939"
USE_SSL = True 

# List of bucket names you want to create
BUCKET_NAMES = ["dorak", "hunter"]

def create_minio_buckets():
    # Initialize Minio client
    minio_client = Minio(
        endpoint=MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=USE_SSL
    )

    try:
        for bucket_name in BUCKET_NAMES:
            minio_client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully :)")

    except S3Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    create_minio_buckets()
