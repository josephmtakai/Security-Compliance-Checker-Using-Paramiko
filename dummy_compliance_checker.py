import os
from datetime import datetime

# Function to generate a dummy compliance report
def generate_dummy_report(server_name, ip_address):
    compliance_items = [
        "Firewall is active",
        "SSH protocol is version 2",
        "Root login is disabled",
        "All packages are up to date",
        "Strong password policy is enforced",
        "SELinux is enabled",
        "Antivirus is installed and up to date",
    ]

    # Simulate compliance check results
    results = [("PASS" if i % 2 == 0 else "FAIL") for i in range(len(compliance_items))]

    # Create the report content
    report_content = f"Compliance Report for {server_name} ({ip_address})\n"
    report_content += f"Generated on: {datetime.now()}\n\n"
    report_content += "Item                                    Status\n"
    report_content += "-" * 50 + "\n"

    for item, result in zip(compliance_items, results):
        report_content += f"{item:<40} {result}\n"

    # Save the report to the reports directory
    if not os.path.exists("reports"):
        os.makedirs("reports")

    report_filename = f"reports/{ip_address}_compliance_report.txt"
    with open(report_filename, "w") as report_file:
        report_file.write(report_content)
    
    print(f"Dummy report generated: {report_filename}")

# List of dummy servers to generate reports for
servers = [
    {"name": "Web Server 1", "ip": "172.168.16.2"},
    {"name": "Database Server 1", "ip": "172.168.16.3"},
    {"name": "App Server 1", "ip": "172.168.16.4"},
    {"name": "Load Balancer 1", "ip": "172.168.16.5"},
]

# Generate dummy reports for each server
for server in servers:
    generate_dummy_report(server["name"], server["ip"])
