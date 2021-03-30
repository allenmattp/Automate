import smtplib, passwordGen

# SMTP object to connect to gmail mail server on port 587
conn = smtplib.SMTP("smtp.gmail.com", 587)

# say hello to server
conn.ehlo()
# start enable TLS encryption
conn.starttls()

# grab my app password so I don't upload it to github
password = passwordGen.passGen()

conn.login("allenmattpdev@gmail.com", password)

conn.sendmail("allenmattpdev@gmail.com", "allen.mattp@gmail.com",
              "Subject: Python test email\n\n"
              "This is a test email.")

conn.quit()