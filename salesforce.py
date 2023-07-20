from simple_salesforce import Salesforce

sf = Salesforce(username='my_username', password='my_password', security_token='my_security_token')

contact = {
    "LastName": "Smith",
    "Email": "example@example.com",
    "Phone": "1234567890"
}

sf.Contact.create(contact)
