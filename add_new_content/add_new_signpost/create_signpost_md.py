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

import yaml
import os

# # Define all filepaths

# ## filepaths for opening input data for creation of md

# +
# go up until we are in the project base directory
base_dir = os.getcwd()
while base_dir.split('/')[-1] != 'goodbye_glaciers':
    base_dir = os.path.normpath(os.path.join(base_dir, '..'))

fp_signpost_yml = os.path.join(base_dir, 'add_new_content', 'add_new_signpost', 'signpost_yml_files')
fp_photo_yml = os.path.join(base_dir, 'add_new_content', 'add_new_photo', 'signpost_photos_yml_files')


# -

def get_all_signpost_yml(fp=fp_signpost_yml):
    return [file for file in os.listdir(fp)
            if file.split('.')[-1] == 'yml']


def read_yml(fp):
    with open(fp) as stream:
        yml_content = yaml.safe_load(stream)
    return yml_content


def check_file_exist(fp, signpost_id):
    fp_total = f"{base_dir}{fp}"
    if not os.path.exists(fp_total):
        print(f'{signpost_id}: {fp} does not exist!')


# ## filepaths used when deploying the website

fp_signpost_photos = '/assets/images/photos_signposts/'
fp_signpost_md = os.path.join(base_dir, '_signposts')


# # Function creating signpost markdown sites
def create_signpost_markdown(signpost_yml):

    # start creating markdown
    markdown_content = "---\n"

    # add data from yml
    signpost_yml_dict = read_yml(os.path.join(fp_signpost_yml, signpost_yml))
    signpost_id = signpost_yml_dict['signpost_id']
    markdown_content += f"signpost_id: {signpost_id}\n"
    markdown_content += f"title: {signpost_yml_dict['title']}\n"
    markdown_content += f"Lat: {signpost_yml_dict['current_location'][0]}\n"
    markdown_content += f"Lon: {signpost_yml_dict['current_location'][1]}\n"
    markdown_content += f"location_description: {signpost_yml_dict['current_location_description']}\n"
    
    if signpost_yml_dict['current_country'] == 'Switzerland':
        signpost_yml_dict['country_de'] = 'Schweiz'
        signpost_yml_dict['country_it'] = 'Svizzera'
        signpost_yml_dict['country_fr'] = 'Suisse'
    elif signpost_yml_dict['current_country'] == 'Italy':
        signpost_yml_dict['country_de'] = 'Italien'
        signpost_yml_dict['country_it'] = 'Italia'
        signpost_yml_dict['country_fr'] = 'Italie'
    elif signpost_yml_dict['current_country'] == 'France':
        signpost_yml_dict['country_de'] = 'Frankreich'
        signpost_yml_dict['country_it'] = 'Francia'
        signpost_yml_dict['country_fr'] = 'France'
    elif signpost_yml_dict['current_country'] == 'Austria':
        signpost_yml_dict['country_de'] = 'Österreich'
        signpost_yml_dict['country_it'] = 'Austria'
        signpost_yml_dict['country_fr'] = 'Autriche'
    markdown_content += f"country: {signpost_yml_dict['current_country']}\n"
    markdown_content += f"country_de: {signpost_yml_dict['country_de']}\n"
    markdown_content += f"country_it: {signpost_yml_dict['country_it']}\n"
    markdown_content += f"country_fr: {signpost_yml_dict['country_fr']}\n"
    
    markdown_content += f"description: {signpost_yml_dict['description']}\n"
    markdown_content += f"past_locations: {signpost_yml_dict['past_locations']}\n"
    markdown_content += f"glaciers: {signpost_yml_dict['glaciers']}\n"

    # add photos
    photo_yml_dict = read_yml(os.path.join(fp_photo_yml, f'{signpost_id}_photos.yml'))
    markdown_content += f"gallery:\n"
    # find main photo
    main_photo = None
    for photo in photo_yml_dict:
        if photo == 'signpost_id':
            assert photo_yml_dict['signpost_id'] == signpost_id, 'signpost_id check photo yml file'
            continue
        elif photo_yml_dict[photo]['is_main_photo']:
            if main_photo is not None:
                raise ValueError(f"Main photo already defined as {main_photo}, "
                                 f"but {photo} also wants to become main photo!")
            main_photo = photo

        # add photo to gallery
        image_path = f"{fp_signpost_photos}{photo_yml_dict[photo]['filename']}"
        check_file_exist(image_path, signpost_id)
        markdown_content += f"  - url: {image_path}\n"
        markdown_content += f"    image_path: {image_path}\n"
        photo_credit = (f"Photo credit: "
                        f'<a href="/methods/#{signpost_id}_{photo}">'
                        f"{photo_yml_dict[photo]['photographer_name']}, "
                        f"{photo_yml_dict[photo]['photo_date']}"
                        '</a>'
                       )
        markdown_content += (f"    alt: "
                             f"{photo_yml_dict[photo]['photographer_name']}, "
                             f"{photo_yml_dict[photo]['photo_date']}\n"
                            )
        markdown_content += f"    title: '{photo_yml_dict[photo]['photo_description']} {photo_credit}'\n"

    filename_main_photo = f"{fp_signpost_photos}{photo_yml_dict[main_photo]['filename']}"
    main_photo_credit = (f"Photo credit: "
                         f'<a href="/methods/#{signpost_id}_{main_photo}">'
                         f"{photo_yml_dict[main_photo]['photographer_name']}, "
                         f"{photo_yml_dict[main_photo]['photo_date']}"
                         '</a>'
                        )
    markdown_content += f"main_photo: {filename_main_photo}\n"
    markdown_content += "header:\n"
    markdown_content += f"  overlay_image: {filename_main_photo}\n"
    markdown_content += f"  teaser: {filename_main_photo}\n"
    markdown_content += f"  caption: '{main_photo_credit}'\n"

    # end file
    markdown_content += "---\n"

    # add contant what is visible below the heading
    markdown_content += ("{% case site.lang %}"
                         '{% when "de" %}'
                         "{% include signpost_heading_de %}"
                         '{% when "it" %}'
                         "{% include signpost_heading_it %}"
                         '{% when "fr" %}'
                         "{% include signpost_heading_fr %}"
                         '{% else %}'
                         "{% include signpost_heading_en %}"
                         '{% endcase %}'
                        )

    # save markdown file
    with open(os.path.join(fp_signpost_md, f"{signpost_id}.md"), 'w') as file:
        file.write(markdown_content)
    
    print(f"Markdown file {signpost_id} created.")



# # Run all

def create_all_signpost_md():
    for signpost_yml in get_all_signpost_yml():
        try:
            create_signpost_markdown(signpost_yml)
        except Exception as error:
            print(f"{signpost_yml} not working, error: {error}")


if __name__ == '__main__':
    create_all_signpost_md()


