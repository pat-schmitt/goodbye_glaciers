---
permalink: /methods/
title: Methods
---
# !!!Work in Progress!!!

# Methods

This page describes the methodology used for estimating the deglaciation year and the glacier projection visualizations.

## Overview

We simulate individual glacier thickness and volume projections from 2000 to 2100 using climate scenarios (climate models and emission scenarios) from CMIP5 and CMIP6 and large-scale glacier models. We primarily focus on **+2.7°C** global warming above pre-industrial by 2100, as this represents the predicted real-world outcome of [current policies and actions](https://climateactiontracker.org/global/cat-thermometer/). For comparison, we also include projections under the **+1.5°C target** of the Paris Agreement. We chose climate scenarios with a range of ±0.2°C from +1.5°C or +2.7°C. 

The warming levels are defined as the 2071–2100 global mean temperature difference relative to 1850–1900, with an added +0.69°C warming between 1850–1900 and 1986–2005 (ref. [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/)).  


### Deglaciation year definition

The **deglaciation year** is defined as the point when less than 10% of a glacier's 2020 volume is expected to remain. While small ice patches might persist beyond this year, the landscape will be very different compared to the current one. This 10%-threshold is considered appropriate for the Alps.  

It is important to note that positive feedback mechanisms, such as localized warming due to glacier retreat, are not accounted for in large-scale glacier models.   

### Likely range

The **likely range** describes the spread of projections and is defined as the 17th to 83rd percentiles, consistent with [IPCC AR6](https://www.ipcc.ch/report/ar6/wg1/).  
If the data follow a Gaussian distribution, this range corresponds approximately to **one standard deviation** (±1σ) from the mean, capturing about 68% of the available projections.

## Glacier projection data sources and models

The **2020 glacier volume**, **deglaciation year**, and **global and regional glacier volume change projections** are derived from these three glacier models (specific model versions and data further summarized in [Zekollari et al. (2024)](https://doi.org/10.5194/tc-18-5045-2024)) by simulating each of the >200,000 glaciers individually:
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


## Results aggregation

For the **2020 glacier volume**, **deglaciation year**, and **regional glacier volume change projections**, we present the **median** and the **likely range** across all available combinations of glacier models and climate scenarios. Since OGGM includes more climate scenarios, its projections contribute the most weight to the overall results.  

The mean global warming above pre-industrial across all combinations of glacier models and climate scenarios is:  
- **+1.57°C** for the **+1.5±0.2°C** range.  
- **+2.71°C** for the **+2.7±0.2°C** range.  


## Photo sources and licenses
Link to all used photos on the website and their corresponding licenses -> TODO
