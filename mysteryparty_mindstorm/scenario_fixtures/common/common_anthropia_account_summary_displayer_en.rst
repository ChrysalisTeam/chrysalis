{# Per-player data are read from the current character (current_player_id, a real player here); hide_anthropia_credentials may be set by the caller #}
{% set permissions = character_properties[current_player_id].permissions %}
{% if permissions %} {# Beware, might give empty list if available_anthropia_abilities is incomplete #}

**On the Anthropia web portal, you also have access to these special operations:**

{% for permission, description in available_anthropia_abilities.items() %}
{% if (permission in permissions) %}- {{description}}{% endif %}
{% endfor %}

{% else %}

**On the Anthropia web portal, you do not have access to any special operations.**

{% endif %}


{% if not hide_anthropia_credentials | default(false) %}

Your Anthropia web credentials
=====================================================

{# TODO move some of this to general rules #}

These authentication details give you access to your account - **strictly personal** - on the Anthropia web portal.
If other users are in **digital friendship** with you, you will also be able to view their data from your account.
Do not forget to **log out** after using Anthropia from a public web terminal (there are some in Loyd Georges' manor).
This web portal is compatible with **mobile devices**.
Email messages sent from Anthropia are deemed **impossible to intercept**.
As a reminder, most inhabitants of Pangea do not yet have an Anthropia account, and must therefore be contacted by other means, such as the telephone or the post.

.. raw:: pdf

   Spacer 0 5

- URL: {{anthropia_portal_url}}
- LOGIN:  {{current_player_id}}
- PASSWORD:  {{ character_properties[current_player_id].password }}

{% endif %}

