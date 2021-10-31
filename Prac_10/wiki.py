"""
CP1404/CP5632 Practical
A Wikipedia search program using the Wikipedia API
"""

import wikipedia

title_of_page = input('>>>')
while title_of_page != "":
    try:
        current_page = wikipedia.page(title_of_page, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as choose:
        print(title_of_page.title, title_of_page.summary, title_of_page.url)
    title_of_page = input('>>>')