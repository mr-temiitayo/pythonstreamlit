import pdfcrowd

# Replace 'your_username' and 'your_api_key' with your Pdfcrowd credentials
username = 'your_username'
api_key = 'your_api_key'

# Create a Pdfcrowd client instance
client = pdfcrowd.Client(username, api_key)

# Specify the URL of the webpage you want to convert
url = 'http://example.com'

# Define the PDF file path where you want to save the result
pdf_file_path = 'output.pdf'

# Convert the webpage to PDF and save it
with open(pdf_file_path, 'wb') as pdf_file:
    client.convertUrlToFile(url, pdf_file)

print(f'PDF saved as {pdf_file_path}')
