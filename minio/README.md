Hi there :)
I build a python script that you can with using it, manage your Minio Buckets and Objects.

What is MiniO API?
 - The MinIO API refers to the application programming interface provided by MinIO, 
 the open-source, cloud-native, distributed object storage server.
 The API allows developers to interact with the MinIO server programmatically, 
 enabling them to manage buckets, upload and download objects, set access policies, 
 and perform various other operations.

Some of the Key features of the MinIO API:
1. RESTful Interface: The MinIO API follows the principles of 
Representational State Transfer (REST), making it accessible 
over standard HTTP methods like GET, PUT, POST, DELETE, etc.

2. Bucket Operations: Developers can create, list,
and delete buckets through the API.

2. Object Operations: The API allows for uploading,
downloading, copying, and deleting objects 
within buckets.(but in this python script you can 
just Upload, Download and Delete)


guide to run my app:
1. First of all you need to install requirements libraries,
for that, in your cloned folder you'll see 
"requirements.txt", Follow below coomand:
    - pip install -r requirements.txt
3. Install minio client on your server:
    Linux(Ubuntu/Debian):
    - sudo apt-get update
    - sudo apt install -y minio-client
    - mc --version
4. Clone the repository
5. After cloning, follow this commands:
    - python3 app.py
---------------------------------------------------
* In the minio_functions.py, you should go and Define 
your ENDPOINT, ACCESS KEY and SECRET KEY
---------------------------------------------------
after run the code, you'll see 7 options:
1. List of all buckets
2. Create a new bucket
3. Delete Bucket
4. List the Objects of a specific bucket
5. Upload Objects
6. Download Objects
7. Delete Objects
