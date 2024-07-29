import unittest
from pathlib import Path

from checkov.runner_filter import RunnerFilter
from checkov.terraform.runner import Runner

from suvorin.terraform.azure.vm.SUV_TF_AZ_VM_001 import check
from suvorin.config_loader import ConfigLoader


class TestPasswordAuthenticationDisabled(unittest.TestCase):
     def test(self):        

        print("Running the test for PasswordAuthenticationDisabled.")
        test_files_dir = Path(__file__).parent / "example_SUV_TF_AZ_VM_001"
        
        # when
        report = Runner().run(root_folder=str(test_files_dir), runner_filter=RunnerFilter(checks=[check.id]))

        # then
        summary = report.get_summary()

        passing_resources = {
            "azurerm_virtual_machine.pass",
        }

        failing_resources = {
            "azurerm_virtual_machine.fail",
        }

        passed_check_resources = {c.resource for c in report.passed_checks}
        failed_check_resources = {c.resource for c in report.failed_checks}

        print(f"{failed_check_resources}")
        
        print(f"{report.print_json()}")


        print(f"summary: {summary}")

        self.assertEqual(summary["passed"], len(passing_resources))
        self.assertEqual(summary["failed"], len(failing_resources))
        self.assertEqual(summary["skipped"], 0)
        self.assertEqual(summary["parsing_errors"], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)
        
if __name__ == '__main__':
    print("Running the test cases.")
    unittest.main()
