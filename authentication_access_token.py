import requests,json
tenant_id = ''
client_id = ''
client_secret = ''
resource_url = 'https://management.azure.com'
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'

token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'resource': resource_url
}


token_response = requests.post(token_url, data=token_data)
token = token_response.json().get('access_token')
if not token:
    print('Failed to get token')

def fetch_all_subscriptions():
    from fetch_resources import fetch_all_subscriptions_details
    print("Fetching All Subscriptions")
    fetch_all_subscriptions_details(token=token)
    print("\n\n\n ")

def fetch_all_resources():
    from fetch_resources import fetch_all_resources_details
    print("Fetching All Resources")
    fetch_all_resources_details(token)
    print("\n\n\n ")

def fetch_vm_resources():
    from fetch_resources import fetch_vm_details
    print("Fetching VM Resources")
    fetch_vm_details(token)
    print("\n\n\n ")
    
def fetch_rg_resources():
    from fetch_resources import fetch_rg_details
    print("Fetching Resource Group Resources")
    fetch_rg_details(token=token)
    print("\n\n\n ")
    

fetch_all_subscriptions()
fetch_vm_resources()
fetch_all_resources()
fetch_rg_resources()
