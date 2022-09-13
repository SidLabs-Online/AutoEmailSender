import smtplib
import config
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_data = pd.read_csv("path to your csv file")
email_list = email_data["email"]

def send_email(content, to_email):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        # Sender's credentials are fed in from the config.py file
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = content.as_string()
        server.sendmail(config.EMAIL_ADDRESS, to_email, message)
        server.quit()
        print("Email Sending Complete: \nYour email has been sent to:\n>", to_email, "successfully.")
    except:
        print("Email Sending Error: \n Email failed to the email address: \n>", to_email, " .")

msg = MIMEMultipart()
# storing data into the parts of the message to be sent
msg['From'] = config.EMAIL_ADDRESS
msg['Subject'] = "This is a test mail from SidLabs"
# MIMEText is used to code in HTML structures within the body of the message
body = MIMEText(
    '<HTML><body><h2> Hello !\n</h2>' +
    '<h2> This is an email sender application. </h2>' +
    '<h3> Thank you!!! </h3>' +
    '</body></html>', 'html', 'utf-8'
)
msg.attach(body)

for i in range(0, 100):
    try:
        send_email(msg, str((email_list[i])))
        i = +1
    except:
        print("\n> The app has reached till the end of the list,"
              "\n> There are no more email addresses in this list."
              "\n> ~~~~~~~ This task is done~~~~~~!")
        quit()