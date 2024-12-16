# How to add a new glacier

1. Create volume evolution figures for all supported languages:
	- Showing +2.7°C: `{RGI_ID}_simple_{language}.png`
	- Showing +1.5°C and +2.7°C: `{RGI_ID}_complex_{language}.png`
	- Save the figures in `assets/images/volume_evolution_glaciers`
2. Add the new glacier to `glacier_data_deglaciation.csv`
	- Include the following columns: `rgi_id`, `CenLon`, `CenLat`, `vol2020_km3` and `deglac_yr_{1.5/2.7}deg_10perc_q{17/83/50}` (=6 columns for deglac_yr_...)
  	- Save file in `add_new_content/add_new_glacier`
3. Create 3D animations:
	- Showing +2.7°C: `{RGI_ID}_simple_{langauage}.mp4`
	- Showing +1.5°C and +2.7°C: `{RGI_ID}_complex_{language}.mp4`
  	- Save videos in `assets/videos/glacier_animations`
4. Add a photo of the glacier which serves as the title picture ([see how to add a photo](../add_new_photo/how_to_add_new_photos.md))
5. Create a yml file for glacier:
	- Copy `template_glacier.yml` and adapt it (update `rgi_id`, `name` and `country`)
	- Save as `{RGI_ID}.yml` inside  `add_new_content/add_new_glacier/glacier_yml_files`
6. Run the script `create_glacier_md.py` or notebook `create_glacier_md.ipynp` to generate individual glacier markdown pages:
	- The script or notebook will create markdown pages only for glaciers where all required information is available!
