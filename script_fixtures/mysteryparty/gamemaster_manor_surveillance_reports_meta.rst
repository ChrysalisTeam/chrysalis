{# BEWARE - this template will need to be evaluated twice recursively #}

Rapports de Surveillance du Manoir
======================================

**Journée des entretiens avec Loyd Georges, la veille de la soirée spéciale d'enchères**


{% for report_time, report_data in abilities.house_reports.settings.reports.items()|sort %}

{{ report_time }}

{{ report_data.surveillance_analysis|indent(width=4, indentfirst=True) }}

{% if report_data.gamemaster_hints %}
    .. container:: gamemaster-hints

{{ report_data.gamemaster_hints|indent(width=8, indentfirst=True) }}
{% endif %}

{% endfor %}
