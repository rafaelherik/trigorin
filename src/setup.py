from setuptools import setup, find_packages
files = ["config.yaml"]
setup(
    name="trigorin",
    version="0.1",
    packages=find_packages(),
    package_data={'trigorin': files},
    install_requires=[
        "checkov",
    ],
    entry_points={
        'checkov.custom.checks': [
            'TRI_TF_AZ_VM_001=trigorin.TRI_TF_AZ_VM_001:PasswordAuthenticationDisabled',
        ],
    },
)
