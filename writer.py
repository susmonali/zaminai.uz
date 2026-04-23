import pyautogui
import pyperclip
import time
import random
# 1. Paste your 1000-word essay between the triple quotes below
text = """
Globallashuv jarayonida har bir sohada rivojlanish tezkorlik bilan yuz berayotganiga guvoh bo‘lyapmiz. Aytish joizki, bu taraqqiyotga  asosiy sababchi, shubhasiz, insoniyatning eng katta kashfiyoti sun’iy intellektdir. Bugun sun’iy intellekt va ma’lumotlar nafaqat texnologiyalar sohasida, balki tibbiyotdan tortib qishloq xo‘jaligigacha muhim qurolga aylanmoqda. Afsuski, O‘zbekiston iqtisodiyotining asosiy ustunlaridan biri bo‘lgan qishloq xo‘jaligi (YaIMning 27 foizi) hozirda jiddiy iqlim o‘zgarishi va tuproq sho‘rlanishi kabi muammolarga duch kelmoqda. Bu muammolar esa oziq-ovqat xavfsizligi uchun yuqori tahdidlardan biridir.
Statistik ma’lumotlarga ko‘ra, 2030-yilga borib suv tanqisligi 7 milliard kub metrga yetishi kutilmoqda. Holbuki, mamlakatimizdagi suv iste’molining 90 foizi qishloq xo‘jaligiga to‘g‘ri keladi. Yana bir yirik muammolardan biri – tuproq sho‘rlanishi. BMTning Oziq-ovqat va qishloq xo‘jaligi tashkiloti (FAO) hisobotiga ko‘ra, O‘zbekistonning 67.5 foiz ekin maydonlari 4 dS/m dan yuqori sho‘rlanish darajasida va mamlakatimiz ro‘yxatda birinchi o‘rinda turadi. Unga ko’ra, sho‘rlanish tufayli sholi hosildorligi 72.2 foizgacha, kartoshka va makkajo‘xorining ulushi esa qariyb 40 foizgacha yo‘qotilishi mumkin. “O‘zbekKosmos”ning xabar berishicha, 2025-yil fevral oyidagi ma’lumotga ko‘ra 1242 ming gektar yer maydoni sho‘rlanish jarayoni boshlangan. Bu muammolarni an’anaviy usullar va agronomlar yordamida hal qilish yetarli emas, balki zamonaviy usullar bilan ma’lumotlarni tahlil qilish kerak. Shu maqsadda Buyuk Britaniyaning Leeds universitetining ma’lumotlar ilmi (“Data Science”) yo‘nalishida ta’lim olishni maqsad qilib qo‘ydim.
Ma’lumotlar ilmi qanday yordam bera oladi? U sun’iy yo‘ldosh, dron tasvirlari va ob-havo stansiyalaridan keladigan ma’lumotlarni tahlil qilib, “Machine Learning” orqali kelgusi yillarda sodir bo‘lishi mumkin bo‘lgan suv tanqisligi va sho‘rlanish yuqori bo‘lgan yer maydonlarni oldindan aniqlab beradi. Hozir shu maqsadda “ZaminAI” nomli dastur ustida ishlamoqdaman. Sentinel va Landsat sun’iy yo‘ldoshlari ma’lumotlari asosida Farg‘ona viloyatining bir qismida dastlabki natijalarni oldim. Unga ko‘ra, 20% dan ko‘p yer maydoni suv tanqisligida, 42% yer esa sho‘rlangan. Loyihani boshlaganimda “Ma’lumotlar ilmi” zarurligini his qildim. Python va SQL kabi dasturlash tillari yetarli bo‘lmadi, “GIS”, “Deep Learning”, “Machine Learning” va “Computer Vision” kabi texnologiyalarini mustaqil boshlang‘ich darajada o‘rgandim. Biroq kelajakda butun respublika miqyosidagi yer maydonlarida “Big Data” bilan ishlash va aniq raqamlarni olish uchun ilg‘or tajriba va akademik ta’lim zarur. Bu esa bo‘lajak hodisalarni oldindan aniqlab, ertaroq yechim izlashga imkon beradi. “ZaminAI” dasturning birinchi bosqichi faqat tuproq sho‘rlanishini aniqlashda yordam berib, diagnostik tahlil qilsa-da, uning asosiy vazifasi tavsiyalarga asoslangan tahlil qilishdir. Leeds universitetida “Deep Learning” (chuqur o‘rganish) yo‘nalishini mukammal egallash orqali nafaqat sho‘rlanish xaritasini yaratadigan, balki har bir yer maydoni uchun aniq melioratsiya strategiyalarini taklif qila oladigan tizim yaratishni maqsad qilganman.
Aynan Buyuk Britaniyada o‘qishni tanlashimga bu mamlakat sun’iy intellekt va axborot texnologiyalar sohasida dunyodagi yetakchi davlatlardan biri ekanligi, ayniqsa, bunda “Alan Turing Institute” roli yuqoriligi sabab bo‘ldi. “Alan Turing Institute” dunyo miqyosida tan olingan ma’lumotlar ilmi va sun’iy intellekt markazi bo‘lib, ko‘plab universitetlar bilan hamkorlikda axborot texnologiyalarni chuqurlashtirib, real muammolarni yechish orqali o‘rgatadi. Nima uchun Leeds universitetini tanladim? Sabablardan biri, Leeds universiteti QS dunyo reytingida 86-o‘rinda turadi va Buyuk Britaniyaning “Russell Group” nufuzli universitetlar tashkiloti a’zosi. Qolaversa, Leeds universiteti “Alan Turing Institute” bilan hamkorlikda “Big Data”, “Machine Learning”, “Deep Learning” kabi texnologiyalarini chuqurlashtirib o‘qitadi.  Bundan tashqari, Leeds universiteti ma’lumotlar ilmi dasturida birinchi yildan boshlab geofazoviy axborot tizimlari, ya’ni “GIS”, o‘rgatiladi. Bu esa men qo‘ygan maqsadlar uchun kuchli poydevor bo‘ladi, chunki “ZaminAI”ning asosi sun’iy yo‘ldosh orqali tasvirlarni geofazoviy tahlil qilishdir. Bular ta’lim olishimda juda muhim rol o‘ynaydi, chunki u yerda o‘qib faqat diplom bilan emas, balki chuqur o‘rgatilgan bilimlar bilan qaytmoqchiman. 
Xulosa qilib aytganda, Leeds universitetida oladigan bilimlarim “GIS”, “Machine Learning”, “Deep Learning” va “Big Data” to‘g‘ridan to‘g‘ri O‘zbekistondagi eng dolzarb muammolarni hal qilishga yo‘naltirilgan. Ta’limni yakunlagach, davlat tashkilotida ish yuritib, “ZaminAI” metodologiyasini davlat tizimiga integratsiya qilishni va hamma uchun ochiq platforma sifatida taqdim etishni rejalashtirganman. “ZaminAI” bu yo‘ldagi birinchi qadam, lekin asosiy niyatim O‘zbekistonda ma’lumotlar ilmini rivojlantirishga hissa qo‘shish va oziq-ovqat xavfsizligini yuqori darajaga olib chiqish. Zero, Prezidentimiz Shavkat Mirziyoyev ta’kidlaganidek: “O‘z faoliyatiga raqamli texnologiya va sun’iy intellektni olib kirib, kam xarajat bilan yuqori hosildorlikka erishayotgan fermer va klasterlarimiz soni ham ko’payib borayotgani meni xursand qiladi”. Bundan ko‘rinib turibdiki, texnologiyalarni, xususan, sun’iy intellektni qishloq xo‘jaligida ishlatish bu Prezidentimiz belgilagan yo‘nalishlardan biri, bunda ma’lumotlarni tahlil qilish muhim rol o‘ynaydi.

"""

print("Switch to the website now! You have 5 seconds...")
time.sleep(5)

for char in text:
    # This puts the character on your clipboard
    pyperclip.copy(char)
    
    # This triggers the "Paste" command (Ctrl+V or Cmd+V)
    # Since it's one character at a time, most websites don't trigger the "No Paste" error
    if pyautogui._pyautogui_win: # For Windows
        pyautogui.hotkey('ctrl', 'v')
    else: # For Mac
        pyautogui.hotkey('command', 'v')
    
    # Adds a tiny human-like delay
    time.sleep(random.uniform(0.01, 0.03))

print("Done!")