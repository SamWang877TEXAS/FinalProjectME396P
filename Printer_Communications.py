import requests
import json
import time


def get_duet_print_progress(api_url, update_interval=5):
    """
    Monitors and prints the progress of a print on a Duet 3D printer.

    Parameters:
        api_url (str): The base URL of the Duet printer's API (e.g., "http://192.168.1.100").
        update_interval (int): Time in seconds between status updates.
    """
    try:
        while True:
            # Send a request to get the machine status
            response = requests.get(f"{api_url}/machine/status")
            if response.status_code == 200:
                data = response.json()

                # Extract print progress information
                job = data.get('job', {})
                progress = job.get('file', {}).get('completion', None)  # Completion percentage
                status = data.get('state', {}).get('status', 'unknown')  # Printer status

                # Print the progress
                if progress is not None:
                    print(f"Printer Status: {status}")
                    print(f"Print Progress: {progress:.2f}%")
                else:
                    print("No active print job.")

                # Wait for the next update
                time.sleep(update_interval)
            else:
                print(f"Error: Unable to fetch printer status (HTTP {response.status_code})")
                break
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    except Exception as e:
        print(f"Error: {e}")

def stop_duet_print(api_url):
    """
    Sends a command to stop the current print job on a Duet 3D printer.

    Parameters:
        api_url (str): The base URL of the Duet printer's API (e.g., "http://192.168.1.100").
    """
    try:
        # Send the stop command
        response = requests.post(f"{api_url}/machine/control", json={"command": "M0"})
        if response.status_code == 200:
            print("Print job stopped successfully.")
        else:
            print(f"Error: Unable to stop the print job (HTTP {response.status_code})")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
duet_api_url = "http://192.168.1.100"  # Replace with your Duet board's IP address

# Start monitoring the print progress
try:
    print("Monitoring print progress. Press Ctrl+C to stop.")
    get_duet_print_progress(duet_api_url)
except KeyboardInterrupt:
    print("\nStopping the print job...")
    stop_duet_print(duet_api_url)
