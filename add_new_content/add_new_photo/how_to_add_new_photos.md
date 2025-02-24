# How to add a new photo

1. Downsize photo to a maximum size of 500kb using `downsize_glacier_photos.ipynb` (for a fast responding website)
2. Save the new photo in `assets/images/photos_glaciers` for a glacier photo or in `assets/images/photos_signposts` for a signpost photo
3. Create/adapt yml file for photo:
    - **Glacier photo**:
        - If adding a new glacier, copy and adapt `template_glacier_photos.yml`, and save it as `{RGI_ID}_photos.yml` in the `glacier_photos_yml_files` directory.
        - If adding a photo to an existing glacier, add the photo information to the existing `{RGI_ID}_photos.yml` file.
    - **Signpost photo**:
        - If adding a new signpost, copy and adapt `template_signpost_photos.yml`, and save it as `{SIGNPOST_NAME}_photos.yml` in the `signpost_photos_yml_files` directory.
        - If adding a photo to an existing signpost, add the photo information to the existing `{SIGNPOST_NAME}_photos.yml` file.
    - Add the photo license link to `list_of_photo_licenses.yml`, if not already included
4. Run the script [`update_website_with_new_content.py`](../update_website_with_new_content.py) or notebook [`update_website_with_new_content.ipynb`](../update_website_with_new_content.ipynb) to update the website with the new content.