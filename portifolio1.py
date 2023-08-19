import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import schedule
import time

# Configurações do servidor SMTP
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_username'
smtp_password = 'your_password'

def remove_duplicates(email_list):
    return list(set(email_list))

def send_email(subject, body, recipients, attachments=None):
    try:
        # Configurar a conexão com o servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        unique_recipients = remove_duplicates(recipients)
        
        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            if attachments:
                for attachment in attachments:
                    with open(attachment, 'rb') as file:
                        part = MIMEApplication(file.read())
                        part.add_header('Content-Disposition', f'attachment; filename="{attachment}"')
                        msg.attach(part)
            
            server.sendmail(smtp_username, recipient, msg.as_string())
            
        server.quit()
        print("E-mails enviados com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mails: {e}")

def schedule_emails(subject, body, recipients, attachments=None, schedule_time=None):
    if schedule_time:
        schedule.every().day.at(schedule_time).do(send_email, subject, body, recipients, attachments)
        print(f"E-mails agendados para envio diário às {schedule_time}")
    else:
        send_email(subject, body, recipients, attachments)

# Exemplo de uso
if __name__ == "__main__":
    subject = "Assunto do e-mail"
    body = "Corpo do e-mail"
    recipients = ["recipient1@example.com", "recipient2@example.com"]
    attachments = ["attachment1.pdf", "attachment2.docx"]
    schedule_time = "14:00"  # Hora de agendamento (formato: "HH:MM")
    
    schedule_emails(subject, body, recipients, attachments, schedule_time)
    
    while True:
        schedule.run_pending()
        time.sleep(1)