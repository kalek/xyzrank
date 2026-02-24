import os
import time
import requests

# Twoja tablica z danymi (skrócona wersja dla przykładu)
cards = [
    { "name": "sally-pride-lioness-leader", "tier": "A+" },
    { "name": "umezawa-s-jitte", "tier": "A+" },
    { "name": "agent-bishop-man-in-black", "tier": "A" },
    { "name": "april-o-neil-hacktivist", "tier": "A" },
    { "name": "savanti-romero-time-s-exile", "tier": "A" },
    { "name": "the-last-ronin", "tier": "A" },
    { "name": "path-to-exile", "tier": "A-" },
    { "name": "armaggon-future-shark", "tier": "A-" },
    { "name": "mikey-don-party-planners", "tier": "A-" },
    { "name": "triceraton-commander", "tier": "B+" },
    { "name": "kitsune-dragon-s-daughter", "tier": "B+" },
    { "name": "the-cloning-of-shredder", "tier": "B+" },
    { "name": "mutagen-man-living-ooze", "tier": "B+" },
    { "name": "leatherhead-swamp-stalker", "tier": "B+" },
    { "name": "north-wind-avatar", "tier": "B+" },
    { "name": "krang-shredder", "tier": "B+" },
    { "name": "turncoat-kunoichi", "tier": "B" },
    { "name": "leader-s-talent", "tier": "B" },
    { "name": "leonardo-sewer-samurai", "tier": "B" },
    { "name": "mighty-mutanimals", "tier": "B" },
    { "name": "dimensional-exile", "tier": "B" },
    { "name": "donatello-mutant-mechanic", "tier": "B" },
    { "name": "does-machines", "tier": "B" },
    { "name": "donatello-gadget-master", "tier": "B" },
    { "name": "mondo-gecko", "tier": "B" },
    { "name": "metalhead", "tier": "B" },
    { "name": "super-shredder", "tier": "B" },
    { "name": "madame-null-power-broker", "tier": "B" },
    { "name": "slash-reptile-rampager", "tier": "B" },
    { "name": "raphael-the-nightwatcher", "tier": "B" },
    { "name": "ravenous-robots", "tier": "B" },
    { "name": "raphael-ninja-destroyer", "tier": "B" },
    { "name": "michelangelo-weirdness-to-11", "tier": "B" },
    { "name": "groundchuck-dirtbag", "tier": "B" },
    { "name": "raph-mikey-troublemakers", "tier": "B" },
    { "name": "mikey-leo-chaos-order", "tier": "B" },
    { "name": "splinter-radical-rat", "tier": "B" },
    { "name": "don-leo-problem-solvers", "tier": "B" },
    { "name": "teleportation-circle", "tier": "B-" },
    { "name": "leonardo-cutting-edge", "tier": "B-" },
    { "name": "lita-little-orphan-amphibian", "tier": "B-" },
    { "name": "leonardo-leader-in-blue", "tier": "B-" },
    { "name": "the-last-ronin-s-technique", "tier": "B-" },
    { "name": "koya-death-from-above", "tier": "B-" },
    { "name": "krang-master-mind", "tier": "B-" },
    { "name": "renet-temporal-apprentice", "tier": "B-" },
    { "name": "cytoplast-manipulator", "tier": "B-" },
    { "name": "donatello-way-with-machines", "tier": "B-" },
    { "name": "ray-fillet-man-ray", "tier": "B-" },
    { "name": "rat-king-verminister", "tier": "B-" },
    { "name": "shark-shredder-killer-clone", "tier": "B-" },
    { "name": "stomped-by-the-foot", "tier": "B-" },
    { "name": "anchovy-banana-pizza", "tier": "B-" },
    { "name": "shredder-s-technique", "tier": "B-" },
    { "name": "lord-dregg-insect-invader", "tier": "B-" },
    { "name": "casey-jones-vigilante", "tier": "B-" },
    { "name": "improvised-arsenal", "tier": "B-" },
    { "name": "manhole-missile", "tier": "B-" },
    { "name": "old-hob-alleycat-blues", "tier": "B-" },
    { "name": "raphael-most-attitude", "tier": "B-" },
    { "name": "general-traag-heart-of-stone", "tier": "B-" },
    { "name": "casey-jones-jury-rig-justiciar", "tier": "B-" },
    { "name": "west-wind-avatar", "tier": "B-" },
    { "name": "novel-nunchaku", "tier": "B-" },
    { "name": "michelangelo-mutant-bff", "tier": "B-" },
    { "name": "raph-leo-sibling-rivals", "tier": "B-" },
    { "name": "baxter-stockman", "tier": "B-" },
    { "name": "brilliance-unleashed", "tier": "B-" },
    { "name": "karai-future-of-the-foot", "tier": "B-" },
    { "name": "karai-s-technique", "tier": "B-" },
    { "name": "the-neutrinos", "tier": "B-" },
    { "name": "tainted-treats", "tier": "B-" },
    { "name": "leonardo-s-technique", "tier": "C+" },
    { "name": "uneasy-alliance", "tier": "C+" },
    { "name": "grounded-for-life", "tier": "C+" },
    { "name": "april-o-neil-kunoichi-trainee", "tier": "C+" },
    { "name": "return-to-the-sewers", "tier": "C+" },
    { "name": "donatello-turtle-techie", "tier": "C+" },
    { "name": "buzz-bots", "tier": "C+" },
    { "name": "april-reporter-of-the-weird", "tier": "C+" },
    { "name": "donatello-s-technique", "tier": "C+" },
    { "name": "fugitive-droid", "tier": "C+" },
    { "name": "south-wind-avatar", "tier": "C+" },
    { "name": "death-in-the-family", "tier": "C+" },
    { "name": "dream-beavers", "tier": "C+" },
    { "name": "shredder-unrelenting", "tier": "C+" },
    { "name": "splinter-hamato-yoshi", "tier": "C+" },
    { "name": "spicy-oatmeal-pizza", "tier": "C+" },
    { "name": "bot-bashing-time", "tier": "C+" },
    { "name": "mouser-foundry", "tier": "C+" },
    { "name": "courier-of-comestibles", "tier": "C+" },
    { "name": "michelangelo-improviser", "tier": "C+" },
    { "name": "tenderize", "tier": "C+" },
    { "name": "ragamuffin-raptor", "tier": "C+" },
    { "name": "frog-butler", "tier": "C+" },
    { "name": "pizza-face-gastromancer", "tier": "C+" },
    { "name": "lessons-from-life", "tier": "C+" },
    { "name": "genghis-frog", "tier": "C+" },
    { "name": "go-ninja-go", "tier": "C+" },
    { "name": "dark-leo-shredder", "tier": "C+" },
    { "name": "henchbots", "tier": "C+" },
    { "name": "the-ooze", "tier": "C+" },
    { "name": "turtle-van", "tier": "C+" },
    { "name": "undercity-sewers", "tier": "C+" },
    { "name": "jennika-bad-apple-big-sister", "tier": "C" },
    { "name": "high-flying-ace", "tier": "C" },
    { "name": "ooze-spill", "tier": "C" },
    { "name": "bespoke-b", "tier": "C" },
    { "name": "mind-transfer-protocol", "tier": "C" },
    { "name": "sewer-veillance-cam", "tier": "C" },
    { "name": "stockman-mad-fly-entist", "tier": "C" },
    { "name": "paramecia-colonies", "tier": "C" },
    { "name": "tunnel-rats", "tier": "C" },
    { "name": "squirellanoids", "tier": "C" },
    { "name": "raphael-tough-turtle", "tier": "C" },
    { "name": "rock-soldiers", "tier": "C" },
    { "name": "venus-torn-between-worlds", "tier": "C" },
    { "name": "saved-by-the-shell", "tier": "C" },
    { "name": "michelangelo-game-master", "tier": "C" },
    { "name": "primordial-pachyderm", "tier": "C" },
    { "name": "zoo-escapees", "tier": "C" },
    { "name": "transdimensional-bovine", "tier": "C" },
    { "name": "don-raph-hard-science", "tier": "C" },
    { "name": "mechanized-ninja-cavalry", "tier": "C" },
    { "name": "ice-cream-kitty", "tier": "C" },
    { "name": "slithering-cryptid", "tier": "C" },
    { "name": "behop-rocksteady", "tier": "C" },
    { "name": "tokka-rahzar-terrible-twos", "tier": "C" },
    { "name": "conquerors-flail", "tier": "C" },
    { "name": "metallic-mimic", "tier": "C" },
    { "name": "shadowspear", "tier": "C" },
    { "name": "chrome-dome", "tier": "C" },
    { "name": "escape-tunnel", "tier": "C" },
    { "name": "dimension-x", "tier": "C" },
    { "name": "foot-headquarters", "tier": "C" },
    { "name": "illegitimate-business", "tier": "C" },
    { "name": "mutant-town", "tier": "C" },
    { "name": "tcri-building", "tier": "C" },
    { "name": "leonardo-big-brother", "tier": "C-" },
    { "name": "east-wind-avatar", "tier": "C-" },
    { "name": "hamato-guardian-stance", "tier": "C-" },
    { "name": "action-news-crew", "tier": "C-" },
    { "name": "make-your-move", "tier": "C-" },
    { "name": "prehistoric-pet", "tier": "C-" },
    { "name": "utrom-scientists", "tier": "C-" },
    { "name": "retro-mutation", "tier": "C-" },
    { "name": "oroku-saki-shredder-rising", "tier": "C-" },
    { "name": "foot-mystic", "tier": "C-" },
    { "name": "wingnut-bat-on-the-belfry", "tier": "C-" },
    { "name": "purple-dragon-punks", "tier": "C-" },
    { "name": "null-group-biological-assets", "tier": "C-" },
    { "name": "mouser-attack", "tier": "C-" },
    { "name": "mutant-town-musicians", "tier": "C-" },
    { "name": "silverclad-ferocidons", "tier": "C-" },
    { "name": "mona-lisa-science-geek", "tier": "C-" },
    { "name": "cowabunga", "tier": "C-" },
    { "name": "guac-marshmallow-pizza", "tier": "C-" },
    { "name": "foot-ninjas", "tier": "C-" },
    { "name": "epf-point-squad", "tier": "C-" },
    { "name": "nobody", "tier": "C-" },
    { "name": "putrid-pals", "tier": "C-" },
    { "name": "weather-maker", "tier": "C-" },
    { "name": "turtle-blimp", "tier": "C-" },
    { "name": "omni-cheese-pizza", "tier": "C-" },
    { "name": "northampton-farm", "tier": "C-" },
    { "name": "turtles-forever", "tier": "D+" },
    { "name": "crustacean-commando", "tier": "D+" },
    { "name": "negate", "tier": "D+" },
    { "name": "brainstorm", "tier": "D+" },
    { "name": "bebop-warthog-warrior", "tier": "D+" },
    { "name": "insectoid-exterminator", "tier": "D+" },
    { "name": "pain-101", "tier": "D+" },
    { "name": "shredder-s-revenge", "tier": "D+" },
    { "name": "ninja-teen", "tier": "D+" },
    { "name": "hard-won-jitte", "tier": "D+" },
    { "name": "underworld-breach", "tier": "D+" },
    { "name": "zog-triceraton-castaway", "tier": "D+" },
    { "name": "rocksteady-crash-courser", "tier": "D+" },
    { "name": "mutant-chain-reaction", "tier": "D+" },
    { "name": "michelangelo-s-technique", "tier": "D+" },
    { "name": "foot-elite", "tier": "D+" },
    { "name": "mouser-mark-iii", "tier": "D+" },
    { "name": "punk-frogs", "tier": "D+" },
    { "name": "arcbound-ravager", "tier": "D+" },
    { "name": "everything-pizza", "tier": "D+" },
    { "name": "sword-of-sinew-and-steel", "tier": "D+" },
    { "name": "technodrome", "tier": "D+" },
    { "name": "turtle-lair", "tier": "D+" },
    { "name": "trouble-in-pairs", "tier": "D" },
    { "name": "quintessential-katana", "tier": "D" },
    { "name": "featherbrained-flicher", "tier": "D" },
    { "name": "kitsune-s-technique", "tier": "D" },
    { "name": "turtles-in-time", "tier": "D" },
    { "name": "shredder-s-armor", "tier": "D" },
    { "name": "splinter-s-technique", "tier": "D" },
    { "name": "ashcoat-of-the-shadow-swarm", "tier": "D" },
    { "name": "plague-of-vermin", "tier": "D" },
    { "name": "jennika-s-technique", "tier": "D" },
    { "name": "cool-but-rude", "tier": "D" },
    { "name": "all-will-be-one", "tier": "D" },
    { "name": "new-generation-s-technique", "tier": "D" },
    { "name": "turtle-power", "tier": "D" },
    { "name": "doubling-season", "tier": "D" },
    { "name": "waves-of-aggression", "tier": "D" },
    { "name": "krang-utrom-warlord", "tier": "D" },
    { "name": "skateboard", "tier": "D" },
    { "name": "raphael-s-technique", "tier": "D-" },
    { "name": "party-dude", "tier": "D-" },
    { "name": "rhythm-of-the-wild", "tier": "D-" },
    { "name": "broadcast-takeover", "tier": "F" }
];

