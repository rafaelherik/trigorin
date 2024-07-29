# Contributing to Suvorin

First off, thanks for taking the time to contribute! 🎉

The following is a set of guidelines for contributing to Suvorin, which is hosted in the [Suvorin Repository](https://github.com/rafaelherik/suvorin) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
   - [Reporting Bugs](#reporting-bugs)
   - [Suggesting Enhancements](#suggesting-enhancements)
   - [Submitting Pull Requests](#submitting-pull-requests)
3. [Development Workflow](#development-workflow)
   - [Setting Up the Development Environment](#setting-up-the-development-environment)
   - [Testing](#testing)
   - [Code Style](#code-style)
4. [Best Practices](#best-practices)

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [your.email@example.com].

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

- **Before submitting a bug report**, check the [issue tracker](https://github.com/rafaelherik/suvorin/issues) to see if the problem has already been reported.
- **If the problem is already reported**, add any additional information that might help reproduce the issue and add a 👍 reaction to indicate you have the same issue.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

- **Before suggesting enhancements**, check the [issue tracker](https://github.com/rafaelherik/suvorin/issues) to see if the enhancement has already been suggested.
- **If the enhancement is already suggested**, add any supporting details and a 👍 reaction to show your interest.

### Submitting Pull Requests

The following steps outline the process of submitting a pull request (PR):

1. Fork the repository and create your branch from `main`.
2. If you have added code that should be tested, add tests.
3. Ensure the test suite passes.
4. Make sure your code follows the project’s coding style.
5. Create a descriptive PR.

## Development Workflow

### Setting Up the Development Environment

To set up a local development environment, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/rafaelherik/suvorin.git
    cd suvorin
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Testing

Run the test suite to ensure everything is working correctly:

```bash
pytest
```

Make sure tests are added for new features and bug fixes.

### Code Style
Ensure your code adheres to the following style guidelines:

- Follow PEP 8 for Python code.
- Use Black for code formatting.
- Ensure code is linted with Flake8.

### Best Practices

- Write clear and descriptive commit messages.
- Keep pull requests small and focused. A pull request should only contain changes related to a single issue or feature.
- Add comments and documentation. Explain the purpose of your changes, especially in complex areas.
- Write tests. Ensure new features and bug fixes are covered by tests.
