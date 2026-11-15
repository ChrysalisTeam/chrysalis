

Alphonse's Private Sales
================================

Unhoped-for bargains at an equally unhoped-for price...
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. raw:: pdf

    Spacer 0 20

{% for section, section_item_structs in murder_party_items %}
{% if section == "Ventes Privées d'Alphonse" %}

.. container:: large-font

    {% for section_item_struct in section_item_structs %}
    {{section_item_struct.item_label|dangerous_render}}

    .. raw:: pdf

        Spacer 0 15

    {% endfor %}

{% endif %}
{% endfor %}
