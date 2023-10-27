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

resource "azurerm_resource_group" "example" {
    name="test-rg-2"
    location = "EastUS"
}