from htmlnode import *
from textnode import *
from static_generator import *

# wait shoot what did i just delete
def main(basepath):
    newtext = TextNode("This is some anchor text",TextType.LINK, "https://www.boot.dev")
    print(newtext)
    copyDirectories(f"{basepath}/static",f"{basepath}/public")
    generate_pages_recursive(f"{basepath}/content",f"{basepath}/template.html",f"{basepath}/docs")

main()

    

