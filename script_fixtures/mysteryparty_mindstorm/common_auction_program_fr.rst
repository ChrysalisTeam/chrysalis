Les Ventes aux Enchères
=============================================

**{% symbol "Les lots de gemmes sont vendus en enchères descendantes, tandis que les artefacts le sont en enchères montantes normales." for "auction_process_instructions" %}**

Les lots achetés seront rapidement transférés sur votre compte Anthropia.

Notez que les gemmes peuvent être dépensées au détail sur ledit portail, au prorata de la valeur totale estimée du lot.


.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Image
     - Description

{% for item_data in game_items.values()|sort(attribute="auction") %}

{% if item_data.auction %}

   *
     -
       ..  image:: ../../{{ item_data.image }}
         :align: center
         :width: 3cm
     - **{{ item_data.title }}**

       .. raw:: pdf

          Spacer 0 20

       {{ item_data.comments }}

       .. raw:: pdf

          Spacer 0 20

       *Prix estimé du lot* : {{ item_data.total_price }} Livres Sabarites

{% endif %}

{% endfor %}
