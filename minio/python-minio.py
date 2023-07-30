from colorama import Fore, Back, Style
from minio import Minio

client = Minio(endpoint="miinioapi.duckdns.org",
    access_key="biighunter",
    secret_key="11236939",
    secure=True)

print(Fore.LIGHTGREEN_EX + f"Here you can do anything with your minio buckets console. \nEnter number of the action you want to do :")

print(Fore.LIGHTCYAN_EX + f"\n1.Total buckets\n2.Create buckets\n3.Delete buckets\n4.Update buckets\n"+ Style.RESET_ALL)


def switch(x):
    if x == 1:
        print(Fore.LIGHTYELLOW_EX + f"Total buckets: ", len(client.list_buckets()) + Style.RESET_ALL)




client_input = int(input())