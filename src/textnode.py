from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = ""
    ITALIC_TEXT = "_"
    BOLD_TEXT = "**"
    CODE_TEXT = "`"
    LINK = "[]"
    IMAGES = "!"

class TextNode():

    def __init__(text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(textObject1,textObject2):
        if(textObject1 == textObject2):
            return True
        return False

    def __repr__():
        return f"{self.text} {self.text_type.value} {self.url}"


