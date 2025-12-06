from manim import *

class AdditiveAttackDemo(Scene):
    def construct(self):
        # Title
        title = Text("Additive Perturbation Attack", font_size=42, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Setup: Original vector x0 with actual cat image
        self.show_original_vector()
        self.wait(1)
        
        # Add perturbation vector r
        self.add_perturbation_vector()
        self.wait(1)
        
        # Show the result x = x0 + r with dog image
        self.show_result()
        self.wait(2)
        
        # Clean up and show final equation
        self.show_final_summary()
        self.wait(2)
        
    def show_original_vector(self):
        # IMAGE PLACEHOLDER: cat.png
        # Download a cat image and save as "cat.png" in same folder
        cat_img = ImageMobject("cat.jpeg")
        cat_img.scale(0.6)
        cat_img.shift(LEFT * 4.5 + UP * 0.5)
        cat_border = SurroundingRectangle(cat_img, color=BLUE, buff=0.1)
        
        # Original vector label
        x0_label = Text("x₀", font_size=36, color=BLUE)
        x0_label.next_to(cat_img, UP, buff=0.2)
        
        # Vector representation
        x0_matrix = Text(
            "[0.8]\n[0.2]\n[0.1]\n[0.9]",
            font_size=32
        )
        x0_matrix.next_to(cat_img, DOWN, buff=0.3)
        
        # Cat label
        cat_text = Text("Cat", font_size=24, color=BLUE)
        cat_text.next_to(x0_matrix, DOWN, buff=0.2)
        
        self.play(FadeIn(cat_img), Create(cat_border))
        self.wait(0.3)
        self.play(Write(x0_label))
        self.play(Write(x0_matrix))
        self.play(FadeIn(cat_text))
        
        # Store for later
        self.cat_img = cat_img
        self.cat_border = cat_border
        self.x0_label = x0_label
        self.x0_matrix = x0_matrix
        self.cat_text = cat_text
        
    def add_perturbation_vector(self):
        # Plus sign
        plus_sign = Text("+", font_size=56)
        plus_sign.shift(LEFT * 2.2 + UP * 0.5)
        
        # IMAGE PLACEHOLDER: noise.jpeg
        # Download adversarial noise pattern and save as "noise.jpeg"
        noise_img = ImageMobject("noise.jpeg")
        noise_img.scale(0.6)
        noise_img.shift(LEFT * 0.5 + UP * 0.5)
        noise_border = SurroundingRectangle(noise_img, color=RED, buff=0.1)
        
        # Perturbation label
        r_label = Text("r", font_size=36, color=RED)
        r_label.next_to(noise_img, UP, buff=0.2)
        
        # Perturbation matrix
        r_matrix = Text(
            "[0.1]\n[-0.05]\n[0.3]\n[-0.2]",
            font_size=32,
            color=RED
        )
        r_matrix.next_to(noise_img, DOWN, buff=0.3)
        
        noise_text = Text("Noise", font_size=24, color=RED)
        noise_text.next_to(r_matrix, DOWN, buff=0.2)
        
        self.play(Write(plus_sign))
        self.wait(0.3)
        self.play(FadeIn(noise_img), Create(noise_border))
        self.play(Write(r_label))
        self.play(Write(r_matrix))
        self.play(FadeIn(noise_text))
        self.wait(1)
        
        # Store for later
        self.plus_sign = plus_sign
        self.noise_img = noise_img
        self.noise_border = noise_border
        self.r_label = r_label
        self.r_matrix = r_matrix
        self.noise_text = noise_text
        
    def show_result(self):
        # Equals sign
        equals_sign = Text("=", font_size=56)
        equals_sign.shift(RIGHT * 1.3 + UP * 0.5)
        
        self.play(Write(equals_sign))
        
        # IMAGE PLACEHOLDER: dog.png
        # Download a dog image and save as "dog.png" in same folder
        dog_img = ImageMobject("cat.jpeg")
        dog_img.scale(0.6)
        dog_img.shift(RIGHT * 3.8 + UP * 0.5)
        dog_border = SurroundingRectangle(dog_img, color=GREEN, buff=0.1)
        
        # Result label
        x_label = Text("x", font_size=36, color=GREEN)
        x_label.next_to(dog_img, UP, buff=0.2)
        
        # Result matrix
        x_matrix = Text(
            "[0.9]\n[0.15]\n[0.4]\n[0.7]",
            font_size=32,
            color=GREEN
        )
        x_matrix.next_to(dog_img, DOWN, buff=0.3)
        
        # Dog label (misclassified)
        dog_text = Text("Dog (!)", font_size=24, color=GREEN)
        dog_text.next_to(x_matrix, DOWN, buff=0.2)
        
        self.play(FadeIn(dog_img), Create(dog_border))
        self.play(Write(x_label))
        self.play(Write(x_matrix))
        self.play(FadeIn(dog_text))
        self.wait(1)
        
        # Highlight the misclassification
        misclass_box = SurroundingRectangle(dog_text, color=YELLOW, buff=0.15)
        self.play(Create(misclass_box))
        self.wait(1)
        
        # Store for cleanup
        self.equals_sign = equals_sign
        self.dog_img = dog_img
        self.dog_border = dog_border
        self.x_label = x_label
        self.x_matrix = x_matrix
        self.dog_text = dog_text
        self.misclass_box = misclass_box
        
    def show_final_summary(self):
        # Clear everything except title
        self.play(
            *[FadeOut(mob) for mob in [
                self.cat_img, self.cat_border, self.x0_label, 
                self.x0_matrix, self.cat_text,
                self.plus_sign, self.noise_img, self.noise_border,
                self.r_label, self.r_matrix, self.noise_text,
                self.equals_sign, self.dog_img, self.dog_border,
                self.x_label, self.x_matrix, self.dog_text, self.misclass_box
            ]]
        )
        self.wait(0.5)
        
        # Final equation
        final_eq = Text(
            "x = x₀ + r",
            font_size=56
        )
        final_eq.shift(UP * 1)
        
        # Explanation
        explanation1 = Text(
            "Small perturbation r is added to x₀",
            font_size=32
        )
        explanation1.shift(DOWN * 0.5)
        
        explanation2 = Text(
            "Humans see the same image",
            font_size=32,
            color=BLUE
        )
        explanation2.shift(DOWN * 1.5)
        
        explanation3 = Text(
            "Model sees completely different class",
            font_size=32,
            color=RED
        )
        explanation3.shift(DOWN * 2.5)
        
        self.play(Write(final_eq))
        self.wait(0.5)
        self.play(FadeIn(explanation1))
        self.wait(0.5)
        self.play(FadeIn(explanation2))
        self.wait(0.5)
        self.play(FadeIn(explanation3))
        self.wait(2)