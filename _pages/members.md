---
title: "Members"
layout: gridlay
sitemap: false
permalink: /members/
---

## Members
<!--- 
**We are looking for new team members** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**
-->
### Professor

{% for member in site.data.pi %}

<div class="well">
<div class="row">
<div class="col-sm-2">
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-9 col-xs-12">
<h4>{{ member.name }}</h4>
<ul>
  <li><i>{{ member.info }}<br></i></li>
  <li><i>Research Interests:</i>{{member.interests}} </li>
 </ul>

{% if member.website %}
<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x" style="color:CornflowerBlue"></i></a> {% endif %}

<ul style="overflow: hidden">
<li> {{ member.education[0] }} </li>
<li> {{ member.education[1] }} </li>
</ul>
</div>
</div>
</div>

{% endfor %}

### Master Students

<div class='well'>
{% assign number_printed = 0 %}
{% for member in site.data.master_students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}

<div class="row">
{% endif %}


<div class="col-sm-2">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<!-- <div class="col-sm-4 col-xs-12"> -->
<div class="col-sm-9 col-xs-12">
  <h4>{{ member.name }}</h4>
  <ul>
  <li><i>{{ member.info }}<br></i></li>
  <li><i>Research Interests:</i>{{member.interests}} </li>
 </ul>

{% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x" style="color:CornflowerBlue"></i></a> {% endif %} {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x" style="color:CornflowerBlue"></i></a> {% endif %}

</div>
<!-- </div> -->

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}

</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}

</div>
{% endif %}
</div>
<!--- 
## Alumni

<div class="well">
{% assign number_printed = 0 %}
{% for member in site.data.alumni %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}

<div class="row">
{% endif %}

<div class="col-sm-2">
<img src="{{ site.url }}{{ site.baseurl }}/images/{{ member.photo }}" width="100%" style="max-width:250px"/>
</div>
<div class="col-sm-4 col-xs-12">
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">
    
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}

</div>
{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}

</div>
{% endif %}
</div>

## Administrative Support

<a href="exampleemail@gmail.com">Example staff</a> is helping us (and other groups) with administration.
-->