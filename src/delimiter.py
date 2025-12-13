from textnode import *

def text_to_textnodes(text):
    Node = [TextNode(text, TextType.TEXT)]
    Node = split_nodes_delimiter(Node,"`",TextType.CODE)
    Node = split_nodes_delimiter(Node,"**",TextType.BOLD)
    Node = split_nodes_delimiter(Node,"_",TextType.ITALIC)
    Node = split_nodes_image(Node)
    Node = split_nodes_link(Node)

    return Node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if(node.text_type != TextType.TEXT):
            new_nodes.append(node)
            continue
        split_node = []
        splitted = node.text.split(delimiter)
        
        if len(splitted) % 2 == 0:
            raise ValueError("invalid markdown, section not closed")
        for i in range(len(splitted)):
            if splitted[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(splitted[i],TextType.TEXT))
            else:
                split_node.append(TextNode(splitted[i],text_type))
            
        new_nodes.extend(split_node)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(image[0],TextType.IMAGE,image[1],))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if(node.text_type != TextType.TEXT):
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
           new_nodes.append(node)
           continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})",1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


