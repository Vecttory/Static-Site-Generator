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


def generate_page(file_path, template_path, dest_file_path):
    print(
        f"Generating page from {file_path} to {dest_file_path} using {template_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        md = file.read()

    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    html_node = markdown_to_html_node(md)
    html_content = html_node.to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)

    with open(dest_file_path, "w", encoding="utf-8") as f:
        f.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)
    for path in dirs:
        full_path = os.path.join(dir_path_content, path)
        if os.path.isfile(full_path):
            dest_path = os.path.join(dest_dir_path, "index.html")
            generate_page(full_path, template_path, dest_path)
        else:
            generate_pages_recursive(
                full_path, template_path, os.path.join(dest_dir_path, path))
