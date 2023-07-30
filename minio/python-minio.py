from colorama import Fore, Back, Style
from minio import Minio
from minio.error import S3Error

client = Minio(endpoint="miinioapi.duckdns.org",
    access_key="biighunter",
    secret_key="11236939",
    secure=True)
while True:
    print(Fore.LIGHTWHITE_EX + f"Here you can do anything with your minio buckets console. \nEnter number of the action you want to do :")
    print(Fore.LIGHTBLUE_EX + f'(Enter "quit-app" to exit.)')
    print(Fore.MAGENTA + f"\n1.Total Buckets\n2.Create A Buckets\n3.Delete An Objects\n4.Download A File\n"+ Style.RESET_ALL)

    def bc():
        try:
            z = input("Please enter your bucket name : ")
            b_name = str(z.strip())
            try:                
                if b_name =="quit-app":
                    exit("Goodbye Fella :)" + Style.RESET_ALL)
                elif client.bucket_exists(b_name):
                    return f"{b_name} is already exist :("
                else:
                    client.make_bucket(b_name)
                    return f"{b_name} Successfully created :)"
            except S3Error as err:
                return f"Error: {err}"
        except ValueError:
            return "Your input was not a string"

    def switch(x):
        try:
            a = int(x)
            if a == 1:
                return f"Total buckets:  {len(client.list_buckets())}"
            elif a == 2:
                result = bc()
                return result
            elif a == 3:
                return
            elif a == 4:
                return
            else:
                return "Please enter a number between 1 & 4 :)"
        except ValueError:
            return "Your input is not a number :("
            
        
    client_input = input(Fore.LIGHTYELLOW_EX)
    if client_input =="quit-app":
                exit("Goodbye Fella :)" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + switch(client_input) + Style.RESET_ALL)