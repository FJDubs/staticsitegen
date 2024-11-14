def markdown_to_blocks(markdown):
    lines = markdown.split('\n')
    lines.append('')
    blocks = []
    sub_block = []
    for l in lines:
        if l.strip() != '':
           sub_block.append(l.strip())
        else:
            if sub_block:
                blocks.append('\n'.join(sub_block).strip())
            sub_block = []
    return blocks