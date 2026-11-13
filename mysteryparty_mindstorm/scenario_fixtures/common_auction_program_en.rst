The Auctions
=============================================

**{% symbol "Gem lots are sold by descending auction, while artefacts are sold by normal ascending auction." for "auction_process_instructions" %}**

The lots you buy will be swiftly transferred to your Anthropia account.

Note that gems can be spent piecemeal on said portal, in proportion to the estimated total value of the lot.


.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Image
     - Description

{% for item_data in game_items.values()|sort(attribute="auction") %}

{% if item_data.auction %}

   *
     -
       ..  image:: ../../alternate_reality_game_auction/{{ item_data.image }}
         :align: center
         :width: 3cm
     - **{{ item_data.title }}**

       .. raw:: pdf

          Spacer 0 20

       {{ item_data.comments }}

       .. raw:: pdf

          Spacer 0 20

       *Estimated lot price*: {{ item_data.total_price }} Sabarith Pounds

{% endif %}

{% endfor %}
