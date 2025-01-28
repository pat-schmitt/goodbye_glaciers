# Metodi

Questa pagina descrive le metodologie utilizzate per stimare l'anno in cui
il ghiacciaio sarà 'quasi scomparso' e per le visualizzazioni delle proiezioni dei ghiacciai. Le spiegazioni dettagliate fornite di seguito sono piuttosto tecniche e potrebbero risultare difficili per i non-scienziati, ma le abbiamo incluse qui per garantire la piena trasparenza.

## Panoramica

Simuliamo le proiezioni dello spessore e del volume dei singoli ghiacciai dal 2000 al 2100 utilizzando scenari climatici (modelli climatici e scenari di emissione) provenienti da CMIP5 e CMIP6 e modelli globali dei ghiacciai. Ci concentriamo principalmente sul riscaldamento globale di **2,7°C** sopra i livelli pre-industriali entro il 2100, poiché rappresenta l'esito previsto del mondo reale delle [politiche e azioni attuali](https://climateactiontracker.org/global/cat-thermometer/). A scopo comparativo, includiamo anche le proiezioni sotto l'**obiettivo di 1,5°C** dell'Accordo di Parigi. Abbiamo scelto scenari climatici con una gamma di ±0,2°C da 1,5°C o 2,7°C.

I livelli di riscaldamento sono definiti come la differenza di temperatura media globale dal 2071 al 2100 rispetto al periodo 1850-1900, con un riscaldamento di 0,69°C dal 1850-1900 al 1986-2005 (rif. [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/)).

### Definizione di un ghiacciaio 'quasi scomparso'
Definiamo 'quasi scomparso' come l'anno in cui si prevede che rimanga meno del 10% del volume del ghiacciaio del 2020 o meno di 0,01 km³ - a seconda di quale soglia venga superata per prima. Sebbene piccole macchie di ghiaccio possano persistere oltre questo anno, il paesaggio sarà molto diverso rispetto a quello attuale. Questa soglia del 10% è considerata appropriata per le Alpi e le regioni con ghiacciai simili in termini di geometria. L'uso di entrambe le soglie ci consente di definire 'quasi scomparso' sia per i ghiacciai alpini relativamente grandi che per quelli già molto piccoli oggi.

È importante notare che i meccanismi di feedback positivi, come il riscaldamento localizzato dovuto al ritiro dei ghiacciai, non sono considerati nei modelli globali dei ghiacciai. Ciò significa che, sebbene i cambiamenti nei ghiacciai che utilizziamo qui siano le proiezioni più affidabili disponibili, il ritiro effettivo dei ghiacciai potrebbe avvenire più rapidamente.

##### Differenze nelle definizioni delle soglie
Abbiamo constatato che la nostra definizione di un ghiacciaio 'quasi scomparso' è, in media, 9 anni prima nelle Alpi quando si utilizzano le due soglie (<10% o <0,01 km³) rispetto all'uso della sola soglia <10%. Rispetto all'uso esclusivo della soglia <10%, la differenza massima può significare che un ghiacciaio sia 'quasi scomparso' 73 anni prima e che meno ghiacciai sopravvivano fino alla fine del secolo.

Cambiare la definizione da una soglia del 10% a una soglia del 5% comporta che i ghiacciai siano 'quasi scomparsi', in media, quattro anni dopo e, al massimo, 34 anni dopo. Per circa 40 ghiacciai, il volume residuo del ghiacciaio nel 2100 è compreso tra il 5% e il 10%, il che significa che questi ghiacciai sopravviverebbero fino alla fine del secolo con la soglia del 5%.

### Likely range

L'**intervallo probabile** ("likely range") descrive la diffusione delle proiezioni ed è definito come il 17° e 83° percentile, coerente con [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/). Se i dati seguono una distribuzione gaussiana, questa gamma corrisponde approssimativamente a **una deviazione standard** (±1σ) dalla media, catturando circa il 68% delle proiezioni disponibili.

## Fonti di dati e modelli delle proiezioni dei ghiacciai

