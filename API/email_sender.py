import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail:
    def __init__(self):
        self.App_name = 'RYTING-WORKAH'
        self.APP_initial = 'RYW'

        self.App_email = "petstellonstudios@gmail.com"
        self.Sender = f"{self.App_name} <{self.App_email}>"
        self.App_password = 'tewknvyyksjptsof'
        self.currency = 'NGN'
        self.deep_color = 'green'

    def email_confirmation(self, receiver, subject, details):
        sender_email = self.App_email  # Enter your address
        receiver_email = receiver  # Enter receiver address
        password = self.App_password

        message = MIMEMultipart("alternative")
        message[ "Subject" ] = subject
        message[ "From" ] = self.Sender
        message[ "To" ] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = f"""\
        <html>
          <body>
          <div style="background-color: grey;">
          <img src='{details[ "email_banner" ][ 0 ]}' alt='logo'/>
          <div style="margin:20px; background-color: white; padding: 20px;">
            <h2> Hi!! </h2>
            <p> Welcome to {self.App_name} </p>
            <p>Kindly use this <a href='{details['link']}'>link</a> to verify your email. </p>
            <p>{details['link']}</p>
            <p>Thank you</p>
          </div>
          <div style="background-color: white;">
          <img src='{details[ "email_banner" ][ 1 ]}' alt='footer'/>
          </div>
          </div>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def set_price(self, receiver, subject, details):
        sender_email = self.App_email  # Enter your address
        receiver_email = receiver  # Enter receiver address
        password = self.App_password

        message = MIMEMultipart("alternative")
        message[ "Subject" ] = subject
        message[ "From" ] = self.Sender
        message[ "To" ] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = f"""\
        <html>
          <body>
          <div style="background-color: grey;">
          <img src='{details[ "email_banner" ][ 0 ]}' alt='logo'/>
          <div style="margin:20px; background-color: white; padding: 20px;">
            <h2> Hi!! {details[ 'client_id' ]}</h2>
            <p>Price Update for {details[ 'project_ref' ]}</p>
            <h3>Update details</h3>
            <p>Ref: {details[ 'project_ref' ]}</p>
            <p>Price: ₦{ '{:,.2f}'.format(details['price']) }</p>
            <p>Kindly login to review.</p>
            <p>Thank you</p>
          </div>
          <div style="background-color: white;">
          <img src='{details[ "email_banner" ][ 1 ]}' alt='footer'/>
          </div>
          </div>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def chat(self, receiver, subject, details):
        sender_email = self.App_email  # Enter your address
        receiver_email = receiver  # Enter receiver address
        password = self.App_password

        message = MIMEMultipart("alternative")
        message[ "Subject" ] = subject
        message[ "From" ] = self.Sender
        message[ "To" ] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = f"""\
        <html>
          <body>
          <div style="background-color: grey;">
          <img src='{details[ "email_banner" ][ 0 ]}' alt='logo'/>
          <div style="margin:20px; background-color: white; padding: 20px;">
            <h2> Hi!! {details[ 'sender' ]} sent you a message.</h2>
            <p>Project ref: <b>{details[ 'project_ref' ]}</b></p>
            <p>Message: <b>{details[ 'message' ]}<b></p>
            <p>Kindly login to reply.</p>
            <p>Thank you</p>
          </div>
          <div style="background-color: white;">
          <img src='{details[ "email_banner" ][ 1 ]}' alt='footer'/>
          </div>
          </div>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def open_bid(self, receiver, subject, details):
        sender_email = self.App_email  # Enter your address
        receiver_email = receiver  # Enter receiver address
        password = self.App_password

        message = MIMEMultipart("alternative")
        message[ "Subject" ] = subject
        message[ "From" ] = self.Sender
        message[ "To" ] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = f"""\
        <html>
          <body>
          <div style="background-color: grey;">
          <img src='{details[ "email_banner" ][ 0 ]}' alt='logo'/>
          <div style="margin:20px; background-color: white; padding: 20px;">
            <h2> Hi!! {details[ 'staff' ]}.</h2>
            <p>New project open for bid, find details below.</b></p>
            <p>Project ref: <b>{details[ 'project_ref' ]}</b></p>
            <p>Kindly login to bid for this project.</p>
            <p>Thank you</p>
          </div>
          <div style="background-color: white;">
          <img src='{details[ "email_banner" ][ 1 ]}' alt='footer'/>
          </div>
          </div>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def bid_approved(self, receiver, subject, details):
        sender_email = self.App_email  # Enter your address
        receiver_email = receiver  # Enter receiver address
        password = self.App_password

        message = MIMEMultipart("alternative")
        message[ "Subject" ] = subject
        message[ "From" ] = self.Sender
        message[ "To" ] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = f"""\
        <html>
          <body>
          <div style="background-color: grey;">
          <img src='{details[ "email_banner" ][ 0 ]}' alt='logo'/>
          <div style="margin:20px; background-color: white; padding: 20px;">
            <h2> Hi!! {details[ 'staff' ]}.</h2>
            <p>Congratulations!! your bid for {details['ref']} was approved.</p>
            <p>Project ref: <b>{details[ 'ref' ]}</b></p>
            <p>Deadline: <b>{details[ 'deadline' ]}</b></p>
            <p>Approved price: <b>NGN { '{:,.2f}'.format(details[ 'approved_price' ]) }</b></p>
            <p>Kindly login to start this project.</p>
            <p>Thank you</p>
          </div>
          <div style="background-color: white;">
          <img src='{details[ "email_banner" ][ 1 ]}' alt='footer'/>
          </div>
          </div>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def review_project(self, receiver, subject, details):
        sender_email = self.App_email  # Enter your address
        receiver_email = receiver  # Enter receiver address
        password = self.App_password

        message = MIMEMultipart("alternative")
        message[ "Subject" ] = subject
        message[ "From" ] = self.Sender
        message[ "To" ] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = f"""\
        <html>
          <body>
          <div style="background-color: grey;">
          <img src='{details[ "email_banner" ][ 0 ]}' alt='logo'/>
          <div style="margin:20px; background-color: white; padding: 20px;">
            <h2> Hi!! </h2>
            <p>{details[ 'staff' ]} has submited {details[ 'project_ref' ]} for review.</p>
            <p>Login to review this project.</p>
            <p>Thank you</p>
          </div>
          <div style="background-color: white;">
          <img src='{details[ "email_banner" ][ 1 ]}' alt='footer'/>
          </div>
          </div>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def complete_project(self, receiver, subject, details):
        sender_email = self.App_email  # Enter your address
        receiver_email = receiver  # Enter receiver address
        password = self.App_password

        message = MIMEMultipart("alternative")
        message[ "Subject" ] = subject
        message[ "From" ] = self.Sender
        message[ "To" ] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = f"""\
        <html>
          <body>
          <div style="background-color: grey;">
          <img src='{details[ "email_banner" ][ 0 ]}' alt='logo'/>
          <div style="margin:20px; background-color: white; padding: 20px;">
            <h2> Hi!! {details[ 'client_id' ]}</h2>
            <p>Your project {details[ 'project_ref' ]} has been completed and ready for download.</p>
            <p>Login to download this project.</p>
            <p>Thank you</p>
          </div>
          <div style="background-color: white;">
          <img src='{details[ "email_banner" ][ 1 ]}' alt='footer'/>
          </div>
          </div>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )