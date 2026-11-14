{# The reports are themselves jinja templates: they are rendered here, with the real identities of characters (gamemaster version) #}

Manor Surveillance Reports
======================================

**Day of the interviews with Loyd Georges, the eve of the special auction evening**


{% for report_time, report_data in abilities.house_reports.settings.reports.items()|sort %}

{{ report_time }}

{{ report_data.surveillance_analysis|indent(width=4, first=True)|replace(".official_name", ".spoiling_official_name")|dangerous_render }}

{% if report_data.gamemaster_hints %}
    .. container:: gamemaster-hints

{{ report_data.gamemaster_hints|indent(width=8, first=True)|replace(".official_name", ".spoiling_official_name")|dangerous_render }}
{% endif %}

{% endfor %}
