from colorama import Fore, Back, Style
from minio import Minio
from minio.error import S3Error
#import minio functions
import minio_functions

while True:
    print(Fore.LIGHTWHITE_EX + f"Here you can do anything with your minio buckets console. \nEnter number of the action you want to do :")
    print(Fore.LIGHTBLUE_EX + f'(Enter "quit" to exit.)')
    print(Fore.MAGENTA + f"\n1.Total buckets\n2.Create a buckets\n3.Delete a bucket\n4.Total objects of a specific bucket\n5.Upload a object\n6.Download a object\n7.Delete a Object\n"+ Style.RESET_ALL)        
    
    def switch(x):
        try:
            a = int(x)
            if a == 1:
                result = minio_functions.list_buckets()
                return result
            elif a == 2:
                result = minio_functions.create_bucket()
                return result
            elif a == 3:
                result = minio_functions.delete_bucket()
                return result
            elif a == 4:
                result = minio_functions.list_objects()
                return result
            elif a == 5:
                result = minio_functions.upload_object()
                return result
            elif a == 6:
                result = minio_functions.download_object()
                return result
            elif a == 7:
                result = minio_functions.delete_object()
                return  result
            else:
                return "Your a number should be between 1 and 7 :)"
        except ValueError:
            return "Your input is not a number :("
            
        
    client_input = input(Fore.LIGHTYELLOW_EX)
    if client_input =="quit":
                exit("Goodbye Fella :)\n" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + switch(client_input) + Style.RESET_ALL)
