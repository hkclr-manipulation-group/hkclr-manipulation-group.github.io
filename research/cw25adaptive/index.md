---
title: "Adaptive Vision-Based Control for Flexible Robot with Unknown Environmental Constraints"
layout: paper
paper_id: doi:10.1109/RCAR65431.2025.11139652
date: 2025-01-01
image: /photo.png
---

{% assign paper = site.data.sources | where: "id", page.paper_id | first %}

{% if paper %}

<h1 class="paper-title">{{ paper.title }}</h1>

<div class="paper-authors">
  {{ paper.authors | join: ", " }}
</div>

<div class="paper-venue">
  <em>{{ paper.publisher }}</em>, {{ paper.date | date: "%Y" }}
</div>

<div class="paper-links">
  <a href="{{ paper.link }}" target="_blank">Paper</a>
  · <a href="https://doi.org/{{ paper.id | remove: 'doi:' }}" target="_blank">DOI</a>
</div>

{% if paper.image %}
<figure class="paper-figure">
  <img src="{{ paper.image | relative_url }}" alt="{{ paper.title }}">
</figure>
{% endif %}

<hr/>

<div class="paper-section">
  <h2>Abstract</h2>
  <p class="paper-abstract">
    This paper presents an adaptive vision-based control framework for flexible robots
    operating under unknown environmental constraints. The proposed method integrates
    real-time visual sensing and adaptive control strategies to estimate environmental
    geometry and robot deformation online. By leveraging vision-based pose and shape
    estimation, the robot achieves robust task execution without prior knowledge of
    environmental constraints.
  </p>
</div>

<div class="paper-section">
  <h2>Method Overview</h2>
  <p>
    We propose a vision-based adaptive control framework that tightly couples real-time
    visual perception with online deformation and constraint estimation. The controller
    adapts robot motion in response to estimated environmental geometry without requiring
    prior models.
  </p>
</div>

<div class="paper-section">
  <h2>Results</h2>

  <div class="paper-grid">
    <img src="{{ '/research/cw25adaptive/images/simulation_1.png' | relative_url }}"
         alt="Three DoFs flexible robot simulation">

    <img src="{{ '/research/cw25adaptive/images/simulation_2.png' | relative_url }}"
         alt="Two DoFs flexible robot simulation">
  </div>

  <p style="margin-top: 1rem; font-size: 0.95rem; color: #555; line-height: 1.5;">
    Simulation results of flexible robot control.
    The first row shows the three-DoFs flexible robot, and the second row shows the
    two-DoFs flexible robot.
    For each case, we compare the image trajectory and image error obtained by the
    proposed method and the classical model-based approach, demonstrating improved
    tracking accuracy and robustness under unknown environmental constraints.
  </p>
</div>

<div class="paper-section">
  <h2>Citation</h2>
  <pre class="paper-bibtex">
@INPROCEEDINGS{11139652,
  author    = {Chen, Wei and Wu, Haiwen and Yang, Bohan and Hu, Jinfei and Liu, Yun-Hui},
  title     = {Adaptive Vision-Based Control for Flexible Robot with Unknown Environmental Constraints},
  booktitle = {2025 IEEE International Conference on Real-time Computing and Robotics (RCAR)},
  pages     = {745--750},
  year      = {2025},
  doi       = {10.1109/RCAR65431.2025.11139652}
}
  </pre>
</div>

{% endif %}
