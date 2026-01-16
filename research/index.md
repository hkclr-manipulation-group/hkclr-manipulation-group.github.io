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
  | first %}
{% assign ui = site.data.citations
  | where: "id", paper.id
  | first %}

{% if paper %}
{% comment %}
  ===== 本地优先逻辑（Highlight）=====
  1. 假定本地页面 URL
  2. 在 site.pages 中查是否存在
  3. 存在 → 本地
  4. 不存在 → 外链（IEEE / DOI）
{% endcomment %}

{% assign local_url = '/research/ybh19fov/' %}
{% assign has_local = site.pages | where: "url", local_url | size %}

{% if has_local > 0 %}
  {% assign highlight_link = local_url | relative_url %}
{% else %}
  {% assign highlight_link = paper.link %}
{% endif %}

<div class="research-item"
     style="display:flex; gap:1.2rem; align-items:flex-start; margin-bottom:1.5rem;">

  {% if ui and ui.image %}
    <a href="{{ highlight_link }}">
      <img
        src="{{ ui.image | relative_url }}"
        alt="{{ paper.title }}"
        style="width:200px; height:auto;"
      >
    </a>
  {% endif %}

  <div>
    <h4 style="margin-top:0.2rem; margin-bottom:0.3rem; font-size:1rem; line-height:1.3;">
      <a href="{{ highlight_link }}">
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

{% comment %}
  本地优先（不依赖 sources.yml 可改）
  用 paper_id 从 site.pages 反查
{% endcomment %}
{% assign local_page = site.pages | where: "paper_id", paper.id | first %}

{% if local_page %}
  {% assign link = local_page.url | relative_url %}
{% else %}
  {% assign link = paper.link %}
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
    <h4 style="margin-top:0.2rem; margin-bottom:0.3rem; font-size:1rem; line-height:1.3;">
      <a href="{{ link }}">
        {{ paper.title }}
      </a>
    </h4>

    <div>{{ paper.authors | join: ", " }}</div>
    <div>{{ paper.publisher }} · {{ paper.date | date: "%d %b %Y" }}</div>
  </div>

</div>

{% endfor %}
