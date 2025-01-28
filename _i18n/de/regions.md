# Globale und regionale Gletscherprojektionen

<div>
  <p>
    Entdecke globale und regionale Projektionen für die mehr als 200.000
    Berggletscher (alle Gletscher außer den Eisschilden von Grönland und der Antarktis).
    Viele Gletscher in den Alpen (Mitteleuropa) werden voraussichtlich bald verschwinden,
    selbst bei einer globalen Erwärmung von nur 1,5°C. Für Gletscher weltweit jedoch macht
    jeder Bruchteil eines Grad an Erwärmung einen Unterschied.
  </p>
  <p>
    Erkunde die regionalen Projektionen, um zu sehen, wie die Begrenzung der globalen Erwärmung
    auf 1,5°C helfen kann, den Gletschervolumenverlust zu verringern:
  </p>
</div>

<!-- Dropdown zur Regionenauswahl -->

<div>
  <select id="regionSelect" style="font-size: 24px; padding: 10px; border: 2px solid #FF5733; border-radius: 5px; background-color: #f8d7da; width: auto; min-width: 200px;">
    <option value="RGI11" selected>Mitteleuropa (11)</option>
    <option value="global">Global</option>
    <option value="RGI01">Alaska (01)</option>
    <option value="RGI02">Westkanada und USA (02)</option>
    <option value="RGI03">Arktisches Kanada Nord (03)</option>
    <option value="RGI04">Arktisches Kanada Süd (04)</option>
    <option value="RGI05">Grönland Peripherie (05)</option>
    <option value="RGI06">Island (06)</option>
    <option value="RGI07">Svalbard (07)</option>
    <option value="RGI08">Skandinavien (08)</option>
    <option value="RGI09">Russische Arktis (09)</option>
    <option value="RGI10">Nordasien (10)</option>
    <option value="RGI12">Kaukasus und Naher Osten (12)</option>
    <option value="RGI13">Zentralasien (13)</option>
    <option value="RGI14">Südasien West (14)</option>
    <option value="RGI15">Südasien Ost (15)</option>
    <option value="RGI13-14-15">Hochgebirgsasien (13-14-15)</option>
    <option value="RGI16">Tropische Breiten (16)</option>
    <option value="RGI17">Südliche Anden (17)</option>
    <option value="RGI18">Neuseeland (18)</option>
    <option value="RGI19">Subantarktische und Antarktische Inseln (19)</option>
  </select>

  <!-- Container für beide Abbildungen -->
  <img id="worldmapImage" src="/assets/images/volume_evolution_regions/RGI11_worldmap_de.png" alt="Karte der ausgewählten Gletscher" />
  <img id="complexImage" src="/assets/images/volume_evolution_regions/RGI11_complex_de.png" alt="Volumenentwicklung der Gletscher in Mitteleuropa für 1,5°C und 2,7°C." />

  <!-- Füge responsives CSS hinzu -->
  <style>
    @media (max-width: 768px) {
      div[style*="display: flex"] {
        flex-direction: column; /* Elemente vertikal stapeln */
      }
      div[style*="margin-right: 20px"] {
        margin-right: 0; /* Entfernt den rechten Rand für den Text */
      }
    }
  </style>

  <script>
    document.getElementById("regionSelect").addEventListener("change", function() {
      var selectedRegion = this.value;
    
      // Hole dir beide Bild-Elemente
      var worldmapImage = document.getElementById("worldmapImage");
      var complexImage = document.getElementById("complexImage");
    
      // Aktualisiere die Quelle des Weltkartenbildes
      worldmapImage.src = "/assets/images/volume_evolution_regions/" + selectedRegion + "_worldmap_de.png";
      worldmapImage.alt = "Karte der ausgewählten Gletscher in " + d_reg_num_name_de[selectedRegion];

      // Aktualisiere die Quelle des komplexen Modellbildes
      complexImage.src = "/assets/images/volume_evolution_regions/" + selectedRegion + "_complex_de.png";
      complexImage.alt = "Volumenentwicklung der Gletscher in " + d_reg_num_name_de[selectedRegion] + " für 1,5°C und 2,7°C.";
    });
  </script>
</div>

Möchtest du etwas Gletschereis bewahren? Finde Lösungen auf der <a href="{{ site.baseurl }}/preserve/">"Wie schützen?"</a> Seite.

<br>

## Zusätzliche Informationen
Bist du weiter an der Zukunft der Gletscher interessiert? Auf den folgenden Webseiten kannst du mehr erfahren (nur auf Englisch, aber dein Browser kann es wahrscheinlich ganz gut übersetzen):

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

