---
title: "Publications"
layout: gridlay
sitemap: false
permalink: /publications/
years: [year >=2012]
---

<!-- <style>
.jumbotron{
    padding:3%;
    padding-bottom:10px;
    padding-top:10px;
    margin-top:10px;
    margin-bottom:30px;
}
</style> -->

<!--- 
<div class="jumbotron">
### Preprints
{% bibliography --query @unpublished %}
</div>
-->

<div class="well">
### International Journal Articles
{% bibliography --query @article %}
</div>

<div class="well">
### Conference Proceedings
{% bibliography --query @inproceedings %}
</div>

<div class="well">
### Book Chapters
{% bibliography --query @book_section %}
</div>
