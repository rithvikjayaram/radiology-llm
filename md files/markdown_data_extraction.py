import markdown
import os
from lxml import html

def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
    return md_content

def extract_all_sections(md_content):
    html_content = markdown.markdown(md_content, extensions=['markdown.extensions.fenced_code'])
    root = html.fromstring(html_content)

    sections = {}
    current_section = None

    for element in root.iter():
        if element.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if element.text:
            	current_section = element.text.strip()  
            sections[current_section] = []
        elif current_section is not None and element.tag == 'p':
            if element.text_content():
            	sections[current_section].append(element.text_content().strip() )
	
    
    return (sections)

def process_md_files(input_folder, output_file):
    with open(output_file, 'a', encoding='utf-8') as output_file:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    print(f"Processing: {file_path}")

                    md_content = read_md_file(file_path)
                    all_sections = extract_all_sections(md_content)

                    # Write information to the output file
                    for section, content in all_sections.items():
                        output_file.write(f"{section}:\n{' '.join(content)}\n")
                        


process_md_files('/home/skartellex/markdown', 'output.txt')

    

    

