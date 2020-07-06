from django.apps import AppConfig


class DesignerConfig(AppConfig):
    name = 'designer'



# text = 'РїСЂРѕРѕРІРµСЂРєР°'
#
# print(text)
# print(text.encode('windows-1251').decode('utf8'))


# text = '\321\202\320\265\321\201\321\202123903\320\263023\320\276\320\272023\320\272'
# text2 = 'ÑÐµÑÑ123903Ð³023Ð¾Ðº023Ðº'
# windows-1252
# print(text.encode('latin1').decode('utf8'))


# text = '��������'
# print(text)
# text = text.encode('latin').decode('utf8')
# print(text)
#
#
# text = '%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582'
# print(text)
# text = text.encode('windows-1252').decode('utf8')
# print(text)


import urllib.parse


# text = urllib.parse.unquote_plus("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# text = urllib.parse.unquote_to_bytes(str("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582"))
# text = urllib.parse.unquote("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# text = urllib.parse.unquote_plus("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# text = urllib.parse.quote("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# text = urllib.parse.quote_plus("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# text = urllib.parse.quote_plus("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")

# text = urllib.parse.unquote("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# print(text)
# # text = urllib.parse.quote_from_bytes(b"%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# text = urllib.parse.parse_qsl(b"%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# print(text)

#
# import urllib.parse.unquote
# data = [("n", "1"), ("n", "3"), ("n", "4"), ("button", "Привет"), ]
# enc_data = urllib.parse.urlencode(data)
# print(enc_data)
# '%d0%a2%d0%b5%d1%81%d1%82'
#
# enc_data = urllib.parse.unquote('%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582')
# # # print(enc_data)
#
# from urllib.parse import unquote
# # s = '%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582'
# # s = '%2525d0%2525a2%2525d0%2525b5%2525d1%252581%2525d1%252582'
# # print(s)
# to_decode = '%2525d0%2525bc%2525d0%2525b0%2525d0%2525b2%2525d0%2525bc%2525d0%2525b2%2525d0%2525b0'
# print(to_decode)
# to_decode = unquote(to_decode)
# print(to_decode)
# to_decode = unquote(to_decode)
# print(to_decode)
#
# to_decode = unquote(to_decode)
# print(to_decode)
#



# print(text.encode('latin1').decode('windows-1252'))

# text = urllib.parse.unquote("%25d0%25a2%25d0%25b5%25d1%2581%25d1%2582")
# print(text)

 #
# a = "%25d1%2582%25d0%25b5%25d1%2581%25d1%2582_%25d1%2580%25d0%25b5%25d0%25b3%25d1%2580%25d1%2583"
# b = "\321\202\320\265\321\201\321\202123903\320\263023\320\276\320\272023\320\272"
# b = b.encode('windows-1251').decode('utf8')
# # c = bytes(b)
# print(a)
# print(a.encode('latin1').decode('utf8'))
# print(b)
# print(b)


# import urllib.parse
#
# question = '\25d1\2582\25d0\25b5\25d1\2581\25d1\2582\2520\25d1\2580\25d0\25b5\25d0\25b3\25d1\2580\25d1\2583'
# print(question.encode('latin1').decode('utf8'))
# чтобы вычленить текст вопроса
# разбейте строку по знаку =, и возьмите
# второй элемент получившегося списка

 # сохраните его в переменной question

# напечатайте на экран запрос в расшифрованном виде
# print(urllib.parse.unquote(question))  # ваш код здесь
# print(urllib.parse.unquote(question))  # ваш код здесь
# print(urllib.parse.unquote(question))  # ваш код здесь
# print(urllib.parse.unquote(question))  # ваш код здесь

#
# with open('text.txt', 'a', encoding='utf-8') as f:
#     print('fff')
#     f.write('adasdasdasfassfc вымывмывмывм\n')
#     f.write('adasdasdasfassfc вымывмывмывм\n')
#     f.write('adasdasdasfassfc вымывмывмывм\n')
#
#
# with open('text.txt', 'a', encoding='utf-8') as f:
#     print('fff')
#     f.write('adasdasdasfassfc вымывмывмывм\n')
#     f.write('adasdasdasfassfc вымывмывмывм\n')
#     f.write('adasdasdasfassfc вымывмывмывм\n')
#
# logi = []
# with open('text.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         logi.append(line)
#         # parts = line.split()
#
# print(logi)

