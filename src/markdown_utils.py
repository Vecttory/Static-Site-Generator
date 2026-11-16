import os
import re
from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str):
    lines = markdown.splitlines()
    for line in lines:
        pattern = r"^# +[\S]+"
        stripped = line.strip()
        matches = re.findall(pattern, stripped)
        if matches:
            result = stripped.split("# ", 1)[1].strip()
            return result

    raise ValueError("Markdown missing a title (eg. '# My title')")


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as file:
        md = file.read()

    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    html_node = markdown_to_html_node(md)
    html_content = html_node.to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)

    dest_file_path = dest_path + "/index.html"
    print(dest_file_path)

    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)

    with open(dest_file_path, "w", encoding="utf-8") as f:
        f.write(template)
