from get_text import get_text

text = get_text('LDPD001992_2018.docx', )
file = open('result.txt','w', encoding='utf-8')
file.write(text)