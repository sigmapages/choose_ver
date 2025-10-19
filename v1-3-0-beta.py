"""
Copyright © 2025 Sigmapages, Product: TS Computing, License: MIT, CC BY-NC 4.0
"""
matrix = {            
    "1": "a",            
    "2": "b",            
    "3": "c",            
    "4": "d",            
    "5": "e",            
    "6": "f",           
}            

upper = False

guide_text = """
TS Computing Beta Guide:

- Keys 1-6: a-z
- 27: Shift (Upper for next character)
- 28: Backspace (remove last character)
- 100: Guide (show this message)
- 0: Exit

Example: 1 2 27 3 -> a b C
"""

while True:
    user_input = input("Enter keys (1-6, 27=Shift, 28=Backspace, 100=Guide, 0=Exit, Separated by space): ").strip()
    
    # Reset output_list mỗi lần nhập mới
    output_list = []

    text = user_input.split(" ")
    show_guide = False

    for t in text:
        if t == "0":
            print("Thanks for the support, my main page: https://sigmapages.github.io/")
            exit()
        elif t == "100": # Guide
            show_guide = True
        elif t == "27": # Shift
            upper = True
        elif t == "28": # Backspace
            if output_list:
                output_list.pop()
        elif t in matrix:
            char = matrix[t]
            if upper:
                char = char.upper()
                upper = False
            output_list.append(char)
        else:
            print(f"Error: '{t}' is invalid")

    if show_guide:
        print(guide_text)
    else:
        print("".join(output_list))
