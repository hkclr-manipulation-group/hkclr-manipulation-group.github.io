---
title: "Adaptive FOV Control of Laparoscopes with Programmable Composed Constraints"
layout: paper
permalink: /research/ybh19fov/
paper_id: doi:10.1109/TMRB.2019.2949881
image: /images/research/ybh19fov.png

authors:
  - Bohan Yang
  - Wei Chen
  - Zerui Wang
  - Yiang Lu
  - Jiayue Mao
  - Hesheng Wang
  - Yun-Hui Liu

venue: IEEE Transactions on Medical Robotics and Bionics
date: 2019-11-01
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
    Overview of adaptive field-of-view control in robotic laparoscopy.
  </figcaption>
</figure>
{% endif %}

<hr/>

<h2>Abstract</h2>
<p class="paper-abstract">
This paper presents an adaptive field-of-view (FOV) control framework
for robotic laparoscopic systems based on programmable composed constraints.
The proposed approach enables intelligent camera motion by integrating
vision-based feedback with task-level constraints, improving both
operational safety and visual efficiency in minimally invasive surgery.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Adaptive FOV control strategy for robotic laparoscopes</li>
  <li>Vision-based programmable composed constraints</li>
  <li>Experimental validation on medical robotic platforms</li>
</ul>


<h2>Citation</h2>
<pre class="paper-bibtex">
@article{yang2019adaptive,
  title   = {Adaptive FOV Control of Laparoscopes with Programmable Composed Constraints},
  author  = {Yang, Bohan and Chen, Wei and Wang, Zerui and Lu, Yiang and
             Mao, Jiayue and Wang, Hesheng and Liu, Yun-Hui},
  journal = {IEEE Transactions on Medical Robotics and Bionics},
  volume  = {1},
  number  = {4},
  pages   = {206--217},
  year    = {2019},
  publisher = {IEEE}
}
</pre>


{% endif %}
