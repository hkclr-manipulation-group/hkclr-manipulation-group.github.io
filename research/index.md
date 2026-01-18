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
/* ===== Bigger & Airier Research Cards (override) ===== */

.research-card{
  padding: 1.25rem 1.5rem;     /* 更大内边距 */
  margin-bottom: 1.25rem;      /* 卡片之间更松 */
  border-radius: 12px;         /* 更圆润 */
  gap: 1.25rem;                /* 图和文字间距更大 */
  align-items: flex-start;
}

.research-thumb{
  width: 160px;                /* 缩略图更大 */
  flex: 0 0 160px;
}

.research-thumb-box{
  width: 160px;
  height: 120px;               /* 更高一点更协调 */
  border-radius: 10px;
}

.research-title{
  font-size: 1.22rem;          /* 标题更大 */
  font-weight: 650;
  margin-bottom: 0.45rem;
  line-height: 1.35;
}

.research-authors{
  font-size: 1.02rem;          /* 作者更大 */
  line-height: 1.55;           /* 文字不“拖/挤” */
  color: #222;
}

.research-venue{
  font-size: 0.95rem;          /* venue 更大 */
  line-height: 1.45;
  margin-top: 0.25rem;
  color: #555;
}

/* 链接更清晰 + hover */
.research-title a{
  color: #1a73e8 !important;
  text-decoration: none !important;
}
.research-title a:hover{
  text-decoration: underline !important;
}

/* ===== Mobile: still comfy ===== */
@media (max-width: 768px){
  .research-card{
    padding: 1.1rem 1.2rem;
    gap: 0.9rem;
  }
  .research-thumb,
  .research-thumb-box{
    width: 100%;
  }
  .research-thumb-box{
    height: auto;
    padding: 0.75rem 0;
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
