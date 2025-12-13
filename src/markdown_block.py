from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    splitted = markdown.split("\n\n")
    filteredList = []
    for string in splitted:
        if string == "":
            continue
        string = string.strip()
        filteredList.append(string)
    return filteredList
