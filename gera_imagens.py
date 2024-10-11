import pdf2image
import tempfile
from enum import Enum
class Parity(Enum):
    ODD=2
    EVEN=1

def generate_images(
    pdf_path,
    first_page: int,
    last_page: int,
    output_file: str,
    output_folder: str | None = None,
    parity: Parity | None = None,
    step: int = 1,
    parity_step: int = 1
):
    if not output_folder:
        output_folder = tempfile.gettempdir()

    if parity:
        step = 2
        match parity:
            case Parity.ODD:
                first_page += parity_step
                last_page += parity_step
    else:
        parity = ""

    for page in range(first_page, last_page, step):
        pdf2image.convert_from_path(
            pdf_path,
            output_folder=output_folder,
            first_page=page,
            last_page=page,
            thread_count=12,
            use_cropbox=True,
            output_file=output_file
        )