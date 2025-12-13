from textnode import TextNode
from textnode import TextType

def main():
    newtext = TextNode("This is some anchor text",TextType.LINK, "https://www.boot.dev")
    print(newtext)

main()
