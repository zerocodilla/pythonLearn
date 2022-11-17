def pets_names(filename):
    """Read pets names from files."""
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        # print(f"Sorry, {filename} file is not found.")
        pass

filenames = ['horse.txt', 'cats.txt', 'dogs.txt']
for filename in filenames:
    pets_names(filename)