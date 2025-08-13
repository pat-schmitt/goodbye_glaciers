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
import json

# # Define all filepaths

# ## filepaths for opening input data for creation of md

# +
# go up until we are in the project base directory
base_dir = os.getcwd()
while base_dir.split('/')[-1] != 'goodbye_glaciers':
    base_dir = os.path.normpath(os.path.join(base_dir, '..'))

fp_glacier_yml = os.path.join(base_dir, 'add_new_content', 'add_new_glacier', 'glacier_yml_files')
fp_photo_yml = os.path.join(base_dir, 'add_new_content', 'add_new_photo', 'glacier_photos_yml_files')
deglac_csv_file = 'https://cluster.klima.uni-bremen.de/~pschmitt/goodby_glaciers/website/data_plots_for_website/deglaciation_csv/rgi_{}_glacier_data_deglaciation.csv'
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

animation_source = 'fileshare'  # 'local', 'fileshare'

# +
fp_glacier_volume = '/assets/images/volume_evolution_glaciers/'
fp_glacier_animations = '/assets/videos/glacier_animations/'
fp_glacier_photos = '/assets/images/photos_glaciers/'
fp_glacier_md = os.path.join(base_dir, '_glaciers')
fp_glacier_list = '/assets/glaciers.json'

fp_glacier_animations_fileshare = 'https://fileshare.uibk.ac.at/d/b1c8bdcb065c4ee5bf3e/files/?p=%2F'
# -

# # Function creating glacier markdown sites

# container to avoid multiple opening
df_deglac_all = {}


