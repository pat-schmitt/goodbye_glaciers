# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import os
import pandas as pd
import yaml

# # Define all filepaths

# ## filepaths for opening input data for creation of md

# +
# go up until we are in the project base directory
base_dir = os.getcwd()
while base_dir.split('/')[-1] != 'goodbye_glaciers':
    base_dir = os.path.normpath(os.path.join(base_dir, '..'))

fp_glacier_photos_yml = os.path.join(base_dir, 'add_new_content', 'add_new_photo', 'glacier_photos_yml_files')
fp_signpost_photos_yml = os.path.join(base_dir, 'add_new_content', 'add_new_photo', 'signpost_photos_yml_files')
fp_photo_licenses_yml = os.path.join(base_dir, 'add_new_content', 'add_new_photo', 'list_of_photo_licenses.yml')


# -

def get_all_photo_yml(fp):
    return [file for file in os.listdir(fp)
            if file.split('.')[-1] == 'yml']


def read_yml(fp):
    with open(fp) as stream:
        yml_content = yaml.safe_load(stream)
    return yml_content


def check_file_exist(fp, photo_id):
    fp_total = f"{base_dir}{fp}"
    if not os.path.exists(fp_total):
        print(f'{photo_id}: {fp} does not exist!')


# ## filepaths used when deploying the website

fp_glacier_photos = '/assets/images/photos_glaciers/'
fp_signpost_photos = '/assets/images/photos_signposts/'
fp_photo_md = os.path.join(base_dir, '_photos')

# # Open data needed by all

photo_licenses = read_yml(fp_photo_licenses_yml)


# # Function creating glacier markdown sites

def create_photo_markdown(fp_photo_yml, fp_photo):

    photo_yml_dict = read_yml(fp_photo_yml)

    # define photo_id prefix
    if 'rgi_id' in photo_yml_dict:
        photo_id_prefix = photo_yml_dict['rgi_id']
    elif 'signpost_id' in photo_yml_dict:
        photo_id_prefix = photo_yml_dict['signpost_id']
    else:
        raise ValueError('Need to provide rgi_id or signpost_id!')

    # loop through all photos and create markdown
    for photo in photo_yml_dict:
        if photo in ['rgi_id', 'signpost_id']:
            continue

        photo_id = f"{photo_id_prefix}_{photo}"
        photo_settings = photo_yml_dict[photo]

        # start creating markdown
        markdown_content = "---\n"
        markdown_content += f"photo_id: {photo_id}\n"

        for setting in photo_settings:
            if setting == 'filename':
                check_file_exist(f"{fp_photo}{photo_settings[setting]}",
                                 photo_id)
                markdown_content += f"{setting}: {fp_photo}{photo_settings[setting]}\n"
            elif setting == 'photo_license' and photo_settings[setting]:
                markdown_content += f'{setting}: "{photo_settings[setting]}"\n'
                markdown_content += f'photo_license_url: "{photo_licenses[photo_settings[setting]]}"\n'
            # ignore blank lines
            elif photo_settings[setting]:
                markdown_content += f'{setting}: "{photo_settings[setting]}"\n'

        # end file
        markdown_content += "---\n"

        # save markdown file
        with open(os.path.join(fp_photo_md, f"{photo_id}.md"), 'w') as file:
            file.write(markdown_content)
    
        print(f"Markdown file {photo_id} created.")


# # Run all

def create_all_photo_md():
    # glacier photos
    print('Glacier photos:')
    for photo_yml in get_all_photo_yml(fp_glacier_photos_yml):
        try:
            fp_photo_yml = os.path.join(fp_glacier_photos_yml, photo_yml)
            create_photo_markdown(fp_photo_yml,
                                  fp_photo=fp_glacier_photos)
        except Exception as error:
            print(f"{photo_yml} not working, error: {error}")
    
    # signpost photos
    print('\nSignpost photos:')
    for photo_yml in get_all_photo_yml(fp_signpost_photos_yml):
        try:
            fp_photo_yml = os.path.join(fp_signpost_photos_yml, photo_yml)
            create_photo_markdown(fp_photo_yml,
                                  fp_photo=fp_signpost_photos)
        except Exception as error:
            print(f"{photo_yml} not working, error: {error}")


if __name__ == '__main__':
    create_all_photo_md()


