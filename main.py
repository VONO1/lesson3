f = open('text.txt')
text = f.read()



#e = список знаков препинания формат ,"#знак препинания"
e = ",", ".","!","-","?","»","«","—"
for i in range(len(e)):
    text = text.replace(e[i], "")

#Текст без знаков препинания
print(text)

#Текст списком
lll = text.split()
print(lll)
print(type(lll))
# lower().


#нижний регистр
low_text = list(map(str.lower, lll))
print(low_text)

dictt = {}
for word in low_text:
    # print(dictt)
    if word in dictt:
        dictt[word] +=1
    else:
        dictt.update({word:1})


list_d = list(dictt.items())
list_d.sort(key=lambda i: i[1])
for i in list_d:
    print(i[0], ':', i[1])





            # print("yes!")


# for word in word_list:
# #2) проверить ключ в словаре word_count = {};
# if word in word_count:
#
# #3) создать индекс в словаре:
# word_count[word] = 0

