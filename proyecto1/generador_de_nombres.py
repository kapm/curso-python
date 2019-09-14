# Generar 3 diccionarios con el archivo de texto
primera_inicial={
    "A":"Amazing",
    "B":"Brilliant",
    "C":"Awesome",
    "D":"Incredible",
    "E":"Uncanny",
    "F":"Impossible",
    "G":"Unbelievable",
    "H":"Surprisingly",
    "I":"Unexpected",
    "J":"Dastardly",
    "K":"Evil",
    "L":"Mounstrous",
    "M":"Preposterous",
    "N":"Alarming",
    "O":"Insane",
    "P":"Terrifying",
    "Q":"Unthinkable",
    "R":"Absurd",
    "S":"Improbable",
    "T":"Outlandish",
    "U":"Questionable",
    "V":"Ridiculous",
    "W":"Erotic",
    "X":"Unfathomable",
    "Y":"Inconceivable",
    "Z":"Unimaginable",
}
segunda_inicial={
    "A":"Giant",
    "B":"Tiny",
    "C:":"Shrinking",
    "D":"Magic",
    "E":"Slimy",
    "F":"Flying",
    "G":"Angry",
    "H":"Crazy",
    "I":"Shiny",
    "J":"Golden",
    "K":"Sticky",
    "L":"Diamond",
    "M":"Flaming",
    "N":"Pyschic",
    "O":"Silent",
    "P":"Screaming",
    "Q":"Jumping",
    "R":"Crouching",
    "S":"Friendly",
    "T":"Omnipotent",
    "U":"Dripping",
    "V":"Flimsy",
    "W":"Hairy",
    "X":"Translucent",
    "Y":"Strange",
    "Z":"Silver",
}
tercera_inicial={
    "A":"Man",
    "B":"Moth",
    "C":"Goat",
    "D":"Princess",
    "E":"Girl",
    "F":"Machine",
    "G":"Bear",
    "H":"Ballon",
    "I":"Ant",
    "J":"Bee",
    "K":"Wolf",
    "L":"Bear",
    "M":"Lion",
    "N":"Ball",
    "O":"Ghost",
    "P":"Witch",
    "Q":"Vampire",
    "R":"Hand",
    "S":"Foot",
    "T":"Tornado",
    "U":"Fish",
    "V":"Millipede",
    "W":"Rock",
    "X":"Nose",
    "Y":"Dog",
    "Z":"Boy",
}


# Pedir nombre, apellido paterno y apellido materno
nombre_inicial=input("Nombre: ")
apellido_paterno=input("Apellido paterno: ")
apellido_materno=input("Apellido materno: ")
# Tomar la primera letra de cada nombre como Key de diccionario
inicial1=nombre_inicial[0]
inicial2=apellido_paterno[0]
inicial3=apellido_materno[0]
# Imprimir el valor de cada key
print("Tu nombre de superheroe es: ")
print(primera_inicial[inicial1])
print(segunda_inicial[inicial2])
print(tercera_inicial[inicial3])