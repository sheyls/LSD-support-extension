from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def list_colors():
    # Sample dictionary of colors
    colors_dict = {
        "Red": "#FF0000",
        "Green": "#00FF00",
        "Blue": "#0000FF",
        "Yellow": "#FFFF00",
        "Magenta": "#FF00FF",
        "Cyan": "#00FFFF",
        "White": "#FFFFFF",
        "Black": "#000000",
        "Orange": "#FFA500",
        "Purple": "#800080",
        "Lime": "#00FF00",
        "Indigo": "#4B0082",
        "Gold": "#FFD700",
        "Pink": "#FFC0CB",
        "Teal": "#008080",
        "Lavender": "#E6E6FA",
        "Brown": "#A52A2A",
        "Beige": "#F5F5DC",
        "Maroon": "#800000",
        "Olive": "#808000"
    }

    print("Hexadecimal colors:")
    for color_name, hex_value in colors_dict.items():
        print(f"{color_name}: {hex_value}")
    print(f"Chech the hexadecimal colors at the pdf file at the Github repo.")

def display_info():
    print("Documentation & More Info:")
    print("   READ ME: https://github.com/sheyls/LSD-support-extension")
    print("    License: MIT LICENSE")

def list_types():
    """Lists various L-system types and their basic rules."""
    l_systems = {
        'Algae Growth': {
            'Axiom': 'A',
            'Rules': [
                'A => AB',
                'B => A'
            ]
        },
        'Dragon Curve': {
            'Axiom': 'FX',
            'Rules': [
                'X => X+YF+',
                'Y => -FX-Y'
            ]
        },
        'Sierpinski Triangle': {
            'Axiom': 'A',
            'Rules': [
                'A => B-A-B',
                'B => A+B+A'
            ]
        },
        'Hexagonal Gosper': {
            'Axiom': 'XF',
            'Rules': [
                'X => X+YF++YF-FX--FXFX-YF+',
                'Y => -FX+YFYF++YF+FX--FX-Y'
            ]
        },
        'Hilbert Curve': {
            'Axiom': 'A',
            'Rules': [
                'A => -BF+AFA+FB-',
                'B => +AF-BFB-FA+'
            ]
        }

    }

    for name, details in l_systems.items():
        print(f"lsys {name.replace(' ', '_').lower()}{{")
        print(f"    axiom : {details['Axiom']},")
        for rule in details['Rules']:
            print(f"    {rule},")
        print("};")
        print()  # For spacing

def main():
    lsd_completer = WordCompleter(['colors', 'info', 'types', 'exit'], ignore_case=True)

    print("LSD: Lindenmayer-System-Drawing CLI v1.0.0 \n ----- WELCOME :) ----- \n Type 'exit' to quit.")
    print("Commands:")
    print("colors: Hexadecimal colors ideas for your L-Systems.")
    print("types: L-system ideas for you <3)")
    print("info: Show documentation and more information about LSD")
    
    while True:
        user_input = prompt("LSD> ", completer=lsd_completer)
        
        if user_input == 'exit':
            break
        elif user_input == 'colors':
            list_colors()
        elif user_input == 'info':
            display_info()
        elif user_input == 'types':
            list_types()
        else:
            print(f"Unknown command: {user_input}")


if __name__ == "__main__":
    main()
