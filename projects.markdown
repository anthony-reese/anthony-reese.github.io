---
layout: page
title: Projects
permalink: /projects/
---

<div class="project-cards">
  {% for project in site.projects %}
    <div class="project-card">
      <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
      <p>{{ project.description }}</p>
    </div>
  {% endfor %}
</div>

