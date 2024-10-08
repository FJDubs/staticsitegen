from extractmarkdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    for on in old_nodes:
        images = extract_markdown_images(on.text)
        remaining_text = on.text
        for i in images:
            image_str = f'![{i[0]}]({i[1]})'
            text_split = remaining_text.split(image_str, 1)
            if text_split[0] == '':
                new_nodes.append(TextNode(i[0], 'image', i[1]))
            else:
                new_nodes.append(TextNode(text_split[0], on.text_type))
                new_nodes.append(TextNode(i[0], 'image', i[1]))
            remaining_text = text_split[-1]
        if remaining_text != '':
            new_nodes.append(TextNode(remaining_text, on.text_type))

    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for on in old_nodes:
        links = extract_markdown_links(on.text)
        remaining_text = on.text
        for l in links:
            link_string = f'[{l[0]}]({l[1]})'
            text_split = remaining_text.split(link_string, 1)
            if text_split[0] == '':
                new_nodes.append(TextNode(l[0], 'link', l[1]))
            else:
                new_nodes.append(TextNode(text_split[0], on.text_type))
                new_nodes.append(TextNode(l[0], 'link', l[1]))
            remaining_text = text_split[-1]
        if remaining_text != '':
            new_nodes.append(TextNode(remaining_text, on.text_type))
            
    return new_nodes