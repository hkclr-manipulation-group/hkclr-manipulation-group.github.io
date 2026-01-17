---
title: "Configurability Selection of Robotic Arm with Constrained Task and Environment in Laparoscopic Hysterectomy for Uterus Manipulation"
layout: paper
paper_id: doi:10.1109/RCAR54675.2022.9872266
date: 2022-01-01
image: /photo.png

authors:
  - Wei Chen
  - Jiahao Wu
  - Jianshu Zhou
  - Hesheng Wang
  - Yudong Wang
  - Tak Hong Cheung
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
This paper investigates the configurability selection problem of robotic arms for uterus
manipulation in laparoscopic hysterectomy under constrained task and environmental
conditions. A unified modeling framework is proposed to systematically evaluate the
feasibility of different robotic configurations by jointly considering task requirements,
anatomical constraints, and robot kinematics. Based on the proposed framework,
heuristic selection strategies are developed to identify suitable robotic arm
configurations that improve operational feasibility and safety in real-time surgical
scenarios. The effectiveness of the proposed method is validated through representative
laparoscopic hysterectomy cases.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Formulation of a configurability selection problem for robotic uterus manipulation in constrained surgical environments</li>
  <li>Unified modeling framework integrating task requirements, anatomical constraints, and robot kinematics</li>
  <li>Heuristic-based configuration selection strategies validated in laparoscopic hysterectomy scenarios</li>
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
