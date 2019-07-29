import codecs
import json

class Resource:
    resource = {}

    @staticmethod
    def load(filename):
#        with codecs.open(filename, 'r', 'utf-8') as jsonfile:
#            Resource.resource = json.load(jsonfile)
        Resource.resource = {
            "firstname" : "First Name",
            "lastname"  : "Last Name",
            "nickname"  : "Nickname",
            "intellect" : "Smarts",
            "physical"  : "Fitness",
            "hentai"    : "Sensuality",
            "sex"       : "Sex",
            "male"      : "Male",
            "female"    : "Female",
            "answer"    : "Answers",
            "animal"    : "Likes animals",
            "eat"       : "Enjoys eating",
            "cook"      : "Enjoys cooking",
            "exercise"  : "Plays sports",
            "study"     : "Studious",
            "fashionable" : "Fashionable",
            "blackCoffee" : "Black Coffee",
            "spicy"     : "Eat spicy",
            "sweet"     : "Sweet tooth",
            "denial"    : "Allow?",
            "kiss"      : "Kiss",
            "aibu"      : "Groping",
            "anal"      : "Anal",
            "massage"   : "Vibrators",
            "notCondom" : "Condomless",
            "attribute" : "Attribute",
            "hinnyo"    : "Small Bladder",
            "harapeko"  : "Always Hungry",
            "donkan"    : "Oblivious",
            "choroi"    : "Slutty",
            "bitch"     : "Bitchy",
            "mutturi"   : "Pervert",
            "dokusyo"   : "Loves Reading",
            "ongaku"    : "Loves Music",
            "kappatu"   : "Active",
            "ukemi"     : "Passive",
            "friendly"  : "Friendly",
            "kireizuki" : "Fastidious",
            "taida"     : "Lazy",
            "sinsyutu"  : "Elusive",
            "hitori"    : "Solitary",
            "undo"      : "Sporty",
            "majime"    : "Serious",
            "personality" : "Personality",
            "likeGirls" : "Into Girls",
            "personalities" : [
                "Flirt", "Heiress", "Snob", "Underclassman", "Enigma", "Space Case",
                "Japanese Ideal", "Tomboy", "Pure Heart", "Girl Next Door", "Dark Lord", "Mother Figure",
                "Big Sister", "Airhead", "Rebel", "Wild Child", "Honor Student", "Sourpuss",
                "Misfortune Magnet", "Bookworm", "Scaredy Cat", "Classic Heroine", "Fangirl", "Geek",
                "Psycho Stalker", "Slacker", "Introvert", "Tough Girl", "Old School", "Loner", "Extrovert", "Willful", "Sincere", "Glamourous",
            "Returnee", "Slangy˜", "Sadistic", "Emotionless"
            ],
            "weak_point" : "Erogenous zone",
            "weak_points" : ["Lips", "Breasts", "Groin", "Anal", "Butt", "Nipples", "None"],
            "feeling" : "Affection",
            "m_love" : "Male Love",
            "h_count" : "Times Intimate",
            "intimacy" : "Carnality",
            "club" : "Koikatsu Club",
            "koikatu" : ["Unaffiliated", "Member"],
            "relation" : "Relation",
            "relations" : ["Friend", "Lover"],
            "emotion" : "Emotion",
            "exmotions" : ["Normal", "Angry"],
            "date" : "Date",
            "dates" : ["None", "Yes"],
            "ac" : ["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"],
            "mune" : "Breasts",
            "kokan" : "Groin",
            "siri" : "Butt",
            "tikubi" : "Nipples",
            "kokan_piston" : "Pound",
            "anal_piston" : "Anal Pound",
            "houshi" : "Receive"
            }

 
    @staticmethod
    def res(key):
        return Resource.resource[key] if key in Resource.resource else key
