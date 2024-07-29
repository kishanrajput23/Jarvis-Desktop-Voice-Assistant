import win32com.client
from datetime import date
from jarvis_actions import speak


#function to read today's unread emails
def read_emails(email_list, num_of_emails, gender):
    #announce total number of unread emails
    print("You have", num_of_emails, "unread emails")
    speak("You have", num_of_emails, "unread emails", gender)

    #if there are no emails from today, then tell the user
    if len(email_list) == 0:
        print("No emails today")
        speak("No emails today", gender)

    else:
        for email in email_list:
            print(email.subject)
            speak(email.subject, gender)


#function to scan inbox for emails to read
def scan_inbox(gender):
    #interact with Outlook inbox
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)

    #get all unread emails
    emails = inbox.Items
    unread_emails = []
    for e in emails:
        if e.unread:
            unread_emails.append(e)

    total_unread_emails = len(unread_emails)

    #today's date to compare to email sent date 
    today = date.today()
    todays_year = today.strftime('%Y')
    todays_month = today.strftime('%m')
    todays_day = today.strftime('%d')

    emails_to_read = []
    #if email was sent today, read
    for ue in unread_emails:
        email_year = ue.ReceivedTime.year
        email_month = ue.ReceivedTime.month
        email_day = ue.ReceivedTime.day

        if todays_year == email_year:
            if todays_month == email_month:
                if todays_day == email_day:
                    emails_to_read.append(ue)

    read_emails(total_unread_emails, emails_to_read, gender)
