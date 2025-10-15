#!/usr/bin/env python3
"""
Simple usage example for WheelSpin library
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wheelspin import create_spinning_wheel

# Create output directory for generated GIFs
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    """Simple example"""
    print("🎲 WheelSpin Simple Example")
    print("=" * 40)
    
    # Create a simple wheel
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    
    print(f"Contestants: {', '.join(names)}")
    print("Spinning the wheel...\n")
    
    output_path = OUTPUT_DIR / "simple_example.gif"
    winner = create_spinning_wheel(names, str(output_path), size=500)
    
    print(f"\n🎉 The winner is: {winner}!")
    print(f"📁 Check '{output_path}' for the animation")

if __name__ == "__main__":
    main()