import gdown
import os
import yaml

EXAMS_PATH = '../exams'
EXAMS_CONF_PATH = '../conf/exams.yaml'

def download_enem_exams(exams: dict) -> None:
    """Baixa todas as provas do enem, da pasta do drive

    Args:
        exams (dict): dicionário, com informações da prova
    """
    for exam in exams:
        name, year, edition = exam['exam'], exam['year'], exam['edition']
        exam_url, answer_sheet_url = exam['exam_url'], exam['answer_sheet_url']
        
        # download da prova
        exam_name = f'{name} {year} {edition}'
        download_file(exam_url, exam_name)
        
        # download do gabarito
        answer_sheet_name = f'{exam_name} (gabarito)'
        download_file(answer_sheet_url, answer_sheet_name)
        

def download_file(file_id: str, file_name: str):
    """Baixa uma prova do google drive e salva na pasta /exams

    Args:
        file_id (str): id fo arquivo do drive
        file_name (str): nome do arquivo
    """
    url = f'https://drive.google.com/uc?id={file_id}'
    full_path = f'{EXAMS_PATH}/{file_name}.pdf'
    
    if os.path.isfile(full_path) == False:
        gdown.download(url, full_path, quiet=False)

    return


def main():
    with open(EXAMS_CONF_PATH) as config_file:
        data = yaml.safe_load(config_file)
    
    download_enem_exams(data['enem_exams'])
    

if __name__ == '__main__':
    main()