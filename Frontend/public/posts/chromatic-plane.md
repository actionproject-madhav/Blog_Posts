---
title: "Chromatic Number of a Plane: The Hadwiger-Nelson Problem"
date: "2025-12-06"
excerpt: "Exploring the fascinating Hadwiger-Nelson problem: What is the minimum number of colors needed to color every point in the plane such that no two points exactly 1 unit apart share the same color?"
tags: ["mathematics", "graph-theory", "combinatorics", "open-problem"]
---

# Chromatic Number of a Plane

> **The Hadwiger-Nelson Problem**: What is the minimum number of colors needed to color every point in the plane such that no two points exactly 1 unit apart share the same color?

---

Imagine you're on a plane and you take two points that have a unit at random. You consider those points as vertices and the connection as an edge. You're free to make any vertices and edges between them as long as two points have a unit distance. If you consider this giant network as a graph, what's the minimum number of colours you need for colouring the nodes (points) so that no two adjacent colours are the same? This is the same as asking what the chromatic number of a 2d plane.

This problem was first proposed by Edward Nelson in 1950, but the earlier results related to this were presented in 1945 by Hugo Hadwiger. Let's see a few examples.

---

## 1.) Colouring with 1 is trivially impossible

Let's say point x has color red, then any edge from this point going to another point a unit distance should have a different color.

---

## 2.) 2 colours

A simple equilateral triangle shows that 2 colours are impossible.

> **Why it fails**: In an equilateral triangle with unit sides, all three vertices are mutually at distance 1 from each other. If vertex A is red, then B must be blue (since A-B = 1 unit). But C is also at distance 1 from both A and B, so C can't be red AND can't be blue. Contradiction!

<video controls width="100%">
  <source src="/videos/codes/hadwiger/media/videos/two-color/480p15/TwoColorsFail.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## 3.) 3 colours

Colouring with just 3 colours, while it works for very basic shapes like a triangle, doesn't work for shapes like the **Moser Spindle** as shown.

> **The Moser Spindle (1961)**: This is a 7-vertex, 11-edge unit-distance graph discovered by brothers William and Leo Moser. It consists of two rhombi (with 60° and 120° angles) sharing a vertex. The key insight is that the two "far" vertices of the rhombi are exactly 1 unit apart. When you try to 3-color this graph, you're forced to give both far vertices the same color—but they're connected! This proves χ ≥ 4.

<video controls width="100%">
  <source src="/videos/codes/hadwiger/media/videos/three-color/480p15/ThreeColorsFail.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## 4.) 7 colours

So how many colours do you need? Let's start with a large number of colours. That will make the problem easier (although our goal is to find the smallest number). Let's take 7 colors in total. A straightforward solution is to tile the coordinate plane with hexagons of different colours. An edge between two points at a unit distance can be considered as a traversal from one hexagon to the other. We need to ensure that no two hexagons of the same color are a unit distance away (that would mean we can connect the two same colour). The following animation explains the procedure:

> **How the 7-coloring works (Isbell, 1950)**:
> - Tile the plane with regular hexagons of diameter slightly less than 1
> - Assign 7 colors in a repeating pattern
> - Since each hexagon has diameter < 1, any two points inside the same hexagon are less than 1 unit apart (so being the same color is fine)
> - Same-colored hexagons are always separated by at least 2 "layers" of other hexagons, ensuring they're more than 1 unit apart
> 
> This proves χ ≤ 7.

<video controls width="100%">
  <source src="/videos/codes/hadwiger/media/videos/seven-color/2160p60/SevenColorsWork.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## 5.) 4 colours

It seems like 4 colors might be a good candidate since 3 is impossible and 7 is too large, despite having a solution. Any simple structure can be colored with 4 colors without too much difficulty. However, finding a proof that 4 colours work for any structure in 2d plane stumped mathematicians for over 60 years. 

Then came **Aubrey de Grey**, a chemist doing math for fun. He showed that 4 colours are unable to colour a special graph with 1581 vertices (de Grey, 2018). The clever construction of this graph is shown as:

> **How de Grey's Construction Works**:
> 
> The proof builds up through several layers:
> 
> 1. **Graph H** (7 vertices): A regular hexagon with its center. This can be 4-colored in exactly 4 distinct ways—2 of which contain a "monochromatic triple" (3 vertices of the same color), and 2 which don't.
> 
> 2. **Graph J** (31 vertices): 13 copies of H arranged together.
> 
> 3. **Graph K** (61 vertices): Two copies of J, with one rotated by 2·arcsin(1/4).
> 
> 4. **Graph L** (121 vertices): Two copies of K, with one rotated by 2·arcsin(1/8). **Key property**: In ANY 4-coloring of L, at least one copy of H must contain a monochromatic triple.
> 
> 5. **Graph M** (1345 vertices): A dense network of Moser spindles surrounding a central copy of H. **Key property**: There is NO 4-coloring of M where the central H has a monochromatic triple.
> 
> **The Contradiction**: Place 52 copies of M so that their central H's align with the 52 copies of H in L. Now L demands that at least one H has a monochromatic triple, but M forbids it. This is impossible—therefore, no 4-coloring exists!
> 
> The final simplified graph G has **1581 vertices**.

<video controls width="100%">
  <source src="/videos/codes/hadwiger/media/videos/four-color/2160p60/FourColorsFail.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Current Status

Hence, so far we know that 7 colors is enough to color the plane, and anything less than 4 isn't enough. **The answer lies somewhere between 5, 6, and 7.** 

| Lower Bound | Upper Bound |
|-------------|-------------|
| χ ≥ 5 (de Grey, 2018) | χ ≤ 7 (Isbell, 1950) |

A [Polymath project](https://dustingmixon.wordpress.com/2018/04/14/polymath16-first-thread-simplifying-de-greys-graph/) has been entirely dedicated to this purpose. Since de Grey's breakthrough, the smallest known 5-chromatic unit-distance graph has been reduced to just **509 vertices** (Parts, 2020).

Hopefully, mathematicians will find the upper bound in the near future, or we might need a new chemist like Grey to come up with a new structure disproving 5 and 6 colors. 

**What do you think? Please comment below.**

---

## References

- de Grey, A.D.N.J. (2018). "The Chromatic Number of the Plane Is at Least 5." *Geombinatorics* 28(1), 18-31. [arXiv:1804.02385](https://arxiv.org/abs/1804.02385)
- Soifer, A. (2008). *The Mathematical Coloring Book*. Springer.
- Moser, L. and Moser, M. (1961). "Solution to Problem 10." *Canadian Mathematical Bulletin* 4, 187-189.