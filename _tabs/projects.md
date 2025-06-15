---
layout: page
icon: fa-solid fa-satellite
title: Projects
permalink: /projects/
order: 2
---

<div class="project-list">
  {% for project in site.categories.projects %}
  <div class="project-card-horizontal">
    <div class="project-image">
      <img src="{{ project.preview_image | relative_url }}" alt="{{ project.title }} preview">
    </div>
    <div class="project-info">
      <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
      <p>{{ project.description }}</p>
    </div>
  </div>
  {% endfor %}
</div>

