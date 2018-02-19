import smtplib
s=smtplib.SMTP('smtpgmail.com',587)
s.starttls()
s.login("sne94813@gmail.com","laaaaaa")
message="hi how are you?"
s.sendmail("sne94813@gmail.com","saimasalutagi@gmail.com",message)
s.quit()
