def count_common_words(filename, word):
    """Count words in the file."""
    try:
        with open(filename, encoding='utf=8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} file is not found.")
    else:
        words = contents.lower().count(word)
        print(f"File contains {words} '{word}' words.")


filenames = ['missing_file.txt', 'twenty_years_after.txt', 'the_three_musketeers.txt', 'the_call_of_the_wild.txt']
for filename in filenames:
    count_common_words(filename, 'the ')

