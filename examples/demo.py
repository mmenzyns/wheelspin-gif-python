#!/usr/bin/env python3
"""
WheelSpin Library - Complete Examples

This script demonstrates all the features of the WheelSpin library.
Run this to see how to use the library for various use cases.
"""

import sys
from pathlib import Path

# Add parent directory to path to import wheelspin package
sys.path.insert(0, str(Path(__file__).parent.parent))

from wheelspin import (
    create_spinning_wheel, 
    create_spinning_wheel_advanced, 
    quick_spin, 
    decision_wheel
)

# Create output directory for generated GIFs
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def example_1_basic():
    """Example 1: Basic wheel creation"""
    print("\n" + "="*50)
    print("📝 EXAMPLE 1: Basic Spinning Wheel")
    print("="*50)
    
    contestants = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    output_path = OUTPUT_DIR / "example1_basic.gif"
    winner = create_spinning_wheel(contestants, str(output_path))
    
    print(f"🏆 Contest winner: {winner}")


def example_2_advanced():
    """Example 2: Advanced wheel with custom options"""
    print("\n" + "="*50)
    print("📝 EXAMPLE 2: Advanced Customization")
    print("="*50)
    
    teams = ["Red Dragons", "Blue Eagles", "Green Wolves", "Yellow Lions", "Purple Tigers"]
    custom_colors = ["#e74c3c", "#3498db", "#2ecc71", "#f1c40f", "#9b59b6"]
    
    output_path = OUTPUT_DIR / "example2_teams.gif"
    winner, info = create_spinning_wheel_advanced(
        segments=teams,
        output_file=str(output_path),
        size=600,
        colors=custom_colors,
        font_size=13,
        animation_speed=1.3,
        start_rotation=45.0  # Fixed starting position
    )
    
    print(f"🏆 Winning team: {winner}")
    print(f"📊 Detailed info: {info}")


def example_3_quick_spin():
    """Example 3: Quick decision making"""
    print("\n" + "="*50)
    print("📝 EXAMPLE 3: Quick Spin")
    print("="*50)
    
    lunch_options = ["Pizza", "Sushi", "Burgers", "Salad", "Tacos"]
    output_path = OUTPUT_DIR / "example3_lunch.gif"
    choice = quick_spin(lunch_options, str(output_path))
    
    print(f"🍽️ Lunch decision: {choice}")


def example_4_decision_wheel():
    """Example 4: Decision wheel with context"""
    print("\n" + "="*50)
    print("📝 EXAMPLE 4: Decision Wheel")
    print("="*50)
    
    weekend_activities = [
        "Go hiking", "Watch movies", "Visit friends", 
        "Learn programming", "Play games", "Read a book"
    ]
    
    activity = decision_wheel(weekend_activities, "What should I do this weekend?")
    print(f"✨ Weekend plan: {activity}")


def example_5_many_segments():
    """Example 5: Wheel with many segments"""
    print("\n" + "="*50)
    print("📝 EXAMPLE 5: Many Segments (Testing Layout)")
    print("="*50)
    
    # Create a list of 20 items to test text positioning
    countries = [
        "USA", "Canada", "Mexico", "Brazil", "Argentina", "UK", "France", 
        "Germany", "Italy", "Spain", "Russia", "China", "Japan", "India", 
        "Australia", "Egypt", "Nigeria", "Kenya", "Morocco", "Algeria"
    ]
    
    output_path = OUTPUT_DIR / "example5_countries.gif"
    winner = create_spinning_wheel(
        countries, 
        str(output_path), 
        size=700  # Larger size for better text visibility
    )
    
    print(f"🌍 Random country selected: {winner}")


def example_6_custom_colors():
    """Example 6: Beautiful custom color schemes"""
    print("\n" + "="*50)
    print("📝 EXAMPLE 6: Custom Color Schemes")
    print("="*50)
    
    # Sunset color scheme
    activities = ["Swimming", "Reading", "Cooking", "Dancing", "Painting", "Singing"]
    sunset_colors = ["#ff9ff3", "#f368e0", "#ff6b6b", "#ee5a24", "#feca57", "#ff9ff3"]
    
    output_path = OUTPUT_DIR / "example6_sunset.gif"
    winner, info = create_spinning_wheel_advanced(
        segments=activities,
        output_file=str(output_path),
        size=500,
        colors=sunset_colors,
        font_size=12,
        animation_speed=0.8  # Slower, more dramatic
    )
    
    print(f"🎨 Beautiful wheel winner: {winner}")


def main():
    """Run all examples"""
    print("🎲 WheelSpin Library - Complete Examples")
    print("🚀 Generating multiple spinning wheels...")
    
    try:
        example_1_basic()
        example_2_advanced()
        example_3_quick_spin()
        example_4_decision_wheel()
        example_5_many_segments()
        example_6_custom_colors()
        
        print("\n" + "="*50)
        print("✅ ALL EXAMPLES COMPLETED!")
        print("="*50)
        print(f"📁 Generated files in: {OUTPUT_DIR}")
        print("   • example1_basic.gif")
        print("   • example2_teams.gif") 
        print("   • example3_lunch.gif")
        print("   • decision_wheel.gif")
        print("   • example5_countries.gif")
        print("   • example6_sunset.gif")
        print(f"\n🎉 Check out all the generated GIF files in {OUTPUT_DIR}/")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())