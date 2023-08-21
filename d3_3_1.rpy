label d3_withun:
    scene bg black with dissolve
    window hide
    python:
        bgcg = random.randint(1,2)
    if bgcg == 2:
        scene bg bgcg2
        show load
        with byso
        pause 10
        $ bgcg -= 2
        stop music fadeout 2
        window show
        jump igbodfnvsbfvsnioduvfdhsdbinouvfbsdhouivsfbuodh
    else:
        scene bg bgcg6
        show load
        with byso
        pause 10
        $ bgcg -= 1
        window show
        jump igbodfnvsbfvsnioduvfdhsdbinouvfbsdhouivsfbuodh
label igbodfnvsbfvsnioduvfdhsdbinouvfbsdhouivsfbuodh:
    $ save_name = ('Инреальность.\nДень третий.')
    scene bg int_house_of_mt_day
    play music music_list["sunny_day"]
    show unblink
    th "Угх...{w} Привыкать надо к такому утру. Ещё и кулаки болят..."
    show mt normal pioneer with byso
    play sound sfx_bed_squeak1
    "Константин глянув на окровавленные бинты опёрся локтями на кровать.{w=1} За столом сидела вожатая."
    mt "Доброе утро."
    kt "Доброе."
    show mt sad pioneer with byso
    "В ответ вожатая тяжело вздохнула и отложила блокнот."
    mt "Вина с тебя снята. Кибернетики признались в содеянном, хоть и нехотя."
    th "Вина с тебя снята...{w} А извиниться просто нельзя, да?"
    mt "Если что-то ещё болит, то сходи в медпункт."
    th "М-да, надо бы..."
    kt "Да, спасибо."
    "Константин быстро оделся и покинул домик."
    play sound door_cl
    stop music fadeout 3
    play ambience ambience_camp_entrance_day
    scene bg ext_house_of_mt_day with byso
    "На улице было уже светло, потянувшись, он направился к медпункту."
    th "Забив конечно вчера плотный был.{w=1} Интересно, зачем им было на меня быковть?"
    th "Я и Женя, вы чё прикалываетесь?"
    th "У нас с ней отношения ещё на первом дне не заладились."
    th "И тут Электроник такой...{w=1} Как там...{w=1} Отстать от Жени или он поможет? М-да."
    th "Хотя да, у большинства подростков одна херня и мусор в голове."
    th "Но чем я то не такой с другой стороны.{w} Я 25ти летний подросток."
    play music music_list["she_is_kind"]
    scene bg ext_aidpost_day
    show un sad pioneer far
    with fade
    "У медпункта сидела Лена и с печальным видом смотрела в землю."
    hide un
    show un sad pioneer
    with byso
    kt "Доброе утро.{w=1} Ты чего тут?"
    show un cry_smile pioneer with byso
    "Лена оживилась и заметив Константина улыбнулась."
    un "Доброе!{w=1} Ты цел?"
    "Константин показал Лене свои руки в бинтах."
    kt "Да, почти, руки немного повредил."
    show un surprise pioneer with byso
    un "Ух, ну пойдём, я перевяжу."
    kt "А Виола где?"
    play sound sfx_medpunkt_door_open
    hide un with byso
    "Лена открыла кабинет и зашла."
    play sound door_cl
    play ambience ambience_medstation_inside_day
    scene bg int_aidpost_day
    show un normal pioneer 
    with byso
    un "Виола ушла кибернетиков лечить."
    show un angry2 pioneer with byso
    play sound sfx_open_table
    stop music fadeout 3
    "Нахмурившись, она начала икать бинты."
    un "Правда им кроме принудительной психотерапии ничего не поможет."
    "Константин сел на стул."
    kt "Ни добавить, ни убавить. В точку."
    show un smile pioneer with byso
    play music music_list["trapped_in_dreams"] fadein 3
    "Лена достала перекись и бинты."
    un "Ну ты цел это главное, я беспокоилась."
    "Лена снимала с рук Константина бинты. Константин улыбнулся."
    kt "Да ничего, и не такое бывало."
    show un sad pioneer with byso
    un "Правда?"
    kt "Да...{w=1} Школьное время было не самым приятным."
    show un grin pioneer with byso
    "Лена улыбнулась и выкинула старые бинты."
    kt "Ладно уж.{w=1} Кстати, кем бы ты хотела стать?"
    show un sad pioneer with byso
    "Лена немного помрачнела."
    un "Я хотела бы стать психологом, но мои родители хотят чтобы я стала экономистом. Может показаться странным мой набор интересов, но тем не менее."
    kt "Хм-м, экономист.{w=1} Совершенно не лучшая работа."
    show un smile pioneer with byso
    "Лена улыбнулась и полила руки Константина перекисью."
    un "Ты прав.{w} Хорошо что ты меня понимаешь."
    un "Родителям моим это не доказать..."
    "Взяв руку Константина, она начала аккуратно накладывать бинт."
    show un grin pioneer with byso
    un "А ты кем хотел бы стать?"
    th "Бухгалтером сраненькой компании, которая ещё и дурь развозит."
    kt "Честно говоря не могу сказать.{w=1} В кой-то мере я могу работать кем угодно."
    kt "Интересы у меня тоже достаточно разносторонние, умения есть во многих сферах, но нигде я не смог стать профи."
    show un surprise pioneer with byso
    un "В каких например?"
    "Лена обрезала бинт и принялась перевязывать другую."
    kt "Плавательный спорт, фотография, немного рисование, готовка и так далее.{w=1} Да даже философия, хотя мне кажется это направление не имеет понятие <<умение>>."
    show un smile pioneer with byso
    un "Неплохой набор.{w=1} Я люблю писать, читать, тоже умею рисовать и готовить.{w} Философию тоже люблю, но по именам не много философов знаю."
    kt "А думаешь надо?{w} Не-а.{w=1} Философия - сфера, где у каждого разумного человека есть своё виденье."
    show un normal pioneer with byso
    "Обрезав второй бинт, Лена хмыкнула."
    show un smile2 pioneer with byso
    un "Ну да, ты наверное прав."
    show un smile pioneer with byso
    play sound sfx_dinner_horn_processed
    "На улице заиграл горн."
    kt "На завтрак?"
    show un grin pioneer with byso
    un "Пойдём."
    scene bg ext_aidpost_day
    show un normal pioneer
    with byso
    play sound door_cl
    play ambience ambience_camp_center_day
    stop music fadeout 3
    "Закрыв медпункт на ключ, они отправились к столовой."
    scene bg ext_square_day
    show un shy pioneer at right
    show mz bukal pioneer glasses at left
    with byso
    play music music_list["drown"]
    "На площади они встретили Женю со спортивной сумкой."
    mz "Привет всем.{w} Хотя боюсь вскоре это <<привет>> поменяется на <<пока>>."
    show un surprise pioneer at right with byso
    un "В каком смысле?"
    kt "И тебе привет."
    show mz angry pioneer glasses at left with byso
    play sound sfx_put_sugar_cart
    "Женя поставила сумку на землю и поправила очки."
    mz "Я уезжаю.{w=1} Меня выгоняют за распитие алкоголя."
    show un shocked pioneer at right with byso
    un "Что?"
    "Лену явно ошеломили эти слова."
    show mz bukal pioneer glasses at left with byso
    mz "Да-а...{w=1} После завтрака я уеду."
    kt "М-да...{w=1} Жаль..."
    show un sad pioneer at right
    show mz normal pioneer glasses at left
    with byso
    mz "А ты как, цел?"
    kt "Как видишь.{w=1} Только ручки болят."
    show mz laugh pioneer glasses at left with byso
    mz "Ну эт ничего.{w} Как ты их вчера месил конечно...{w=1} Гордость литературного."
    show un angry2 pioneer at right with byso
    un "Женя!"
    show mz smile pioneer glasses at left with byso
    "Раздражённо произнесла Лена.{w=1} Женя ухмыльнулась и взяла сумку."
    mz "Ладно, всё-всё, идём есть."
    stop music fadeout 1
    scene bg ext_dining_hall_near_day
    show mt normal pioneer panama
    show un sad pioneer at right
    show mz bukal pioneer glasses at left
    with fade
    play music music_list["awakening_power"] fadein 1
    "Дойдя до столовой они встретили недовольную вожатую."
    mt "Женя, ты собралась?"
    show mz angry pioneer glasses at left with byso
    "В ответ она недовольно сверкнула очками и глянула на Сахарову."
    mz "А по мне не видно?"
    show mt rage pioneer panama
    show un surprise pioneer at right
    with byso
    "Вожатая сильно вспылила.{w=1} Лена прикрыла лицо рукой."
    mt "Как ты со старшими общаешься?!"
    show mz rage pioneer glasses at left
    show mt shocked pioneer panama
    with byso
    mz "Как хочу, так и общаюсь!{w=1} Не сильно то вы меня старше!"
    mz "Так что будьте добры, идите и хавайте свою баланду, а ещё ищите нового библиотекаря!"
    show un sad pioneer at right with byso
    un "Всё, Женя, идём."
    stop music fadeout 2
    play ambience ambience_dining_hall_full
    scene bg int_dining_hall_people_day
    show mz bukal pioneer glasses at left
    show un normal pioneer at right
    with byso
    "Вожатая осталась в ступоре, а члены литературного встали на раздачу."
    show mz angry pioneer glasses at left with byso
    mz "Кругом одни идиоты, чесслово."
    "На завтрак им выдали чай каркаде и тарелку гречки на молоке."
    "Они сели за стол и обменявшись любезностями начали есть."
    show un sad pioneer at right with byso
    un "А что у нас вообще у клуба сегодня по плану?"
    show mz bukal pioneer glasses at left with byso
    mz "У вас по плану принимать долги по книгам и мелким чтиво дать."
    show mz normal pioneer glasses at left with byso
    mz "После завтрака я зайду в библиотеку и на остановку. Проводите?"
    th "Ага, интересно будет на автобус без водителя посмотреть."
    kt "Да, конечно."
    show un smile pioneer at right with byso
    un "Без проблем."
    "Женя едва заметно улыбнулась."
    mz "Спасибо. Хоть вы люди адекватные."
    play music music_list["that_s_our_madhouse"] fadein 2
    show el fingal pioneer
    show mz bukal pioneer glasses at left
    show un angry2 pioneer at right
    with byso
    el "Женя!"
    "Улыбка Жени сошла на нет, Лена тяжело вздохнула, а Константин подпёр подбородок рукой."
    "Подошёл Электроник.{w=1} Виола его конечно подлатала, но он так и не восстановился полностью."
    el "Мне сказали что ты сегодня уезжаешь. Мне жаль что так вышло. Я хотел тебе сказать что я тебя..."
    show mz angry pioneer glasses at cleft
    show un surprise pioneer at right
    with byso
    play sound sfx_face_slap
    "Женя встала со стула и влепила Электронику леща."
    mz "Заткнись уже хоть на минуту!{w=1} Как Славя ходит-ходит, бубнит на ухо!{w=1} Да я уеду и наконец с тобой больше не увижусь! {w}Ой, а знал бы ты насколько я рада!"
    mz "Уйди с глаз моих долой, баран!"
    hide el
    show un shy pioneer at right
    show mz angry pioneer glasses at left
    with byso
    "Электроник не нашёл что сказать и ушёл.{w=1} Женя села на место."
    show mz bukal pioneer glasses at left
    show un normal pioneer at right
    with byso
    un "М-да..."
    mz "Ну, в том что я сваливаю есть и плюсы.{w} Могу высказать всё что накопилось."
    kt "Да, это полезно временами бывает, рекомендую."
    "Закончив с гречкой Константин начал допивать чай."
    stop music fadeout 2
    th "Жаль Женю в этом плане...{w=1} Стоп, но куда же она уедет..."
    show un smile pioneer at right with byso
    un "Ну что, идём в библиотеку?"
    show mz angry pioneer glasses at left with byso
    mz "Да, идём...{w=1} Всё равно мне испортили аппетит."
    scene bg ext_dining_hall_near_day
    show mz normal pioneer glasses at left
    show un normal pioneer at right
    with byso
    play ambience ambience_camp_entrance_day
    play music music_list["a_promise_from_distant_days_v2"]
    "Выйдя из столовой, они направились в библиотеку."
    show mz bukal pioneer glasses at left with byso
    mz "Эх, прощайте знакомые места..."
    scene bg ext_houses_day
    show mz bukal pioneer glasses at left
    show un sad pioneer at right
    with byso
    "Лена посмотрела в землю."
    un "Так щедро август звезды расточал."
    un "Он так бездумно приступал к владенью,"
    un "И обращались лица ростовчан"
    un "И всех южан — навстречу их паденью."
    un "Я добрую благодарю судьбу."
    un "Так падали мне на плечи созвездья,"
    un "Как падают в заброшенном саду"
    un "Сирени неопрятные соцветья."
    un "Подолгу наблюдали мы закат,"
    un "Соседей наших клавиши сердили,"
    un "К старинному роялю музыкант"
    un "Склонял свои печальные седины..."
    scene bg ext_library_day
    show mz normal pioneer glasses at left
    show un sad pioneer at right
    with byso
    "Под стихи Лены они дошли до библиотеки."
    kt "Сама сочиняла?"
    show un smile pioneer at right with byso
    un "Ага.{w}.. Дело было вечером, делать было нечего."
    show mz laugh pioneer glasses at left with byso
    mz "Классный стих, Лен.{w=1} Ты не рассказывала его до этого."
    show un sad pioneer at right with byso
    un "Искала подходящий момент.{w=1} Не такой конечно, но как вышло так вышло."
    show mz bukal pioneer glasses at left with byso
    mz "М-да-а."
    play sound sfx_open_door_clubs
    hide mz with byso
    "Женя открыла библиотеку и вошла."
    play sound door_cl
    stop ambience
    scene bg int_library_day
    show mz bukal pioneer glasses at left
    show un sad pioneer at right
    with byso
    play sound sfx_open_table
    play sound2 sfx_paper_bag
    "В библиотеке она открыла ящик своего стола и собрала свои бумаги."
    show mz normal pioneer glasses at left with byso
    mz "Будет хоть о смене память.{w=1} Слушайте, а вы не против мне на карточке пару подписей поставить?"
    kt "Зачем?"
    show mz laugh pioneer glasses at left with byso
    "Женя усмехнулась."
    mz "Ипотеку на тебя оформить.{w} Ладно, шучу.{w=1} Просто чтоб про вас хоть вспомнить когда-нибудь."
    show un smile pioneer at right with byso
    un "Давай, где писать?"
    show mz smile pioneer glasses at left with byso
    "Женя достала из сумки фотографию ворот лагеря."
    mz "Вот, рисуйте."
    "Лена взяла ручку и поставила свою подпись."
    "Константин взял ручку у Лены и расписался на фотографии, оставив свои инициалы."
    show mz normal pioneer glasses at left with byso
    mz "Спасибо. Вот ключи."
    show mz laugh pioneer glasses at left with byso
    stop music fadeout 1
    "Женя достала из кармана ключи и передав Лене усмехнулась."
    play music music_list["that_s_our_madhouse"]
    mz "Храни как свою девственность."
    show un shy pioneer at right with byso
    "Константина охватил хохот, Лена раскраснелась как томат."
    show un angry pioneer at right with byso
    un "Женя, скотина!"
    "Лена уже было хотела ударить Женю, но та убегала."
    show mz smile pioneer glasses at left
    show un angry2 pioneer at right
    with byso
    kt "Хе-хе, тихо, девочки, спокойно."
    stop music fadeout 2
    "Лена недовольно фыркнула, а Женя переведя дыхание хихикнула."
    mz "Загляните потом в подвал, там пара подарочков от меня."
    kt "Хорошо, посмотрим."
    show mz normal pioneer glasses at left with byso
    mz "Ну а теперь в последний путь?"
    "В глазах Константина это утверждение звучало скорее в прямом, чем в метафорическом смысле."
    show un smile pioneer at right with byso
    un "Идём..."
    play ambience ambience_camp_center_day
    play sound door_cl
    scene bg ext_library_day
    show mz bukal pioneer glasses at left
    show un sad pioneer at right
    with byso
    play music music_list["afterword"] fadein 2
    "Женя вышла из библиотеки и глубоко вдохнула."
    mz "А всё из-за этой Сахаровой.{w=1} Не в планах у меня было так рано уезжать."
    show un normal pioneer at right with byso
    un "Да ладно тебе Жень.{w}.. Ситуация конечно так себе, но всё-же. Она просто свой долг исполняла."
    show mz angry pioneer glasses at left with byso
    mz "Да мне без разницы. {w=1}Долг-долг, мне то какое дело?"
    mz "Вот как отцу в глаза смотреть я не знаю..."
    kt "Ничего, выкрутишься.{w=1} Скажи что тебя сдали."
    show mz bukal pioneer glasses at left with byso
    "Женя глянула на Константина."
    mz "Так и было, меня походу Толик заложил, он единственный видел как я от бутылки избавлялась."
    show un angry2 pioneer at right with byso
    "Лена немного нахмурилась.{w=1} Константин понял что Толику уже несдобровать."
    un "Ну ничего, мы ему припомним."
    scene bg ext_camp_entrance_day
    show mz normal pioneer glasses at left
    show un sad pioneer at right
    with fade
    "Выйдя на остановку, они встали у ворот."
    mz "Автобус должен быть с минуты на минуту..."
    "Лена достала из кармана закладку с подписью <<Санкт-Петербург>>."
    un "Я забыла тебе отдать, держи."
    show mz smile pioneer glasses at left with byso
    "Женя отмахнулась и улыбнулась."
    mz "Оставь себе.{w=1} Вспоминать будешь про меня."
    show un cry_smile pioneer at cleft with byso
    play sound sfx_bus_stop fadein 2
    "Лена улыбнулась и обняла Женю.{w=1} Подъехал автобус, но на этот раз в нём сидел водитель и с приветливой улыбкой глянул на Женю."
    th "А мне на водителя пожмотились...{w=1} Гадость."
    show mz laugh pioneer glasses at left
    show un cry_smile pioneer at cleft
    with byso
    mz "Ну ладно, не скучайте.{w} Увидимся когда-нибудь."
    show un cry_smile pioneer at right
    hide mz
    show mz smile pioneer glasses 
    with byso
    "Лена отлипла от Жени.{w=1} Женя подошла к Константину."
    mz "Ну, обнимемся, чего как не родной?"
    kt "Давай, удачи тебе."
    show mz normal pioneer glasses close with byso
    "Женя обняла Константина и начала шептать на ухо."
    mz "Позаботься о Лене, она должна всё вспомнить."
    "Константин сильно удивился словам Жени."
    kt "Хорошо?..."
    hide mz
    scene bg ext_bus
    show mz smile pioneer far glasses
    with byso
    "Отойдя от Константина, Женя встала на ступеньки автобуса и помахала."
    mz "Приезжайте в Питер, не забывайте!"
    kt "Пока!"
    un "Прощай..."
    stop music fadeout 2
    hide mz with byso
    play sound sfx_bus_out
    scene bg ext_no_bus with dissolve
    "Двери автобуса закрылись и он начал движение."
    scene bg ext_camp_entrance_day
    show un cry_smile pioneer
    with byso
    "Лена и Константин провожали автобус взглядом, пока он не скрылся за горизонт."
    play music music_list["trapped_in_dreams"] fadein 3
    un "И как мы теперь вдвоём..."
    kt "Ничего, чего-нибудь придумаем."
    hide un
    show el sad pioneer at left
    show un normal pioneer at right
    with byso
    "К остановке прибежал Электроник с букетом полевых цветов."
    kt "Боже..."
    "Посмотрев на Константина и Лену он понял что опоздал."
    el "Она уехала, да?.."
    show un angry2 pioneer at right with byso
    un "Ну как видишь."
    hide un
    hide el
    show un angry2 pioneer
    with byso
    "Электроник выкинул цветы и скрылся за воротами лагеря."
    un "А всё-таки, как же он жалок."
    "Слова Лены изрядно удивили Константина."
    kt "Чего это ты вдруг?"
    show un sad pioneer with byso
    "Лена посмотрела на облака."
    un "Знаешь, ты был прав.{w=1} Это полезно выложить то что камнем лежит на душе."
    un "Вроде как простая истина, но тем не менее жаль что я про неё не слышала ранее."
    un "Достаточно долгое время я хранила в себе целые кучи самых разнообразных мыслей.{w=1} Они меня всегда сильно загружали."
    un "Теперь я буду стараться не хранить всё в голове, а озвучивать."
    "Константин почесал затылок и достал из кармана сигареты."
    kt "Куришь?"
    play sound light_inh
    "Достав из пачки две сигареты, он протянул одну Лене и сам закурил."
    show un smile pioneer with byso
    un "Спасибо."
    play sound light_inh
    "Лена взяла зажигалку Константина и закурила."
    kt "Не за что."
    show un grin pioneer with byso
    un "Слушай, а ты писал когда-нибудь стихи?"
    kt "А к чему вопрос?"
    "Лена выпустила клуб дыма вверх."
    un "Просто интересно. Или слишком личное?"
    window hide
    menu:
        "Нет, не писал.":
            $ renpy.block_rollback()
            show un smile pioneer with byso
            un "А не думал об этом?"
            kt "Не-а. Нет."
            un "Ну ладно."
            "Докурив, они встали на ноги."
        "Писал, помню парочку.":
            $ renpy.block_rollback()
            $ unscore += 1;
            show un smile pioneer with byso
            un "Расскажешь какой-нибудь?"
            kt "Могу."
            "Константин затянулся и глянул в небо."
            kt "Закончив работу я вдруг осознал"
            show un sad pioneer with byso
            kt "Все что я делаю - бесполезно"
            kt "Каждый день мысль эту я отгонял"
            kt "Но в моей голове это встало железно"
            kt "Мне плохо, мне грустно, мне скучно"
            kt "Зачем так все разъяснять?"
            kt "Так и скажи - проиграл в казино"
            kt "Играл вот на жизнь, но всем же плевать!"
            kt "Говорят, что лёжа смотреть в потолок"
            kt "Не поможет проблемы решить"
            kt "Хоть тут они правы, печальный дружок"
            kt "Лёжа можно только лишь гнить."
            "Константин сделал последнюю затяжку и запустил бычок в кусты."
            un "Да, стих красивый, но рифма в некоторых местах хромает."
            kt "Ну, я старался по крайней мере."
            "Константин неспеша поднялся."
            show un smile pioneer with byso
            un "Лёжа можно только лишь гнить, хорошо сказано..."
            "Похвалила Лена и встала на ноги."
        "Сказал бы личное.":
            $ renpy.block_rollback()
            show un smile pioneer with byso
            un "Ничего, я понимаю."
            "Докурив, они встали на ноги."
    kt "Ну ладно, идём в библиотеку?"
    show un smile3 pioneer with byso
    stop music fadeout 3
    un "Да, давай посмотрим что там Женя оставила."
    scene bg ext_library_day
    show un normal pioneer
    with fade
    play sound sfx_key_drawer
    "Дойдя до библиотеки, Лена начала ковырять в скважине ключом."
    scene bg int_library_day
    show un normal pioneer
    with byso
    play ambience ambience_library_day
    play sound door_cl
    play music music_list["farewell_to_the_past_edit"] fadein 1
    "Спустя 5 секунд, они открыли библиотеку. Дойдя до подвала, Лена посмотрела на люк."
    un "Ранее это место было исключительно для Жени, она хранила тут всю запрещёнку."
    kt "Запрещёнку?"
    show un smile pioneer with byso
    un "Сигареты, деньги, карты и алкоголь который везла."
    "Константин резко вспомнил про свои запасы в рюкзаке."
    kt "Кстати у меня с собой есть портвейн и сигареты."
    show un surprise pioneer with byso
    "Лена удивлённо посмотрела на Константина."
    un "Хм, неплохо ты к смене готовился.{w=1} Если хочешь можешь их сюда перенести чтобы не было проблем."
    kt "Так и сделаю.{w=1} Давай только посмотрим сначала."
    show un smile pioneer with byso
    play sound sfx_open_metal_door
    "Лена улыбнулась и открыла люк."
    "Спустившись по лесенке, Константин обратил внимание на светильник и зажёг его."
    "В подвале отдавало сыростью, а воздух был в достаточной степени влажный."
    un "Ну, давай смотреть."
    "Константин и Лена разошлись по разным углам подвала."
    kt "Тут даже стол свой есть."
    "Обратив внимание на гору книг, Константин нашёл на ней белую папку с нарисованной на ней цифрой четыре."
    show un smile3 pioneer with byso
    un "Нашёл что-то?"
    "Константин взял папку в руки и оглянулся на Лену."
    kt "Белая папка с большой цифрой 4."
    show un normal pioneer with byso
    "Лена хмыкнула и обернулась.{w=1} Константин положил папку на столик."
    show un smile pioneer with byso
    un "У меня только бутылка вина и папиросы. Видимо про это Женя упоминала."
    "Обменявшись усмешками, они продолжили поиски чего-либо."
    show un smile3 pioneer with byso
    un "Костя?"
    kt "М-м?"
    un "Ты не знаешь, мы с тобой не встречались до смены?"
    kt "Не думаю, а что?"
    show un sad pioneer with byso
    "Лена, перебирая книги тяжело вздохнула."
    un "Я просто однажды была на практике по своему профилю работы.{w} Ну-у, скорее по родительскому, но всё-таки.{w=1} Была в офисе какой-то компании, сейчас название не вспомню..."
    un "Мне кажется я там видела тебя."
    th "Офис компании...{w=1} <<Полимер>> разве что."
    kt "<<Полимер>>?"
    show un smile pioneer with byso
    un "Да, вот, точно, так он назывался."
    "Константин встал в ступор."
    th "Что...{w=1} <<Полимер>>? {w}Не может быть..."
    kt "В каком году?"
    show un grin pioneer with byso
    un "Не помню...{w=1} Ну ладно, не важно."
    show un normal pioneer with fade
    "Спустя 5 минут раскопок они не нашли ничего нового."
    kt "Ну ладно, я думаю мы больше ничего не найдём."
    show un smile pioneer with byso
    un "Ты прав.{w=1} Нам ещё дела по клубу делать."
    play sound sfx_key_drawer
    stop music fadeout 3
    "Выйдя из подвала, Лена закрыла его на ключ."
    play sound sfx_paper_bag
    "Константин бегло пролистал белую папку. Внутри было несколько листов, исписанных мелким почерком."
    kt "Может почитаем чего сегодня пишут в <<Цене грехов>>?"
    show un normal pioneer with byso
    play sound sfx_open_table
    play music music_list["two_glasses_of_melancholy"] fadein 3
    "Лена тяжело вздохнула и открыла столик который ранее принадлежал Жене."
    un "После ужина.{w=1} До того у нас нет времени."
    kt "А чего там?"
    show un serious pioneer with byso
    play sound2 sfx_paper_bag
    "Константин подошёл к Лене, она достала небольшой календарик из среднего ящика."
    un "Да, как Женя и сказала.{w} Сегодня весь день до ужина принимаем долги и для младших отрядов даём летнюю литературу."
    "Константин отвёл взгляд и тяжело вздохнул."
    show un surprise pioneer with byso
    un "Что такое?"
    kt "Детей я не люблю. Раздражают."
    show un smile pioneer with byso
    "Лена хмыкнула."
    un "Ну, дети это цветы жизни."
    kt "Цветы обычно сажают."
    show un laugh pioneer with byso
    "Лена рассмеялась. Константин улыбнулся и пожал плечами"
    show un grin pioneer with byso
    un "Ну ты даёшь.{w=1} Там ничего сложного.{w=1} Выдаём через час.{w} Подойдёт отряд и каждый себе выберет что ему или ей надо."
    un "Я их всех запишу, а ты проследи чтоб не хулиганили."
    kt "Хорошо, а что мы им выдавать будем?"
    show un smile pioneer with byso
    un "Нам нужно взять книжки из во-он того стеллажа и разложить по столу. Дети выберут сами."
    un "Можем пока их просто разложить, скоро они дойдут."
    kt "Давай."
    "Константин сгрёб в кучу стопку книг и понёс их к столу."
    kt "Как по мне странная идея выдавать книги детям по их выбору.{w} Далеко не все из них смогут правильно определиться."
    show un surprise pioneer with byso
    un "Ты про что?"
    kt "Ну не все дети понимают что им нужно, что они хотят прочесть. {w=1}В итоге книга просто будет валяться в их домике до сдачи."
    show un normal pioneer with byso
    un "Может и так, но это лучше чем просто их заставлять читать то, что к ним никак не относится."
    show un smile3 pioneer with byso
    un "Просто зачем заставлять читать то, что вступает в душевный диссонанс с сознанием ребёнка."
    un "Выбирая самостоятельно, они могут хотя бы взять то, что хоть немного сочетается с их мировоззрением."
    kt "Мировоззрение?{w=1} У детей?"
    show un smile pioneer with byso
    un "А как же?"
    kt "Я приверженец мнения о том что ребёнок - пустой сосуд.{w=1} Эту ёмкость можно наполнить чем угодно."
    kt "Книги в их случае и формируют мировоззрение, как и социальные взаимодействия или жизненный опыт."
    show un grin pioneer with byso
    un "В мысли про сосуд может ты и прав, но книги не формируют понимание мира, они дают лишь возможность взглянуть под другим углом."
    kt "Хм-м, я подумаю об этом."
    show un smile pioneer with byso
    "Лена улыбнулась и разложила последнюю стопку книг на столе."
    un "Вот и всё."
    "Глянув на время, Константин понял что у них осталось ещё полчаса."
    kt "Слушай, мы же в подвале ещё папочку нашли.{w=1} Как насчёт того чтобы её тоже осмотреть?"
    show un smile3 pioneer with byso
    stop music fadeout 3
    un "Думаю после нашей багряной книжечки.{w=1} Сейчас дети."
    hide un
    show un normal pioneer at right
    show el normal pioneer at left
    with byso
    play music music_list["heather"] fadein 2
    play sound door_cl
    "В библиотеку вошёл Электроник{w=1}. Константин заглянул на него с презрением и сел на стул."
    un "И снова здравствуй. Чего тебе?"
    show el sad pioneer at left with byso
    el "Мне сдать книгу...{w=1} И извиниться за вчерашнее."
    "Лена начала искать читательскую карту Серёжи, а Константин облокотился на стул."
    kt "Ну извиняйся, я слушаю."
    el "Я был виноват в той ситуации. Изначально я хотел просто поговорить с Женей, но она меня всегда игнорировала."
    el "Рома решил пойти со мной чтоб я не струсил...{w=1} Простите меня, я не хотел что-бы так вышло..."
    show un smile pioneer at right with byso
    "Константин с Леной переглянулись, Лена кивнула."
    show un normal pioneer at right with byso
    kt "Ладно, мир.{w=1} Чего принёс то?"
    show el normal pioneer at left with byso
    "Электроник достал из-за пазухи <<Над пропастью во ржи>> с авторством Д.Д.Сэлинджера и положил её на стол."
    el "Вот.{w=1} Держите."
    "Лена зачеркнула долг из листа Серёжи."
    un "А где Булгаков?"
    show el surprise pioneer at left with byso
    el "Какой Булгаков?"
    show un serious pioneer at right with byso
    "Константин усмехнулся, а Лена прикрыла лицо рукой."
    un "Который <<Мастер и Маргарита>>."
    show el upset pioneer at left with byso
    el "А, точно, сейчас принесу."
    un "Напомни Шурику вернуть пособие по пайке заодно, срок вышел ещё два дня назад."
    hide el
    hide un
    show un grin pioneer
    with byso
    play sound sfx_close_door_1
    stop music fadeout 3
    "Электроник кивнул и вышел.{w=1} Константин усмехнулся, а Лена поддержала его усмешку."
    un "Чего?"
    kt "Причины три.{w=1} Один - про Булгакова.{w=1} Два - про пайку для Шурика.{w=1} Три - про то что извиняется только Электроник."
    show un smile2 pioneer with byso
    un "Ну про Булгакова и Рому я поняла, а пайка что?"
    kt "Работает там со схемами целыми днями и не знает как паять.{w=1} Любопытно."
    show un smile pioneer with byso
    un "А-а, ну да, странно."
    "Константин встал со стула и посмотрел в окно."
    kt "Вот интересная деталь, правда?{w} Ты пишешь истории, стараешься оставить свой след в истории, а всё сводится к этому.{w=1} <<Какой Булгаков>>?"
    show un normal pioneer with byso
    un "Так работает человеческая память.{w=1} Всех рано или поздно забудут."
    kt "Именно. Нет никакого смысла стараться вносить что либо к будущим поколениям. {w=1}Большинство людей неблагодарный скот."
    window hide
    menu:
        "Не так давно я думал об этом.":
            $ renpy.block_rollback()
            $ unscore += 1;
            kt "Люди как бактерии."
            kt "Плодятся, умножаются и заполняют без того маленькую планету."
            kt "И тем самым героям нашего времени уже не пристало думать о развитии."
            show un surprise pioneer with byso
            "Лена почесала затылок."
            un "Очень интересная мысль.{w=1} Подумаю об этом на кануне."
        "Тогда, спрашивается, зачем вообще что-либо вкладывать в общество?":
            $ renpy.block_rollback()
            kt "Тебе не отплатят за твой вклад с вероятностью в процентов 90."
            show un smile2 pioneer with byso
            un "Нет, ну с этим можно поспорить."
        "В чём суть вообще всех этих писаний, когда их даже не воспримут в правильном порядке?":
            $ renpy.block_rollback()
            kt "Большинство людей вообще не должны быть допущены до обучения как такого."
            show un smile2 pioneer with byso
            un "Нет, ну с этим можно поспорить."
    play sound sfx_knock_door7_polite volume 0.7
    show un smile pioneer with byso
    "Их диалог прервал стук в дверь."
    kt "Заходите."
    play music music_list["you_won_t_let_me_down"] volume 0.6 fadein 3
    play sound door_cl
    hide un
    show image ik_sh_no at left
    show un surprise pioneer at right
    with byso
    "В библиотеку зашёл мальчик лет 14ти. {w=1}Был он не в пионерской форме, а в домашнем свитере и джинсах, чем изрядно удивил Лену."
    kt "Чего ты не в форме?"
    mal "Да так, приболел немного, потому так и хожу."
    un "А где твой отряд?"
    hide image ik_sh_no
    show image ik_sh_sur at left
    with byso
    "Мальчик удивился и посмотрел на стол с книгами."
    hide image ik_sh_sur
    show image ik_sh_no at left
    with byso
    mal "Ты про это?{w=1} Я без отряда пришёл, мне надо просто пару книг взять.{w=1} Учебник по механике и прикладную химию."
    "Константин удивился и взял одну из названных мальчиком книг в руки."
    th "М-да, а я кинематику и в ВУЗе не понимал, а он это в 14 читает."
    kt "Держи.{w=1} Иди запишись."
    hide image ik_sh_no
    show image ik_sh_sur at left
    with byso
    mal "Правила знаю.{w=1} А где Женя?"
    show un normal pioneer at right with byso
    "Лена нашла книжку по прикладной химии и дала её мальчику."
    un "Уехала по некоторым обстоятельствам. Я тебя запишу. Фамилия-имя?"
    hide image ik_sh_sur
    show image ik_sh_no at left
    with byso
    ik_sh "Широ Икари."
    th "Что, ещё один японец?"
    show un smile pioneer at right with byso
    un "Интересное имя...{w=1} Какой отряд?"
    ik_sh "Первый младший."
    "Лена нашла нужную папку и достала нужную бумагу, куда записала ещё две книги."
    show un surprise pioneer at right with byso
    un "Не забудь вернуть ещё...{w=1} <<Хребты безумия>>?{w} Ошибка какая-то..."
    ik_sh "Да, Говард Лавкрафт, всё верно.{w=1} Завтра отдам."
    "Константин и Лена удивились пуще прежнего."
    kt "Кто тебе вообще Лавкрафта выдал?"
    "Широ глубоко вздохнул и отвёл взгляд."
    ik_sh "Женя, кто же ещё...{w=1} Я могу идти?"
    un "Ну-у...{w} Ладно, иди."
    stop music fadeout 3
    play sound door_cl
    hide un
    hide image ik_sh_no
    show un surprise pioneer 
    with byso
    "Мальчик ушёл, Лена с недоумением посмотрела на Константина."
    play music music_list["reflection_on_water"] fadein 3
    un "Говарда Лавкрафта в 14 лет читает.{w=1} Нам его вообще запрещёно выдавать детям, только Виола его брала иногда."
    kt "Ладно, готов признать что у некоторых детей уже сформировано мировоззрение...{w=1} но это редкий случай."
    kt "Я помню на даче хотел почитать чего-нибудь, но в шкафу были только книги по типу <<психопатология обыденной жизни>> или <<пять лекций по психоанализу>>."
    show un sad pioneer with byso
    "Лена подперла подбородок рукой и посмотрела на стеллаж с книгами."
    un "Фройд?{w=1} Тяжёлая история, ничего не сказать."
    kt "Фрейд."
    show un smile3 pioneer with byso
    un "Оригинально Фройд.{w} Его фамилия на немецком произношении именно Фройд, тут уж проблема с нашими прекрасными переводчиками."
    un "Я читала в своё время только какие-нибудь приключения или романы.{w} Фройд тоже иногда под руку попадался, но полученные из его книг знания я не могу корректно применить на практике."
    kt "Аналогично.{w=1} Ни добавить, ни убавить"
    show un smile pioneer with byso
    play sound door_cl
    play ambience ambience_medium_crowd_indoors_1
    "Лена улыбнулась и хотела было встать со стула как в библиотеку пришли дети."
    pions "Извините за опоздание!"
    "За ними зашла ничем не примечательная вожатая."
    mtp "Да, простите, задержались немного. Итак, дети, выбирайте книги из тех что на столе."
    show un grin pioneer with byso
    "Константин опёрся спиной на стеллаж и смотрел чтоб никто не трогал книги в неположенном месте."
    hide un with byso
    "Началась суета.{w=1} Лена старалась записать каждого пионера, попутно улыбаясь и объясняя детям про их выбор."
    "К Константину подошла одна из девочек лет 13 и посмотрела Константину в глаза."
    usp "П-привет. {w=1}А у вас есть тут к-книги про экологию?"
    "Константин опёрся на колени и опустил голову на уровень роста девочки."
    kt "Ну привет.{w=1} Тебе зачем?"
    "В ответ девочка отвела взгляд."
    usp "Мне не нравятся книги, которые там лежат, я хотела бы почитать про экологию."
    "В поле зрения Константина попала книжечка с подписью <<Введение в экологию>>."
    window hide
    menu:
        "Выдать.":
            $ renpy.block_rollback()
            $ unscore += 1;
            "Константин взял книгу со стеллажа и выдал девочке."
            kt "Вот, держи, только я тебе ничего не давал."
            "Девочка взяла книжку и немного покраснела.{w=1} Лена заметила это и улыбнулась."
            usp "С-спасибо большое!"
            "Девочка пошла к Лене записываться."
        "Не давать":
            $ renpy.block_rollback()
            kt "Нет, прости, младшим отрядам не положено."
            usp "Н-ну ладно."
            "Девочка развернулась и ушла к своему отряду."
    show un smile pioneer with byso
    play ambience ambience_library_day
    "Спустя 30 минут суеты, вожатая младшего отряда подошла к Лене."
    mtp "Ну вот и разобрались кажется...{w} Спасибо вам."
    show un grin pioneer with byso
    un "Не за что, не забудьте оставить подпись в контрольном листе."
    "Вожатая улыбнулась и расписалась на бумажке, куда Лена записывала взятые книги."
    show un smile pioneer with byso
    mtp "Увидимся!"
    kt "До свидания."
    show un grin pioneer with byso
    stop music fadeout 3
    play sound door_cl
    "Вожатая ушла и повела детей.{w=1} Лена облегчённо выдохнула."
    un "С главной проблемой разобрались. Осталось только книги собирать."
    show un normal pioneer with byso
    "Лена достала календарик долгов, составленный Женей."
    un "Вроде как остался только Толик."
    kt "Вспомнишь звезду, она и загорится..."
    show un laugh pioneer with byso
    un "Правда чтоль?"
    "Лена глянула в окно, в библиотеку на самом деле шёл Толик с книгой."
    hide un
    show image tl_normal at left
    show un normal pioneer at right
    with byso
    play music music_list["heather"]
    play sound door_cl
    "Войдя в библиотеку, Толик осмотрелся."
    kt "Эу, сегодня Лена вместо Жени."
    hide image tl_normal
    show image tl_angry at left
    with byso
    "Толик положил книгу и просто молча стоял.{w=1} Лена зачеркнула долг и передала книгу Константину."
    un "Поставь в стихи."
    "Константин нашёл соответствующий стеллаж и поставил туда сборник сочинений Есенина."
    kt "На этом всё, шагай отсюдова."
    hide un
    show un smile pioneer
    hide image tl_angry
    with byso
    play sound door_cl
    stop music fadeout 3
    "Толик молча ушёл."
    un "Вот теперь на этом всё, но могут зайти просто так сдать прочитанное."
    kt "Быстро мы, я думал сегодня должно быть больше работы."
    show un smile3 pioneer with byso
    play music music_list["i_want_to_play"] fadein 3
    un "Хочешь разок в карты сыграть на желание?"
    kt "А есть?"
    show un grin pioneer with byso
    "Лена с хитрой улыбкой достала из ящика стола книгу и открыв её достала из подшитого кармашка набор карт."
    un "Да, так и думала, Женя их не забрала."
    show un smile pioneer with byso
    play sound card_mix
    "Глянув на часы, Лена начала тасовать колоду."
    show un smile2 pioneer with byso
    un "В дурака?"
    show un smile pioneer with byso
    kt "Давай, почему нет."
    kt "Давно не играл."
    play sound card_mix
    "Лена сделала тасовку рифл-шафл и начала раздавать по две карты."
    kt "А ты смотрю времени не тратила..."
    show un grin pioneer with byso
    play sound card_take
    "Лена улыбнулась и выложила козырь - шестёрка пик."
    show un sad pioneer with byso
    un "М-м...{w} 6 пик может символизировать потерю, эмоциональное беспокойство, не очень удачную дорогу. {w=1}Шестёрка является предупреждением о том, что нужно быть готовым к тем или иным трудностям или проблемам."
    play sound card_take
    "Константин взял свои карты и тяжело вздохнул."
    kt "Ну давай не надо, не люблю гадания."
    show un grin pioneer with byso
    un "Ладно-ладно."
    show un normal pioneer with fade
    "Спустя некоторое время у Лены и Константина осталось по 6 карт.{w=1} У Константина на руках был козырной туз, валет и шестёрка, а также пики-черви короли и валет крести."
    th "У Лены должен быть король и дама, остальное шваль..."
    play sound card_take
    "Константин положил на стол валета крести."
    show un serious pioneer with byso
    un "Хм-м..."
    play sound card_take
    "Лена выложила короля крести, на что Константин докинул двух своих королей."
    kt "Хе, похоже кое-кто проиграл."
    play sound card_take
    "Она отбила их козырной дамой и королём, на что Константин докинул козырного валета."
    kt "Знаешь игру <<Храп>>?"
    show un angry2 pioneer with byso
    "Лена забрала карты и уныло посмотрела на Константина."
    un "Помню, а что?"
    kt "Так у меня вертолёт!"
    play sound card_take
    play sound2 sfx_dinner_horn_processed
    "Константин выложил козырного туза и шестёрку, в дополнение действий Константина заиграл горн."
    "Лена забрала карты в колоду."
    show un smile3 pioneer with byso
    un "Ну всё-всё, проиграла."
    kt "Ладно, пошли на обед."
    show un smile pioneer with byso
    stop music fadeout 3
    play sound sfx_open_table
    "Убрав карты на место, Лена утвердительно кивнула."
    scene bg ext_library_day
    show un normal pioneer
    with byso
    play ambience ambience_camp_center_day
    play sound door_cl
    play music music_list["two_glasses_of_melancholy"] fadein 2
    "Выйдя из библиотеки, они направились к столовой.{w=1} Лена потёрла глаза и заразительно зевнула."
    kt "Спать охота?"
    un "Да, немного.{w=1} Я спала очень плохо."
    kt "Почему?"
    show un sad pioneer with byso
    un "Кошмар приснился, видимо вещий, раз Женя уехала."
    un "Я сижу в каком-то ресторане, пью виски, попутно читая одну книжку, не помню какую."
    un "Как вдруг в этот ресторан врывается Генда и начинает расстреливать всех окружающих из винтовки, после чего я просыпаюсь..."
    "Константин почесал затылок."
    kt "Да-а, странный сон."
    th "У меня это была реальность и в менее располагающей обстановке."
    scene bg ext_dining_hall_near_day
    show un normal pioneer at left
    show mt normal pioneer panama at right
    with fade
    "У столовой их встретила вожатая, которая ходила вокруг да около."
    show mt smile pioneer panama at right with byso
    mt "Привет Костя, привет Лена.{w=1} Справляетесь в библиотеке?"
    kt "Да, всё хорошо.{w=1} Работаем потихоньку."
    show un smile pioneer at left with byso
    "В подтверждение слов Константина Лена кивнула, а Вожатая улыбнулась."
    show mt grin pioneer panama at right with byso
    mt "Хорошо. Работайте. Завтра кстати завезут новые книги."
    kt "Поняли."
    play ambience ambience_dining_hall_full
    scene bg int_dining_hall_people_day
    show un smile pioneer
    with byso
    "Войдя в столовую Лена и Константин встали на раздачу.{w=1} Столовая была на удивление забитой."
    "На обед подавали рассольник и ту же гречку, только на воде и с мелкими кусочками мяса."
    kt "Приятного."
    show un grin pioneer with byso
    un "Тебе тоже."
    "Обменявшись любезностями, участники литературного преступили к трапезе."
    show un smile pioneer with byso
    un "Сейчас сможем почитать <<Цену грехов>> я думаю, никто не должен после обеда подходить."
    kt "Откуда такие предположения?"
    show un normal pioneer with byso
    "Лена водила ложкой по тарелке рассольника."
    un "Статистика. Все обычно приходят до обеда за исключением должников, но как понимаешь должников уже не осталось."
    kt "А чего ты говорила что только после ужина?"
    show un smile3 pioneer with byso
    un "Да я думала что за должниками придётся походить, но они сами дошли, так что всё хорошо."
    "Константин пожал плечами и продолжил есть."
    show un normal pioneer
    show el normal pioneer at left
    with byso
    "Под конец трапезы к их столику подошёл унылый Электроник с двумя толстыми книжками."
    el "Вот долги."
    show un smile pioneer with byso
    "Лена пролистала книги на предмет повреждений и глянув на Константина кивнула."
    kt "Запишем, теперь свободен."
    hide el with byso
    "Электроник ушёл, а Лена с Константином направились на выход."
    scene bg ext_dining_hall_near_day
    show un grin pioneer
    with byso
    play ambience ambience_camp_center_day fadeout 2
    stop music fadeout 2
    un "Слушай, я пока отнесу и запишу книги, а ты возьми чайник с горячей водой, пожалуйста. {w}За прочтением чаю выпьём."
    kt "Хорошо, возьму."
    hide un with byso
    play music god fadein 2
    play sound sfx_knock_door7_polite
    "Константин обошёл столовую и постучал в дверь."
    show image pov_sad with byso
    play sound sfx_open_door_clubs
    "Открыла повариха и удивлённо глянула на Константина."
    pov "Ты за книгой?"
    kt "Что?{w=1} Нет, я хотел чайник попросить."
    pov "Чего-то ты рано, но ладно, у меня есть, заодно отдам книгу."
    play sound door_cl
    hide image pov_sad with byso
    "Дверь закрылась, а Константин засмотрелся в небо."
    th "Да-а, видимо тут весь лагерь пользуется услугами библиотеки, в том числе и персонал."
    th "И что же хотела почитать повариха, наверняка какой-нибудь роман о несправедливости и неразделённой любви."
    play sound sfx_open_door_clubs_2
    show image pov_normal with byso
    "Дверь снова открылась и повариха протянула Константину чайник с водой и толстенную книгу на страниц 600."
    pov "Чайник не забудьте вернуть."
    kt "Хорошо, спасибо."
    hide image pov_normal
    scene bg ext_dining_hall_away_day
    with byso
    "Отойдя от столовой Константин глянул на полученную книгу."
    th "Данте, <<Божественная комедия>>...{w=1} Интересный у неё вкус, не ожидал."
    scene bg ext_square_day with byso
    "Константин направился к библиотеке."
    th "Много в последнее время я думаю о книгах, никогда так не было."
    th "Я не читатель по природе, но тем не менее я состою в литературном клубе."
    show image na_no with byso
    "Он заметил девочку, которую видел в первый день."
    th "И кто она вообще? Знакомая внешность, но я не пойму кто она."
    play sound dissapearance
    hide image na_no with flash 
    "Девочка снова пропала."
    stop music fadeout 2
    th "Ещё и пропадает куда-то постоянно, как это понимать?"
    scene bg int_library_day
    show un smile pioneer
    with fade
    play sound door_cl
    play ambience ambience_library_day
    play music Gallow fadein 2
    "Дойдя до библиотеки, он без стука вошёл.{w=1} За столом сидела Лена и грызла овсяное печенье."
    kt "Вернулся.{w=1} Вот ещё повариха вернула книгу."
    "Константин поставил чайник на стол, а книгу отдал Лене."
    show un surprise pioneer with byso
    un "Данте...{w=1} Да, видимо Женя выдавала книги даже персоналу."
    kt "А что такого?"
    show un normal pioneer with byso
    "Лена встала и поставила книгу на стеллаж."
    un "Может я и ошибаюсь, но книги библиотекарь выдаёт только пионерам согласно возрастному цензу."
    show un smile3 pioneer with byso
    un "Если такое правило и было, то Жене было на него абсолютно плевать."
    kt "Да я думаю без разницы. Что просили, то и дали."
    show un sad pioneer with byso
    "Лена отвела взгляд."
    un "Не то что бы я спорю, но уж простите, партия всё портит."
    un "В политике я не имею никаких предпочтений, но эти лозунги <<равенства>> меня немного ставят в ступор."
    "Лена засыпала несколько ложек заварки в чайник и достала пару чашек."
    un "Что-то вроде того что было в книге <<1984>> Джорджа Оруэлла, <<война — это мир, свобода — это рабство, незнание — сила, власть — не средство>>."
    kt "Этим и славится тоталитаризм.{w=1} Не знаю почему, но мне этот режим может симпатизировать по некоторым причинам."
    show un surprise pioneer with byso
    un "М-м...{w=1} И по каким же?"
    kt "В условиях сильно-тоталитарного государства нет всей этой либеральной шелухи.{w=1} Никто не выйдет на пикеты или протесты по мелочам, поскольку таковых сразу поставят к стене."
    "Константин глянул в окно."
    kt "А знала бы ты, каково жить в стране в которой ни то и не другое.{w=1} Люди, хоть и имея нужный фундамент для жизни постоянно чем-либо недовольны."
    kt "Власть им не так, тунеядство не поощряет, а надо."
    kt "В таких условиях человеческая наглость начинает просто плодиться в неведомых масштабах."
    kt "Не буду говорить про то, что люди ненавидят друг друга, это вполне естественный процесс, сама понимаешь."
    kt "Но факт того, что в вполне адекватных, в сравнительной степени, условиях люди начинают возмущаться словно они коровы на скотобойне...{w=1} для меня процесс непонятный."
    show un normal pioneer with byso
    "Лена разлила заваренный чай по чашкам."
    un "Люди на подсознательном уровне всегда хотят идти по пути наименьшего сопротивления, тут уж ничего не поделать."
    un "Ну что, <<Цена грехов>>?"
    hide un with byso
    "Константин кивнул, а Лена отошла."
    un "Ничего себе..."
    show un surprise pioneer with byso
    "Константин встал со стула и посмотрел на Лену.{w=1} Том увеличился вдвое."
    kt "Ух ты-ж ё..."
    kt "Видимо нам будет чего сегодня почитать..."
    show un normal pioneer with byso
    stop music fadeout 2
    "Они вернулись за стол и сели по местам."
    "Константин открыл книгу в середине и начал читать."
    play music lim
    kt "Харитонов Алексей.{w=1} 2015 год.{w=1} Студент третьего курса международных отношений.{w=1} Грех его был в чрезмерном самобичевании."
    stop ambience
    scene bg ext_bus_night
    show shum_white
    with flash
    "Учился на отлично и никогда не прогуливал пары, отдавая приоритет знаниям, а не личной жизни или чему-либо другому."
    "Предстоял сессионный экзамен, который требовал буквально несколько дней непрерывной подготовки в честь чего Алексей буквально не мог пропустить ни минуты."
    "Переработка и отсутствие здорового сна дали о себе знать и на очередной лекции у него случился сердечный приступ."
    "Очнулся он в пустоте.{w=1} Пред ним был лишь образ девочки."
    deva "Ты пойдёшь со мной?"
    "Лёша осмотрелся и начал паниковать."
    lesha "Где я? Кто ты? Что происходит?!"
    "Образ лишь промолчал но затем повторил свой вопрос."
    deva "Ты пойдёшь со мной?"
    lesha "Может это сон? Ну ладно, пойду."
    hide shum_white
    scene bg ext_houses_night
    show shum_white
    with flash
    "Он попал в пионерский лагерь, где своими попытками выяснения ответов стал кем-то вроде местного сумасшедшего."
    hide shum_white
    scene bg int_mine_crossroad
    show shum_white
    with flash
    "Спустя 5 дней он направился в местные катакомбы на поиски ответов."
    "Потерявшись в пещере он сел и начал думать о том как выбраться."
    pi "Значит, ты тоже решил убежать?"
    "Алексей вскочил с места и начал в панике оглядываться."
    pi "Не бойся, я тут дать тебе ответы, просто возьми себя в руки."
    "Лёша собрал силы в кулак и успокоился, понимая что ответы совсем рядом."
    lesha "Не назвал бы это бегством."
    "Через некоторое время ответил он, растягивая каждое слово."
    pi "Да? А как же тогда?"
    lesha "Поиск ответов."
    pi "Блестяще!"
    "Пионер расхохотался."
    lesha "Слушай, может, ты расскажешь всё-таки, что здесь происходит, кто ты и чего от меня хочешь?"
    pi "Что же, это вполне в нашем духе... Убежать, спрятаться..."
    "Пионер проигнорировал вопрос Лёши, в его голосе звучало раздражение."
    pi "Тебе не так важно знать кто я, тебе важно знать кто она."
    lesha "Я не знаю, что у тебя тут за цирк с конями, но у меня, честно говоря, нет никакого желания участвовать в этом представлении!"
    pi "О, почему же...{w} Ты главная звезда!"
    "Сквозь темноту было видно улыбку пионера, Лёше стало не по себе."
    lesha "Если так, то объясни мне мою роль!"
    pi "Знаешь, я вначале тоже был таким, как ты... Первый раз всё прошло спокойно."
    pi "Потом я убегал, пытался выяснить, что происходит, сходил с ума..."
    "Он заржал как умалишённый."
    pi "Но всё бесполезно!"
    "Немного успокоившись, продолжил пионер."
    pi "Бесполезно...{w} Она..."
    pi "Сначала я слышал её голос – где-то далеко, а иногда у себя в голове."
    pi "Она не имеет никаких человеческих качеств! Она монстр! Она словно питается нашей кровью!"
    pi "И наконец вошла в мой мир! В поисках меня! Она убила их всех! Порубила на части своим топором..."
    pi "Я сбежал из того мира через портал... Но она продолжила охоту за мной! Она где-то рядом."
    pi "Она хочет меня убить!!!"
    "Он сбился на крик."
    pi "И раз за разом всё повторялось... Она убивала людей, одного за другим."
    pi "Потом я и сам научился попадать в их миры, взаимодействовать с другими. Однако она умеет так же!"
    pi "Нам нужно бежать, остальное потом! Сопротивление нам поможет!"
    stop music fadeout 4
    "Он замолчал. Позади раздался шорох и Алексей обернулся."
    lesha "Что там..."
    "Раздалось влажное хрипение. Лёша обернулся обратно к пионеру..."
    play music CowCowCow
    rep "Приве-етик! С ним ты уже познакомился, говорить вам больше не о чем!"
    "Неизвестная рыжая девочка в белом платье срезала голову пионера с плеч. Лёша стоял с замороженной гримасой ужаса."
    rep "Ой, только не начинай бежать, я хочу сделать это быстро, думаю ты тоже."
    "Оторвав голову с позвонков, девочка выкинула её в сторону. Тело пионера упало на землю."
    "Осознав происходящее, Лёша закричал и начал бежать прочь из катакомб."
    hide shum_white
    scene bg int_mine
    show shum_white
    with byso
    "В след ему долетал лишь хохот девочки."
    rep "Ха-ха-ха, не рекомендую тебе выходить на поверхность!"
    hide shum_white
    scene bg int_old_building2
    show shum_white
    with byso
    "Закрыв люк через который он заходил в катакомбы, он побежал в сторону домика вожатой."
    hide shum_white
    scene bg ext_square_night_blood
    show shum_white
    with byso
    "На площади лежала целая куча трупов обитателей лагеря, лужи крови уже начинали свёртываться, а воздухе преобладал лёгкий запах железа."
    hide shum_white
    scene bg int_house_of_mt_night2
    show shum_white
    with byso
    "Добежав до домика вожатой, он стал будить лежащую на кровати вожатую."
    lesha "Вставайте!{w=1} Вставайте!!!{w=1} У нас убийца в лагере."
    "Алексей тряс вожатую за плечо, как вдруг со шлепком её голова не упала на пол."
    "Алексей начал кричать пуще прежнего, и побежал на выход."
    hide shum_white
    scene ext_house_of_mt_night_without_light
    show shum_white
    with byso
    rep "Сюрприз!" with vpunch
    "Лёша получил по лицу трубой, после чего упал на землю."
    "Он попытался встать на ноги, но девочка раздавила его коленную чашечку."
    rep "Год попадания?"
    "Девочка достала из ножн ножик и села на колени лежачего Алексея."
    lesha "Что ты вообще несёшь?!"
    "Он попытался ударить девочку, но она поймала его руку и вонзила в неё нож, перерезав сухожилия."
    lesha "А-а-а!!!"
    rep "Все вы кричите, убегаете...{w=1} Но результат то один, вы все трупы."
    "Вынув нож из руки Алексея, она вонзила его в другую руку, сделав те же действия."
    "Алексей кричал, но судя по лицу девочки ей это доставляло удовольствие."
    rep "Так чего, не хочешь мне год попадания озвучить?"
    lesha "2015..."
    "Сквозь зубы проговорил Алексей. Девочка глянула в сторону."
    rep "М-м, замечательно..."
    lesha "Ты м-м-монстр!"
    "Она резко оживилась и воткнула нож ему в грудь, пробив лёгкое."
    rep "Как думаешь, что лучше, жить монстром или умереть человеком?{w=1} Я выбираю жить монстром, а ты - умереть животным."
    "Алексей ничего не отвечал и лишь стонал от боли. Девочка вздохнула и перерезала ему глотку."
    rep "Никакого от вас толку..."
    "Отерев ножик от крови об его рубаху, она встала на ноги и пошла к площади."
    stop music fadeout 3
    "Повествование 43-ей души завершено."
    hide shum_white
    scene bg int_library_day
    show un shocked pioneer
    with flash
    play ambience ambience_library_day
    play music music_list["drown"]
    "Лена была в ужасе, Константин отложил книгу и сделал глоток чая."
    kt "Девочка эта...{w=1} Похоже в край сошла с ума."
    show un scared pioneer with byso
    un "Да какое там!{w=1} Она просто озверела!"
    show un normal pioneer with byso
    un "Перерезать весь лагерь... Дай-ка сюда."
    play sound sfx_paper_bag
    "Лена взяла книгу и стала перелистывать её страницы."
    show un sad pioneer with fade
    "Спустя полчаса она вернула книгу на стол и с мрачным видом допила чай."
    kt "И чего?"
    un "145 убийств...{w=1} И то главных героев!"
    un "И этот лагерь в описании..."
    "Лена заглянула в окно."
    un "Точно наш."
    kt "С чего бы то?"
    show un normal pioneer with byso
    "Лена перевела взгляд обратно на Константина."
    un "В <<Совёнке>> есть комплекс катакомб, который ранее был использован в качестве бомбоубежища."
    un "Герой книги похоже пошёл на полученную наводку в результате чего всё так и закончилось."
    stop music fadeout 2
    "На пару минут настала тишина."
    hide un
    show un normal pioneer at right
    show dv smile pioneer2 at left
    with byso
    play music music_list["torture"] fadein 4
    play sound door_cl
    "Тишину нарушила Алиса, которая вломилась в библиотеку."
    dv "Всем здрасте, мне книжечку сдать."
    "Она положила на стол книгу <<Тимур и его команда>>.{w=1} Лена молча поставила подпись о сдаче книги и передала её Константину."
    show dv laugh pioneer2 at left with byso
    dv "О, ясно чего вы вдвоём, одна умеет писать, другой носить."
    show un angry2 pioneer at right with byso
    un "Слушай, сгинь с глаз долой, а?"
    show dv shocked pioneer2 at left with byso
    "Алиса и Константин удивились такому обороту речи от Лены."
    show dv smile pioneer2 at left with byso
    dv "Ничего себе, у тебя тут чего, голосок прорезался?"
    "Лена молча указала Алисе на выход."
    show dv laugh pioneer2 at left with byso
    dv "Хе-хе, ладно-ладно, иду."
    stop music fadeout 2
    play sound door_cl
    hide dv
    hide un
    show un sad pioneer close
    with byso
    pause 3
    play music music_list["door_to_nightmare"] fadein 4
    "Алиса ушла. Константин поставил стул и подсел к Лене."
    kt "Что с тобой?"
    un "Мне страшно.{w=1} Мне кажется что девочка придёт и к нам."
    kt "Ничего, всё будет нормально, нам такое не грозит."
    un "Все они так думали...{w=1} Все 145 человек..."
    kt "Не стоит бояться. Это не случилось, всё хорошо, скоро мы пойдём на ужин, поедим и посидим вечером."
    kt "У меня есть портвейн если ты хочешь."
    show un cry_smile pioneer close with byso
    un "Знаешь, может и Женю за это выгнали, но если нас выгонят мне уже не страшно."
    un "Давай."
    stop music fadeout 3
    kt "Тогда мне нужно сходить в домик, он не далеко."
    show un grin pioneer close with byso
    "Лена успокоилась и легко улыбнулась."
    un "Хорошо, неси. Я тут его потом спрячу."
    scene bg ext_library_day with byso
    play sound door_cl
    play ambience ambience_camp_entrance_day
    play music Aleph fadein 3
    "Константин встал со стула, улыбнулся и вышел из библиотеки."
    "Направившись в сторону домика, Константин задумался."
    th "Как бы мне не пришлось говорить Лене, но она-то права.{w=1} По рассказам пионера она вполне может попасть к на и тогда нам всем будет не очень приятно..."
    th "Судя по всему девочка убивает по конкретной потребности кого-то тут найти, но мне начинает казаться что её цель немного поменялась."
    th "Может быть она как и я попала сюда и решила сбежать, попутно захватив кого-то с собой."
    th "Какие бы то цели она не преследовала, она очень сильна ненавидит местный порядок вещей."
    scene bg int_house_of_mt_day with fade
    play sound sfx_open_door_clubs
    stop ambience
    "Константин дошёл до домика и открыл дверь."
    "Вожатой не было на месте, Константин взял рюкзак и понёс его в библиотеку."
    th "А чё мелочиться, возьму всё сразу..."
    scene bg ext_house_of_mt_day with byso
    play sound door_cl
    play ambience ambience_camp_center_day
    "Выйдя из домика, Константин направился обратно."
    scene bg ext_square_day with byso
    th "Порядок вещей...{w=1} Вспомнилась одна песня."
    "Константин начал прогонять песню в своих мыслях."
    window hide
    $ set_mode_nvl()
    window show
    "Естественный"
    "Порядок вещей"
    "Жизнь и смерть"
    "Обычных людей"
    "Так много не успел сказать"
    "Как же сложно осознать"
    ""
    "Не уходи останься ещё на миг"
    "Я буду помнить тебя всегда"
    "И может напишу пару книг"
    "Под чёрной пеленой открыв глаза"
    window hide
    $ set_mode_adv()
    window show
    stop music fadeout 2
    play sound door_cl
    play ambience ambience_library_day
    scene bg int_library_day with fade
    "Дойдя до библиотеки он зашёл внутрь."
    show un smile pioneer with byso
    play music music_list["a_promise_from_distant_days_v2"] 
    "Лена стояла у стеллажа и раскладывала книги по полкам."
    un "Ты вернулся.{w=1} С рюкзаком даже?"
    "Константин кивнул и поставил рюкзак на пол."
    kt "Тут есть сигареты и портвейн, всё самое необходимое так сказать."
    "Константин достал бутылку портвейна и передал Лене."
    show un smile3 pioneer with byso
    un "Хм-м, неужто у трёх топоров новое оформление?"
    play sound sfx_dinner_horn_processed
    stop music fadeout 3
    "На улице заиграл горн."
    show un surprise pioneer with byso
    un "Как это, уже?"
    "Лена глянула на время."
    un "Мне казалось мы обедали не так давно..."
    kt "Хм-м...{w=1} Мне кажется это дело в книжке.{w} Когда ты сильно увлекаешься чтением, ты не понимаешь сколько времени проходит."
    show un sad pioneer with byso
    play sound sfx_open_table
    "Лена убрала бутылку в ящик стола."
    un "Похоже на то."
    scene bg ext_square_sunset
    show un sad pioneer
    with fade
    play ambience ambience_camp_entrance_evening fadein 1
    play music music_list["silhouette_in_sunset"] fadein 4
    un "Не знаю как ты, но я не сильно голодна."
    kt "Я тоже.{w=1} За <<ценой грехов>> похоже время летит куда быстрее..."
    scene bg ext_dining_hall_near_sunset
    show mt smile pioneer panama at right
    show un normal pioneer at left
    with byso
    "У столовой их снова ждала вожатая."
    th "Вот заняться ей нечем?{w} Стоит и караулит."
    mt "Пионеры, не забудьте что у нас сегодня свечка."
    un "Хорошо..."
    kt "Что за свечка?"
    show un smile pioneer at left with byso
    un "Небольшое событие к концу смены, где каждый может выразить свои мысли про смену и отряд."
    show mt grin pioneer panama at right with byso
    "Отчеканила Лена.{w=1} Вожатая кивнула, а Константина смутила точность и принуждённость ответа."
    show mt smile pioneer panama at right with byso
    mt "Ладно, идите на ужин, после ужина собираемся."
    scene bg int_dining_hall_people_sunset_cust
    show un normal pioneer
    with byso
    play ambience ambience_dining_hall_full
    "Лена с Константином ушли в столовую и встали на раздачу."
    show un smile pioneer with byso
    kt "Добрый вечер, можно нам понемногу еды, мы не особо голодны."
    pov "Хорошо, без проблем."
    "Повариха положила по тарелкам половинную порцию рыбы с жареной капустой."
    show un normal pioneer with byso
    "Лена и Константин сели за столик, снова обменялись любезностями и начали неохотно есть."
    stop music fadeout 3
    un "Я вот что думаю...{w=1} Мне кажется с этой сменой что-то не так."
    "Константин отвлёкся от рыбы и глянул на Лену."
    kt "М-м?"
    show un sad pioneer with byso
    play music music_list["mystery_girl_v2"] fadein 5
    "Лена неохотно отломила кусочек от рыбы."
    un "Ну как тебе сказать...{w=1} Я помню четыре прошлые смены, но я не помню что было между ними."
    un "Пустота...{w=1} Словно я тут не по своей воле."
    "Константина сильно озадачили мысли Лены."
    kt "Что ты последнее помнишь?"
    show un normal pioneer with byso
    "Лена глубоко ушла в свои мысли.{w=1} Константин доел кусочек рыбы."
    show un sad pioneer with byso
    un "Ничего...{w=1} Вот вообще...{w=1} Может у меня амнезия?"
    "Константин почесал затылок и отложил вилку."
    kt "Давай потом это обсудим.{w} Лучше не оповещать окружающих о такого плана проблемах."
    show un smile pioneer with byso
    "Лена кивнула и положила вилку на тарелку."
    un "Мы не вернули чайник, а надо."
    show un smile3 pioneer with byso
    un "Ничего, подожди меня у столовой, я быстро."
    kt "Хорошо."
    stop music fadeout 3
    hide un with byso
    "Лена выбежала из столовой, Константин сдал две тарелки и пошёл на выход."
    play ambience ambience_camp_entrance_evening fadein 1
    scene bg ext_dining_hall_near_sunset
    show mt surprise pioneer panama
    with byso
    "На крыльце стояла вожатая с удивлённым видом."
    mt "А куда Лена побежала?"
    kt "Сказала по делам, она скоро вернётся."
    mt "Ну...{w=1} ладно."
    hide mt with byso
    play music exodus fadein 5
    "Константин сел на ступеньки."
    th "<<Пустота>>...{w=1} Лена похоже тоже не из этого мира...{w=1} Но откуда тогда она?"
    th "Странно-странно...{w=1} Вообще ничего не ясно...{w} А ещё куда сбежала Женя...{w=1} С ней был водитель."
    th "Транзит по мирам?{w=1} Возможно ли такое?"
    th "Да-а, к пионеру у меня будет сегодня о-очень много вопросов."
    th "И попадёт ли Лена в кошмар?{w=1} По логике, она ведь тоже должна быть <<игроком>>...{w} Я понял!{w=1} Когда я приехал сюда, я тоже мало чего мог вспомнить."
    th "Видимо симуляция циклична. Лена сказала что у неё было четыре смены, а между ними пустота."
    th "Пазл в моей голове начинает складываться, но тем не менее без пионера я не могу дать тому корректное объяснение."
    show mt smile pioneer panama with byso
    "От мыслей Константина отвлекла вожатая."
    mt "Костя, подожди Лену и иди потом за нами на...{w=1} А, вот и она."
    hide mt
    show mt smile pioneer panama at right
    show un normal pioneer at left
    with byso
    "Прибежала Лена, уже без чайника."
    mt "Хорошо, все в сборе, можем выдвигаться.{w} Мой отряд!{w=1} За мной."
    hide mt
    hide un
    show un smile pioneer
    with byso
    "Весь отряд пошёл за Сахаровой."
    un "О чём думал?"
    kt "Да так, по мелочи...{w=1} Потом более разнопланово обсудим."
    show un sad pioneer with byso
    un "Как скажешь..."
    stop music fadeout 3
    play ambience ambience_camp_entrance_night
    scene bg ext_stage_normal_night
    show un smile pioneer
    with fade
    "Как только их отряд добрался до сцены, уже полноценно стемнело."
    show mt normal pioneer far at right with byso
    play music warm_evening
    mt "Пионеры, аккуратно поднимайтесь по лестнице и занимайте удобные места на полу."
    "Константин поднялся и подал руку Лене."
    show un grin pioneer with byso
    un "Спасибо..."
    show un smile pioneer with byso
    mt "Ребята, кучнее и в круг."
    hide un
    hide mt
    show mt smile pioneer
    show sl smile pioneer at right
    with byso
    "Константин сел спиной к кулисам сцены, справа от него села Лена."
    "Вожатая достала спички, зажгла толстую свечу и вставила её в фонарь."
    mt "Друзья, исполняя традицию нашего лагеря, сегодня у нас свечка.{w=1} Каждый может оставить своё слово для остальных."
    hide mt
    hide sl
    show mt grin pioneer at left
    show sl smile2 pioneer
    show sh normal pioneer at right
    with byso
    "Вожатая передала свечку Славе."
    sl "Говорить может только тот у кого в руках свечка.{w=1} Остальные могут только тихо похлопать под конец выступления."
    sl "Итак, я начну.{w} Я очень рада что нахожусь тут с вами уже какую смену.{w=1} Каждый раз я снова и снова влюбляюсь в это место."
    sl "Я рада что нахожусь в нашем прекрасном и дружном отряде..."
    th "Бла-бла-бла...{w=1} Балобольства больше чем сути."
    "Как только Славя закончила свою нудную речь, похлопала только вожатая."
    hide sl
    hide mt
    hide sh
    show sl smile pioneer at left
    show sh normal_smile pioneer
    show image rm_th at right
    with byso
    "Славя передала свечу Шурику."
    sh "Спасибо. Хочу сказать спасибо своему клубу за удачную работу.{w=1} Скоро мы представим свою новую разработку и я обещаю, вы все будете приятно удивлены."
    show sh upset pioneer with byso
    sh "Приходите в клуб кибернетики мы ждём всех. Почти. Всех."
    hide sl
    hide sh
    hide image rm_th
    show sh upset pioneer at left
    show image rm_th
    show el sad pioneer at right
    with byso
    "Сказал он и передал фонарь Роме."
    rm "Мой коллега по цеху сказал всё верно. Приходите."
    hide el
    hide sh
    hide image rm_th
    show image rm_no at left
    show el upset pioneer
    show mi upset pioneer at right
    with byso
    "Рома передал фонарь Электронику."
    el "Мы ждём всех..."
    hide el
    hide image rm_no
    hide mi
    show el sad pioneer at left
    show mi dontlike pioneer
    show dv smile pioneer at right
    with byso
    "Уныло сказал Электроник и передал свечу Мику."
    mi "Спасибо всем за смену и за доп.работу в музклубе!"
    hide el
    hide dv
    hide mi
    show mi angry pioneer at left
    show dv laugh pioneer
    show us smile pioneer at right
    with byso
    "Мику передала свечу Алисе."
    dv "Да-да, на нашей смене всё трещит по швам, кибернетиков избили, музклуб распадается, библиотекарь уехал, класс."
    hide mi
    hide dv
    hide us
    show dv grin pioneer at left
    show us grin pioneer
    show un normal pioneer at right
    with byso
    "Все осуждающе смотрели на Алису, которая задыхаясь от смеха передала свечу Ульянке."
    us "О, наконец я!{w=1} Я вот рада быть в этом отряде."
    us "Тут мои друзья и я буду рада приехать на ещё одну смену."
    us "Завтра у моей команды матч, чтоб были все!"
    hide dv
    hide us
    hide un
    show un serious pioneer
    with byso
    "С ухмылкой сказала Ульянка и передала свечку Лене."
    un "Могу сказать вопреки словам Алисы, библиотека не <<трещит>>.{w=1} Работа продолжается, да и пионерку без клуба толком никто на эту тему не спрашивал."
    show un angry2 pioneer with byso
    un "Хотя должна согласиться с Женей, это моя последняя смена."
    un "Как и нашего отряда, он, судя по всему, на следующую смену даже не наберётся."
    show un smile pioneer with byso
    "Никто не ожидал таких слов от самой тихой девочки лагеря.{w=1}Лена с ухмылкой передала свечу Константину."
    kt "Хм...{w=1} Что-ж сказать."
    window hide
    menu:
        "Думаю, все уже всё сказали, мне сказать нечего.":
            $ unscore += 1;
            kt "Всем спасибо за внимание."
        "Эта смена стала лучшей для меня.":
            kt "На этой смене было много веселья, я рад что приехал сюда и получил хороший опыт благодаря некоторым людям."
            kt "Возможно я приеду сюда ещё раз.{w=1} Спасибо за внимание."
        "Спасибо за интересную смену.":
            $ unscore += 1;
            kt "И за внимание тоже."
    hide un
    show mt grin pioneer
    with byso
    "Константин вернул свечу вожатой."
    mt "Что-ж, на этом наша прекрасная свечка заканчивается."
    "Вожатая задула свечку в фонаре."
    show mt smile pioneer with byso
    stop music fadeout 3
    mt "А теперь все по домикам. Всем спокойной ночи."
    "Отряд стал расходиться."
    "Константин подошёл к вожатой."
    kt "Ольга Дмитриевна! Мы не доделали дела в библиотеке, могу я вернуться в домик позже?"
    show mt normal pioneer with byso
    mt "М-м, и какие же у вас там дела?"
    show un serious pioneer at right with byso
    un "Мы не успели заполнить отчётность по сданным книгам. "
    "В диалог вклинилась Лена, при том вполне уместно."
    show mt surprise pioneer with byso
    mt "А, в таком случае без проблем, раз Жени нет, то работайте."
    show mt normal pioneer with byso
    mt "В 11 быть в домике."
    hide mt
    hide un
    show un smile pioneer
    with byso
    "Строго сказала вожатая Константину и ушла."
    kt "А чётко ты подобрала ситуацию чтоб её надурить. Она боится умных словосочетаний."
    scene bg ext_houses_night
    show un smile3 pioneer
    with byso
    play music BlueJetta fadein 7
    "Константин и Лена направились в сторону библиотеки."
    un "Да, а откуда ты знаешь?"
    kt "Долгая история, сядем расскажу."
    show un grin pioneer with byso
    un "Заинтриговал."
    "С улыбкой протянула Лена и глянула в небо."
    show un smile pioneer with byso
    un "Ты был прав, выговориться иногда помогает.{w=1} Когда легко на душе, хочется подмигнуть звездам, и заглядеться на них..."
    kt "Да-а, ты там всех разнесла в несколько предложений."
    show un laugh pioneer with byso
    "Лена хихикнула."
    un "Нет, ну а что они?"
    play ambience ambience_int_cabin_night
    scene bg int_library_night 
    show un smile pioneer far
    with fade
    play sound door_cl 
    scene bg int_library_night2
    show un smile pioneer
    with byso
    "Дойдя до библиотеки Лена нашла пару свечей и зажгла их для лучшего освещения."
    kt "М-м, свечи, прям романтика."
    show un grin pioneer with byso
    "Лена мило улыбнулась."
    un "Другие источники света в библиотеке не работают. Обходимся свечами и лунным светом."
    show un smile pioneer with byso
    "Лена села за столик и поставила чашки на стол."
    play sound sfx_open_table
    "Достав бутылку портвейна она передала её Константину."
    show un smile3 pioneer with byso
    un "Откроешь?"
    kt "Конечно."
    show un smile pioneer with byso
    "Привычным движением руки Константин открыл бутылку и разлил её содержимое по чашкам из которых они пили чай ближе к обеду."
    kt "Ну что, за вечер?"
    show un smile2 pioneer with byso
    un "За вечер."
    "Они стукнулись чашками и понемногу отпили."
    show un serious pioneer with byso
    un "Да-а, три топора ничуть не изменились."
    kt "Пила раньше?"
    show un smile3 pioneer with byso
    "Лена улыбнулась и заглянула Константину в глаза."
    un "Конечно...{w=1} Это по крайней мере я помню..."
    kt "А с этого момента подробнее, нам надо в этом разобраться."
    show un surprise pioneer with byso
    "Лена удивилась такому рвению Константина вернуть ей память."
    un "Тебе это так важно?"
    window hide
    menu:
        "Как бы сказать... У моей подруги вдруг пропала память, я должен тебе помочь.":
            $ renpy.block_rollback()
            $ unscore += 1;
            show un grin pioneer with byso
            "Лена улыбнулась."
            un "Мило с твоей стороны."
        "Есть одна теория... Я хочу её проверить. Теория в достаточной важная, потому сконцентрируйся.":
            $ renpy.block_rollback()
            un "Какая теория?"
            kt "Узнаешь. Постарайся хоть что-нибудь вспомнить."
    show un normal pioneer with byso
    "Лена отпила портвейна и глянула в окно."
    un "Хм-м-м...{w} Я помню что я была в городе и ехала домой на такси после дня рождения какого-то из родственников...{w=1} Вот, отца."
    show un surprise pioneer with byso
    un "Мы праздновали в ресторане... Меня спрашивали про работу... Какую работу..."
    "Лена пришла в смятение."
    kt "Может быть <<Полимер>>?"
    show un smile3 pioneer with byso
    un "Да!{w=1} <<Полимер>>...{w} Наверное я там была на практике..."
    un "Всё так завуалированно, словно это сон..."
    show un normal pioneer with byso
    "Лена допила портвейн, Константин сделал так-же и обновил напитки."
    un "<<Полимер>>-<<Полимер>>...{w=1} Хм-м..."
    kt "Находился около спального района..."
    show un surprise pioneer with byso
    un "Точно!{w=1} Так, а ты откуда знаешь?"
    kt "Не отвлекайся."
    show un normal pioneer with byso
    un "Хорошо...{w=1} Так...{w=1} Работа...{w=1} Спальный район..."
    un "У меня был руководитель...{w=1} Хм-м...{w=1} Тут не помню."
    un "Ладно...{w} Дом...{w=1} Точно!{w} Я съехала от родителей..."
    show un surprise pioneer with byso
    un "Но тогда почему я тут?"
    kt "Не помнишь никакого Генду?"
    "Лена ошеломлённо глянула на Константина."
    un "Генда?{w} Нет, почему, партийный де...{w=1} Сто-оп..."
    show un shocked pioneer with byso
    stop music fadeout 3
    "Лена схватила бутылку портвейна и посмотрела на дату изготовления."
    un "Что?!{w=1} 14 августа 2022 года?!{w=1} Это же будущее!"
    "Константин перевёл взгляд в окно."
    kt "Нет, скорее то настоящее откуда приехал я.{w=1} Добавь ещё несколько месяцев только."
    kt "Скажу так, не сочти за бред, но слушай..."
    kt "ФИО - Брусков Константин Павлович."
    kt "1997 год рождения."
    kt "Должность - бухгалтер среднего звена."
    kt "Год попадания сюда 2022, как и производство портвейна."
    kt "И это не путешествие во времени.{w=1} Это Генда."
    show un scared pioneer with byso
    hide un with byso
    play sound sfx_bodyfall_1
    play music the_date_of_death fadein 2
    "Лена в шоке посмотрела на Константина, побледнела и упала на пол."
    kt "Лена!"
    "Константин тряс её за плечи, но ответа не следовало."
    "Найдя стакан с водой, Константин усадил Лену на стул и рукой попрыскал на неё несколько капель."
    kt "Что-ж такое, вставай-вставай!"
    "Взяв руку Лены, он начал прощупывать её пульс."
    show un sad pioneer with byso
    "Лена очнулась и взяла Константина за руку."
    un "Я вспомнила...{w=1} Свою прошлую жизнь...{w=1} И тебя."
    kt "Фух, ты меня напугала...{w=1} И чего?"
    un "Мы с тобой учились в одной школе а позже вместе работали в <<Полимере>>."
    un "Климова Елена Константиновна.{w} Я ещё шутила что ты как мой папа."
    un "Мы общались до середины 10го класса, потом я переехала."
    stop ambience
    play sound in_vosp
    scene bg street
    show shum_white
    with flash
    "Костя шёл со школы после очередного дня натаскивания на ЕГЭ."
    "К нему подошла его старая знакомая - Лена.{w=1} Девочка была стеснительной и кроме Константина имела только пару двоюродных братьев, которые часто с ней пересекались."
    ks "Привет, как ты?"
    un "П-привет, я в порядке, только с правом завал, никак не могу во вариантах разобраться..."
    ks "Хм-м, ну если хочешь то можем завтра после уроков посидеть, я подскажу чего знаю."
    un "С-спасибо, б-было бы не плохо..."
    un "А ты как? Я слышала про Настю..."
    "Костя тяжело вздохнул и глянул на старую остановку."
    ks "Недавно похороны были...{w=1} Ужасно честно говоря...{w=1} Уродам в моём классе это лишь ещё один повод для насмешек."
    ks "Всегда знал что этих тварей даже на расстояние выстрела подпускать не надо."
    un "Ничего, всё наладится...{w} Я понимаю что это пустые слова, но это всё что я могу сказать..."
    hide shum_white
    scene bg int_library_night2
    show un sad pioneer
    with flash
    un "Потом работали в <<Полимере>>...{w=1} Я поняла откуда ты знаешь Сахарову, она была твоей подчинённой."
    play sound in_vosp
    scene bg ofis
    show shum_white
    with flash
    "Константин вернулся от кофейного автомата в свою каморку и начал ковыряться в бумагах."
    kt "14 февраля...{w=1} Какой же убогий праздник, жуть..."
    "Прошептал Константин и открыл папку с графиками оплаты поставок."
    kt "Бла-бла-бла...{w=1} Сколько раз не повторяй Сахаровой не писать херь, а она всё за своё.{w} <<Требуется снизить оплату ТО корпоративных автомобилей>>.{w=1} Да-да, мне на шубку не хватает, а водитель пусть там убьётся!"
    "Гневно пробубнил Константин и поставил печать <<хуйня, переделывай>>, которую ему подарили в офисе."
    kt "Каждый раз одно и то же...{w=1} Лишь бы отстреляться..."
    "Константин открыл другую папку по страховым случаям.{w=1} В ней лежала красная бумажка в форме сердечка с подписью."
    kt "Я иду по следам чужой жизни, за ней наблюдая в стороне.{w=1} Без обид и сильной укоризны, смотрю в глаза своей судьбе."
    kt "Интересно...{w=1} Страховщики походу позитива словили, но если отчёт кривой, то им это не поможет."
    "Проговорил он и отложил бумажку в карман."
    hide shum_white
    scene bg int_library_night2
    show un sad pioneer
    with flash
    un "Когда я ехала домой со дня рождения отца, таксистом оказался Генда, который отвёз меня сюда...{w=1} Прошло несколько так называемых <<циклов>>."
    un "И теперь мы тут...{w=1} Я хотела подойти к тебе ещё в <<Полимере>>, но боялась что ты со мной будешь как с Сахаровой..."
    play sound in_vosp
    scene bg ofis
    show shum_white
    with flash
    kt "Сахарова!{w=1} Что это такое?!"
    "Константин скомкал и выкинул бумагу, которую напечатала Ольга."
    od "В чём проблема?"
    kt "За коим хером нам облагать сверхплатой <<Петролаб>>, вы в своём уме?"
    "Сахарова неловко почесала затылок."
    od "Ну ты же понимаешь, что они себе в карман кладут часть?"
    "Лицо Константина изображало высшую степень гнева и он перешёл на крик."
    kt "Во первых на <<Вы>>!!!{w=1} Во втор-рых, то что у них творится порно с конями это не наша забота!{w=1} И в тр-ретьих идите переписывайте!"
    od "Ладно-ладно, чего сразу кричать то?.."
    kt "Какой раз я вам повторяю?! {w=1}Одно и то же, раз за разом, раз за разом, а потом ничерта не меняется, всё та же дешёвая порнография!{w=1} Идите работать!{w} Сейчас-же!!!"
    "Ольга ушла, а Константин успокоился, поправил причёску и пошёл к себе в кабинет."
    hide shum_white
    scene bg int_library_night2
    show un sad pioneer
    with flash
    stop music fadeout 3
    "Константин сложил всю информацию в голове."
    window hide
    menu:
        "Обнять Лену.":
            $ renpy.block_rollback()
            $ unscore += 1;
            show un shy pioneer close with byso
            play music proshloe fadein 3
            "Константин отпустил руку Лены и обнял её. Она явно такого не ожидала."
            kt "Да...{w=1} Я это помню, прости за то что не обращал внимание на то, с кем я работал."
            un "Н-ничего...{w=1} Я-я понимаю...{w=1} Т-тебе б-было тяжело..."
            "Константин и Лена отпустили друг друга. Константин вернулся в исходное положение."
        "Сесть на свой стул.":
            $ renpy.block_rollback()
            play music proshloe fadein 3
            "Константин повалился на свой стул."
    "Разлив остатки портвейна по стаканам, Константин поднял кружку."
    kt "Ну что...{w=1} За встречу?"
    un "За встречу..."
    "Выпив понемногу, они переглянулись."
    kt "Дай угадаю, ты хочешь узнать как я тут оказался?"
    show un grin pioneer with byso
    "Лена с усмешкой кивнула."
    kt "Ты не поверишь, но я был признан самым бесчеловечным террористом в нашем городе..."
    show un shocked pioneer with byso
    "Константин кратко пересказал встречу с Гендой и всё что ему удалось пережить.{w=1} Лена была в шоке от услышанного."
    show un sad pioneer with byso
    un "М-да. Видимо хорошо что я раньше сюда попала..."
    "Допив портвейн, они глянули в окно."
    kt "Ну что по домикам."
    un "Да, уже пора..."
    show un normal pioneer with byso
    play sound sfx_open_table
    "Лена сонно зевнула и убрала чашки и портвейн."
    scene ext_library_night
    show un smile pioneer
    with byso
    play ambience ambience_camp_entrance_night
    play sound door_cl
    "Выйдя из библиотеки, Лена закрыла её на ключ.{w=1} Константин вдохнул ночной воздух и потянулся."
    kt "До сих пор интересно куда делась Женя..."
    show un surprise pioneer with byso
    un "Не могу быть уверена, но она вроде как говорила о каком-то сопротивлении...{w=1} И мне не кажется что речь была о физике."
    kt "Хах, понимаю.{w=1} Когда это она говорила?"
    show un normal pioneer with byso
    un "За пару дней до твоего приезда. {w=1}Мы пили вино которое она привозила, и она про это невзначай упомянула."
    kt "М-м, звучит как сюжет низкобюджетного фантастического фильма."
    show un laugh pioneer with byso
    "Лена рассмеялась."
    un "Может и так."
    scene bg ext_house_of_mi_night
    show un smile pioneer
    with fade
    "Они дошли до домика Лены."
    kt "Ну чего до..."
    show un shy pioneer with byso
    "Лена, покраснев, поцеловала Константина, чем вогнала его в ступор."
    kt "...завтра."
    un "С-спокойной ночи."
    hide un with byso
    "Проговорила Лена и ушла в свой домик."
    stop music fadeout 3
    "Константин потёр губы и пошёл спать."
    scene bg int_house_of_mt_night2 with fade
    stop ambience fadeout 1
    play sound door_cl volume 0.3
    "Войдя в домик, он по храпу понял что вожатая уже спит."
    th "Если бы так отчёты оформляла как храпела, то цены бы тебе не было."
    scene bg son_kt with byso
    play sound sfx_bed_squeak1
    "Константин снял с себя лишнюю одежду и лёг в постель под умеренный храп вожатой."
    th "По полям, по полям, зелёный трактор едет к нам..."
    show blink
    "Подумал Константин и тут же уснул."
    scene bg cafe
    show unblink
    play music music_list["torture"] fadein 2
    "Очнулся он на стуле в уже знакомом зале."
    gg "Здравствуй.{w=1} Рад меня видеть?"
    kt "Ну привет.{w=1} Не то что бы."
    show image so_gd with byso
    "Генда поправил очки и через спину глянул на Константина."
    gg "Тебе знакомо понятие стабильность?"
    kt "Да, эмоциональная. То чего тебе не хватает."
    hide image so_gd
    show image so_sm
    with byso
    "Создатель усмехнулся."
    gg "Шутки шутишь?{w} Это хорошо. А теперь слушай меня."
    "Создатель подошёл к стулу на котором сидел Константин."
    gg "С твоим появлением кое-кто портит мне стабильность инреальности. Не хочешь мне ничего рассказать?"
    th "Та самая рыжая девочка?.."
    kt "Нет, знать бы ещё чего ты опять несёшь."
    hide image so_sm
    show image so_gd
    with byso
    gg "Хм-м, ладно, допустим, но если ты это знаешь, то тебе мало не покажется."
    "Грозно проговорил создатель. Его выражение лица быстро сменилось на улыбку и он отошёл от Константина."
    hide image so_gd
    show image so_sm
    with byso
    gg "Сегодня у нас блекджек. Играешь на фишки. Если до 3й игры у тебя вылетят все фишки то ты не проснёшься."
    gg "Правила знакомы?"
    kt "Угу. Надо набрать 21"
    "Безынтересно ответил Константин."
    gg "Тогда начнём."
    hide image so_sm
    show image so_gd at cright
    with byso
    "Генда сел на стул и перед ними образовался стол для блекджека."
    show image me_no at left
    with byso
    play sound door_cl
    "Открылся шкаф и оттуда вышел пионер."
    gg "Это Семён, знакомься. Он наш дилер."
    th "Ещё один человек?"
    kt "Ну привет."
    "Семён лишь молча занял положение у стола."
    th "То-то их та девочка на фарш пускает... Быдло."
    me "Вот фишки."
    play sound kosti
    "Он достал из стола 2 фишки и дал их Константину."
    hide image so_gd
    show image so_sm at cright
    with byso
    kt "А вы чё без фишек?"
    gg "На твою-ж жизнь играем а не на мою. А он, так уж и быть, умрёт если ты выиграешь."
    th "М-м..."
    me "Тасую колоду."
    play sound card_mix
    "Семён быстро размешал карты и раздал по две каждому. Свои он выложил на стол рубашкой вниз. Валет буби и семёрка крести."
    "Константин украдкой глянул на карты. У него была четвёрка черви и четвёрка пики."
    gg "Мне не нужно."
    me "Беру карту."
    play sound card_take
    "Дама черви."
    me "На столе перебор."
    th "Везучий ты парень, Сёма."
    kt "Ещё."
    play sound card_take
    "Генда непрерывно смотрел на Константина. Константин подобрал тройку треф."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            play sound card_take
            "Константин получил туза пик."
            kt "Блекджек."
            "Константин выложил свои карты. Генда улыбнулся."
            gg "Ну, поздравляю, живёшь пока."
        "Стоп.":
            $ renpy.block_rollback()
            $ gameoverr += 1
            me "Игроки, вскрывайтесь."
            play sound card_take
            "У Генды в две карты было 20. Он улыбнулся."
            th "Вот чертила..."
            gg "Первый кон - первый пролёт. Ну, в следующей жизни повезёт."
            "Жетон со стола Константина пропал."
    play sound card_mix
    "Семён снова перетасовал колоду."
    "На столе лежала четвёрка буби и король буби."
    me "Генда?"
    gg "Я возьму."
    play sound card_take
    "Семён дал создателю карту."
    hide image so_sm
    show image so_gd at cright
    with byso
    gg "М-м, я в пролёте."
    "Сказал он и насмешливо посмотрел на Константина. У него был дама и шестёрка треф."
    th "Хреново..."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            $ gameoverr += 1
            play sound card_take
            "Король пик. Пролёт."
            hide image so_gd
            show image so_sm at cright
            with byso
            gg "Хе-хе."
        "Стоп.":
            $ renpy.block_rollback()
            "Константин хитро улыбнулся и посмотрел на Семёна."
            play sound card_take
            "Семён занервничал и взял ещё одну."
            "Король пик, стол в пролёте. Семен нервно застучал по столу."
            hide image so_gd
            show image so_sm at cright
            with byso
            gg "А тебе сегодня везёт, ничего не сказать."
            hide image so_sm
            show image so_gd at cright
            with byso
            gg "По крайней мере с тем что кое-кто не знает что такое блеф."
            "Генда раздражённо глянул на Семёна, тот занервничал пуще прежнего."
