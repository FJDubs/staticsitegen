from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    heading_pattern = re.compile(r"^#{1,6} ")
    if re.match(heading_pattern, block):
        return BlockType.HEADING
    if len(block) >= 6:
        if block[:3] == "```" and block[-3:] == "```":
            return BlockType.CODE
    line_break = block.split("\n")
    quote_case = 0
    for line in line_break:
        if len(line) >= 1:
            if line[0] == ">":
                quote_case += 1
    if quote_case == len(line_break):
        return BlockType.QUOTE
    unordered_case = 0
    for line in line_break:
        if len(line) >= 3:
            if line[:2] == "* " or line[:2] == '- ':
                unordered_case += 1
    if unordered_case == len(line_break):
        return BlockType.ULIST
    order_case = 1
    for line in line_break:
        order_num_length = len(str(order_case))
        if len(line) >= 1:
            if line[0].isdigit():
                if len(line) >= order_num_length + 2 and int(line[:order_num_length]) == order_case and line[order_num_length:order_num_length + 2] == ". ":
                    order_case += 1  
    if order_case == len(line_break) + 1:
        return BlockType.OLIST
    return BlockType.PARAGRAPH