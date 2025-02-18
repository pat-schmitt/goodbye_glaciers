---
title: ''
layout: default
header:
  overlay_image: /assets/images/others/landing_page_hef_picture.png
---
{% case site.lang %}
    {% when "de" %}
        {% assign tagline = "Ein Projekt mit Wegweiser, das auf den Verlust von Gletschern aufmerksam macht" %}
    {% when "it" %}
        {% assign tagline = "Un progetto di cartelli escursionistici per sensibilizzare sulla perdita dei ghiacciai" %}
    {% when "fr" %}
        {% assign tagline = "Un projet de panneaux de signalisation pour sensibiliser à la disparition des glaciers" %}
    {% else %}
        {% assign tagline = "A hiking signpost project to raise glacier loss awareness" %}
{% endcase %}

{% capture overlay_img_path %}{{ page.header.overlay_image | relative_url }}{% endcapture %}

{% if page.header.overlay_filter contains "gradient" %}
  {% capture overlay_filter %}{{ page.header.overlay_filter }}{% endcapture %}
{% elsif page.header.overlay_filter contains "rgba" %}
  {% capture overlay_filter %}{{ page.header.overlay_filter }}{% endcapture %}
  {% capture overlay_filter %}linear-gradient({{ overlay_filter }}, {{ overlay_filter }}){% endcapture %}
{% elsif page.header.overlay_filter %}
  {% capture overlay_filter %}rgba(0, 0, 0, {{ page.header.overlay_filter }}){% endcapture %}
  {% capture overlay_filter %}linear-gradient({{ overlay_filter }}, {{ overlay_filter }}){% endcapture %}
{% endif %}

{% if page.header.image_description %}
  {% assign image_description = page.header.image_description %}
{% else %}
  {% assign image_description = page.title %}
{% endif %}

{% assign image_description = image_description | markdownify | strip_html | strip_newlines | escape_once %}

<div class="page__hero{% if page.header.overlay_color or page.header.overlay_image %}--overlay{% endif %}"
  style="{% if page.header.overlay_color %}background-color: {{ page.header.overlay_color | default: 'transparent' }};{% endif %} {% if overlay_img_path %}background-image: {% if overlay_filter %}{{ overlay_filter }}, {% endif %}url('{{ overlay_img_path }}');{% endif %}"
>
  {% if page.header.overlay_color or page.header.overlay_image %}
    <div class="wrapper">
      <h1 id="page-title" class="page__title" itemprop="headline">
        {% if paginator and site.paginate_show_page_num %}
          {{ site.title }}{% unless paginator.page == 1 %} {{ site.data.ui-text[site.locale].page | default: "Page" }} {{ paginator.page }}{% endunless %}
        {% else %}
          {{ page.title | default: site.title | markdownify | remove: "<p>" | remove: "</p>" | remove: "(!!!IN PROGRESS!!!)"}}
        {% endif %}
      </h1>
      {% if tagline %}
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
            <div style="text-align: left;">
                <p class="page__lead">{{ tagline | markdownify | remove: "<p>" | remove: "</p>" }}</p>
            </div>
            <a href="https://www.un-glaciers.org/en" style="display: flex; justify-content: center; align-items: center;">
                <img src="/assets/images/logos/logo_iygp_en.svg" alt="Logo International Year of Glaciers' Preservation" style="height: auto; width: 300px; background-color: white;">
            </a>
        </div>
      {% elsif page.header.show_overlay_excerpt != false and page.excerpt %}
        <p class="page__lead">{{ page.excerpt | markdownify | remove: "<p>" | remove: "</p>" }}</p>
      {% endif %}
      {% include page__meta.html %}
      {% if page.header.actions %}
        <p>
        {% for action in page.header.actions %}
          <a href="{{ action.url | relative_url }}" class="btn btn--light-outline btn--large">{{ action.label | default: site.data.ui-text[site.locale].more_label | default: "Learn More" }}</a>
        {% endfor %}
        </p>
      {% endif %}
    </div>
  {% else %}
    <img src="{{ page.header.image | relative_url }}" alt="{{ image_description }}" class="page__hero-image">
  {% endif %}
  {% if page.header.caption %}
    <span class="page__hero-caption">{{ page.header.caption | markdownify | remove: "<p>" | remove: "</p>" }}</span>
  {% endif %}
</div>

<div id="main" role="main">
  <article class="splash" itemscope itemtype="https://schema.org/CreativeWork"{% if page.locale %} lang="{{ page.locale }}"{% endif %}>
    {% if page.title %}<meta itemprop="headline" content="{{ page.title | markdownify | strip_html | strip_newlines | escape_once }}">{% endif %}
    {% if page.excerpt %}<meta itemprop="description" content="{{ page.excerpt | markdownify | strip_html | strip_newlines | escape_once }}">{% endif %}
    {% if page.date %}<meta itemprop="datePublished" content="{{ page.date | date_to_xmlschema }}">{% endif %}
    {% if page.last_modified_at %}<meta itemprop="dateModified" content="{{ page.last_modified_at | date_to_xmlschema }}">{% endif %}

    <section class="page__content" itemprop="text">
      <br>
      {% translate_file index.md %}
    </section>
  </article>
</div>
