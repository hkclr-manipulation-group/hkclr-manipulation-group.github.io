---
title: Research
nav:
  order: 1
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %} Research

Our research focuses on vision-based robotic manipulation, embodied AI, and
learning-based control for real-world robotic systems.
We aim to develop robotic systems that can perceive, reason, and interactmarkdown="0"
robustly with complex and unstructured environments.

{% include section.html %}

## Highlighted

{% assign paper = site.data.sources | where: "id", "doi:10.1109/TMRB.2019.2949881" | first %}

{% if paper %}
{% assign local_page = site.pages | where: "paper_id", paper.id | first %}
{% assign link = local_page.url | relative_url | default: paper.link %}

<div markdown="0" style="
  display:flex !important;
  gap:1.2rem;
  align-items:flex-start;
  margin-bottom:2rem;
  background:#f6f8fa;
  padding:1rem 1.2rem;
  border-radius:8px;
  text-align:left !important;
  width:100%;
">

  <!-- left image column -->
  <div style="width:180px; flex:0 0 180px;">
    {% if paper.image %}
    <div style="
      width:180px;
      height:100px;
      background:#ffffff;
      border-radius:6px;
      display:flex;
      align-items:center;
      justify-content:center;
    ">
      <img
        src="{{ paper.image | relative_url }}"
        alt="{{ paper.title }}"
        style="max-width:100%; max-height:100%; object-fit:contain;"
      >
    </div>
    {% endif %}
  </div>

  <!-- right text column -->
  <div>
    <h4 style="margin:0 0 0.4rem 0; font-size:1rem; line-height:1.35;">
      <a href="{{ link }}" style="color:#1a73e8; text-decoration:none;">
        {{ paper.title }}
      </a>
    </h4>
    <div>{{ paper.authors | join: ", " }}</div>
    <div style="color:#666;">
      {{ paper.publisher }} · {{ paper.date | date: "%Y" }}
    </div>
  </div>

</div>
{% endif %}

{% include section.html %}

## All

{% include search-box.html %}
{% include search-info.html %}

{% assign years = "2025,2024,2023,2022,2021,2019" | split: "," %}

{% for y in years %}
### {{ y }}

{% for paper in site.data.sources %}
{% if paper.date %}
{% assign py = paper.date | date: "%Y" %}
{% if py == y %}

{% assign local_page = site.pages | where: "paper_id", paper.id | first %}
{% assign link = local_page.url | relative_url | default: paper.link %}

<div markdown="0" style="
  background:#f6f8fa;
  padding:1rem 1.2rem;
  margin-bottom:1rem;
  border-radius:8px;
  display:flex !important;
  align-items:flex-start;
  text-align:left !important;
  width:100%;
">

  <!-- left fixed image slot (always occupies space) -->
  <div style="width:120px; flex:0 0 120px; margin-right:1rem;">
    {% if paper.image %}
    <div style="
      width:120px;
      height:90px;
      background:#ffffff;
      border-radius:6px;
      display:flex;
      align-items:center;
      justify-content:center;
    ">
      <img
        src="{{ paper.image | default: '/images/research/photo.jpg' | relative_url }}"
        alt="{{ paper.title }}"
        style="max-width:100%; max-height:100%; object-fit:contain;"
      >
    </div>
    {% endif %}
  </div>

  <!-- right text column (perfect alignment) -->
  <div>
    <div style="font-size:1rem; font-weight:500; margin-bottom:0.3rem;">
      <a href="{{ link }}" style="color:#1a73e8; text-decoration:none;">
        {{ paper.title }}
      </a>
    </div>

    <div style="font-size:0.9rem; color:#333;">
      {{ paper.authors | join: ", " }}
    </div>

    <div style="font-size:0.85rem; color:#666; margin-top:0.1rem;">
      {{ paper.publisher }} · {{ py }}
    </div>
  </div>

</div>

{% endif %}
{% endif %}
{% endfor %}

{% endfor %}
