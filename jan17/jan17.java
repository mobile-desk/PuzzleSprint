import java.util.Scanner;

public class ManualSort {
    public static void manualSort(int[] inputArray) {
        int n = inputArray.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (inputArray[j] > inputArray[j + 1]) {
                    // Swap elements if they are in the wrong order
                    int temp = inputArray[j];
                    inputArray[j] = inputArray[j + 1];
                    inputArray[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a list of space-separated numbers: ");
        String input = scanner.nextLine();
        String[] inputArrayStr = input.split(" ");

        int[] inputArray = new int[inputArrayStr.length];
        for (int i = 0; i < inputArrayStr.length; i++) {
            inputArray[i] = Integer.parseInt(inputArrayStr[i]);
        }

        System.out.print("Original List: ");
        for (int num : inputArray) {
            System.out.print(num + " ");
        }

        manualSort(inputArray);

        System.out.print("\nSorted List: ");
        for (int num : inputArray) {
            System.out.print(num + " ");
        }

        scanner.close();
    }
}