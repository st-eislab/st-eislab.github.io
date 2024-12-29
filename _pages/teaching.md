---
title: "Teaching"
layout: gridlay
sitemap: false
permalink: /teaching/
---

## Teaching

Dr. Obregon usually teaches two undergraduate courses in the [Information Techonology Management (ITM) major](https://itm.seoultech.ac.kr/), and one graduate course in the department of [Data Science](https://data.seoultech.ac.kr/) at SeoulTech.

Please sign up for this courses on the [University eclass website](https://eclass.seoultech.ac.kr/ilos/main/main_form.acl). If you have any specific questions about course topics, feel free to message me and I will try respond as soon as possible.

{% assign itmSpringCourses = site.data.courses | where_exp: "course", "course.major=='ITM' and  course.semester=='Spring'" %}
{% assign dsSpringCourses = site.data.courses | where_exp: "course", "course.major=='Data Science' and  course.semester=='Spring'"  %}
{% assign itmFallCourses = site.data.courses | where_exp: "course", "course.major=='ITM' and  course.semester=='Fall'"  %}
{% assign dsFallCourses = site.data.courses | where_exp: "course", "course.major=='Data Science' and  course.semester=='Fall'"  %}

### Spring Semester

#### ITM courses
{% for course in itmSpringCourses %}

<div class="well">
<div class="col-md-12 col-sm-12">
* {{course.name}}
    - {{course.description}}
</div>
</div>
{% endfor %}


#### Data Science courses

{% for course in dsSpringCourses %}

<div class="well">
<div class="col-md-12 col-sm-12">
* {{course.name}}
    - {{course.description}}
</div>
</div>
{% endfor %}

### Fall Semester

#### ITM courses

{% for course in itmFallCourses %}

<div class="well">
<div class="col-md-12 col-sm-12">
* {{course.name}}
    - {{course.description}}
</div>
</div>
{% endfor %}

#### Data Science courses

{% for course in dsFallCourses %}

<div class="well">
<div class="col-md-12 col-sm-12">
* {{course.name}}
    - {{course.description}}
</div>
</div>
{% endfor %}