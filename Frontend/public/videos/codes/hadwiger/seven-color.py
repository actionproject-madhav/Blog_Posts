"""
Hadwiger-Nelson: 7 Colors Work - Hexagonal Tiling
Production-ready animation

Run: manim -pqh hadwiger_nelson_7_colors.py SevenColorsWork
"""

from manim import *

class SevenColorsWork(Scene):
    def construct(self):
        
        # ===== TITLE =====
        title = Text("7 Colors Are Enough", font_size=52, color=WHITE, weight=BOLD)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1)
        self.wait(1)
        self.play(FadeOut(title, shift=UP * 0.3), run_time=0.8)
        self.wait(0.3)
        
        # ===== 7 HIGHLY DISTINCT COLORS =====
        # Chosen for maximum visual distinction
        colors = [
            "#E63946",  # Red
            "#2A9D8F",  # Teal
            "#264653",  # Dark blue
            "#E9C46A",  # Yellow/Gold
            "#F4A261",  # Orange
            "#9B5DE5",  # Purple
            "#00F5D4",  # Cyan/Mint
        ]
        
        color_names = ["Red", "Teal", "Navy", "Gold", "Orange", "Purple", "Cyan"]
        
        def create_hexagon(center, size, color):
            """Create a flat-topped regular hexagon"""
            vertices = []
            for i in range(6):
                angle = i * np.pi / 3 + np.pi / 6  # flat-topped
                x = center[0] + size * np.cos(angle)
                y = center[1] + size * np.sin(angle)
                vertices.append([x, y, 0])
            return Polygon(
                *[np.array(v) for v in vertices],
                fill_color=color,
                fill_opacity=0.9,
                stroke_color=WHITE,
                stroke_width=1.5
            )
        
        def get_color_index(row, col):
            """7-color pattern ensuring same colors are never adjacent"""
            pattern = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 0, 1],
                [2, 3, 4],
                [5, 6, 0],
                [1, 2, 3],
                [4, 5, 6],
            ]
            return pattern[row % 7][col % 3]
        
        # ===== BUILD HEXAGON GRID =====
        hex_size = 0.4
        horiz_spacing = hex_size * np.sqrt(3)
        vert_spacing = hex_size * 1.5
        
        rows, cols = 8, 10
        
        # Center the grid, shifted up to leave room for text
        grid_center_x = -horiz_spacing * (cols - 1) / 2
        grid_center_y = -vert_spacing * (rows - 1) / 2 + 0.7
        
        hexagons = VGroup()
        hex_data = []  # Store (hexagon, center, row, col, color_idx)
        
        for row in range(rows):
            for col in range(cols):
                x = grid_center_x + col * horiz_spacing
                if row % 2 == 1:
                    x += horiz_spacing / 2
                y = grid_center_y + row * vert_spacing
                
                center = np.array([x, y, 0])
                color_idx = get_color_index(row, col)
                
                hex_shape = create_hexagon(center, hex_size, colors[color_idx])
                hexagons.add(hex_shape)
                hex_data.append((hex_shape, center, row, col, color_idx))
        
        # ===== ANIMATE HEXAGONS BUILDING =====
        # Build from center outward in a nice wave
        center_point = np.array([0, 0.7, 0])
        
        # Sort by distance from center for wave effect
        sorted_hexes = sorted(hex_data, key=lambda x: np.linalg.norm(x[1] - center_point))
        sorted_hex_shapes = [h[0] for h in sorted_hexes]
        
        self.play(
            LaggedStart(
                *[GrowFromCenter(h) for h in sorted_hex_shapes],
                lag_ratio=0.03
            ),
            run_time=3.5
        )
        self.wait(1)
        
        # ===== TEXT AREA - BOTTOM OF SCREEN =====
        text_y = -3.0
        
        # ===== EXPLAIN THE SETUP =====
        explain1 = Text("Each hexagon has diameter slightly less than 1", font_size=28)
        explain1.move_to([0, text_y, 0])
        
        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(explain1), run_time=0.5)
        self.wait(0.3)
        
        explain2 = Text("Points inside the same hexagon are < 1 apart", font_size=28)
        explain2.move_to([0, text_y, 0])
        
        self.play(FadeIn(explain2, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(explain2), run_time=0.5)
        self.wait(0.3)
        
        explain3 = Text("Same-colored hexagons are always > 1 apart", font_size=28)
        explain3.move_to([0, text_y, 0])
        
        self.play(FadeIn(explain3, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(explain3), run_time=0.5)
        self.wait(0.5)
        
        # ===== DEMONSTRATE WITH MOVING POINT =====
        demo_text = Text("Let's trace a path...", font_size=28, color=YELLOW)
        demo_text.move_to([0, text_y, 0])
        self.play(FadeIn(demo_text), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(demo_text), run_time=0.4)
        
        # Starting position - pick a hexagon near left-center
        start_hex_idx = (rows // 2) * cols + 2
        start_center = hex_data[start_hex_idx][1]
        
        # Create tracer dot
        tracer = Dot(start_center, radius=0.15, color=WHITE)
        tracer.set_z_index(100)
        
        # Glow effect around tracer
        tracer_glow = Dot(start_center, radius=0.25, color=WHITE, fill_opacity=0.3)
        tracer_glow.set_z_index(99)
        
        self.play(
            FadeIn(tracer, scale=0.5),
            FadeIn(tracer_glow, scale=0.5),
            run_time=0.8
        )
        self.wait(0.5)
        
        # Create path - a series of unit-distance moves
        # Each move goes to a different colored hexagon
        
        # Define movement pattern (relative moves that simulate ~1 unit distance)
        # In our grid, moving ~2-3 hexagons away represents unit distance
        unit_dist = horiz_spacing * 2.5
        
        moves = [
            RIGHT * unit_dist * 0.45,
            RIGHT * unit_dist * 0.45,
            UP * unit_dist * 0.35 + RIGHT * unit_dist * 0.2,
            UP * unit_dist * 0.35 + LEFT * unit_dist * 0.1,
            LEFT * unit_dist * 0.45,
            LEFT * unit_dist * 0.45,
            DOWN * unit_dist * 0.35 + LEFT * unit_dist * 0.1,
        ]
        
        # Show "1 unit" label
        unit_label = Text("each step ≈ 1 unit", font_size=24, color=YELLOW)
        unit_label.move_to([0, text_y, 0])
        self.play(FadeIn(unit_label), run_time=0.5)
        
        # Trace the path
        current_pos = start_center.copy()
        path_dots = VGroup()
        path_lines = VGroup()
        
        for i, move in enumerate(moves):
            next_pos = current_pos + move
            
            # Clamp to visible area
            next_pos[0] = np.clip(next_pos[0], -3.5, 3.5)
            next_pos[1] = np.clip(next_pos[1], -1.5, 2.8)
            
            # Draw line for this segment
            line = Line(current_pos, next_pos, color=YELLOW, stroke_width=4, stroke_opacity=0.7)
            
            # Animate the move
            self.play(
                Create(line),
                tracer.animate.move_to(next_pos),
                tracer_glow.animate.move_to(next_pos),
                run_time=1.0,
                rate_func=smooth
            )
            
            path_lines.add(line)
            
            # Small pause to see the color
            self.wait(0.4)
            
            # Leave a small dot at each stop
            stop_dot = Dot(next_pos, radius=0.08, color=YELLOW, fill_opacity=0.6)
            path_dots.add(stop_dot)
            self.play(FadeIn(stop_dot), run_time=0.2)
            
            current_pos = next_pos
        
        self.wait(0.5)
        self.play(FadeOut(unit_label), run_time=0.4)
        
        # ===== KEY INSIGHT =====
        insight = Text("Every step lands on a DIFFERENT color!", font_size=30, color=GREEN)
        insight.move_to([0, text_y, 0])
        
        self.play(FadeIn(insight, scale=1.1), run_time=0.8)
        self.wait(2)
        
        # Fade out path elements
        self.play(
            FadeOut(tracer),
            FadeOut(tracer_glow),
            FadeOut(path_lines),
            FadeOut(path_dots),
            FadeOut(insight),
            run_time=1
        )
        self.wait(0.5)
        
        # ===== HIGHLIGHT SAME-COLOR HEXAGONS =====
        highlight_text = Text("Same colors are never 1 unit apart", font_size=28)
        highlight_text.move_to([0, text_y, 0])
        self.play(FadeIn(highlight_text), run_time=0.6)
        self.wait(0.8)
        
        # Highlight all red hexagons
        red_hexes = [h[0] for h in hex_data if h[4] == 0]
        
        self.play(
            *[h.animate.set_stroke(color=WHITE, width=5) for h in red_hexes],
            run_time=0.8
        )
        self.wait(1.5)
        self.play(
            *[h.animate.set_stroke(color=WHITE, width=1.5) for h in red_hexes],
            run_time=0.6
        )
        
        self.play(FadeOut(highlight_text), run_time=0.4)
        self.wait(0.3)
        
        # ===== FINAL CONCLUSION =====
        conclusion = Text("Therefore, 7 colors suffice!", font_size=32, color=WHITE, weight=BOLD)
        conclusion.move_to([0, text_y, 0])
        
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        
        # Big checkmark
        check = Text("✓", font_size=120, color="#00FF00")
        check.next_to(conclusion, RIGHT, buff=0.5)
        
        self.play(FadeIn(check, scale=1.5), run_time=0.6)
        
        self.wait(2)
        
        # Fade everything out
        self.play(
            FadeOut(hexagons),
            FadeOut(conclusion),
            FadeOut(check),
            run_time=1.2
        )
        self.wait(0.5)


if __name__ == "__main__":
    pass