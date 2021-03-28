import smtplib, passwordGen

conn = smtplib.SMTP("smtp.gmail.com", 587)

conn.ehlo()
conn.starttls()

# grab my app password so I don't upload it to github
password = passwordGen.passGen()

conn.login("allenmattpdev@gmail.com", password)

conn.sendmail("allenmattpdev@gmail.com", "allen.mattp@gmail.com",
              "Subject: Python test email\n\n"
              "This is a test email.")