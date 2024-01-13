import java.util.Scanner;

public class GuessTheNumber {
    public static void guessTheNumber() {
        int lowerBound = 1;
        int upperBound = 100;
        int targetNumber = (int) (Math.random() * (upperBound - lowerBound + 1) + lowerBound);

        System.out.println("Welcome to Guess the Number!");
        System.out.println("Guess the number between " + lowerBound + " and " + upperBound);

        Scanner scanner = new Scanner(System.in);
        int attempts = 0;

        while (true) {
            int userGuess = scanner.nextInt();
            attempts++;

            if (userGuess == targetNumber) {
                System.out.println("Congratulations! You guessed the correct number in " + attempts + " attempts.");
                break;
            } else if (userGuess < targetNumber) {
                System.out.println("Too low! Try again.");
            } else {
                System.out.println("Too high! Try again.");
            }
        }

        scanner.close();
    }

    public static void main(String[] args) {
        guessTheNumber();
    }
}