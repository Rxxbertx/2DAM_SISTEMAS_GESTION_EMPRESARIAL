
plantilla_ud_las_palmas = {
    "Brindisi": {
        "posición": "Delantero",
        "nacionalidad": "Argentina",
    },
    "Vicente González": {
        "posición": "Portero",
        "nacionalidad": "Española",
    },
    "Héctor Núñez": {
        "posición": "Delantero",
        "nacionalidad": "Uruguay",
    },
    "Quique Wolff": {
        "posición": "Delantero",
        "nacionalidad": "Argentina",
    },
    "Tonono": {
        "posición": "Centrocampista",
        "nacionalidad": "Española",
    },
    "Ortega": {
        "posición": "Desconocida",
        "nacionalidad": "Española",
    },
    "Juan Guedes": {
        "posición": "Mediocampista",
        "nacionalidad": "Española",
    },
    "Castellano": {
        "posición": "Defensor",
        "nacionalidad": "Española",
    },
    "Cardona": {
        "posición": "Centrocampista",
        "nacionalidad": "Española",
    },
    "Ufarte": {
        "posición": "Centrocampista",
        "nacionalidad": "Francesa",
    },
    "Noly": {
        "posición": "Extremo",
        "nacionalidad": "Italiana",
    },
    "Mesa": {
        "posición": "Extremo",
        "nacionalidad": "Española",
    },
    "Ito": {
        "posición": "Defensor",
        "nacionalidad": "Española",
    },
    "Padrón": {
        "posición": "Defensor",
        "nacionalidad": "Italiana",
    },
    "Soto": {
        "posición": "Defensor",
        "nacionalidad": "Polaca",
    }
}



def get_nationalities():
    nationalities = set()
    for player in plantilla_ud_las_palmas.values():
        nationalities.add(player["nacionalidad"])
    return list(nationalities)

print(get_nationalities())

cantidad_de_arroz = 64
dias = 64

for dia in range(1, dias + 1):
    print(f'Día {dia}: {cantidad_de_arroz} unidades de arroz')
    cantidad_de_arroz *= 2

print(f"Después de {dias} días, tendrás un total de {cantidad_de_arroz} unidades de arroz.")
