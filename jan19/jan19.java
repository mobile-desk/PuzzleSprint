import java.util.*;

public class NestedDataStructure {
    public static void main(String[] args) {
        Map<String, Object> data = new HashMap<>();
        data.put("name", "John Doe");

        Map<String, Object> details = new HashMap<>();
        details.put("age", 30);

        Map<String, String> location = new HashMap<>();
        location.put("city", "Anytown");
        location.put("country", "Wonderland");

        List<Map<String, String>> contacts = new ArrayList<>();
        Map<String, String> emailContact = new HashMap<>();
        emailContact.put("type", "email");
        emailContact.put("value", "john.doe@example.com");

        Map<String, String> phoneContact = new HashMap<>();
        phoneContact.put("type", "phone");
        phoneContact.put("value", "+1234567890");

        contacts.add(emailContact);
        contacts.add(phoneContact);

        details.put("location", location);
        details.put("contacts", contacts);

        data.put("details", details);

        // Extracting the email value
        String emailValue = ((List<Map<String, String>>) details.get("contacts")).get(0).get("value");
        System.out.println("Extracted email value: " + emailValue);
    }
}