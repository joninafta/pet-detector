
import ConfigParser, os, smtplib
from email.Utils import COMMASPACE, formatdate
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
class email_class():
    
    def __init__(self,serviceName,configFile):
        config = ConfigParser.ConfigParser()
        fp = open(configFile)
        config.readfp(fp)
        config.sections()
              
        
        self.address = config.get(serviceName,'addr')
        self.password = config.get(serviceName,'pass')
        self.target = [config.get(serviceName,'target')]
        self.server = []
        
        fp.close()
        
    def login(self):
        self.server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.address, self.password)
        
 #   def sendText(self,messageText):
 #       self.server.sendmail(self.address, COMMASPACE.join(self.target), messageText)
        
        
    def sendMail(self,messageSubject,messageText,filesList):
        message = MIMEMultipart()
        message['Subject'] = messageSubject
        message['body'] = messageText
        for currentFile in filesList:
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(currentFile,"rb").read() )
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(currentFile))
            message.attach(part)
        self.server.sendmail(self.address, COMMASPACE.join(self.target), message.as_string())






