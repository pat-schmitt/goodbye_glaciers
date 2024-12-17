# How to add a new signpost

1. Add a photo of the signpost to serve as the title picture ([see how to add a photo](../add_new_photo/how_to_add_new_photos.md)).
2. Create a yml file for the signpost:
   - Copy `template_signpost.yml` and adapt it.
   - Save the file as `{SIGNPOST_ID}.yml` inside `add_new_content/add_new_signpost/signpost_yml_files`.
3. Run the script [`create_signpost_md.py`](create_signpost_md.py) or notebook [`create_signpost_md.ipynb`](create_signpost_md.ipynb) to generate individual signpost markdown pages:
   - The script or notebook will create markdown pages only for signposts where all required information is available.
4. Run the script [`create_glacier_md.py`](../add_new_glacier/create_glacier_md.py) to link the signpost to the corresponding glaciers.