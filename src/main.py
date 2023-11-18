from pypdf import PdfReader

DEFAULT_RAW_TXT_PATH = '../raw_txts'

def get_exam(exam_path: str) -> PdfReader:
    """Obtém o pdf da prova e converte-o em uma classe PdfReader

    Args:
        exam_path (str): caminho do arquivo

    Returns:
        PdfReader: classe PdfReader do pdf da prova
    """
    return PdfReader(exam_path)


def get_raw_text(exam: PdfReader) -> str:
    """Obtém texto bruto do arquivo pdf da prova

    Args:
        exam (PdfReader): prova

    Returns:
        str: texto bruto da prova inteira
    """
    pages_text = [page.extract_text() for page in exam.pages]
    raw_txt = "".join(pages_text)
    
    return raw_txt


def save_raw_text(exam_name: str, text: str) -> None:
    """Salva o texto bruto da prova em txt, na pasta /raw_txts

    Args:
        exam_name (str): nome da prova
        text (str): texto bruto do exame
    """
    file_extension = ".txt"
    full_path = DEFAULT_RAW_TXT_PATH + '/' + exam_name + file_extension
    
    f = open(full_path, "w")
    f.write(text)
    f.close()
    
    return


def main():
    print("MELVIN EXAM SCRAPPER")
    
    exam = get_exam("../exams/enem.pdf")
    raw_txt = get_raw_text(exam)
    save_raw_text("texto_bruto_enem", raw_txt)


if __name__ == "__main__":
    main()