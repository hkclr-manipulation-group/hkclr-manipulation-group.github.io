---
title: "Intuitive Teleoperation Control for Flexible Robotic Endoscopes Under Unknown Environmental Interferences"
layout: paper
date: 2024-06-01
paper_id: doi:10.1109/ICCA62789.2024.10591885

authors:
  - Wei Chen
  - Yiang Lu
  - Bin Li
  - Jianshu Zhou
  - Hanwen Cao
  - Fei Chen
  - Yun-Hui Liu

venue: "2024 IEEE 18th International Conference on Control & Automation (ICCA)"
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

<div class="paper-section">
  <h2>Abstract</h2>
  <p class="paper-abstract">
    Teleoperation control plays a pivotal role in robot-assisted endoscopic surgery,
    particularly for flexible robotic endoscopes operating in unstructured and
    contact-rich environments.
    Unlike conventional rigid laparoscopic systems, flexible endoscopes suffer from
    severe eye–head coordination issues caused by large bending, motion coupling,
    and unknown environmental interferences.
    <br><br>
    This paper proposes an intuitive teleoperation control framework that enables
    field-of-view (FOV) manipulation consistent with surgeons’ intuition.
    A virtual workspace is constructed to map master inputs directly to FOV motion,
    eliminating the need for explicit hand–eye coordination.
    To enhance robustness against unknown disturbances, accurate shape and distal pose
    feedback obtained from embedded multi-core fiber Bragg grating (FBG) sensors is
    integrated into an iterative constraint compliant control (ICCC) algorithm.
    <br><br>
    The proposed framework is validated on a robotic flexible ureteroscopy system with
    large deflection (up to 270° bending).
    Experimental results demonstrate improved trajectory tracking accuracy, disturbance
    resistance, and operational intuitiveness compared with conventional configuration
    space control methods.
  </p>
</div>

<div class="paper-section">
  <h2>Method Overview</h2>
  <ul class="paper-contributions">
    <li>
      An intuitive teleoperation control framework for flexible robotic endoscopes that
      directly maps master motion to field-of-view (FOV) control using a virtual workspace.
    </li>
    <li>
      An iterative constraint compliant control (ICCC) algorithm that leverages FBG-based
      shape and pose sensing to robustly handle unknown environmental interferences.
    </li>
    <li>
      Robust shape sensing and disturbance-resistant control validated on a robotic
      flexible ureteroscopy system with large bending angles and strong environmental
      interactions.
    </li>
  </ul>
</div>

<h3>Results</h3>

<div class="paper-grid">
  <figure>
    <img src="{{ '/research/icca24_endoscope/images/tracking_1.png' | relative_url }}">
    <figcaption>Trajectory tracking with intuitive teleoperation.</figcaption>
  </figure>

  <figure>
    <img src="{{ '/research/icca24_endoscope/images/disturbance.png' | relative_url }}">
    <figcaption>Disturbance resistance using ICCC.</figcaption>
  </figure>
</div>

<div class="paper-section">
  <h2>Citation</h2>
  <pre class="paper-bibtex">
@INPROCEEDINGS{10591885,
  author    = {Chen, Wei and Lu, Yiang and Li, Bin and Zhou, Jianshu and Cao, Hanwen and Chen, Fei and Liu, Yun-Hui},
  title     = {Intuitive Teleoperation Control for Flexible Robotic Endoscopes Under Unknown Environmental Interferences},
  booktitle = {2024 IEEE 18th International Conference on Control & Automation (ICCA)},
  pages     = {24--29},
  year      = {2024},
  doi       = {10.1109/ICCA62789.2024.10591885}
}
  </pre>
</div>

{% endif %}
