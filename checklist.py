menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?>>>')


'manti' in menyu #menyuda manti bormi?

#natija: FALSE
'shashlik' in menyu #menyuda manti bormi?

#natija: TRUE

'osh' in menyu; #menyuda osh bormi

#Natija: True


if ovqat.lower() in menyu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunday taom yo\'q')


#Natija: Nima ovqat yeysiz?>>> somsa 
# Buyurtma qabul qilindi.

#Natija 2 : Nima ovqat yeysiz?>>>dimlama
# Afsuski bizda bunday taom yo'q

'manti' not in menyu # menyuda manti yo'qmi?
#Natija: True

'osh' not in menyu # menyuda osh yo'qmi?
#Natija:False

if ovqat.lower() not in menyu:
    print('Afsuski bizda bunday taom yo\'q')
else:
    print('Buyurtma qabul qilindi.')

