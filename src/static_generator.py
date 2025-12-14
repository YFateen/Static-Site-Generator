from textnode import TextNode
from textnode import TextType
from htmlnode import *
import os
import shutil
from pathlib import Path
from markdown_block import *

def extract_title(markdown):
    #pull h1
    lines = markdown.split("\n")
    if not lines[0].startswith("#"):
        raise ValueError("Incorrect Format")
    stripped = lines[0].split("# ")
    if len(stripped) < 2:
        raise ValueError("Incorrect Format")
    return stripped[1]

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    files = os.listdir(dir_path_content)
    for file in files:
        if os.path.isfile(os.path.join(dir_path_content,file)):
            dest_path = Path(os.path.join(dest_dir_path,file)).with_suffix(".html")
            generate_page(os.path.join(dir_path_content,file),template_path,dest_path)
        else:
            generate_pages_recursive(os.path.join(dir_path_content,file),template_path,os.path.join(dest_dir_path,file))


def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    readedfromfile = open(from_path).read()
    readertemplatefile = open(template_path).read()
    markdown = markdown_to_html_node(readedfromfile).to_html()
    title = extract_title(readedfromfile)
    text1 = readertemplatefile.replace("{{ Title }}", title)
    text2 = text1.replace("{{ Content }}", markdown)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    newFile = open(dest_path,"w")
    newFile.write(text2)



def copyDirectories(startDirectory, copyTo):
    staticDirItems = os.listdir(startDirectory)
    if os.path.isdir(copyTo):
        shutil.rmtree(copyTo)
    os.mkdir(copyTo)
    for item in staticDirItems:
        newItemPath = startDirectory + "/" + item
        
        if os.path.isdir(newItemPath):
            newCopyPath = copyTo + "/" + item
            copyDirectories(newItemPath,newCopyPath)
        if os.path.isfile(newItemPath):
            shutil.copy(newItemPath,copyTo)
    


