# Isso converte o 'A'-'E' no início de linha de um .txt para 'A A'-'E E' para ficar um padrão fácil de detectar
# Achei uma alternativa melhor, mas vou deixar aqui

def padronize_answer_pattern():
    # Abre o arquivo para leitura
    with open('../raw_txts/2019_enem_1_dia.txt', 'r', encoding='utf-8') as file:
        # Lê o conteúdo do arquivo
        content = file.read()

    # Divide o conteúdo em linhas
    lines = content.split('\n')

    # Lista de letras para mapear
    letras = ['A', 'B', 'C', 'D', 'E']

    # Itera sobre as linhas e modifica o padrão de alternativas
    for i in range(len(lines)):
        # Verifica se a linha começa com uma letra (alternativa) seguida por espaço
        if any([lines[i].strip().startswith(letra + ' ') or lines[i].startswith(letra + ' ') for letra in letras]):
            # Adiciona a letra duas vezes
            lines[i] = lines[i][:2] + lines[i][:2] + lines[i][2:]

    # Junta as linhas modificadas de volta em um único texto
    modified_content = '\n'.join(lines)

    # Abre o arquivo para escrita e escreve o conteúdo modificado
    with open('modded_txt.txt', 'w', encoding='utf-8') as file:
        file.write(modified_content)
        
if __name__ == '__main__':
    padronize_answer_pattern()