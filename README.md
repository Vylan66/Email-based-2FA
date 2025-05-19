Project Description
This is a simple Python-based security solution that implements basic two-factor authentication (2FA) using email. It adds an extra layer of protection by verifying a user's identity through a randomized code sent to their email address.

This solution can be integrated into small scripts, internal tools, or learning projects to demonstrate the concept of multi-factor verification without relying on third-party APIs or complex infrastructure.

How the Code Works
User Input:
The program prompts the user to enter their email address.

Random Code Generation:
It generates a random 4-digit numeric code using Python’s random module.

Email Sending:
The code is sent to the user’s email via SMTP (using a Gmail account with an app password).

User Verification:
The user is then asked to enter the code they received. If the code matches, access is granted; otherwise, it's denied.

Security Logic:

The code is one-time-use and time-sensitive (implicitly).

TLS is used to encrypt the email in transit.

Email address input is kept simple for learning purposes.
