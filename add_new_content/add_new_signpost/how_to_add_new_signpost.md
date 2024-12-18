# How to add a new signpost

1. Add a photo of the signpost to serve as the title picture ([see how to add a photo](../add_new_photo/how_to_add_new_photos.md)).
2. Create a yml file for the signpost:
   - Copy `template_signpost.yml` and adapt it.
   - Save the file as `{SIGNPOST_ID}.yml` inside `add_new_content/add_new_signpost/signpost_yml_files`.
3. Run the script [`update_website_with_new_content.py`](../update_website_with_new_content.py) or notebook [`update_website_with_new_content.ipynb`](../update_website_with_new_content.ipynb) to update the website with the new content.
