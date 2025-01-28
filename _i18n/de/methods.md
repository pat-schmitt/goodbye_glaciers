# Methoden

Diese Seite beschreibt die Methoden, die zur Visualisierung der 3D-Gletscherprojektionen und der Ermittlung des Jahres verwendet werden, in dem der Gletscher "fast verschwunden" ist. Die nachfolgenden detaillierten Erklärungen sind technisch und könnten für Nicht-Wissenschaftler herausfordernd sein, aber wir haben sie hier aufgenommen, um vollständige Transparenz zu gewährleisten.

## Überblick

Wir simulieren die Projektionen der Dicke und des Volumens einzelner Gletscher von 2000 bis 2100 unter Verwendung von Klimaszenarien (Klimamodelle und Emissionsszenarien) aus CMIP5 und CMIP6 sowie großräumigen Gletschermodellen. Wir konzentrieren uns hauptsächlich auf einer globalen Erwärmung von **2,7°C**  im Vergleich zu vorindustriellen Werten bis 2100, da dies das voraussichtliche Ergebnis der [aktuellen politischen Maßnahmen](https://climateactiontracker.org/global/cat-thermometer/) darstellt. Zum Vergleich enthalten wir auch Projektionen unter dem **1,5°C Ziel** des Pariser Abkommens. Wir wählten Klimaszenarien mit einem Bereich von ±0,2°C um 1,5°C oder 2,7°C.

Die Erwärmungsniveaus sind als die globale Mitteltemperaturdifferenz für den Zeitraum 2071–2100 im Vergleich zu 1850–1900 definiert, mit einer Erwärmung von 0,69°C von 1850–1900 bis 1986–2005 (siehe [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/)).

### Definition eines "fast verschwundenen" Gletschers
Wir definieren "fast verschwunden" als das Jahr, in dem entweder weniger als 10% des Gletschervolumens von 2020 oder weniger als 0,01 km³ übrig sein wird – je nachdem, welcher Schwellenwert zuerst erreicht wird. Während kleine Eisflächen über dieses Jahr hinaus bestehen bleiben könnten, wird die Landschaft im Vergleich zu der aktuellen sehr unterschiedlich sein. Dieser 10%-Schwellenwert ist für die Alpen und andere Regionen mit ähnlicher Geometrie geeignet. Die Verwendung beider Schwellenwerte stellt sicher, dass wir "fast verschwunden" sowohl für relativ große Alpen-Gletscher als auch für jene, die heute bereits sehr klein sind, definieren können.

Es ist wichtig zu beachten, dass positive Rückkopplungsmechanismen, wie z.B. lokalisierte Erwärmung aufgrund des Gletscherrückzugs, in großräumigen Gletschermodellen nicht berücksichtigt werden. Das bedeutet, dass der tatsächliche Gletscherrückzug möglicherweise schneller erfolgen könnte als die projizierten Veränderungen.

##### Unterschiede in der Schwellenwert-Definition
Wir stellen fest, dass unsere Definition eines "fast verschwundenen" Gletschers im Median 9 Jahre früher in den Alpen erreicht wird, wenn beide Schwellenwerte (<10% oder <0,01 km³) verwendet werden, im Vergleich zur Verwendung nur des <10%-Schwellenwerts. Im Vergleich zur Verwendung nur des <10%-Schwellenwerts kann der maximale Unterschied dazu führen, dass ein Gletscher 73 Jahre früher als "fast verschwunden" gilt und dass weniger Gletscher bis zum Ende des Jahrhunderts überleben.

Die Änderung der Definition von einem 10%-Schwellenwert auf einen 5%-Schwellenwert führt dazu, dass Gletscher im Median vier Jahre später als "fast verschwunden" gelten und maximal 34 Jahre später. Für ungefähr 40 Gletscher liegt das verbleibende Gletschervolumen im Jahr 2100 zwischen 5% und 10%, was bedeutet, dass diese Gletscher unter dem 5%-Schwellenwert bis zum Ende des Jahrhunderts überleben würden.

### Likely range

Der **wahrscheinliche Bereich** (likely range) beschreibt die Streuung der Projektionen und ist als der 17. bis 83. Perzentilbereich definiert, im Einklang mit dem [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/). Wenn die Daten einer Gaußschen Verteilung folgen, entspricht dieser Bereich ungefähr **einer Standardabweichung** (±1σ) vom Mittelwert, was etwa 68% der verfügbaren Projektionen erfasst.

## Datenquellen und Modelle für die Gletscherprojektionen

Das **2020 Gletschervolumen**, das **Jahr, in dem wir schätzen, dass der Gletscher fast verschwunden ist**, und die **globalen und regionalen Projektionen der Gletschervolumenänderung** stammen aus diesen drei Gletschermodellen (spezifische Modellversionen und Daten sind weiter zusammengefasst in [Zekollari et al. (2024)](https://doi.org/10.5194/tc-18-5045-2024)) durch die Simulation jedes der >200.000 Gletscher einzeln:
- **OGGM v1.6.1**  
  - **Daten:** [DOI](https://doi.org/10.5281/zenodo.8286064)  
  - **Dokumentation:** [OGGM](https://oggm.org/)  
  - **Details:**  
    - CMIP5 und CMIP6 verfügbar.  
    - Beinhaltet weniger genutzte Klimamodelle und Overshoot-Emissionsszenarien.  
    - Für 2,7±0,2°C: n=14 Klimaszenarien 
    - Für 1,5±0,2°C: n=11 Klimaszenarien 
- **PyGEM-OGGM**  
  - **Daten:** [DOI](https://doi.org/10.5067/P8BN9VO9N5C7)  
  - **Dokumentation:** [PyGEM](https://pygem.readthedocs.io/en/latest/introduction.html)  
  - **Details:**  
    - CMIP5 und CMIP6 verfügbar.  
    - Dieselben Szenarien wie in [Rounce et al., 2023](https://doi.org/10.1126/science.abo1324).  
    - Für 2,7±0,2°C: n=7 Klimaszenarien  
    - Für 1,5±0,2°C: n=9 Klimaszenarien 
- **GloGEM**  
  - **Daten:** [DOI](https://doi.org/10.5281/zenodo.10908277)  
  - **Dokumentation:** [Huss & Hock (2015)](https://doi.org/10.3389/feart.2015.00054)  
  - **Details:**  
    - Nur CMIP6.  
    - Für 2,7±0,2°C: n=3 Klimaszenarien  
    - Für 1,5±0,2°C: n=4 Klimaszenarien 

Die **3D Gletscherprojektionen der Eisdicke** basieren ausschließlich auf OGGM-Simulationen und werden mit dem [Glacier:3D-Viz](https://glacier3dviz.oggm.org/tutorials/welcome.html) Tool visualisiert. Diese 3D-Projektionen weichen leicht von den anderen Schätzungen ab, die auf einer Kombination von drei Gletschermodellen basieren.

Beachten Sie, dass diese Gletscherprojektionen auf globalen Gletschermodellen basieren, die weltweit verfügbare Beobachtungsdaten von Gletschern verwenden. Daten, die nur für einige wenige Gletscher verfügbar sind (d.h. nur geodätische, aber keine direkten In-situ-Beobachtungen werden verwendet), sind nicht enthalten. Daher performen die Modelle auf globaler Ebene besser als auf der Ebene einzelner Gletscher. Obwohl einige wichtige Prozesse auf der Ebene einzelner Gletscher nicht dargestellt sind, präsentieren wir hier Ergebnisse für einzelne Gletscher zu Bildungszwecken. Zudem ist das individuelle Gletscher und regionale Volumen im Jahr 2020 kein beobachtetes Gletschervolumen, sondern ein modelliertes Volumen (es handelt sich um die Median-Schätzung des Gletschermodells der Multi-Klimamodell-Mediane).

## Ergebnisaggregation

Für das **2020 Gletschervolumen**, das **Abschmelzjahr** und die **globalen und regionalen Projektionen der Gletschervolumenänderung** präsentieren wir den **Median** und den **wahrscheinlichen Bereich** über alle verfügbaren Kombinationen von Gletschermodellen und Klimaszenarien. Da OGGM mehr Klimaszenarien umfasst, tragen seine Projektionen am meisten zum Gesamtergebnis bei.

Die durchschnittliche globale Erwärmung über vorindustrielle Werte bei allen Kombinationen von Gletschermodellen und Klimaszenarien beträgt:  
- **1,57°C** für den **1,5±0,2°C** Bereich.  
- **2,71°C** für den **2,7±0,2°C** Bereich.

## Fotoquellen und Lizenzen
<style>
  .photo-container {
    display: flex;
    align-items: flex-start;
    border: 1px solid #ddd; /* Fügt jedem Fotoblock einen hellgrauen Rand hinzu */
    padding: 10px; /* Fügt Abstand zwischen Inhalt und Rand hinzu */
    margin-bottom: 10px; /* Fügt Abstand zwischen Fotoblocks hinzu */
    border-radius: 5px; /* Abrundung der Ecken des Rands */
    background-color: #f9f9f9; /* Helle Hintergrundfarbe für besseren Kontrast */
  }

  .photo-container img {
    margin-right: 10px; /* Fügt Abstand zwischen dem Bild und dem Text hinzu */
    width: 100px; /* Fixiert die Bildbreite */
    height: auto; /* Bewahrt das Seitenverhältnis */
    border-radius: 5px; /* Optional: Fügt den Bildern abgerundete Ecken hinzu */
    min-width: 100px;
  }

  .photo-container .text-content {
    display: block;
    flex-direction: column; /* Stapelt den Textinhalt vertikal */
  }

  .photo-container a {
    color: #0073e6; /* Macht Links visuell auffällig */
    text-decoration: none; /* Entfernt die Unterstreichung von Links */
  }

  .photo-container a:hover {
    text-decoration: underline; /* Fügt eine Unterstreichung hinzu, wenn der Mauszeiger darüber schwebt */
  }

</style>
<div>
  {% for photo in site.photos %}
    <div class="photo-container" id="{{ photo.photo_id }}">
      <a href="{{ site.baseurl }}{{ photo.filename }}">
        <img src="{{ site.baseurl }}{{ photo.filename }}" alt="{{ photo.photo_id }}" style="width: 100px; height: auto;">
      </a>
      <div class="text-content">
        {% if photo.photographer_name %}
          <b>Photographer:</b> {{ photo.photographer_name }}
        {% endif %}
        {% if photo.photo_date %}
          <br><b>Date:</b> {{ photo.photo_date }}
        {% endif %}
        {% if photo.photo_link %}
          <br><b>Original URL:</b> <a href="{{ photo.photo_link }}">{{ photo.photo_link }}</a>
        {% endif %}
        {% if photo.citation %}
          <br><b>Citation:</b> {{ photo.citation }}
        {% endif %}
        {% if photo.photo_license %}
          <br><b>License:</b> <a href="{{ photo.photo_license_url }}">{{ photo.photo_license }}</a>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>

