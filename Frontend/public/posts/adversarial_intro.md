---
title: "Machines Don't 'Think': Introduction to Adversarial Machine Learning"
date: "2025-01-11"
excerpt: "Exploring how machines differ from human thinking and the fascinating world of adversarial attacks on machine learning models."
tags: ["machine-learning", "adversarial-attacks", "ai-safety"]
---

# Machines Don't "Think": Introduction to Adversarial Machine Learning


![Adversarial Example: Panda vs Gibbon](/posts/panda.jpeg)
It's super cool to see machines behave like humans. Whether it's a detector perfectly detecting an image of a cat or a self-driving car detecting everything going on lanes, it's fascinating to see how capable Machine Learning models are. The machine is learning, right? 

<video controls width="100%">
  <source src="/videos/media/videos/Adversarial.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

However, that's far from the truth. Machines differ fundamentally in the way human brains process things. They're not technically "learning" things based on intuition. In fact, most of the popular machine learning models are like "parrots", memorising weights. Even the slightest change in the input or carefully crafted prompts can make them act stupid. There's an interesting field of research ongoing in this area for more than a decade, commonly known in the literature as **Adversarial Machine Learning**. The study of attacks on machine learning algorithms has exposed vulnerabilities in their real-world usage, creating debates and dilemmas in AI safety.


While the attacks on Machine Learning models have been there for a long time, this field caught special attention when Goodfellow et al. (2014) demonstrated this phenomenon. How a simple change in the input image of a Panda, that's indistinguishable to the human eye, can fool a machine learning model to deliver incorrect predictions.

Let's say we have a model that detects an image of animals. As shown below, it correctly identifies the image as a Panda. An attacker adds a small distortion to the image. To a human eye, the image on the right is clearly a Panda and looks the same as the image on the left. However, the model thinks the image on the right is a Gibbon with a very high confidence. This is a classic example of fooling the deep neural network. But what's so special about these distortions that look like nothing to human eyes, but make the models go terribly wrong? Read on to explore the wonderful math behind adversarial attacks.


