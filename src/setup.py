from setuptools import setup, find_packages
files = ["config.yaml"]
setup(
    name="suvorin",
    version="0.1",
    packages=find_packages(),
    package_data={'suvorin': files},
    install_requires=[
        "checkov",
    ],
    entry_points={
        'checkov.custom.checks': [
            'SUV_TF_AZ_VM_001=suvorin.SUV_TF_AZ_VM_001:PasswordAuthenticationDisabled',
        ],
    },
)
