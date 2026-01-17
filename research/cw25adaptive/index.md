---
title: "Adaptive Vision-Based Control for Flexible Robot with Unknown Environmental Constraints"
layout: paper
paper_id: doi:10.1109/RCAR65431.2025.11139652
date: 2025-01-01
image: /photo.png

authors:
  - Wei Chen
  - Haiwen Wu
  - Bohan Yang
  - Jinfei Hu
  - Yun-Hui Liu

venue: IEEE International Conference on Real-time Computing and Robotics (RCAR)
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

<h2>Abstract</h2>
<p class="paper-abstract">
This paper presents an adaptive vision-based control framework for flexible robots
operating under unknown environmental constraints. The proposed method integrates
real-time visual sensing and adaptive control strategies to estimate environmental
geometry and robot deformation online. By leveraging vision-based pose and shape
estimation, the robot is able to achieve robust task execution without prior knowledge
of environmental constraints. Experimental results demonstrate the effectiveness and
robustness of the proposed approach in real-time robotic manipulation scenarios.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Adaptive vision-based control framework for flexible robots in unknown environments</li>
  <li>Online estimation of robot shape and environmental constraints using visual feedback</li>
  <li>Real-time experimental validation demonstrating robustness and adaptability</li>
</ul>

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

{% endif %}
