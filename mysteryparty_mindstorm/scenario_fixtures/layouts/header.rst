{# Title page and table of contents of decorated sheets. The title is document_titles[title_key] if "title_key" is defined, else the official name of the current character #}
{% if title_key is defined %}{% set sheet_title = document_titles[title_key] %}{% else %}{% set sheet_title = character_properties[current_player_id].official_name %}{% endif %}

#######################################################################################
MINDSTORM
#######################################################################################

{{ sheet_title }}
################################################################################

.. raw:: pdf

   Spacer 0 80

   PageBreak standardPage

.. contents:: {{ document_titles.table_of_contents }}
   :depth: {{ toc_depth }}

