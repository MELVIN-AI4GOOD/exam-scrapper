# exam-scrapper

## Obtenção de Texto a partir de PDF da Prova
1. Coloque a prova dentro da pasta `/exams`
2. No `main.py`, leia o arquivo pdf
```python
exam = get_exam(<exam_path>)
```
3. Extraia seu texto para uma string
```python
raw_txt = get_raw_text(exam)
```
4. Salve o texto na pasta `/raw_txts` 
```python
save_raw_text(<filename>, raw_txt)
```

## Separação das questões
1. Leia o texto bruto do txt:
```python
txt = get_raw_text("texto_bruto_enem")
```

2. Separe as questões
```python
questions = separate_questions(txt)
```

3. Separe os enunciados das alternativas
```python
statement, alternatives = separate_question_elements(question)
```
2. 