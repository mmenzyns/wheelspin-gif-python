"""
WheelGenerator - Core implementation for spinning wheel generation
"""

from PIL import Image, ImageDraw, ImageFont
import math
import platform
from typing import List, Tuple, Optional


class WheelGenerator:
    """Core wheel generation class"""
    
    def __init__(self, size: int = 500, colors: List[str] = None, font_size: int = 11, animation_speed: float = 1.0):
        self.size = size
        self.colors = colors or ['#eeb312', '#d61126', '#346ae9', '#019b26']
        self.font_size = font_size
        self.animation_speed = animation_speed
        self.transparent_color = (255, 0, 255, 0)
        self.circle_degrees = 360
        self._font_cache = {}  # Cache loaded fonts
    
    def distribute_colors(self, num_segments: int) -> List[str]:
        """
        Distribute colors to segments ensuring no two adjacent segments have the same color.
        Uses a greedy approach to maximize color separation.
        """
        if num_segments <= len(self.colors):
            # If we have enough colors, just use them in order
            return [self.colors[i % len(self.colors)] for i in range(num_segments)]
        
        # If we have more segments than colors, distribute intelligently
        color_distribution = []
        num_colors = len(self.colors)
        
        # Calculate how many times each color should appear
        times_per_color = num_segments // num_colors
        extra_segments = num_segments % num_colors
        
        # Create a list of color indices with their usage counts
        color_usage = [times_per_color] * num_colors
        for i in range(extra_segments):
            color_usage[i] += 1
        
        # Distribute colors to maximize spacing between same colors
        used_colors = [0] * num_colors  # Track how many times each color has been used
        
        for i in range(num_segments):
            # Find the best color for this position
            # Avoid the previous color if possible
            prev_color_idx = None
            if i > 0:
                prev_color_idx = self.colors.index(color_distribution[i - 1])
            
            # Also avoid the first color when placing the last segment (wraparound)
            avoid_wraparound = None
            if i == num_segments - 1 and num_segments > 1:
                avoid_wraparound = self.colors.index(color_distribution[0])
            
            # Find available colors (ones we still need to use)
            available = [idx for idx in range(num_colors) if used_colors[idx] < color_usage[idx]]
            
            # Filter out the previous color and wraparound color if possible
            if len(available) > 1:
                if prev_color_idx is not None and prev_color_idx in available:
                    filtered = [idx for idx in available if idx != prev_color_idx]
                    if filtered:
                        available = filtered
                
                if avoid_wraparound is not None and avoid_wraparound in available:
                    filtered = [idx for idx in available if idx != avoid_wraparound]
                    if filtered:
                        available = filtered
            
            # Pick the first available color
            chosen_idx = available[0]
            color_distribution.append(self.colors[chosen_idx])
            used_colors[chosen_idx] += 1
        
        return color_distribution
    
    def _load_font(self, size: int = None) -> ImageFont.FreeTypeFont:
        """
        Load a font that supports Unicode characters.
        Note: PIL/Pillow has limited emoji support - emoji may render as outlined symbols.
        Tries multiple font options with fallback to default.
        """
        if size is None:
            size = self.font_size
        
        cache_key = size
        if cache_key in self._font_cache:
            return self._font_cache[cache_key]
        
        # List of fonts to try, in order of preference
        # These fonts have good Unicode support (emoji will render as black/white symbols)
        font_options = [
            # macOS fonts with best Unicode coverage
            "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",  # Best Unicode support
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            # Linux fonts
            "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",  # Good Unicode
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/unifont/unifont.ttf",
            # Windows fonts
            "Arial Unicode MS",
            # Generic fallbacks
            "Arial",
            "DejaVuSans",
            "Helvetica",
        ]
        
        font = None
        for font_name in font_options:
            try:
                font = ImageFont.truetype(font_name, size)
                break
            except (IOError, OSError):
                continue
        
        # Ultimate fallback to PIL default font
        if font is None:
            font = ImageFont.load_default()
        
        self._font_cache[cache_key] = font
        return font
    
    def get_text_dimensions(self, text: str) -> dict:
        """Get the dimensions of text when rendered"""
        temp_img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
        temp_draw = ImageDraw.Draw(temp_img)
        
        font = self._load_font()
        
        bbox = temp_draw.textbbox((0, 0), text, font=font)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        
        return {
            'width': width,
            'height': height,
            'font': font
        }
    
    def calculate_segment_space(self, radius: int, angle_per_segment: float, text_radius_ratio: float = 0.65) -> dict:
        """Calculate available space for text in a wheel segment"""
        text_radius = radius * text_radius_ratio
        angle_rad = math.radians(angle_per_segment)
        arc_length = text_radius * angle_rad
        radial_space = radius * 0.3
        
        return {
            'arc_length': arc_length,
            'radial_space': radial_space,
            'text_radius': text_radius,
            'angle_degrees': angle_per_segment
        }
    
    def calculate_consistent_text_position(self, radius: int, angle_per_segment: float, labels: List[str]) -> dict:
        """Calculate consistent text position for all labels"""
        needs_outer = False
        
        for label in labels:
            text_dims = self.get_text_dimensions(label)
            inner_space = self.calculate_segment_space(radius, angle_per_segment, 0.65)
            
            text_fits_inner = (text_dims['width'] <= inner_space['arc_length'] * 0.8 and
                              text_dims['height'] <= inner_space['radial_space'])
            
            if not text_fits_inner:
                needs_outer = True
                break
        
        position_ratio = 0.85 if needs_outer else 0.65
        position_name = 'outer' if needs_outer else 'inner'
        
        space = self.calculate_segment_space(radius, angle_per_segment, position_ratio)
        
        return {
            'text_radius_ratio': position_ratio,
            'text_radius': space['text_radius'],
            'position': position_name,
            'consistent': True
        }
    
    def draw_segment_label(self, draw, center: int, radius: int, angle: float, label: str, 
                          angle_per_segment: float, consistent_position: dict):
        """Draw a text label on a wheel segment"""
        angle_rad = math.radians(angle)
        
        text_radius = consistent_position['text_radius']
        text_x = center + text_radius * math.cos(angle_rad)
        text_y = center + text_radius * math.sin(angle_rad)
        
        text_dims = self.get_text_dimensions(label)
        font = text_dims['font']
        
        # Create temporary image for rotated text
        temp_img = Image.new('RGBA', (200, 50), (0, 0, 0, 0))
        temp_draw = ImageDraw.Draw(temp_img)
        temp_draw.text((100, 25), label, fill='black', font=font, anchor='mm')
        
        # Adjust rotation for readability
        if 90 < (angle % 360) < 270:
            angle += 180
        
        rotated_text = temp_img.rotate(-angle, expand=True)
        
        paste_x = int(text_x - rotated_text.width / 2)
        paste_y = int(text_y - rotated_text.height / 2)
        
        draw._image.paste(rotated_text, (paste_x, paste_y), rotated_text)
    
    def draw_triangle_pointer(self, draw, center: int, radius: int):
        """Draw a triangle pointer at the 3 o'clock position"""
        leftest_point = center + radius * 0.95
        rightest_point = self.size * 0.99
        triangle_y = center
        size = self.size - leftest_point
        
        triangle_points = [
            (leftest_point, triangle_y),
            (rightest_point, triangle_y - size / 2),
            (rightest_point, triangle_y + size / 2)
        ]
        
        draw.polygon(triangle_points, fill='white', outline='black', width=1)
    
    def create_wheel_frame(self, segments: int, rotation_angle: float, labels: List[str]) -> Image.Image:
        """Create a single frame of the wheel"""
        img = Image.new('RGBA', (self.size, self.size), self.transparent_color)
        draw = ImageDraw.Draw(img)
        
        center = self.size // 2
        radius = self.size // 2 - 20
        angle_per_segment = self.circle_degrees / segments
        
        consistent_position = self.calculate_consistent_text_position(radius, angle_per_segment, labels)
        
        # Get intelligent color distribution
        segment_colors = self.distribute_colors(segments)
        
        for i in range(segments):
            start_angle = rotation_angle + (i * angle_per_segment)
            end_angle = start_angle + angle_per_segment
            
            # Draw pie slice with intelligently distributed color
            draw.pieslice(
                [center - radius, center - radius, center + radius, center + radius],
                start_angle, end_angle,
                fill=segment_colors[i]
            )
            
            # Add text label
            if i < len(labels):
                mid_angle = start_angle + (angle_per_segment / 2)
                self.draw_segment_label(draw, center, radius, mid_angle, labels[i], 
                                      angle_per_segment, consistent_position)
        
        # Draw center circle
        draw.ellipse([center-radius/10, center-radius/10, center+radius/10, center+radius/10], 
                     fill='white')
        
        # Draw triangle pointer
        self.draw_triangle_pointer(draw, center, radius)
        
        return img
    
    def calculate_frames(self, segments: int) -> int:
        """Calculate number of animation frames based on segment count"""
        base_frames = 60
        base_segments = 8
        frame_multiplier = max(1.0, segments / base_segments * 0.27)
        return int(base_frames * frame_multiplier * self.animation_speed)
    
    def create_gif(self, labels: List[str], start_rotation: float, output_file: str) -> int:
        """Create the animated GIF"""
        segments = len(labels)
        num_frames = self.calculate_frames(segments)
        frames = []
        
        print(f"Generating {num_frames} frames for {segments} segments...")
        
        for i in range(num_frames):
            progress = i / num_frames
            eased_progress = 1 - (1 - progress) ** 3  # Cubic easing
            rotation = start_rotation + (eased_progress * 2 * self.circle_degrees)
            
            frame = self.create_wheel_frame(segments, rotation, labels)
            frames.append(frame)
        
        # Save animated GIF
        frames[0].save(
            output_file,
            format='GIF',
            append_images=frames[1:],
            save_all=True,
            duration=50,
            transparency=0,
            disposal=2
        )
        
        return num_frames
    
    def calculate_winner(self, start_rotation: float, segments: List[str]) -> Tuple[int, str]:
        """Calculate which segment wins"""
        angle_per_segment = self.circle_degrees / len(segments)
        relative_angle = (0 - start_rotation) % self.circle_degrees  # Pointer at 0 degrees
        segment_index = int(relative_angle / angle_per_segment) % len(segments)
        
        return segment_index, segments[segment_index]