---
title: "Tele-Operated Oropharyngeal Swab (TOOS) Robot Enabled by TSS Soft Hand for Safe and Effective Sampling"
layout: paper
permalink: /research/cw21toos/
paper_id: doi:10.1109/TMRB.2021.3123530
image: /images/research/cw21toos.png

authors:
  - Wei Chen
  - Jianshu Zhou
  - Shing Shin Cheng
  - Yiang Lu
  - Fangxun Zhong
  - Yuan Gao
  - Yaqing Wang
  - Lingbin Xue
  - Michael C. F. Tong
  - Yun-Hui Liu

venue: IEEE Transactions on Medical Robotics and Bionics
date: 2021-11-01
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
    Tele-operated oropharyngeal swab robot enabled by a TSS soft hand for safe COVID‑19 sampling.
  </figcaption>
</figure>
{% endif %}

<hr/>

<h2>Abstract</h2>
<p class="paper-abstract">
This paper presents a tele-operated oropharyngeal swab (TOOS) robot designed for safe
and effective COVID‑19 sampling. The system integrates a TSS soft robotic hand with
a teleoperation framework to enable compliant and precise swab manipulation in the
oropharyngeal region. By combining soft robotic grasping, force sensing, and real-time
teleoperation, the TOOS robot significantly reduces cross‑infection risk to healthcare
workers while maintaining reliable sampling performance.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Tele-operated robotic system for safe oropharyngeal swab sampling</li>
  <li>Integration of TSS soft hand for compliant and safe interaction</li>
  <li>Experimental validation in medical and clinical scenarios</li>
</ul>

<h2>Citation</h2>
<pre class="paper-bibtex">
@ARTICLE{9590555,
  author  = {Chen, Wei and Zhou, Jianshu and Cheng, Shing Shin and Lu, Yiang and
             Zhong, Fangxun and Gao, Yuan and Wang, Yaqing and Xue, Lingbin and
             Tong, Michael C. F. and Liu, Yun-Hui},
  title   = {Tele-Operated Oropharyngeal Swab (TOOS) Robot Enabled by TSS Soft Hand
             for Safe and Effective Sampling},
  journal = {IEEE Transactions on Medical Robotics and Bionics},
  volume  = {3},
  number  = {4},
  pages   = {1040--1053},
  year    = {2021},
  doi     = {10.1109/TMRB.2021.3123530}
}
</pre>

{% endif %}
