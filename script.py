from markdownify import MarkdownConverter

class CustomMarkdownConverter(MarkdownConverter):
    def convert_pre(self, el, text, convert_as_inline):
        return 'pre';

    def convert_comment(self, el, text, convert_as_inline):
        # Remove the comment and any surrounding whitespace
        return ''


def convert_to_markdown(input_html: str) -> str:
    return CustomMarkdownConverter().convert(input_html)


def read_content_from_filename(input_filename: str) -> str:
       with open(input_filename, 'r', encoding='utf-8') as file:
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
    output_filename='output.txt'
    convert_txt_file_to_markdown(input_filename, output_filename)