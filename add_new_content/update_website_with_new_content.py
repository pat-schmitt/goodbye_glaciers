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

from add_new_glacier.create_glacier_md import create_all_glacier_md
from add_new_signpost.create_signpost_md import create_all_signpost_md
from add_new_photo.create_photos_md import create_all_photo_md

# This notebook/script updates the website with new content.
#
# **It is important that the signposts are updated before the glaciers!**

# # Create photo markdowns

print('Creating photo markdowns')
create_all_photo_md()
print('\n\n')

# # Create signpost markdowns

print('Creating signpost markdowns')
create_all_signpost_md()
print('\n\n')

# # Create glacier markdowns

print('Creating glacier markdowns')
create_all_glacier_md()
print('\n\n')


