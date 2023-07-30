from minio import Minio

client = Minio(endpoint="miinioapi.duckdns.org",
    access_key="biighunter",
    secret_key="11236939",
    secure=True)

print("Total buckets: ", len(client.list_buckets()))