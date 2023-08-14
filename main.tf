terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=2.7"
    }
  }
}
provider "azurerm"{
features {}
skip_provider_registration = "true"
subscription_id = ""
tenant_id = ""
client_id = ""
client_secret=""
}

#Creating Resource Group name - test-rg-2 this is modified by me

resource "azurerm_resource_group" "rg" {
    name="test-rg-2"
    location = "EastUS"
  
}