# -*- coding: utf-8 -*-
"""
Variables hook of the Descent RPG ("storygen_hooks.check_variables" in configuration.yaml).

It validates the "descent_rpg" variable of descent_rpg_data_<lang>.yaml (a check formerly done by
the DescentRpgData module of Pychronia, which doesn't load this data anymore), before sheets are rendered.
"""

STAT_NAMES = ("constitution", "agility", "observation")
MIN_STAT, MAX_STAT = 1, 5  # 6 on the dice is always a FUMBLE


class DescentDataError(ValueError):
    pass


def _check(condition, path, message):
    if not condition:
        raise DescentDataError("Invalid descent_rpg data at %s: %s" % (path, message))


def _check_string(value, path, multiline):
    _check(isinstance(value, str), path, "a string is expected, not %r" % (value,))
    _check(value.strip(), path, "the string must not be empty")
    if not multiline:
        _check("\n" not in value, path, "the string must hold on a single line")


def _check_string_list(values, path):
    _check(isinstance(values, list), path, "a list is expected, not %r" % (values,))
    for index, entry in enumerate(values):
        _check_string(entry, "%s[%d]" % (path, index), multiline=False)


def check_descent_rpg_data(descent_data):
    _check(isinstance(descent_data, dict), "descent_rpg", "a mapping is expected")

    _check_string_list(descent_data["common_equipments"], "descent_rpg.common_equipments")

    players = descent_data["players"]
    _check(isinstance(players, dict) and players, "descent_rpg.players", "a non-empty mapping is expected")

    for player_id, player_data in players.items():
        path = "descent_rpg.players.%s" % player_id
        _check(isinstance(player_id, str) and player_id and not any(c.isspace() for c in player_id),
               path, "the player ID must be a slug")

        _check_string(player_data["name"], path + ".name", multiline=False)
        _check_string(player_data["missions"], path + ".missions", multiline=True)

        for stat_name in STAT_NAMES:
            stat = player_data["stats"][stat_name]
            _check(isinstance(stat, int) and not isinstance(stat, bool) and MIN_STAT <= stat <= MAX_STAT,
                   "%s.stats.%s" % (path, stat_name), "an integer between %d and %d is expected, not %r"
                   % (MIN_STAT, MAX_STAT, stat))

        _check_string_list(player_data["abilities"], path + ".abilities")
        _check_string_list(player_data["equipments"], path + ".equipments")


def check_variables(variables, *, language, jinja_env):
    check_descent_rpg_data(variables["descent_rpg"])
    # None means "keep the variables unchanged"
