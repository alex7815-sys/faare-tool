import requests
import time  # Import time module for sleep function
import sys  # Import sys for command-line arguments
from bs4 import BeautifulSoup

def report_facebook_account(account_url, reason, num_reports=1):
    # Replace with actual Facebook reporting URL and form data
    report_url = 'https://www.facebook.com/help/contact/1448613805579647'

    # Example form data (replace with actual fields based on Facebook's form)
    data = {
        'url': account_url,
        'reason': reason,
        # Add other required fields based on Facebook's reporting form
    }

    try:
        for i in range(num_reports):
            # Send POST request to submit the report
            response = requests.post(report_url, data=data)

            # Check response status
            if response.status_code == 200:
                print(f"Report {i+1} submitted successfully.")
            else:
                print(f"Failed to submit report {i+1}. Status code: {response.status_code}")

            # Introduce a delay between requests (optional but recommended to avoid rate limiting or blocking)
            time.sleep(1)  # Sleep for 1 second between requests

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Main block to accept command-line arguments
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 report_tool.py <account_url> <reason_for_reporting> <num_reports>")
        sys.exit(1)

    account_url = sys.argv[1]
    reason_for_reporting = sys.argv[2]
    num_reports = int(sys.argv[3])

    report_facebook_account(account_url, reason_for_reporting, num_reports)
