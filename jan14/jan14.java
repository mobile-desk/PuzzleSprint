import java.util.Scanner;

public class MultiplicationTable {
    public static void generateMultiplicationTable(int number, int rangeLimit) {
        System.out.printf("Multiplication table for %d up to %d * %d:\n\n", number, number, rangeLimit);
        for (int i = 1; i <= rangeLimit; i++) {
            System.out.printf("%d * %d = %d\n", number, i, number * i);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        System.out.print("Enter the range: ");
        int rangeLimit = scanner.nextInt();

        generateMultiplicationTable(number, rangeLimit);
        scanner.close();
    }
}