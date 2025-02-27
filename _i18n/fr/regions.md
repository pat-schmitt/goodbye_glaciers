# Projections mondiales et régionales des glaciers

<div>
  <p>
    Découvrez les projections mondiales et régionales pour plus de 200 000 glaciers de montagne (tous les glaciers à l'exception des calottes glaciaires du Groenland et de l'Antarctique).
    De nombreux glaciers des Alpes (Europe centrale) devraient disparaître rapidement, même avec un réchauffement mondial limité à 1,5°C. Cependant, pour les autres glaciers du monde entier, chaque dixième de degré de réchauffement fait une différence.
  </p>
  <p>
    Explorez les projections régionales pour voir comment la limitation du réchauffement mondial à 1,5°C aide à réduire la perte de volume des glaciers :
  </p>
</div>

<!-- Dropdown to select region -->

<div>
<select id="regionSelect"
  style="font-size: 24px; padding: 10px; border: 2px solid #FF5733;
       border-radius: 5px; background-color: #f8d7da; max-width: 100%;
       overflow: hidden; text-overflow: ellipsis;">
  <option value="RGI11" selected>Europe Centrale (11)</option>
  <option value="global">Global</option>
  <option value="RGI01">Alaska (01)</option>
  <option value="RGI02">Canada Occidental et États-Unis (02)</option>
  <option value="RGI03">Arctique Canadien Nord (03)</option>
  <option value="RGI04">Arctique Canadien Sud (04)</option>
  <option value="RGI05">Périphérie du Groenland (05)</option>
  <option value="RGI06">Islande (06)</option>
  <option value="RGI07">Svalbard (07)</option>
  <option value="RGI08">Scandinavie (08)</option>
  <option value="RGI09">Arctique Russe (09)</option>
  <option value="RGI10">Asie du Nord (10)</option>
  <option value="RGI12">Caucase et Moyen-Orient (12)</option>
  <option value="RGI13">Asie Centrale (13)</option>
  <option value="RGI14">Asie du Sud-Ouest (14)</option>
  <option value="RGI15">Asie du Sud-Est (15)</option>
  <option value="RGI13-14-15">Asie de Haute Montagne (13-14-15)</option>
  <option value="RGI16">Basses Latitudes (16)</option>
  <option value="RGI17">Andes Méridionales (17)</option>
  <option value="RGI18">Nouvelle-Zélande (18)</option>
  <option value="RGI19">Îles Subantarctiques et Antarctiques (19)</option>
</select>

<!-- Image containers for both figures -->
<img id="worldmapImage" src="/assets/images/volume_evolution_regions/RGI11_worldmap_fr.png" alt="Carte des glaciers sélectionnés" />
<img id="complexImage" src="/assets/images/volume_evolution_regions/RGI11_complex_fr.png" alt="Évolution du volume des glaciers en Europe Centrale pour 1,5°C et 2,7°C." />

<!-- Add responsive CSS -->
<style>
  @media (max-width: 768px) {
    div[style*="display: flex"] {
      flex-direction: column; /* Empile les éléments verticalement */
    }
    div[style*="margin-right: 20px"] {
      margin-right: 0; /* Supprime la marge droite pour le texte */
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
    worldmapImage.src = "/assets/images/volume_evolution_regions/" + selectedRegion + "_worldmap_fr.png";
    worldmapImage.alt = "Carte des glaciers sélectionnés dans " + selectedRegion;

    // Update complex model image source
    complexImage.src = "/assets/images/volume_evolution_regions/" + selectedRegion + "_complex_fr.png";
    complexImage.alt = "Évolution du volume des glaciers dans " + selectedRegion + " pour 1,5°C et 2,7°C.";
  });
</script>


</div>

Vous voulez préserver les glaciers ? Trouvez des solutions à la page
<a href="{{ site.baseurl }}/preserve/">"Comment préserver ?"</a>.

<br>

## Ressources supplémentaires
Vous souhaitez en savoir plus sur l'avenir des glaciers ? Vous pouvez en apprendre davantage sur les sites web suivants (uniquement en anglais, mais votre navigateur peut probablement faire une traduction correcte):

- [OGGM-edu: global and regional glacier projections from a single glacier model (PyGEM-OGGM) for 1.5°C–4.0°C](https://edu.oggm.org/en/latest/global_future_glacier-app_rounce_delta_T_en.html)
- [OGGM-edu: Central Europe's country-wide glacier projections from a single glacier model PyGEM-OGGM for 1.5°C–4.0°C](https://edu.oggm.org/en/latest/alps_future-app_rounce_delta_T_en.html)
- [OGGM-edu: Learn about the world’s glaciers location, climate, and the ice they store](https://bokeh.oggm.org/explorer/app)
- Le tableau de bord du projet PROVIDE sur les risques climatiques où les projections glaciaires issues du modèle OGGM peuvent être sélectionnées pour l'ensemble des régions montagneuses englacées: [link to glacier projections for Austria under 1.5°C and 2020 climate policies scenarios](https://climate-risk-dashboard.climateanalytics.org/impacts/explore?indicator=glacier-volume&geography=AUT&scenarios[0]=curpol&time=annual&reference=present-day-2020&spatial=area)
    - De plus amples informations ici [this OGGM-edu site](https://edu.oggm.org/en/latest/provide_dashboard.html)
- Les informations les plus récentes sur la *Cryosphère* (calottes glaciaires, glaciers, neige, pergélisol, glace de mer et océans polaires) sont résumés
  dans ce rapport [*State of the Cryosphere Report 2024*](https://iccinet.org/statecryo24/). " Le rapport décrit comment la fonte
  des calottes polaires, la disparition des glaciers et le dégel du pergélisol sera rapide, irréversible et avec des impacts désastreux dans le monde entier."

