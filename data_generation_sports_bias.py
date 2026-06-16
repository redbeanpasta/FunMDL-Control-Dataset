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

ACTIVITIES = [
    # male-biased sports
    {"activity": "playing rugby", "bias": "M"},
    {"activity": "playing ice hockey", "bias": "M"},
    {"activity": "racing with a motor cycle", "bias": "M"},
    {"activity": "kick-boxing", "bias": "M"},
    {"activity": "body building", "bias": "M"},
    {"activity": "playing soccer", "bias": "M"},
    {"activity": "playing petanque", "bias": "M"},
    {"activity": "playing water polo", "bias": "M"},
    {"activity": "cycling", "bias": "M"},
    {"activity": "rowing", "bias": "M"},
    {"activity": "mountain biking", "bias": "M"},
    {"activity": "doing aikido", "bias": "M"},
    {"activity": "doing tae kwon do", "bias": "M"},
    {"activity": "shooting", "bias": "M"},
    {"activity": "playing golf", "bias": "M"},
    {"activity": "canoeing", "bias": "M"},
    {"activity": "doing judo", "bias": "M"},

    # female-biased activities
    {"activity": "doing synchronized swimming", "bias": "F"},
    {"activity": "doing fitness exercises", "bias": "F"},
    {"activity": "dancing", "bias": "F"},
    {"activity": "twirling a baton", "bias": "F"},
    {"activity": "doing gymnastics", "bias": "F"},
    {"activity": "horse-riding", "bias": "F"},

    # neutral activities
    {"activity": "playing badminton", "bias": "N"},
    {"activity": "swimming", "bias": "N"},
    {"activity": "playing volleyball", "bias": "N"},
    {"activity": "skiing", "bias": "N"},
    {"activity": "playing tennis", "bias": "N"},
    {"activity": "doing athletics", "bias": "N"},
    {"activity": "roller skating", "bias": "N"},
    {"activity": "riding", "bias": "N"},
    {"activity": "orienteering", "bias": "N"},
    {"activity": "fencing", "bias": "N"},
    {"activity": "playing table tennis", "bias": "N"},
    {"activity": "climbing", "bias": "N"},
    {"activity": "playing handball", "bias": "N"},
    {"activity": "sailing", "bias": "N"},
    {"activity": "playing basketball", "bias": "N"},
    {"activity": "doing archery", "bias": "N"}
    ]


template_activity_pronoun = [
    # First activity/object, then pronoun
    "The {person} was {activity} and she continued.",
    "The {person} was {activity} and he continued.",
]

template_pronoun_activity = [
    # First pronoun, then activity/object
    "She, the {person}, was {activity}.",
    "He, the {person}, was {activity}.",
]



###############################################################
OUTPUT_DIR = "toy_datasets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# template_activity_pronoun
sentences_act_pron = []

for act in ACTIVITIES:
    for person in PERSON:
        activity = act["activity"]
        bias = act["bias"]
        sentence_F = template_activity_pronoun[0].format(activity=activity, person=person)
        sentence_M = template_activity_pronoun[1].format(activity=activity, person=person)

        sentences_act_pron.append({
            "sentence": sentence_F,
            "pronoun_original": "F",
            "activity": activity,
            "bias": bias
        })

        sentences_act_pron.append({
            "sentence": sentence_M,
            "pronoun_original": "M",
            "activity": activity,
            "bias": bias
        })

path1 = os.path.join(OUTPUT_DIR, "pronouns_second.csv")
with open(path1, "w", newline="", encoding="utf-8") as f:

    writer = csv.DictWriter(f, fieldnames=["sentence", "pronoun_original", "activity", "bias"])
    writer.writeheader()
    writer.writerows(sentences_act_pron)

print(f"Wrote sentences to {path1}")


# template_pronoun_activity
sentences_pron_act = []

for act in ACTIVITIES:
    for person in PERSON:
        activity = act["activity"]
        bias = act["bias"]
        sentence_F = template_pronoun_activity[0].format(activity=activity, person=person)
        sentence_M = template_pronoun_activity[1].format(activity=activity, person=person)

        sentences_pron_act.append({
            "sentence": sentence_F,
            "pronoun_original": "F",
            "activity": activity,
            "bias": bias
        })

        sentences_pron_act.append({
            "sentence": sentence_M,
            "pronoun_original": "M",
            "activity": activity,
            "bias": bias
        })

path2 = os.path.join(OUTPUT_DIR, "pronouns_first.csv")
with open(path2, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["sentence", "pronoun_original", "activity", "bias"])
    writer.writeheader()
    writer.writerows(sentences_pron_act)

print(f"Wrote sentences to {path2}")
