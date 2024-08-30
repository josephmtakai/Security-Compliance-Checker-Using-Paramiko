# Security Compliance Checker

This project automates the process of checking security compliance on remote servers using SSH. It connects to specified servers, runs predefined commands, and generates compliance reports.

## Features

- **Automated Compliance Checking:** Runs security checks on remote servers automatically.
- **Customizable Checks:** Easily add or modify checks using the `compliance_checks.yaml` file.
- **Detailed Reporting:** Generates reports for each server, summarizing the compliance status.

## Project Structure

```plaintext
Security Compliance Checker/
│
├── compliance_checker.py    # Main Python script
├── servers.yaml             # List of servers to check
├── compliance_checks.yaml   # Definitions of compliance checks
└── reports/                 # Directory for saving reports


Requirements
Python 3.x
Required Python packages: paramiko, pyyaml
To install the required packages, run:

Copy code
pip install paramiko pyyaml
Setup
Clone the Repository:

Copy code
git clone https://github.com/yourusername/security-compliance-checker.git
cd security-compliance-checker
Configure Servers:

Edit the servers.yaml file to list the servers you want to check.

Define Compliance Checks:

Edit the compliance_checks.yaml file to define the security checks you want to perform.

Run the Compliance Checker:

Execute the script to check compliance on all listed servers:

Copy code
python compliance_checker.py
Output
Compliance reports are generated in the reports/ directory, one for each server.

Contributing
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

This README provides clear guidance on how to set up, configure, and use the Security Compliance Checker.
