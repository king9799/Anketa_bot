from urllib import request
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,  HttpResponse
import telebot
from django.views.decorators.csrf import csrf_exempt
from telebot import *
from .models import *
from .texts import *
from django.core.files.base import ContentFile
from datetime import date
# Create your views here.

bot = TeleBot("1971047625:AAHjxhFMp2iA5Y2W7w4DdnsaTswbHHQtOjU")


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    if request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)


# def clients(request, id):
#     today = date.today()
#     Str = date.isoformat(today)
#     client = Clients.objects.all()
#     clients = Clients.objects.filter(cr_on=Str)
#     branch = Branch.objects.all()
#     get_branch = Branch.objects.get(id=id)
#     get_client = Clients.objects.filter(ish_joyi=get_branch.name)
#     provinces = Province.objects.all()
#     return render(request, 'clients.html', {'today': len(clients), 'client': client, 'clients': get_client, 'provinces': provinces, 'branch': branch})
#
#
# def clients_info(request, id):
#     today = date.today()
#     Str = date.isoformat(today)
#     client = Clients.objects.all()
#     clients = Clients.objects.filter(cr_on=Str)
#     branch = Branch.objects.all()
#     get_branch = Branch.objects.get(id=id)
#     get_client = Clients.objects.filter(ish_joyi=get_branch.name)
#     provinces = Province.objects.all()
#     return render(request, 'clients.html', {'today': len(clients), 'client': client, 'clients': get_client, 'provinces': provinces, 'branch': branch})
#
#
# def dashboard(request):
#     today = date.today()
#     Str = date.isoformat(today)
#     client = Clients.objects.all()
#     clients = Clients.objects.filter(cr_on=Str)
#     provinces = Province.objects.all()
#     branch = Branch.objects.all()
#     return render(request, 'dashboard.html', {'today': len(clients), 'provinces': provinces, 'client': len(client), 'branch': branch})
#
#
# def log_in(request):
#     return render(request, 'login-2.html')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    register_user(message)
    bot.send_message(message.from_user.id, 'Салом 👋🏻 \
Ушбу бот Юксалишда лабор️ анкеталарни тўлдириш ва меҳнат учун мўлжалланган! \nБу эрда сиз ўзингизнинг аризангизни 📄 тўлдиришингиз ✍️\nва бизнинг компаниямиздаги мавжуд бўш иш ўринлари ҳақида билиб олишингиз мумкин! \n\n\
Здравствуйте 👋🏻 \nЭтот бот предназначен для заполнения анкеты ✍️ и трудоустройства  в Юксалиш \nЗдесь Вы можете заполнить свою анкету 📄 и узнать о существующих вакансиях нашей Компании!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('🇺🇿 o`zbek tili 🇺🇿')
    btn2 = types.KeyboardButton('🇸🇰 Русскый язык 🇸🇰')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, 'Давайте для начала выберем язык:\n\nАввалига тилни танлаб олайлик:', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    client = Clients.objects.get(user_id=message.from_user.id)
    a = ['sadas', 'sdaasd', 'dakj']
    if message.text == '🇺🇿 o`zbek tili 🇺🇿':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Orqaga ↩️')
        btn2 = types.KeyboardButton('Bekor qilish 🚫')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '👤 Familiyangizni yozing:', reply_markup=markup)
        client = Clients.objects.get(user_id=message.from_user.id)
        client.step = 1
        client.save()
    elif message.text == '🇸🇰 Русскый язык 🇸🇰':
        bot.send_message(message.from_user.id, 'ru case good')
    elif message.text == 'Bekor qilish 🚫':
        client = Clients.objects.get(user_id=message.from_user.id)
        client.delete()
        register_user(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('🇺🇿 o`zbek tili 🇺🇿')
        btn2 = types.KeyboardButton('🇸🇰 Русскый язык 🇸🇰')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Салом 👋🏻 \
        Ушбу бот Юксалишда лабор️ анкеталарни тўлдириш ва меҳнат учун мўлжалланган! \nБу эрда сиз ўзингизнинг аризангизни 📄 тўлдиришингиз ✍️\nва бизнинг компаниямиздаги мавжуд бўш иш ўринлари ҳақида билиб олишингиз мумкин! \n\n\
        Здравствуйте 👋🏻 \nЭтот бот предназначен для заполнения анкеты ✍️ и трудоустройства  в Юксалиш \nЗдесь Вы можете заполнить свою анкету 📄 и узнать о существующих вакансиях нашей Компании!')

        bot.send_message(message.from_user.id, 'Давайте для начала выберем язык:\n\nАввалига тилни танлаб олайлик:',
                         reply_markup=markup)
    elif message.text == 'Orqaga ↩️' or message.text == '▶️ O‘tkazib yuborish':
        if message.text == 'Orqaga ↩️':
            client = Clients.objects.get(user_id=message.from_user.id)
            client.step -= 1
            client.save()
        else:
            client = Clients.objects.get(user_id=message.from_user.id)
            client.step += 1
            client.save()
        if client.step in [1,2, 4, 8, 11, 15, 17, 20, 22]:
            buttons(message, client)
        elif client.step == 5:
            btn_mal(message,client)
        elif client.step == 7:
            btn_ax(message,client)
        elif client.step == 9:
            vil_buttons(message,client)
        elif client.step == 10:
            tum_buttons(message,client, client.manzil_vil)
        elif client.step == 12:
            fil_buttons(message,client)
        elif client.step == 13:
            lav_buttons(message,client)
        elif client.step == 14:
            tel_buttons(message,client)
        elif client.step == 13:
            lav_buttons(message,client)
        elif client.step in [16, 18]:
            if client.step == 16:
                til_btn(message,client, "✔️ O'zbek tili", "✔️ Ingliz tili", "✔️ Rus tili")
            else:
                til_btn(message, client, message, client, "✔️ Excel", "✔️ Word", "✔️ Power Point", '▶️ O‘tkazib yuborish')
        elif client.step in [3,6,19,21]:
            if client.step == 21:
                btn_pass(message,client, 'Yoq')
            else:
                btn_pass(message,client)
    elif message.text == '✅ Tasdiqlash':
        client = Clients.objects.get(user_id=message.from_user.id)
        client.step += 1
        client.save()
        buttons(message, client)
    elif message.text == "✔️ O'zbek tili":
        client.qay_til += ':'+"O'zbek tili"
        print(client.qay_til)
        client.save()
        a = ["✔️ O'zbek tili" if "O'zbek" not in client.qay_til else "❌ O'zbek tili"]
        b = ["✔️ Ingliz tili" if 'Ingliz' not in client.qay_til else '❌ Ingliz tili']
        d = ["✔️ Rus tili" if 'Rus' not in client.qay_til else "❌ Rus tili"]
        til_btn(message, client, client.qay_til, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "✔️ Ingliz tili":
        client.qay_til += ':'+"Ingliz tili"
        client.save()
        a = ["✔️ O'zbek tili" if "O'zbek" not in client.qay_til else "❌ O'zbek tili"]
        b = ["✔️ Ingliz tili" if 'Ingliz' not in client.qay_til else '❌ Ingliz tili']
        d = ["✔️ Rus tili" if 'Rus' not in client.qay_til else "❌ Rus tili"]
        til_btn(message, client, client.qay_til, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "✔️ Rus tili":
        client.qay_til += ':' + "Rus tili"
        client.save()
        a = ["✔️ O'zbek tili" if "O'zbek" not in client.qay_til else "❌ O'zbek tili"]
        b = ["✔️ Ingliz tili" if 'Ingliz' not in client.qay_til else '❌ Ingliz tili']
        d = ["✔️ Rus tili" if 'Rus' not in client.qay_til else "❌ Rus tili"]
        til_btn(message, client, client.qay_til, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "❌ O'zbek tili":
        if client.qay_til.strip() == "O'zbek tili":
            client.qay_til = ':'
            client.save()
        else:
            remov = client.qay_til.split(':')
            remov.remove("O'zbek tili")
            client.qay_til = ':'.join(map(str, remov))
            client.save()
        a = ["✔️ O'zbek tili" if "O'zbek" not in client.qay_til else "❌ O'zbek tili"]
        b = ["✔️ Ingliz tili" if 'Ingliz' not in client.qay_til else '❌ Ingliz tili']
        d = ["✔️ Rus tili" if 'Rus' not in client.qay_til else "❌ Rus tili"]
        til_btn(message, client, client.qay_til, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "❌ Ingliz tili":
        if client.qay_til.strip() == 'Ingliz tili':
            client.qay_til = ':'
            client.save()
        else:
            remov = client.qay_til.split(':')
            remov.remove('Ingliz tili')
            client.qay_til = ':'.join(map(str, remov))
            client.save()
        a = ["✔️ O'zbek tili" if "O'zbek" not in client.qay_til else "❌ O'zbek tili"]
        b = ["✔️ Ingliz tili" if 'Ingliz' not in client.qay_til else '❌ Ingliz tili']
        d = ["✔️ Rus tili" if 'Rus' not in client.qay_til else "❌ Rus tili"]
        til_btn(message, client, client.qay_til, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "❌ Rus tili":
        print(len(client.qay_til))
        if client.qay_til.strip() == 'Rus tili':
            client.qay_til = ':'
            client.save()
        else:
            remov = client.qay_til.split(':')
            remov.remove('Rus tili')
            client.qay_til = ':'.join(map(str, remov))
            client.save()
            print(client.qay_til)
        a = ["✔️ O'zbek tili" if "O'zbek" not in client.qay_til else "❌ O'zbek tili"]
        b = ["✔️ Ingliz tili" if 'Ingliz' not in client.qay_til else '❌ Ingliz tili']
        d = ["✔️ Rus tili" if 'Rus' not in client.qay_til else "❌ Rus tili"]
        til_btn(message, client, client.qay_til, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "✔️ Excel":
        client.qay_das += ':'+"Excel"
        client.save()
        a = ["✔️ Excel" if "Excel" not in client.qay_das else "❌ Excel"]
        b = ["✔️ Word" if 'Word' not in client.qay_das else '❌ Word']
        d = ["✔️ Power Point" if 'Power Point' not in client.qay_das else "❌ Power Point"]
        til_btn(message, client, client.qay_das, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "✔️ Word":
        client.qay_das += ':'+"Word"
        client.save()
        a = ["✔️ Excel" if "Excel" not in client.qay_das else "❌ Excel"]
        b = ["✔️ Word" if 'Word' not in client.qay_das else '❌ Word']
        d = ["✔️ Power Point" if 'Power Point' not in client.qay_das else "❌ Power Point"]
        til_btn(message, client, client.qay_das, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "✔️ Power Point":
        client.qay_das += ':' + "Power Point"
        client.save()
        a = ["✔️ Excel" if "Excel" not in client.qay_das else "❌ Excel"]
        b = ["✔️ Word" if 'Word' not in client.qay_das else '❌ Word']
        d = ["✔️ Power Point" if 'Power Point' not in client.qay_das else "❌ Power Point"]
        til_btn(message, client, client.qay_das, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "❌ Excel":
        if client.qay_das.strip() == 'Excel':
            client.qay_das = ':'
            client.save()
        else:
            remov = client.qay_das.split(':')
            remov.remove('Excel')
            client.qay_das = ':'.join(map(str, remov))
            client.save()
        a = ["✔️ Excel" if "Excel" not in client.qay_das else "❌ Excel"]
        b = ["✔️ Word" if 'Word' not in client.qay_das else '❌ Word']
        d = ["✔️ Power Point" if 'Power Point' not in client.qay_das else "❌ Power Point"]
        til_btn(message, client, client.qay_das, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "❌ Word":
        if client.qay_das.strip() == 'Word':
            client.qay_das = ':'
            client.save()
        else:
            remov = client.qay_das.split(':')
            remov.remove('Word')
            client.qay_das = ':'.join(map(str, remov))
            client.save()
        a = ["✔️ Excel" if "Excel" not in client.qay_das else "❌ Excel"]
        b = ["✔️ Word" if 'Word' not in client.qay_das else '❌ Word']
        d = ["✔️ Power Point" if 'Power Point' not in client.qay_das else "❌ Power Point"]
        til_btn(message, client, client.qay_das, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == "❌ Power Point":
        if client.qay_das.strip() == 'Power Point':
            client.qay_das = ':'
            client.save()
        else:
            remov = client.qay_das.split(':')
            remov.remove('Power Point')
            client.qay_das = ':'.join(map(str, remov))
            client.save()
            print(client.qay_til)
        a = ["✔️ Excel" if "Excel" not in client.qay_das else "❌ Excel"]
        b = ["✔️ Word" if 'Word' not in client.qay_das else '❌ Word']
        d = ["✔️ Power Point" if 'Power Point' not in client.qay_das else "❌ Power Point"]
        til_btn(message, client, client.qay_das, a[0], b[0], d[0], '✅ Tasdiqlash')
    elif message.text == 'Fargona viloyati':
        fil_buttons(message, client, 'Uchkòprik', 'Yozyovon', 'Qòshtepa')
    elif message.text == 'Namangan viloyati':
        fil_buttons(message, client, 'Uychi tumani', 'Kosonsoy tumani', 'Chust tumani', 'Pop tumani', 'Uchqo\'rg\'ong')
    elif message.text == 'Sirdaryo viloyati':
        fil_buttons(message, client, 'Guliston shaxri')
    elif message.text == 'Men roziman':
        bot.send_message(message.from_user.id, '✔️Arizangiz qabul qilindi tez orada siz bilan bog`lanishadi', reply_markup=types.ReplyKeyboardRemove())
        text = f'👤: {client.familiyasi} {client.ismi} {client.otasini_ismi} \n  📆: {client.tugulgan_sana} \n 📍: {client.manzil_vil} {client.manzil_tum} {client.manzil} \n 👨‍👩‍👧‍👦:{client.oilaviy}\n 💼:{client.mutaxasis}\n📞1:{client.tel_raq} \n📞2:{client.tel_raq_qosh}\n 🧳:{client.ish_davri}\n🎓: {client.malumoti}\n 🏫: {client.qosh_mal}\n 🧑‍💻: {client.qay_das}\n 🇷🇺🇺🇿🇺🇸: {client.qay_til}\n 🔍📍: {client.ish_joyi}\n🧰:{client.lavozimi}\n 💰:{client.maosh}\n'
        bot.send_photo(593914942, client.photo, text)
        bot.send_photo(1763634473, client.photo, text)
        # if len(Clients.objects.filter(user_id=593914942)) == 1 or 1 == len(Clients.objects.filter(user_id=1763634473)):
        #     x = 593914942
        #     y = 1763634473
        #     bot.send_photo(x, client.photo, text)
    else:
        working(message)


def working(message):
    client = Clients.objects.get(user_id=message.from_user.id)
    if client.step == 0:
        bot.send_message(message.from_user.id, '0')
    elif client.step == 1:
        client.familiyasi = message.text
        client.step += 1
        client.save()
        buttons(message, client)
    elif client.step == 2:
        client.ismi = message.text
        client.step += 1
        client.save()
        btn_pass(message, client)
    elif client.step == 3:
        client.step += 1
        client.otasini_ismi = message.text
        client.save()
        buttons(message,client)
    elif client.step == 4:
        client.step += 1
        client.tugulgan_sana = message.text
        client.save()
        btn_mal(message, client)
    elif client.step == 5:
        client.step += 1
        client.malumoti = message.text
        client.save()
        btn_pass(message, client)
    elif client.step == 6:
        client.step += 1
        client.talim_olgan = message.text
        client.save()
        btn_ax(message, client)
    elif client.step == 7:
        client.step += 1
        client.oilaviy = message.text
        client.save()
        buttons(message,client)
    elif client.step == 8:
        client.step += 1
        client.mutaxasis = message.text
        client.save()
        vil_buttons(message, client)
    elif client.step == 9:
        client.step += 1
        client.manzil_vil = message.text
        client.save()
        print(message.text)
        tum_buttons(message, client, client.manzil_vil)
    elif client.step == 10:
        client.step += 1
        client.manzil_tum = message.text
        client.save()
        buttons(message,client)
    elif client.step == 11:
        client.step += 1
        client.manzil = message.text
        client.save()
        fil_buttons(message, client, 'Fargona viloyati', 'Namangan viloyati', 'Sirdaryo viloyati' )
    elif client.step == 12:
        client.step += 1
        client.ish_joyi = message.text
        client.save()
        lav_buttons(message, client)
    elif client.step == 13:
        client.step += 1
        client.lavozimi = message.text
        client.save()
        tel_buttons(message, client)
    elif client.step == 14:
        tel_buttons(message, client)
    elif client.step == 15:
        if message.text.isdigit():
            client.step += 1
            client.tel_raq_qosh = message.text
            client.save()
            til_btn(message, client, client.qay_das, "✔️ O'zbek tili", "✔️ Ingliz tili", "✔️ Rus tili")
        else:
            buttons(message, client)
    elif client.step == 16:
        client.step += 1
        client.qay_til = message.text
        client.save()
        buttons(message,client)
    elif client.step == 17:
        client.step += 1
        client.ish_davri = message.text
        client.save()
        til_btn(message, client, client.qay_das, "✔️ Excel", "✔️ Word", "✔️ Power Point", '▶️ O‘tkazib yuborish')
    elif client.step == 18:
        client.step += 1
        client.qay_das = message.text
        client.save()
        btn_pass(message, client)
    elif client.step == 19:
        client.step += 1
        client.qosh_mal = message.text
        client.save()
        buttons(message,client)
    elif client.step == 20:
        if message.text.isdigit():
            client.step += 1
            client.maosh = message.text
            client.save()
            btn_pass(message,client, skip='Yo`q')
        else:
            buttons(message, client)
    elif client.step == 21:
        client.step += 1
        client.yaqin_qar = message.text
        client.save()
        buttons(message, client)
    elif client.step == 22:
        buttons(message, client)
    elif client.step == 23:
        bot.send_message(message.from_user.id, 'Arizangiz korib chiqilyapti Natijasi yaqin orada chiqadi hamda siz bilan bog`lanishadi')


@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    client = Clients.objects.get(user_id=message.from_user.id)
    client.step += 1
    client.tel_raq = message.contact.phone_number
    client.save()
    buttons(message, client)


def save_client_image(message, path, file):
    client = Clients.objects.get(user_id=message.from_user.id)
    content = ContentFile(file)
    client.photo.save(path, content, save=True)


@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    client = Clients.objects.get(user_id=message.from_user.id)
    if client.step == 22:
        print('good')
        raw = message.photo[1].file_id
        path = raw + ".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        content = ContentFile(downloaded_file)
        client.photo.save(path, content, save=True)
        client.step += 1
        client.save()
    if client.otasini_ismi is None:
        text = f'👤: {client.familiyasi} {client.ismi} \n  📆: {client.tugulgan_sana} \n 📍: {client.manzil_vil} {client.manzil_tum} {client.manzil} \n 👨‍👩‍👧‍👦:{client.oilaviy}\n 💼:{client.mutaxasis}\n📞:{client.tel_raq}\n 🧳:{client.ish_davri}\n🎓: {client.malumoti}\n 🏫: {client.qosh_mal}\n 🧑‍💻: {client.qay_das}\n 🇷🇺🇺🇿🇺🇸: {client.qay_til}\n 🔍📍: {client.ish_joyi}\n🧰:{client.lavozimi}\n 💰:{client.maosh}\n'
        bot.send_photo(message.from_user.id, client.photo, text)
        btn_pass(message, client, skip='Men roziman')
    else:
        text = f'👤: {client.familiyasi} {client.ismi} {client.otasini_ismi} \n  📆: {client.tugulgan_sana} \n 📍: {client.manzil_vil} {client.manzil_tum} {client.manzil} \n 👨‍👩‍👧‍👦:{client.oilaviy}\n 💼:{client.mutaxasis}\n📞:{client.tel_raq}\n 🧳:{client.ish_davri}\n🎓: {client.malumoti}\n 🏫: {client.qosh_mal}\n 🧑‍💻: {client.qay_das}\n 🇷🇺🇺🇿🇺🇸: {client.qay_til}\n 🔍📍: {client.ish_joyi}\n🧰:{client.lavozimi}\n 💰:{client.maosh}\n'
        bot.send_photo(message.from_user.id, client.photo, text)
        btn_pass(message, client, skip='Men roziman')


def register_user(message):
    if len(Clients.objects.filter(user_id=message.from_user.id)) == 0:
        client = Clients.objects.create(
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            qay_til=':',
            qay_das=':'
        )
        client.save()


def buttons(message, client):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Orqaga ↩️')
    btn2 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def btn_ax(message, client):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton('Turmush qurgan')
    btn1 = types.KeyboardButton('Turmush qurmagan')
    btn2 = types.KeyboardButton('Orqaga ↩️')
    btn3 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn, btn1)
    markup.add(btn2, btn3)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def register(message, client, texts):
    pass


def btn_mal(message, client):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton('Oliy')
    btn1 = types.KeyboardButton('Magistratura')
    btn2 = types.KeyboardButton('Talaba')
    btn3 = types.KeyboardButton('O`rta maxsus')
    btn4 = types.KeyboardButton('Orqaga ↩️')
    btn5 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn, btn1)
    markup.add(btn2, btn3)
    markup.add(btn4, btn5)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def btn_pass(message, client, skip='▶️ O‘tkazib yuborish'):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton(skip)
    btn1 = types.KeyboardButton('Orqaga ↩️')
    btn2 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn)
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def vil_buttons(message, client):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for v1, v2 in vil:
        btn1 = types.KeyboardButton(v1)
        btn2 = types.KeyboardButton(v2)
        markup.add(btn1, btn2)
    btn1 = types.KeyboardButton('Orqaga ↩️')
    btn2 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def tum_buttons(message, client, a):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for v1, v2 in tum[a]:
        btn1 = types.KeyboardButton(v1)
        btn2 = types.KeyboardButton(v2)
        markup.add(btn1, btn2)
    btn1 = types.KeyboardButton('Orqaga ↩️')
    btn2 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def fil_buttons(message, client, *args):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if 4 > len(args) > 1:
        btn1 = types.KeyboardButton(args[0])
        btn2 = types.KeyboardButton(args[1])
        btn3 = types.KeyboardButton(args[2])
        markup.add(btn1, btn2, btn3)
    elif len(args) == 4:
        btn1 = types.KeyboardButton(args[0])
        btn2 = types.KeyboardButton(args[1])
        btn3 = types.KeyboardButton(args[2])
        btn4 = types.KeyboardButton(args[3])
        markup.add(btn1, btn2, btn3, btn4)
    elif len(args) == 5:
        btn1 = types.KeyboardButton(args[0])
        btn2 = types.KeyboardButton(args[1])
        btn3 = types.KeyboardButton(args[2])
        btn4 = types.KeyboardButton(args[3])
        btn5 = types.KeyboardButton(args[4])
        markup.add(btn1, btn2, btn3, btn4, btn5)
    else:
        btn1 = types.KeyboardButton(args[0])
        markup.add(btn1)
    btn1 = types.KeyboardButton('Orqaga ↩️')
    btn2 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def lav_buttons(message, client):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for v1, v2 in lav:
        btn1 = types.KeyboardButton(v1)
        btn2 = types.KeyboardButton(v2)
        markup.add(btn1, btn2)
    btn1 = types.KeyboardButton('Orqaga ↩️')
    btn2 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def tel_buttons(message, client):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton('📞 Telegram akkount raqamingizni yuborish', request_contact=True)
    btn1 = types.KeyboardButton('Orqaga ↩️')
    btn2 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn)
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, texts[client.step], reply_markup=markup)


def til_btn(message, client, text,  *args):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn = types.KeyboardButton(args[0])
    btn1 = types.KeyboardButton(args[1])
    btn2 = types.KeyboardButton(args[2])
    btn3 = types.KeyboardButton('Orqaga ↩️')
    btn4 = types.KeyboardButton('Bekor qilish 🚫')
    markup.add(btn, btn1, btn2)
    if len(args) > 3:
        btn5 = types.KeyboardButton(args[3])
        markup.add(btn5)
    markup.add(btn3, btn4)
    bot.send_message(message.from_user.id, texts[client.step]+f'\n:{text}', reply_markup=markup)