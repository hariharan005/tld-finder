#This includes the libraries need for this project
import os
import csv
import requests
from banner import main_banner, sub_banner, tld_banner

"""This is the main function use to call first and get the input from the user to select which feature should use, 
 if the user wants to use the Top level domain finder then he/she should enter the option 1 or the user wants to use
 the subdomain finder then he/she should enter the option 2 """                                                                                                                                                 
def main():
    main_banner()

    option = input("\nEnter the number: ")

    if option == '1':
        os.system('clear')
        tld_banner()
        tld()
    elif option =='2':
        os.system('clear')
        sub_banner()
        subdomain()
    else:
        print("Select 1 or 2")
    
def tld():
    domain = input("\nEnter Domain: ") #get the domain from the user
    
    with open('alltld.csv', 'r') as file:
        csvreader = csv.reader(file)
        for line in csvreader:
            tld = line[0]
            url = f"https://{domain}{tld}"
            print(url)
            
            try:
                r = requests.get(url, allow_redirects=False)
                stscode = r.status_code
                stat = f"{url} <------  [ {stscode} ]"
                tlddomain = f"{domain}{tld}"
                print(stat)
                
                with open(f"{domain}.txt", 'a+') as f:
                    f.write(tlddomain + '\n')
            except Exception:
                print("URL NOT FOUND\n")
    
def subdomain():
    print("2 is chosen")
    
    
if __name__ == "__main__":
    main()