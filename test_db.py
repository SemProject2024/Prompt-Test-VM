
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('test-prompt-vm-firebase-adminsdk-gyfhc-f421a767db.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection("Users").document('Template')
users_ref = users_ref.collection('resource "azurerm_virtual_network" "main" {')
docs = users_ref.stream()
dic1 = {}
template_code = ""
for doc in docs:
    dic1 = doc.to_dict()
    for x,y in dic1.items():
        
        if x == "name                = ":
            y = "vnet-modified"
        
        template_code +=x
        template_code+=y
        template_code+="\n"
        
print(template_code)
with open("hi.txt","w") as file:
    file.write(template_code)
    
# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")
