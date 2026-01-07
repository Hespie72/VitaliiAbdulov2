import smtplib, ssl
from email.message import EmailMessage
#iccp iixp npok vsnp
def saada_email(saaja_email):
    kiri="""Tere see on test https://github.com/Hespie72/VitaliiAbdulov2/blob/master/VitaliiAbdulov2/email1message.py"""
    teema="Test e-kiri Pythonist"
    saatja_email="vitalya.abdulov.1979@gmail.com"
    parool=input("Sisesta rakenduse parool: ")
    smtp_server="smtp.gmail.com"
    port=587
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg["Subject"]=teema
    msg["From"]=saatja_email
    msg["To"]=saaja_email
    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(saatja_email,parool)
            server.send_message(msg) #kui ei kasuta with siis on vaja sulgeda server.quit()
    except Exception as e:
        print(f"Midagi läks valesti... {e}")
kellele=input("Sisesta saaja e-posti aadress: ")
saada_email(kellele)
