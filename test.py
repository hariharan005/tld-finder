#This includes the libraries need for this project
import os
import csv
import requests

"""This is the main function use to call first and get the input from the user to select which feature should use, 
 if the user wants to use the Top level domain finder then he/she should enter the option 1 or the user wants to use
 the subdomain finder then he/she should enter the option 2 """
 
 
def tld_banner():
    print("  _______ _     _      ______ _           _                           ")
    print(" |__   __| |   | |    |  ____(_)         | |                          ")
    print("    | |  | | __| |    | |__   _ _ __   __| | ___ _ __                 ")
    print("    | |  | |/ _` |    |  __| | | '_ \ / _` |/ _ \ '__|                ")
    print("    | |  | | (_| |    | |    | | | | | (_| |  __/ |                   ")
    print("    |_|  |_|\__,_|    |_|    |_|_| |_|\__,_|\___|_|                   ")
                                                    
                                                   
def sub_banner():
    print("   _____       _          ______ _           _                          ")
    print("  / ____|     | |        |  ____(_)         | |                         ")
    print(" | (___  _   _| |__      | |__   _ _ __   __| | ___ _ __                ")
    print("  \___ \| | | | '_ \     |  __| | | '_ \ / _` |/ _ \ '__|               ")
    print("  ____) | |_| | |_) |    | |    | | | | | (_| |  __/ |                  ")
    print(" |_____/ \__,_|_.__/     |_|    |_|_| |_|\__,_|\___|_|                  ")
                                                       
                                                      
def main():
    print("          _ _      ______ _           _                                  ")
    print("    /\   | | |    |  ____(_)         | |                                 ")
    print("   /  \  | | |    | |__   _ _ __   __| | ___ _ __                        ")
    print("  / /\ \ | | |    |  __| | | '_ \ / _` |/ _ \ '__|                       ")
    print(" / ____ \| | |    | |    | | | | | (_| |  __/ |                          ")
    print("/_/    \_\_|_|    |_|    |_|_| |_|\__,_|\___|_|                          ")
                                                
                                                

    print("\nOptions:")
    print("1. TLD Finder (Top Level Domain )")
    print("2. Subdomain Finder")

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
                print(stat)
                
                with open(f"{domain}.txt", 'a+') as f:
                    f.write(stat + '\n')
            except Exception:
                print("URL NOT FOUND")
    
def subdomain():
    print("2 is chosen")
    
    
if __name__ == "__main__":
    main()