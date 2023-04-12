import csv
import email_validator

# Define a function to validate email addresses
def is_valid_email(email):
    try:
        email_validator.validate_email(email)
        return True
    except email_validator.EmailNotValidError:
        return False

# Open input and output CSV files
with open('kk.csv', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header row to output CSV file
    header = next(reader)
    writer.writerow(header)

    # Find index of email address column
    email_index = None
    for i, col in enumerate(header):
        if 'email' in col.lower():
            email_index = i
            break

    # Iterate over rows in input CSV file
    num_valid_emails = 0
    for row in reader:
        try:
            # Get email address from appropriate column
            email = row[email_index]

            # Validate email address
            if is_valid_email(email):
                writer.writerow(row)  # Write row to output CSV file if email is valid
                num_valid_emails += 1  # Increment count of valid email addresses
        except (IndexError, ValueError):
            pass  # Skip row if email address column is not found or email is not valid
    
    # Print number of valid email addresses
    print(f"Number of valid email addresses: {num_valid_emails}")






'''
import csv
import email_validator

# Define a function to validate email addresses
def is_valid_email(email):
    try:
        email_validator.validate_email(email)
        return True
    except email_validator.EmailNotValidError:
        return False

# Open input and output CSV files
with open('emails.csv', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header row to output CSV file
    header = next(reader)
    writer.writerow(header)

    # Find index of email address column
    email_index = None
    for i, col in enumerate(header):
        if 'email' in col.lower():
            email_index = i
            break

    # Iterate over rows in input CSV file
    for row in reader:
        try:
            # Get email address from appropriate column
            email = row[email_index]

            # Validate email address
            if is_valid_email(email):
                writer.writerow(row)  # Write row to output CSV file if email is valid
        except (IndexError, ValueError):
            pass  # Skip row if email address column is not found or email is not valid
'''
