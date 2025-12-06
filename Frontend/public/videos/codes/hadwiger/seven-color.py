"""
Hadwiger-Nelson: 7 Colors Work - Hexagonal Tiling
Run: manim -pql hadwiger_nelson_7_colors.py SevenColorsWork
"""

from manim import *

class SevenColorsWork(Scene):
    def construct(self):
        # Title
        title = Text("7 Colors Work!", font_size=44, color=GREEN)
        self.play(FadeIn(title, scale=0.8), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(title), run_time=0.4)
        
        # 7 colors
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
            pattern = [[0,1,2], [3,4,5], [6,0,1], [2,3,4], [5,6,0], [1,2,3], [4,5,6]]
            return pattern[row % 7][col % 3]
        
        hex_size = 0.38
        horiz = hex_size * np.sqrt(3)
        vert = hex_size * 1.5
        
        hexagons = VGroup()
        rows, cols = 10, 12
        cx, cy = -horiz * cols / 2, -vert * rows / 2 + 0.3
        
        for row in range(rows):
            for col in range(cols):
                x = cx + col * horiz + (horiz / 2 if row % 2 else 0)
                y = cy + row * vert
                color_idx = get_color_index(row, col)
                hexagons.add(create_hexagon(np.array([x, y, 0]), hex_size, colors[color_idx]))
        
        # Animate hexagons appearing row by row
        self.play(
            LaggedStart(*[FadeIn(h, scale=0.5) for h in hexagons], lag_ratio=0.008),
            run_time=2
        )
        self.wait(0.5)
        
        # Explanation text
        rule = Text("Each hexagon has diameter < 1", font_size=24, color=WHITE)
        rule.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(rule), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(rule), run_time=0.3)
        
        rule2 = Text("Same colors are always > 1 apart", font_size=24, color=WHITE)
        rule2.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(rule2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(rule2), run_time=0.3)
        
        # Show unit distance circle moving around
        point = Dot(LEFT * 2 + DOWN * 0.5, radius=0.1, color=WHITE).set_z_index(10)
        circle = Circle(radius=hex_size * 2.8, color=RED, stroke_width=3)
        circle.move_to(point.get_center())
        
        label = Text("unit distance", font_size=18, color=RED)
        label.next_to(circle, UP, buff=0.1)
        
        self.play(Create(point), Create(circle), FadeIn(label), run_time=0.6)
        self.wait(0.5)
        
        # Move around smoothly
        path = [
            LEFT * 2 + DOWN * 0.5,
            LEFT * 0.5 + UP * 1,
            RIGHT * 1.5 + UP * 0.3,
            RIGHT * 2 + DOWN * 1,
            ORIGIN,
        ]
        
        for target in path:
            self.play(
                point.animate.move_to(target),
                circle.animate.move_to(target),
                label.animate.next_to(Circle(radius=hex_size*2.8).move_to(target), UP, buff=0.1),
                run_time=0.8
            )
            self.wait(0.3)
        
        self.play(FadeOut(point), FadeOut(circle), FadeOut(label), run_time=0.4)
        
        # Highlight same-colored hexagons to show they're far apart
        highlight_text = Text("Same color = far apart", font_size=26, color=YELLOW)
        highlight_text.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(highlight_text), run_time=0.4)
        
        # Find red hexagons and pulse them
        red_hexes = [h for i, h in enumerate(hexagons) if get_color_index(i // cols, i % cols) == 0]
        
        self.play(
            *[h.animate.set_stroke(color=WHITE, width=4) for h in red_hexes[:8]],
            run_time=0.6
        )
        self.wait(0.6)
        self.play(
            *[h.animate.set_stroke(color=WHITE, width=1) for h in red_hexes[:8]],
            run_time=0.4
        )
        
        self.play(FadeOut(highlight_text), run_time=0.3)
        
        # Final checkmark
        check = Text("✓", font_size=100, color=GREEN)
        check.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(check, scale=1.3), run_time=0.5)
        
        self.wait(1)


if __name__ == "__main__":
    pass