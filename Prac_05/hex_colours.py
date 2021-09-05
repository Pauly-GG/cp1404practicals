HEX_CODES = {"alice blue": "#f0f8ff", "antiquewhite": "#faebd7", "black": "#000000",
             "blanchedalmond": "#ffebcd", "azure1": "#f0ffff",
             "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
             "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

colour_name = input("Enter a colour name: ").capitalize()
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, HEX_CODES.get(colour_name)))
colour_name = input("Enter a colour name: ")
