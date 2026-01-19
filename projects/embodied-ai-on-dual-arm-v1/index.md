---
layout: default
title: "Embodied AI on Dual-Arm System V1"
permalink: /projects/embodied-ai-on-dual-arm-v1/
---

# Embodied AI on Dual-Arm System V1

**Embodied Intelligence** refers to intelligent systems that acquire capabilities
through physical embodiment, integrating **perception, action, and interaction
with the environment**.
By coupling robotic embodiment with modern **Vision–Language Models (VLMs)**,
robots can interpret high-level semantic instructions such as
*“organize the workspace”* or *“assist a human operator”*, and autonomously
decompose them into executable, multi-step manipulation behaviors.

This project presents a **Dual-Arm Embodied AI System (V1)** as a
**demonstration-oriented research platform**, showcasing how contemporary
embodied intelligence paradigms can be integrated with dual-arm robotic
manipulation systems.

---

## Core Capabilities

- **Long-horizon task planning**  
  High-level semantic commands are decomposed into structured, multi-step action
  sequences, enabling coherent task execution over extended temporal horizons.

- **Online adaptability**  
  The system continuously perceives environmental changes and dynamically
  adjusts strategies during execution, allowing robust operation in unstructured
  environments.

- **Semantic reasoning and embodied decision-making**  
  Through the integration of large-scale vision–language models and multimodal
  perception, the system performs semantic understanding, reasoning, and
  decision-making grounded in physical interaction.

---

## Dual Embodied Intelligence Pipelines

- Vision–Language Model (VLM) Pipeline

<center>
  <img src="assets/vlm_preview.gif" width="60%" />
</center>

The **VLM pipeline** focuses on long-horizon, semantically guided manipulation
tasks such as desktop organization.
High-level language instructions are decomposed into structured task plans,
which are executed through predefined manipulation primitives on the dual-arm
platform.

---

- Vision–Language–Action (VLA) Pipeline

<center>
  <img src="assets/vla_preview.gif" width="60%" />
</center>

The **VLA pipeline** targets dynamic and reactive object manipulation, such as
real-time object grasping and interaction.
By tightly coupling perception, language understanding, and action generation,
this pipeline enables responsive embodied behaviors in dynamic environments.

---

## Application Scenarios

- Dual-arm object manipulation and coordination  
- Semantically guided task execution  
- Human-centered service and assistance  
- Complex manipulation in unstructured environments
