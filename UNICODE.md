# Unicode Support

The WheelSpin library has full UTF-8 and Unicode text support! 🎉

## What's Supported

### ✅ Unicode Text Characters
- **Cyrillic**: Москва, Привет, Київ, София
- **Chinese**: 北京, 你好, 上海, 广州
- **Japanese**: 東京, こんにちは, 大阪, 京都
- **Arabic**: مرحبا, شكرا, نعم, لا
- **Accented Latin**: Café, José, Zürich, François
- **Special Symbols**: ★ ♥ ♪ ☀ ☁ ⚡ ☃

### �🎨 Examples

#### International Cities
```python
from wheelspin import create_spinning_wheel

cities = ["Paris", "東京", "Москва", "北京", "Cairo"]
winner = create_spinning_wheel(cities, "cities.gif", size=600)
```

#### Multilingual Greetings
```python
greetings = ["Hello", "Bonjour", "こんにちは", "你好", "مرحبا"]
winner = create_spinning_wheel(greetings, "greetings.gif", size=600)
```

#### Accented Names

#### International Cities with Flags
```python
cities = ["Paris 🇫🇷", "東京 🇯🇵", "Москва 🇷🇺", "北京 🇨🇳", "Cairo 🇪🇬"]
winner = create_spinning_wheel(cities, "cities.gif", size=600)
```

#### Pure Emoji Wheel
```python
# Emoji render in full color!
emoji = ["�", "�", "⚽", "�", "🎸", "🎨"]
winner = create_spinning_wheel(emoji, "emoji.gif", size=500)
```

#### Accented Names
```python
names = ["José", "François", "Søren", "Łukasz", "Zürich"]
winner = create_spinning_wheel(names, "names.gif", size=600)
```

## How It Works

### Smart Font Loading
The library automatically tries multiple Unicode-compatible fonts:

1. **macOS**: Arial Unicode, Helvetica
2. **Linux**: DejaVuSans, Liberation Sans, Noto Sans, Unifont
3. **Windows**: Arial Unicode MS
4. **Fallback**: PIL default font

### Font Caching
Fonts are cached for better performance when creating multiple wheels.

### Cross-Platform
Works on all platforms (macOS, Linux, Windows) with automatic font detection.

## Running the Demo

```bash
# Run the comprehensive Unicode demo
python examples/unicode_demo.py
```

This will create 4 example wheels showcasing:
- 🌍 International city names
- 👋 Multilingual greetings
- 👥 Names with accents
- ⭐ Special symbols

## Testing

All Unicode functionality is tested:

```bash
# Run Unicode tests
pytest tests/test_unicode.py -v

# Run all tests
pytest tests/ -v
```

## Technical Details

### Implementation
- **Font Loading**: `wheel_generator.py::_load_font()`
- **Caching**: Fonts cached in `_font_cache` dict
- **Unicode Text**: Full UTF-8 support in all text rendering

### Supported Operations
- ✅ Text dimension calculation
- ✅ Segment label rendering
- ✅ Text rotation
- ✅ Multi-line emoji + text
- ✅ Right-to-left languages (Arabic)

## Examples Gallery

Check out these generated wheels:
- `emoji_food_wheel.gif` - Food with emoji
- `international_cities.gif` - Cities with flags
- `greetings_wheel.gif` - Multilingual greetings
- `pure_emoji_wheel.gif` - Only emoji
- `zodiac_wheel.gif` - Zodiac symbols

## Tips

1. **Emoji Sizing**: Emoji are rendered at the same font size as text
2. **Mixed Content**: You can combine emoji and text: "🍕 Pizza"
3. **Font Fallback**: If a character isn't supported, the library tries alternative fonts
4. **Performance**: Fonts are cached, so repeated wheel creation is fast

## Known Limitations

- Some very rare Unicode characters may fall back to default font
- Emoji color rendering depends on system font availability
- Complex emoji sequences (ZWJ) may render as separate characters

## Future Enhancements

- [ ] Custom font file support
- [ ] Better emoji color rendering
- [ ] Font fallback chain customization
- [ ] Unicode normalization options

---

**Full UTF-8 support - use any language, any emoji!** 🌈
