---
title: "Intuitive Teleoperation Control for Flexible Robotic Endoscopes Under Unknown Environmental Interferences"
layout: paper
paper_id: doi:10.1109/ICCA62789.2024.10591885
date: 2024-06-01

authors:
  - Wei Chen
  - Yiang Lu
  - Bin Li
  - Jianshu Zhou
  - Hanwen Cao
  - Fei Chen
  - Yun-Hui Liu

venue: 2024 IEEE 18th International Conference on Control & Automation (ICCA)
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
</figure>
{% endif %}

<hr/>

<h2>Abstract</h2>
<p class="paper-abstract">
This paper presents an intuitive teleoperation control framework for flexible robotic endoscopes
operating under unknown environmental interferences. The proposed approach aims to maintain stable
and accurate trajectory tracking during contact-rich interaction without requiring an explicit model
of the environment. By leveraging real-time shape/kinematic feedback within the teleoperation loop,
the system improves robustness against external disturbances and enhances operator usability in
constrained endoscopic scenarios.
</p>

<h2>Main Contributions</h2>
<ul class="paper-contributions">
  <li>Intuitive teleoperation control framework for flexible robotic endoscopes under unknown environmental interferences</li>
  <li>Robust trajectory tracking strategy that does not rely on explicit environment modeling</li>
  <li>Experimental validation demonstrating improved stability and tracking performance in interference-prone scenarios</li>
</ul>

<h2>Citation</h2>
<pre class="paper-bibtex">
@INPROCEEDINGS{10591885,
  author    = {Chen, Wei and Lu, Yiang and Li, Bin and Zhou, Jianshu and Cao, Hanwen and Chen, Fei and Liu, Yun-Hui},
  booktitle = {2024 IEEE 18th International Conference on Control & Automation (ICCA)},
  title     = {Intuitive Teleoperation Control for Flexible Robotic Endoscopes Under Unknown Environmental Interferences},
  year      = {2024},
  pages     = {24-29},
  doi       = {10.1109/ICCA62789.2024.10591885}
}
</pre>

{% endif %}
