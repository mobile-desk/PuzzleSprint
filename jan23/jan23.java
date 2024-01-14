public class FrameCounter {
    public static int frames(int minutes, int fps) {
        int seconds = minutes * 60;
        int totalFrames = seconds * fps;
        return totalFrames;
    }

    public static void main(String[] args) {
        // Examples
        System.out.println(frames(1, 1));    // Output: 60
        System.out.println(frames(10, 1));   // Output: 600
        System.out.println(frames(10, 25));  // Output: 15000
    }
}