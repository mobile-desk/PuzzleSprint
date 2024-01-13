const data = {
    name: "John Doe",
    details: {
        age: 30,
        location: {
            city: "Anytown",
            country: "Wonderland"
        },
        contacts: [
            {
                type: "email",
                value: "john.doe@example.com"
            },
            {
                type: "phone",
                value: "+1234567890"
            }
        ]
    }
};

const emailValue = data.details.contacts[0].value;
console.log("Extracted email value:", emailValue);