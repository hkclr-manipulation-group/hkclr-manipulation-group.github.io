---
title: "Adaptive FOV Control of Laparoscopes with Programmable Composed Constraints"
layout: paper
permalink: /research/ybh19fov/
paper_id: doi:10.1109/TMRB.2019.2949881
---

<style>
/* ===== Global ===== */
.paper-container {
  max-width: 900px;
  margin: auto;
  padding: 3rem 1.5rem;
  font-family: Inter, -apple-system, BlinkMacSystemFont,
               "Segoe UI", Roboto, "Helvetica Neue",
               Arial, sans-serif;
  font-size: 16px;
  line-height: 1.65;
  letter-spacing: 0.01em;
  color: #222;
}

/* ===== Title ===== */
.paper-title {
  font-size: 2.1rem;
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -0.01em;
  margin-bottom: 0.5rem;
}

/* ===== Meta ===== */
.paper-authors {
  font-size: 1.05rem;
}

.paper-venue {
  margin-top: 0.25rem;
  color: #666;
}

/* ===== Links ===== */
.paper-links {
  margin-top: 0.8rem;
}

.paper-links a {
  color: #0056d6;
  text-decoration: none;
  margin-right: 0.4rem;
}

.paper-links a:hover {
  text-decoration: underline;
}

/* ===== Figure ===== */
.paper-figure {
  margin: 2.5rem 0;
  text-align: center;
}

.paper-figure img {
  max-width: 100%;
  border-radius: 6px;
}

.paper-figure figcaption {
  margin-top: 0.5rem;
  font-size: 0.9rem;
  color: #666;
}

/* ===== Sections ===== */
.paper-container h2 {
  margin-top: 2.5rem;
  font-size: 1.4rem;
  font-weight: 600;
}

/* ===== Abstract ===== */
.paper-abstract {
  max-width: 120ch;
  text-align: justify;
}

/* ===== Contributions ===== */
.paper-contributions {
  padding-left: 1.2rem;
}

.paper-contributions li {
  margin-bottom: 0.4rem;
}

/* ===== BibTeX ===== */
.paper-bibtex {
  background: #f6f8fa;
  padding: 1rem;
  overflow-x: auto;
  border-radius: 6px;
  font-family: Consolas, "SF Mono", "JetBrains Mono", monospace;
  font-size: 0.9rem;
  line-height: 1.5;
}
</style>

{% assign paper = site.data.sources | where: "id", "doi:10.1109/TMRB.2019.2949881" | first %}
{% assign ui = site.data.citations | where: "id", paper.id | first %}

{% if paper %}
<div class="paper-container">

  <h1 class="paper-title">
    {{ paper.title }}
  </h1>

  <div class="paper-authors">
    {{ paper.authors | join: ", " }}
  </div>

  <div class="paper-venue">
    <em>{{ paper.publisher }}</em>,
    {{ paper.date | date: "%Y" }}
  </div>

  <div class="paper-links">
    <a href="{{ paper.link }}" target="_blank">Paper</a>
    {% if paper.doi %}
      · <a href="https://doi.org/{{ paper.doi }}" target="_blank">DOI</a>
    {% endif %}
    {% if ui.code %}
      · <a href="{{ ui.code }}" target="_blank">Code</a>
    {% endif %}
    {% if ui.video %}
      · <a href="{{ ui.video }}" target="_blank">Video</a>
    {% endif %}
  </div>

  {% if ui and ui.image %}
  <figure class="paper-figure">
    <img src="{{ ui.image | relative_url }}" alt="{{ paper.title }}">
    <figcaption>
      Overview of adaptive field-of-view control in robotic laparoscopy.
    </figcaption>
  </figure>
  {% endif %}

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

</div>
{% endif %}