Il **volume dei ghiacciai nel 2020**, l'**anno in cui stimiamo che il ghiacciaio sarà quasi scomparso** e le **proiezioni dei cambiamenti del volume dei ghiacciai globali e regionali** sono derivati da questi tre modelli di ghiacciai (versioni specifiche dei modelli e dati ulteriormente riassunti in [Zekollari et al. (2024)](https://doi.org/10.5194/tc-18-5045-2024)) simulando ciascuno dei >200.000 ghiacciai individualmente:
- **OGGM v1.6.1**  
  - **Dati:** [DOI](https://doi.org/10.5281/zenodo.8286064)  
  - **Documentazione:** [OGGM](https://oggm.org/)  
  - **Dettagli:**  
    - Disponibile CMIP5 e CMIP6.  
    - Include modelli climatici meno utilizzati e scenari di emissione di overshoot.  
    - Per 2.7±0.2°C: n=14 scenari climatici  
    - Per 1.5±0.2°C: n=11 scenari climatici  
- **PyGEM-OGGM**  
  - **Dati:** [DOI](https://doi.org/10.5067/P8BN9VO9N5C7)  
  - **Documentazione:** [PyGEM](https://pygem.readthedocs.io/en/latest/introduction.html)  
  - **Dettagli:**  
    - Disponibile CMIP5 e CMIP6.  
    - Gli stessi scenari presentati in [Rounce et al., 2023](https://doi.org/10.1126/science.abo1324).  
    - Per 2.7±0.2°C: n=7 scenari climatici  
    - Per 1.5±0.2°C: n=9 scenari climatici  
- **GloGEM**  
  - **Dati:** [DOI](https://doi.org/10.5281/zenodo.10908277)  
  - **Documentazione:** [Huss & Hock (2015)](https://doi.org/10.3389/feart.2015.00054)  
  - **Dettagli:**  
    - Solo CMIP6.  
    - Per 2.7±0.2°C: n=3 scenari climatici  
    - Per 1.5±0.2°C: n=4 scenari climatici  

Le **proiezioni 3D dello spessore dei ghiacciai** si basano esclusivamente sulle simulazioni OGGM
e sono visualizzate utilizzando lo strumento [Glacier:3D-Viz](https://glacier3dviz.oggm.org/tutorials/welcome.html). Queste proiezioni 3D differiscono
lievemente dalle altre stime, che si basano su una combinazione di tre
modelli di ghiacciai.

Si noti che queste proiezioni dei ghiacciai si basano su modelli globali che utilizzano
dati di osservazione dei ghiacciai disponibili a livello globale. I dati disponibili solo
per alcuni ghiacciai (cioè solo osservazioni geodetiche ma nessuna osservazione in-situ
direttamente utilizzata) non sono inclusi. Di conseguenza, i modelli funzionano meglio su scala globale rispetto alla
scala di singoli ghiacciai. Sebbene alcuni processi importanti a livello del singolo
ghiacciaio non siano rappresentati, presentiamo qui i risultati dei singoli ghiacciai
a scopo educativo. Inoltre, il volume per singolo ghiacciaio e regionale nel
2020 non è un volume osservato, ma un volume modellato (è la stima mediana del modello di ghiacciaio
delle mediane dei modelli climatici multipli).

## Aggregazione dei risultati

Per il **volume dei ghiacciai nel 2020**, l'**anno di deglaciazione** e le **proiezioni di cambiamento del volume dei ghiacciai regionali**, presentiamo la **mediana** e l'**intervallo probabile**
across all combinations of glacier models and climate scenarios. Since OGGM includes more climate scenarios, its projections contribute the most weight to the overall results.  

La media del riscaldamento globale rispetto ai livelli pre-industriali per tutte le combinazioni di modelli climatici e scenari climatici è:  
- **1.57°C** per la gamma **1,5±0,2°C**.  
- **2.71°C** per la gamma **2,7±0,2°C**.  

## Fonti fotografiche e licenze
<style>
  .photo-container {
    display: flex;
    align-items: flex-start;
    border: 1px solid #ddd; /* Adds a light gray border around each photo block */
    padding: 10px; /* Adds space between the content and the border */
    margin-bottom: 10px; /* Adds space between each photo block */
    border-radius: 5px; /* Rounds the corners of the border */
    background-color: #f9f9f9; /* Light background color for better contrast */
  }

  .photo-container img {
    margin-right: 10px; /* Adds space between the image and the text */
    width: 100px; /* Fixes image width */
    height: auto; /* Maintains aspect ratio */
    border-radius: 5px; /* Optional: adds rounded corners to the image */
    min-width: 100px;
  }

  .photo-container .text-content {
    display: block;
    flex-direction: column; /* Stacks text content vertically */
  }

  .photo-container a {
    color: #0073e6; /* Makes links visually distinct */
    text-decoration: none; /* Removes underline from links */
  }

  .photo-container a:hover {
    text-decoration: underline; /* Adds underline on hover for clarity */
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
          <b>Fotografo:</b> {{ photo.photographer_name }}
        {% endif %}
        {% if photo.photo_date %}
          <br><b>Data:</b> {{ photo.photo_date }}
        {% endif %}
        {% if photo.photo_link %}
          <br><b>URL originale:</b> <a href="{{ photo.photo_link }}">{{ photo.photo_link }}</a>
        {% endif %}
        {% if photo.citation %}
          <br><b>Citazione:</b> {{ photo.citation }}
        {% endif %}
        {% if photo.photo_license %}
          <br><b>Licenza:</b> <a href="{{ photo.photo_license_url }}">{{ photo.photo_license }}</a>
        {% endif %}
      </div>
    </div>
  {% endfor %}
</div>

