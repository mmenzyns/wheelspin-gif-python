# Test frame scaling
def calculate_frames(segments):
    base_frames = 60
    base_segments = 8
    frame_multiplier = max(1.0, segments / base_segments * 0.27)  # Updated scaling factor
    return int(base_frames * frame_multiplier)

test_segments = [8, 16, 32, 50, 100, 200]

print("Segment Count -> Animation Frames (Duration)")
print("-" * 45)
for segments in test_segments:
    frames = calculate_frames(segments)
    duration_ms = frames * 50  # 50ms per frame
    duration_sec = duration_ms / 1000
    print(f"{segments:3d} segments -> {frames:3d} frames ({duration_sec:.1f}s)")