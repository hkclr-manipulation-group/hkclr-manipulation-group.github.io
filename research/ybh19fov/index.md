---
title: "Adaptive FOV Control of Laparoscopes with Programmable Composed Constraints"
layout: paper
permalink: /research/ybh19fov/
paper_id: doi:10.1109/TMRB.2019.2949881

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

<!-- ================= Title & Meta ================= -->

<h1 class="paper-title">{{ paper.title }}</h1>

<div class="paper-authors">
  {{ paper.authors | join: ", " }}
</div>

<div class="paper-venue">
  <em>{{ paper.publisher }}</em>, {{ paper.date | date: "%Y" }}
</div>

<div class="paper-links">
  <a href="{{ paper.link }}" target="_blank">Paper (PDF)</a>
  · <a href="https://doi.org/{{ paper.id | remove: 'doi:' }}" target="_blank">DOI</a>
</div>

{% if paper.image %}
<figure class="paper-figure">
  <img src="{{ paper.image | relative_url }}" alt="{{ paper.title }}">
  <figcaption>
    Overview of adaptive field-of-view control for robotic laparoscopy.
  </figcaption>
</figure>
{% endif %}

<hr/>

<!-- ================= Abstract ================= -->

<h2>Abstract</h2>

<p class="paper-abstract">
This paper presents an adaptive field-of-view (FOV) control framework
for robotic laparoscopic systems based on programmable composed constraints.
The proposed approach integrates region-based image-based visual servoing (IBVS)
with remote center of motion (RCM) and intuitive virtual plane (IVP) constraints,
leading to improved visual stability, safety, and eye–hand coordination
in minimally invasive surgery.
</p>

<h2>Method Overview</h2>

<p>
The proposed controller decouples the image-based visual servoing task
and constraint enforcement using a null-space formulation, allowing
extension to laparoscopes with different optical axis configurations.
</p>

<!-- ================= Video ================= -->

<h2>Video Demonstration</h2>

<div class="paper-video">
  <iframe
    width="720"
    height="405"
    src="https://www.youtube.com/embed/VIDEO_ID_HERE"
    title="Adaptive FOV Control Demo"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
  </iframe>
</div>

<p class="paper-video-note">
Demonstration of automatic laparoscope manipulation with adaptive FOV control
under RCM–IVP constraints.
</p>

<!-- ================= Contributions ================= -->

<h2>Main Contributions</h2>

<ul class="paper-contributions">
  <li>Adaptive region-based IBVS for robotic laparoscope FOV control</li>
  <li>Programmable composed constraints integrating RCM and IVP</li>
  <li>Online estimation of depth-related parameters</li>
  <li>Extensive experimental validation and user studies</li>
</ul>

<!-- ================= Citation ================= -->

<h2>Citation</h2>

<pre class="paper-bibtex">
@article{yang2019adaptive,
  title     = {Adaptive FOV Control of Laparoscopes with Programmable Composed Constraints},
  author    = {Yang, Bohan and Chen, Wei and Wang, Zerui and Lu, Yiang and
               Mao, Jiayue and Wang, Hesheng and Liu, Yun-Hui},
  journal   = {IEEE Transactions on Medical Robotics and Bionics},
  volume    = {1},
  number    = {4},
  pages     = {206--217},
  year      = {2019},
  publisher = {IEEE}
}
</pre>

{% endif %}
