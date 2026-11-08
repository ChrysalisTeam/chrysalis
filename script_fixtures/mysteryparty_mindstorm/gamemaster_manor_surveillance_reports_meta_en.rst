{# BEWARE - this template will need to be evaluated twice recursively #}

Manor Surveillance Reports
======================================

**Day of the interviews with Loyd Georges, the eve of the special auction evening**


{% for report_time, report_data in abilities.house_reports.settings.reports.items()|sort %}

{{ report_time }}

{{ report_data.surveillance_analysis|indent(width=4, indentfirst=True) }}

{% if report_data.gamemaster_hints %}
    .. container:: gamemaster-hints

{{ report_data.gamemaster_hints|indent(width=8, indentfirst=True) }}
{% endif %}

{% endfor %}
