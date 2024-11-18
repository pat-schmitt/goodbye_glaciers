---
permalink: /regions/
title: Regions
---
# !!!Work in Progress!!!

# Region page


<div style="display: flex; align-items: flex-start; flex-wrap: wrap;">
  <!-- Text on the left side -->
  <div style="flex: 1; margin-right: 20px; min-width: 300px;">
    <p>Although many glaciers in the Alps are projected to vanish in the near future, even under +1.5°C global warming, for glaciers globally, every degree of warming matters. Select different regional projections to explore how much we can reduce glacier mass loss regionally by limiting global warming to +1.5°C:</p>
  </div>

  <!-- Image on the right side -->
  <div style="flex: 1; min-width: 300px;">
    <img src="/assets/images/global_map_rgi6_small.jpeg" alt="Global Map of RGI6" style="width: 100%; height: auto;" />
  </div>
</div>

<!-- Add responsive CSS -->
<style>
  @media (max-width: 768px) {
    div[style*="display: flex"] {
      flex-direction: column; /* Stack items vertically */
    }
    div[style*="margin-right: 20px"] {
      margin-right: 0; /* Remove the right margin for text */
    }
  }
</style>

<!-- Dropdown to select region -->
<select id="regionSelect">
  <option value="global">Global</option>
  <option value="RGI01">01: Alaska</option>
  <option value="RGI02">02: Western Canada and U.S.</option>
  <option value="RGI03">03: Arctic Canada North</option>
  <option value="RGI04">04: Arctic Canada South</option>
  <option value="RGI05">05: Greenland Periphery</option>
  <option value="RGI06">06: Iceland</option>
  <option value="RGI07">07: Svalbard</option>
  <option value="RGI08">08: Scandinavia</option>
  <option value="RGI09">09: Russian Arctic</option>
  <option value="RGI10">10: North Asia</option>
  <option value="RGI11">11: Central Europe</option>
  <option value="RGI12">12: Caucasus and Middle East</option>
  <option value="RGI13">13: Central Asia</option>
  <option value="RGI14">14: South Asia West</option>
  <option value="RGI15">15: South Asia East</option>
  <option value="RGI16">16: Low Latitudes</option>
  <option value="RGI17">17: Southern Andes</option>
  <option value="RGI18">18: New Zealand</option>
  <option value="RGI19">19: Subantarctic and Antarctic Islands</option>
  <option value="RGI13-14-15">13-14-15: High-Mountain Asia</option>
</select>

<!-- Image container -->
<img id="regionImage" src="/assets/images/global_complex_en_three_glac_models_v1.png" alt="Volume evolution of all glaciers in selected region for 1.5°C and 2.7°C." />

<script>
  document.getElementById("regionSelect").addEventListener("change", function() {
    var selectedRegion = this.value;
    var image = document.getElementById("regionImage");
    image.src = "/assets/images/" + selectedRegion + "_complex_en_three_glac_models_v1.png";
    image.alt = "Volume evolution of glaciers in " + selectedRegion + " for 1.5°C and 2.7°C.";
  });
</script>

By “glaciers”, we mean all glaciers outside of the two continental ice sheets (Greenland and Antarctica).

## Additional resources
Are you further interested in the future of glaciers? You can discover their future projected evolution from the following resources: 
- [OGGM-edu: global and regional glacier projections from PyGEM-OGGM for 1.5°C–4.0°C](https://edu.oggm.org/en/latest/global_future_glacier-app_rounce_delta_T_en.html)
- [OGGM-edu: Alpine and alpine country-wide glacier projections from PyGEM-OGGM for 1.5°C–4.0°C](https://edu.oggm.org/en/latest/alps_future-app_rounce_delta_T_en.html)
- [OGGM-edu: Learn about the world’s glaciers location, climate, and the ice they store](https://bokeh.oggm.org/explorer/app)
- PROVIDE climate risk dashboard where glacier projections from OGGM can be selected for every country with glaciers: [link to glacier projections for Austria under 1.5°C and 2020 climate policies scenarios](https://climate-risk-dashboard.climateanalytics.org/impacts/explore?indicator=glacier-volume&geography=AUT&scenarios[0]=curpol&time=annual&reference=present-day-2020&spatial=area)
- Most recent information on the *Cryosphere* (ice sheets, glaciers, snow, permafrost, sea ice and polar oceans) are summarised in the [*State of the Cryosphere Report 2024*](https://iccinet.org/statecryo24/). "The report describes how a combination of melting polar ice sheets, vanishing glaciers, and thawing permafrost will have rapid, irreversible, and disastrous impacts worldwide."

