from markdownify import MarkdownConverter
from typing import List

class CustomMarkdownConverter(MarkdownConverter):
    def convert_pre(self, el, text, convert_as_inline):
        language = el.get('data-enlighter-language', 'text')
        code_block = f"```{language}\n{text}\n```"
        return code_block


def convert_to_markdown(input_html: str) -> str:
    return CustomMarkdownConverter().convert(input_html)


def read_content_from_filename(input_filename: str) -> str:
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if not line.strip().startswith('<!--')]

    with open(intermediate_filename, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)

    with open(intermediate_filename, 'r', encoding='utf-8') as file:
        return file.read()
       
def save_markdown(markdown_content: str, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write(markdown_content)


def convert_txt_file_to_markdown(input_filename: str, output_filename: str) -> None:
    html = read_content_from_filename(input_filename)
    markdown_content = convert_to_markdown(html)
    save_markdown(markdown_content, output_filename)


if __name__ == '__main__':
    input_filename='markdown.txt'
    intermediate_filename='intermediate.txt'
    output_filename='output.md'
    convert_txt_file_to_markdown(input_filename, output_filename)