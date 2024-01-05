#Documentation to setup gmail for app password 
#https://support.google.com/accounts/answer/185833?hl=en-GB
#See also: 
#https://realpython.com/python-send-email/
#option-1-setting-up-a-gmail-account-for-development

import smtplib, ssl

class EmailNotification:
    """Sends email notification to specified email adress from a specified email""" 

    def __init__ (self, email):
        """Initializes set values"""

        self.port = 465
        self.password = "" #setup your own passoword, documented above
        self.smtp_server = "smtp.gmail.com"
        self.fromEmail = "" #put your own personal email
        self.toEmail = email

    def sendEmail(self, message):
        """Sends email using smtplib, ssl"""

        self.context = ssl.create_default_context()
        self.message = message
        

        with smtplib.SMTP_SSL(self.smtp_server, self.port, self.context == self.context) as server: 
            server.login(self.fromEmail, self.password)
            server.sendmail(self.fromEmail, self.toEmail, self.message)
        