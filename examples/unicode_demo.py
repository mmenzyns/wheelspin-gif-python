#!/usr/bin/env python3
"""
Unicode and Emoji Examples for WheelSpin Library

Demonstrates support for international characters and emoji.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wheelspin import create_spinning_wheel, create_spinning_wheel_advanced

# Create output directory for generated GIFs
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)





def example_international_cities():
    """Create a wheel with international city names"""
    print("\n🌍 International Cities")
    print("=" * 50)
    
    cities = [
        "Paris",
        "東京",  # Tokyo
        "Москва",  # Moscow
        "北京",  # Beijing
        "Cairo",
        "São Paulo"
    ]
    
    output_path = OUTPUT_DIR / "international_cities.gif"
    winner = create_spinning_wheel(cities, str(output_path), size=600)
    print(f"\n✈️ You're going to: {winner}!\n")


def example_multilingual_greetings():
    """Create a wheel with greetings in different languages"""
    print("\n👋 Multilingual Greetings")
    print("=" * 50)
    
    greetings = [
        "Hello",
        "Bonjour",
        "こんにちは",
        "你好",
        "مرحبا",
        "Привет",
        "Hola",
        "Ciao"
    ]
    
    output_path = OUTPUT_DIR / "greetings_wheel.gif"
    winner = create_spinning_wheel(greetings, str(output_path), size=600)
    print(f"\n🗣️ Today's greeting: {winner}!\n")


def example_accented_names():
    """Create a wheel with accented names"""
    print("\n👥 Names with Accents")
    print("=" * 50)
    
    names = ["José", "François", "Søren", "Łukasz", "Ñoño", "Çağlar", "Åsa", "Žaneta"]
    
    output_path = OUTPUT_DIR / "accented_names.gif"
    winner = create_spinning_wheel(names, str(output_path), size=500)
    print(f"\n🎯 Winner: {winner}!\n")


def example_symbols_and_special():
    """Create a wheel with special symbols"""
    print("\n⭐ Symbols and Special Characters")
    print("=" * 50)
    
    symbols = ["★ Star", "♥ Heart", "♪ Music", "☀ Sun", "☁ Cloud", "⚡ Lightning"]
    
    output_path = OUTPUT_DIR / "symbols_wheel.gif"
    winner = create_spinning_wheel(symbols, str(output_path), size=550)
    print(f"\n✨ You chose: {winner}!\n")


def main():
    """Run all Unicode examples"""
    print("\n" + "=" * 50)
    print("🌈 WheelSpin Unicode Examples")
    print("=" * 50 + "\n")
    
    examples = [
        example_international_cities,
        example_multilingual_greetings,
        example_accented_names,
        example_symbols_and_special,
    ]
    
    for i, example in enumerate(examples, 1):
        try:
            example()
        except Exception as e:
            print(f"⚠️  Example {i} failed: {e}\n")
    
    print("=" * 50)
    print("✅ All examples completed!")
    print("📁 Check the generated .gif files")
    print("=" * 50)


if __name__ == "__main__":
    main()
