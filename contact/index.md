---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %} Contact Us

We are the **Manipulation Group at the Hong Kong Centre for Logistics Robotics (HKCLR)**,  
CUHK T Stone Robotics Institute.

Our research focuses on vision-based robotic manipulation, embodied intelligence,
and learning-based control for real-world robotic systems.  
Feel free to reach out or visit our lab.

{%
  include button.html
  type="email"
  text="wchen@hkclr.hk"
  link="mailto:wchen@hkclr.hk"
%}
{%
  include button.html
  type="address"
  tooltip="Open our location on Google Maps"
  link="https://www.google.com/maps"
%}

{% include section.html %}

{% capture col1 %}
{%
  include figure.html
  image="images/photo.jpg"
  caption="Vision-based robotic manipulation"
%}
{% endcapture %}

{% capture col2 %}
{%
  include figure.html
  image="images/photo.jpg"
  caption="Embodied AI for interaction and control"
%}
{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html dark=true %}

{% capture col1 %}
**Vision-Based Manipulation**  
Visual servoing  
Deformable object manipulation  
Flexible and adaptive robot control
{% endcapture %}

{% capture col2 %}
**AI & Representation**  
Embodied AI  
Vision-Language Models (VLM)  
Vision-Language-Action (VLA)
{% endcapture %}

{% capture col3 %}
**Control & Learning**  
Model-based control  
Model-free control  
Learning-based manipulation
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}
