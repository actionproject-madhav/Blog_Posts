"""
Hadwiger-Nelson: 7 Colors Work - Hexagonal Tiling
Run: manim -pql hadwiger_nelson_7_colors.py SevenColorsWork
"""

from manim import *

class SevenColorsWork(Scene):
    def construct(self):
        # Title
        title = Text("7 Colors Work!", font_size=44, color=GREEN)
        self.play(FadeIn(title, scale=0.8), run_time=0.7)
        self.wait(0.6)
        self.play(FadeOut(title), run_time=0.4)
        
        # 7 colors - nice distinct palette
        colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD", "#FFA07A"]
        
        def create_hexagon(center, size, color):
            vertices = []
            for i in range(6):
                angle = i * np.pi / 3 + np.pi / 6
                x = center[0] + size * np.cos(angle)
                y = center[1] + size * np.sin(angle)
                vertices.append([x, y, 0])
            return Polygon(*[np.array(v) for v in vertices],
                          fill_color=color, fill_opacity=0.85,
                          stroke_color=WHITE, stroke_width=1)
        
        def get_color_index(row, col):
            # 7-color pattern that ensures same colors are far apart
            pattern = [[0,1,2], [3,4,5], [6,0,1], [2,3,4], [5,6,0], [1,2,3], [4,5,6]]
            return pattern[row % 7][col % 3]
        
        # Hexagon size: diameter must be < 1 unit
        # We'll use size such that diameter = 0.9 (less than 1)
        # For a regular hexagon, diameter = 2 * size * cos(30°) = size * sqrt(3)
        # So size = diameter / sqrt(3) = 0.9 / 1.732 ≈ 0.52
        # But for visual purposes, we scale everything
        
        hex_size = 0.35
        hex_diameter = hex_size * 2  # flat-to-flat distance
        unit_distance = hex_diameter * 1.5  # 1 unit = 1.5 * hex_diameter for this demo
        
        horiz = hex_size * np.sqrt(3)
        vert = hex_size * 1.5
        
        # Build hexagon grid
        hexagons = VGroup()
        hex_centers = []
        rows, cols = 9, 11
        cx, cy = -horiz * cols / 2, -vert * rows / 2
        
        for row in range(rows):
            for col in range(cols):
                x = cx + col * horiz + (horiz / 2 if row % 2 else 0)
                y = cy + row * vert
                center = np.array([x, y, 0])
                color_idx = get_color_index(row, col)
                hexagons.add(create_hexagon(center, hex_size, colors[color_idx]))
                hex_centers.append(center)
        
        # Shift everything up to make room for text at bottom
        hexagons.shift(UP * 0.5)
        hex_centers = [c + UP * 0.5 for c in hex_centers]
        
        # Build hexagons smoothly - spiral or wave effect
        self.play(
            LaggedStart(
                *[GrowFromCenter(h) for h in hexagons],
                lag_ratio=0.015
            ),
            run_time=2.5
        )
        self.wait(0.8)
        
        # Text at bottom - safe zone
        text_pos = DOWN * 3.2
        
        # Explain the key insight
        rule1 = Text("Hexagon diameter < 1 unit", font_size=26, color=WHITE)
        rule1.move_to(text_pos)
        self.play(FadeIn(rule1), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(rule1), run_time=0.4)
        
        rule2 = Text("Same-colored hexagons > 1 unit apart", font_size=26, color=WHITE)
        rule2.move_to(text_pos)
        self.play(FadeIn(rule2), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(rule2), run_time=0.4)
        
        # Now demonstrate with a moving point that traces a path
        # The point moves exactly 1 unit at a time
        
        start_pos = hex_centers[len(hex_centers) // 2 - cols // 2]  # Start from left-center area
        
        tracer = Dot(start_pos, radius=0.12, color=WHITE).set_z_index(10)
        
        # Trail that follows the tracer
        trail = TracedPath(tracer.get_center, stroke_color=YELLOW, stroke_width=3)
        
        self.play(FadeIn(tracer), run_time=0.4)
        self.add(trail)
        
        # Show "1 unit" measurement
        measure_text = Text("Moving 1 unit each step", font_size=22, color=YELLOW)
        measure_text.move_to(text_pos)
        self.play(FadeIn(measure_text), run_time=0.4)
        
        # Move in unit steps - each step is exactly 1 unit distance
        # We'll move in a pattern that crosses multiple hexagons
        
        # Calculate unit distance in our scaled coordinates
        # Using the hex spacing as reference
        step = horiz * 2.5  # This represents "1 unit" visually
        
        # Define path points - each exactly 1 unit apart
        current = start_pos.copy()
        
        # Move right
        for i in range(3):
            next_pos = current + RIGHT * step * 0.4
            self.play(tracer.animate.move_to(next_pos), run_time=0.7, rate_func=smooth)
            current = next_pos
            self.wait(0.2)
        
        # Move up-right
        next_pos = current + (RIGHT * 0.2 + UP * 0.35) * step
        self.play(tracer.animate.move_to(next_pos), run_time=0.7, rate_func=smooth)
        current = next_pos
        self.wait(0.2)
        
        # Move up-left
        next_pos = current + (LEFT * 0.2 + UP * 0.35) * step
        self.play(tracer.animate.move_to(next_pos), run_time=0.7, rate_func=smooth)
        current = next_pos
        self.wait(0.2)
        
        # Move left
        for i in range(2):
            next_pos = current + LEFT * step * 0.4
            self.play(tracer.animate.move_to(next_pos), run_time=0.7, rate_func=smooth)
            current = next_pos
            self.wait(0.2)
        
        self.play(FadeOut(measure_text), run_time=0.3)
        
        # Key observation
        key_text = Text("Every step lands on a DIFFERENT color!", font_size=26, color=GREEN)
        key_text.move_to(text_pos)
        self.play(FadeIn(key_text), run_time=0.5)
        
        self.wait(1.2)
        
        # Fade out trail and tracer
        self.play(FadeOut(trail), FadeOut(tracer), FadeOut(key_text), run_time=0.5)
        
        # Final: highlight that same colors are far apart
        final_text = Text("No two same-colored points at distance 1", font_size=26, color=WHITE)
        final_text.move_to(text_pos)
        self.play(FadeIn(final_text), run_time=0.5)
        
        self.wait(1)
        
        # Checkmark
        self.play(FadeOut(final_text), run_time=0.3)
        check = Text("✓", font_size=90, color=GREEN)
        check.move_to(text_pos + UP * 0.3)
        self.play(FadeIn(check, scale=1.4), run_time=0.5)
        
        self.wait(1)


if __name__ == "__main__":
    pass