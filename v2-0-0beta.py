"""
2025 © Sigmapages: MIT License, CC BY-NC 4.0 License
"""
matrix = {            
    "1": "a",            
    "2": "b",            
    "3": "c",            
    "4": "d",            
    "5": "e",            
    "6": "f",
    "7" : "g",
    "8": "h",
    "9": "i",
    "10": "j",
    "11": "k",
    "12": "l",
    "13": "m",
    "14": "n",
    "15": "o",
    "29": " "  
}            

upper = False

guide_text = """
TS Computing Beta Guide:

- Keys 1-15: a-z
- 27: Shift (Upper for next character)
- 28: Backspace (remove last character)
- 100: Guide (show this message)
- 29: Space
- 99: Code Table
- 0: Exit

Example: 1 2 27 3 -> a b C
"""
code_table = """
1 = a, 2 = b, 3 = c, 4 = d, 5 = e, 6 = f, 7 = g, 8 = h, 9 = i, 10 = j, 11 = k, 12 = l, 13 = m, 14 = n, 15 = o
"""

while True:
    user_input = input("Enter keys (1-15, 27=Shift, 28=Backspace, 100=Guide, 0=Exit, 29=Space, 99=Code Table): ").strip()
    
    # Reset output_list mỗi lần nhập mới
    output_list = []

    text = user_input.split(" ")
    show_guide = False
    show_code = False

    for t in text:
        if t == "0":
            exit()
        elif t == "100": # Guide
            show_guide = True
        elif t == "27": # Shift
            upper = True
        elif t == "28": # Backspace
            if output_list:
                output_list.pop()
        elif t == "99":
            show_code = True
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
    elif show_code:
        print(code_table)
    else:
        print("".join(output_list))