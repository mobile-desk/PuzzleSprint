function frames(minutes, fps) {
    const seconds = minutes * 60;
    const totalFrames = seconds * fps;
    return totalFrames;
}

// Examples
console.log(frames(1, 1));    // Output: 60
console.log(frames(10, 1));   // Output: 600
console.log(frames(10, 25));  // Output: 15000