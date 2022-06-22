def switch_level(argument):

    switcher = {
        "Dia": "1d",
        "Mes": "1mo",
        "Hora": ("1h", "2y"),
        "Minuto": ("1m", "7d"),
    }

    return switcher.get(argument, None)
