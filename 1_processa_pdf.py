import os
from gera_imagens import generate_images, Parity

livros = [
    {
        "file_name": "CBO2002_Liv1.pdf",
        "first_page": 24,
        "last_page": 827,
        "output_filename": "1"
    },
    {
        "file_name": "CBO2002_Liv2.pdf",
        "first_page": 10,
        "last_page": 593,
        "output_filename": "2"
    }
]

output_folder = "tmp/"

def clear_tmp_folder(tmp_folder):
    for filename in os.listdir(tmp_folder):
        os.unlink(os.path.join(tmp_folder, filename))

for livro in livros:
    generate_images(pdf_path=livro['file_name'], first_page=livro['first_page'], last_page=livro['last_page'], output_file=f"{livro['output_filename']}-", output_folder=output_folder, parity=Parity.EVEN)
    generate_images(pdf_path=livro['file_name'], first_page=livro['first_page'], last_page=livro['last_page'], output_file=f"{livro['output_filename']}-", output_folder=output_folder, parity=Parity.ODD)