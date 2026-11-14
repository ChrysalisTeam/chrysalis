
.. CUSTOM ROLES HERE


#######################################################################################
{{ document_titles.game_title }}
#######################################################################################

{% if title_key is defined %}{{ document_titles[title_key] }}{% else %}{{ character_properties[current_player_id].official_name }}{% endif %}
################################################################ 


.. raw:: pdf

   PageBreak standardPage

.. XXX contents:: {{ document_titles.table_of_contents }}
..    :depth: {{ toc_depth | default(1) }}

