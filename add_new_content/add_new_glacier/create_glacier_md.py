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

fp_glacier_yml = os.path.join(base_dir, 'add_new_content', 'add_new_glacier', 'glacier_yml_files')
fp_photo_yml = os.path.join(base_dir, 'add_new_content', 'add_new_photo', 'glacier_photos_yml_files')
deglac_csv_file = os.path.join(base_dir, 'add_new_content', 'add_new_glacier', 'glacier_data_deglaciation.csv')
fp_signpost_yml = os.path.join(base_dir, 'add_new_content', 'add_new_signpost', 'signpost_yml_files')


# -

def get_all_glacier_yml(fp=fp_glacier_yml):
    return [file for file in os.listdir(fp)
            if file.split('.')[-1] == 'yml']


def read_yml(fp):
    with open(fp) as stream:
        yml_content = yaml.safe_load(stream)
    return yml_content


def check_file_exist(fp, rgi_id):
    fp_total = f"{base_dir}{fp}"
    if not os.path.exists(fp_total):
        print(f'{rgi_id}: {fp} does not exist!')


# ## filepaths used when deploying the website

fp_glacier_volume = '/assets/images/volume_evolution_glaciers/'
fp_glacier_animations = '/assets/videos/glacier_animations/'
fp_glacier_photos = '/assets/images/photos_glaciers/'
fp_glacier_md = os.path.join(base_dir, '_glaciers')

# # Open data needed by all

df_deglac = pd.read_csv(deglac_csv_file, index_col=0)


# # Function creating glacier markdown sites

def create_glacier_markdown(glacier_yml):

    rgi_id = glacier_yml.replace('.yml', '')

    # start creating markdown
    markdown_content = "---\n"
    markdown_content += f"rgi_id: {rgi_id}\n"

    # add data from yml
    glacier_yml_dict = read_yml(os.path.join(fp_glacier_yml, glacier_yml))
    assert glacier_yml_dict['rgi_id'] == rgi_id, 'rgi_id check glacier yml file'
    markdown_content += f"title: {glacier_yml_dict['name']}\n"
    markdown_content += f"country: {glacier_yml_dict['country']}\n"

    # add data from csv
    try:
        rgi_id_csv = df_deglac.loc[rgi_id]
    except KeyError:
        raise KeyError(f'{rgi_id} not included in glacier_data_deglaciation.csv!')
    for csv_var in ['CenLon', 'CenLat', 'vol2020_km3',
                    'deglac_yr_2.7deg_10perc_q50',
                    'deglac_yr_2.7deg_10perc_q17',
                    'deglac_yr_2.7deg_10perc_q83',
                    'deglac_yr_1.5deg_10perc_q50',
                    'deglac_yr_1.5deg_10perc_q17',
                    'deglac_yr_1.5deg_10perc_q83']:
        markdown_content += f"{csv_var.replace('.', '_')}: {rgi_id_csv[csv_var]}\n"

    # add volume evolution curves
    fp_file = f"{fp_glacier_volume}{rgi_id}_simple_en.png"
    check_file_exist(fp_file, rgi_id)
    markdown_content += f"volume_evolution_simple: {fp_file}\n"
    fp_file = f"{fp_glacier_volume}{rgi_id}_complex_en.png"
    check_file_exist(fp_file, rgi_id)
    markdown_content += f"volume_evolution_complex: {fp_file}\n"

    # add 3d animations
    fp_file = f"{fp_glacier_animations}{rgi_id}_simple_en.mp4"
    check_file_exist(fp_file, rgi_id)
    markdown_content += f"animation_simple: {fp_file}\n"
    fp_file = f"{fp_glacier_animations}{rgi_id}_complex_en.mp4"
    check_file_exist(fp_file, rgi_id)
    markdown_content += f"animation_complex: {fp_file}\n"

    # add photos
    photo_yml_dict = read_yml(os.path.join(fp_photo_yml, f'{rgi_id}_photos.yml'))
    markdown_content += f"gallery:\n"
    # find main photo
    main_photo = None
    for photo in photo_yml_dict:
        if photo == 'rgi_id':
            assert photo_yml_dict['rgi_id'] == rgi_id, 'rgi_id check photo yml file'
            continue
        elif photo_yml_dict[photo]['is_main_photo']:
            if main_photo is not None:
                raise ValueError(f"Main photo already defined as {main_photo}, "
                                 f"but {photo} also wants to become main photo!")
            main_photo = photo

        # add photo to gallery
        image_path = f"{fp_glacier_photos}{photo_yml_dict[photo]['filename']}"
        check_file_exist(image_path, rgi_id)
        markdown_content += f"  - url: {image_path}\n"
        markdown_content += f"    image_path: {image_path}\n"
        photo_credit = ("Photo credit: "
                        f'<a href="/methods/#{rgi_id}_{main_photo}">'
                        f"{photo_yml_dict[photo]['photographer_name']}, "
                        f"{photo_yml_dict[photo]['photo_date']}"
                        '</a>'
                       )
        markdown_content += (f"    alt: "
                             f"{photo_yml_dict[photo]['photographer_name']}, "
                             f"{photo_yml_dict[photo]['photo_date']}\n"
                            )
        markdown_content += f"    title: '{photo_credit}'\n"

    filename_main_photo = f"{fp_glacier_photos}{photo_yml_dict[main_photo]['filename']}"
    main_photo_credit = (f"Photo credit: "
                         f'<a href="/methods/#{rgi_id}_{main_photo}">'
                         f"{photo_yml_dict[main_photo]['photographer_name']}, "
                         f"{photo_yml_dict[main_photo]['photo_date']}"
                         '</a>'
                        )
    markdown_content += f"main_photo: {filename_main_photo}\n"
    markdown_content += "header:\n"
    markdown_content += f"  overlay_image: {filename_main_photo}\n"
    markdown_content += f"  teaser: {filename_main_photo}\n"
    markdown_content += f"  caption: '{main_photo_credit}'\n"

    # add signposts to glacier
    all_signpost_yml_files = get_all_glacier_yml(fp=fp_signpost_yml)
    featured_signposts = None
    for signpost_file in all_signpost_yml_files:
        signpost_yml_dict = read_yml(os.path.join(fp_signpost_yml, signpost_file))
    
        if rgi_id in signpost_yml_dict['glaciers']:
            if featured_signposts is None:
                featured_signposts = [signpost_yml_dict['signpost_id']]
            else:
                featured_signposts.append(signpost_yml_dict['signpost_id'])
    if featured_signposts:
        markdown_content += f"signposts: {featured_signposts}\n"

    # end file
    markdown_content += "---\n"

    # add contant what is visible below the heading
    markdown_content += ("Country: {{ page.country }}  <br>"
                         "+2.7°C: Mostly gone by {{ page.deglac_yr_2_7deg_10perc_q50 | floor }} <br>"
                         "+1.5°C: Mostly gone by  X2 <br>"
                         "<b>Every 0.1°C avoided saves glaciers and limits impacts!</b>"
                        )

    # save markdown file
    with open(os.path.join(fp_glacier_md, f"{rgi_id}.md"), 'w') as file:
        file.write(markdown_content)
    
    print(f"Markdown file {rgi_id} created.")


# # Run all

def create_all_glacier_md():
    for glacier_yml in get_all_glacier_yml():
        try:
            create_glacier_markdown(glacier_yml)
        except Exception as error:
            print(f"{glacier_yml} not working, error: {error}")


if __name__ == '__main__':
    create_all_glacier_md()


