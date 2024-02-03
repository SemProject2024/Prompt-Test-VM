import csv
import random
code = """
resource "azurerm_resource_group" "example" {
    name=""
    location = "EastUS"
}

"""

# Sample text data
text_data = [["prompt","code"]
]
from faker import Faker
fake = Faker()
for i in range(1000):
    
    
    
    

    #nn = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    nn = fake.city()
    reg = random.choice(['EastUS','WestUS','NorthCentralUS','SouthCentralUS','EastUS2'])

    prompt = "provision me a rg with name "+nn+" in location "+reg
    
    code = """
resource "azurerm_resource_group" "example" {
    name=\""""+nn+"""\"
    location =\""""+reg +"""\"
}
"""
    arr = [prompt,code]
    text_data.append(arr)



csv_file_path = "resource_group.csv"

# Open the CSV file in write mode and specify newline='' to ensure consistent line endings
with open(csv_file_path, mode='a', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)
    
    # Write the text data to the CSV file
    csv_writer.writerows(text_data)

print(f"Data has been saved to {csv_file_path}")
