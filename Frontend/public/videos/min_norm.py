from manim import *
import numpy as np

class MinimumNormDemo(Scene):
    def construct(self):
        # Title
        title = Text("Minimum Norm Attack", font_size=42, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Show the optimization problem
        self.show_optimization_problem()
        self.wait(2)
        
        # Visualize decision boundary
        self.visualize_decision_boundary()
        self.wait(2)
        
        # Show minimum perturbation
        self.show_minimum_perturbation()
        self.wait(2)
        
        # Final summary
        self.show_summary()
        self.wait(2)
        
    def show_optimization_problem(self):
        # Optimization problem
        problem = Text(
            "min_x ||x - x₀||",
            font_size=38
        )
        problem.shift(UP * 0.5)
        
        constraint = Text(
            "subject to: max_j≠t g_j(x) - g_t(x) ≤ 0",
            font_size=30
        )
        constraint.next_to(problem, DOWN, buff=0.7)
        
        self.play(Write(problem))
        self.wait(1)
        self.play(Write(constraint))
        self.wait(1)
        
        # Explanation boxes - positioned well below
        obj_explanation = Text(
            "Minimize perturbation size",
            font_size=26,
            color=BLUE
        )
        obj_explanation.shift(DOWN * 1.5)
        
        constraint_explanation = Text(
            "While ensuring misclassification",
            font_size=26,
            color=RED
        )
        constraint_explanation.next_to(obj_explanation, DOWN, buff=0.6)
        
        self.play(FadeIn(obj_explanation))
        self.wait(0.5)
        self.play(FadeIn(constraint_explanation))
        self.wait(1.5)
        
        # Store and clear
        self.problem_group = VGroup(
            problem, constraint, obj_explanation, constraint_explanation
        )
        self.play(FadeOut(self.problem_group))
        self.wait(0.5)
        
    def visualize_decision_boundary(self):
        # Create axes - smaller to leave room for labels
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=5,
            axis_config={"include_tip": False, "stroke_width": 2},
        ).shift(DOWN * 0.5)
        
        self.play(Create(axes), run_time=1)
        
        # Decision boundary (curved line)
        boundary = axes.plot(
            lambda x: 0.3 * x**2 - 1.5,
            x_range=[-3, 3],
            color=YELLOW,
            stroke_width=5
        )
        
        boundary_label = Text("Decision Boundary", font_size=22, color=YELLOW)
        boundary_label.move_to(axes.c2p(-1.5, 2))
        
        self.play(Create(boundary), Write(boundary_label))
        self.wait(1)
        
        # Class regions with actual images
        cat_img = ImageMobject("cat_icon.png")
        cat_img.scale(0.35)
        cat_img.move_to(axes.c2p(-2.5, -2.2))
        
        cat_region = Text("Cat Region", font_size=20, color=BLUE)
        cat_region.move_to(axes.c2p(-2.5, -1.4))
        
        dog_img = ImageMobject("dog_icon.png")
        dog_img.scale(0.35)
        dog_img.move_to(axes.c2p(2.3, 1.8))
        
        dog_region = Text("Dog Region", font_size=20, color=GREEN)
        dog_region.move_to(axes.c2p(2.3, 1.0))
        
        self.play(FadeIn(cat_img), FadeIn(cat_region))
        self.play(FadeIn(dog_img), FadeIn(dog_region))
        self.wait(1)
        
        # Original point x0
        x0_point = Dot(axes.c2p(-1, -2), color=BLUE, radius=0.12)
        x0_label = Text("x₀", font_size=28, color=BLUE)
        x0_label.next_to(x0_point, LEFT, buff=0.3)
        
        self.play(FadeIn(x0_point), Write(x0_label))
        self.wait(1)
        
        # Store for next scene
        self.axes = axes
        self.boundary = boundary
        self.boundary_label = boundary_label
        self.cat_img = cat_img
        self.cat_region = cat_region
        self.dog_img = dog_img
        self.dog_region = dog_region
        self.x0_point = x0_point
        self.x0_label = x0_label
        
    def show_minimum_perturbation(self):
        # Show large perturbation first
        large_pert_point = Dot(self.axes.c2p(1.8, 1.3), color=RED, radius=0.1)
        large_pert_arrow = Arrow(
            self.x0_point.get_center(),
            large_pert_point.get_center(),
            buff=0.1,
            color=RED,
            stroke_width=4
        )
        large_pert_label = Text("Large\nperturbation", font_size=18, color=RED)
        large_pert_label.move_to(self.axes.c2p(3.2, 0.3))
        
        self.play(
            GrowArrow(large_pert_arrow),
            FadeIn(large_pert_point),
            Write(large_pert_label)
        )
        self.wait(1)
        
        # Cross it out
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT, color=RED, stroke_width=6),
            Line(UP + RIGHT, DOWN + LEFT, color=RED, stroke_width=6)
        ).scale(0.3)
        cross.move_to(large_pert_point)
        self.play(Create(cross))
        self.wait(0.5)
        
        # Fade out large perturbation
        self.play(
            FadeOut(large_pert_arrow),
            FadeOut(large_pert_point),
            FadeOut(large_pert_label),
            FadeOut(cross)
        )
        self.wait(0.3)
        
        # Show optimal (minimum) perturbation
        optimal_point = Dot(self.axes.c2p(-0.3, -0.4), color=GREEN, radius=0.12)
        optimal_arrow = Arrow(
            self.x0_point.get_center(),
            optimal_point.get_center(),
            buff=0.1,
            color=GREEN,
            stroke_width=6
        )
        
        optimal_label = Text("x*", font_size=28, color=GREEN)
        optimal_label.next_to(optimal_point, UP, buff=0.3)
        
        min_pert_text = Text("Minimum\nperturbation", font_size=18, color=GREEN)
        min_pert_text.move_to(self.axes.c2p(2.1, -1))
        
        self.play(
            GrowArrow(optimal_arrow),
            FadeIn(optimal_point),
            Write(optimal_label)
        )
        self.wait(0.5)
        self.play(Write(min_pert_text))
        self.wait(1)
        
        # Highlight that it crosses boundary
        circle = Circle(radius=0.3, color=YELLOW, stroke_width=4)
        circle.move_to(optimal_point)
        self.play(Create(circle), run_time=0.8)
        self.play(FadeOut(circle))
        self.wait(1)
        
        # Store for cleanup
        self.optimal_arrow = optimal_arrow
        self.optimal_point = optimal_point
        self.optimal_label = optimal_label
        self.min_pert_text = min_pert_text
        
    def show_summary(self):
        # Clear visualization
        self.play(
            *[FadeOut(mob) for mob in [
                self.axes, self.boundary, self.boundary_label,
                self.cat_img, self.cat_region, 
                self.dog_img, self.dog_region,
                self.x0_point, self.x0_label,
                self.optimal_arrow, self.optimal_point,
                self.optimal_label, self.min_pert_text
            ]]
        )
        self.wait(0.5)
        
        # Key insight - better spacing
        insight1 = Text(
            "Minimum Norm Attack finds the",
            font_size=32
        )
        insight1.shift(UP * 1.8)
        
        insight2 = Text(
            "SMALLEST possible perturbation",
            font_size=36,
            color=BLUE,
            weight=BOLD
        )
        insight2.next_to(insight1, DOWN, buff=0.5)
        
        insight3 = Text(
            "that crosses the decision boundary",
            font_size=32
        )
        insight3.next_to(insight2, DOWN, buff=0.5)
        
        # Formula - positioned lower
        formula = Text(
            "||x* - x₀|| = minimum",
            font_size=40,
            color=GREEN
        )
        formula.shift(DOWN * 1.8)
        
        self.play(Write(insight1))
        self.wait(0.3)
        self.play(Write(insight2))
        self.wait(0.3)
        self.play(Write(insight3))
        self.wait(0.8)
        self.play(Write(formula))
        self.wait(2)