# To send email (pdf report), yagmail (Yet Another Gmail Client) is used
import yagmail


# function to send email
def sendmail(emailid):
    # credentials of sender
    yag = yagmail.SMTP("example@example.com", "PassWoRdExample")

    # details of the email
    yag.send(
        to=emailid,
        subject="SECURITY BREACH DETECTED",
        contents="Someone/something tried to access your system physically",
        attachments="logs/key_log.txt",
    )


# test your SMTP email feature
if __name__ == '__main__':
    sendmail("example@example.com")

