from pypdf import PdfReader

def get_exam(exam_path: str) -> PdfReader:
    """Obtém o pdf da prova e converte-o em uma classe PdfReader

    Args:
        exam_path (str): caminho do arquivo

    Returns:
        PdfReader: classe PdfReader do pdf da prova
    """
    return PdfReader(exam_path)


def main():
    print("MELVIN EXAM SCRAPPER")


if __name__ == "__main__":
    main()