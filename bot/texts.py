texts = {
     1: '👤 Familiyangizni yozing:',
     2: '👤 Ismingizni yozing:',
     3: '👤 Otangizning ismini yozing:',
     4:   '📅 Tug‘ilgan sanangiz :\n\n KK.OO.YYYY(12.08.1967) formatida:',
     5: '💼 Maʼlumotingizni tanlang:',
     6: 'Ta‘lim muassasasining nomi va bitirgan yilingiz:',
     7: '👨‍👩‍👧‍👦 Oilaviy ahvolingiz:',
     8: '👨‍🔧 Mutaxassisligingiz:',
     9: '🌐 Yashash manzilingiz: viloyat(haqiqiy turar joy):',
     10: '🌐 Yashash manzilingiz: tuman yoki shahar(haqiqiy turar joy):',
     11:'🏘 To‘liq manzilingizni kiriting(MFY, ko‘cha):',
     12: 'Siz qaysi viloyatdagi filialda ishlashni xohlaysiz?',
     13: '👨🏻‍💼 Qaysi lavozimda ishlashni xohlaysiz?',
     14: '📞 Telefon raqamingiz +998xxxxxxxxx formatida:',
     15: '☎️ Qo‘shimcha telefon raqamingiz +998xxxxxxxxx formatida',
     16: '🇷🇺 Hozirda qaysi tillarni bilasiz?',
     17: '◀️🏦 Ish tajribangizni ishlagan joyingiz, lavozimingiz, vazifangiz va ishlagan davringiz formatida yozing.\nMisol uchun:\n\nMasnad MCHJ, Dasturchi, Dastur tuzish - 11.2020 - 03.2021n\nMasnad MCHJ, Dasturchi, Dastur tuzish - 11.2020 - 03.2021:\n',
     18: '👨‍💻 Qaysi dasturlardan foydalana olasiz?',
     19: '📝 Qo‘shimcha maʼlumotlar::',
     20: '💰 Qancha maosh olishni xohlaysiz?(faqat raqamlarda kiriting):',
     21: '❗️"Yuksalish" kompaniyasida ishlaydigan yaqin qarindoshlaringiz bormi? Agar bo\'lsa, to\'liq familiyasi, ismi, otasining ismini va lavozimini yozing:',
     22: '📷 O‘zingizni rasmingizni yuboring:',
     23: '"Men roziman" tugmachasini bosish orqali siz o`zingizning shaxsiy ma`lumotlaringizni kompaniya maqsadlarida qayta ishlash uchun ularni saqlashga, foydalanishga va o`zaro almashishga rozilik bildirasiz. Shuningdek, ushbu anketada siz taqdim etgan barcha ma`lumotlar ishonchli ekanligi va yolg`on ma`lumot uzatilishi holatlari aniqlangan taqdirda barcha javobgarlikni o`z zimmangizga olasiz.'
}

model = (
          '',
          'familiyasi',
          'ismi',
          'otasini_ismi',
          'tugulgan_sana',
          'malumoti',
          'talim_olgan',
          'oilaviy',
          'mutaxasis',
          'manzil_vil',
          'manzil_tum',
          'manzil',
          'ish_joyi',
          'lavozimi',
          'tel_raq',
          'tel_raq_qosh',
          'qay_til',
          'ish_davri',
          'qay_das',
          'qosh_mal',
          'maosh',
          'yaqin_qar',
          'photo',
          'active'
)
vil = (
    ('Qoraqalpogʻiston Respublikasi',
    'Andijon viloyati'
    ),('Buxoro viloyati',
    'Fargʻona viloyati'),
    ('Jizzax viloyati',
    'Xorazm viloyati'
    ),('Namangan viloyati',
    'Navoiy viloyati'
    ),('Qashqadaryo viloyati',
    'Samarqand viloyati'
    ),('Toshkent viloyati',
    'Sirdaryo viloyati'
    ),('Surxondaryo viloyati',
    'Toshkent shahri')
)

