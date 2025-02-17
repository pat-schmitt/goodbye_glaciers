# Méthodes

Cette page décrit les méthodes utilisées pour estimer l'année où le glacier aura "presque disparu" et pour obtenir les visualisations de projections des glaciers. Les explications détaillées fournies ci-dessous sont quelque peu techniques et peuvent être difficiles à comprendre pour les non-scientifiques, mais nous les avons incluses ici pour garantir une transparence totale.

## Aperçu

Nous simulons les projections d'épaisseur et de volume de chaque glacier de 2000 à 2100 en couplant des scénarios climatiques provenant de CMIP5 et CMIP6 (modèles climatiques et scénarios d'émissions) et des modèles de glaciers à grande échelle. Nous nous concentrons sur un réchauffement global de **2,7°C** par rapport à l'ère pré-industrielle d'ici 2100, car c’est ce vers quoi nous tendons dans le cadre des [politiques et actions actuelles](https://climateactiontracker.org/global/cat-thermometer/). Pour comparaison, nous incluons également des projections sous l'objectif de **1,5°C** de l'Accord de Paris. Nous avons choisi des scénarios climatiques avec une plage de ±0,2°C par rapport à 1,5°C ou 2,7°C. 

Les niveaux de réchauffement sont définis comme la différence de température moyenne mondiale de 2071-2100 par rapport à 1850-1900, avec un réchauffement de 0,69°C de 1850-1900 à 1986-2005 (réf. [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/)).

### Définition d'un glacier ayant "presque disparu"
Nous considérons qu’un glacier a "presque disparu" l'année où 1/ le glacier a perdu plus de 90% de son volume de 2020 ou 2/ le glacier fait moins de 0,01 km³. Bien que des restes de glace puissent subsister au-delà de cette année, le paysage sera très différent de l’actuel et apparaîtra comme dépourvu de tout glacier. Ce seuil de 10% est considéré comme valable pour les Alpes et les régions ayant des glaciers aux géométries similaires. L'utilisation de ces deux seuils garantit la possibilité d’appliquer la définition d’ayant "presque disparu" à la fois aux glaciers relativement grands et à ceux déjà très petits aujourd'hui.

Il est important de noter que les mécanismes de rétroaction positive, tels que le réchauffement local dû au retrait des glaciers, ne sont pas pris en compte dans les modèles de glaciers à grande échelle. Cela signifie que, bien que les changements des glaciers que nous utilisons ici soient les projections les plus fiables actuellement disponibles, le retrait réel des glaciers pourrait se produire plus rapidement.

##### Sensibilité à la définition des seuils
Notre définition d'un glacier ayant "presque disparu" se produit, en médiane 9 ans plus tôt dans les Alpes, et davantage de glaciers survivent jusqu’à la fin du siècle lorsque nous utilisons les deux seuils (<10% ou <0,01 km³) que lorsque nous utilisons uniquement le seuil <10%. Dans le cas le plus extrême, l’écart entre ces deux définitions atteint 73 ans.

Un changement de seuil de 10% à 5% entraîne la "presque disparition" des glaciers en médiane quatre ans plus tard, et au maximum 34 ans plus tard. Pour une quarantaine de glaciers, le volume restant du glacier en 2100 est compris entre 5% et 10%, ce qui signifie que ces glaciers survivraient jusqu'à la fin du siècle selon le seuil de 5%.

### Plage probable

La **plage probable** ("likely range") décrit la répartition des projections et est définie par les 17èmes et 83èmes centiles, selon la même définition que l’[IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/). En faisant l’hypothèse que les données suivent une distribution gaussienne, cette plage correspondrait approximativement à **un écart-type** (±1σ) par rapport à la moyenne, capturant environ 68% des projections disponibles.

## Sources des données et modèles de projection des glaciers

Le **volume du glacier en 2020**, **l'année où nous estimons que le glacier aura presque disparu**, et **les projections mondiales et régionales du changement de volume des glaciers** sont dérivés de trois modèles de glaciers (versions spécifiques des modèles et données résumées dans [Zekollari et al. (2024)](https://doi.org/10.5194/tc-18-5045-2024)) en simulant chacun des plus de 200 000 glaciers individuellement :

- **OGGM v1.6.1**
  - **Données** : [DOI](https://doi.org/10.5281/zenodo.8286064)
  - **Documentation** : [OGGM](https://oggm.org/)
  - **Détails** :
    - CMIP5 et CMIP6.
    - Inclut des modèles climatiques moins utilisés et des scénarios d'émissions excédentaires.
    - Pour 2.7±0.2°C : n=14 scénarios climatiques
    - Pour 1.5±0.2°C : n=11 scénarios climatiques
- **PyGEM-OGGM**
  - **Données** : [DOI](https://doi.org/10.5067/P8BN9VO9N5C7)
  - **Documentation** : [PyGEM](https://pygem.readthedocs.io/en/latest/introduction.html)
  - **Détails** :
    - CMIP5 et CMIP6.
    - Même scénarios que présentés dans [Rounce et al., 2023](https://doi.org/10.1126/science.abo1324).
    - Pour 2.7±0.2°C : n=7 scénarios climatiques
    - Pour 1.5±0.2°C : n=9 scénarios climatiques
- **GloGEM**
  - **Données** : [DOI](https://doi.org/10.5281/zenodo.10908277)
  - **Documentation** : [Huss & Hock (2015)](https://doi.org/10.3389/feart.2015.00054)
  - **Détails** :
    - CMIP6 uniquement.
    - Pour 2.7±0.2°C : n=3 scénarios climatiques
    - Pour 1.5±0.2°C : n=4 scénarios climatiques

Les **projections 3D de l'épaisseur des glaciers** sont basées uniquement sur les simulations faites avec le modèle OGGM et l’outil de visualisation [Glacier:3D-Viz](https://glacier3dviz.oggm.org/tutorials/welcome.html). Ces projections 3D diffèrent légèrement des autres estimations, qui sont basées sur la combinaison des trois modèles de glaciers.  

Notez que ces projections de glaciers sont basées sur des modèles de glaciers utilisant des données d'observation des glaciers disponibles au niveau mondial. Les données qui ne sont disponibles que pour quelques glaciers ne sont pas incluses, ce qui signifie que nous prenons en compte les bilans de masse géodésiques mais pas directement les données ponctuelles de bilan de masse réalisées sur le terrain. En conséquence, les modèles que nous utilisons sont plus performants à l'échelle mondiale qu'à l'échelle des glaciers individuels. Bien que certains processus importants à l'échelle des glaciers individuels ne soient pas représentés, nous présentons ici ces résultats à des fins pédagogiques. De plus, le volume par glacier et régional en 2020 n'est pas un volume observé mais un volume modélisé (c'est l'estimation médiane du modèle de glacier des multiples modèles climatiques).

## Agrégation des résultats

Pour le **volume du glacier en 2020**, **l'année de déglaciation**, et les **projections régionales du changement de volume des glaciers**, nous présentons la **médiane** et la **plage probable** sur toutes les combinaisons disponibles de modèles de glaciers et de scénarios climatiques. Puisque OGGM comprend d’avantage de scénarios climatiques, ses projections contribuent le plus à l'ensemble des résultats.

Le réchauffement moyen global au-dessus du niveau pré-industriel sur toutes les combinaisons de modèles de glaciers et de scénarios climatiques est :  
- **1,57°C** pour la plage **1,5±0,2°C**.  
- **2,71°C** pour la plage **2,7±0,2°C**.

## Sources de photos et licences

<style>
  .photo-container {
    display: flex;
    align-items: flex-start;
    border: 1px solid #ddd; /* Ajoute une bordure grise claire autour de chaque bloc de photo */
    padding: 10px; /* Ajoute de l'espace entre le contenu et la bordure */
    margin-bottom: 10px; /* Ajoute de l'espace entre chaque bloc de photo */
    border-radius: 5px; /* Arrondit les coins de la bordure */
    background-color: #f9f9f9; /* Couleur de fond claire pour un meilleur contraste */
  }

  .photo-container img {
    margin-right: 10px; /* Ajoute de l'espace entre l'image et le texte */
    width: 100px; /* Fixe la largeur de l'image */
    height: auto; /* Maintient le ratio de l'image */
    border-radius: 5px; /* Optionnel : ajoute des coins arrondis à l'image */
    min-width: 100px;
  }

  .photo-container .text-content {
    display: block;
    flex-direction: column; /* Empile le texte verticalement */
  }

  .photo-container a {
    color: #0073e6; /* Rend les liens visuellement distincts */
    text-decoration: none; /* Supprime le soulignement des liens */
  }

  .photo-container a:hover {
    text-decoration: underline; /* Ajoute un soulignement au survol pour plus de clarté */
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
          <b>Photographe :</b> {{ photo.photographer_name }}
        {% endif %}
        {% if photo.photo_date %}
          <br><b>Date :</b> {{ photo.photo_date }}
        {% endif %}
        {% if photo.photo_link %}
          <br><b>URL d'origine :</b> <a href="{{ photo.photo_link }}">{{ photo.photo_link }}</a>
        {% endif %}
        {% if photo.citation %}
          <br><b>Citation :</b> {{ photo.citation }}
        {% endif %}
        {% if photo.photo_license %}
          <br><b>Licence :</b> <a href="{{ photo.photo_license_url }}">{{ photo.photo_license }}</a>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>

