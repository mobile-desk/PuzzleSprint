using System;

class Program {
    public static bool JudgeCircle(string moves) {
        int x = 0, y = 0;
        foreach (char move in moves) {
            if (move == 'U') y++;
            else if (move == 'D') y--;
            else if (move == 'L') x--;
            else if (move == 'R') x++;
        }
        return x == 0 && y == 0;
    }

    static void Main() {
        string input = "UD";
        bool result = JudgeCircle(input);
        Console.WriteLine(result);
    }
}
