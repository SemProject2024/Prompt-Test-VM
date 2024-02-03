def provisionResourceGroup(resList,totalNoOfResources):
    
    
    import datetime
    stackDetails = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) +str(datetime.datetime.now().second)
    defaultNameResourceGroup = "rg-"+stackDetails
    default_loc = "eastus"
    
    index = -1 
    for i in range(totalNoOfResources):
        if resList[i][0] == 'resource-group':
            index = i
            
    locationResourceGroup = ""
    nameResourceGroup = ""
    
    
    
    if index == -1:
        locationResourceGroup = default_loc
        nameResourceGroup = defaultNameResourceGroup
    else:
        if index+1 < totalNoOfResources:
                if index+3 < totalNoOfResources:
                    if resList[index+2][0] == 'location':
                        locationResourceGroup = resList[index+3][0]
                        nameResourceGroup = resList[index+1][0]
                    
                else:
                    if index+1 < totalNoOfResources:
                        if resList[index+1][0] == 'location': 
                            locationResourceGroup= resList[index+2][0]
                            nameResourceGroup = defaultNameResourceGroup
                        else:
                            if resList[index+1][0] != 'location':
                                nameResourceGroup = resList[index+1][0]
                                locationResourceGroup= "eastus"  
        else:
            locationResourceGroup = "eastus"
            nameResourceGroup = defaultNameResourceGroup          
    code = """
                resource "azurerm_resource_group" "example" {
                    name=\""""+nameResourceGroup+"""\"
                    location =\""""+locationResourceGroup +"""\"
                }
                """               

    return code     


def provisionVnet(resList,totalNoOfResources):
    
    nameVnet = ""
    addressSpaceVnet = ""
    defaultAdressSpaceVnet = "10.0.0.0/16"
    import datetime
    stackDetails = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) +str(datetime.datetime.now().second)
    defaultNameVnet = "vnet-"+stackDetails
    
    index = -1 
    for i in range(totalNoOfResources):
        if resList[i][0] == 'vnet':
            index = i
    
    if index == -1:
        nameVnet = defaultNameVnet
        addressSpaceVnet = defaultAdressSpaceVnet
    else:
        
        
        if index+1 < totalNoOfResources:
            if resList[index+1][0] != 'address_space' or resList[index+1][0] != 'address-space':
                nameVnet = resList[index+1][0]
                if index+3 < totalNoOfResources:
                    if resList[index+2][0] == 'address_space' or resList[index+2][0] == 'address-space':
                        addressSpaceVnet = resList[index+3][0]
                    else:
                        addressSpaceVnet = defaultAdressSpaceVnet
                        
                else:
                    addressSpaceVnet = defaultAdressSpaceVnet
            else:
                
                nameVnet = defaultNameVnet
                if index+2 < totalNoOfResources:
                    if resList[index+1][0] == 'address_space' or resList[index+1][0] == 'address-space':
                        addressSpaceVnet = resList[index+2][0]
                    else:
                        addressSpaceVnet = defaultAdressSpaceVnet
                
                
        else:
            nameVnet =defaultNameVnet
            addressSpaceVnet = "10.0.0.0/16"
            
        
    code = """
    
            resource "azurerm_virtual_network" "main" {
                name=\""""+nameVnet+"""\"
                address_space       = [\""""+addressSpaceVnet+"""\"]
                location            = azurerm_resource_group.example.location
                resource_group_name = azurerm_resource_group.example.name
}"""       
    
    
    
    
    return code


def provisionSubnet(resList,totalNoOfResources):
    import datetime
    stackDetails = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) +str(datetime.datetime.now().second)
    defaultNameSubnet = "subnet-"+stackDetails
    
    
    
    code = """
    
            resource "azurerm_subnet" "internal" {
                name                 = \""""+defaultNameSubnet+"""\"
                resource_group_name  = azurerm_resource_group.example.name
                virtual_network_name = azurerm_virtual_network.main.name
                address_prefixes     = ["10.0.2.0/24"]
}"""       
   
    
    
    
    
    return code

