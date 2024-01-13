public class AnimalLegsCounter {
    public static int countLegs(int chickens, int cows, int pigs) {
        int chickenLegs = chickens * 2;
        int cowLegs = cows * 4;
        int pigLegs = pigs * 4;

        return chickenLegs + cowLegs + pigLegs;
    }

    public static void main(String[] args) {
        // Example usage
        int totalLegs = countLegs(2, 3, 5);
        System.out.println("Total number of legs: " + totalLegs);
    }
}