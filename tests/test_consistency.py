import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wheelspin.wheel_generator import WheelGenerator

# Test with the actual 56 segments like in your main.py
labels = [
    "Ali", "Beatriz", "Charles", "Diya", "Eric", "Fatima", "Gabriel", "Hanna",
    "Ali", "Beatriz", "Charles", "Diya", "Eric", "Fatima", "Gabriel", "Hanna",
    "Ali", "Beatriz", "Charles", "Diya", "Eric", "Fatima", "Gabriel", "Hanna",
    "Ali", "Beatriz", "Charles", "Diya", "Eric", "Fatima", "Gabriel", "Hanna",
    "Ali", "Beatriz", "Charles", "Diya", "Eric", "Fatima", "Gabriel", "Hanna",
    "Ali", "Beatriz", "Charles", "Diya", "Eric", "Fatima", "Gabriel", "Hanna",
    "Ali", "Beatriz", "Charles", "Diya", "Eric", "Fatima", "Gabriel", "Hanna",
]

generator = WheelGenerator(size=500)
radius = 250  # Half of 500
angle_per_segment = 360 / len(labels)  # Much smaller segments now

result = generator.calculate_consistent_text_position(radius, angle_per_segment, labels)

print(f"Labels: {labels}")
print(f"Consistent position: {result['position']} (ratio: {result['text_radius_ratio']})")
print(f"All labels will be positioned at radius: {result['text_radius']:.1f}")

# Show individual analysis
print("\nIndividual label analysis:")

inner_space = generator.calculate_segment_space(radius, angle_per_segment, 0.65)
for label in labels:
    text_dims = generator.get_text_dimensions(label)
    fits_inner = (text_dims['width'] <= inner_space['arc_length'] * 0.8 and
                  text_dims['height'] <= inner_space['radial_space'])
    print(f"  {label:8s}: width={text_dims['width']:2.0f}px, fits_inner={fits_inner}")