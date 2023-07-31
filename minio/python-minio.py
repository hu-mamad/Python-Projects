from colorama import Fore, Back, Style
from minio import Minio
from minio.error import S3Error

# Define my self as a client   
client = Minio(endpoint="miinioapi.duckdns.org",
    access_key="biighunter",
    secret_key="11236939",
    secure=True)
while True:
    print(Fore.LIGHTWHITE_EX + f"Here you can do anything with your minio buckets console. \nEnter number of the action you want to do :")
    print(Fore.LIGHTBLUE_EX + f'(Enter "quit" to exit.)')
    print(Fore.MAGENTA + f"\n1.Total buckets\n2.Create a buckets\n3.Delete a bucket\n4.Total objects of a specific bucket\n5.Upload a object\n6.Download a object\n"+ Style.RESET_ALL)

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
                    exit("Goodbye Fella :)" + Style.RESET_ALL)
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
                    exit("Goodbye Fella :)" + Style.RESET_ALL)
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
                    exit("Goodbye Fella :)" + Style.RESET_ALL)
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
                    exit("Goodbye Fella :)" + Style.RESET_ALL)
            object_name = input("Enter the object name: ").strip()
            if object_name == "quit":
                    exit("Goodbye Fella :)" + Style.RESET_ALL)
            file_path = input("Enter the path of the file you want to upload: ").strip()
            if file_path == "quit":
                    exit("Goodbye Fella :)" + Style.RESET_ALL)

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
            object_name = input("Enter the object name: ").strip()
            save_path = input("Enter the path where you want to save the downloaded file: ").strip()

            if not client.bucket_exists(bucket_name):
                return f"{bucket_name} bucket does not exist :("
            else:
                try:
                    # Retrieve the object from Minio
                    response = client.get_object(bucket_name, object_name)

                    # Save the object content to the specified path
                    with open(save_path, "wb") as file_data:
                        for data in response.stream(32 * 1024):
                            file_data.write(data)
                    
                    return f"{object_name} Successfully downloaded from {bucket_name} and saved to {save_path}"
                except S3Error as err:
                    return f"Error: {err}"
                except FileNotFoundError:
                    return "File not found."
        except Exception as e:
            return f"Error: {e}"        
    
    
    def switch(x):
        try:
            a = int(x)
            if a == 1:
                result = list_buckets()
                return result
            elif a == 2:
                result = create_bucket()
                return result
            elif a == 3:
                result = delete_bucket()
                return result
            elif a == 4:
                result = list_objects()
                return result
            elif a == 5:
                result = upload_object()
                return result
            elif a == 6:
                result = download_object()
                return 
            else:
                return "Your a number should be between 1 and 6 :)"
        except ValueError:
            return "Your input is not a number :("
            
        
    client_input = input(Fore.LIGHTYELLOW_EX)
    if client_input =="quit":
                exit("Goodbye Fella :)" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + switch(client_input) + Style.RESET_ALL)