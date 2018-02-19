import smtplib
s=smtplib.smtp('smtp.gmail.com',587)
s.starttls()
s.login("sne94813@gmail.com","shyam07*")
msg="hi saima,how are you?"
s.sendmail("sne94813@gmail.com","saimasalugi@gmail.com",msg)
s.quit()

