import requests
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def report_facebook_account(account_url, reason, num_reports=1):
    report_url = 'https://www.facebook.com/help/contact/1448613805579647'
    data = {
        'url': account_url,
        'reason': reason,
        # Add other required fields based on Facebook's reporting form
    }

    try:
        for i in range(num_reports):
            response = requests.post(report_url, data=data)
            if response.status_code == 200:
                logging.info(f"Report {i+1}/{num_reports} submitted successfully.")
            else:
                logging.error(f"Failed to submit report {i+1}. Status code: {response.status_code}")
            
            time.sleep(1)  # Introduce a 1-second delay between requests to avoid rate limiting

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    try:
        account_url = input("Enter the Facebook account URL to report: ")
        reason_for_reporting = input("Enter the reason for reporting: ")
        num_reports = int(input("Enter the number of times to report the account (default is 1): ") or 1)

        report_facebook_account(account_url, reason_for_reporting, num_reports)

    except ValueError:
        logging.error("Invalid input. Please enter a valid number for the number of reports.")

    except KeyboardInterrupt:
        logging.info("Reporting process interrupted by user.")

    except Exception as ex:
        logging.error(f"Unexpected error: {ex}")
