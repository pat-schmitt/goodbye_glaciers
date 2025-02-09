# Goodbye Glaciers website

This repository contains the website [goodbye-glaciers.info](https://goodbye-glaciers.info). Powered by [Jekyll](https://jekyllrb.com/) and [Minimal Mistakes](https://mademistakes.com/work/jekyll-themes/minimal-mistakes/).

## Links to documentation for adding new content to website
- [add new glacier](/add_new_content/add_new_glacier/how_to_add_new_glaciers.md)
- [add new signpost](/add_new_content/add_new_signpost/how_to_add_new_signpost.md)
- [add new photo](/add_new_content/add_new_photo/how_to_add_new_photos.md)
- [create QR code for sign](/add_new_content/add_new_qr_code_for_sign/how_to_create_qr_codes_for_signs.md)

## Locations of translations
- main pages: `/_i18n/{language}`
- individual heading text (on top of images) for glaciers and signposts: `/_includes/glacier_heading_{language}` or `/_includes/signpost_heading_{language}`
- individual body text (below images) for glaciers and signposts: `/_includes/glaciers_{language}` or `/_includes/signposts_{language}`
- menu text: `/_data/navigation.yml`
- welcome page heading (text overlay of the image): `index.md`
