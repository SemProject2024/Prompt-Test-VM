import requests,json



def fetch_all_subscriptions_details(token):
    auth = 'Bearer '+token
    url_for_all_resources = 'https://management.azure.com/subscriptions?api-version=2021-04-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_all_resources,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    
    data_dict = json.loads(response.text)
    for item in data_dict["value"]:
        name = item.get("subscriptionId")
        print(f"Subscription ID: {name}")



def fetch_all_resources_details(token):
    auth = 'Bearer '+token
    url_for_all_resources = 'https://management.azure.com/subscriptions/72a851c4-6ce9-4328-902a-1b4f3e431554/resources?api-version=2021-04-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_all_resources,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    
    data_dict = json.loads(response.text)
    for item in data_dict["value"]:
        name = item.get("name")
        item_type = item.get("type")
        location = item.get("location")
        print(f"Name: {name}, Type: {item_type}, Location: {location}")



def fetch_rg_details(token):
    auth = 'Bearer '+token
    url_for_all_resources = 'https://management.azure.com/subscriptions/72a851c4-6ce9-4328-902a-1b4f3e431554/resourcegroups?api-version=2021-04-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_all_resources,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    data_dict = json.loads(response.text)
    for item in data_dict["value"]:
        name = item.get("name")
        item_type = item.get("type")
        location = item.get("location")
        print(f"Name: {name}, Type: {item_type}, Location: {location}")
    

def fetch_vm_details(token):
    auth = 'Bearer '+token
    url_for_vm = 'https://management.azure.com/subscriptions/72a851c4-6ce9-4328-902a-1b4f3e431554/resourceGroups/test-rg-1//providers/Microsoft.Compute/virtualMachines/test-vm?api-version=2021-04-01'
    headers = {
    'Authorization':auth
    }
    response = requests.get(url_for_vm,headers=headers )
    if response.status_code == 200:
        print(response.text)
        print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")
    data_dict = json.loads(response.text)
    for key, value in data_dict.items():
        if key == "properties":
            print("Properties:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")
    