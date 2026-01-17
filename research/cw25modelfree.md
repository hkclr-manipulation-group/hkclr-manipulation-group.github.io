---
title: "Data-driven Visual Servoing of Flexible Continuum Robots in Constrained Environments"
layout: paper
permalink: /research/iros25-dvscr/
paper_id: doi:10.1109/IROS60139.2025.11246163
image: /images/research/cw25modelfree.png

authors:
  - Wei Chen
  - Haiwen Wu
  - Xiyue Dong
  - Bohan Yang
  - Yun-Hui Liu

venue: IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
date: 2025-09-25
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
    Data-driven visual servoing for flexible continuum robots operating in constrained environments.
  </figcaption>
</figure>
{% endif %}

<hr/>

<h2>Abstract</h2>
<p class="paper-abstract">
This paper presents a data-driven visual servoing framework for flexible
continuum robots operating in constrained environments.
By leveraging learning-based models to handle system uncertainty and
nonlinear deformation, the proposed approach achieves robust and accurate
visual servoing performance in real-time robotic manipulation tasks.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Data-driven visual servoing framework for continuum robots</li>
  <li>Robust control under uncertainty and environmental constraints</li>
  <li>Experimental validation on flexible robotic platforms</li>
</ul>

<h2>Citation</h2>
<pre class="paper-bibtex">
@INPROCEEDINGS{11246163,
  author    = {Chen, Wei and Wu, Haiwen and Dong, Xiyue and Yang, Bohan and Liu, Yun-Hui},
  booktitle = {2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  title     = {Data-driven Visual Servoing of Flexible Continuum Robots in Constrained Environments},
  year      = {2025},
  pages     = {20746--20751},
  doi       = {10.1109/IROS60139.2025.11246163}
}
</pre>

{% endif %}
