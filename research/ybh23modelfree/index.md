---
title: "Model-Free 3-D Shape Control of Deformable Objects Using Novel Features Based on Modal Analysis"
layout: paper
permalink: /research/tro23-modelfree-shape/
paper_id: doi:10.1109/TRO.2023.3269347
image: /photo.png

authors:
  - Bohan Yang
  - Bo Lu
  - Wei Chen
  - Fangxun Zhong
  - Yun-Hui Liu

venue: IEEE Transactions on Robotics
date: 2023-08-01
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
    Model-free 3-D shape control of deformable objects using modal-analysis-based features.
  </figcaption>
</figure>
{% endif %}

<hr/>

<h2>Abstract</h2>
<p class="paper-abstract">
This paper presents a model-free framework for three-dimensional shape control of
deformable objects using novel features derived from modal analysis.
By exploiting intrinsic deformation modes, the proposed approach enables effective
visual servoing without requiring explicit physical models of the deformable object.
Experimental results on deformable object manipulation tasks demonstrate accurate
shape regulation, robustness to modeling uncertainties, and improved control
performance compared to conventional model-based methods.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Model-free 3-D shape control framework for deformable objects</li>
  <li>Novel modal-analysis-based features for visual servoing</li>
  <li>Extensive experimental validation on deformable object manipulation</li>
</ul>

<h2>Citation</h2>
<pre class="paper-bibtex">
@ARTICLE{10122176,
  author  = {Yang, Bohan and Lu, Bo and Chen, Wei and
             Zhong, Fangxun and Liu, Yun-Hui},
  title   = {Model-Free 3-D Shape Control of Deformable Objects Using Novel Features Based on Modal Analysis},
  journal = {IEEE Transactions on Robotics},
  volume  = {39},
  number  = {4},
  pages   = {3134--3153},
  year    = {2023},
  doi     = {10.1109/TRO.2023.3269347}
}
</pre>

{% endif %}
