import re
from nltk import pos_tag, word_tokenize
import re
def custom_pos_tag(sentence, custom_tags,target_tags):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]+\b'
    username_pattern = r'username\s+([^\s]+)'
    password_pattern = r'password\s+([^\s]+)'
    name_pattern = r'name\s+([^\s]+)'
    vmname_pattern = r'vmname\s+([^\s]+)'
    ip_matches = re.findall(ip_pattern, sentence)
    for ip_match in ip_matches:
        custom_tags[ip_match] = 'NN'

    sentence = sentence.lower()
    ip_matches = re.findall(ip_pattern, sentence)
    for ip_match in ip_matches:
        custom_tags[ip_match] = 'NN'
        
        
    allNames = re.findall(name_pattern,sentence)
    for name in allNames:
        custom_tags[name] = "NN"
    
    allNames = re.findall(vmname_pattern,sentence)
    for name in allNames:
        custom_tags[name] = "NN"
        
    
    for w in sentence:
      if w in region_names_with_spaces.keys():
        reg = region_names_with_spaces[w]
        w = str(re.sub(r'\s', '', reg.lower()))
        
    print(sentence)
    tokens = str.split(sentence)
    pos_tags = pos_tag(tokens)


    # Replace specific words with custom POS tags
    specific_tags = [(word, tag) for word, tag in pos_tags if tag in target_tags and word != 'name']
    pos_tags = [(word, custom_tags.get(word, tag)) for word, tag in pos_tags
                if tag in target_tags or custom_tags.get(word, tag) in target_tags
               ]
    return pos_tags,

# Example usage:
sentence = "deploy me a "
target_tags = ['VB', 'NN', 'NNP']
custom_tags = {'virtual-machine': 'NN',
               'virtual-network': 'NN',
               'subnet': 'NN',
               'subnetwork': 'NN',
               'virtual-subnet': 'NN',
               'rg': 'NN',
               'resource-group': 'NN',
               'nic': 'NN',
               'public-ip':'NN',
               'pip':'NN',
               'network-interface-card': 'NN',
               'name':'NN',
               'vnet':'NN',
               'v-net':'NN',
               'specifications':'NN',
               'configs':'NN',
               'configurations':'NN',
               'specs':'NN',
               'us-east':'NN',
               'us-east-2':'NN',
               'us-east-3':'NN',
               'address_space':'NN',
               'address-space':'NN',
               'Linux':'NN',
               'linux':'NN',
               'redhat':'NN',
               'RedHat':'NN',
               'CentOS':'NN',
               'centos':'NN',
               'suse':'NN',
               'Suse-linux':'NN',
               'SUSE':'NN',
               'vmname':'NN',
              }


region_names_with_spaces = {
    'east-us': 'East US',
    'west-us': 'West US',
    'north-central-us': 'North Central US',
    'south-central-us': 'South Central US',
    'central-us': 'Central US',
    'east-us-2': 'East US 2',
    'west-us-2': 'West US 2',
    'canada-central': 'Canada Central',
    'canada-east': 'Canada East',
    'north-europe': 'North Europe',
    'west-europe': 'West Europe',
    'uk-south': 'UK South',
    'uk-west': 'UK West',
    'france-central': 'France Central',
    'france-south': 'France South',
    'germany-central': 'Germany Central',
    'germany-northeast': 'Germany Northeast',
    'east-asia': 'East Asia',
    'southeast-asia': 'Southeast Asia',
    'australia-east': 'Australia East',
    'australia-southeast': 'Australia Southeast',
    'japan-east': 'Japan East',
    'japan-west': 'Japan West',
    'korea-central': 'Korea Central',
    'korea-south': 'Korea South',
    'south-africa-north': 'South Africa North',
    'south-africa-west': 'South Africa West',
    'brazil-south': 'Brazil South',
    'central-india': 'Central India',
    'south-india': 'South India',
    'west-india': 'West India'
}

pos_tags = custom_pos_tag(sentence, custom_tags,target_tags)

print(pos_tags[0])

level = 0

resources_order = {"resource-group":1,
                    "vnet":2,
                    "subnet":3,
                    "nsg":4,
                    "publicip":5,
                    "nic":6,
                    "vm":7}

level = 0

for resources in pos_tags[0]:
    if resources[0] in resources_order.keys() and  level < resources_order[resources[0]]:
        level = resources_order[resources[0]]
print(level)


template  = ""


from provisions import provisionResourceGroup,provisionVnet,provisionSubnet,provisionNsg,provisionPublicIp,provisionNic,provisionVM

resList = []

for resource in pos_tags[0]:
    if resource[0] != 'name' and resource[0] != 'specs':
        resList.append(resource)
print(resList)

totalNoOfResources = len(resList)

if level == 1:
    template = provisionResourceGroup(resList,totalNoOfResources)

elif level == 2:
    template = provisionVnet(resList,totalNoOfResources)

elif level == 3:
    template = provisionSubnet(resList,totalNoOfResources)

elif level == 4:
    template = provisionNsg(resList,totalNoOfResources)
    
elif level == 5:
    template = provisionPublicIp(resList,totalNoOfResources)

elif level == 6:
    template = provisionNic(resList,totalNoOfResources)
    
elif level == 7:
    template = provisionVM(resList,totalNoOfResources)
    
print(template)

