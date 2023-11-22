def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60
        if heures == 0:
            temps_texte = f"{minutes_restantes} minute{'s' if minutes_restantes != 1 else ''}"
        elif minutes_restantes == 0:
            temps_texte = f"{heures} heure{'s' if heures != 1 else ''}"
        else:
            temps_texte = f"{heures} heure{'s' if heures != 1 else ''} et {minutes_restantes} minute{'s' if minutes_restantes != 1 else ''}"

     
        print(temps_texte)
    else:
        print("Veuillez entrer un nombre entier de minutes positif.")

time_to_text(120)
time_to_text(75)
time_to_text(45)
time_to_text(0)
time_to_text(-30)
time_to_text(90)
