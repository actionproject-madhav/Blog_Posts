from manim import *

class HandshakingLemma(Scene):
    def construct(self):
        # Title
        title = Text("The Handshaking Lemma", font_size=42, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)
        
        # Create a simple graph with 5 vertices - positioned in upper half
        vertices = {
            "A": np.array([-3.5, 1.8, 0]),
            "B": np.array([-1.5, 2.5, 0]),
            "C": np.array([1, 2.3, 0]),
            "D": np.array([3, 1.5, 0]),
            "E": np.array([-0.5, 0.8, 0])
        }
        
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
            circle = Circle(radius=0.25, color=vertex_colors[v], fill_opacity=0.8)
            circle.move_to(pos)
            vertex_circles[v] = circle
            
            label = Text(v, font_size=28, color=BLACK, weight=BOLD)
            label.move_to(pos)
            vertex_labels[v] = label
        
        # Define edges
        edges = [
            ("A", "B"),
            ("A", "E"),
            ("B", "C"),
            ("B", "E"),
            ("C", "D"),
            ("C", "E"),
            ("D", "E")
        ]
        
        edge_lines = []
        for v1, v2 in edges:
            line = Line(vertices[v1], vertices[v2], color=BLUE_C, stroke_width=2)
            edge_lines.append(line)
        
        # Animate graph creation
        self.play(*[Create(line) for line in edge_lines])
        self.play(*[Create(circle) for circle in vertex_circles.values()])
        self.play(*[Write(label) for label in vertex_labels.values()])
        self.wait(1)
        
        # Show degree labels
        degree_positions = {
            "A": np.array([-4.2, 1.8, 0]),
            "B": np.array([-1.5, 3.2, 0]),
            "C": np.array([1, 3, 0]),
            "D": np.array([3.7, 1.5, 0]),
            "E": np.array([-0.5, 0.1, 0])
        }
        
        degrees = {"A": 2, "B": 3, "C": 3, "D": 2, "E": 4}
        degree_labels = {}
        
        for v, deg in degrees.items():
            deg_text = Text(f"d={deg}", font_size=20, color=vertex_colors[v])
            deg_text.move_to(degree_positions[v])
            degree_labels[v] = deg_text
        
        self.play(*[Write(deg_label) for deg_label in degree_labels.values()])
        self.wait(1.5)
        
        # PROOF STEP 1: Sum of degrees = 2n
        proof_step1 = Text("Step 1: Sum of all degrees = 2 × (edges)", font_size=28, color=WHITE)
        proof_step1.move_to(np.array([0, -0.8, 0]))
        self.play(Write(proof_step1))
        self.wait(1)
        
        # Show calculation
        sum_degrees = sum(degrees.values())
        num_edges = len(edges)
        
        calc1 = Text(f"Sum = 2 + 3 + 3 + 2 + 4 = {sum_degrees}", font_size=24, color=GREEN)
        calc1.move_to(np.array([0, -1.4, 0]))
        self.play(Write(calc1))
        self.wait(1)
        
        calc2 = Text(f"2 × edges = 2 × {num_edges} = {2*num_edges}", font_size=24, color=GREEN)
        calc2.move_to(np.array([0, -1.9, 0]))
        self.play(Write(calc2))
        self.wait(1.5)
        
        # PROOF STEP 2: Break down by odd and even
        self.play(
            FadeOut(proof_step1),
            FadeOut(calc1),
            FadeOut(calc2)
        )
        
        proof_step2 = Text("Step 2: Separate odd and even degree vertices", font_size=26, color=WHITE)
        proof_step2.move_to(np.array([0, -0.8, 0]))
        self.play(Write(proof_step2))
        self.wait(1)
        
        # Highlight odd degree vertices (B and C with degree 3)
        self.play(
            vertex_circles["B"].animate.set_stroke(YELLOW, width=4),
            vertex_circles["C"].animate.set_stroke(YELLOW, width=4),
        )
        
        odd_label = Text("Odd degrees: B(3) + C(3)", font_size=24, color=YELLOW)
        odd_label.move_to(np.array([-2, -1.5, 0]))
        self.play(Write(odd_label))
        self.wait(1)
        
        # Highlight even degree vertices
        self.play(
            vertex_circles["A"].animate.set_stroke(BLUE, width=4),
            vertex_circles["D"].animate.set_stroke(BLUE, width=4),
            vertex_circles["E"].animate.set_stroke(BLUE, width=4),
        )
        
        even_label = Text("Even degrees: A(2) + D(2) + E(4)", font_size=24, color=BLUE)
        even_label.move_to(np.array([2.2, -1.5, 0]))
        self.play(Write(even_label))
        self.wait(1.5)
        
        # PROOF STEP 3: The equation
        self.play(
            FadeOut(proof_step2),
            FadeOut(odd_label),
            FadeOut(even_label)
        )
        
        equation = Text("Odd sum + Even sum = 2n", font_size=28, color=WHITE)
        equation.move_to(np.array([0, -1, 0]))
        self.play(Write(equation))
        self.wait(1)
        
        equation2 = Text("Odd sum = 2n - Even sum", font_size=28, color=YELLOW)
        equation2.move_to(np.array([0, -1.6, 0]))
        self.play(Write(equation2))
        self.wait(1.5)
        
        # PROOF STEP 4: Key insight
        self.play(
            FadeOut(equation),
            FadeOut(equation2)
        )
        
        insight1 = Text("2n is EVEN", font_size=28, color=GREEN)
        insight1.move_to(np.array([0, -0.9, 0]))
        self.play(Write(insight1))
        self.wait(1)
        
        insight2 = Text("Even sum is EVEN", font_size=28, color=GREEN)
        insight2.move_to(np.array([0, -1.4, 0]))
        self.play(Write(insight2))
        self.wait(1)
        
        insight3 = Text("∴ Odd sum must be EVEN!", font_size=28, color=YELLOW, weight=BOLD)
        insight3.move_to(np.array([0, -1.9, 0]))
        self.play(Write(insight3))
        self.wait(1.5)
        
        # PROOF STEP 5: Final conclusion
        self.play(
            FadeOut(insight1),
            FadeOut(insight2),
            FadeOut(insight3)
        )
        
        conclusion1 = Text("When is sum of odd numbers EVEN?", font_size=26, color=WHITE)
        conclusion1.move_to(np.array([0, -1, 0]))
        self.play(Write(conclusion1))
        self.wait(1)
        
        conclusion2 = Text("Only when there's an EVEN count of them!", font_size=26, color=YELLOW, weight=BOLD)
        conclusion2.move_to(np.array([0, -1.6, 0]))
        self.play(Write(conclusion2))
        self.wait(1)
        
        example = Text("Example: 3 + 3 = 6 (2 odd numbers → even sum)", font_size=22, color=GREEN)
        example.move_to(np.array([0, -2.2, 0]))
        self.play(Write(example))
        self.wait(2)
        
        # Final emphasis on the 2 odd vertices
        self.play(
            vertex_circles["B"].animate.set_stroke(YELLOW, width=6).scale(1.15),
            vertex_circles["C"].animate.set_stroke(YELLOW, width=6).scale(1.15),
        )
        self.wait(2)
        
        # Fade all and show final statement
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        final = Text("Handshaking Lemma: Always an even number\nof odd-degree vertices!", 
                     font_size=36, color=BLUE, line_spacing=1.5)
        self.play(Write(final))
        self.wait(2)