#
# a = "мир".encode('utf-8')
# print('a', a)
# a_enc = b'\xd0\xbc\xd0\xb8\xd1\x80'
# print('a_enc', a_enc)
#
# b = "мир".encode('cp1251')
# print('b', b)
# b_enc = b'\xec\xe8\xf0'.decode('utf8')
# print('b_enc', b_enc)
#
# c = "мир".encode('cp866')
# print('c', c)
# c_enc = b'\xac\xa8\xe0'.decode('utf8')
# print('c_enc', c_enc)
#
# d = "мир".encode('koi8-r')
# print('d', d)
# d_enc = b'\xcd\xc9\xd2'.decode('utf8')
# print('d_enc', d_enc)


#
# text = '\xd0\xa2\xd0\xb5\xd1\x81\xd1\x82'
# print(text)
#
# text = text.encode('cp1251').decode('utf8')
# print(text)


# text = '\xd0\xa2\xd0\xb5\xd1\x81\xd1\x82'
# print(text.encode('latin1').decode('utf8'))
# #
# text = '\xd0\xb2\xd0\xb0\xd1\x8b\xd0\xb2\xd0\xb0\xd1\x8b\xd0\xb2'
# text = text.encode('latin1').decode('utf8')
# print(text)
#
# text = '\xd0\xa2\xd0\xb5\xd1\x81\xd1\x82'
# text = text.encode('latin1').decode('utf8')
# print(text)


dic = {'room': ['\xd0\x97\xd0\xb0\xd0\xbb'], 'product_name': ['\xd0\x9f\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb0'],
       'link': ['http://127.0.0.1:8000/designer/newproject'], 'unit': ['\xd1\x88\xd1\x82'],
       'retail_price': ['5646'], 'qty': ['231'], 'file_3dmax': [''], 'file_revit': [''],
       'file_technical_instruction': ['']}

print(str('\xd0\x97\xd0\xb0\xd0\xbb').encode('latin1').decode('utf8'))


param = '\xd0\xbf\xd1\x80\xd0\xbe\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xba\xd0\xb0.txt'

print(param.encode('latin1').decode('utf8'))


from django.utils.datastructures import MultiValueDict

d = MultiValueDict({'name': ['Adrian', 'Simon'], 'position': ['Developer']})
print(d)
print(d['name'][:5].encode('utf8'))
# 'Simon'
print(d.getlist('name'))



# # ['Adrian', 'Simon']
print(d.getlist('doesnotexist'))
# # []
print(d.getlist('doesnotexist', ['Adrian']))
# # ['Adrian', 'Simon']
print(d.get('lastname', 'nonexistent'))
# # 'nonexistent'
print(d.setlist('lastname', ['Holovaty', 'Willison']))

pa = '\xd0\xba.JPG'
print(pa.encode('utf8').decode('utf8').encode('windows-1252').decode('utf8'))

pa = '\u043a'
pa = '\xd0\xba\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbb\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0'
print(pa.encode('latin').decode('utf8'))
# print(pa.encode('latin1').decode('utf8'))

pa = '%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F'




tx = 'кирил.txt'
# # i = 0
# print(len(tx))
# i = len(tx) - 1
# # print('кирил.txt'[8])
# for sym in tx[-1]:
#     if sym == '.':
#         print(sym)
#         break
#     i -= 1
#
# print(i)
# print(tx[i])

# print(type(tx))
#
# tx = u''.join(str(tx.encode('utf8')))
# print(tx)

# print(tx.split('.')[-1])
#
# <MultiValueDict({
# 	'images': [<InMemoryUploadedFile: \xd0\xba.JPG (image/jpeg)>],
# 'file_3dmax': [<InMemoryUploadedFile: '\xd0\xbf\xd1\x80\xd0\xbe\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xba\xd0\xb0.txt (text/plain)'>],
# 'file_revit': [<InMemoryUploadedFile: '\xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0.xlsx (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)'>],
# 'file_technical_instruction': [<InMemoryUploadedFile: \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0.xlsx (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)>]}>

s = 'TesT@gmail.ru'
print(s)
s = str(s).lower()
print(s)
