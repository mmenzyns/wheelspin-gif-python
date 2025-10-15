"""Test Unicode and emoji support"""

import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from wheelspin import create_spinning_wheel, create_spinning_wheel_advanced
from wheelspin.wheel_generator import WheelGenerator


@pytest.fixture
def generator():
    """Fixture to create a WheelGenerator instance"""
    return WheelGenerator(size=500)


def test_unicode_text_dimensions(generator):
    """Test that Unicode characters can be measured"""
    unicode_labels = [
        "Café",
        "Naïve",
        "Zürich",
        "Москва",  # Moscow in Cyrillic
        "北京",    # Beijing in Chinese
        "こんにちは",  # Hello in Japanese
        "مرحبا",  # Hello in Arabic
    ]
    
    for label in unicode_labels:
        dims = generator.get_text_dimensions(label)
        assert dims['width'] > 0, f"Unicode text '{label}' should have width"
        assert dims['height'] > 0, f"Unicode text '{label}' should have height"
        print(f"\n{label}: width={dims['width']}px, height={dims['height']}px")


def test_emoji_text_dimensions(generator):
    """Test that emoji can be measured"""
    emoji_labels = [
        "🎲",
        "🎉",
        "🍕",
        "⚽",
        "🎮",
        "🏆",
    ]
    
    for label in emoji_labels:
        dims = generator.get_text_dimensions(label)
        assert dims['width'] > 0, f"Emoji '{label}' should have width"
        assert dims['height'] > 0, f"Emoji '{label}' should have height"
        print(f"\n{label}: width={dims['width']}px, height={dims['height']}px")


def test_mixed_emoji_text(generator):
    """Test mixed emoji and text"""
    mixed_labels = [
        "🍕 Pizza",
        "🎲 Roll Dice",
        "🏆 Winner",
        "⚽ Football",
    ]
    
    for label in mixed_labels:
        dims = generator.get_text_dimensions(label)
        assert dims['width'] > 0, f"Mixed text '{label}' should have width"
        assert dims['height'] > 0, f"Mixed text '{label}' should have height"
        print(f"\n{label}: width={dims['width']}px, height={dims['height']}px")


def test_create_wheel_with_unicode(tmp_path):
    """Test creating wheel with Unicode labels"""
    labels = ["Café", "Naïve", "Zürich", "Résumé"]
    output_file = tmp_path / "unicode_wheel.gif"
    
    winner = create_spinning_wheel(labels, str(output_file), size=400)
    
    assert winner in labels, "Winner should be one of the Unicode labels"
    assert output_file.exists(), "GIF should be created with Unicode text"
    
    print(f"\nUnicode wheel winner: {winner}")


def test_create_wheel_with_emoji(tmp_path):
    """Test creating wheel with emoji"""
    labels = ["🍕 Pizza", "🍔 Burger", "🍣 Sushi", "🌮 Taco", "🥗 Salad"]
    output_file = tmp_path / "emoji_wheel.gif"
    
    winner = create_spinning_wheel(labels, str(output_file), size=500)
    
    assert winner in labels, "Winner should be one of the emoji labels"
    assert output_file.exists(), "GIF should be created with emoji"
    
    print(f"\nEmoji wheel winner: {winner}")


def test_create_wheel_with_cyrillic(tmp_path):
    """Test creating wheel with Cyrillic text"""
    labels = ["Москва", "Киев", "Минск", "София"]
    output_file = tmp_path / "cyrillic_wheel.gif"
    
    winner = create_spinning_wheel(labels, str(output_file), size=400)
    
    assert winner in labels
    assert output_file.exists()
    
    print(f"\nCyrillic wheel winner: {winner}")


def test_create_wheel_with_chinese(tmp_path):
    """Test creating wheel with Chinese characters"""
    labels = ["北京", "上海", "广州", "深圳"]
    output_file = tmp_path / "chinese_wheel.gif"
    
    winner = create_spinning_wheel(labels, str(output_file), size=400)
    
    assert winner in labels
    assert output_file.exists()
    
    print(f"\nChinese wheel winner: {winner}")


def test_create_wheel_with_japanese(tmp_path):
    """Test creating wheel with Japanese characters"""
    labels = ["東京", "大阪", "京都", "横浜"]
    output_file = tmp_path / "japanese_wheel.gif"
    
    winner = create_spinning_wheel(labels, str(output_file), size=400)
    
    assert winner in labels
    assert output_file.exists()
    
    print(f"\nJapanese wheel winner: {winner}")


def test_create_wheel_with_arabic(tmp_path):
    """Test creating wheel with Arabic text"""
    labels = ["مرحبا", "شكرا", "نعم", "لا"]
    output_file = tmp_path / "arabic_wheel.gif"
    
    winner = create_spinning_wheel(labels, str(output_file), size=400)
    
    assert winner in labels
    assert output_file.exists()
    
    print(f"\nArabic wheel winner: {winner}")


def test_create_wheel_pure_emoji(tmp_path):
    """Test creating wheel with only emoji"""
    labels = ["🎲", "🎉", "🏆", "⚽", "🎮", "🍕"]
    output_file = tmp_path / "pure_emoji_wheel.gif"
    
    winner = create_spinning_wheel(labels, str(output_file), size=500)
    
    assert winner in labels
    assert output_file.exists()
    
    print(f"\nPure emoji wheel winner: {winner}")


def test_font_caching(generator):
    """Test that fonts are cached for performance"""
    # First call should load font
    generator.get_text_dimensions("Test")
    
    # Second call should use cached font
    generator.get_text_dimensions("Test")
    
    # Both should use the same font object
    assert generator._font_cache, "Font cache should not be empty"
    print(f"\nFont cache contains {len(generator._font_cache)} entries")


def test_advanced_wheel_with_emoji_and_custom_colors(tmp_path):
    """Test advanced wheel creation with emoji and custom colors"""
    labels = ["🔴 Red", "🔵 Blue", "🟢 Green", "🟡 Yellow"]
    colors = ["#ff0000", "#0000ff", "#00ff00", "#ffff00"]
    output_file = tmp_path / "emoji_colors_wheel.gif"
    
    winner, info = create_spinning_wheel_advanced(
        segments=labels,
        output_file=str(output_file),
        size=500,
        colors=colors,
        font_size=14
    )
    
    assert winner in labels
    assert output_file.exists()
    assert 'winner_name' in info
    
    print(f"\nEmoji+colors wheel winner: {winner}")


@pytest.mark.parametrize("label", [
    "Café ☕",
    "🎲 Dice",
    "北京 🇨🇳",
    "مرحبا 👋",
    "こんにちは 🇯🇵",
])
def test_various_unicode_combinations(generator, label):
    """Test various combinations of Unicode and emoji"""
    dims = generator.get_text_dimensions(label)
    assert dims['width'] > 0
    assert dims['height'] > 0
