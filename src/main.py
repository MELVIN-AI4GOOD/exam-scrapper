from pypdf import PdfReader

def get_exam(exam_path: str) -> PdfReader:
    """Obtém o pdf da prova e converte-o em uma classe PdfReader

    Args:
        exam_path (str): caminho do arquivo

    Returns:
        PdfReader: classe PdfReader do pdf da prova
    """
    return PdfReader(exam_path)


def get_raw_text(exam: PdfReader) -> [str]:
    """Obtém texto bruto do arquivo pdf da prova, separado por página

    Args:
        exam (PdfReader): prova

    Returns:
        [str]: textos brutos de de cada página (lista)
    """
    pages_text = [page.extract_text() for page in exam.pages]
    
    return pages_text


def main():
    print("MELVIN EXAM SCRAPPER")
    
    exam = get_exam("../exams/enem.pdf")
    raw_txt = get_raw_text(exam)


if __name__ == "__main__":
    main()