def create_glacier_markdown(glacier_yml, glacier_location_list):

    rgi_id = glacier_yml.replace('.yml', '')

    rgi_reg = rgi_id.split('-')[1].split('.')[0]
    if rgi_reg not in df_deglac_all:
        df_deglac_all[rgi_reg] = pd.read_csv(deglac_csv_file.format(rgi_reg)).set_index('rgi_id')
    df_deglac = df_deglac_all[rgi_reg]

    # start creating markdown
    markdown_content = "---\n"
    markdown_content += f"rgi_id: {rgi_id}\n"

    # add data from yml
    glacier_yml_dict = read_yml(os.path.join(fp_glacier_yml, glacier_yml))
    assert glacier_yml_dict['rgi_id'] == rgi_id, 'rgi_id check glacier yml file'
    markdown_content += f"title: {glacier_yml_dict['name']}\n"
    
    if glacier_yml_dict['country'] == 'Switzerland':
        glacier_yml_dict['country_de'] = 'Schweiz'
        glacier_yml_dict['country_it'] = 'Svizzera'
        glacier_yml_dict['country_fr'] = 'Suisse'
    elif glacier_yml_dict['country'] == 'Italy':
        glacier_yml_dict['country_de'] = 'Italien'
        glacier_yml_dict['country_it'] = 'Italia'
        glacier_yml_dict['country_fr'] = 'Italie'
    elif glacier_yml_dict['country'] == 'France':
        glacier_yml_dict['country_de'] = 'Frankreich'
        glacier_yml_dict['country_it'] = 'Francia'
        glacier_yml_dict['country_fr'] = 'France'
    elif glacier_yml_dict['country'] == 'Austria':
        glacier_yml_dict['country_de'] = 'Österreich'
        glacier_yml_dict['country_it'] = 'Austria'
        glacier_yml_dict['country_fr'] = 'Autriche'
    elif glacier_yml_dict['country'] == 'Germany':
        glacier_yml_dict['country_de'] = 'Deutschland'
        glacier_yml_dict['country_it'] = 'Germania'
        glacier_yml_dict['country_fr'] = 'Allemagne'
    elif glacier_yml_dict['country'] == 'Sweden':
        glacier_yml_dict['country_de'] = 'Schweden'
        glacier_yml_dict['country_it'] = 'Svezia'
        glacier_yml_dict['country_fr'] = 'Suède'
    elif glacier_yml_dict['country'] == 'Kyrgyzstan':
        glacier_yml_dict['country_de'] = 'Kirgisistan'
        glacier_yml_dict['country_it'] = 'Kirghizistan'
        glacier_yml_dict['country_fr'] = 'Kirghizistan'
    elif glacier_yml_dict['country'] == 'Canada':
        glacier_yml_dict['country_de'] = 'Kanada'
        glacier_yml_dict['country_it'] = 'Canada'
        glacier_yml_dict['country_fr'] = 'Canada'
    elif glacier_yml_dict['country'] == 'USA':
        glacier_yml_dict['country_de'] = 'USA'
        glacier_yml_dict['country_it'] = 'Stati Uniti'
        glacier_yml_dict['country_fr'] = 'États-Unis'
    elif glacier_yml_dict['country'] == 'Chile':
        glacier_yml_dict['country_de'] = 'Chile'
        glacier_yml_dict['country_it'] = 'Cile'
        glacier_yml_dict['country_fr'] = 'Chili'
    elif glacier_yml_dict['country'] == 'New Zealand':
        glacier_yml_dict['country_de'] = 'Neuseeland'
        glacier_yml_dict['country_it'] = 'Nuova Zelanda'
        glacier_yml_dict['country_fr'] = 'Nouvelle-Zélande'
    
    markdown_content += f"country: {glacier_yml_dict['country']}\n"
    markdown_content += f"country_de: {glacier_yml_dict['country_de']}\n"
    markdown_content += f"country_it: {glacier_yml_dict['country_it']}\n"
    markdown_content += f"country_fr: {glacier_yml_dict['country_fr']}\n"

    # add data from csv
    try:
        rgi_id_csv = df_deglac.loc[rgi_id].copy()
    except KeyError:
        raise KeyError(f'{rgi_id} not included in glacier_data_deglaciation.csv!')
    for csv_var in ['Lon', 'Lat', 'vol2020_km3',
                    'deglac_yr_2.7deg_10perc_e-2km3_q50',
                    'deglac_yr_2.7deg_10perc_e-2km3_q17',
                    'deglac_yr_2.7deg_10perc_e-2km3_q83',
                    'deglac_yr_1.5deg_10perc_e-2km3_q50',
                    'deglac_yr_1.5deg_10perc_e-2km3_q17',
                    'deglac_yr_1.5deg_10perc_e-2km3_q83',
                    '2100_perc_2.7deg_q17',
                    '2100_perc_2.7deg_q83',
                    '2100_perc_2.7deg_q50',
                    '2100_perc_1.5deg_q50',
                    '2100_perc_1.5deg_q17',
                    '2100_perc_1.5deg_q83']:
        if csv_var == 'vol2020_km3':
            rgi_id_csv[csv_var] = rgi_id_csv[csv_var].round(2)
        if csv_var in ['Lon', 'Lat']:
            markdown_content += f"{csv_var.replace('.', '_')}: {rgi_id_csv[f'{csv_var}']}\n"
        else:
            markdown_content += f"{csv_var.replace('.', '_')}: {rgi_id_csv[csv_var]}\n"

    # add volume evolution curves
    fp_file = f"{fp_glacier_volume}{rgi_id}_simple_en.png"
    check_file_exist(fp_file, rgi_id)
    markdown_content += f"volume_evolution_simple: {fp_file}\n"
    fp_file = f"{fp_glacier_volume}{rgi_id}_complex_en.png"
    check_file_exist(fp_file, rgi_id)
    markdown_content += f"volume_evolution_complex: {fp_file}\n"

    # add 3d animations
    if animation_source == 'fileshare':
        fp_file = f"{fp_glacier_animations_fileshare}{rgi_id}_%2B1.5%C2%B0C.mp4&dl=1"
        markdown_content += f"animation_15: {fp_file}\n"
        fp_file = f"{fp_glacier_animations_fileshare}{rgi_id}_%2B2.7%C2%B0C.mp4&dl=1"
        markdown_content += f"animation_27: {fp_file}\n"
        fp_file = f"{fp_glacier_animations_fileshare}{rgi_id}_both.mp4&dl=1"
        markdown_content += f"animation_both: {fp_file}\n"
    elif animation_source == 'local':
        fp_file = f"{fp_glacier_animations}{rgi_id}_+1.5°C.mp4"
        check_file_exist(fp_file, rgi_id)
        markdown_content += f"animation_15: {fp_file}\n"
        fp_file = f"{fp_glacier_animations}{rgi_id}_+2.7°C.mp4"
        check_file_exist(fp_file, rgi_id)
        markdown_content += f"animation_27: {fp_file}\n"
        fp_file = f"{fp_glacier_animations}{rgi_id}_both.mp4"
        check_file_exist(fp_file, rgi_id)
        markdown_content += f"animation_both: {fp_file}\n"

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
    markdown_content += ("{% case site.lang %}"
                         '{% when "de" %}'
                         "{% include glacier_heading_de %}"
                         '{% when "it" %}'
                         "{% include glacier_heading_it %}"
                         '{% when "fr" %}'
                         "{% include glacier_heading_fr %}"
                         '{% else %}'
                         "{% include glacier_heading_en %}"
                         '{% endcase %}'
                        )

    # save markdown file
    with open(os.path.join(fp_glacier_md, f"{rgi_id}.md"), 'w') as file:
            file.write(markdown_content)
    
    print(f"Markdown file {rgi_id} created.")

    # add glacier to glacier list for compass functionality
    glacier_location_list.append(
        {
            'name': glacier_yml_dict['name'],
            'latitude': rgi_id_csv['Lat'],
            'longitude': rgi_id_csv['Lon'],
        }
    )


# # Run all

def create_all_glacier_md():
    # clear folder before starting
    for file in os.listdir(fp_glacier_md):
        file_path = os.path.join(fp_glacier_md, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    glacier_location_list = []
    for glacier_yml in get_all_glacier_yml():
        try:
            create_glacier_markdown(glacier_yml, glacier_location_list)
        except Exception as error:
            print(f"{glacier_yml} not working, error: {error}")
    with open(f"{base_dir}{fp_glacier_list}", 'w') as file:
        json.dump(glacier_location_list, file)


if __name__ == '__main__':
    create_all_glacier_md()

do_debugging = False

if do_debugging:
    for file in os.listdir(fp_glacier_md):
        file_path = os.path.join(fp_glacier_md, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
    
    glacier_location_list = []
    #for glacier_yml in get_all_glacier_yml()

if do_debugging:
    print(get_all_glacier_yml())

if do_debugging:
    create_glacier_markdown(get_all_glacier_yml()[-2], glacier_location_list)


