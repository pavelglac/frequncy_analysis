import json
import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class EnglishWords:
    def __init__(self):
        self.transcripts = self.get_transcript()
        self.all_words_frequency = FreqDist()
        self.set_frequency_analysis(self.get_selected_words())
        self.print_most_frequent_words()
    
    def frequency_analysis(self, text, comparasion_words):
        words = [word.lower() for word in word_tokenize(text) if word.lower() in comparasion_words]
        frequency = FreqDist(words)
        return frequency

    def set_frequency_analysis(self, comparasion_words):
        for record in self.transcripts:
            video_name = record.get('name', 'N/A')
            transcript = record.get('content', '')
            result_frequency_analysis = self.frequency_analysis(transcript, comparasion_words)
            self.all_words_frequency += result_frequency_analysis
            self.print_video_most_frequent_words(result_frequency_analysis, video_name)
    
    def get_selected_words(self):
        return ["film", "flics", "putain", "cool", "bosser", "ouf", "match", "jock", "foutre", "hyper", "cul", "catch", "camp", "ranch", "pote", "dalle", "british", "parking", "move", "creepy", "gadget", "pro", "van", "star", "news", "giga", "culot", "flic", "interview", "big", "coach", "hashtag", "game", "kidnapper", "trip", "new", "perf", "pudding", "boss", "bouffe", "job", "prime", "fan", "foot", "checker", "deal", "city", "gamins", "bleak", "roar", "rails", "crack", "bond", "bluff", "bullshit", "hype", "random", "hab", "mater", "stalker", "life", "lock", "pitch", "staff", "copain", "fuck", "story", "gamin", "gang", "gang", "spoil", "gaffe", "swing", "style", "slip", "bunker", "interviewer", "stress", "nickel", "clean", "king", "flop", "moves", "stock", "pubs", "hardcore", "mark", "troll", "giant", "safety", "packs", "fun", "healthy", "choice", "cash", "bull", "seventies", "vache", "hippies", "bass", "stop", "challenger", "cap", "cargo", "league", "legends", "check", "vip", "chuck", "kidnapping", "welcome", "extradition", "cocktails", "jobs", "momo", "fucking", "clubs", "prank", "good", "kif", "gogo", "smart", "merch", "stars", "battle", "bubble", "sponsor", "intact", "trolls", "time", "troller", "cockpit", "dead", "gangs", "weed", "far", "west", "flipper", "bad", "gala", "jet", "united", "way", "bulldozers", "guinness", "book", "squeeze", "ticket", "ratio", "joke", "puddings", "american", "dream", "willy", "disneyland", "blues", "dealers", "overdose", "classes", "school", "french", "destroyer", "premium", "crew", "script", "jackass", "girls", "macho", "hockey", "yes", "buzz", "gains", "raft", "one", "warner", "spot", "manor", "house", "hotel", "banger", "trips", "success", "call", "duty", "casting", "fox", "callback", "bankable", "crim", "travel", "academy", "gun", "hookman", "smile", "name", "dropping", "gadgets", "chips", "certif", "nullo", "standing", "ovation", "hoppy", "update", "morning", "britain", "airways", "class", "spring", "stag", "trophy", "chair", "bowling", "kits", "weekends", "feedback", "need", "speed", "shortcut", "snow", "gentleman", "quiz", "setup", "dispatch", "cartoon", "say", "england", "foulards", "pillow", "fight", "guest", "handball", "killers", "slips", "eighties", "killer", "trigger", "bite", "rafting", "skins", "wife", "carrying", "championship", "uppercut", "teaser", "twitch", "round", "rust", "jacking", "warning", "thank", "businessman", "comeback", "smash", "showman", "catcher", "storytelling", "dragon", "blue", "panther", "balloon", "blend", "slogan", "options", "please", "fail", "leader", "squatter", "cocktail", "discount", "grocery", "outlet", "low", "cost", "flasher", "revolvers", "bombed", "boom", "puzzle", "buggy", "events", "duncan", "try", "freedom", "social", "stands", "rolling", "stone", "event", "silent", "cools", "hot", "dog", "zombie", "freestyle", "surfer", "making", "pranks", "cookie", "misplay", "flip", "psycho", "fake", "make", "sheriff", "shot", "bourbon", "scoop", "blick", "shopper", "stickers", "discord", "best", "admin", "jungle", "trek", "halloween", "surplus", "buzzers", "sixties", "spoiler", "chiller", "chill", "soldier", "zoos", "steak", "royalties", "touchy", "foundation", "easter", "eggs", "clip", "haters", "tweets", "sweats", "times", "stats", "bangers", "cloud", "tank", "sketch", "badminton", "vibes", "gym", "crash", "punk", "mythos", "channel", "piece", "road", "sterling", "troubles", "dark", "zing", "cold", "forcing", "cam", "drift", "hobbies", "dealer", "gay", "hobby", "weekend", "dolphin", "hustler", "hard", "earth", "coincidence", "control", "office"]
    
    def get_all_english_words(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        exclude_words = []
        return [word.lower() for word in self.get_all_english_words() if word.lower() in self.get_all_english_words() and len(word) > 2 and word not in exclude_words and word.lower() not in stopwords.words('english') and word.lower() not in stopwords.words('french')]

    def get_all_english_words(self):
        with open('words_alpha.txt') as word_file:
            valid_words = set(word_file.read().split())
        return valid_words

    def get_transcript(self):
        with open('transcripts.json', 'r', encoding='utf-8') as file:
            transcripts = json.load(file)
        return transcripts

    def print_most_frequent_words(self):
        print("Summary for all English words across all videos:")
        for word, frequency in self.all_words_frequency.most_common(5000):
            print(f"{word}: {frequency}")
    
    def print_video_most_frequent_words(self, transcript, video_name):
        print(f"Most frequent words in the transcript for video '{video_name}':")
        for word, frequency in transcript.most_common(5000):
            print(f"{word}: {frequency}")
        print('\n' + '-'*50 + '\n')

EnglishWords()
