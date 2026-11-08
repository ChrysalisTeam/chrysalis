
{% macro single_mandate(country_name) %}

.. raw:: pdf

   Spacer 0 40

.. container:: large-font

    Nous, l'Etat Souverain de **{{ country_name }}**,

    mandatons le porteur de la présente missive, citoyen de notre pays, pour négocier en notre nom l'achat d'un gisement de sables bitumineux situé dans le Royaume de Subael, en Austrion.

.. image:: ../../assets/red_seal_wax_empty.png
    :align: right
    :width: 200px

.. raw:: pdf

   Spacer 0 40


{% endmacro %}


{{ single_mandate('Masslavie') }}


{{ single_mandate('Dorie') }}


{{ single_mandate('Lordanie') }}

