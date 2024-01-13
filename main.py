import os
import requests

print(
    "Welcome to Michael's Flight Club.\nWe find the best flight deals and email you."
)
first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()

email = "email1"
email_check = "email2"

while email != email_check:
  email = input("What is your email?\n").lower()
  if email.lower() == "exit":
    exit()
  email_check = input("Type your email again.\n").lower()
  if email_check.lower() == "exit":
    exit()
print("You're in the club!")

sheety_headers = {"Authorization": os.environ['SHEETY_TOKEN']}
sheety_config = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}
response = requests.post(url=os.environ['SHEETY_ENDPOINT'],
                         headers=sheety_headers,
                         json=sheety_config)
print(response.text)
