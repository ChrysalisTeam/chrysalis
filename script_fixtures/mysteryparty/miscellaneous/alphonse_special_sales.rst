

Ventes Privées d'Alphonse
================================

Des occasions inespérées à un prix qui l'est tout autant...
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. raw:: pdf

    Spacer 0 20

{% for section, item_titles in murder_party_items %}
{% if section == "Ventes Privées d'Alphonse" %}

.. container:: large-font

    {% for item_title in item_titles %}
    {{item_title|dangerous_render}}

    .. raw:: pdf

        Spacer 0 15

    {% endfor %}

{% endif %}
{% endfor %}
