def main(): #This function check file Markdown
    print("Введіть текст у форматі Markdown (натисніть Ctrl + D або Ctrl + Z після введення для завершення):")
    markdown_input = []
    while True:
        try:
            path = input()
            if path[len(path)-3:len(path)] == ".md":
                file = open(path, "r")
                #print(file.read())
                markdown_input = file.read()
                #print(markdown_text)
            else: print("Incorrect markdown File")
        except EOFError:
            break
if __name__ == "__main__":
   main()