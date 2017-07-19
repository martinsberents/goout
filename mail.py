import smtplib
import settings

def get_instance():
    smtp_instance = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
    smtp_instance.starttls()
    smtp_instance.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
    return smtp_instance

def send_mail(address_from, addresses_to, message):
    smtp_instance = get_instance()
    smtp_instance.sendmail(address_from, addresses_to, message)
    smtp_instance.quit()
