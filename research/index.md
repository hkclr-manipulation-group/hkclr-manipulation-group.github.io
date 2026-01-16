---
title: Research
nav:
  order: 1
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %} Research

Our research focuses on vision-based robotic manipulation, embodied AI, and
learning-based control for real-world robotic systems.
We aim to develop robotic systems that can perceive, reason, and interact
robustly with complex and unstructured environments.

{% include section.html %}

## Highlighted

{% assign paper = site.data.sources
  | where: "id", "doi:10.1109/TMRB.2019.2949881"
  | first
%}
{% assign ui = site.data.citations
  | where: "id", paper.id
  | first
%}

{% if paper %}
<div class="research-item"
     style="display:flex; gap:1.2rem; align-items:flex-start; margin-bottom:1.5rem;">

  {% if ui and ui.image %}
    <a href="/research/ybh19fov/">
      <img
        src="{{ ui.image | relative_url }}"
        alt="{{ paper.title }}"
        style="width:200px; height:auto;"
      >
    </a>
  {% endif %}

  <div>
    <h4 style="
      margin-top:0.2rem;
      margin-bottom:0.3rem;
      font-size:1rem;
      line-height:1.3;
    ">
      <a href="/research/ybh19fov/">
        {{ paper.title }}
      </a>
    </h4>

    <div>{{ paper.authors | join: ", " }}</div>
    <div>{{ paper.publisher }} · {{ paper.date | date: "%d %b %Y" }}</div>
  </div>

</div>
{% endif %}

{% include section.html %}

## All

{% for paper in site.data.sources %}
{% assign ui = site.data.citations | where: "id", paper.id | first %}

{% assign link = paper.link %}
{% if ui and ui.page %}
  {% assign link = ui.page %}
{% endif %}

<div class="research-item"
     style="display:flex; gap:1.2rem; margin-bottom:1.5rem; align-items:flex-start;">

  {% if ui and ui.image %}
    <a href="{{ link }}">
      <img
        src="{{ ui.image | relative_url }}"
        alt="{{ paper.title }}"
        style="width:200px; height:auto;"
      >
    </a>
  {% endif %}

  <div>
    <h4 style="
      margin-top:0.2rem;
      margin-bottom:0.3rem;
      font-size:1rem;
      line-height:1.3;
    ">
      <a href="{{ link }}">
        {{ paper.title }}
      </a>
    </h4>

    <div>{{ paper.authors | join: ", " }}</div>
    <div>{{ paper.publisher }} · {{ paper.date | date: "%d %b %Y" }}</div>
  </div>

</div>

{% endfor %}
