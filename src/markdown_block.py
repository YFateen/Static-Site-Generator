from enum import Enum
from htmlnode import *
from textnode import *
from delimiter import *

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        HTMLnode = text_node_to_html_node(node)
        children.append(HTMLnode)
    return children

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_HTML(block)
    if block_type == BlockType.CODE:
        return code_to_HTML(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ul_to_HTML(block)
    if block_type == BlockType.QUOTE:
        return quote_to_HTML(block)
    if block_type == BlockType.ORDERED_LIST:
        return ol_to_HTML(block)
    if block_type == BlockType.HEADING:
        return heading_to_HTML(block)
    raise ValueError("Invalid BlockType")

def paragraph_to_HTML(text):
    lines = text.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p",children)

def heading_to_HTML(text):
    currentChar = 0
    for char in text:
        if char == "#":
            currentChar += 1
        else:
            break
    if currentChar + 1 >= len(text):
        raise ValueError(f"invalid heading level: {currentChar}")
    text = text[currentChar + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{currentChar}", children)

def ul_to_HTML(text):
    items = text.split("\n")
    lines = []
    for item in items:
        itemtext = item[2:]
        children = text_to_children(itemtext)
        lines.append(ParentNode("li",children))
    return ParentNode("ul",lines)
def ol_to_HTML(text):
    items = text.split("\n")
    lines = []
    for item in items:
        itemtext = item[3:]
        children = text_to_children(itemtext)
        lines.append(ParentNode("li",children))
    return ParentNode("ol", lines)

def quote_to_HTML(text):
    lines = text.split("\n")
    totalLines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid Quote Block")
        totalLines.append(line.lstrip(">").strip())
    paragraph = " ".join(totalLines)
    children = text_to_children(paragraph)
    return ParentNode("blockquote", children)


def code_to_HTML(text):
    if not text.startswith("```") or not text.endswith("```"):
        raise ValueError("invalid code block")
    text_block = text[4:-3]
    text_from_block = TextNode(text_block, TextType.TEXT)
    child = text_node_to_html_node(text_from_block)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])



def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i+=1
        return BlockType.ORDERED_LIST

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
