class Email:
    def __init__(self, subject, email_address, content):
        self.subject = subject
        self.email_address = email_address
        self.content = content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True
inbox = []
def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    email1 = Email("subject1", "email1@gmail.com", "Content of email 1")
    email2 = Email("subject2", "email2@gmail.com", "Content of email 2")
    email3 = Email("subject3", "email3@gmail.com", "Content of email 3")
    inbox.extend([email1, email2, email3])
    pass

def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for i, email in enumerate(inbox):
        print(f"{i}: {email.subject}")
    

def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    email = inbox[index]
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")
    email.mark_as_read()

def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    print("Unread Emails:")
    for i, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{i}: {email.subject}")

populate_inbox()

while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        email_index = int(input("Enter the email index to read: "))
        read_email(email_index)
        pass

    elif user_choice == 2:
        # Add logic here to view unread emails
        view_unread_emails()
        pass

    elif user_choice == 3:
        # Add logic here to quit application.
        print("Exiting application.")
        break

    else:
        print("Oops - incorrect input.")
