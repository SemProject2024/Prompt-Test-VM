import cachegen
def provisionResourceGroup(resList,totalNoOfResources):
    print('Initated Provisioning Resource Group...')
    template = cachegen.provisionResourceGroup(resList,totalNoOfResources)
    return template


def provisionVnet(resList,totalNoOfResources):
    print('Initated Provisioning Virtual Network...')
    resourceGroupTemplate = provisionResourceGroup(resList,totalNoOfResources)
    vNetTemplate = cachegen.provisionVnet(resList,totalNoOfResources)
    template = resourceGroupTemplate + vNetTemplate
    return template


def provisionSubnet(resList,totalNoOfResources):
    vNetTemplate = provisionVnet(resList,totalNoOfResources)
    subnetTemplate = cachegen.provisionSubnet(resList,totalNoOfResources)
    template = vNetTemplate + subnetTemplate
    print('Initated Provisioning Subnet...')
    
    
    return template

def provisionNsg(resList,totalNoOfResources):
    subnetTemplate = provisionSubnet(resList,totalNoOfResources)
    nsgTemplate = cachegen.provisionNsg(resList,totalNoOfResources)
    template = subnetTemplate + nsgTemplate
    print('Initated Provisioning Provision NSG...')
    return template


def provisionVM(resList,totalNoOfResources):
    nsgTemplate = provisionNsg(resList,totalNoOfResources)
    vmTemplate = cachegen.provisionVM(resList,totalNoOfResources)
    template = nsgTemplate + vmTemplate
    
    print('Initated Provisioning VM...')
    
    
    
    return template

def provisionPublicIp(resList,totalNoOfResources):
    template4 = provisionNsg(resList,totalNoOfResources)
    print('Initated Provisioning Public IP...')
    
    
    
    return None

def provisionNic(resList,totalNoOfResources):
    template5 = provisionPublicIp(resList,totalNoOfResources)
    print('Initated Provisioning NIC...')
    
    
    
    return None
