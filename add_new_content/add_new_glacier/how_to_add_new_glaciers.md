# How to add a new glacier

1. Download volume evolution figures for all supported languages [here](https://cluster.klima.uni-bremen.de/~lschuster/glacier_deglaciation_year/figures/):
	- Showing +2.7°C: `{RGI_ID}_simple_{language}.png`
	- Showing +1.5°C and +2.7°C: `{RGI_ID}_complex_{language}.png`
	- Save the figures in `assets/images/volume_evolution_glaciers`
2. Create 3D animations:
	- Showing +2.7°C: `{RGI_ID}_simple_{langauage}.mp4`
	- Showing +1.5°C and +2.7°C: `{RGI_ID}_complex_{language}.mp4`
  	- Save videos to fileshare
3. Add a photo of the glacier which serves as the title picture ([see how to add a photo](../add_new_photo/how_to_add_new_photos.md))
4. Create a yml file for glacier:
	- Copy `template_glacier.yml` and adapt it (update `rgi_id`, `name` and `country`)
	- Save as `{RGI_ID}.yml` inside  `add_new_content/add_new_glacier/glacier_yml_files`
5. Run the script [`update_website_with_new_content.py`](../update_website_with_new_content.py) or notebook [`update_website_with_new_content.ipynb`](../update_website_with_new_content.ipynb) to update the website with the new content.
