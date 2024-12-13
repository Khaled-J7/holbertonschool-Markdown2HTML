#!/usr/bin/python3
"""
markdown2html.py

A script to convert a Markdown file (README.md) into an HTML file (README.html).
Supports headings and basic paragraph conversion.
"""

import sys
import os

# Function to handle heading tags

def heading_parse(index, lines_read_list):
    """
    Parse lines to convert Markdown headings (#) into HTML heading tags (e.g., <h1>, <h2>).

    Args:
        index (int): The current line index.
        lines_read_list (list): List of lines read from the input Markdown file.

    Returns:
        tuple: Updated index and list of HTML strings for headings.
    """
    count_heading = 0
    list_heading = []
    min_level = 1
    max_level = 6

    while index < len(lines_read_list):
        if lines_read_list[index][0] != '#':
            break

        data = lines_read_list[index].strip()
        heading_level = len(data) - len(data.lstrip('#'))

        if min_level <= heading_level <= max_level:
            string_to_parsing = data.lstrip("#").strip()
            list_heading.append(f'<h{heading_level}>{string_to_parsing}</h{heading_level}>\n')

        index += 1

    return (index, list_heading)

# Dictionary for mapping Markdown syntax to parsing functions
function_parsing = {
    '#': heading_parse,
}

if __name__ == '__main__':
    """
    Main entry point for the script.
    Handles command-line arguments and performs the Markdown to HTML conversion.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    try:
        html_tag_list = []  # List to hold the generated HTML content
        input_file = sys.argv[1]  # Input Markdown file
        output_file = sys.argv[2]  # Output HTML file

        # Read the input Markdown file
        with open(input_file, 'r') as f:
            lines_read_list = f.readlines()
            index = 0

            # Process each line in the Markdown file
            while index < len(lines_read_list):
                line = lines_read_list[index].strip()
                first_char = line[0]

                if first_char in function_parsing.keys():
                    # Parse using the corresponding function
                    index, html_tags = function_parsing[first_char](index, lines_read_list)
                else:
                    # Default to paragraph handling
                    html_tags = [f'<p>{line}</p>\n']
                    index += 1

                html_tag_list.extend(html_tags)

        # Write the generated HTML content to the output file
        with open(output_file, 'w') as f:
            for html_line in html_tag_list:
                f.write(html_line)

        print(f"Conversion successful: {input_file} -> {output_file}")
        sys.exit(0)

    except FileNotFoundError:
        sys.stderr.write(f"Error: Missing file {sys.argv[1]}\n")
        sys.exit(1)
