# Use this template to send email using sendgrid

# docker exec - it enerlly_server_backend_1 zsh
# python manage.py shell

from comm_services import public as comm_service_public

SENDMAIL_USING_SENDGRID = true


context_data = {}  # the data which has to be shared in json to the email template
to_mails = ["nikhil@enerlly.com", "ganesh@enerlly.com"]

comm_service_public.send_email("testing", to_mails, context_data)
