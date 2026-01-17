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

{% assign paper = site.data.sources | where: "id", "doi:10.1109/TMRB.2019.2949881" | first %}
{% assign ui = site.data.citations | where: "id", paper.id | first %}

{% if paper %}
{% assign local_page = site.pages | where: "paper_id", paper.id | first %}
{% assign link = local_page.url | relative_url | default: paper.link %}

<div class="research-item"
     style="display:flex; gap:1.2rem; align-items:flex-start; margin-bottom:2rem;">

  {% if ui and ui.image %}
  <div style="width:200px; height:100px; display:flex; align-items:center; justify-content:center; background:#f6f8fa;">
    <img
      src="{{ ui.image | relative_url }}"
      alt="{{ paper.title }}"
      style="max-width:100%; max-height:100%; object-fit:contain;"
    >
  </div>
  {% endif %}

  <div>
    <h4 style="margin:0 0 0.4rem 0; font-size:1rem; line-height:1.35;">
      <a href="{{ link }}">{{ paper.title }}</a>
    </h4>
    <div>{{ paper.authors | join: ", " }}</div>
    <div>{{ paper.publisher }} · {{ paper.date | date: "%Y" }}</div>
  </div>

</div>
{% endif %}

{% include section.html %}

## All

{% include search-box.html %}
{% include search-info.html %}

<div style="margin-bottom:1.5rem;"></div>

{% assign sorted_papers = site.data.sources | where_exp: "p", "p.date" | sort: "date" | reverse %}
{% assign papers_by_year = sorted_papers | group_by_exp: "paper", "paper.date | date: '%Y'" %}

{% for year in papers_by_year %}
### {{ year.name }}

{% for paper in year.items %}
{% assign ui = site.data.citations | where: "id", paper.id | first %}
{% assign local_page = site.pages | where: "paper_id", paper.id | first %}
{% assign link = local_page.url | relative_url | default: paper.link %}

<div class="research-item"
     style="display:flex; gap:1.2rem; align-items:flex-start; margin-bottom:1.5rem;">

  {% if ui and ui.image %}
  <div style="width:200px; height:100px; display:flex; align-items:center; justify-content:center; background:#f6f8fa;">
    <img
      src="{{ ui.image | relative_url }}"
      alt="{{ paper.title }}"
      style="max-width:100%; max-height:100%; object-fit:contain;"
    >
  </div>
  {% endif %}

  <div>
    <h4 style="margin:0 0 0.4rem 0; font-size:1rem; line-height:1.35;">
      <a href="{{ link }}">{{ paper.title }}</a>
    </h4>
    <div>{{ paper.authors | join: ", " }}</div>
    <div>{{ paper.publisher }} · {{ paper.date | date: "%d %b %Y" }}</div>
  </div>

</div>

{% endfor %}
{% endfor %}
