from setuptools import setup, find_packages

setup(
    name="suvorin",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "checkov",
    ],
    entry_points={
        'checkov.custom.checks': [
            'SUV_TF_AZ_VM_001 = suvorin.SUV_TF_AZ_VM_001:PasswordAuthenticationDisabled',            
        ],
    },
)
