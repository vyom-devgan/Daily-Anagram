import random
import requests
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
from typing import List, Tuple

def all_anagrams(word: str, current_anagram: str = '', anagrams: List[str] = []) -> List[str]:
    """
    Generates all possible anagrams of a given word.
    Returns a list of anagrams.
    """
    if len(word) == 0:
        if current_anagram not in anagrams:
            anagrams.append(current_anagram)
        return anagrams

    for i in range(len(word)):
        new_word = word[:i] + word[i + 1:]
        new_anagram = current_anagram + word[i]
        all_anagrams(new_word, new_anagram, anagrams)
        all_anagrams(word[i + 1:], current_anagram, anagrams)

    return anagrams

def def_checker(word: str) -> bool:
    """
    Checks if a word has a definition in WordNet.
    Returns True if a definition is found, False otherwise.
    """
    synsets = wordnet.synsets(word)
    return bool(synsets)

def fetch_webpage(url: str) -> str:
    """
    Fetches the webpage content from the given URL.
    Returns the HTML content as a string.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return ""

def gather_information_title(html_content: str) -> str:
    """
    Parses the HTML content to extract the title of the webpage.
    Returns the title as a string.
    """
    title = ""
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.text.strip()
    return title

def word_finalizer(anagram: str) -> Tuple[int, str]:
    """
    Generates the length and definition of the given anagram.
    Returns a tuple containing length and definition.
    """
    syn = wordnet.synsets(anagram)[0]
    return (len(anagram), syn.definition())

def words_finder(anagrams: List[str]) -> List[str]:
    """
    Generates all anagrams that have definitions and are at least 3 letters long.
    Returns a list of defined words longer than 3 letters.
    """
    defined_list = []
    for anagram in anagrams:
        if def_checker(anagram) and len(anagram) > 2:
            defined_list.append(anagram)
    return defined_list

if __name__ == "__main__":
    url = 'https://www.merriam-webster.com/word-of-the-day'
    html_content = fetch_webpage(url)
    title = gather_information_title(html_content)
    daily_word = title.split()[4]  # Extracting the 5th word from the title
    print("Daily Word:", daily_word)
    anagrams = all_anagrams(daily_word.lower())
    usable_words = words_finder(anagrams)
    ANAGRAM_WORD = random.choice(usable_words)
    print("Randomly chosen anagram word:", ANAGRAM_WORD)
    print(word_finalizer(ANAGRAM_WORD))