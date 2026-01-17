---
title: "A Robotic Skin Using Low-density FBGs for Human-robot Interaction"
layout: paper
permalink: /research/robio24-skin/
paper_id: doi:10.1109/ROBIO64047.2024.10907681
#image: /images/research/robio24_skin.png
authors:
  - Xiyue Dong
  - Chin-Kiu Lam
  - Wei Chen
  - Bohan Yang
  - Yun-Hui Liu

venue: IEEE International Conference on Robotics and Biomimetics (ROBIO)
date: 2024-01-01
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
    Low-density FBG-based robotic skin for force and shape sensing in human–robot interaction.
  </figcaption>
</figure>
{% endif %}

<hr/>

<h2>Abstract</h2>
<p class="paper-abstract">
This paper presents a robotic skin system based on low-density fiber Bragg gratings (FBGs)
for human–robot interaction. By strategically deploying a sparse array of FBG sensors,
the proposed skin accurately perceives contact force and surface deformation while
significantly reducing sensor density and system complexity. Experimental results
demonstrate reliable force sensing and shape estimation, enabling safe and responsive
interaction in soft robotic and collaborative systems.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Low-density FBG-based robotic skin design</li>
  <li>Accurate force and shape sensing with reduced sensor complexity</li>
  <li>Experimental validation for human–robot interaction scenarios</li>
</ul>

<h2>Citation</h2>
<pre class="paper-bibtex">
@INPROCEEDINGS{10907681,
  author    = {Dong, Xiyue and Lam, Chin-Kiu and Chen, Wei and
               Yang, Bohan and Liu, Yun-Hui},
  title     = {A Robotic Skin Using Low-density FBGs for Human-robot Interaction},
  booktitle = {2024 IEEE International Conference on Robotics and Biomimetics (ROBIO)},
  pages     = {129--134},
  year      = {2024},
  doi       = {10.1109/ROBIO64047.2024.10907681}
}
</pre>

{% endif %}
