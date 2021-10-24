"""
Cleanup inconsistent song lyrics file names
"""
import os


def main():
    """Cleanup inconsistent song lyrics file names."""
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('Lyrics/Christmas')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for i, character in enumerate(filename):
        if i != 0:
            try:
                if character.islower() and filename[i - 1] == '_' or character.islower() and filename[i - 1] == ')':
                    new_name += character.upper()
                elif not new_name:
                    new_name += character.upper()
                else:
                    new_name += character
                if character.islower() and filename[i + 1].isupper():
                    new_name += '_'
                if character.islower() and filename[i + 1] == '(':
                    new_name += '_'
            except IndexError:
                pass
        return new_name


main()
