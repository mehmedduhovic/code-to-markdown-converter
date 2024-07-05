def read_content_from_filename(input_filename: str) -> str:
       with open(input_filename, 'r', encoding='utf-8') as file:
        return file.read()

def convert_txt_file_to_markdown(input_filename: str, output_filename: str) -> None:
    html = read_content_from_filename(input_filename)
    print(html)


if __name__ == '__main__':
    input_filename='markdown.txt'
    output_filename='output.txt'
    convert_txt_file_to_markdown(input_filename, output_filename)