import re
import yaml
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class ResourceNamePatternCheck(BaseResourceCheck):
    def __init__(self, config_file):
        print("12345")
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
            
        name = "Ensure resource names match the specified regex pattern"
        id = "SUV_TF_AZ_NAMING"
        supported_resources = [config['SUV_TF_AZ_NAMING']['supported_resources']]
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
        self.name_pattern = re.compile(config['SUV_TF_AZ_NAMING']['regex_pattern'])

    def scan_resource_conf(self, conf):
        """
        Validate resource name against the regex pattern
        """
        if "name" in conf:
            resource_name = conf["name"][0]
            if not self.name_pattern.match(resource_name):
                return CheckResult.FAILED
        return CheckResult.PASSED


check = ResourceNamePatternCheck()