---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %} Team

We are the Manipulation Group at HKCLR. Our research focuses on robotic system
development, including lightweight robotic arms and mobile dual-arm systems.
We also work on AI and control algorithm development, such as vision-language-action
models, vision-language models, and both model-based and model-free control methods.

{% include section.html %}

## Postdoctoral Researchers
{% include list.html data="members" component="portrait" filter="role == 'team-leader'" %}
{% include list.html data="members" component="portrait" filter="role == 'postdoc'" %}

{% include section.html %}

## Ph.D. Students
{% include list.html data="members" component="portrait" filter="name == 'Qiwei Meng'" %}
{% include list.html data="members" component="portrait" filter="name == 'Gang Wang'" %}
{% include list.html data="members" component="portrait" filter="name == 'Weiwei Zhang'" %}
{% include list.html data="members" component="portrait" filter="name == 'Taoran Jiang'" %}
{% include list.html data="members" component="portrait" filter="name == 'Youpeng Wen'" %}
{% include list.html data="members" component="portrait" filter="name == 'Ziqin Wei'" %}

{% include section.html %}

## Engineers
{% include list.html data="members" component="portrait" filter="role == 'engineer'" %}

{% include section.html %}

{% capture content %}

{% endcapture %}

{% include grid.html style="square" content=content %}
