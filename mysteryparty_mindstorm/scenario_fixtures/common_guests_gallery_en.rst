Sir Loyd Georges' Guests
=============================================

.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Identity
     - {% if use_player_photos %} Photograph {% else %} Avatar {% endif %}

{% for username, user_data in character_properties.items()|sort() %}

{% if not user_data.is_npc %}

   * - **"{{ username.capitalize() }}"**

       {{ user_data.official_name }}

       {{ user_data.official_role }}

       .. raw:: pdf

          Spacer 0 60

     -
       ..  image:: {% if use_player_photos %} ../trombinoscope/{{ username.capitalize() }}-{{ user_data.real_life_identity | replace(' ', '\\ ') }}.jpg {% else %} ../../alternate_reality_game_auction/{{ user_data.avatar }} {% endif %}
         :align: center
         :width: 3cm

{% endif %}

{% endfor %}
