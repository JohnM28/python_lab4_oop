def email_composer(subject,sender_email,receiver_email,receiver_name):
    structure = f"From: {sender_email}\n" \
                f"To {receiver_email}\n\n" \
                f"Hi, {receiver_name}\n" \
                f"This is an email template thanks!"
    email_file = open(f'{subject}.txt', "w")
    email_file.write(structure)
    email_file.close()

#email_composer("test email","john@gmail.com","folan@gmail.com","reciver_name")

def email_tempalte(subject, sender_email, receiver_email, receiver_name,msg):
    structure = f"From: {sender_email}\n" \
                f"To {receiver_email}\n\n" \
                f"Hi, {receiver_name}\n" \
                f"{msg}"
    email_file = open(f'{subject}.txt', "w")
    email_file.write(structure)
    email_file.close()