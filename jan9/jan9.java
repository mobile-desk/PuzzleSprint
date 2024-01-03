import java.util.ArrayList;
import java.util.List;

public class Permutations {
    public static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), nums);
        return result;
    }

    private static void backtrack(List<List<Integer>> result, List<Integer> current, int[] remaining) {
        if (current.size() == remaining.length) {
            result.add(new ArrayList<>(current));
        } else {
            for (int i = 0; i < remaining.length; i++) {
                if (current.contains(remaining[i])) {
                    continue;
                }
                current.add(remaining[i]);
                backtrack(result, current, remaining);
                current.remove(current.size() - 1);
            }
        }
    }

    public static void main(String[] args) {
        int[] input = {1, 2, 3};
        List<List<Integer>> result = permute(input);
        System.out.println(result);
    }
}