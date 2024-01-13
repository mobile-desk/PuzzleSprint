data = {
    "name": "John Doe",
    "details": {
        "age": 30,
        "location": {
            "city": "Anytown",
            "country": "Wonderland"
        },
        "contacts": [
            {
                "type": "email",
                "value": "john.doe@example.com"
            },
            {
                "type": "phone",
                "value": "+1234567890"
            }
        ]
    }
}



#extracting the value
email_value = data["details"]["contacts"][0]["value"]
print("Extracted email value:", email_value)