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
        problem = MathTex(
            r"\min_{x} \|x - x_0\|",
            font_size=40
        )
        problem.shift(UP * 1.5)
        
        constraint = MathTex(
            r"\text{subject to: } \max_{j \neq t} g_j(x) - g_t(x) \leq 0",
            font_size=36
        )
        constraint.next_to(problem, DOWN, buff=0.5)
        
        self.play(Write(problem))
        self.wait(1)
        self.play(Write(constraint))
        self.wait(1)
        
        # Explanation boxes
        obj_explanation = Text(
            "Minimize perturbation size",
            font_size=28,
            color=BLUE
        )
        obj_explanation.next_to(problem, DOWN, buff=1.5)
        
        constraint_explanation = Text(
            "While ensuring misclassification",
            font_size=28,
            color=RED
        )
        constraint_explanation.next_to(constraint, DOWN, buff=0.8)
        
        self.play(FadeIn(obj_explanation))
        self.wait(0.5)
        self.play(FadeIn(constraint_explanation))
        self.wait(1.5)
        
        # Store and clear
        self.problem_group = VGroup(
            problem, constraint, obj_explanation, constraint_explanation
        )
        self.play(FadeOut(self.problem_group))
        
    def visualize_decision_boundary(self):
        # Create axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": False, "stroke_width": 2},
        ).shift(DOWN * 0.3)
        
        # Don't show axes labels to reduce clutter
        self.play(Create(axes), run_time=1)
        
        # Decision boundary (curved line)
        boundary = axes.plot(
            lambda x: 0.3 * x**2 - 1.5,
            x_range=[-3, 3],
            color=YELLOW,
            stroke_width=5
        )
        
        boundary_label = Text("Decision Boundary", font_size=24, color=YELLOW)
        boundary_label.move_to(axes.c2p(0, 1.5))
        
        self.play(Create(boundary), Write(boundary_label))
        self.wait(1)
        
        # Class regions with actual images
        # IMAGE PLACEHOLDER: cat_icon.png (small icon)
        cat_img = ImageMobject("cat_icon.png")
        cat_img.scale(0.4)
        cat_img.move_to(axes.c2p(-2.5, -2))
        
        cat_region = Text("Cat Region", font_size=24, color=BLUE)
        cat_region.next_to(cat_img, DOWN, buff=0.1)
        
        # IMAGE PLACEHOLDER: dog_icon.png (small icon)
        dog_img = ImageMobject("dog_icon.png")
        dog_img.scale(0.4)
        dog_img.move_to(axes.c2p(2, 1.2))
        
        dog_region = Text("Dog Region", font_size=24, color=GREEN)
        dog_region.next_to(dog_img, DOWN, buff=0.1)
        
        self.play(FadeIn(cat_img), FadeIn(cat_region))
        self.play(FadeIn(dog_img), FadeIn(dog_region))
        self.wait(1)
        
        # Original point x0
        x0_point = Dot(axes.c2p(-1.5, -1.5), color=BLUE, radius=0.12)
        x0_label = MathTex(r"x_0", font_size=32, color=BLUE)
        x0_label.next_to(x0_point, LEFT, buff=0.2)
        
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
        # Show multiple possible perturbations
        large_pert_point = Dot(self.axes.c2p(1.5, 1), color=RED, radius=0.1)
        large_pert_arrow = Arrow(
            self.x0_point.get_center(),
            large_pert_point.get_center(),
            buff=0.1,
            color=RED,
            stroke_width=4
        )
        large_pert_label = Text("Large perturbation", font_size=22, color=RED)
        large_pert_label.next_to(large_pert_point, UP, buff=0.2)
        
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
        
        # Show optimal (minimum) perturbation
        optimal_point = Dot(self.axes.c2p(-0.2, -0.3), color=GREEN, radius=0.12)
        optimal_arrow = Arrow(
            self.x0_point.get_center(),
            optimal_point.get_center(),
            buff=0.1,
            color=GREEN,
            stroke_width=6
        )
        
        optimal_label = MathTex(r"x^*", font_size=32, color=GREEN)
        optimal_label.next_to(optimal_point, RIGHT, buff=0.2)
        
        min_pert_text = Text("Minimum perturbation", font_size=24, color=GREEN)
        min_pert_text.next_to(optimal_point, DOWN, buff=0.8)
        
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
        
        # Key insight
        insight1 = Text(
            "Minimum Norm Attack finds the",
            font_size=34
        )
        insight1.shift(UP * 1.5)
        
        insight2 = Text(
            "SMALLEST possible perturbation",
            font_size=38,
            color=BLUE,
            weight=BOLD
        )
        insight2.next_to(insight1, DOWN, buff=0.4)
        
        insight3 = Text(
            "that crosses the decision boundary",
            font_size=34
        )
        insight3.next_to(insight2, DOWN, buff=0.4)
        
        # Formula
        formula = MathTex(
            r"\|x^* - x_0\| = \text{minimum}",
            font_size=44,
            color=GREEN
        )
        formula.shift(DOWN * 1.5)
        
        self.play(Write(insight1))
        self.wait(0.3)
        self.play(Write(insight2))
        self.wait(0.3)
        self.play(Write(insight3))
        self.wait(0.8)
        self.play(Write(formula))
        self.wait(2)