resource "azurerm_virtual_machine" "fail" {
    name                  = "example-vm-password"
    location              = "eastus"
    resource_group_name   = "resource_group_name"
    vm_size               = "Standard_DS2_v2"

    storage_image_reference {
        publisher = "Canonical"
        offer     = "UbuntuServer"
        sku       = "18.04-LTS"
        version   = "latest"
    }

    storage_os_disk {
        name              = "example-osdisk-password"
        caching           = "ReadWrite"
        create_option     = "FromImage"
        managed_disk_type = "Standard_LRS"
    }

    os_profile {
        computer_name  = "example-vm-password"
        admin_username = "adminuser"
        admin_password = "Password1234!"
    }

    os_profile_linux_config {
        disable_password_authentication = false
    }

    network_interface_ids = [" azurerm_network_interface.example_nic.id "]
}

resource "azurerm_virtual_machine" "pass" {
    name                  = "example-vm-ssh"
    location              = "eastus"
    resource_group_name   = "resource_group_name"
    vm_size               = "Standard_DS2_v2"

    storage_image_reference {
        publisher = "Canonical"
        offer     = "UbuntuServer"
        sku       = "18.04-LTS"
        version   = "latest"
    }

    storage_os_disk {
        name              = "example-osdisk-ssh"
        caching           = "ReadWrite"
        create_option     = "FromImage"
        managed_disk_type = "Standard_LRS"
    }

    os_profile {
        computer_name  = "example-vm-ssh"
        admin_username = "adminuser"
    }

    os_profile_linux_config {
            disable_password_authentication = true
            ssh_keys {
                path     = "/home/adminuser/.ssh/authorized_keys"
                key_data = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..."
            }
    }

    network_interface_ids = [ "azurerm_network_interface.example_nic.id" ]
}
    

    

    