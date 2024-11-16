import folium
# Full list of locations from the user's table with updated coordinates
locations = [
    {"name": "Galleria Borghese", "maps_link": "https://maps.app.goo.gl/5wMpH9yHbvnvFMsf6", "type": "Muzeum/Galeria", "coords": [ 41.9140607, 12.4920302]},
    {"name": "Piazza del Popolo", "maps_link": "https://maps.app.goo.gl/A3BQwEs5dYuoBZyU8", "type": "Obiekt", "coords": [41.910693, 12.476360]},
    {"name": "Museo e Cripta dei Cappuccini", "maps_link": "https://maps.app.goo.gl/4gy4FyGcYMHES36h7", "type": "Muzeum/Galeria", "coords": [41.904772, 12.488615]},
    {"name": "Chiesa di Santa Susanna alle Terme di Diocleziano", "maps_link": "https://maps.app.goo.gl/G3NcDRk1oNnkUVoh8", "type": "Chiesa", "coords": [41.904267, 12.493676]},
    {"name": "Chiesa di San Carlino alle Quattro Fontane", "maps_link": "https://maps.app.goo.gl/DbAaBuK5LhMT1Fhq8", "type": "Chiesa", "coords": [41.901806, 12.490771]},
    {"name": "Fontana del Tritone", "maps_link": "https://maps.app.goo.gl/u1w2jVYqNN45zTzMA", "type": "Obiekt", "coords": [41.903666, 12.488483]},
    {"name": "Fontana delle Naiadi", "maps_link": "https://maps.app.goo.gl/w9JhDVXZXwXfUygt8", "type": "Obiekt", "coords": [41.902716, 12.496235]},
    {"name": "Gallerie Nazionali di Arte Antica - Palazzo Barberini", "maps_link": "https://maps.app.goo.gl/P5Qj5CKcZw8egKnV9", "type": "Galeria", "coords": [41.903469, 12.489948]},
    {"name": "Chiesa di Santa Maria della Vittoria", "maps_link": "https://maps.app.goo.gl/fdRyqyv149pwnFnS9", "type": "Chiesa", "coords": [41.904724, 12.494178]},
    {"name": "Fontana dell'Acqua Felice", "maps_link": "https://maps.app.goo.gl/7eFg5J7AVxeStTyT8", "type": "Obiekt", "coords": [41.904387, 12.494446]},
    {"name": "Musei Vaticani", "maps_link": "https://maps.app.goo.gl/V7ooJG2S23R4PFtG6", "type": "Muzeum/Galeria", "coords": [41.904972, 12.454671]},
    {"name": "Castel Sant'Angelo", "maps_link": "https://maps.app.goo.gl/QL1iZmibC8pHDrHh8", "type": "Muzeum/Galeria", "coords": [41.903094, 12.466355]},
    {"name": "Basilica di San Pietro in Vaticano", "maps_link": "https://maps.app.goo.gl/EXgF88ngNSo6Ru7P9", "type": "Chiesa", "coords": [41.902171, 12.453663]},
    {"name": "All’Antico Vinaio", "maps_link": "https://maps.app.goo.gl/B39aAeR6W4XCU7ic8", "type": "Jedzenie", "coords": [41.899063, 12.477282]},
    {"name": "Chiesa di Sant'Ignazio di Loyola", "maps_link": "https://maps.app.goo.gl/qkEf6RpQnRLMJC6K7", "type": "Chiesa", "coords": [44.979265, 10.041265]},
    {"name": "Fontana di Trevi", "maps_link": "https://maps.app.goo.gl/qpZ29ponZJ6Qxgo7A", "type": "Obiekt", "coords": [41.900943, 12.483290]},
    {"name": "Chiesa di San Marcello al Corso", "maps_link": "https://maps.app.goo.gl/mJxXD48nbZWRPW7c9", "type": "Chiesa", "coords": [41.898688, 12.481976]},
    {"name": "Galleria Doria Pamphilj", "maps_link": "https://maps.app.goo.gl/po9NPHHiHpjHZNoC9", "type": "Muzeum/Galeria", "coords": [41.896931, 12.481359]},
    {"name": "Chiesa del Gesù", "maps_link": "https://maps.app.goo.gl/4Za5dgLPeUPgaTHJ8", "type": "Chiesa", "coords": [41.895904, 12.479798]},
    {"name": "Pantheon", "maps_link": "https://maps.app.goo.gl/8CbiFPko5aPeYyz77", "type": "Atrakcja", "coords": [41.898596, 12.476834]},
    {"name": "Chiesa di Sant’Ivo alla Sapienza", "maps_link": "https://maps.app.goo.gl/QiMnrx5GXRmpEuqR9", "type": "Chiesa", "coords": [41.898184, 12.474876]},
    {"name": "Piazza Navona", "maps_link": "https://maps.app.goo.gl/tVDYyRQtXBYDkcsV8", "type": "Obiekt", "coords": [41.898967, 12.473093]},
    {"name": "Chiesa di San Luigi dei Francesi", "maps_link": "https://maps.app.goo.gl/nutYaM56TGZCv2tF7", "type": "Chiesa", "coords": [41.899578, 12.474554]},
    {"name": "Basilica di Sant'Andrea della Valle", "maps_link": "https://maps.app.goo.gl/JyT1wnSQV7a96DFt5", "type": "Chiesa", "coords": [41.895962, 12.474343]},
    {"name": "Fontana dei Quattro Fiumi", "maps_link": "https://maps.app.goo.gl/fvNR7sYZLuS7tiLk7", "type": "Obiekt", "coords": [41.898953, 12.473085]},
    {"name": "Chiesa di Santa Maria della Pace", "maps_link": "https://maps.app.goo.gl/MJtQCFyuV73SzxPf6", "type": "Chiesa", "coords": [41.899869, 12.471682]},
    {"name": "Oratorio dei Filippini", "maps_link": "https://maps.app.goo.gl/HSJUfG1WnuV1SVsJ9", "type": "Chiesa", "coords": [41.898664, 12.468809]},
    {"name": "Campo de' Fiori", "maps_link": "https://maps.app.goo.gl/ZEXx3FVbptUGcpei7", "type": "Obiekt", "coords": [41.895591, 12.472149]},
    {"name": "Scalinata di Trinità dei Monti", "maps_link": "https://maps.app.goo.gl/tkHPsJxEqdZfBHUB9", "type": "Obiekt", "coords": [41.906014, 12.482837]},
    {"name": "Trastevere", "maps_link": "https://maps.app.goo.gl/KEipRHegG3EKhKyj8", "type": "Atrakcja", "coords": [41.88854, 12.47111]},
    {"name": "Basilica di Santa Cecilia in Trastevere", "maps_link": "https://maps.app.goo.gl/D8SMFUAM47jz6dtJ7", "type": "Chiesa", "coords": [41.887566, 12.475855]},
    {"name": "Chiesa di San Francesco a Ripa", "maps_link": "https://maps.app.goo.gl/EutWL9PU8FBh1gv5A", "type": "Chiesa", "coords": [41.885052, 12.473305]},
    {"name": "L'Aventino", "maps_link": "https://maps.app.goo.gl/no1EGVPo8zff1hmy5", "type": "Atrakcja", "coords": [41.885018, 12.480356]},
    {"name": "Piazza dei Cavalieri di Malta", "maps_link": "https://maps.app.goo.gl/eA6oCBNJYfBuETET9?g_st=com.google.maps.preview.copy", "type": "Atrakcja", "coords": [41.882884, 12.478570]},
    {"name": "Foro Romano", "maps_link": "https://maps.app.goo.gl/PSGbjDYw352ynfdJA", "type": "Atrakcja", "coords": [41.891584, 12.486638]},
    {"name": "Musei Capitolini", "maps_link": "https://maps.app.goo.gl/ipMUeaP62Ca13zrS8", "type": "Muzeum/Galeria", "coords": [41.892886, 12.482464]},
    {"name": "Colosseo", "maps_link": "https://maps.app.goo.gl/NJe6ZZq7hg2noHLa9", "type": "Atrakcja", "coords": [41.890232, 12.492351]},
    {"name": "Catacombe di San Callisto", "maps_link": "https://maps.app.goo.gl/pQaMvG9aBsvsfrjB6", "type": "Atrakcja", "coords": [41.85890, 12.51070]},
    {"name": "Via Appia Antica", "maps_link": "https://maps.app.goo.gl/mvcyb8qhm1sXrwXj7", "type": "Atrakcja", "coords": [41.85412, 12.51819]},
    {"name": "Basilica di San Giovanni in Laterano", "maps_link": "https://maps.app.goo.gl/pttecYuLYkweMFZU9", "type": "Chiesa", "coords": [41.88575, 12.50560]},
    {"name": "Altare della Patria", "maps_link": "https://maps.app.goo.gl/nKJhRD4iGP1cXVbs6", "type": "Atrakcja", "coords": [41.894651, 12.483070]},
    {"name": "Monumento a Vittorio Emanuele II", "maps_link": "https://maps.app.goo.gl/c1gt6wWLXiGVr3o9A", "type": "Muzeum/Galeria", "coords": [41.894451, 12.483154]},
    {"name": "Foro di Cesare - Viaggio nei fori", "maps_link": "https://maps.app.goo.gl/SExSPF8zT3XyrXuT7", "type": "Obiekt", "coords": [41.893716, 12.485085]},
    {"name": "Parco degli Acquedotti", "maps_link": "https://maps.app.goo.gl/kXEFrQAyb8YonzDT9", "type": "Atrakcja", "coords": [41.84492, 12.56184]},
]


# Define a dictionary of colors for different types
type_colors = {
    "Muzeum/Galeria": "blue",
    "Chiesa": "green",
    "Obiekt": "red",
    "Atrakcja": "orange",
    "Jedzenie": "purple"
}

# Initialize the map centered on Rome
rome_map = folium.Map(location=[41.9028, 12.4964], zoom_start=13)

# Add markers to the map based on the corrected coordinates
for location in locations:
    folium.Marker(
        location=location["coords"],
        popup=f"<a href='{location['maps_link']}' target='_blank'>{location['name']}</a>",
        icon=folium.Icon(color=type_colors.get(location["type"], "gray"))
    ).add_to(rome_map)

# Save the updated map as an HTML file
map_path = "Rome_chunks_map.html"
rome_map.save(map_path)