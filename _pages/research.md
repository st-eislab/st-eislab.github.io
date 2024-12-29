---
title: "Research"
layout: gridlay
sitemap: false
permalink: /research/
---

<style>
img{
  border-radius: 10px;
}
.col-md-3 {
  margin-top:10px;
  margin-bottom:10px;
  padding:0px;
  display:block;
  overflow:hidden;
  text-align:center;
  display: table-cell;
  background: white;
  border-radius: 20px;
  height: auto;
}
iframe {
  margin:0;
  padding:0;
  width: 175px;
  display: inline;
  vertical-align: middle;
}
</style>

## Research

{% for project in site.data.research %}
<div class="well">
<div class="col-md-12 col-sm-12">
<h4>{{ project.project_name }}</h4>

<p><strong>Goal:</strong> {{ project.goal }}</p>
<p><strong>Description:</strong> {{ project.description }}</p>
<p><strong>Skills Used:</strong> {{ project.skills_used | join: ', ' }}</p>

   
</div>
</div>
 {% endfor %}