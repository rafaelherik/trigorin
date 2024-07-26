
![](/.assets/images/logo.png)

# Suvorin IaaC policies for Checkov

![Build Status](https://github.com/rafaelherik/suvorin/actions/workflows/suvorin-build.yml/badge.svg)


This python package has a set of useful custom policies to Checkov.

The objective is to add customizable policies to ensure naming conventions, resource sizing, and governance checks. This helps your infrastructure code adhere to best practices and identifies issues before code integration into your repository, preventing compliance problems at deployment time.

By implementing these policies, you reduce the effort required to manage Infrastructure as Code (IaC) and improve the maintainability and reliability of your systems.


## Preparing development environment

 - Create a Python Virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```
 - Install the requirements

```bash
pip install -r requirements.txt
```


## Why Suvorin?

The name "Suvorin" is inspired by the deep friendship between Suvorin and Checkov, symbolizing our project's commitment to complement and augment the capabilities of Checkov. Just as Suvorin supported and enriched Checkov's work, our goal is to provide innovative policies that bolster the security and compliance of your infrastructure.

Join us in this journey to make your cloud environments more secure and resilient, with Suvorin as your steadfast companion.

Feel free to modify it to better fit your project's tone and vision!