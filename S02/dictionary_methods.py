song = {"singer": "Edith Piaf",
        "release": 1977,
        "country": "France",
        "title": "la vie en rose", }


# song["title"] = "La Vie En Rose"

dct_new = {"language": "FR", "title": "La Vie En Rose"}
song.update(dct_new)
# import collections

list_of_keys = list(song.keys())
list_of_values = list(song.values())
print(list_of_keys)
print(list_of_values)
print(song)