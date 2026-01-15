---
title: Projects
nav:
  order: 2
  tooltip: Software, datasets, and more
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

Our projects span robotic manipulation, medical and continuum robotics, and
data-driven control. We develop open-source software, hardware prototypes,
and experimental platforms that translate theoretical advances into
real-world robotic systems.

{% include tags.html tags="publication, resource, website" %}

{% include search-info.html %}

{% include section.html %}

## Featured

Highlighted projects that represent our core research directions and recent
developments in robotic manipulation and medical robotics.

{% include list.html component="card" data="projects" filter="group == 'featured'" %}

{% include section.html %}

## More

Additional projects, tools, and experimental platforms developed by the group.

{% include list.html component="card" data="projects" filter="!group" style="small" %}
