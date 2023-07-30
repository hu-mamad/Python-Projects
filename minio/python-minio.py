from colorama import Fore, Back, Style
from minio import Minio
from minio.error import S3Error

client = Minio(endpoint="miinioapi.duckdns.org",
    access_key="biighunter",
    secret_key="11236939",
    secure=True)

print(Fore.LIGHTGREEN_EX + f"Here you can do anything with your minio buckets console. \nEnter number of the action you want to do :")

print(Fore.MAGENTA + f"\n1.Total Buckets\n2.Create A Buckets\n3.Delete An Objects\n4.Download A File\n"+ Style.RESET_ALL)

def bc():
    try:
        b_name = input("Please enter your bucket name : ")
        if client.bucket_exists(b_name):
            return f"{b_name} is already exist :("
        else:
            client.make_bucket(b_name)
            return f"{b_name} Successfully created :)"
    except S3Error as err:
        return f"Error: {err}"

def switch(x):
    if x == "1":
        return f"Total buckets:  {len(client.list_buckets())}"
    elif x == "2":
        result = bc()
        return result
client_input = input(Fore.LIGHTYELLOW_EX)
print(Fore.LIGHTRED_EX + switch(client_input) + Style.RESET_ALL)