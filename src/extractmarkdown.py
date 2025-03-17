import re

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_title(text):
    heading_pattern = re.compile(r"^# ")
    lines = text.split('\n')
    for line in lines:
        if re.match(heading_pattern, line):
            title = line[1:].strip()
            return title
        else:
            raise ValueError('No title found. Please provide a H1 heading ("# ").')