---
title: Research
nav:
  order: 1
  tooltip: Published works
---

# Research

Our research focuses on vision-based robotic manipulation, embodied AI, and
learning-based control for real-world robotic systems.
We aim to develop robotic systems that can perceive, reason, and interact
robustly with complex and unstructured environments.

{% include section.html %}

<style>
/* ===== Research Card Layout ===== */

.research-card {
  background: #f6f8fa;
  padding: 1rem 1.2rem;
  margin-bottom: 1rem;
  border-radius: 8px;

  display: flex;
  align-items: flex-start;
  gap: 1rem;

  width: 100%;
  text-align: left;
}

.research-thumb {
  width: 150px;
  flex: 0 0 120px;
}

.research-thumb-box {
  width: 130px;
  height: 100px;
  background: #ffffff;
  border-radius: 6px;

  display: flex;
  align-items: center;
  justify-content: center;
}

.research-thumb-box img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.research-meta {
  flex: 1;
}

.research-title {
  font-size: 1.05rem;
  font-weight: 500;
  margin-bottom: 0.3rem;
}

.research-authors {
  font-size: 0.9rem;
  color: #333;
}

.research-venue {
  font-size: 0.85rem;
  color: #666;
  margin-top: 0.1rem;
}

/* ===== Mobile: stack vertically ===== */
@media (max-width: 768px) {
  .research-card {
    flex-direction: column;
  }

  .research-thumb,
  .research-thumb-box {
    width: 100%;
  }

  .research-thumb-box {
    height: auto;
    padding: 0.5rem 0;
  }
}
</style>

## Highlighted

{% assign paper = site.data.sources | where: "id", "doi:10.1109/TMRB.2019.2949881" | first %}
{% if paper %}
{% assign local_page = site.pages | where: "paper_id", paper.id | first %}
{% assign link = local_page.url | relative_url | default: paper.link %}

<div class="research-card">

  <div class="research-thumb">
    <div class="research-thumb-box">
      <img src="{{ paper.image | relative_url }}" alt="{{ paper.title }}">
    </div>
  </div>

  <div class="research-meta">
    <div class="research-title">
      <a href="{{ link }}" style="color:#1a73e8; text-decoration:none;">
        {{ paper.title }}
      </a>
    </div>

    <div class="research-authors">
      {{ paper.authors | join: ", " }}
    </div>

    <div class="research-venue">
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

<div class="research-card">

  <div class="research-thumb">
    <div class="research-thumb-box">
      <img src="{{ paper.image | relative_url }}" alt="{{ paper.title }}">
    </div>
  </div>

  <div class="research-meta">
    <div class="research-title">
      <a href="{{ link }}" style="color:#1a73e8; text-decoration:none;">
        {{ paper.title }}
      </a>
    </div>

    <div class="research-authors">
      {{ paper.authors | join: ", " }}
    </div>

    <div class="research-venue">
      {{ paper.publisher }} · {{ py }}
    </div>
  </div>

</div>

{% endif %}
{% endif %}
{% endfor %}
{% endfor %}
