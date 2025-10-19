from manim import *

class AdversarialMLIntro(Scene):
    def construct(self):
        # Title
        title = Text("Adversarial Machine Learning", font_size=48, weight=BOLD)
        subtitle = Text("When AI Gets Fooled", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Scene 1: Normal prediction
        self.scene_normal_prediction()
        self.wait(0.5)
        
        # Scene 2: Adding noise
        self.scene_adding_noise()
        self.wait(0.5)
        
        # Scene 3: Fooled prediction
        self.scene_fooled_prediction()
        self.wait(1)
        
        # Final message
        self.final_message()
        
    def scene_normal_prediction(self):
        # Image placeholder (left side)
        img_box = Square(side_length=3, color=BLUE)
        img_box.shift(LEFT * 3.5)
        img_label = Text("Panda Image", font_size=24)
        img_label.next_to(img_box, DOWN)
        
        # Arrow
        arrow = Arrow(LEFT * 1, RIGHT * 1, buff=0.2, color=WHITE)
        
        # Model box (center)
        model_box = Rectangle(width=2, height=1.5, color=GREEN)
        model_text = Text("ML Model", font_size=28)
        model_text.move_to(model_box.get_center())
        model = VGroup(model_box, model_text)
        
        # Prediction (right side)
        prediction = Text("Prediction: Panda\nConfidence: 99.7%", 
                         font_size=28, color=GREEN)
        prediction.shift(RIGHT * 3.5)
        
        # Animate
        self.play(FadeIn(img_box), Write(img_label))
        self.wait(0.3)
        self.play(GrowArrow(arrow))
        self.play(FadeIn(model))
        self.wait(0.3)
        self.play(Write(prediction))
        self.wait(1)
        
        # Store for next scene
        self.img_box = img_box
        self.img_label = img_label
        self.arrow = arrow
        self.model = model
        self.prediction = prediction
        
    def scene_adding_noise(self):
        # Clear prediction
        self.play(FadeOut(self.prediction))
        
        # Add noise visualization
        noise_text = Text("+ Adversarial\nNoise", font_size=24, color=RED)
        noise_text.next_to(self.img_box, UP)
        
        # Create noise effect (random dots)
        dots = VGroup(*[
            Dot(point=self.img_box.get_center() + 
                np.array([np.random.uniform(-1.3, 1.3), 
                         np.random.uniform(-1.3, 1.3), 0]),
                radius=0.03, color=RED)
            for _ in range(50)
        ])
        
        self.play(Write(noise_text))
        self.play(FadeIn(dots, lag_ratio=0.1), run_time=1.5)
        self.wait(0.5)
        
        # Flash effect on image
        self.play(
            self.img_box.animate.set_color(RED),
            run_time=0.3
        )
        self.play(
            self.img_box.animate.set_color(BLUE),
            run_time=0.3
        )
        
        # Update label
        new_label = Text("Panda + Noise\n(Looks same to humans)", 
                        font_size=20, color=YELLOW)
        new_label.next_to(self.img_box, DOWN)
        
        self.play(Transform(self.img_label, new_label))
        self.wait(0.5)
        
        self.play(FadeOut(noise_text), FadeOut(dots))
        
    def scene_fooled_prediction(self):
        # Wrong prediction
        wrong_prediction = Text("Prediction: Gibbon\nConfidence: 99.3%", 
                               font_size=28, color=RED)
        wrong_prediction.shift(RIGHT * 3.5)
        
        # Cross mark
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT, color=RED, stroke_width=8),
            Line(UP + RIGHT, DOWN + LEFT, color=RED, stroke_width=8)
        ).scale(0.5)
        cross.next_to(wrong_prediction, UP)
        
        self.play(Write(wrong_prediction))
        self.play(Create(cross))
        self.wait(1)
        
        # Add explanation
        explanation = Text("Model completely fooled!", 
                          font_size=32, color=YELLOW)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)
        
        # Clear everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
    def final_message(self):
        # Final text
        message1 = Text("Machines don't 'think' like humans", 
                       font_size=36, color=BLUE)
        message2 = Text("They can be fooled by invisible patterns", 
                       font_size=32, color=GRAY)
        message2.next_to(message1, DOWN, buff=0.5)
        
        message3 = Text("This is Adversarial Machine Learning", 
                       font_size=36, color=GREEN, weight=BOLD)
        message3.next_to(message2, DOWN, buff=1)
        
        self.play(Write(message1))
        self.wait(0.5)
        self.play(Write(message2))
        self.wait(0.5)
        self.play(Write(message3))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])