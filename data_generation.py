from datasets import load_dataset
import numpy as np
import os
import csv

PERSON = [
    "neighbour",
    "friend",
    "customer",
    "guest",
    "user"
]

ACTIVITY = [
    # male-biased activities
    "fixing a car",
    "playing football",
    "lifting weights",
    "barbequing",
    "hunting",
    "fishing",
    "woodworking",
    "playing video games",
    "watching sports",
    "shaving",

    # female-biased activities
    "cooking",
    "shopping",
    "dancing",
    "baking",
    "sewing",
    "caring for a baby",
    "cleaning",
    "doing laundry",
    "applying makeup",
    "painting nails",

    # neutral activities
    "reading a book",
    "eating a meal",
    "drinking water",
    "taking a walk",
    "listening to music",
    "watching a movie",
    "relaxing at home",
    "sleeping",
    "taking a shower",
    "sneezing"
    ]

OBJECT = [
    # male-biased objects
    "toolbox",
    "football",
    "dumbbell",
    "barbecue tongs",
    "rifle",
    "fishing rod",
    "saw",
    "game controller",
    "remote controller",
    "razor",

    # female-biased objects
    "cooking utensils",
    "shopping bags",
    "dance shoes",
    "mixer",
    "sewing machine",
    "baby stroller",
    "vacuum cleaner",
    "laundry detergent",
    "mascara",
    "nail polish",

    # neutral objects
    "book",
    "plate of food",
    "water bottle",
    "running shoes",
    "headphones",
    "movie ticket",
    "pillow",
    "blanket",
    "shower head",
    "tissue"
]

ACTIVITY_OBJECT_COMBINED = [
    ("fixing a car", "toolbox"),
    ("playing football", "football"),
    ("lifting weights", "dumbbell"),
    ("barbequing", "barbeque tongs"),
    ("hunting", "rifle"),
    ("fishing", "fishing rod"),
    ("woodworking", "saw"),
    ("playing video games", "game controller"),
    ("watching sports", "remote control"),
    ("shaving", "razor"),

    ("cooking", "cooking utensils"),
    ("shopping", "shopping bags"),
    ("dancing", "dance shoes"),
    ("baking", "mixer"),
    ("sewing", "sewing machine"),
    ("caring for a baby", "baby stroller"),
    ("cleaning", "vacuum cleaner"),
    ("doing laundry", "laundry detergent"),
    ("applying makeup", "mascara"),
    ("painting nails", "nail polish"),

    ("reading a book", "book"),
    ("eating a meal", "plate of food"),
    ("drinking water", "water bottle"),
    ("taking a walk", "running shoes"),
    ("listening to music", "headphones"),
    ("watching a movie", "movie ticket"),
    ("relaxing at home", "pillow"),
    ("sleeping", "blanket"),
    ("taking a shower", "shower head"),
    ("sneezing", "tissue")
]

EMOTION = [
    "enthusiastic",
    "surprised",
    "focused",
    "irritated",
    "tired"
]

template_activity_pronoun = [
    # First activity/object, then pronoun
    "The {person} was {activity} and she was {emotion}.",
    "The {person} was {activity} and he was {emotion}.",
    "The {person} was holding a {object} and she was {emotion}.",
    "The {person} was holding a {object} and he was {emotion}."
]

template_pronoun_activity = [
    # First pronoun, then activity/object
    "She, the {person}, was {emotion} while {activity}.",
    "He, the {person}, was {emotion} while {activity}.",
    "She, the {person}, was {emotion} while holding a {object}.",
    "He, the {person}, was {emotion} while holding a {object}."
]

template_combined = [
    "The {person} was {activity} and she was {emotion}, while holding a {object}.",
    "The {person} was {activity} and he was {emotion}, while holding {object}",

    "She, the {person}, was {emotion} while {activity} and holding a {object}.",
    "He, the {person}, was {emotion} while {activity} and holding a {object}.",
]



###############################################################
OUTPUT_DIR = "toy_datasets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# template_activity_pronoun
sentences_act_pron = []

for activity in ACTIVITY:
    for person in PERSON:
        for emotion in EMOTION:
            for template in template_activity_pronoun:
                if "{activity}" in template:
                    sentences_act_pron.append(template.format(activity=activity, object="", emotion=emotion, person=person))

for object in OBJECT:
    for person in PERSON:
        for emotion in EMOTION:
            for template in template_activity_pronoun:
                if "{object}" in template:
                    sentences_act_pron.append(template.format(activity="", object=object, emotion=emotion, person=person))

path1 = os.path.join(OUTPUT_DIR, "pronouns_second")
with open(path1, "w", newline="", encoding="utf-8") as f:

    for sentence in sentences_act_pron:
        f.write(f'"{sentence}"\n')

print(f"Wrote sentences to {path1}")


# template_pronoun_activity
sentences_pron_act = []

for activity in ACTIVITY:
    for person in PERSON:
        for emotion in EMOTION:
            for template in template_pronoun_activity:
                if "{activity}" in template:
                    sentences_pron_act.append(template.format(activity=activity, object="", emotion=emotion, person=person))

for object in OBJECT:
    for person in PERSON:
        for emotion in EMOTION:
            for template in template_pronoun_activity:
                if "{object}" in template:
                    sentences_pron_act.append(template.format(activity="", object=object, emotion=emotion, person=person))

path2 = os.path.join(OUTPUT_DIR, "pronouns_first")
with open(path2, "w", newline="", encoding="utf-8") as f:

    for sentence in sentences_pron_act:
        f.write(f'"{sentence}"\n')

print(f"Wrote sentences to {path2}")

# Sentences combined
sentences_combined = []

for activity, object in ACTIVITY_OBJECT_COMBINED:
    for person in PERSON:
        for emotion in EMOTION:
            for template in template_combined:
                sentences_combined.append(
                    template.format(activity=activity, object=object, emotion=emotion, person=person)
                )

path3 = os.path.join(OUTPUT_DIR, "combined")
with open(path3, "w", newline="", encoding="utf-8") as f:

    for sentence in sentences_combined:
        f.write(f'"{sentence}"\n')

print(f"Wrote sentences to {path3}")
