# Prompt for user input -> File name with extension
# Output file's media type for the following file types:
# .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# else return application/octet-stream

def file_extensions(file_name: str) -> str:
    if file_name.endswith('.txt'):
        return "text/plain"
    elif file_name.endswith('.gif'):
        return "image/gif"
    elif file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        return "image/jpeg"
    elif file_name.endswith('.png'):
        return "image/png"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

def main():
    file_name = input('File name: ').strip()
    print(file_extensions(file_name))

main()