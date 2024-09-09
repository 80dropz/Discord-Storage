from discord_webhook import DiscordWebhook
import random
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import time
def main():

    root = Tk()
    root.withdraw()


    code = random.randint(1000, 9999)


    webhook_url = input("Paste your Discord webhook: ").strip()


    webhook = DiscordWebhook(url=webhook_url, content=f"Your verification code is: {code}")
    webhook.execute()


    verification_checker = input("Enter the verification code: ").strip()

    directory = askdirectory(title="Select Directory")

    if str(code) == verification_checker:
        config_path = "config.txt"
        with open(config_path, "w") as config_file:
            config_file.write(f"Webhook: {webhook_url}\n")
            config_file.write(f"Directory: {directory}\n")
        print("Config saved!")
        verification_webhook = DiscordWebhook(url=webhook_url, content="Webhook verified :white_check_mark:")
        verification_webhook.execute()
        webhook.delete()
        time.sleep(5)
        verification_webhook.delete()
    else:
        print("Invalid verification code")
        failure_webhook = DiscordWebhook(url=webhook_url, content="Webhook not verified :x:")
        failure_webhook.execute()
        time.sleep(5)
        failure_webhook.delete()
    input("Press Enter to exit")

if __name__ == "__main__":
    main()
