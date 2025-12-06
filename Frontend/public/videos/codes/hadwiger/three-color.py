"""
Hadwiger-Nelson: 3 Colors Fail - Moser Spindle (Short)
Run: manim -pql hadwiger_nelson_3_colors.py ThreeColorsFail
"""

from manim import *

class ThreeColorsFail(Scene):
    def construct(self):
        # Quick title
        title = Text("Why 3 Colors Fail", font_size=44, color=YELLOW)
        self.play(FadeIn(title, scale=0.8), run_time=0.5)
        self.wait(0.3)
        self.play(FadeOut(title), run_time=0.3)
        
        # Moser Spindle
        scale = 1.4
        
        A = np.array([0, 0, 0])
        B = np.array([-0.5, 0.866, 0]) * scale
        C = np.array([-0.5, -0.866, 0]) * scale
        D = np.array([-1.5, 0, 0]) * scale
        E = np.array([0.5, 0.866, 0]) * scale
        F = np.array([0.5, -0.866, 0]) * scale
        G = np.array([1.5, 0, 0]) * scale
        
        vertices = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G}
        
        edges = [
            ('A', 'B'), ('A', 'C'), ('A', 'E'), ('A', 'F'),
            ('B', 'C'), ('B', 'D'), ('C', 'D'),
            ('E', 'F'), ('E', 'G'), ('F', 'G'),
            ('D', 'G')
        ]
        
        # Draw edges
        edge_lines = VGroup()
        for e in edges:
            line = Line(vertices[e[0]], vertices[e[1]], color=GRAY, stroke_width=3)
            edge_lines.add(line)
        
        # Draw dots
        dots = {}
        for name, pos in vertices.items():
            dots[name] = Dot(pos, radius=0.18, color=WHITE)
        
        self.play(Create(edge_lines), run_time=0.5)
        self.play(*[Create(d) for d in dots.values()], run_time=0.4)
        self.wait(0.3)
        
        # Fast coloring
        self.play(dots['A'].animate.set_color(RED), run_time=0.2)
        self.play(dots['B'].animate.set_color(BLUE), dots['E'].animate.set_color(BLUE), run_time=0.2)
        self.play(dots['C'].animate.set_color(GREEN), dots['F'].animate.set_color(GREEN), run_time=0.2)
        self.play(dots['D'].animate.set_color(RED), dots['G'].animate.set_color(RED), run_time=0.2)
        
        self.wait(0.3)
        
        # Highlight D-G edge - both RED!
        dg_edge = Line(D, G, color=YELLOW, stroke_width=6)
        self.play(Create(dg_edge), run_time=0.3)
        self.play(Flash(dots['D'], color=RED), Flash(dots['G'], color=RED), run_time=0.4)
        
        # X mark
        x_mark = Text("✗", font_size=80, color=RED).shift(DOWN * 2)
        self.play(FadeIn(x_mark, scale=1.5), run_time=0.3)
        
        self.wait(0.5)


if __name__ == "__main__":
    pass