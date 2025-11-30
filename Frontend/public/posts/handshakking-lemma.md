# The Handshaking Lemma

## The Party Problem

Imagine you walk into a party. There are many people and many handshakes. You might see people's outfits, someone's jewellery, their family, their presence and start making assumptions about their origin, wealth and so on, so on. Some assumptions are probably right, some aren't. 

Let's be less judgmental. Let's make some mathematical assumptions. With math, sometimes you can be 100% sure of your assumptions.

You go around asking people how many people they have met (handshakes they have done). **You will always find an even number of people who shook hands with an odd number of people.** 

Ok, bet let's prove this.

## The Mathematical Setup

Let's phrase this problem mathematically. Imagine people are nodes, and edges represent handshakes. The degree of a vertex is the total number of incoming and outgoing edges. 

If you have **n** total edges, the sum of degrees of the vertices will be **2n**. Think of counting each edge twice (two ends of edges) while counting the degrees. Hence, they add up twice, making the sum of degrees 2n. Notice that 2n is always an even number for any natural number n.

## The Proof

**Total sum of degrees = 2n**

**Degree of odd degree vertices + degree of even degree vertices = 2n**

**Degree of odd degree vertices = 2n - degree of even degree vertices**

Since RHS is even, LHS has to be even. But when is the sum of odd-degree vertices numbers like 1 + 3… an even number? 

**The sum of odd numbers is even only when there are an even number of them.** 

For instance, the sum of 1 + 3 = 4, an even number, because we added 2 (even) numbers, but the sum of 1 + 3 + 5 = 9 (odd sum) because we added 3 (odd) numbers. 

This proves the handshaking lemma.

---

## Manim Animation

This repository contains a Manim animation visualizing the Handshaking Lemma proof.

<video controls width="100%">
  <source src="/videos/media/videos/handshaking/HandshakingLemma (1).mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Features

- ✅ Clear graph with 5 vertices and 7 edges
- ✅ Color-coded vertices (no overlapping labels)
- ✅ Step-by-step proof visualization
- ✅ Highlights odd vs even degree vertices
- ✅ Mathematical equations shown clearly
- ✅ Voiceover script included

### Requirements

```bash
pip install manim
pip install elevenlabs  # For voiceover generation
```

### Run the Animation

```bash
manim -pql handshaking_lemma_proof.py HandshakingLemma
```

For high quality:
```bash
manim -pqh handshaking_lemma_proof.py HandshakingLemma
```

### Generate Voiceover

1. Get your ElevenLabs API key from [https://elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys)
2. Edit `generate_voiceover.py` and add your API key
3. Run:
```bash
python generate_voiceover.py
```

### Files

- `handshaking_lemma_proof.py` - Main Manim animation
- `voiceover_script_short.txt` - Short voiceover script (<1000 chars)
- `generate_voiceover.py` - ElevenLabs voiceover generator
- `README.md` - This file

### The Animation Steps

1. **Step 1**: Sum of all degrees = 2 × (number of edges)
2. **Step 2**: Separate odd and even degree vertices
3. **Step 3**: Show equation: Odd sum = 2n - Even sum
4. **Step 4**: Key insight: Both sides must be even!
5. **Step 5**: Conclusion: Even count of odd-degree vertices

### Example Graph

```
Vertices: A(2), B(3), C(3), D(2), E(4)
Edges: 7
Sum of degrees: 14 = 2 × 7 ✓
Odd-degree vertices: 2 (B and C) ✓
```

---

## Key Takeaway

**In any graph, there's always an even number of vertices with odd degree.**

Back to our party: no matter how many people attend or how many handshakes happen, the number of people who shook hands an odd number of times will always be even.

Mathematics gives us certainty in an uncertain world.