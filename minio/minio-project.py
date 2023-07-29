from flask import Flask, jsonify, render_template
from minio import Minio
from minio.error import S3Error

MINIO_ENDPOINT = "https://miinioapi.duckdns.org"
MINIO_ACCESS_KEY = "python-test"
MINIO_SECRET_KEY = "11236939"
USE_SSL = True 

BUCKET_NAMES = ["dorak", "hunter"]

hunt = Flask(__name__)

def create_minio_buckets():
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

@hunt.route("/create_buckets", methods=["POSTMAN"])
def create_buckets():
    create_minio_buckets()
    return jsonify({"message": "Buckets created successfully"}), 200

#if __name__ == "__main__":
hunt.run(host="0.0.0.0", port=5000)