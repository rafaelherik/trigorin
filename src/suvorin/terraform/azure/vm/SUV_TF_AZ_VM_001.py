from __future__ import annotations
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class PasswordAuthenticationDisabled(BaseResourceCheck):

    def __init__(self):
        name = "Ensure that password authentication is disabled for Azure Linux VMs"
        id = "SUV_TF_AZ_VM_001"
        supported_resources = [
            'azurerm_linux_virtual_machine_scale_set',
            'azurerm_linux_virtual_machine',
            "azurerm_virtual_machine"]
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'os_profile_linux_config' in conf:
            os_profile_linux_config = conf['os_profile_linux_config'][0]
            if 'disable_password_authentication' in os_profile_linux_config:
                data = os_profile_linux_config['disable_password_authentication']
                if data == [False]:
                    return CheckResult.FAILED
        return CheckResult.PASSED


check = PasswordAuthenticationDisabled()
