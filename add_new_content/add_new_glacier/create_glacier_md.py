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
#     display_name: Python [conda env:oggm_env]
#     language: python
#     name: conda-env-oggm_env-py
# ---

import os
import pandas as pd
import yaml


# # check if notebook or script

# +
# Function to detect if we're running in a Jupyter notebook
def check_if_notebook():
    try:
        shell_name = get_ipython().__class__.__name__
        if shell_name == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or JupyterLab
        elif shell_name in ['TerminalInteractiveShell', 'InteractiveShell']:
            return False  # IPython terminal or other interactive shells
        else:
            # Fallback or default behavior for unidentified environments
            return False
    except NameError:
        return False      # Not in IPython, likely standard Python interpreter

# Use this to conditionally execute tests/debugging
if check_if_notebook():
    is_notebook = True
else:
    is_notebook = False
# -

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


# -

def get_all_glacier_yml(fp=fp_glacier_yml):
    return [file for file in os.listdir(fp)
            if file.split('.')[-1] == 'yml']


def read_yml(fp):
    with open(fp) as stream:
        yml_content = yaml.safe_load(stream)
    return yml_content


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
    markdown_content += f"volume_evolution_simple: {fp_glacier_volume}{rgi_id}_simple_en.png\n"
    markdown_content += f"volume_evolution_complex: {fp_glacier_volume}{rgi_id}_complex_en.png\n"

    # add 3d animations
    markdown_content += f"animation_simple: {fp_glacier_animations}{rgi_id}_simple_en.mp4\n"
    markdown_content += f"animation_complex: {fp_glacier_animations}{rgi_id}_complex_en.mp4\n"

    # add photos
    photo_yml_dict = read_yml(os.path.join(fp_photo_yml, f'{rgi_id}_photos.yml'))
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
    filename_main_photo = f"{fp_glacier_photos}{photo_yml_dict[main_photo]['filename']}"
    main_photo_credit = (f"Photo credit: {photo_yml_dict[main_photo]['photographer_name']}, "
                         f"{photo_yml_dict[main_photo]['photo_date']}")
    markdown_content += f"main_photo: {filename_main_photo}\n"
    markdown_content += "header:\n"
    markdown_content += f"  overlay_image: {filename_main_photo}\n"
    markdown_content += f"  teaser: {filename_main_photo}\n"
    markdown_content += f'  caption: "{main_photo_credit}"\n'

    # end file
    markdown_content += "---\n"

    # add contant what is visible below the heading
    markdown_content += "Country: {{ page.country }}  <br>Mostly gone by {{ page.deglac_yr_2_7deg_10perc_q50 | floor }}\n"

    # save markdown file
    with open(os.path.join(fp_glacier_md, f"{rgi_id}.md"), 'w') as file:
        file.write(markdown_content)
    
    print(f"Markdown file {rgi_id} created.")


# # Test for notebook

if is_notebook:
    glacier_yml = get_all_glacier_yml()[0]

    create_glacier_markdown(glacier_yml)

# # Run all

for glacier_yml in get_all_glacier_yml():
    try:
        create_glacier_markdown(glacier_yml)
    except Exception as error:
        print(f"{glacier_yml} not working, error: {error}")

