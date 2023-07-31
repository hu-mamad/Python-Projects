from colorama import Fore, Back, Style
from minio import Minio
from minio.error import S3Error
# Define my self as a client   
client = Minio(endpoint="---your-http-endpoint---",
    access_key="---your-access-key---",
    secret_key="---your-secret-key---",
    secure=True)# IF YOUR ENDPOINT ARE USING HTTPS IT SHOULD BE TRUE
# ------------Buckets------------- #
# Buckets list
def list_buckets():
    buckets = client.list_buckets()
    bucket_names = [bucket.name for bucket in buckets]
    return f"Total buckets:  {len(bucket_names)}\nBucket names : {', '.join(bucket_names)}"
# Create bucket
def create_bucket():
    try:
        z = input("Please enter your bucket name : ")
        b_name = str(z.strip())
        try:                
            if b_name =="quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
            elif client.bucket_exists(b_name):
                return f"{b_name} bucket is already exist :("
            else:
                client.make_bucket(b_name)
                return f"{b_name} Successfully created :)"
        except S3Error as err:
            return f"Error: {err}"
    except ValueError:
        return "Your input was not a string"
# Delete bucket
def delete_bucket():
    try:
        z = input("Please enter the bucket name you want to delete : ")
        b_name = str(z.strip())
        try:                
            if b_name == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
            elif not client.bucket_exists(b_name):
                return f"{b_name} does not exist :("
            else:
                client.remove_bucket(b_name)
                return f"{b_name} Successfully deleted :)"
        except S3Error as err:
            return f"Error: {err}"
    except ValueError:
        return "Your input was not a string"
    
# ------------Objects------------- #
# Objects list
def list_objects():
    try:
        z = input("Please enter the bucket name: ")
        b_name = str(z.strip())
        try:
            if b_name == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
            elif not client.bucket_exists(b_name):
                return f"{b_name} bucket does not exist :("
            else:
                objects = client.list_objects(b_name)
                object_list = [obj.object_name for obj in objects]
                return f"Objects in {b_name}: {', '.join(object_list)}"
        except S3Error as err:
            return f"Error: {err}"
    except ValueError:
        return "Your input was not a string"
# Upload a Object to a specific bucket
def upload_object():
    try:
        bucket_name = input("Enter the bucket name: ").strip()
        if bucket_name == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
        object_name = input("Enter the object name: ").strip()
        if object_name == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
        file_path = input("Enter the path of the file you want to upload: ").strip()
        if file_path == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)

        if not client.bucket_exists(bucket_name):
            return f"{bucket_name} bucket does not exist :("
        else:
            try:
                with open(file_path, "rb") as file_data:
                    file_size = file_data.seek(0, 2)
                    if file_size == 0:
                        return "File is empty. Please provide a non-empty file."
                    file_data.seek(0)
                    client.put_object(bucket_name, object_name, file_data, length=file_size)
                return f"{object_name} Successfully uploaded to {bucket_name}"
            except FileNotFoundError:
                return "File not found."
    except Exception as e:
        return f"Error: {e}"

# Download a Object
def download_object():
    try:
        bucket_name = input("Enter the bucket name: ").strip()
        if bucket_name == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
        object_name = input("Enter the object name: ").strip()
        if object_name == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
        version_id = input("Enter the version ID (leave empty to download the latest version): ").strip()
        if version_id == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
        save_path = input("Enter the path where you want to save the downloaded file: ").strip()
        if save_path == "quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)

        if not client.bucket_exists(bucket_name):
            return f"{bucket_name} bucket does not exist :("
        else:
            try:
                response = client.get_object(bucket_name, object_name, version_id=version_id)
                if save_path.endswith('/'):
                    save_path = save_path + object_name
                with open(save_path, "wb") as file_data:
                    for data in response.stream(32 * 1024):
                        file_data.write(data)
                return f"{object_name} (Version ID: {version_id}) Successfully downloaded from {bucket_name} and saved to {save_path}"
            except S3Error as err:
                return f"Error: {err}"
            except FileNotFoundError:
                return "File not found."
    except Exception as e:
        return f"Error: {e}"
    
# Delete a Object
def delete_object():
    try:
        bucket_name = input("Enter the bucket name: ").strip()
        if bucket_name == "quit":
            exit("Goodbye Fella :)\n" + Style.RESET_ALL)
        object_name = input("Enter the object name: ").strip()
        if object_name == "quit":
            exit("Goodbye Fella :)\n" + Style.RESET_ALL)

        if not client.bucket_exists(bucket_name):
            return f"{bucket_name} bucket does not exist :("
        else:
            try:
                client.remove_object(bucket_name, object_name)
                return f"{object_name} Successfully deleted from {bucket_name}"
            except S3Error as err:
                return f"Error: {err}"
            except FileNotFoundError:
                return "Object not found."
    except Exception as e:
        return f"Error: {e}"