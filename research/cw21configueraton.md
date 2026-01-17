---
title: "Configurability Selection of Robotic Arm with Constrained Task and Environment in Laparoscopic Hysterectomy for Uterus Manipulation"
layout: paper
permalink: /research/rcar22-configurability/
paper_id: doi:10.1109/RCAR54675.2022.9872266
# image omitted → script / sources.yaml will fall back to photo.jpg

authors:
  - Wei Chen
  - Jiahao Wu
  - Jianshu Zhou
  - Hesheng Wang
  - Yudong Wang
  - Tak Hong Cheung
  - Yun-Hui Liu

venue: IEEE International Conference on Real-time Computing and Robotics (RCAR)
date: 2022-01-01
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
  <figcaption>
    Configurability analysis of robotic arm setups for constrained laparoscopic uterus manipulation.
  </figcaption>
</figure>
{% endif %}

<hr/>

<h2>Abstract</h2>
<p class="paper-abstract">
This paper investigates the configurability selection of robotic arms for uterus manipulation
in laparoscopic hysterectomy under constrained task and environmental conditions.
A unified modeling framework is proposed to evaluate feasible robotic configurations by
considering task requirements, anatomical constraints, and robot kinematics.
Heuristic-based selection strategies are employed to identify suitable robotic arm configurations
that improve feasibility and safety in real-time surgical scenarios.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Unified modeling framework for configurability analysis in constrained surgical tasks</li>
  <li>Heuristic-based selection of robotic arm configurations</li>
  <li>Validation in laparoscopic hysterectomy scenarios</li>
</ul>

<h2>Citation</h2>
<pre class="paper-bibtex">
@INPROCEEDINGS{9872266,
  author    = {Chen, Wei and Wu, Jiahao and Zhou, Jianshu and
               Wang, Hesheng and Wang, Yudong and
               Cheung, Tak Hong and Liu, Yun-Hui},
  title     = {Configurability Selection of Robotic Arm with Constrained Task and Environment
               in Laparoscopic Hysterectomy for Uterus Manipulation},
  booktitle = {2022 IEEE International Conference on Real-time Computing and Robotics (RCAR)},
  pages     = {419--424},
  year      = {2022},
  doi       = {10.1109/RCAR54675.2022.9872266}
}
</pre>

{% endif %}
