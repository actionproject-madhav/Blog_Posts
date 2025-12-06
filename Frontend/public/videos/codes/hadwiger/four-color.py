"""
Hadwiger-Nelson: 4 Colors Fail - de Grey 2018 (Short)
Run: manim -pql hadwiger_nelson_4_colors.py FourColorsFail
"""

from manim import *

class FourColorsFail(Scene):
    def construct(self):
        # Quick title
        title = Text("Why 4 Colors Fail", font_size=44, color=YELLOW)
        self.play(FadeIn(title, scale=0.8), run_time=0.5)
        self.wait(0.3)
        self.play(FadeOut(title), run_time=0.3)
        
        # Show Moser spindle as building block
        scale = 0.8
        A = np.array([0, 0, 0])
        B = np.array([-0.5, 0.866, 0]) * scale
        C = np.array([-0.5, -0.866, 0]) * scale
        D = np.array([-1.5, 0, 0]) * scale
        E = np.array([0.5, 0.866, 0]) * scale
        F = np.array([0.5, -0.866, 0]) * scale
        G = np.array([1.5, 0, 0]) * scale
        
        vertices = [A, B, C, D, E, F, G]
        edges = [(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(4,5),(4,6),(5,6),(3,6)]
        
        spindle = VGroup()
        for e in edges:
            spindle.add(Line(vertices[e[0]], vertices[e[1]], color=BLUE, stroke_width=2))
        for v in vertices:
            spindle.add(Dot(v, radius=0.08, color=WHITE))
        
        spindle.shift(LEFT * 3 + UP * 1.5)
        label1 = Text("Moser Spindle", font_size=20).next_to(spindle, DOWN)
        
        self.play(Create(spindle), Write(label1), run_time=0.6)
        self.wait(0.3)
        
        # Arrow
        arrow = Arrow(LEFT * 1.5 + UP * 1.5, RIGHT * 0.5 + UP * 1.5, color=WHITE)
        self.play(Create(arrow), run_time=0.3)
        
        # Big messy graph (representation of 1581 vertices)
        np.random.seed(42)
        big_graph = VGroup()
        for _ in range(150):
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-1.5, 1.5)
            big_graph.add(Dot([x + 2.5, y, 0], radius=0.025, color=WHITE))
        
        for i in range(80):
            j, k = np.random.randint(0, 150), np.random.randint(0, 150)
            if j != k:
                big_graph.add(Line(
                    big_graph[j].get_center(),
                    big_graph[k].get_center(),
                    color=BLUE, stroke_width=0.3, stroke_opacity=0.4
                ))
        
        self.play(FadeIn(big_graph), run_time=0.8)
        
        label2 = Text("1581 vertices", font_size=24, color=YELLOW).next_to(big_graph, DOWN)
        self.play(Write(label2), run_time=0.3)
        
        self.wait(0.4)
        
        # Try coloring - show 4 colors aren't enough
        colors_text = Text("4 colors?", font_size=32).to_edge(DOWN)
        self.play(Write(colors_text), run_time=0.3)
        
        # Color some dots
        color_list = [RED, BLUE, GREEN, PURPLE]
        for i, dot in enumerate(big_graph[:50]):
            if isinstance(dot, Dot):
                dot.set_color(color_list[i % 4])
        
        self.play(big_graph.animate, run_time=0.5)
        
        # X mark
        x_mark = Text("✗", font_size=80, color=RED).move_to(big_graph.get_center())
        self.play(FadeIn(x_mark, scale=1.5), run_time=0.3)
        
        self.wait(0.3)
        
        # Credit
        credit = Text("Aubrey de Grey, 2018", font_size=20, color=GRAY).to_corner(DR)
        self.play(FadeIn(credit), run_time=0.3)
        
        self.wait(0.5)


if __name__ == "__main__":
    pass