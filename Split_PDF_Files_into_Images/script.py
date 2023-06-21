from pdf2image import convert_from_path

pages = convert_from_path('test.pdf',500)

for num,page in enumerate(pages):
    page.save(str(num)+".jpg","JPEG")
