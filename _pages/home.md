---
title: "EIS Lab - Home"
layout: homelay
sitemap: false
permalink: /
---

### Welcome to EIS Lab

<div markdown="0" id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel"  data-bs-interval="4000" data-bs-pause="hover">
   



    {% assign number = 0 %}
    <div class="carousel-inner" markdown="0">

    {% for slide in site.data.carousel %}

    {% if number == 0 %}

   <div class="carousel-item active">
    {% else %}
    <div class="carousel-item">

    {% endif %}        
            <img class="d-block w-100" src="{{ site.url }}{{ site.baseurl }}/{{ slide.src }}" alt="{{ slide.alt }}"  />
        </div>

    {% assign number =  1 %}
<!--         <div class="carousel-item">
            <img class="d-block w-100" src="{{ site.url }}{{ site.baseurl }}/images/slider20250927/soh_batteries.png" alt="SOH batteries" />
        </div>
        <div class="carousel-item">
            <img class="d-block w-100" src="{{ site.url }}{{ site.baseurl }}/images/slider20250927/XAI%20methods.png" alt="XAI methods" />
        </div> -->
    {% endfor %}

    </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>

<br>
<blockquote class="blockquote">
<p>"We develop explainable AI methods for trustworthy applications in smart manufacturing and smart energy industries."</p>
</blockquote>

### Lab Goals 

- Advance explainable AI for tree ensembles and deep learning.  
- Apply XAI to create trustworthy, practicable AI in smart factories.  
- Develop advanced AI methods for sustainable energy forecasting.  

### About Us 

_The Explainable Intelligent Systems (EIS) Lab at SeoulTech develops novel XAI methods and applies them to real-world challenges in smart manufacturing and sustainable energy. Our work bridges fundamental algorithm design and practical industry applications, aiming to create trustworthy, transparent, and impactful AI solutions._


