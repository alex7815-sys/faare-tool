import requests
import time  # Import time module for sleep function
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

# Example usage
if __name__ == '__main__':
    # Replace these values with actual Facebook account URL, reason for reporting, and number of reports
    account_url = 'https://www.facebook.com/example_account'
    reason_for_reporting = 'This account is posting harmful content.'
    num_reports = 100  # Number of times to report the account

    report_facebook_account(account_url, reason_for_reporting, num_reports)
