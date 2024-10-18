---
title: "Past Events"
---

<h1>Past Events</h1>

{% assign now = "now" | date: "%Y-%m-%d" %}

<ul>
  {% assign past_events = site.events | sort: 'start_date' %}
  {% for event in past_events %}
    {% assign event_end = event.end_date | date: "%s" %}
    {% if event_end < now %}
      <li>
        <h2><a href="{{ event.url }}">{{ event.title }}</a></h2>
        <p><strong>Date:</strong> {{ event.start_date | date: "%B %d, %Y" }} - {{ event.end_date | date: "%B %d, %Y" }}</p>
        <p><strong>Location:</strong> {{ event.location }}</p>
        <p>{{ event.description }}</p>
      </li>
    {% endif %}
  {% endfor %}
</ul>

{% assign past_events_count = upcoming_events | where_exp: "event", "event.end_date | date: '%s' < now" | size %}
{% if past_events_count == 0 %}
  <p>No past events.</p>
{% endif %}
