import os
import subprocess
import ipinfo

def run_infoga(email):
    subprocess.run(['python', 'Infoga/infoga.py', '--info', email])

def run_ipinfo(ip_address):
    access_token = 'YOUR_IPINFO_ACCESS_TOKEN'  # Reemplaza con tu token de acceso
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    print(details.all)

def run_sherlock(username):
    subprocess.run(['python', 'sherlock/sherlock.py', username])

if __name__ == '__main__':
    email = 'example@example.com'
    ip_address = '8.8.8.8'
    username = 'exampleuser'

    print("Running Infoga...")
    run_infoga(email)

    print("\nRunning IPinfo...")
    run_ipinfo(ip_address)

    print("\nRunning Sherlock...")
    run_sherlock(username)
