# To send email (pdf report), yagmail (Yet Another Gmail Client) is used
import yagmail
import os


# function to send email
def sendmail(email_id: str):
    # credentials of sender
    yag = yagmail.SMTP("example@example.com", "PassWoRdExample")

    # details of the email
    yag.send(
        to=email_id,
        subject="SECURITY BREACH DETECTED",
        contents=f"HID attack detected for user: {os.getlogin()} \nPlease refer the attached webcam capture & logs "
                 f"for investigation.",
        attachments=["logs/key_log.txt", "camshots/webcam_shot.jpg"],
    )

    print(f"Email sent successfully")


# test your SMTP email feature
if __name__ == '__main__':
    sendmail("example@example.com")