tum = {
'Qoraqalpogʻiston Respublikasi':(
('Amudaryo tumani','Beruniy tumani'),
('Chimboy tumani', 'Ellikqalʼa tumani'),
('Kegeyli tumani', 'Moʻynoq tumani'),
('Nukus tumani', 'Qanlikoʻl tumani'),
('Qoʻngʻirot tumani', 'Qoraoʻzak tumani'),
('Shumanay tumani','Taxtakoʻpir tumani'),
('Toʻrtkoʻl tumani','Xoʻjayli tumani'),
),
'Andijon viloyati': (
('Andijon (tuman)','Asaka tumani'),
('Baliqchi tumani','Boʻston (tuman)'),
('Buloqboshi tumani', 'Izboskan (tuman)'),
('Jalaquduq (tuman)','Xoʻjaobod tumani'),
('Qoʻrgʻontepa tumani','Marhamat tumani'),
('Oltinkoʻl (tuman)','Paxtaobod tumani'),
('Shahrixon (tuman)','Ulugʻnor (tuman)'),
),
'Buxoro viloyati':(
('Olot tumani', 'Buxoro tumani'),
('Gʻijduvon tumani','Jondor tumani'),
('Kogon tumani', 'Qorakoʻl tumani'),
('Qorovulbozor tumani', 'Peshku tumani'),
('Romitan tumani', 'Shofirkon tumani'),
('Vobkent tumani', 'Buxoro shaxri')
),
'Fargʻona viloyati':(
('Oltiariq tumani','Bagʻdod tumani'),
('Beshariq tumani','Buvayda tumani'),
('Dangʻara tumani','Fargʻona tumani'),
('Furqat tumani','Qoʻshtepa tumani'),
('Quva tumani','Rishton tumani'),
('Soʻx tumani','Toshloq tumani'),
('Uchkoʻprik tumani','Oʻzbekiston tumani'),
('Yozyovon tumani','Fargʻona shahar')
),
'Jizzax viloyati':(
('Arnasoy tumani','Baxmal tumani'),
('Doʻstlik tumani','Forish tumani'),
('Gʻallaorol tumani','Sharof Rashidov tumani'),
('Mirzachoʻl tumani','Paxtakor tumani'),
('Yangiobod tumani','Zomin tumani'),
('Zafarobod tumani','Zarbdor tumani')
),
'Xorazm viloyati':(
('Bogʻot tumani','Gurlan tumani'),
('Xonqa tumani','Hazorasp tumani'),
('Xiva tumani','Qoʻshkoʻpir tumani'),
('Shovot tumani','Urganch tumani'),
('Yangiariq tumani','Yangibozor tumani'),
('upproqqalʼa tumani','Xorazm shahar')
),
'Namangan viloyati':(
('Chortoq tumani','Chust tumani'),
('Kosonsoy tumani','Mingbuloq tumani'),
('Namangan tumani','Norin tumani' ),
('Pop tumani','Toʻraqoʻrgʻon tumani'),
('Uchqoʻrgʻon tumani','Uychi tumani'),
('Yangiqoʻrgʻon tumani','Davlatobod tumani'),
),
'Navoiy viloyati':(
('Konimex tumani', 'Karmana tumani'),
('Qiziltepa tuman', 'Xatirchi tumani'),
('Navbahor tumani', 'Nurota tumani'),
('Tomdi tumani', 'Uchquduq tumani'),
),
'Qashqadaryo viloyati':(
('Chiroqchi tumani','Dehqonobod tumani'),
('Guzor tumani','Kasbi tumani'),
('Kitob tumani','Koson tumani' ),
('Mirishkor tumani','Muborak tumani'),
('Nishon tumani','Qarshi tumani'),
('Qarshi shahri','Davlatobod tumani'),
('Shahrisabz shahri', 'Yakkabog tumani' )
),
'Samarqand viloyati':(
('Bulungʻur tumani','Ishtixon tumani'),
('Jomboy tumani','Kattaqoʻrgʻon tumani	'),
('Qoʻshrabot tumani','Narpay tumani' ),
('Nurobod tumani','Oqdaryo tumani'),
('Paxtachi tumani','Payariq tumani'),
('Pastdargʻom tumani','Samarqand tumani'),
('Toyloq tumani', 'Urgut tumani' )
),
'Sirdaryo viloyati':(
('Sardoba tumani', 'Boyovut tumani'),
('Guliston tumani', 'Xovos tumani'),
('Mirzaobod tumani', 'Sayxunobod tumani'),
('Oqoltin tumani', 'Sirdaryo tumani'),
),
'Toshkent viloyati':(
('Bekobod tumani','Boʻstonliq tumani'),
('Boʻka tumani','Chinoz tumani	'),
('Qibray tumani','Ohangaron tumani' ),
('Oqqoʻrgʻon tumani','Parkent tumani'),
('Piskent tumani','Quyi chirchiq tumani'),
('Oʻrta Chirchiq tumani','Yangiyoʻl  tumani'),
('Yuqori Chirchiq tumani', 'Zangiota tumani' )
),
'Surxondaryo viloyati':(
('Angor tumani','Boysun tumani'),
('Denov tumani','Jarqoʻrgʻon tumani	'),
('Qiziriq tumani','Qumqoʻrgʻon tumani' ),
('Muzrabot tumani','Oltinsoy tumani'),
('Sariosiyo tumani','Sherobod tumani'),
('Shoʻrchi tumani','Termiz  tumani'),
('Uzun tumani', 'Bandixon  tumani' )
),
'Toshkent shahri':(
('Bektemir  tumani','Mirobod tumani'),
('Mirzo tumani','Sergeli tumani	'),
('Uchtepa tumani','Olmazor tumani' ),
('Shayxontohur tumani','Yashnobod tumani'),
('Chilonzor tumani','Yakkasaroy  tumani'),
('Yunusobod  tumani', ' ')
),
}


fili = (('Fargona viloyati','Uchkòprik'),
        ('Yozyovon','Qòshtepa'),
        ('Namangan viloyati','Uychi tumani'),
        ('Kosonsoy tumani','Chust tumani'),
        ('Sirdaryo viloyati','Guliston shaxri'),
        )

lav = (("Shartnoma rasmiylashtirish","Kassir"),
        ("Supervayzer", "Sotuvchi maslahatchi"
        ),("Ombor mudiri", "Ombor yordamchisi"
        ),("Ombor xodimi", "Yetkazib beruvchi"
        ),("Qarzdorlikni undirish bo'limi", "Reception"
        ),("Oshxona xodimi", "Reklama bo'limi"
        ),("Xo'jalik xodimi",  "operator")
       )


''' 
'''