# SMTP Python
This was a project for my Python Classes 1st semester, my first tiny project.
The task was to code a SMTP in Python only using smtplib, making it as easy as possible for the user.
For that, the project uses a lot of input functions in order to attend to that need.

Sending for more than one e-mail was tricky as first, but since we changed what destinatario() previously returned from a list to a str, the variable email_msg['To'] = destinatario() finally worked.

So, email_msg['To'] needs to receive a string value, but on sendmail(email_msg['From'], email_msg['To'], ...), email_msg['To'] needs to be a list. That's the reason for the split(',').
