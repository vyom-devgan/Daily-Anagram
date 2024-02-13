# Daily Anagram Generator

Anagram Generator is a Python tool designed to generate all possible anagrams of a given word and filter out meaningful words with definitions.

## Objective

The main objective of Anagram Generator is to provide a tool for generating meaningful words from an input word by finding all possible anagrams and filtering out those with definitions.

## Features

- Generates all possible anagrams of a given word.
- Filters out anagrams with definitions from WordNet.
- Simple and intuitive command-line interface.

## Usage

1. Run the Python script.
2. Input a word to generate anagrams.
3. View the generated anagrams with definitions.

## Implementation

- Utilizes Python's `requests`, `BeautifulSoup`, and `nltk` libraries.
- Fetches HTML content from a webpage to extract word of the day.
- Generates anagrams and checks for definitions using WordNet.
- Selects a random anagram word with a definition.

## Outcomes

- Provides users with meaningful words derived from the word of the day.
- Enhances vocabulary and word recognition skills.

## Limitations

- Requires an internet connection to fetch the word of the day.
- Relies on WordNet for word definitions, which may not cover all words.

Feel free to contribute to the project by forking the repository and submitting pull requests. Your feedback and suggestions are highly appreciated!
