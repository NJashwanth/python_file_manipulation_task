import os
from bs4 import BeautifulSoup
import PyPDF2

# Reviewed By Jessica


# fetching file type
def get_file_type(file_path):
    # splitting file path
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == ".txt":
        return "text"
    elif file_extension == ".html":
        return "html"
    elif file_extension == ".pdf":
        return "pdf"
    else:
        return "Invalid File Type"

# reading File
def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except:
        print("Invalid Directory")


# reading PDF file
def read_pdf_file(file_path):
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except:
        print("Invalid Directory")



# writing Text File
def write_text_file(file_path, content):
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except:
        print("Invalid Directory")



#  Extract Text from HTML Data
def get_text_from_html(html_data):
    soup_parsed_data = BeautifulSoup(html_data, features="html.parser")
    return soup_parsed_data.get_text('\n')


# Manipulate Selected File
def manipulate():
    file_path = input("Please Enter File Path")
    file_type = get_file_type(str(file_path))
    file_name = os.path.splitext(file_path)[0]
    if file_type == 'text':
        text_contents = read_file(file_path)
        output_file_path = file_name + "_output" + ".csv"
        write_text_file(output_file_path, text_contents)
    elif file_type == 'pdf':
        text_contents = read_pdf_file(file_path)
        output_file_path = file_name + "_output" + ".txt"
        write_text_file(output_file_path, text_contents)
    elif file_type == 'html':
        html_content = read_file(file_path)
        text_content_from_html = get_text_from_html(html_content)
        output_file_path = file_name + "_output" + ".txt"
        write_text_file(output_file_path, text_content_from_html)


if __name__ == '__main__':
    manipulate()

# Sources :
#  opening file - https://www.w3schools.com/python/python_file_open.asp
#  html to text - https://stackoverflow.com/a/66690657/10256415
#  pdf to Text  - https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/

#  worked with Jessica and Shriya
