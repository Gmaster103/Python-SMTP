
#*Import libreria smtplib per inviare email tramite protocollo SMTP

import smtplib

#*Import libreria tkinter per creare interfaccia GUI del client
import tkinter as tk


#*Definizione funzione per l'invio dell'email
def send_email(HOST, PORT, from_email, to_email, subject, body, password):

    try:
        #*Connessione al server SMTP
        smtp = smtplib.SMTP(HOST, PORT)
        
        #*Creazione del messaggio
        message = "Subject: "+subject+"\n\n"+body
        

        #*Feedback della connessione al server
        status_code, response = smtp.ehlo()
        print(f"[*] Echoing the server: {status_code} {response} [*]")
        
        status_code, response = smtp.starttls()
        print(f"[*] Starting TLS connection: {status_code} {response} [*]")
        
        
        #*Login nell'account
        status_code, response = smtp.login(from_email, password)
        print(f"[*] Logging in: {status_code} {response} [*]")

        #*Invio email SMTP
        smtp.sendmail(from_email, to_email, message)
        print(f"[*] Successfully sent mail to {to_email} [*]")
        smtp.quit()
        
    except Exception as e:
        print(f"[*] Error: {e} [*]")


#*Definizione funzione per l'impostazione dei campi dell'email
def set_info():
    
    #*Creazione delle costanti per la connessione al server SMTP di Outlook
    HOST = "smtp-mail.outlook.com"
    PORT = 587
    
    #*Inizializzazione variabili dei campi
    from_email = input_mittente.get()
    
    password = input_password.get()
    
    to_email = input_destinatario.get()
    
    subject = input_subject.get()
    
    body = input_body.get()
    
    send_email(HOST, PORT, from_email, to_email, subject, body, password)




#*Creazione della finestra di interfaccia
window = tk.Tk()
window.title("SMTP Email")
window.geometry("500x300")
frame = tk.Frame(window)
frame.pack()
frame_email = tk.LabelFrame(frame, text="Input email")
frame_email.grid(row=0, column=0, padx=10, pady=10)


label_mittente = tk.Label(frame_email, text="Email mittente:")
label_mittente.grid(row=0, column=0)

input_mittente = tk.Entry(frame_email, width=50)
input_mittente.grid(row=0, column=1)


label_password = tk.Label(frame_email, text="Password:")
label_password.grid(row=1, column=0)

input_password = tk.Entry(frame_email, text="Password:", show="*", width=50)
input_password.grid(row=1, column=1)



label_destinatario = tk.Label(frame_email, text="Email destinatario:")
label_destinatario.grid(row=2, column=0)

input_destinatario = tk.Entry(frame_email, width=50)
input_destinatario.grid(row=2, column=1)


label_subject = tk.Label(frame_email, text="Oggetto:")
label_subject.grid(row=3, column=0)

input_subject = tk.Entry(frame_email, width=50)
input_subject.grid(row=3, column=1)


label_body = tk.Label(frame_email, text="Corpo:")
label_body.grid(row=4, column=0)

input_body = tk.Entry(frame_email, width=50)
input_body.grid(row=4, column=1)


#*Bottone di invio della email
button = tk.Button(frame, text="Invia email", command=set_info)
button.grid(row=5, column=0, sticky="news", padx=40, pady=20)


window.mainloop()










#*Definizione Server SMTP e Porta SMTP
#Outlook: 	smtp-mail.outlook.com

# host = input("Inserisci l'host del server SMTP: ")
#Outlook: 587
# PORT = int(input("Inserisci la porta del server SMTP: "))

#*Definizione mittente, destinatario, oggetto e contenuto

# from_email = input("Inserisci la tua email: ")
# FROM_EMAIL = "emanuelepapi103@outlook.com"
#from_email = "emanuelepapi103@outlook.com"


# TO_EMAIL = "emanuelepapi49@gmail.com"


# SUBJECT = "Test email"


# BODY = "Questa email e' inviata con un programma\nGrazie, \nEmanuele"


# message = MIMEMultipart("alternative")
# message["From"] = from_email
# message["To"] = to_email
# message["Subject"] = subject
# MESSAGE = """Subject: Ciao

# Ciao sono io
# Questa email e' inviata con un programma
# Grazie,
# Emanuele"""

#*Creazione del messaggio
# message = "Subject: "+subject+"\n\n"+body

#*Inserimento della password dell'email
# password = getpass.getpass("Inserisci la password dell'email per continuare: ")