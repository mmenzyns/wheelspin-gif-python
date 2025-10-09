#!/usr/bin/env python3
"""
Simple test of the WheelSpin library
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wheelspin import create_spinning_wheel

def test_library():
    """Test the library with a simple example"""
    print("🎲 Testing WheelSpin Library")
    print("=" * 30)
    
    # Simple test
    names = ["Alice", "Bob", "Charlie", "Diana"]
    print(f"Spinning wheel with: {names}")
    
    winner = create_spinning_wheel(names, "test_wheel.gif", size=400)
    
    print(f"🎉 Winner: {winner}")
    print("✅ Test completed! Check 'test_wheel.gif'")

if __name__ == "__main__":
    test_library()