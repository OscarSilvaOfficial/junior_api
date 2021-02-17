import requests, logging
from junior_api.settings import SAND_MAIL_API

def create_email(request, subject, content):
  payload = {
    "destination": request['email'],
    "subject": subject,
    "content": f"{request['username']}, {content}"
  }
  
  try:
    requests.post(SAND_MAIL_API, json=payload)
  except Exception as e:
    logging.error(e)
    return "Não foi possível enviar email"
  return 'Email enviado para fila'