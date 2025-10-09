import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wheelspin.wheel_generator import WheelGenerator

# Test with different numbers of segments
generator = WheelGenerator(size=500)
radius = 250  # Half of 500

test_cases = [
    (8, ["Prize 1"]),      # 8 segments - should fit in inner position
    (20, ["Prize 1"]),     # 20 segments - might fit in inner position
    (50, ["Prize 1"]),     # 50 segments - likely needs outer position
    (100, ["Prize 1"]),    # 100 segments - definitely needs outer position
    (100, ["Prize 100"]),  # 100 segments with longer text
]

for segments, labels in test_cases:
    angle_per_segment = 360 / segments
    result = generator.calculate_consistent_text_position(radius, angle_per_segment, labels)
    
    print(f"Segments: {segments:3d}, Label: '{labels[0]:8s}' -> Position: {result['position']:5s}, "
          f"Radius: {result['text_radius']:.1f}")