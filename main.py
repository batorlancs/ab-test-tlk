import matplotlib.pyplot as plt
import numpy as np
from results import RESULTS

class Colors():
    GREEN = '#38c172'
    PURPLE = '#9561e2'
    LIGHT_PURPLE = '#b37feb'
    SLIGHT_PURPLE = '#d57feb'
    PINK = '#f66d9b'
    RED = '#e3342f'
    MEDIUM_RED = '#e53e3e'
    LIGHT_RED = '#f56565'
    LIGHTER_RED = '#f6adad'
    GRAY = '#808080'
    LIGHT_BLUE = '#4dc0b5'
    BLUE_VIOLET = '#3490dc'
    DARK_ORANGE = '#bf7126'
    ORANGE = '#f6993f'
    LIGHT_ORANGE = '#f6ad55'
    LIGHTER_ORANGE = '#f6c77f'
    YELLOW = '#ffed4a'
    
class ColorsOuter():
    RED = '#e3342f'
    GREEN = '#38c172'
    PURPLE = '#9561e2'
    YELLOW = '#ffed4a'
    ORANGE = '#f6993f'

THEMES = [
    # good response
    'jó válasz',
    # model difference, but good response
    'llama jobb',
    'search jobb',
    # bad response
    'nincs/rossz válasz, de jogi kérdés',
    'no response',
    'válasz és a link nem egyezik',
    # user hiba
    'nem jogi kérdés',
    'user hiba',
    # other backend bugs
    'egyéb bug',
]

GOOD = ['jó válasz']
BAD = ['nincs/rossz válasz, de jogi kérdés', 'no response', 'válasz és a link nem egyezik']
USER_ERROR = ['nem jogi kérdés', 'user hiba']
MODEL_DIFF = ['llama jobb', 'search jobb']
OTHER = ['egyéb bug']

# count the number of occurrences of each theme in RESULTS
print("-"*40)
for theme in THEMES:
    print(f"{theme}: {RESULTS.count(theme)}")
    
total_count = len(RESULTS)
good_answers_count = sum([RESULTS.count(g) for g in GOOD])
bad_answers_count = sum([RESULTS.count(b) for b in BAD])
user_error_count = sum([RESULTS.count(u) for u in USER_ERROR])
model_diff_count = sum([RESULTS.count(m) for m in MODEL_DIFF])
other_count = sum([RESULTS.count(o) for o in OTHER])

print("-"*40)
print(f"Total: {total_count}")
print(f"Good answers: {good_answers_count} ({good_answers_count/total_count:.2%})")
print(f"Bad answers: {bad_answers_count} ({bad_answers_count/total_count:.2%})")
print(f"Other: {other_count} ({other_count/total_count:.2%})")
print(f"Model difference: {model_diff_count} ({model_diff_count/total_count:.2%})")

# ----------------------------------------------------------------------------------------------------------------------
# make a pie chart showing each theme and their percentages
# ----------------------------------------------------------------------------------------------------------------------
theme_counts = [RESULTS.count(theme) for theme in THEMES]

plt.pie(
    theme_counts,
    labels=[
        "Jó válasz",
        "Llama jobb",
        "Search jobb",
        "Rossz válasz,\nde jogi kérdés",
        "Nincs válasz",
        "Válasz és a link\nnem egyezik",
        "Nem jogi kérdés",
        "Felhasználó hiba",
        "Egyéb hibák\n(pl. backend bug)"
    ],
    colors=[
        Colors.GREEN,  # "Jó válasz"
        Colors.PURPLE,  # "Llama jobb"
        Colors.LIGHT_PURPLE,  # "Search jobb"
        Colors.RED,  # "Rossz válasz, de jogi kérdés"
        Colors.LIGHT_RED,  # "Nincs válasz"
        Colors.LIGHTER_RED,  # "Válasz és a link nem egyezik"
        Colors.ORANGE,  # "Nem jogi kérdés"
        Colors.LIGHT_ORANGE,  # "Felhasználó hiba"
        Colors.YELLOW,   # "Egyéb hibák (pl. backend bug)"
    ],
    autopct='%1.1f%%',
    # textprops={'size': 'smaller'}
)
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# make a pie chart just showing the good and bad and other answers and their percentages
# ----------------------------------------------------------------------------------------------------------------------
fig, ax = plt.subplots()

size = 0.3
vals = np.array([
    [theme_counts[0], 0, 0],
    [theme_counts[1], theme_counts[2], 0],
    [theme_counts[3], theme_counts[4], theme_counts[5]],
    [theme_counts[6], theme_counts[7], 0],
    [theme_counts[8], 0, 0]
])

