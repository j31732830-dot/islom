import asyncio
import logging,sys,os
from aiogram import Dispatcher,Bot,F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
load_dotenv()
API=os.getenv("API")
dp=Dispatcher()

@dp.message(Command('start'))
async def start_handler(msg:Message):
    await msg.answer("salom hush kelibsiz",reply_markup=Menu)

menu=[
    'It live haqida🏫',
    'Kurslar📚',
    'Mentorlar🧑‍🏫',
    "Biz bilan bog`lanish📞",
    "Loktsiaya🚩"
]

Menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=item)]for item in menu
    ],resize_keyboard=True
)
@dp.message(F.text.in_(menu))
async def Menu_handler(msg:Message):
    T=msg.text
    if menu[0]==T:
        await msg.answer("""
IT Live haqida ma’lumot 💻
IT Live — bu axborot texnologiyalari (IT) sohasiga oid jonli (live) tarzda o‘tkaziladigan darslar, seminarlar yoki treninglardir. Bunday tadbirlarda mutaxassislar yoki o‘qituvchilar internet orqali yoki auditoriyada real vaqt rejimida bilim berishadi.

IT Live tadbirlarida odatda quyidagi mavzular bo‘ladi:
    Dasturlash (Python, JavaScript va boshqalar)
    Web dasturlash (veb sayt yaratish)
    Grafik dizayn
    Kompyuter savodxonligi
    Sun’iy intellekt va yangi texnologiyalar

IT Live’ning afzalliklari:
    O‘qituvchi bilan jonli muloqot qilish mumkin
    Savollar berib, darhol javob olish mumkin
    Amaliy mashg‘ulotlar ko‘p bo‘ladi
    Zamonaviy kasbni o‘rganishga yordam beradi        
        """)
    elif menu[1]==T:
        await msg.answer('Kurs tanlang',reply_markup=Kurslar)
    elif menu[2]==T:
        await msg.answer('Mentor tanlang')
    elif menu[3]==T:
        button=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Telegram uchun',url='https://t.me/+998915093298')]
            ]
        )
        await msg.answer("""
📞 Biz bilan bog‘lanish
Agar siz kurslar haqida batafsil ma’lumot olishni istasangiz yoki ro‘yxatdan o‘tmoqchi bo‘lsangiz, biz bilan bog‘lanishingiz mumkin:
    📞 Telefon: +998 99 721 20 17
    📱 Telegram: @itlive
    📧 Email: info@itlive.uz
Biz sizning savollaringizga mamnuniyat bilan javob beramiz.
        """,reply_markup=button)
    elif menu[4]==T:
        # 40.502724, 68.764829
        await msg.answer("""
 Bizning manzil:        
        
 IT Live O`quv Markazi
 Guliston shahri
        
 Bizni xaritadan ko`ring:
        """)
        await msg.answer_location(latitude=40.502724,longitude=68.764829)

mentorlar=[
    ()
]



