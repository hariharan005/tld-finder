import os
import csv
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from banner import main_banner, sub_banner, tld_banner

# Global session for connection reuse
session = requests.Session()

# Max concurrent threads
MAX_THREADS = 20

# Delay after each batch to avoid getting blocked
BATCH_SLEEP_SECONDS = 2

# Number of domains to process before sleeping
BATCH_SIZE = 20

def main():
    main_banner()
    option = input("\nEnter the number: ")

    if option == '1':
        os.system('clear')
        tld_banner()
        tld()
    elif option == '2':
        os.system('clear')
        sub_banner()
        subdomain()
    else:
        print("Select 1 or 2")

def check_tld(domain, tld):
    url = f"https://{domain}{tld}"
    try:
        response = session.get(url, allow_redirects=False, timeout=3)
        status_code = response.status_code
        print(f"{url} <------  [ {status_code} ]")
        return f"{domain}{tld}"
    except Exception:
        print(f"{url} <------  [ ERROR ]")
        return None

def tld():
    domain = input("\nEnter Domain: ").strip()

    # Load all TLDs
    with open('alltld.csv', 'r') as file:
        csvreader = csv.reader(file)
        tlds = [line[0] for line in csvreader]

    valid_domains = []  # Store successful domains to write later

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for i, tld in enumerate(tlds):
            futures.append(executor.submit(check_tld, domain, tld))

            # Batch processing for rate limiting
            if (i + 1) % BATCH_SIZE == 0:
                time.sleep(BATCH_SLEEP_SECONDS)

        # Collect results
        for future in as_completed(futures):
            result = future.result()
            if result:
                valid_domains.append(result)

    # Write valid domains to file
    if valid_domains:
        with open(f"{domain}.txt", 'a+') as f:
            f.write('\n'.join(valid_domains) + '\n')
        print(f"\n✅ Saved {len(valid_domains)} valid domains to {domain}.txt")
    else:
        print("\n⚠️ No valid domains found.")

def subdomain():
    print("2 is chosen")

if __name__ == "__main__":
    main()
