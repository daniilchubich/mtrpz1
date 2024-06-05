def parse_markdown(markdown_text):
    html_text = ""
    in_paragraph = False
    in_code_block = False

    for line in markdown_text.split('\n'):
        if line.startswith('```'):
            in_code_block = not in_code_block
            if not in_code_block:
                html_text += "</pre>\n"
            else:
                html_text += "<pre>\n"
        elif in_code_block:
            html_text += line + '\n'
        elif line.strip():
            if not in_paragraph:
                html_text += "<p>"
                in_paragraph = True
            line = apply_formatting(line)
            html_text += line + ' '
        elif in_paragraph:
            html_text += "</p>\n"
            in_paragraph = False
        else: print("Помилка")    

    if in_paragraph:
        html_text += "</p>\n"

    if in_code_block:
        html_text += "</pre>\n"

    return html_text


def apply_formatting(text):
    text = apply_bold(text)
    text = apply_italic(text)
    text = apply_monospace(text)
    return text


def apply_bold(text):
    while '**' in text:
        if not  text[2] in "#*_`":
            text = text.replace('**', '<b>', 1)
            text = text.replace('**', '</b>', 1)     
    return text


def apply_italic(text):
    while '_' in text:
        if not  text[2] in "#*_`":
            text = text.replace('_', '<i>', 1)
            text = text.replace('_', '</i>', 1)
    return text


def apply_monospace(text):
    while '`' in text:
        if not  text[2] in "#*_`":
            text = text.replace('`', '<tt>', 1)
            text = text.replace('`', '</tt>', 1)
    return text

def main():
    print("Введіть назву файлу з контентом у форматі Markdown:")
    markdown_input = []
    while True:
        try:
            path = input()
            if path[len(path)-3:len(path)] == ".md":
                file = open(path, "r")
                #print(file.read())
                markdown_input = file.read()
                #print(markdown_text)
                html_output = parse_markdown(markdown_input)
                print(html_output)
                html(html_output)
            else: print("Incorrect markdown File")
        except EOFError:
            break
            
def html(string):
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Мій HTML-файл</title>
</head>
<body>
"""

    
    html_content += string + "\n"

    html_content += """</body>
</html>
"""
    create_html_file(html_content)    
def create_html_file(html_content, file_name="output.html"):
    #os.remove(file_name)
    with open(file_name, "w") as html_file:
        html_file.write(html_content)     
if __name__ == "__main__":
   main()

