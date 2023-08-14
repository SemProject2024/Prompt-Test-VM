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
subscription_id = "72a851c4-6ce9-4328-902a-1b4f3e431554"
tenant_id = "f2a009da-b491-4dbb-94e8-5809162549cd"
client_id = "9e46e6ee-df6f-438d-bf40-6dbfa737777c"
client_secret="szF8Q~xjzDW2_IFD0yyaOZE_SjkvX8TysLW86c8T"
}

resource "azurerm_resource_group" "rg" {
    name="test-rg-2"
    location = "EastUS"
  
}