if gameoverr ==2:
    jump Poker_Death
else:
    jump jigfodpjgosdfjgoijdsogjfduiojgbhiofdmbjmdsiobjo
label jigfodpjgosdfjgoijdsogjfduiojgbhiofdmbjmdsiobjo:
    hide image so_sm
    hide image so_gd
    show image so_gd at cright
    with byso
    play sound card_mix
    me "Тасую колоду."
    play sound card_take
    "Семён размешал карты и раздал по две. Его руки дрожали. На столе 16."
    hide image me_no
    show image me_su at left
    with byso
    me "Б-беру карту."
    play sound card_take
    "Шестёрка пик."
    th "Шестёрка пик может символизировать потерю, эмоциональное беспокойство, не очень удачную дорогу. Н-да, Лена была права."
    hide image me_su
    show image me_st at left
    with byso
    me "На столе п-п... Н-нет.. Я не хочу!"
    gg "Да нет, плохой из тебя помощник..."
    play sound flame_up
    hide image me_st
    hide image so_gd
    show image so_sm at cright
    with flash
    "Семён самовоспламенился и начал в огне кричать и кататься по полу пока не утратил такую способность."
    gg "Меня умиляет это <<я не хочу умирать>> и прочая чушь. Выглядит жалко."
    "Константин, пытаясь не подавать волнения посмотрел в карты. В сумме у него было 17."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            play sound card_take
            "Константин вытащил тройку буби."
            hide image so_sm
            show image so_gd at cright
            with byso
            gg "Тоже возьму... Упс..."
            "Генда выложил на стол даму треф, восьмёрку пик и короля черви."
            gg "Перебор."
        "Стоп.":
            $ renpy.block_rollback()
            $ gameoverr += 1
            gg "А я возьму одну."
            play sound card_take
            "Генда взял карту, рассмеялся и выложил на стол даму треф, восьмёрку пик и тройку буби."