outer_colors = [ColorsOuter.GREEN, ColorsOuter.PURPLE, ColorsOuter.RED, ColorsOuter.ORANGE, ColorsOuter.YELLOW]
inner_colors = [
    Colors.GREEN, Colors.GREEN, Colors.GREEN,
    Colors.SLIGHT_PURPLE, Colors.LIGHT_PURPLE, Colors.LIGHT_PURPLE,
    Colors.LIGHT_RED, Colors.LIGHTER_RED, Colors.LIGHT_RED,
    Colors.LIGHT_ORANGE, Colors.LIGHTER_ORANGE, Colors.LIGHTER_ORANGE,
    Colors.YELLOW, Colors.YELLOW, Colors.YELLOW
]
outer_labels = [
    "Jó válasz",
    "Model különbség",
    "Rossz válasz",
    "Felhasználó hiba",
    "Egyéb hibák"
]

# inner_labels = [
#     "Jó válasz", " ", " ",
#     "Llama jobb", "Search jobb", " ",
#     "Rossz válasz, de jogi kérdés", "Nincs válasz", "Válasz és a link nem egyezik",
#     "Nem jogi kérdés", "Felhasználó hiba", " ",
#     "Egyéb hibák", " ", " "
# ]

inner_labels = [
    "Jó\nválasz", "", "",
    "Llama\njobb", "Search\njobb", "",
    "Rossz,\nde jogi kérdés", "Nincs\nválasz", "Link\nnem egyezik",
    "Nem jogi\nkérdés", "Felhasználó\nhiba", "",
    "Egyéb\nhibák", "", ""
]


print(len(inner_labels), len(inner_colors), len(vals.flatten()))

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors, labels=outer_labels, autopct='%1.1f%%', pctdistance=.85,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors, labels=inner_labels, textprops={'size': 7, 'horizontalalignment': 'center'}, labeldistance=.8,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Összesített eredmények')
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# make a pie chart for showing the good and bad and other answers and their percentages
# make two of these for each llama and search to compare them
# ----------------------------------------------------------------------------------------------------------------------

llama_good = ["llama jobb", "jó válasz"]
search_good = ["search jobb", "jó válasz"]

# llama
num_of_llama_good = sum([RESULTS.count(g) for g in llama_good])
num_of_llama_bad = sum([RESULTS.count(b) for b in BAD])
num_of_llama_other = sum([RESULTS.count(o) for o in OTHER])

# search
num_of_search_good = sum([RESULTS.count(g) for g in search_good])
num_of_search_bad = sum([RESULTS.count(b) for b in BAD])
num_of_search_other = sum([RESULTS.count(o) for o in OTHER])


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.pie(
    [num_of_llama_good, num_of_llama_bad, num_of_llama_other],
    labels=['Good Response', 'Bad Response', 'Other (e.g. backend bug)'],
    colors=[Colors.GREEN, Colors.MEDIUM_RED, Colors.YELLOW],
    autopct='%1.1f%%',
    textprops={'size': 'smaller'}
)
ax1.set_title('Llama Results')

ax2.pie(
    [num_of_search_good, num_of_search_bad, num_of_search_other],
    labels=['Good Response', 'Bad Response', 'Other (e.g. backend bug)'],
    colors=[Colors.GREEN, Colors.MEDIUM_RED, Colors.YELLOW],
    autopct='%1.1f%%',
    textprops={'size': 'smaller'}
)
ax2.set_title('Search Results')

plt.tight_layout()
plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# make a bar chart for showing the good and bad and other answers and their percentages
# make two of these for each llama and search to compare them
# ----------------------------------------------------------------------------------------------------------------------

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# ax1.bar(
#     ['Good Response', 'Bad Response', 'Other (e.g. backend bug)'],
#     [num_of_llama_good/total_count, num_of_llama_bad/total_count, num_of_llama_other/total_count],
#     color=[Colors.GREEN, Colors.MEDIUM_RED, Colors.YELLOW],

# )

# ax1.set_title('Llama Results')

# ax2.bar(
#     ['Good Response', 'Bad Response', 'Other (e.g. backend bug)'],
#     [num_of_search_good/total_count, num_of_search_bad/total_count, num_of_search_other/total_count],
#     color=[Colors.GREEN, Colors.MEDIUM_RED, Colors.YELLOW],

# )

# ax2.set_title('Search Results')

# plt.tight_layout()

# plt.show()
