
![](/.assets/images/logo.png)

# Trigorin IaaC policies for Checkov

![Build Status](https://github.com/rafaelherik/trigorin/actions/workflows/build.yml/badge.svg)


This python package is a useful implementention to help to create custom policies to Checkov.

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

## Why Trigorin?

The name "Trigorin" is inspired by the intricate character from Chekhov's "The Seagull," symbolizing our project's dedication to enhancing and extending the functionalities of Checkov. Just as Trigorin, with his depth and complexity, adds layers of meaning to Chekhov's work, the goal of this repo is to provide innovative solutions that reinforce the security and compliance of your infrastructure.

Feel free to modify it to better fit your project's tone and vision!
