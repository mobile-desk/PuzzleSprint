public class JudgeCircle {
    public static boolean judgeCircle(String moves) {
        int x = 0, y = 0;
        for (char move : moves.toCharArray()) {
            if (move == 'U') y++;
            else if (move == 'D') y--;
            else if (move == 'L') x--;
            else if (move == 'R') x++;
        }
        return x == 0 && y == 0;
    }

    public static void main(String[] args) {
        String input = "UD";
        boolean result = judgeCircle(input);
        System.out.println(result);
    }
}
