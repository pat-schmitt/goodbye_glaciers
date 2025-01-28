# Proiezioni globali e regionali dei ghiacciai

<div>
  <p>
    Scopri le proiezioni globali e regionali per oltre 200.000 ghiacciai di montagna (tutti i ghiacciai esclusi le calotte glaciali di Groenlandia e Antartide).
    Molti ghiacciai nelle Alpi (Europa centrale) sono destinati a scomparire presto, anche con un riscaldamento globale di 1,5°C. Tuttavia, per i ghiacciai di tutto il mondo, ogni decimo di grado di riscaldamento fa la differenza.
  </p>
  <p>
    Esplora le proiezioni regionali per vedere come limitare il riscaldamento globale a 1,5°C può aiutare a ridurre la perdita di volume dei ghiacciai:
  </p>
</div>

<!-- Dropdown to select region -->

<div>
<select id="regionSelect" style="font-size: 24px; padding: 10px; border: 2px solid #FF5733; border-radius: 5px; background-color: #f8d7da; width: auto; min-width: 200px;">
  <option value="RGI11" selected>Europa Centrale (11)</option>
  <option value="global">Globale</option>
  <option value="RGI01">Alaska (01)</option>
  <option value="RGI02">Canada Occidentale e Stati Uniti (02)</option>
  <option value="RGI03">Artico Canadese Settentrionale (03)</option>
  <option value="RGI04">Artico Canadese Meridionale (04)</option>
  <option value="RGI05">Periferia della Groenlandia (05)</option>
  <option value="RGI06">Islanda (06)</option>
  <option value="RGI07">Svalbard (07)</option>
  <option value="RGI08">Scandinavia (08)</option>
  <option value="RGI09">Artico Russo (09)</option>
  <option value="RGI10">Asia Settentrionale (10)</option>
  <option value="RGI12">Caucaso e Medio Oriente (12)</option>
  <option value="RGI13">Asia Centrale (13)</option>
  <option value="RGI14">Asia Meridionale Occidentale (14)</option>
  <option value="RGI15">Asia Meridionale Orientale (15)</option>
  <option value="RGI13-14-15">Asia d’Alta Montagna (13-14-15)</option>
  <option value="RGI16">Basse Latitudini (16)</option>
  <option value="RGI17">Ande Meridionali (17)</option>
  <option value="RGI18">Nuova Zelanda (18)</option>
  <option value="RGI19">Isole Subantartiche e Antartiche (19)</option>
</select>

<!-- Image containers for both figures -->
<img id="worldmapImage" src="/assets/images/volume_evolution_regions/RGI11_worldmap_it.png" alt="Mappa dei ghiacciai selezionati" />
<img id="complexImage" src="/assets/images/volume_evolution_regions/RGI11_complex_it.png" alt="Evoluzione del volume dei ghiacciai in Europa Centrale per 1,5°C e 2,7°C." />

<!-- Add responsive CSS -->
<style>
  @media (max-width: 768px) {
    div[style*="display: flex"] {
      flex-direction: column; /* Impila gli elementi verticalmente */
    }
    div[style*="margin-right: 20px"] {
      margin-right: 0; /* Rimuove il margine destro per il testo */
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
    worldmapImage.src = "/assets/images/volume_evolution_regions/" + selectedRegion + "_worldmap_it.png";
    worldmapImage.alt = "Mappa dei ghiacciai selezionati in " + selectedRegion;

    // Update complex model image source
    complexImage.src = "/assets/images/volume_evolution_regions/" + selectedRegion + "_complex_it.png";
    complexImage.alt = "Evoluzione del volume dei ghiacciai in " + selectedRegion + " per 1,5°C e 2,7°C.";
  });
</script>


</div>

Vuoi preservare del ghiaccio dei ghiacciai? Trova delle soluzioni nella pagina
<a href="{{ site.baseurl }}/preserve/">"Come preservare?"</a>.

<br>

## Risorse aggiuntive
Sei interessato ulteriormente al futuro dei ghiacciai? Puoi imparare di più sui seguenti siti web (solo in inglese, ma il tuo browser probabilmente può tradurlo abbastanza bene):

- [OGGM-edu: global and regional glacier projections from a single glacier model (PyGEM-OGGM) for 1.5°C–4.0°C](https://edu.oggm.org/en/latest/global_future_glacier-app_rounce_delta_T_en.html)
- [OGGM-edu: Central Europe's country-wide glacier projections from a single glacier model PyGEM-OGGM for 1.5°C–4.0°C](https://edu.oggm.org/en/latest/alps_future-app_rounce_delta_T_en.html)
- [OGGM-edu: Learn about the world’s glaciers location, climate, and the ice they store](https://bokeh.oggm.org/explorer/app)
- PROVIDE climate risk dashboard where glacier projections from a single glacier model (OGGM) can be
  selected for every country with glaciers: [link to glacier projections for Austria under 1.5°C and 2020 climate policies scenarios](https://climate-risk-dashboard.climateanalytics.org/impacts/explore?indicator=glacier-volume&geography=AUT&scenarios[0]=curpol&time=annual&reference=present-day-2020&spatial=area)
    - Further explanations available from [this OGGM-edu site](https://edu.oggm.org/en/latest/provide_dashboard.html)
- Most recent information on the *Cryosphere* (ice sheets, glaciers, snow, permafrost, sea ice and
  polar oceans) are summarised in the [*State of the Cryosphere Report 2024*](https://iccinet.org/statecryo24/). "The report
  describes how a combination of melting polar ice sheets, vanishing glaciers, and thawing
  permafrost will have rapid, irreversible, and disastrous impacts worldwide."

