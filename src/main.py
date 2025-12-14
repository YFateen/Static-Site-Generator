from htmlnode import *
from textnode import *
from static_generator import *

# wait shoot what did i just delete
def main():
    newtext = TextNode("This is some anchor text",TextType.LINK, "https://www.boot.dev")
    print(newtext)
    copyDirectories("./static","./public")
    generate_pages_recursive("./content","./template.html","./public")

main()

    

