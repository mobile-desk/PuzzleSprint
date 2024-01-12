import java.util.Scanner;

public class DecimalToBinary {
    public static String decimalToBinary(int decimalNumber) {
        return Integer.toBinaryString(decimalNumber);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a decimal number: ");
        int decimalNumber = scanner.nextInt();

        if (decimalNumber < 0) {
            System.out.println("Please enter a non-negative integer.");
        } else {
            String binaryRepresentation = decimalToBinary(decimalNumber);
            System.out.println("The binary representation of " + decimalNumber + " is: " + binaryRepresentation);
        }
        scanner.close();
    }
}