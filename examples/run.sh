
checkov -d ./terraform/azure  --external-checks-dir ./custom-policies --skip-path ./custom-policies/config.yaml
