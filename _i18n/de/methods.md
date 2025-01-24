# DE: Methods

This page describes the technical methodology used for estimating the year where the glacier is 'mostly gone' and the glacier projection visualizations. The detailed explanations provided below are somewhat technical and might be challenging for non-scientists, but we have included them here to ensure full transparency.

## Overview

We simulate individual glacier thickness and volume projections from 2000 to 2100 using climate scenarios (climate models and emission scenarios) from CMIP5 and CMIP6 and large-scale glacier models. We primarily focus on **+2.7°C** global warming above pre-industrial by 2100, as this represents the predicted real-world outcome of [current policies and actions](https://climateactiontracker.org/global/cat-thermometer/). For comparison, we also include projections under the **+1.5°C target** of the Paris Agreement. We chose climate scenarios with a range of ±0.2°C from +1.5°C or +2.7°C. 

The warming levels are defined as the 2071–2100 global mean temperature difference relative to 1850–1900, with an added +0.69°C warming between 1850–1900 and 1986–2005 (ref. [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/)).  


### Definition of a glacier being 'mostly gone'
We define 'mostly gone' as the year when either less than 10% of the glacier's 2020 volume or less than 0.01 km³ is expected to remain - whichever threshold is crossed first. While small ice patches might persist beyond this year, the landscape will be very different compared to the current one. This 10%-threshold is considered appropriate for the Alps. Using both thresholds ensures we can define 'mostly gone' for both relatively large glaciers and those already very small today.

It is important to note that positive feedback mechanisms, such as localized warming due to glacier retreat, are not accounted for in large-scale glacier models. This means that, while the glacier changes we use here are the most reliable projections available, the actual glacier retreat may occur faster. 

##### Threshold definition differences
We find that our definition of a glacier being 'mostly gone' is, in the median, 9 years earlier in the Alps when using the two thresholds (<10% or <0.01 km³) compared to just using <10%. Compared to using only the <10% threshold, the maximum difference can mean a glacier is mostly gone 73 years earlier and that fewer glaciers survive until the end of the century.

Changing the definition from a 10% threshold to a 5% threshold results in glaciers being 'mostly gone', in the median, four years later, but this can be up to 34 years later.  For approximately 40 glaciers, the remaining glacier mass in 2100 is between 5% and 10%, meaning these glaciers would survive until the end of the century under the 5% threshold.



### Likely range

The **likely range** describes the spread of projections and is defined as the 17th to 83rd percentiles, consistent with [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/).  
If the data follow a Gaussian distribution, this range corresponds approximately to **one standard deviation** (±1σ) from the mean, capturing about 68% of the available projections.

## Glacier projection data sources and models

The **2020 glacier volume**, **year where we estimate the glacier to be mostly gone**, and **global and regional glacier volume change projections** are derived from these three glacier models (specific model versions and data further summarized in [Zekollari et al. (2024)](https://doi.org/10.5194/tc-18-5045-2024)) by simulating each of the >200,000 glaciers individually:
- **OGGM v1.6.1**  
  - **Data:** [DOI](https://doi.org/10.5281/zenodo.8286064)  
  - **Documentation:** [OGGM](https://oggm.org/)  
  - **Details:**  
    - CMIP5 and CMIP6 available.  
    - Includes less-used climate models and overshoot emission scenarios.  
    - For +2.7±0.2°C: n=14 climate scenarios 
    - For +1.5±0.2°C: n=11 climate scenarios 
- **PyGEM-OGGM**  
  - **Data:** [DOI](https://doi.org/10.5067/P8BN9VO9N5C7)  
  - **Documentation:** [PyGEM](https://pygem.readthedocs.io/en/latest/introduction.html)  
  - **Details:**  
    - CMIP5 and CMIP6 available.  
    - Same scenarios as presented in [Rounce et al., 2023](https://doi.org/10.1126/science.abo1324).  
    - For +2.7±0.2°C: n=7 climate scenarios  
    - For +1.5±0.2°C: n=9 climate scenarios 
- **GloGEM**  
  - **Data:** [DOI](https://doi.org/10.5281/zenodo.10908277)  
  - **Documentation:** [Huss & Hock (2015)](https://doi.org/10.3389/feart.2015.00054)  
  - **Details:**  
    - CMIP6 only.  
    - For +2.7±0.2°C: n=3 climate scenarios  
    - For +1.5±0.2°C: n=4 climate scenarios 

The **3D glacier thickness projections** are based solely on OGGM simulations and visualized using the [Glacier:3D-Viz](https://glacier3dviz.oggm.org/tutorials/welcome.html) tool. These 3D projections differ slightly from the other estimates, which are based on a combination of three glacier models.  

Note that these glacier projections are based on global glacier models that use globally available glacier observation data and not use data that is only available for a few glaciers (i.e., only geodetic but no in-situ observations directly used). As a result, the models perform better on a global scale than at the individual glacier scale. Although some important processes at the individual glacier scale are not represented, we present individual glacier results here for educational purposes. In addition, the per-glacier and regional volume in 2020 is not an observed volume but a modelled volume (it is the glacier model median estimate of the multi-climate-model medians). 

## Results aggregation

For the **2020 glacier volume**, **deglaciation year**, and **regional glacier volume change projections**, we present the **median** and the **likely range** across all available combinations of glacier models and climate scenarios. Since OGGM includes more climate scenarios, its projections contribute the most weight to the overall results.  

The mean global warming above pre-industrial across all combinations of glacier models and climate scenarios is:  
- **+1.57°C** for the **+1.5±0.2°C** range.  
- **+2.71°C** for the **+2.7±0.2°C** range.  


## Photo sources and licenses
<ul>
  {% for photo in site.photos %}
    <li id="{{ photo.photo_id }}">
      <a href="{{ site.baseurl }}{{ photo.filename }}">
        <img src="{{ site.baseurl }}{{ photo.filename }}" alt="{{ photo.photo_id }}" style="width: 100px; height: auto;">
      </a>
      {% if photo.photographer_name %}
        <br><b>Photographer</b>: {{ photo.photographer_name }}
      {% endif %}
      {% if photo.photo_date %}
        <br><b>Date</b>: {{ photo.photo_date }}
      {% endif %}
      {% if photo.photo_link %}
        <br><b>Original URL</b>: <a href="{{ photo.photo_link }}">{{ photo.photo_link }}</a>
      {% endif %}
      {% if photo.citation %}
        <br><b>Citation</b>: {{ photo.citation }}
      {% endif %}
      {% if photo.photo_license %}
        <br><b>License</b>: <a href="{{ photo.photo_license_url }}">{{ photo.photo_license }}</a>
      {% endif %}
    </li>
  {% endfor %}
 </ul>
