---
title: Adaptive FOV Control of Laparoscopes
doi: 10.1109/TMRB.2019.2949881
authors:
  - Bohan Yang
  - Wei Chen
  - Yun-Hui Liu
image: images/research/ybh19fov.png
---

{% assign paper = site.data.sources | where: "id", "doi:10.1109/TMRB.2019.2949881" | first %}
{% assign ui = site.data.citations | where: "id", paper.id | first %}

{% if paper %}
<div class="paper-header"
     style="display:flex; gap:1.5rem; align-items:flex-start; margin-bottom:2rem;">

  {% if ui and ui.image %}
    <img
      src="{{ ui.image | relative_url }}"
      alt="{{ paper.title }}"
      style="width:260px; height:auto;"
    >
  {% endif %}

  <div>
    <h1 style="margin-top:0; text-transform:none;">
      {{ paper.title }}
    </h1>

    <div>
      {{ paper.authors | join: ", " }}
    </div>

    <div>
      {{ paper.publisher }} ·
      {{ paper.date | date: "%d %b %Y" }} ·
      <a href="{{ paper.link }}">{{ paper.id }}</a>
    </div>
  </div>

</div>
{% endif %}

## Abstract

This paper presents an adaptive field-of-view control method for robotic
laparoscopic systems using programmable composed constraints.

## Highlights

- Vision-based control  
- Medical robotics  
- Programmable constraints
