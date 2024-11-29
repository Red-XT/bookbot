def sort_on(dict):
     return dict["num"]

def sort_dict(dict):
    char_list = []
    for character, count in dict.items():
        char_info = {"char" : character , "num" : count}
        char_list.append(char_info)
    return char_list

def counting_characters(text):
     character_count = {}
     for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
             character_count[character] = 1
     return character_count

def count_words(text):
        return len(text.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    total_words = count_words(file_contents)
    total_characters = counting_characters(file_contents)
    char_list = sort_dict(total_characters)

    char_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    for char_info in char_list:
         if char_info["char"].isalpha():
            print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