def download_card_images(card_list):
    # Tworzymy folder na obrazki, jeśli nie istnieje
    if not os.path.exists('card_images'):
        os.makedirs('card_images')

    for card in card_list:
        file_name = f"{card['name']}.jpg"
        file_path = os.path.join('card_images', file_name)

        # Pomijamy, jeśli już pobrano
        if os.path.exists(file_path):
            print(f"Pominięto: {card['name']} (już istnieje)")
            continue

        # API Scryfall - szukanie po nazwie (fuzzy search)
        # Zamieniamy myślniki na spacje dla lepszego wyszukiwania w API
        search_name = card['name'].replace('-', ' ')
        api_url = f"https://api.scryfall.com/cards/named?fuzzy={search_name}"

        try:
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                # Wybieramy obrazek w wersji 'large' lub 'normal'
                image_url = data.get('image_uris', {}).get('large')
                
                # Obsługa kart dwustronnych (Transform)
                if not image_url and 'card_faces' in data:
                    image_url = data['card_faces'][0].get('image_uris', {}).get('large')

                if image_url:
                    img_data = requests.get(image_url).content
                    with open(file_path, 'wb') as f:
                        f.write(img_data)
                    print(f"Pobrano: {card['name']}")
                else:
                    print(f"Błąd: Nie znaleziono URL obrazka dla {card['name']}")
            
            elif response.status_code == 404:
                print(f"Błąd: Karta {card['name']} nie została znaleziona w Scryfall")
            
            # Scryfall prosi o 50-100ms przerwy między zapytaniami
            time.sleep(0.1)

        except Exception as e:
            print(f"Wystąpił błąd przy {card['name']}: {e}")

if __name__ == "__main__":
    download_card_images(cards)