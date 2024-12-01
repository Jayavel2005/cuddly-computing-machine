import requests

url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def generateMeaning(user_word):
    word_url = f"{url}{user_word}"
    response = requests.get(word_url)

    if not response.ok:
        print(f"Cannot find the word. HTTP Status Code: {response.status_code}")
        return None
    else:
        return response.json()

def displayMeaning(result):
    print("\n=== Dictionary Results ===\n")
    
    # Word and Phonetics
    print(f"Word: {result[0]['word']}")
    if 'phonetics' in result[0] and len(result[0]['phonetics']) > 0 and 'text' in result[0]['phonetics'][0]:
        print(f"Phonetic: {result[0]['phonetics'][0]['text']}")
    else:
        print("Phonetic: Not available")
    
    # Meanings and Definitions
    print("\nMeanings:\n")
    for meaning in result[0]['meanings']:
        print(f"Part of Speech: {meaning['partOfSpeech']}")
        print()  # Add a blank line for readability

        for definition in meaning['definitions']:
            print(f"  Definition: {definition['definition']}\n")
            
            if 'example' in definition:
                print(f"    Example: {definition['example']}\n")
            
            if 'synonyms' in definition and len(definition['synonyms']) > 0:
                print(f"    Synonyms: {', '.join(definition['synonyms'])}\n")
            
            print()  # Blank line between each definition set

        print("------------------------------------------------\n")  # Add a separator line after each part of speech

# Continuously prompt the user to input a word until 'exit' is typed
while True:
    word = input("\nEnter a word to look up its meaning (or type 'exit' to quit): ").strip()
    if word.lower() == 'exit':
        print("\nExiting the dictionary. Goodbye!")
        break

    result = generateMeaning(word)
    if result:
        displayMeaning(result)
    else:
        print("\nNo data available for the entered word.")
