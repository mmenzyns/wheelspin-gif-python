from PIL import Image, ImageDraw, ImageFont
import math

# Test to understand the wheel coordinate system
def test_wheel_segments():
    """Test which segment is at 0 degrees (3 o'clock position)"""
    
    size = 500
    center = size // 2
    radius = size // 2 - 20
    segments = 8
    angle_per_segment = 360 / segments  # 45 degrees per segment
    
    print(f"Angle per segment: {angle_per_segment}°")
    print("\nSegment positions when rotation_angle = 0:")
    
    for i in range(segments):
        start_angle = 0 + (i * angle_per_segment)  # rotation_angle = 0
        end_angle = start_angle + angle_per_segment
        mid_angle = start_angle + (angle_per_segment / 2)
        
        print(f"Segment {i}: start={start_angle}°, mid={mid_angle}°, end={end_angle}°")
        
        # Check if 0° (3 o'clock) falls within this segment
        if start_angle <= 0 <= end_angle or start_angle <= 360 <= end_angle:
            print(f"  -> 0° (pointer position) is in Segment {i}")
    
    # Also check what happens with our starting rotation
    start_rotation = 283.82
    print(f"\nWith start_rotation = {start_rotation}°:")
    
    for i in range(segments):
        start_angle = start_rotation + (i * angle_per_segment)
        end_angle = start_angle + angle_per_segment
        mid_angle = start_angle + (angle_per_segment / 2)
        
        # Normalize angles to 0-360 range
        start_angle_norm = start_angle % 360
        end_angle_norm = end_angle % 360
        mid_angle_norm = mid_angle % 360
        
        print(f"Segment {i}: start={start_angle_norm:.1f}°, mid={mid_angle_norm:.1f}°, end={end_angle_norm:.1f}°")
        
        # Check if 0° (pointer position) falls within this segment
        if start_angle_norm <= 0 <= end_angle_norm or (end_angle_norm < start_angle_norm and (0 >= start_angle_norm or 0 <= end_angle_norm)):
            print(f"  -> 0° (pointer position) is in Segment {i}")

if __name__ == "__main__":
    test_wheel_segments()