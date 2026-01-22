import os
import requests
import time

# Pełna lista kart z Twojego zestawienia
cards = [
    "Spinerock Tyrant", "Ajani, Outland Chaperone", "Curious Colossus", "Eirdu, Carrier of Dawn // Isilu, Carrier of Twilight",
    "Champions of the Shoal", "Loch Mare", "Sunderflock", "End-Blaze Epiphany", "Soul Immolation", "Bitterbloom Bearer", 
    "Champion of the Weird", "Moonshadow", "Champion of the Clachan", "Disruptor of Currents", "Flitterwing Nuisance", 
    "Glen Elendra Guardian", "Lofty Dreams", "Oko, Lorwyn Liege // Oko, Shadowmoor Scion", 
    "Sygg, Wanderwine Wisdom // Sygg, Wanderbrine Shield", "Sear", "Gloom Ripper", "Taster of Wares", "Adept Watershaper", 
    "Brigid, Clachan’s Heart // Brigid, Doun’s Mind", "Kinbinding", "Pyrrhic Strike", "Blossombind", "Glamer Gifter", 
    "Harmonized Crescendo", "Mirrorform", "Rime Chill", "Rimekin Recluse", "Shinestriker", "Swat Away", "Temporal Cleansing", 
    "Unwelcome Sprite", "Ashling, Rekindled // Ashling, Rimebound", "Boulder Dash", "Champion of the Path", "Cinder Strike", 
    "Collective Inferno", "Explosive Prodigy", "Feed the Flames", "Giantfall", "Goliath Daydreamer", "Sizzling Changeling", 
    "Blight Rot", "Bogslither’s Embrace", "Creakwood Safewright", "Dawnhand Dissident", "Gnarlbark Elm", "Graveshifter", 
    "Iron-Shield Elf", "Nameless Inversion", "Burdened Stoneback", "Encumbered Reejerey", "Kinscaer Sentry", "Liminal Hold", 
    "Moonlit Lamenter", "Protective Response", "Rhys, the Evermore", "Slumbering Walker", "Spiral into Solitude", 
    "Wanderbrine Trapper", "Winnowing", "Glamermite", "Noggle the Mind", "Silvergill Mentor", "Unexpected Assistance", 
    "Boldwyr Aggressor", "Elder Auntie", "Flamebraider", "Kulrath Zealot", "Scuzzback Scrounger", "Sourbread Auntie", 
    "Squawkroaster", "Sting-Slinger", "Tweeze", "Boggart Mischief", "Dream Seizer", 
    "Grub, Storied Matriarch // Grub, Notorious Auntie", "Gutsplitter Gang", "Mudbutton Cursetosser", "Nightmare Sower", 
    "Requiting Hex", "Retched Wretch", "Scarblade Scout", "Shimmercreep", "Twilight Diviner", "Unbury", "Flock Impostor", 
    "Thoughtweft Imbuer", "Wanderbrine Preacher", "Aquitect’s Defenses", "Illusion Spinners", "Omni-Changeling", 
    "Stratosoarer", "Summit Sentinel", "Thirst for Identity", "Wild Unraveling", "Boneclub Berserker", "Brambleback Brute", 
    "Flamekin Gildweaver", "Goatnap", "Gristle Glutton", "Hexing Squelcher", "Kindle the Inner Flame", "Soulbright Seeker", 
    "Warren Torchmaster", "Auntie’s Sentence", "Barbed Bloodletter", "Bloodline Bidding", "Boggart Prankster", 
    "Dawnhand Eulogist", "Dose of Dawnglow", "Heirloom Auntie", "Goldmeadow Nomad", "Keep Out", "Kinsbaile Aspirant", 
    "Morningtide’s Light", "Personify", "Reluctant Dounguard", "Shore Lurker", "Sun-Dappled Celebrant", "Timid Shieldbearer", 
    "Tributary Vaulter", "Glen Elendra’s Answer", "Gravelgill Scoundrel", "Kulrath Mystic", "Pestered Wellguard", 
    "Run Away Together", "Silvergill Peddler", "Tanufel Rimespeaker", "Wanderwine Distracter", "Wanderwine Farewell", 
    "Burning Curiosity", "Enraged Flamecaster", "Flame-Chain Mauler", "Impolite Entrance", "Lavaleaper", "Reckless Ransacking", 
    "Bile-Vial Boggart", "Blighted Blackthorn", "Moonglove Extractor", "Perfect Intimidation", "Scarblade’s Malice", 
    "Appeal to Eirdu", "Bark of Doran", "Clachan Festival", "Crib Swap", "Evershrike’s Gift", "Gallant Fowlknight", 
    "Kithkeeper", "Meanders Guide", "Riverguard’s Reflexes", "Rimefire Torque", "Spell Snare", "Lasting Tarfire", 
    "Meek Attack", "Darkness Descends", "Mornsong Aria"
]

if not os.path.exists('img'):
    os.makedirs('img')

print(f"Rozpoczynam pobieranie {len(cards)} obrazków...")

for full_name in cards:
    # Czyścimy nazwę do zapisu pliku
    clean_filename = full_name.replace(' ', '_').replace(',', '').replace('’', '').replace("'", "").replace('//', '_').split('_')[0]
    filepath = f"img/{clean_filename}.jpg"
    
    # Pomijamy, jeśli już pobrane
    if os.path.exists(filepath):
        continue

    # Do API wysyłamy tylko pierwszą część nazwy przed //
    search_name = full_name.split('//')[0].strip()
    
    try:
        url = f"https://api.scryfall.com/cards/named?fuzzy={search_name}"
        res = requests.get(url).json()
        
        # Pobieranie URL obrazka (obsługa normalnych i dwustronnych)
        img_url = None
        if 'image_uris' in res:
            img_url = res['image_uris']['normal']
        elif 'card_faces' in res:
            img_url = res['card_faces'][0]['image_uris']['normal']
            
        if img_url:
            img_data = requests.get(img_url).content
            with open(filepath, 'wb') as f:
                f.write(img_data)
            print(f"Sukces: {clean_filename}")
        else:
            print(f"Nie znaleziono obrazka dla: {full_name}")
            
        # Odczekaj 100ms zgodnie z prośbą Scryfall (żeby nie dostać bana)
        time.sleep(0.1)
        
    except Exception as e:
        print(f"Błąd przy {full_name}: {e}")

print("Zakończono! Sprawdź folder 'img'.")