"""
Hadwiger-Nelson Problem: Why 2 Colors Fail
==========================================
An equilateral triangle with unit side length requires 3 colors.
If all edges are unit distance, adjacent vertices must have different colors.
A triangle has 3 mutually adjacent vertices -> needs 3 colors.
"""

from manim import *

class TwoColorsFail(Scene):
    def construct(self):
        # Title
        title = Text("Hadwiger-Nelson Problem", font_size=48)
        subtitle = Text("Why 2 Colors Fail", font_size=36, color=YELLOW)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Explanation
        explanation = Text(
            "Consider an equilateral triangle with unit side length",
            font_size=28
        ).to_edge(UP)
        self.play(Write(explanation))
        
        # Create equilateral triangle with unit edges
        # Vertices of equilateral triangle
        A = np.array([-1.5, -1, 0])
        B = np.array([1.5, -1, 0])
        C = np.array([0, 1.6, 0])  # sqrt(3) ≈ 1.73
        
        # Create triangle
        triangle = Polygon(A, B, C, color=WHITE, stroke_width=3)
        
        # Vertices as dots
        dot_A = Dot(A, radius=0.2, color=WHITE)
        dot_B = Dot(B, radius=0.2, color=WHITE)
        dot_C = Dot(C, radius=0.2, color=WHITE)
        
        # Labels
        label_A = Text("A", font_size=24).next_to(dot_A, DOWN)
        label_B = Text("B", font_size=24).next_to(dot_B, DOWN)
        label_C = Text("C", font_size=24).next_to(dot_C, UP)
        
        # Edge labels (all unit distance)
        edge_AB = Text("1", font_size=20, color=YELLOW).move_to((A + B) / 2 + DOWN * 0.4)
        edge_BC = Text("1", font_size=20, color=YELLOW).move_to((B + C) / 2 + RIGHT * 0.4)
        edge_CA = Text("1", font_size=20, color=YELLOW).move_to((C + A) / 2 + LEFT * 0.4)
        
        self.play(Create(triangle))
        self.play(
            Create(dot_A), Create(dot_B), Create(dot_C),
            Write(label_A), Write(label_B), Write(label_C)
        )
        self.play(Write(edge_AB), Write(edge_BC), Write(edge_CA))
        self.wait(1)
        
        # Now try to color with 2 colors
        rule_text = Text(
            "Rule: Points at distance 1 must have DIFFERENT colors",
            font_size=24, color=RED
        ).to_edge(DOWN, buff=1.5)
        self.play(Write(rule_text))
        self.wait(1)
        
        # Try coloring
        try_text = Text("Let's try with only RED and BLUE...", font_size=24)
        try_text.next_to(rule_text, DOWN)
        self.play(Write(try_text))
        self.wait(0.5)
        
        # Color A red
        step1 = Text("Step 1: Color A = RED", font_size=22, color=RED).to_edge(LEFT).shift(UP)
        self.play(Write(step1))
        self.play(dot_A.animate.set_color(RED))
        self.wait(0.5)
        
        # B must be different from A -> Blue
        step2 = Text("Step 2: B is distance 1 from A → B = BLUE", font_size=22, color=BLUE)
        step2.next_to(step1, DOWN, aligned_edge=LEFT)
        self.play(Write(step2))
        self.play(dot_B.animate.set_color(BLUE))
        self.wait(0.5)
        
        # C must be different from A (dist=1) -> not RED
        # C must be different from B (dist=1) -> not BLUE
        step3 = Text("Step 3: C is distance 1 from A → C ≠ RED", font_size=22)
        step3.next_to(step2, DOWN, aligned_edge=LEFT)
        step4 = Text("         C is distance 1 from B → C ≠ BLUE", font_size=22)
        step4.next_to(step3, DOWN, aligned_edge=LEFT)
        
        self.play(Write(step3))
        self.play(Write(step4))
        self.wait(1)
        
        # Contradiction!
        contradiction = Text(
            "CONTRADICTION! C cannot be RED or BLUE!",
            font_size=32, color=YELLOW
        )
        contradiction.to_edge(DOWN, buff=0.3)
        box = SurroundingRectangle(contradiction, color=RED, buff=0.2)
        
        self.play(
            FadeOut(rule_text), FadeOut(try_text),
            Write(contradiction), Create(box)
        )
        
        # Flash C to show the problem
        self.play(
            dot_C.animate.set_color(RED),
            rate_func=there_and_back,
            run_time=0.5
        )
        self.play(
            dot_C.animate.set_color(BLUE),
            rate_func=there_and_back,
            run_time=0.5
        )
        self.play(Flash(dot_C, color=YELLOW))
        
        self.wait(1)
        
        # Conclusion
        self.play(
            FadeOut(VGroup(step1, step2, step3, step4, explanation)),
            FadeOut(VGroup(triangle, dot_A, dot_B, dot_C)),
            FadeOut(VGroup(label_A, label_B, label_C)),
            FadeOut(VGroup(edge_AB, edge_BC, edge_CA)),
            FadeOut(box), FadeOut(contradiction)
        )
        
        conclusion = Text(
            "Therefore, 2 colors are NOT enough!",
            font_size=40, color=GREEN
        )
        conclusion2 = Text(
            "We need at least 3 colors.",
            font_size=36
        ).next_to(conclusion, DOWN)
        
        self.play(Write(conclusion))
        self.play(Write(conclusion2))
        self.wait(2)


if __name__ == "__main__":
    # Run with: manim -pql hadwiger_nelson_2_colors.py TwoColorsFail
    pass