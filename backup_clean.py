import subprocess
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

date = datetime.datetime.now()
rar_name = date.strftime("%d-%m-%Y")+"Archive"+date.strftime("%H-%M")+".rar"
rar = r"rar a \\ip\path\{n} \\ip\path\archived".format(n=rar_name)  # Use Network Path or Absolute
cp = r"copy \\ip\path\{n} \\destination\Save".format(n=rar_name)  # Use Network Path or Absolute
dellog = r"del /q /s /f /a \\ip\path\archived\*"  # Use Network Path or Absolute
delrar = r"del /q /s /f /a \\ip\path\*.rar"  # Use Network Path or Absolute
tabcom = [rar, cp, dellog, delrar]


def mail0(txt):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # This for Gmail
    server.ehlo()
    server.login('sender_email', 'password***')
    toaddr = ['receiver_email1', 'receiver_email2']
    cc = ['receiver_email in Cc']
    msg = MIMEMultipart()
    msg['From'] = 'OBJECT OF MAIL'
    msg['to'] = 'receiver_email'
    msg['Cc'] = ','.join(cc)
    msg['Subject'] = 'Backup Logs Report'
    message = f"Backup Logs Report \n" + txt + "\n Cordially"
    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    server.sendmail('sender_email', toaddr, text)
    server.quit()


def option0():
    global tabcom
    for t in tabcom:
        try:
            com = subprocess.run(t, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            res = com.stdout
            if ("Cannot open" in res) or ("The specified file can not be found." in res):
                mail0(str(res))
        except:
            mail0(f"Error \n {str(res)}")
    mail0("Well Done")


option0()

