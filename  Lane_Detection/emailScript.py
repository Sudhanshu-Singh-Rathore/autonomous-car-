#Note: enable "less secure apps" on Gmail before running the code
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

email='viditpathak14@gmail.com'
password='vidit14p'
receiver='vidit.amarnath.15cse@bml.edu.in'

msg=MIMEMultipart()  #creating an object

msg['From']= email
msg['To']= receiver
msg['Subject']= 'Python Test email'

body='Test email sent form python'
msg.attach(MIMEText(body,'plain'))

filename="Test.txt"   #name of attachment
attachment=open('/home/vidit/Desktop/Test.txt','rb') #path of attachment

part=MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename=%s'%filename)

msg.attach(part)

mail= smtplib.SMTP('smtp.gmail.com:587')

mail.ehlo()     #Identify user to the server
mail.starttls() #To encrypt all SMTP commands TLS:Transport Layer Security

mail.login(email, password)
text=msg.as_string()
mail.sendmail(email, receiver, text)
mail.quit()
