from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for n in old_nodes:
        old_text_type = n.text_type
        delimiter_split = n.text.split(delimiter)
        i = 0
        for ds in delimiter_split:
            if ds == '':
                i += 1
            else:
                if i % 2 == 0:
                    new_nodes.append(TextNode(ds, old_text_type))
                    i += 1
                else:
                    new_nodes.append(TextNode(ds, text_type))
                    i += 1
    return new_nodes