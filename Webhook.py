import requests
import time
from pystyle import Colorate, Colors

ascii_art = """

 /$$$$$$$$ /$$    /$$  /$$$$$$         /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$ /$$      /$$ /$$$$$$$$ /$$$$$$$       
|__  $$__/| $$   | $$ /$$__  $$       /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$| $$$    /$$$| $$_____/| $$__  $$      
   | $$   | $$   | $$| $$  \__/      | $$  \__/| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$$$  /$$$$| $$      | $$  \ $$      
   | $$   |  $$ / $$/| $$            |  $$$$$$ | $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$ $$/$$ $$| $$$$$   | $$$$$$$/      
   | $$    \  $$ $$/ | $$             \____  $$| $$____/ | $$__  $$| $$  $$$| $$| $$  $$$| $$| $$__/   | $$__  $$      
   | $$     \  $$$/  | $$    $$       /$$  \ $$| $$      | $$  | $$| $$\  $ | $$| $$\  $ | $$| $$      | $$  \ $$      
   | $$      \  $/   |  $$$$$$/      |  $$$$$$/| $$      | $$  | $$| $$ \/  | $$| $$ \/  | $$| $$$$$$$$| $$  | $$      
   |__/       \_/     \______/        \______/ |__/      |__/  |__/|__/     |__/|__/     |__/|________/|__/  |__/      
                                                                                                                       
                                                                                                                       
                                                                                                                       

"""

print(Colorate.Vertical(Colors.red_to_blue, ascii_art))

def send_discord_message(webhook_url, name, message):
    payload = {
        "content": message,
        "username": name
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print("[>] Sent Message")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    webhook_urls = input("[>] Enter the webhook URLs separated by comma: ").split(',')
    webhook_name = input("[>] Enter the new name for the webhook: ")
    message = input("[>] Enter the message to send: ")

    try:
        while True:
            for url in webhook_urls:
                send_discord_message(url.strip(), webhook_name, message)
             time.sleep(0.5)
    except KeyboardInterrupt:
        print("[>] Keyboard Interrupt. Goodbye! :D")