kurslar = [
    "Mobil dasturlash",      #0
    "Foundation Dasturlash", #1
    "Frontend Dasturlash",   #2
    "Backend Dasturlash",    #3
    "Full Stack Dasturlash", #4
    "Suniy inteleg",         #5
    "Kibir hafsizlik",       #6
    "Robotexnika",           #7
    "Buga`lteriya",          #8
    "SMM",                   #9
    "DevOps",                #10
    "Ardunio",               #11
    "⬅️ Orqaga"              #12
]
Kurslar=ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=item )]for item in kurslar],resize_keyboard=True
)
@dp.message(F.text.in_(kurslar))
async def Kurs_handler(msg:Message):
    T=msg.text
    if kurslar[0]==T:
        await msg.answer("""
              📱 Mobil dasturlash kursi

              Mobil dasturlash kursida siz Android va iOS qurilmalari uchun ilovalar yaratishni o‘rganasiz. 
              Kurs davomida zamonaviy texnologiyalar yordamida mobil ilovalar ishlab chiqish ko‘nikmalariga ega bo‘lasiz.

              📚 Kurs davomida:
              • Mobil dasturlash asoslari
              • UI/UX tushunchalari
              • Ilova interfeyslarini yaratish
              • API bilan ishlash
              • Real loyihalar ustida amaliy ishlar

              👨‍🏫 Tajribali mentorlar yordamida siz noldan boshlab mobil ilovalar yaratishni o‘rganasiz va o‘z loyihalaringizni ishlab chiqishingiz mumkin. """)

    elif kurslar[2] == T:
            await msg.answer("""
              🌐 Frontend dasturlash kursi/.


        📚 Kurs davomida:
        • Robotlarning ishlash prinsiplari
        • Sensorlar va aktuatorlar bilan ishlash
        • Mikroprotsessor va mikrokontrollerlar
        • Dasturlash va robotlarni boshqarish
        • Amaliy loyihalar va mini-robotlar yaratish

        👨‍🏫 Tajribali mentorlar yordamida siz robototexnika sohasida 
        zarur bilim va ko‘nikmalarga ega bo‘lasiz, o‘z loyihalaringizni yaratishingiz mumkin.
            """)
    elif kurslar[8] == T:
        if menu[0] == "🧪 Laboratoriya":
            await msg.answer("""
        🧪 Laboratoriya amaliyotlari

        IT Live kurslarida laboratoriya mashg‘ulotlari talabalarni amaliy bilim bilan ta’minlaydi. 
        Bu mashg‘ulotlarda siz nazariy bilimlarni real loyihalarda qo‘llashni o‘rganasiz.

        📚 Laboratoriyada:
        • Kod yozish va test qilish
        • Robototexnika va AI loyihalarini qurish
        • Mobil va veb-ilovalarni amaliy sinovdan o‘tkazish
        • Mentorlar bilan birga real loyiha yaratish

        👨‍🏫 Tajribali mentorlar yordamida siz o‘rganayotgan yo‘nalishingiz bo‘yicha mustahkam amaliy ko‘nikmalarni olasiz.
            """)
    elif kurslar[9] == T:
        if menu[0] == "📱 SMM":
            await msg.answer("""
        📱 SMM (Social Media Marketing) kursi

        SMM kursi — bu ijtimoiy tarmoqlarda brendni targ‘ib qilish, auditoriya bilan ishlash va marketing strategiyalarini yaratishni o‘rgatadi. 
        Kurs orqali siz zamonaviy digital marketing ko‘nikmalariga ega bo‘lasiz.

        📚 Kurs davomida:
        • Ijtimoiy tarmoqlar strategiyasi
        • Kontent yaratish va rejalashtirish
        • Reklama kampaniyalarini boshqarish
        • Analitika va natijalarni tahlil qilish
        • Real loyihalar ustida amaliy ishlar

        👨‍🏫 Tajribali mentorlar yordamida siz SMM sohasida professional bilim va amaliy ko‘nikmalarni egallaysiz, brendingizni rivojlantira olasiz.
            """)
    elif kurslar[10] == T:
        if menu[0] == "⚙️ DevOps":
            await msg.answer("""
        ⚙️ DevOps kursi

        DevOps — bu dasturiy ta’minot ishlab chiqish va uni serverlarga joylashtirish jarayonini birlashtiradigan zamonaviy IT yo‘nalishi. 
        Kurs orqali siz dastur ishlab chiqishdan tortib, uni doimiy ishlashini ta’minlashgacha bo‘lgan jarayonlarni o‘rganasiz.

        📚 Kurs davomida:
        • CI/CD (Continuous Integration / Continuous Deployment) asoslari
        • Server va bulutli texnologiyalar bilan ishlash
        • Avtomatlashtirish va monitoring
        • Docker, Kubernetes va boshqa zamonaviy vositalar
        • Real loyihalar ustida amaliy ishlar

        👨‍🏫 Tajribali mentorlar yordamida siz DevOps sohasida professional ko‘nikmalarni egallab, IT tizimlarini samarali boshqarish imkoniga ega bo‘lasiz.
            """)
    elif kurslar[11] == T:
        if menu[0] == "🛠 Arduino":
            await msg.answer("""
        🛠 Arduino kursi

        Arduino kursi — bu elektronika va dasturlashni birlashtirib, turli qurilmalar va robotlar yaratishni o‘rgatuvchi yo‘nalishdir. 
        Kurs orqali siz mikrokontrollerlar yordamida loyihalarni yaratishni o‘rganasiz.
        Kiber xavfsizlik — bu kompyuter tizimlari, tarmoqlar va ma’lumotlarni 
        xavfsizligini ta’minlashga qaratilgan zamonaviy yo‘nalishdir.

        📚 Kurs davomida:
        • Tarmoq xavfsizligi asoslari
        • Ma’lumotlarni himoyalash
        • Xakerlik hujumlariga qarshi kurash
        • Real loyihalar va laboratoriya ishlari

        👨‍🏫 Tajribali mutaxassislar yordamida siz kiber tahdidlardan himoyalanish va 
        IT sohasida xavfsizlik bo‘yicha professional bilimga ega bo‘lasiz.
            """)
    elif kurslar[7] == T:
        if menu[0] == "🤖 Robototexnika":
            await msg.answer("""
        🤖 Robototexnika kursi

        Robototexnika — bu mexanika, elektronika va dasturlashni birlashtirib, 
        turli robot va avtomatlashtirilgan tizimlar yaratishni o‘rgatuvchi yo‘nalishdir.


        📚 Kurs davomida:
        • Robotlarning ishlash prinsiplari
        • Sensorlar va aktuatorlar bilan ishlash
        • Mikroprotsessor va mikrokontrollerlar
        • Dasturlash va robotlarni boshqarish
        • Amaliy loyihalar va mini-robotlar yaratish

        👨‍🏫 Tajribali mentorlar yordamida siz robototexnika sohasida 
        zarur bilim va ko‘nikmalarga ega bo‘lasiz, o‘z loyihalaringizni yaratishingiz mumkin.
            """)
    elif kurslar[8] == T:
        if menu[0] == "🧪 Laboratoriya":
            await msg.answer("""
        🧪 Laboratoriya amaliyotlari

        IT Live kurslarida laboratoriya mashg‘ulotlari talabalarni amaliy bilim bilan ta’minlaydi. 
        Bu mashg‘ulotlarda siz nazariy bilimlarni real loyihalarda qo‘llashni o‘rganasiz.

        📚 Laboratoriyada:
        • Kod yozish va test qilish
        • Robototexnika va AI loyihalarini qurish
        • Mobil va veb-ilovalarni amaliy sinovdan o‘tkazish
        • Mentorlar bilan birga real loyiha yaratish

        👨‍🏫 Tajribali mentorlar yordamida siz o‘rganayotgan yo‘nalishingiz bo‘yicha mustahkam amaliy ko‘nikmalarni olasiz.
            """)
    elif kurslar[9] == T:
        if menu[0] == "📱 SMM":
            await msg.answer("""
        📱 SMM (Social Media Marketing) kursi

        SMM kursi — bu ijtimoiy tarmoqlarda brendni targ‘ib qilish, auditoriya bilan ishlash va marketing strategiyalarini yaratishni o‘rgatadi. 
        Kurs orqali siz zamonaviy digital marketing ko‘nikmalariga ega bo‘lasiz.

        📚 Kurs davomida:
        • Ijtimoiy tarmoqlar strategiyasi
        • Kontent yaratish va rejalashtirish
        • Reklama kampaniyalarini boshqarish
        • Analitika va natijalarni tahlil qilish
        • Real loyihalar ustida amaliy ishlar

        👨‍🏫 Tajribali mentorlar yordamida siz SMM sohasida professional bilim va amaliy ko‘nikmalarni egallaysiz, brendingizni rivojlantira olasiz.
            """)
    elif kurslar[10] == T:
        if menu[0] == "⚙️ DevOps":
            await msg.answer("""
        ⚙️ DevOps kursi

        DevOps — bu dasturiy ta’minot ishlab chiqish va uni serverlarga joylashtirish jarayonini birlashtiradigan zamonaviy IT yo‘nalishi. 
        Kurs orqali siz dastur ishlab chiqishdan tortib, uni doimiy ishlashini ta’minlashgacha bo‘lgan jarayonlarni o‘rganasiz.

        📚 Kurs davomida:
        • CI/CD (Continuous Integration / Continuous Deployment) asoslari
        • Server va bulutli texnologiyalar bilan ishlash
        • Avtomatlashtirish va monitoring
        • Docker, Kubernetes va boshqa zamonaviy vositalar
        • Real loyihalar ustida amaliy ishlar

        👨‍🏫 Tajribali mentorlar yordamida siz DevOps sohasida professional ko‘nikmalarni egallab, IT tizimlarini samarali boshqarish imkoniga ega bo‘lasiz.
            """)
    elif kurslar[11] == T:
        if menu[0] == "🛠 Arduino":
            await msg.answer("""
        🛠 Arduino kursi

        Arduino kursi — bu elektronika va dasturlashni birlashtirib, turli qurilmalar va robotlar yaratishni o‘rgatuvchi yo‘nalishdir. 
        Kurs orqali siz mikrokontrollerlar yordamida loyihalarni yaratishni o‘rganasiz.
📚 Kurs davomida:
        • Arduino asoslari va dasturlash
        • Sensorlar va aktuatorlar bilan ishlash
        • Elektron sxemalar yaratish
        • Real loyihalar va mini-robotlar qurish
        • Amaliy mashg‘ulotlar

        👨‍🏫 Tajribali mentorlar yordamida siz Arduino yordamida real loyihalarni yaratish va elektron qurilmalarni boshqarish ko‘nikmalarini egallaysiz.
            """)

    elif kurslar[12]==T:
        await msg.answer('Bosh menu',reply_markup=Menu)


        
@dp.message()
async def message_handler(msg:Message):
    T=msg.text
    if T.lower()=='seni kim yaratgan'or T.lower()=='seni kim yasagan':
        await msg.answer('Asadbek')
    else:
        await msg.answer('Salom')


async def main():
    bot=Bot(token=API)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