def provisionNsg(resList,totalNoOfResources):
    template3 = provisionSubnet(resList,totalNoOfResources)
    import datetime
    stackDetails = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) +str(datetime.datetime.now().second)
    defaultNameNsg = "nsg-"+stackDetails
    print('Initated Provisioning Provision NSG...')
    
    code  = """
            resource "azurerm_network_security_group" "example" {
                name                = \""""+defaultNameNsg+"""\"
                location            = azurerm_resource_group.example.location
                resource_group_name = azurerm_resource_group.example.name

                security_rule {
                    name                       = "test123"
                    priority                   = 100
                    direction                  = "Inbound"
                    access                     = "Allow"
                    protocol                   = "Tcp"
                    source_port_range          = "*"
                    destination_port_range     = "22"
                    source_address_prefix      = "*"
                    destination_address_prefix = "*"
                    
                }
            }
    """
    
    
    
    return code


def provisionVM(resList,totalNoOfResources):
    import datetime
    stackDetails = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) +str(datetime.datetime.now().second)
    defaultVMName = "vm-"+stackDetails
    defaultVMName = "test-vm"
    defaultPublisher = "Canonical"
    defaultOffer = "0001-com-ubuntu-server-focal"
    defaultSku = "20_04-lts"
    defaultversion   = "latest"
    defaultUserName = 'azureuser'
    defaultPassword = "P@ssword!123"
    publisher = defaultPublisher
    offer = defaultOffer
    sku = defaultSku
    version = defaultversion
    vmName = defaultVMName
    userName = defaultUserName
    password = defaultPassword
    
    
    
    for i in range(totalNoOfResources):
        if (resList[i][0]) == 'os' or resList[i][0] == 'operating-system' or resList[i][0] == 'publisher' or resList[i][0] == 'image':
            if resList[i+1][0] == 'linux':
                publisher = defaultPublisher
                offer = defaultOffer
                sku = defaultSku
                version = defaultversion
            elif resList[i+1][0] == 'redhat':
                publisher = "RedHat"
                offer = "RHEL"
                sku = "8-lvm-gen2"
                version = "latest"
            elif resList[i+1][0] == 'suse':
                publisher = "SUSE"
                offer = "sles-15-sp3"
                sku = "gen2"
                version = "latest"
        if resList[i][0] == 'vmname':
            vmName = resList[i+1][0]
        if resList[i][0] == 'username':
            userName = resList[i+1][0]
        if resList[i][0] == 'password':
            password = resList[i+1][0]
        
    code = """
    resource "azurerm_public_ip" "example" {
            name                = \""""+vmName+"""-ip\"
            resource_group_name = azurerm_resource_group.example.name
            location            = azurerm_resource_group.example.location
            allocation_method   = "Static"
        }

    resource "azurerm_network_interface" "main" {
        name                = \""""+vmName+"""-nic\"
        location            = azurerm_resource_group.example.location
        resource_group_name = azurerm_resource_group.example.name
        ip_configuration {
            name                          = "testconfiguration1"
            subnet_id                     = azurerm_subnet.internal.id
            private_ip_address_allocation = "Dynamic"
            public_ip_address_id = azurerm_public_ip.example.id
        }
    }
    resource "azurerm_virtual_machine" "main" {
        name                  = \""""+vmName+"""\"
        location              = azurerm_resource_group.example.location
        resource_group_name   = azurerm_resource_group.example.name
        network_interface_ids = [azurerm_network_interface.main.id]
        vm_size               = "Standard_B1ls"
        delete_os_disk_on_termination = true
        delete_data_disks_on_termination = true
        storage_image_reference {
            publisher = \""""+publisher+"""\"
            offer     = \""""+offer+"""\"
            sku       = \""""+sku+"""\"
            version   = \""""+version+"""\"
        }
        storage_os_disk {
            name              = \""""+vmName+"""-osdisk\"
            caching           = "ReadWrite"
            create_option     = "FromImage"
            managed_disk_type = "Standard_LRS"
        }
        os_profile {
            computer_name  = "hostname"
            admin_username = \""""+userName+"""\"	
            admin_password = \""""+password+"""\"
        }
        os_profile_linux_config {
            disable_password_authentication = false
        }
        tags = {
            Deployment = "From Test VM App"
        }
        }
        output "ip_address" {
        value = azurerm_public_ip.example.ip_address
        }
    """
    return code



def provisionPublicIp(resList,totalNoOfResources):
    template4 = provisionNsg(resList,totalNoOfResources)
    print('Initated Provisioning Public IP...')
    
    
    
    return None

def provisionNic(resList,totalNoOfResources):
    template5 = provisionPublicIp(resList,totalNoOfResources)
    print('Initated Provisioning NIC...')
    
    
    
    return None


