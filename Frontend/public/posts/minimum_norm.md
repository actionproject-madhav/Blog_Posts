
---
title: "Minimum Norm Attack: Finding the Smallest Adversarial Perturbation"
date: "2025-01-20"
excerpt: "Exploring the minimum norm attack, an optimization approach that finds the smallest possible perturbation to cause misclassification while maintaining visual similarity to humans."
tags: ["machine-learning", "adversarial-attacks", "optimization", "mathematics"]
---

## Minimum Norm Attack

I mentioned above that the perturbed data point is very small and there is a slight difference between the original vector $x_0$ and the new vector $x$. How do we decide what's the perturbation? How do we ensure it's as small as possible while still misclassifying the initial cat? This can be formulated as an interesting optimization problem.


<video width="100%" controls>
  <source src="../videos/media/videos/min_norm/min_norm.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### The Optimization Problem

The minimum norm attack finds a perturbed data $x$ by solving the optimization:

$$\min_{x} \|x - x_0\|$$

subject to:

$$\max_{j \neq t} \{g_j(x)\} - g_t(x) \leq 0$$

where $\|\cdot\|$ can be any norm specified by the user (commonly $L_2$ or $L_\infty$ norm), and $g_j(x)$ represents the model's confidence score for class $j$.

### Breaking Down the Constraint

The constraint $\max_{j \neq t} \{g_j(x)\} - g_t(x) \leq 0$ ensures that:
- $g_t(x)$ (confidence for target class $C_t$) is greater than all other class confidences
- This forces the model to classify $x$ as the target class $C_t$


### Why This Matters

As shown in the definition, the goal of the minimum norm attack is to minimize the perturbation magnitude while ensuring the new data $x$ is classified as $C_t$. This is a classic attack as it ensures the initial image of cat and the image after noise look the same to human eyes since the noise is very small, while still causing the machine to misclassify.

**Key insight:** We're finding the **smallest possible change** that crosses the decision boundary of the classifier.


### Generalization Beyond Classification

Remember the above example given is for classification problem, but it generalizes well to different kinds of networks where the goal is to minimize the difference between feature vectors of old $x$ and new $x$ after the noise. Whether you're attacking:
- Image classifiers
- Object detectors
- Segmentation networks
- Even generative models

The core principle remains: **find the smallest perturbation that achieves your adversarial goal**.

---

*In the next section, we'll dive into specific attack algorithms like FGSM (Fast Gradient Sign Method) and see how these theoretical concepts translate into practical attacks.*