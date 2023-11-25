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


def scrappe_enem(year):
    exams_filenames = [
        f'{year}_enem_1_dia',
        f'{year}_enem_1_dia_gabarito',
        f'{year}_enem_2_dia',
        f'{year}_enem_2_dia_gabarito',
    ]
    
    exams_paths = [f'../exams/{exam_filename}.pdf' for exam_filename in exams_filenames]
    
    exams = [get_exam(exam_path) for exam_path in exams_paths]
    
    raw_txts = [get_raw_text(exam) for exam in exams]
    
    for i in range(4):
        save_raw_text(f'{exams_filenames[i]}', raw_txts[i])
        

def main():
    print("MELVIN EXAM SCRAPPER")
    enem_editions = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    
    for enem_edition in enem_editions:
        scrappe_enem(enem_edition)


if __name__ == "__main__":
    main()