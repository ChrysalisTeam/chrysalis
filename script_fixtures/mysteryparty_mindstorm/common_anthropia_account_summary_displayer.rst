
{% if permissions %} {# Beware, might give empty list if available_anthropia_abilities is incomplete #}

**Sur le portail web Anthropia, vous avez aussi accès à ces opérations spéciales :**

{% for permission, description in available_anthropia_abilities.items() %}
{% if (permission in permissions) %}- {{description}}{% endif %}
{% endfor %}

{% else %}

**Sur le portail web Anthropia, vous n'avez pas accès à des opérations spéciales.**

{% endif %}


{% if not hide_anthropia_credentials %}

Vos identifiants web sur Anthropia
=====================================================

{# TODO move some of this to general rules #}

Ces informations d'authentification vous donnent accès à votre compte - **strictement personnel** - sur le portail web Anthropia.
Si d'autres utilisateurs sont en **amitié numérique** avec vous, vous aurez aussi la possibilité de visualiser leurs données depuis votre compte.
N'oubliez pas de vous **déconnecter** après avoir utilisé Anthropia depuis un terminal web public (il en existe dans le manoir de Loyd Georges).
Ce portail web est compatible avec les **appareils mobiles**.
Les messages email envoyés depuis Anthropia sont réputés **non interceptables**.
Pour rappel, la plupart des habitants de Pangéa n'ont pas encore de compte Anthropia, et doivent donc être contactés par d'autres moyens, comme le téléphone ou la Poste.

.. raw:: pdf

   Spacer 0 5

- URL : {{anthropia_portal_url}}
- LOGIN :  {{current_player_id}}
- PASSWORD :  {{current_player_password}}

{% endif %}

