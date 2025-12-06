"""
Hadwiger-Nelson: Why 4 Colors Fail
Based on Aubrey de Grey's 2018 paper

The construction builds up:
H (7 vertices) → J (31) → K (61) → L (121) → M (1345) → G (1581)

Run: manim -pqh hadwiger_nelson_4_colors.py FourColorsFail
"""

from manim import *
import numpy as np

class FourColorsFail(Scene):
    def construct(self):
        
        # ===== TITLE =====
        title = Text("Why 4 Colors Fail", font_size=52, color=WHITE, weight=BOLD)
        subtitle = Text("de Grey's Construction (2018)", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1)
        self.play(FadeIn(subtitle), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)
        self.wait(0.5)
        
        # ===== STEP 1: GRAPH H =====
        step1_title = Text("Step 1: Graph H", font_size=36, color=YELLOW)
        step1_title.to_edge(UP, buff=0.5)
        self.play(FadeIn(step1_title), run_time=0.6)
        
        # Create H: hexagon + center (7 vertices, 12 edges)
        def create_H(center, scale=1.0, color=WHITE):
            """Create graph H: regular hexagon with center, side length 1"""
            vertices = []
            # Center vertex
            vertices.append(center)
            # 6 hexagon vertices
            for i in range(6):
                angle = i * np.pi / 3
                pos = center + scale * np.array([np.cos(angle), np.sin(angle), 0])
                vertices.append(pos)
            
            edges = []
            # Edges from center to each hex vertex
            for i in range(1, 7):
                edges.append((0, i))
            # Edges around hexagon
            for i in range(1, 7):
                next_i = (i % 6) + 1
                edges.append((i, next_i))
            
            return vertices, edges
        
        H_verts, H_edges = create_H(ORIGIN, scale=1.2)
        
        H_group = VGroup()
        # Draw edges
        for e in H_edges:
            line = Line(H_verts[e[0]], H_verts[e[1]], color=BLUE_C, stroke_width=2.5)
            H_group.add(line)
        # Draw vertices
        H_dots = []
        for v in H_verts:
            dot = Dot(v, radius=0.12, color=WHITE)
            H_group.add(dot)
            H_dots.append(dot)
        
        H_label = Text("H: Hexagon + center", font_size=24)
        H_label.next_to(H_group, DOWN, buff=0.5)
        H_stats = Text("7 vertices, 12 edges", font_size=22, color=GRAY)
        H_stats.next_to(H_label, DOWN, buff=0.2)
        
        self.play(Create(H_group), run_time=1.5)
        self.play(FadeIn(H_label), FadeIn(H_stats), run_time=0.6)
        self.wait(1.5)
        
        # Show the key property: 4-colorings
        self.play(FadeOut(H_label), FadeOut(H_stats), run_time=0.4)
        
        key_text = Text("4 ways to color H with 4 colors:", font_size=26)
        key_text.next_to(H_group, DOWN, buff=0.4)
        self.play(FadeIn(key_text), run_time=0.5)
        self.wait(0.8)
        
        # Show coloring with monochromatic triple
        colors_4 = [RED, BLUE, GREEN, YELLOW]
        
        # Coloring 1: center and two opposite vertices same color (monochromatic triple)
        coloring1 = [RED, RED, BLUE, RED, GREEN, BLUE, GREEN]  # 0,1,3 are red (triple)
        
        for i, dot in enumerate(H_dots):
            self.play(dot.animate.set_color(coloring1[i]), run_time=0.15)
        
        triple_text = Text("2 colorings have a 'monochromatic triple'", font_size=24, color=ORANGE)
        triple_text.next_to(key_text, DOWN, buff=0.3)
        self.play(FadeIn(triple_text), run_time=0.5)
        
        # Highlight the triple
        triple_highlight = VGroup(
            Circle(radius=0.2, color=YELLOW, stroke_width=3).move_to(H_verts[0]),
            Circle(radius=0.2, color=YELLOW, stroke_width=3).move_to(H_verts[1]),
            Circle(radius=0.2, color=YELLOW, stroke_width=3).move_to(H_verts[3]),
        )
        self.play(Create(triple_highlight), run_time=0.6)
        self.wait(1.2)
        
        self.play(FadeOut(triple_highlight), FadeOut(key_text), FadeOut(triple_text), run_time=0.5)
        
        # Reset colors
        for dot in H_dots:
            dot.set_color(WHITE)
        
        self.play(FadeOut(H_group), FadeOut(step1_title), run_time=0.6)
        self.wait(0.3)
        
        # ===== STEP 2: GRAPH J =====
        step2_title = Text("Step 2: Graph J", font_size=36, color=YELLOW)
        step2_title.to_edge(UP, buff=0.5)
        self.play(FadeIn(step2_title), run_time=0.6)
        
        # J contains 13 copies of H: 1 center, 6 at distance 1, 6 at distance √3
        J_text = Text("13 copies of H arranged together", font_size=26)
        J_text.next_to(step2_title, DOWN, buff=0.4)
        self.play(FadeIn(J_text), run_time=0.5)
        
        # Create simplified J visualization
        J_group = VGroup()
        
        # Central H (smaller for visualization)
        scale = 0.35
        center_H_verts, center_H_edges = create_H(ORIGIN, scale=scale)
        for e in center_H_edges:
            J_group.add(Line(center_H_verts[e[0]], center_H_verts[e[1]], 
                            color=BLUE_C, stroke_width=1.5))
        for v in center_H_verts:
            J_group.add(Dot(v, radius=0.06, color=WHITE))
        
        # 6 copies at distance 1 (scaled)
        for i in range(6):
            angle = i * np.pi / 3
            offset = np.array([np.cos(angle), np.sin(angle), 0]) * 0.8
            H_v, H_e = create_H(offset, scale=scale * 0.7)
            for e in H_e:
                J_group.add(Line(H_v[e[0]], H_v[e[1]], color=TEAL, stroke_width=1))
            for v in H_v:
                J_group.add(Dot(v, radius=0.04, color=TEAL))
        
        # 6 copies at distance √3 (scaled)
        for i in range(6):
            angle = i * np.pi / 3 + np.pi / 6
            offset = np.array([np.cos(angle), np.sin(angle), 0]) * 1.5
            H_v, H_e = create_H(offset, scale=scale * 0.6)
            for e in H_e:
                J_group.add(Line(H_v[e[0]], H_v[e[1]], color=GREEN_C, stroke_width=1))
            for v in H_v:
                J_group.add(Dot(v, radius=0.04, color=GREEN_C))
        
        J_stats = Text("31 vertices", font_size=22, color=GRAY)
        J_stats.to_edge(DOWN, buff=0.8)
        
        self.play(Create(J_group), run_time=2)
        self.play(FadeIn(J_stats), run_time=0.4)
        self.wait(1.5)
        
        self.play(FadeOut(J_group), FadeOut(J_text), FadeOut(J_stats), FadeOut(step2_title), run_time=0.6)
        self.wait(0.3)
        
        # ===== STEP 3: GRAPH K =====
        step3_title = Text("Step 3: Graph K", font_size=36, color=YELLOW)
        step3_title.to_edge(UP, buff=0.5)
        self.play(FadeIn(step3_title), run_time=0.6)
        
        K_text = Text("Two copies of J, one rotated by 2·arcsin(1/4)", font_size=26)
        K_text.next_to(step3_title, DOWN, buff=0.4)
        self.play(FadeIn(K_text), run_time=0.5)
        
        # Show two overlapping J's
        J1 = J_group.copy()
        J2 = J_group.copy()
        J2.rotate(2 * np.arcsin(0.25))
        J2.set_color(ORANGE)
        
        K_group = VGroup(J1, J2)
        K_group.scale(0.8)
        
        K_stats = Text("61 vertices, 26 copies of H", font_size=22, color=GRAY)
        K_stats.to_edge(DOWN, buff=0.8)
        
        self.play(FadeIn(J1), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(J2), run_time=0.8)
        self.play(FadeIn(K_stats), run_time=0.4)
        self.wait(1.5)
        
        self.play(FadeOut(K_group), FadeOut(K_text), FadeOut(K_stats), FadeOut(step3_title), run_time=0.6)
        self.wait(0.3)
        
        # ===== STEP 4: GRAPH L =====
        step4_title = Text("Step 4: Graph L", font_size=36, color=YELLOW)
        step4_title.to_edge(UP, buff=0.5)
        self.play(FadeIn(step4_title), run_time=0.6)
        
        L_text = Text("Two copies of K, rotated around vertex A", font_size=26)
        L_text.next_to(step4_title, DOWN, buff=0.4)
        self.play(FadeIn(L_text), run_time=0.5)
        
        # Show two K's
        K1 = K_group.copy().scale(0.6).shift(LEFT * 1.5)
        K2 = K_group.copy().scale(0.6).shift(RIGHT * 1.5)
        K2.rotate(2 * np.arcsin(0.125))
        K2.set_color(PURPLE)
        
        L_group = VGroup(K1, K2)
        
        L_stats = Text("121 vertices, 52 copies of H", font_size=22, color=GRAY)
        L_stats.to_edge(DOWN, buff=0.8)
        
        self.play(FadeIn(K1), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(K2), run_time=0.8)
        self.play(FadeIn(L_stats), run_time=0.4)
        
        self.wait(1)
        
        # KEY PROPERTY OF L
        key_L = Text("KEY: In any 4-coloring of L,", font_size=26, color=RED)
        key_L2 = Text("at least one H has a monochromatic triple!", font_size=26, color=RED)
        key_group = VGroup(key_L, key_L2).arrange(DOWN, buff=0.15)
        key_group.to_edge(DOWN, buff=0.3)
        
        self.play(FadeOut(L_stats), run_time=0.3)
        self.play(FadeIn(key_group), run_time=0.7)
        self.wait(2)
        
        self.play(FadeOut(L_group), FadeOut(L_text), FadeOut(key_group), FadeOut(step4_title), run_time=0.6)
        self.wait(0.3)
        
        # ===== STEP 5: GRAPH M =====
        step5_title = Text("Step 5: Graph M", font_size=36, color=YELLOW)
        step5_title.to_edge(UP, buff=0.5)
        self.play(FadeIn(step5_title), run_time=0.6)
        
        M_text = Text("Dense graph of Moser spindles around H", font_size=26)
        M_text.next_to(step5_title, DOWN, buff=0.4)
        self.play(FadeIn(M_text), run_time=0.5)
        
        # Create representation of M (dense spindle network)
        M_group = VGroup()
        np.random.seed(42)
        
        # Central H
        center_H_verts, center_H_edges = create_H(ORIGIN, scale=0.4)
        for e in center_H_edges:
            M_group.add(Line(center_H_verts[e[0]], center_H_verts[e[1]], 
                            color=YELLOW, stroke_width=2))
        for v in center_H_verts:
            M_group.add(Dot(v, radius=0.08, color=YELLOW))
        
        # Surrounding dense structure (simplified visualization)
        for _ in range(200):
            angle = np.random.uniform(0, 2 * np.pi)
            r = np.random.uniform(0.5, 2.0)
            pos = np.array([r * np.cos(angle), r * np.sin(angle), 0])
            M_group.add(Dot(pos, radius=0.025, color=RED_C))
        
        # Add some edges to show density
        for _ in range(150):
            angle1 = np.random.uniform(0, 2 * np.pi)
            r1 = np.random.uniform(0.5, 1.8)
            angle2 = angle1 + np.random.uniform(-0.3, 0.3)
            r2 = r1 + np.random.uniform(-0.3, 0.3)
            p1 = np.array([r1 * np.cos(angle1), r1 * np.sin(angle1), 0])
            p2 = np.array([r2 * np.cos(angle2), r2 * np.sin(angle2), 0])
            M_group.add(Line(p1, p2, color=RED_C, stroke_width=0.5, stroke_opacity=0.4))
        
        M_stats = Text("1345 vertices (many Moser spindles)", font_size=22, color=GRAY)
        M_stats.to_edge(DOWN, buff=0.8)
        
        self.play(FadeIn(M_group), run_time=1.5)
        self.play(FadeIn(M_stats), run_time=0.4)
        
        self.wait(1)
        
        # KEY PROPERTY OF M
        key_M = Text("KEY: NO 4-coloring of M has", font_size=26, color=GREEN)
        key_M2 = Text("a monochromatic triple in central H!", font_size=26, color=GREEN)
        key_M_group = VGroup(key_M, key_M2).arrange(DOWN, buff=0.15)
        key_M_group.to_edge(DOWN, buff=0.3)
        
        self.play(FadeOut(M_stats), run_time=0.3)
        self.play(FadeIn(key_M_group), run_time=0.7)
        self.wait(2)
        
        self.play(FadeOut(M_group), FadeOut(M_text), FadeOut(key_M_group), FadeOut(step5_title), run_time=0.6)
        self.wait(0.3)
        
        # ===== THE CONTRADICTION =====
        contra_title = Text("The Contradiction", font_size=40, color=RED, weight=BOLD)
        self.play(FadeIn(contra_title), run_time=0.8)
        self.wait(1)
        self.play(contra_title.animate.to_edge(UP, buff=0.5), run_time=0.6)
        
        # Show the logic
        logic1 = Text("• L forces at least one H to have a monochromatic triple", font_size=26)
        logic2 = Text("• M forbids its central H from having a monochromatic triple", font_size=26)
        logic3 = Text("• Place 52 copies of M so their central H's form L", font_size=26)
        
        logic_group = VGroup(logic1, logic2, logic3).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        logic_group.center()
        
        self.play(FadeIn(logic1), run_time=0.8)
        self.wait(1.2)
        self.play(FadeIn(logic2), run_time=0.8)
        self.wait(1.2)
        self.play(FadeIn(logic3), run_time=0.8)
        self.wait(1.5)
        
        # CONTRADICTION!
        result = Text("IMPOSSIBLE!", font_size=48, color=RED, weight=BOLD)
        result.next_to(logic_group, DOWN, buff=0.8)
        
        self.play(FadeIn(result, scale=1.3), run_time=0.7)
        self.wait(1.5)
        
        # Final conclusion
        self.play(
            FadeOut(logic_group),
            FadeOut(result),
            FadeOut(contra_title),
            run_time=0.8
        )
        
        conclusion = Text("Therefore: 4 colors are NOT enough!", font_size=36, color=WHITE)
        conclusion2 = Text("χ(plane) ≥ 5", font_size=52, color=GREEN, weight=BOLD)
        
        final_group = VGroup(conclusion, conclusion2).arrange(DOWN, buff=0.6)
        final_group.center()
        
        self.play(FadeIn(conclusion), run_time=0.8)
        self.wait(0.8)
        self.play(FadeIn(conclusion2, scale=1.2), run_time=0.8)
        
        self.wait(2.5)
        
        # Fade out
        self.play(FadeOut(final_group), run_time=1)
        self.wait(0.5)


if __name__ == "__main__":
    pass