from manim import *

class HandshakingLemma(Scene):
    def construct(self):
        # Title
        title = Text("The Handshaking Lemma", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create a simple graph with 5 vertices
        # Vertices positioned to avoid overlap
        vertices = {
            "A": np.array([-3, 1, 0]),
            "B": np.array([-1, 2, 0]),
            "C": np.array([1, 1.5, 0]),
            "D": np.array([2.5, 0, 0]),
            "E": np.array([0, -1, 0])
        }
        
        # Create vertex circles with colors
        vertex_colors = {
            "A": RED,
            "B": GREEN,
            "C": YELLOW,
            "D": PURPLE,
            "E": ORANGE
        }
        
        vertex_circles = {}
        vertex_labels = {}
        
        for v, pos in vertices.items():
            circle = Circle(radius=0.3, color=vertex_colors[v], fill_opacity=0.7)
            circle.move_to(pos)
            vertex_circles[v] = circle
            
            label = Text(v, font_size=32, color=WHITE)
            label.move_to(pos)
            vertex_labels[v] = label
        
        # Define edges (connections between vertices)
        edges = [
            ("A", "B"),
            ("A", "E"),
            ("B", "C"),
            ("B", "E"),
            ("C", "D"),
            ("C", "E"),
            ("D", "E")
        ]
        
        # Create edge lines
        edge_lines = []
        for v1, v2 in edges:
            line = Line(
                vertices[v1], 
                vertices[v2], 
                color=WHITE,
                stroke_width=3
            )
            edge_lines.append(line)
        
        # Animate vertices
        self.play(*[Create(circle) for circle in vertex_circles.values()])
        self.play(*[Write(label) for label in vertex_labels.values()])
        self.wait(0.5)
        
        # Animate edges
        self.play(*[Create(line) for line in edge_lines])
        self.wait(1)
        
        # Show degree labels (positioned away from vertices to avoid overlap)
        degree_positions = {
            "A": np.array([-3.8, 1, 0]),
            "B": np.array([-1, 2.8, 0]),
            "C": np.array([1, 2.3, 0]),
            "D": np.array([3.3, 0, 0]),
            "E": np.array([0, -1.8, 0])
        }
        
        degrees = {"A": 2, "B": 3, "C": 3, "D": 2, "E": 4}
        degree_labels = {}
        
        for v, deg in degrees.items():
            deg_text = Text(f"deg={deg}", font_size=24, color=vertex_colors[v])
            deg_text.move_to(degree_positions[v])
            degree_labels[v] = deg_text
        
        self.play(*[Write(deg_label) for deg_label in degree_labels.values()])
        self.wait(1)
        
        # Highlight odd degree vertices
        odd_degree_text = Text("Odd degree vertices", font_size=32, color=YELLOW)
        odd_degree_text.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(odd_degree_text))
        
        # Highlight B and C (odd degrees: 3 and 3)
        self.play(
            vertex_circles["B"].animate.set_stroke(YELLOW, width=5),
            vertex_circles["C"].animate.set_stroke(YELLOW, width=5),
        )
        self.wait(1)
        
        # Show the formula
        self.play(FadeOut(odd_degree_text))
        
        formula1 = Text(
            "Sum of degrees = 2 × (number of edges)",
            font_size=32
        )
        formula1.to_edge(DOWN).shift(UP * 1.5)
        self.play(Write(formula1))
        self.wait(1)
        
        # Calculate sum of degrees
        sum_degrees = sum(degrees.values())
        num_edges = len(edges)
        
        calculation = Text(
            f"{sum_degrees} = 2 × {num_edges}",
            font_size=32,
            color=GREEN
        )
        calculation.next_to(formula1, DOWN, buff=0.3)
        self.play(Write(calculation))
        self.wait(1)
        
        # Key insight
        self.play(
            FadeOut(formula1),
            FadeOut(calculation)
        )
        
        insight = Text(
            "Even number of odd-degree vertices!",
            font_size=36,
            color=YELLOW
        )
        insight.to_edge(DOWN).shift(UP * 0.8)
        self.play(Write(insight))
        self.wait(1)
        
        count_text = Text(
            f"Count: 2 vertices (B, C)",
            font_size=28,
            color=GREEN
        )
        count_text.next_to(insight, DOWN, buff=0.3)
        self.play(Write(count_text))
        self.wait(2)
        
        # Final emphasis
        self.play(
            vertex_circles["B"].animate.set_stroke(YELLOW, width=8).scale(1.2),
            vertex_circles["C"].animate.set_stroke(YELLOW, width=8).scale(1.2),
        )
        self.wait(1)
        
        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
        # Final theorem statement
        theorem = Text(
            "Handshaking Lemma Proven!",
            font_size=48,
            color=BLUE
        )
        self.play(Write(theorem))
        self.wait(2)