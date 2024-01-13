import java.util.Scanner;

public class CalculateArea {
    public static double calculateCircleArea(double radius) {
        return Math.PI * Math.pow(radius, 2);
    }

    public static double calculateSquareArea(double sideLength) {
        return Math.pow(sideLength, 2);
    }

    public static double calculateTriangleArea(double base, double height) {
        return 0.5 * base * height;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose a geometric shape:");
        System.out.println("1. Circle");
        System.out.println("2. Square");
        System.out.println("3. Triangle");

        System.out.print("Enter the number corresponding to the shape: ");
        String choice = scanner.nextLine();

        if (choice.equals("1")) {
            System.out.print("Enter the radius of the circle: ");
            double radius = scanner.nextDouble();
            double area = calculateCircleArea(radius);
            System.out.println("The area of the circle is: " + area);
        } else if (choice.equals("2")) {
            System.out.print("Enter the side length of the square: ");
            double sideLength = scanner.nextDouble();
            double area = calculateSquareArea(sideLength);
            System.out.println("The area of the square is: " + area);
        } else if (choice.equals("3")) {
            System.out.print("Enter the base length of the triangle: ");
            double base = scanner.nextDouble();
            System.out.print("Enter the height of the triangle: ");
            double height = scanner.nextDouble();
            double area = calculateTriangleArea(base, height);
            System.out.println("The area of the triangle is: " + area);
        } else {
            System.out.println("Invalid choice. Please choose a valid option.");
        }

        scanner.close();
    }
}