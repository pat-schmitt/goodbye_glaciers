# EN: Global and regional glacier projections

<div>
  <p>
    Discover global and regional projections for the over 200,000 mountain
    glaciers (all glaciers excluding the Greenland and Antarctic ice sheets).
    Many glaciers in the Alps (Central Europe) are expected to disappear soon,
    even under 1.5°C global warming. However, for glaciers worldwide, every
    tenth of a degree of warming makes a difference.
  </p>
  <p>
    Explore the regional projections to see how limiting global warming to 1.5°C
    can help reduce glacier volume loss:
  </p>
 </div>

<!-- Dropdown to select region -->

<div>
<select id="regionSelect" style="font-size: 24px; padding: 10px; border: 2px solid #FF5733; border-radius: 5px; background-color: #f8d7da; width: auto; min-width: 200px;">
  <option value="RGI11" selected>Central Europe (11)</option>
  <option value="global">Global</option>
  <option value="RGI01">Alaska (01)</option>
  <option value="RGI02">Western Canada and U.S. (02)</option>
  <option value="RGI03">Arctic Canada North (03)</option>
  <option value="RGI04">Arctic Canada South (04)</option>
  <option value="RGI05">Greenland Periphery (05)</option>
  <option value="RGI06">Iceland (06)</option>
  <option value="RGI07">Svalbard (07)</option>
  <option value="RGI08">Scandinavia (08)</option>
  <option value="RGI09">Russian Arctic (09)</option>
  <option value="RGI10">North Asia (10)</option>
  <option value="RGI12">Caucasus and Middle East (12)</option>
  <option value="RGI13">Central Asia (13)</option>
  <option value="RGI14">South Asia West (14)</option>
  <option value="RGI15">South Asia East (15)</option>
  <option value="RGI13-14-15">High-Mountain Asia (13-14-15)</option>
  <option value="RGI16">Low Latitudes (16)</option>
  <option value="RGI17">Southern Andes (17)</option>
  <option value="RGI18">New Zealand (18)</option>
  <option value="RGI19">Subantarctic and Antarctic Islands (19)</option>
</select>

<!-- Image containers for both figures -->
<img id="worldmapImage" src="/assets/images/volume_evolution_regions/RGI11_worldmap_en.png" alt="Map of selected glaciers" />
<img id="complexImage" src="/assets/images/volume_evolution_regions/RGI11_complex_en.png" alt="Volume evolution of glaciers in Central Europe for 1.5°C and 2.7°C." />

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

<script>
  document.getElementById("regionSelect").addEventListener("change", function() {
    var selectedRegion = this.value;
    
    // Get both image elements
    var worldmapImage = document.getElementById("worldmapImage");
    var complexImage = document.getElementById("complexImage");
    
    // Update world map image source
    worldmapImage.src = "/assets/images/volume_evolution_regions/" + selectedRegion + "_worldmap_en.png";
    worldmapImage.alt = "Map of selected glaciers in " + selectedRegion;

    // Update complex model image source
    complexImage.src = "/assets/images/volume_evolution_regions/" + selectedRegion + "_complex_en.png";
    complexImage.alt = "Volume evolution of glaciers in " + selectedRegion + " for 1.5°C and 2.7°C.";
  });
</script>


</div>

Do you want to preserve some glacier ice? Find some solutions under the
<a href="{{ site.baseurl }}/preserve/">"How you can help preserve glacier ice?" page</a>.

<br>

## Additional resources
Are you further interested in the future of glaciers? You can discover their
future projected evolution from the following resources: 
- [OGGM-edu: global and regional glacier projections from PyGEM-OGGM for 1.5°C–4.0°C](https://edu.oggm.org/en/latest/global_future_glacier-app_rounce_delta_T_en.html)
- [OGGM-edu: Central Europe's country-wide glacier projections from PyGEM-OGGM for 1.5°C–4.0°C](https://edu.oggm.org/en/latest/alps_future-app_rounce_delta_T_en.html)
- [OGGM-edu: Learn about the world’s glaciers location, climate, and the ice they store](https://bokeh.oggm.org/explorer/app)
- PROVIDE climate risk dashboard where glacier projections from OGGM can be
  selected for every country with glaciers: [link to glacier projections for Austria under 1.5°C and 2020 climate policies scenarios](https://climate-risk-dashboard.climateanalytics.org/impacts/explore?indicator=glacier-volume&geography=AUT&scenarios[0]=curpol&time=annual&reference=present-day-2020&spatial=area)
    - Further explanations available from [this OGGM-edu site](https://edu.oggm.org/en/latest/provide_dashboard.html)
- Most recent information on the *Cryosphere* (ice sheets, glaciers, snow, permafrost, sea ice and
  polar oceans) are summarised in the [*State of the Cryosphere Report 2024*](https://iccinet.org/statecryo24/). "The report
  describes how a combination of melting polar ice sheets, vanishing glaciers, and thawing
  permafrost will have rapid, irreversible, and disastrous impacts worldwide."