if gameoverr ==2:
    jump Poker_Death
else:
    jump idfgohnohdsbnguofbnosvfhnd87uerw989fhdsuihvo
label idfgohnohdsbnguofbnosvfhnd87uerw989fhdsuihvo:
    hide image so_sm
    hide image so_gd
    show image so_gd at cright
    with byso
    gg "Молодец, отстоял право на жизнь, теперь в кошмар."
    stop music fadeout 3
    show blink
    pause 2
    hide so_gd
    scene bg int_house_of_mt_night2
    show unblink
    play music nightmare
    "Глаза Константина закрылись и он очнулся в домике вожатой."
    "На столе лежала записка."
    play sound sfx_paper_bag
    th "Старый корпус, второй этаж, комната слева, мы ждём."
    th "И где это..."
    play sound sfx_paper_bag
    scene bg map_camp with byso
    "Константин открыл карту."
    th "А, ага. Через весь лагерь бежать..."
    scene bg int_house_of_mt_night2 with byso
    "Константин собрался с силами."
    th "Раз."
    th "Два."
    th "Три!"
    play sound door_break
    scene bg ext_house_of_mt_night_without_light with byso
    "Константин вышиб дверь и побежал в указанном направлении."
    scene bg ext_square_night_blood
    show image me_st at left
    show image monster at right
    with byso
    "На площади Константин заметил как чудовище гонится за каким-то пионером."
    play sound sfx_lena_hits_alisa
    hide image me_st
    hide image monster
    show image monster
    with byso
    play sound2 monster_sfx
    pause 2
    play sound krik
    play sound3 sfx_bones_breaking
    "Тот пионер упал, а монстр начал разделывать его тело, попутно выедая съедобные части."
    th "Сильно..."
    "Константин зачем-то остановился."
    "Монстр представлял собой сильно искорёженную кучу трупов. Некоторые человеческие кости использовались совершенно с другими функциями."
    "Бедренные мышцы были распределены на плечах, а на ногах наоборот мышцы с плеч."
    "Череп был сильно вытянут и видоизменён. Сразу было видно что бог не прилагал свою заботу к этому существу."
    scene bg ext_houses_night with byso
    "Константин решил не задерживаться и побежал дальше."
    scene bg int_old_building_night with byso
    stop music fadeout 3
    "Добежав до старого корпуса, он быстро забежал по лестнице."
    th "Второй этаж... Комната справа..."
    show image poter_n at left
    show un normal pioneer at right
    with byso
    play music ToxiSector fadein 10
    "Забежав в комнату, он встретил пионера и Лену, которые курили в окно."
    show un shy pioneer at right with byso
    un "О, п-привет... И-извини за то что было сегодня вечером."
    kt "Ничего страшного... Так, стоп, чего ты тут делаешь?"
    pp "Да, и тебе привет. Сигаретку?"
    kt "Давай, почему нет."
    "Пионер дал Константину уже зажжённую сигарету."
    show un laugh pioneer at right with byso
    un "Ну ты фокусник."
    show image poter_s at left with byso
    "Пионер ухмыльнулся."
    show un smile pioneer at right with byso
    pp "И не такое умеем."
    kt "Благодарю."
    hide image poter_s with byso
    "Константин раскурил сигарету, а улыбка с лица пионера пропала."
    pp "Так, а теперь по делу."
    "Константин сел на пол, Лена последовала его примеру."
    pp "Значит так, да, поздравляю с пробуждением, Лена. Другой вопрос уже что ты в немного другом теле, но это не важно."
    show un surprise pioneer at right with byso
    un "Да, спасибо."
    pp "Итак, товарищи, я так понимаю вы уже знаете про нашу рыжую красавицу?"
    kt "Да, 145 убийств за день."
    show image poter_s at left with byso
    "Пионер истерично улыбнулся."
    pp "За твой второй. Сейчас общее число равно 548."
    show un shocked pioneer at right with byso
    "Константин и Лена были ошеломлены."
    kt "Как так быстро?"
    hide image poter_s with byso
    pp "Время в инреальности абстрактно. В то время как ты обедаешь, кто-то может уже закончить пару циклов."
    pp "Лене повезло что она смогла восстановиться. Ещё бы пара циклов и её реальная душа была бы стёрта и перезаписана под Лену Тихонову, стандартную пустышку инреальности."
    pp "Кстати, я так помню вы сегодня нашли четвёртое писание."
    show un surprise pioneer at right with byso
    un "Что это?"
    pp "Путеводитель по инреальности так сказать. Белая папочка из подвала."
    kt "И чего там?"
    "Пионер выкинул бычок."
    pp "Не буду распыляться, это надолго. Просто завтра прочитайте сами, полезно будет."
    kt "Понятно. Как ты объяснишь уезд Жени?"
    "Пионер сел на корточки."
    pp "Это удивительно. Она уехала с неким Олегом, хотя ни один автобус инреальности не включают в себя водителя."
    pp "То есть она просто взяла и у всех на глазах уехала в другой сегмент инреальности. Отследить куда мне не удалось, у них походу есть что-то вроде активной маскировки от Генды."
    show un sad pioneer at right with byso
    un "Женя упоминала какое-то сопротивление, может это оно?"
    "Пионер почесал подбородок."
    pp "Один пионер за которым я следил тоже говорил про какое-то сопротивление, да и в писании про него сказано... но я не думал что это правда."
    pp "Тем не менее, мне кажется что оно как формирование бесполезно. Генде хватит трёх-четырёх армий своей нечисти чтоб это сопротивление подавить."
    pp "Нет, ну с другой стороны может у них там свои средства борьбы есть... вряд-ли это спасёт от Генды."
    pp "Так что не знаю... Давайте о наших проблемах. Я сбился с темы."
    kt "Ну?"
    pp "Наша рыжая девочка уже нарезала столько людей что даже инреальность перестала выдерживать такие приколы."
    "Пионер встал и посмотрел в окно."
    pp "Она 100 процентов не связана с Гендой. Она пошатнула стабильность всей инреальности на 20 процентов!"
    show un surprise pioneer at right with byso
    un "Что это значит?"
    pp "Ладно, перескажу кое что из писания. Начнём издалека. Это кошмар - место пыток путников. Сюда попадают все кроме потерявших самосознание Семёнов и других обитателей лагеря."
    show un sad pioneer at right with byso
    un "Я сюда не попадала ранее."
    pp "Ничего не могу сказать, не знаю почему. Я продолжу."
    pp "Симуляция - ваш мир с вашими пустышками и возможно путниками."
    pp "Путник - человек который всё ещё способен осознать то что находится не в родном мире. Пустышка - антоним путника или просто население пустых симуляций."
    pp "Далее. Инреальность - совокупность всех симуляций Генды."
    pp "Потом. Стабильность представляет собой величину от 100 до -100, где 100 это абсолютное равновесие, а -100 разрушение мира. В нуле мир соединяется с кошмаром."
    "Пионер глянул на Лену."
    pp "С того момента можно считать что мир утерян."
    kt "Ага... И чего?"
    pp "Создателю явно не понравились такие фокусы. Он начал поиски причины неведанного ранее ухудшения в работе инреальности."
    pp "Как только он найдёт потенциальную причину, он начнёт собирать отряды на их устранение."
    pp "Рыжая не связана с сопротивлением. Насколько я слышал, в интересах сопротивления спасать, а не резать в фарш, да ещё и с такой страстью."
    pp "Девочка буквально против всех... За одним исключением - она ищет какого-то парня."
    pp "Интересно кем она была до попадания сюда. Ощущение что она даже не человек..."
    pp "Я не помню ни одного такого путника, который сказал бы: <<Мне не хватает разнообразия в убийствах. Я тебе проведу трепанацию черепа циркулярной пилой?>>"
    pp "Это не пустые слова, если что."
    pp "Симуляций всего 10000. 548 уничтожены плюс те которые она косит сейчас."
    pp "Ладно, чего-то мы разговорились, вам надо скоро вставать."
    kt "Хорошо, пробуждай."
    show un surprise pioneer at right with byso
    un "Это как?"
    pp "Сейчас узнаешь, что сказать..."
    pp "Удачи. Загляните в бункер по мере возможности."
    show blink
    stop music fadeout 3
    "Глаза Константина сомкнулись."
    jump d4_withun