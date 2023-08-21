label d3_withre:
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
        scene bg black
        hide load
        with byso
        window show
        jump vuisfdbovbfsdipvbhnidfosvbnipdfvd
    else:
        scene bg bgcg6
        show load
        with byso
        pause 10
        $ bgcg -= 1
        stop music fadeout 2
        scene bg black
        hide load
        with byso
        window show
        jump vuisfdbovbfsdipvbhnidfosvbnipdfvd
label vuisfdbovbfsdipvbhnidfosvbnipdfvd:
    $ save_name = ('Инреальность.\nДень третий.')
    scene bg int_house_of_kt_day
    show image re_sad_swim
    play music music_list["drown"]
    show unblink
    th "Угх.{w}.. Привыкать надо к такому утру."
    "Константин открыл глаза. Напротив лежала Рена, что потирала лоб."
    ren "Утро добрым не бывает..."
    kt "Да, и тебя с мягким пробуждением."
    play sound sms
    "Рена села на кровать и выключила заигравший на телефоне будильник."
    ren "Ну с другой стороны это минимальная плата за то что мы имеем."
    hide image re_sad_swim
    show image re_smile4_pioneer
    with byso
    stop music fadeout 5
    "Проговорила Рена, надевая синюю юбку."
    ren "Еда, досуг, отдельное жильё.{w} Я ранее могла об этом только мечтать."
    "Константин оделся и принялся развязывать галстук, который не перевязывал со дня получения."
    play music music_list["trapped_in_dreams"] fadein 4
    kt "Согласен с тобой.{w} Именно таких моментов мне не хватало всю предыдущую жизнь."
    kt "Я уже даже стал забывать про Генду, ну подумаешь кошмары по ночам."
    ren "Ну не знаю.{w} Пытки по ночам так себе идея."
    kt "Как сказать, в том мире у меня были пытки весь день напролёт."
    kt "Маршрут квартира-работа меня весьма раздражал.{w} Что уж там о людях."
    hide image re_smile4_pioneer
    show image re_smile3_pioneer
    with byso
    "У Константина не получалось завязать галстук, Рена усмехнулась и наклонилась к нему."
    ren "Эх ты, позабыл школьные уроки труда.{w} Давай помогу."
    "Она ловко перевязала и затянула Константину галстук."
    window hide
    menu:
        "Поблагодарить словами.":
            $ renpy.block_rollback()
            hide image re_smile3_pioneer
            show image re_smile2_pioneer
            with byso
            ren "Спасибо в карман не положишь."
            "С усмешкой сказала она и махнула рукой в сторону двери."
            ren "Пошли. Сахарова нас наверняка уже заждалась."
        "Поцеловать.":
            $ renpy.block_rollback()
            $ rerp += 1
            hide image re_smile3_pioneer
            show image re_happy_pioneer
            with byso
            "Константин поцеловал её. Рена немного покраснела и закрыла глаза."
            kt "Спасибо тебе."
            play sound glad
            "Рена легко улыбнулась и погладила Константина по голове."
            ren "Для тебя что угодно."
            hide image re_happy_pioneer
            show image re_smile2_pioneer
            with byso
            ren "Ладно, нас уже Сахарова заждалась."
            kt "Идём."
        "Промолчать.":
            $ renpy.block_rollback()
            hide image re_smile3_pioneer
            show image re_smile_pioneer
            with byso
            "Рена выпрямилась и махнула рукой в сторону двери."
            ren "Пошли. Сахарова нас наверняка уже заждалась."
    play sound sfx_bed_squeak1
    "Константин с улыбкой встал с кровати и пошёл за Реной."
    play sound sfx_close_door_1
    play ambience ambience_camp_center_day
    scene bg ext_house_of_sl_day
    show image re_smile_pioneer
    with byso
    "Улица встретила их прохладным ветерком и переменной облачностью."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена потянулась и глянула на облака."
    stop music fadeout 3
    ren "Так бы всегда..."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at right
    show mt smile pioneer panama at left
    with byso
    "Рену перебила подошедшая вожатая."
    play music music_list["my_daily_life"] fadein 3
    mt "Доброе утро, пионеры.{w} Думала уже вас будить, а вы вроде и сами вовремя просыпаетесь."
    kt "Доброе."
    ren "Доброе утро."
    show mt grin pioneer panama at left with byso
    "Вожатая улыбнулась и посмотрела на домик."
    mt "Вас всё устраивает, никаких проблем с домиком?"
    kt "Да, всё отлично."
    th "Да даже если бы и были, то ей было бы малахитово плевать."
    hide image re_smile_pioneer
    show image re_smile4_pioneer at right
    with byso
    "Рена, видимо, подумала о том же и с улыбкой глянула на Константина."
    show mt smile pioneer panama at left with byso
    mt "Это хорошо.{w} Значит смотрите.{w} Сегодня у вас обходы, как и всегда, но ещё вам нужно помочь Галине Петровне на обед и ужин после завтрака и обеда соответственно."
    hide image re_smile4_pioneer
    show image re_bored_pioneer at right
    with byso
    ren "Кто это?"
    mt "Наша главная повариха.{w} Несколько рабочих отправились в отпуск, потому я поручаю работу вам.{w} Просто делайте то что она вас попросит."
    "Вожатая поправила панамку и окинула взглядом Рену и Константина."
    mt "Задача ясна?"
    kt "А обходы надо делать?"
    show mt grin pioneer panama at left with byso
    mt "После столовой."
    kt "Тогда всё ясно."
    th "Сахарова и в Африке Сахарова. {w}Лишь бы самой ничерта не делать."
    stop music fadeout 3
    mt "Идите. Не смею задерживать."
    hide mt
    hide image re_bored_pioneer
    scene bg ext_square_sunset
    show image re_smile_pioneer
    with byso
    "Рена и Константин отправились на площадь."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    show us grin pioneer at left
    with byso
    play music music_list["i_want_to_play"] fadein 3
    "На площади к ним подбежала Ульянка.{w} Рена мило улыбнулась, заметив её."
    us "Утречка!{w} Как настроение?"
    ren "Доброе.{w} Хорошо, а ты как?"
    show us normal pioneer at left with byso
    "Ульяна немного поменялась в лице."
    us "Да Алиса чудит. Совсем с ней скучно стало.{w} Ходит там одна да только на своей гитаре играет на сцене."
    us "Заболела чтоль..."
    "Константин усмехнулся."
    kt "Видимо ей всё это надоело, вот и сидит тоскует."
    us "Да-а, совсем потеряла хватку."
    show us smile pioneer at left with byso
    us "А вы сегодня готовите?"
    hide image re_smile2_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Да, а ты откуда знаешь?"
    show us grin pioneer at left with byso
    "Ульяна игриво улыбнулась.{w} И без слов стало понятно что она подслушала разговор с Ольгой."
    kt "Понятно. У тебя выдающиеся таланты шпиона."
    us "Агась, от деда досталось. Он был шпионом во время войны.{w} Он может определить кто к нему идёт по стуку в дверь."
    us "Ладненько, я умываться, не скучайте."
    hide us
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    stop music fadeout 3
    "Протараторила Ульянка и испарилась из виду."
    "Константин и Рена пошли в укромное место для курения."
    scene bg ext_polyana_sunset
    show image re_smile_pioneer
    with byso
    play music proshloe fadein 7
    play sound light_inh
    "Сев на тёплую землю, они обменялись сигаретами и закурили."
    ren "Нередко я думала о том, как вообще люди додумались до того чтоб курить табак. Как думаешь?"
    kt "Да наверняка как-то поле с растущим табаком сгорело, пошёл дым, а людям и по кайфу."
    kt "Потом поняли что это из-за растения и начали его собирать."
    kt "Ну далее сама.{w} По крайней мере я так думаю."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена затянулась и глянула на кроны деревьев."
    ren "Вполне логично.{w} Хоть какую-то пользу внесли предки в нашу жизнь."
    kt "Как сказать... С другой стороны все наркотики, в том числе никотин и этанол это средство сокращения людской популяции."
    kt "Вот ты прикинь, люди сами платят за то чтобы пораньше сдохнуть. Сказка для некоторых сфер рынка и пенсионного фонда."
    "Константин затянулся и показал Рене фильтр."
    kt "Вот тебе наглядный пример того как люди это маскируют - фильтр."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Типа так куда менее вредно и меньше запаха?"
    kt "Да, но по сути это лишь реклама от наших любимых табачных компаний.{w} Фильтр не делает сигарету безвредной."
    hide image re_smile_pioneer
    show image re_sad_pioneer
    with byso
    kt "Но я в принципе и не против загнуться на пару-тройку лет пораньше."
    window hide
    menu:
        "Хотя может и теперь всё поменяется.":
            $ renpy.block_rollback()
            $ rerp += 1
            kt "Но кто его знает.{w}.. Слишком поздно всё это со мной происходит."
        "Так что я и не против на эту рекламу цепляться.":
            $ renpy.block_rollback()
            kt "Так и живём."
        "Тем не менее от сигарет, как по мне, пользы больше чем вреда.":
            $ renpy.block_rollback()
            kt "Они хоть меня заставляли по утрам вставать."
    ren "М-да, тяжело."
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Тот мир всё-таки никогда не поменяется, но у нас есть новый."
    ren "И опять-таки всё портит наш любимый Генда."
    play sound sfx_dinner_horn_processed
    "Докурив, Константин встал и потянулся.{w} Вдали заиграл горн."
    kt "Что-то мы правило Архимеда перевернули немного, но ладно.{w} Идём на завтрак?"
    hide image re_smile4_pioneer
    show image re_smile3_pioneer
    with byso
    stop music fadeout 2
    "Усмехнувшись, Рена кивнула и пошла за Константином."
    scene bg ext_dining_hall_near_day
    show image re_bored_pioneer at right
    show sl smile pioneer at left
    with byso
    play music music_list["my_daily_life"] fadein 3
    "Выйдя из столовой, их встретила Славя."
    sl "Утречка, друзья!{w} Как вы, готовы к работе?"
    ren "Друзья, ещё чё хошь..."
    "Прошептала Рена, Константин улыбнулся от её слов и махнул рукой Славе."
    kt "Угу, порядок."
    show sl smile2 pioneer at left with byso
    sl "Поможете мне сегодня?"
    hide image re_bored_pioneer
    show image re_angry2_pioneer at right
    with byso
    ren "Ага, а свою работу когда мы будем делать?"
    show sl surprise pioneer at left with byso
    "Славя, которая рассчитывала на помощь сильно удивилась."
    sl "Как это, вы не хотите помочь товарищу?"
    hide image re_angry2_pioneer
    show image re_angry_pioneer at right
    with byso
    ren "Нет.{w} Точка.{w} У нас своих дел достаточно."
    sl "Ну-у, ладно, идите."
    hide sl
    hide image re_angry_pioneer
    show image re_bored_pioneer
    with byso
    "Удивлённо протянула Славя и скрылась в столовой."
    kt "Сахарова 2.{w} Неточная копия."
    ren "Угу, смотрите во всех кинотеатрах страны..."
    scene bg int_dining_hall_people_day
    show image re_smile_pioneer at right
    show image pov_normal at left
    with byso
    play ambience ambience_dining_hall_full
    "В столовой повариха с раздачи посмотрела на Константина, затем на Рену"
    pov "Доброе утро, мальчики-девочки.{w} Поможете сегодня?"
    kt "Доброе."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    with byso
    ren "Доброе утро. Нас вожатая уже оповестила."
    hide image pov_normal
    show image pov_smile at left
    with byso
    "Повариха мило улыбнулась и открыла пару тарелок с яичницей и аппетитными гренками."
    pov "Хорошо. Сейчас поедите - возвращайтесь на раздачу, я дам задание.{w} Сейчас, ещё сок налью."
    "Налив до краёв светлого яблочного сока, она передала два стакана Константину и Рене."
    kt "Принято, спасибо."
    pov "Пейте на здоровье."
    hide image pov_smile
    hide image re_smile2_pioneer
    show image re_mad_pioneer at left
    show image tl_normal at right
    with byso
    stop music fadeout 2
    "Константин и Рена направились за свой столик.{w} Там их ожидал Толик."
    kt "Так..."
    play music music_list["eat_some_trouble"] fadein 4
    "Рена поставила на столик свою тарелку и села напротив Толика."
    hide image tl_normal
    show image tl_angry at right
    hide image re_mad_pioneer
    show image re_madsmile2_pioneer at left
    with byso
    ren "Чума лысая, куда ты села?"
    kt "Третий день подряд.{w} Мне интересно почему ты продолжаешь тут сидеть."
    ren "Что там у тебя в стакане?{w}.. Чаёк?"
    kt "Да-а Рен, сладкий чай плохо отмывается с волос.{w}.. А, да точно."
    hide image re_madsmile2_pioneer
    show image re_laugh_pioneer at left
    with byso
    play sound sfx_borshtch
    "Рена искренне рассмеялась. Константин взял стакан Толика и оттянув заднюю часть воротника полил его спину."
    kt "Рена, ёмаё, у него на спине все волосы с головы.{w} Я то думал.{w}.. А тут такое переселение народов."
    "Рена продолжала смеяться.{w} Константин взял тарелку гречки на молоке."
    kt "На голову или на спину?"
    hide image tl_angry
    hide image re_laugh_pioneer
    show image re_smile_pioneer
    with byso
    stop music fadeout 2
    "Толик встал и ушёл, оставив еду. Рена еле отсмеялась и смотрела вслед.{w} Константин переставил посуду на соседний столик и поставил свою."
    ren "С каждым днём всё лучше. Какой ужас."
    kt "Ага, неповторимый аттракцион. Приятного кушанья."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Хах, тебе тоже."
    "Сырные гренки напомнили Константину о прошлой жизни."
    kt "Помню делал похожие на утро перед работой.{w} Так выходило что они были самым вкусным за весь день."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Да-а, всё вспоминаю китайский ресторанчик на отшибе.{w} Было время."
    stop ambience
    play sound in_vosp
    play music sab
    scene bg cafe
    show shum_white
    with flash
    mak "Вот где мы можем так вкусно и бюджетно похавать.{w} Фей-фань.{w} Ланч за 200 рублей и ешь пока не треснешь."
    ks "Да-да. Я сразу тебе говорил что место хорошее, а ты отнекивался."
    "Макс усмехнулся и продолжил трапезу."
    mak "Да, безусловно надо будет сюда вернуться."
    "Костя глянул на местную раздачу."
    ks "Было бы хорошо. Кстати тут до этого было много таких рестиков.{w} Позакрывали к чертям."
    mak "А чего так?"
    ks "Роспотреб с рейдом пришёл.{w} Остался только этот."
    hide shum_white
    scene bg cafe
    show shum_white
    with flash
    "Константин пришёл к китайскому ресторану."
    th "Не плохо было бы пообедать. Давно тут не ел."
    "Войдя в ресторан, он увидел в его помещении лишь бюджетную столовку, где уже давно не подавали китайских блюд."
    kt "Последний аванпост пал..."
    stop music
    play ambience ambience_dining_hall_full
    hide shum_white
    scene bg int_dining_hall_people_day
    show image re_smile4_pioneer
    with flash
    kt "Мне вот до сих пор интересно почему рестик закрылся.{w}.. А ещё куда же пропал Макс."
    hide image re_smile4_pioneer
    show image re_sad_pioneer
    with byso
    "Рена положила ногу на ногу и облокотилась на спинку стула."
    ren "Да... Помню уехал и поминай как звали."
    hide image re_sad_pioneer
    show image re_smile_pioneer
    with byso
    ren "Ладно, не будем о нём. Говорить там не о чем.{w} Ты всё?"
    kt "Угу."
    "Сказал Константин и залпом опустошил стакан сока."
    ren "Ну ты пей помедленнее. Даже сок не распробовал."
    kt "Спасибо мам, так нормально."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    "Рена улыбнулась и встала со стула."
    ren "Тогда пошли."
    play music music_list["lightness"] fadein 5
    show image pov_normal at right with byso
    "Вернувшись к раздаче, их встретила повариха."
    pov "Обойдите раздачу, там проход."
    hide image pov_normal with byso
    "Указала она и указала в правую сторону."
    play ambience ambience_dining_hall_empty
    hide image re_smile2_pioneer
    scene bg kitchen
    show image pov_normal at left
    show image re_smile_pioneer at right
    with byso
    "Константин и Рена попали в основной блок столовой."
    pov "Итак, готовить умеете?"
    "Уточнила повариха, собирая чистые тарелки в стопку."
    kt "Я на любительском уровне."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    with byso
    ren "Я тоже."
    pov "Замечательно. {w}На обед надо сварить перловку. Мясо поставить в духовой шкаф 200 градусов на 2 часа, потом на 80 градусов до обеда.{w} Суп готов, компот и тарелки на мне."
    pov "Запомнили?"
    hide image re_smile2_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Да."
    hide image pov_normal
    show image pov_smile at left
    with byso
    stop music fadeout 3
    pov "Хорошо, тогда работаем.{w} Ножи и прочее на столе."
    "Кивнув, она пошла к раковине и взяла жёлтые перчатки."
    hide image re_smile4_pioneer
    show image re_surprise_pioneer at right
    with byso
    ren "Смотри..."
    "Шепнула Рена и указала на запястье поварихи.{w} На ней была свежая наколка в виде волка."
    th "Неужто она..."
    hide image re_surprise_pioneer
    hide image pov_smile
    show image re_surprise_pioneer
    with byso
    $ volume(0.34, "music")
    play sound sfx_radio_tune
    pause 1
    play music sanari fadein 3
    "Повариха ушла на мойку. Заиграло радио.{w} Рена и Константин остались одни."
    kt "Интересно всё-таки почему такая девушка стала той свиноподобной бабкой."
    hide image re_surprise_pioneer
    show image re_sad_pioneer
    with byso
    "Рена взяла со стола нож и проверила его на остроту."
    ren "Видимо нашёлся обрыган, который с ней такое сделал.{w} Частое в достаточной степени явление."
    kt "М-да... Печально, что сказать."
    play sound fridge
    "Рена открыла холодильник и нашла несколько больших кусков свиного окорока."
    kt "Помочь?"
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Не, я сама."
    "Она с необычайной лёгкостью подняла несколько огромных упакованных тушек и положила их на стол."
    th "Неплохо она так... В качалку тайком ходит?"
    ren "Я порежу мясо в духовку, а ты свари перловки."
    kt "Есть."
    "Отчеканил Константин и взял две кастрюли по 20 литров."
    "На столе лежало 10 бумажных упаковок перловки."
    kt "Перловку всю варим?!"
    "Крикнул Констатин поварихе."
    pov "Да. Мясо тоже всё."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Так точно."
    "Константин принялся наполнять кастрюли водой."
    kt "День ностальгии прямо. {w}Я же работал в общепите."
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Я такого не помню. Это когда?"
    "Уточнила Рена не отвлекаясь от нарезки свинины."
    kt "А, ну мне тогда было 15 я подрабатывал нелегально.{w} Знакомые устроили."
    kt "Ставка помощника повара. {w}27 с копейками не самая плохая зарплата для подростка."
    hide image re_smile3_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Хе, с учётом того что тебе в <<Полимере>> не доплачивали, то и для взрослого."
    kt "Ага.{w} Жуть жуткая."
    kt "Но честно говоря я ни о чём тогда не жалел."
    "Константин наполнил обе кастрюли до нужного уровня и поставил на плиту."
    kt "М-м, газовые промышленные.{w} Чем не школьная столовая?"
    play sound light_inh
    pause 0.5
    stop sound
    "Он достал из кармана свою зажигалку и поджёг конфорку."
    kt "Так вот."
    kt "Именно во время работы там я понял что только меня по счастливой случайности окружает быдло."
    kt "Школа, универ, работа по спецу.{w} На той подработке у меня был лучший коллектив."
    kt "Слаженный механизм.{w} За 2 лета работы не было никаких глобальных конфликтов. Даже я на время стал частью этого механизма."
    kt "Повар в горячем цеху, мясник, раздатчик и повар холодного цеха."
    "Константин насыпал по 5 килограмм перловки и по 5 ложек соли в каждый чан и убавил огонь."
    hide image re_smile2_pioneer
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Да, какой универсал."
    "Словно с похвалой съязвила Рена, отложив ножик."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Где противень?"
    kt "Не знаю, иди спроси на мойке."
    hide image re_smile_pioneer with byso
    "Она ушла на мойку.{w} Константина поразила скорость и качество работы Рены."
    th "Ровные куски 2х2х2.{w} Рена, конечно, мастер."
    th "Хотя да, у неё достаточно большой опыт в нарезке <<свинины>>..."
    show image re_smile2_pioneer with byso
    "Рена вернулась со стопкой противней и разложила их по столу."
    kt "Давай помогу."
    "Константин начал раскладывать ровно нарезанное мясо по поверхности противня."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Знаешь, если бы я вернулась в тот мир, то я бы хотела связать свою жизнь с едой."
    kt "Общепит?{w} Серьёзно?"
    ren "Ага. Мне кажется это достаточно интересно."
    ren "Вкусовые рецепторы способны воспринимать огромный спектр вкусов.{w} С этим, разумеется, можно экспериментировать."
    ren "Работа не требует долгого освоения и сама по себе является интересным делом."
    window hide
    menu:
        "Ну да, у тебя уже есть хороший опыт в нарезке.":
            $ renpy.block_rollback()
            hide image re_smile3_pioneer
            show image re_angry2_pioneer
            with byso
            ren "Не смешно."
            "Отрезала Рена и строго посмотрела на Константина."
            ren "Если честно я не сильно хочу к этому возвращаться."
            kt "Прости, не подумал."
            hide image re_angry2_pioneer
            show image re_bored_pioneer
            with byso
            ren "Ладно, забыли."
        "Не знаю, как по мне на любителя.":
            $ renpy.block_rollback()
            $ rerp += 1
            hide image re_smile3_pioneer
            show image re_smile2_pioneer
            with byso
            ren "Всяко лучше чем тухнуть в <<Полимере>>."
            "С ехидной усмешкой подметила Рена."
            kt "Ха-ха, смешно."
            "С той же усмешкой ответил Константин."
    ren "Так а теперь в духовки."
    "Указала Рена, доложив последний кусок свинины в ёмкость."
    "Константин еле разобрался как заставить советский аппарат работать и поставил несколько противней."
    hide image re_bored_pioneer
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Готово.{w} Перловка как вижу тоже."
    show mt normal pioneer at right with byso
    "Рена поставила минимальный огонь. На кухню пришла Сахарова."
    show mt smile pioneer at right with byso
    mt "Работаете вижу."
    "Константин огорчённо вздохнул и посмотрел на вожатую."
    kt "Да, уже закончили.{w} В чём дело?"
    mt "Как сдадите работу идите на площадь.{w} У нас сюрприз."
    ren "Хорошо, поняли."
    hide mt with byso
    "Вожатая улыбнулась и ушла."
    kt "Галина Петровна!{w} У нас всё."
    pov "Да, быстро вы.{w}.. Сейчас посмотрю."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    show image pov_normal at left
    with byso
    "Повариха вышла с мойки и сложила перчатки на раковину."
    "Сняв крышку с кастрюли перловки, она ложкой достала пару крупиц и попробовала."
    hide image pov_normal
    show image pov_smile at left
    with byso
    pov "Хм-м, даже посолил в меру. Хорошо."
    "Затем она открыла духовку."
    pov "Мясо жарится.{w}.. А как нарезано, от{w=0.2}-лич{w=0.2}-но!"
    kt "Спасибо, мы старались."
    pov "Хорошо, спасибо за помощь ребята. Поможете ещё с ужином и цены вам не будет.{w} Теперь идите, я дальше сама."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Спасибо."
    hide image pov_smile
    hide image re_smile_pioneer
    scene bg int_dining_hall_day
    show image re_smile_pioneer
    with byso
    stop music fadeout 3
    "Константин и Рена обошли раздачу."
    kt "Может повариха-продавщица не такая плохая женщина, как могло казаться там."
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Ну да.{w}.. Кажется словно она взята более молодого образца чтоль..."
    $ volume(1, "music")
    play ambience ambience_camp_center_day
    play music music_list["your_bright_side"] fadein 3
    hide image re_smile3_pioneer
    scene bg ext_square_day
    show image re_smile_pioneer at right
    show mt smile pioneer panama
    show un smile2 pioneer at fleft
    show mz smile pioneer at left
    with fade
    "На площади собрался весь отряд.{w} Ольга фотографировала Лену и Женю на новенький <<Киев-80>>."
    mt "А вот и оставшиеся из наставников."
    hide mz 
    hide un 
    with byso
    "Подметила Ольга и передала 2 листа быстропроявляющейся плёнки членам литературного клуба."
    th "Я конечно не уверен, но мне кажется в это время не должны были такую фотопечать изобрести..."
    mt "Сегодня нам доставили фотоаппарат вместе с запчастями для кибернетиков.{w} Каждому по две фотографии."
    hide image re_smile_pioneer
    show image re_laugh_pioneer at right
    with byso
    "Рена радостно схватила за руку Константина."
    ren "Я с Костей!"
    stop music fadeout 1
    rm "Не понял момент."
    hide image re_laugh_pioneer
    show image rm_an at left
    show image re_mad_pioneer at right
    with byso
    play music music_list["drown"]
    "Подошёл недовольный Рома.{w} Рена быстро омрачнела."
    show mt grin pioneer panama with byso
    mt "Ну вы решайте, я пока сфотографирую остальных."
    hide mt with byso
    ren "Что ты не понял конкретно?"
    rm "Я буду фотографироваться с Костей.{w} Он мой брат."
    rm "Да и фотоаппарат с плёнкой доставили нам, потому мне и решать."
    hide image re_mad_pioneer
    show image re_madsmile2_pioneer at cleft
    with byso
    "Рена почесала шею и подошла к Роме в поинт бланк."
    ren "Да?{w} Давай отойдём поболтаем?"
    rm "Пф, пошли!"
    hide image rm_an
    hide image re_madsmile2_pioneer
    scene bg ext_path2_day
    show image re_madsmile2_pioneer
    show image rm_an at right
    with byso
    "Рена и Рома отошли с площади, Константин пошёл за ними."
    "Не приближаясь к центру конфликта, Константин смотрел и слушал."
    hide image re_madsmile2_pioneer
    show image re_mad_pioneer
    hide image rm_an
    play sound sfx_punch_washstand volume 1.3
    play music "<from 21.5>inrealnost/Music/Music/kittycity.mp3"
    "Как только Рена вышла из поля зрения людей на площади, она дала Роме сильный удар в солнечное сплетение." with vpunch
    "Настолько резкого и сильного удара Рома просто не мог ожидать в этот момент, потому быстро согнулся в 90 градусов."
    ren "Если ты думаешь что я о тебе кроме истории с котёнком ничего не знаю, то ты сильно в этом ошибаешься."
    ren "Я о тебе много знаю, скотина."
    "Прошипела Рена и схватила его за волосы."
    ren "Если ты, тупорылая свинина, будешь мне мешать..."
    "Она за волосы подтянула лицо Ромы на уровень своего и смотрела чётко в его глаза."
    ren "То я с тебя скальп сниму. {cps=6}Лично...{/cps}"
    ren "Он мой.{w} Ни твой, ни вожатой, ни кого либо ещё.{w} Мой."
    ren "И любой кто будет мне мешать получит своё."
    ren "Возражения?"
    "Рене удалось запугать Рому. Он не решился возразить."
    hide image re_mad_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Отлично.{w} А теперь прочь с дороги."
    stop music fadeout 2
    "Приказала она и за волосы оттянула Рому в сторону."
    hide image re_smile2_pioneer
    scene bg ext_square_day
    show image re_smile2_pioneer at right
    show image rm_th
    with byso
    play music music_list["your_bright_side"] fadein 3
    "Константин принял стандартное положение на площади.{w} Рома и Рена вернулись."
    rm "Ладно, я с клубом сфотографируюсь."
    ren "Класс, теперь нам ничего не мешает."
    hide image rm_th
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена снова взяла Константина за руку и повела к Ольге."
    kt "Быстро ты его переубедила. Что сказала?"
    ren "Вежливо попросила уступить даме."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at right
    show mt smile pioneer panama at left
    with byso
    "С милой улыбкой ответила Рена. Вместе они подошли к вожатой."
    kt "Мы хотим сфотографироваться."
    mt "Хорошо, решили. Вставайте."
    "Константин и Рена встали на фоне медного Генды.{w} Рена держала Константина за руку."
    mt "Два кадра, стойте смирно."
    scene bg ext_square_day
    show image re_serious2_pioneer at right
    show mt normal pioneer panama at left
    with flash
    play sound fotoapparat
    "Константина ослепила вспышка фотоаппарата."
    th "На кой чёрт днём снимать со вспышкой..."
    "Подумал он и потёр глаза."
    ren "Ни ума не совести..."
    "Шёпотом пробормотала Рена и прикрыла глаза рукой."
    kt "Ага..."
    hide image re_serious2_pioneer
    show image re_smile_pioneer at right
    show mt smile pioneer panama at left
    with byso
    mt "Так, вторая фотография, снова смирно."
    scene bg ext_square_day
    show image re_smile_pioneer at right
    show mt normal pioneer panama at left
    with flash
    play sound fotoapparat
    "Константина снова ослепила вспышка фотоаппарата."
    "Вожатая достала второй лист и раздала по одному."
    mt "Вот ваши фотографии.{w} А теперь давайте все вместе, кучкуйтесь."
    "Весь отряд встал в плотную шеренгу. Ульяна и Шурик сели на корточки поодаль друг от друга."
    mt "Итак. Раз.{w} Два.{w} Три."
    hide image re_madsmile2_pioneer with fade
    "Спустя 5 минут вожатая наделала фотографий на всех и раздала их каждому."
    mt "Так, а теперь по делам. До обеда чтоб никто не бездельничал, я всё вижу."
    hide mt
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    kt "Да-да, ага."
    "Рена улыбнулась и засмотрелась на фотографию с Константином."
    ren "Трофей."
    "С усмешкой протянула она и положила фотографию в карман."
    kt "Пойдём донесём до домика. Они особой износостойкостью не отличаются."
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    stop music fadeout 1
    ren "Окей, пошли."
    show us calml pioneer at right with byso
    play music music_list["i_want_to_play"] 
    us "{cps=14}О-к-е-й{/cps}.{w} Что это значит?"
    th "М-да, теперь выкручивайся..."
    hide image re_smile4_pioneer
    show image re_smile3_pioneer
    with byso
    "Недолго думая Рена нашла ответ на вопрос любопытной Ульянки."
    ren "Окей - наше с Константином тайное слово, означающее утверждение.{w} Только никому!"
    show us grin pioneer at right with byso
    "Ульянка игриво подмигнула."
    us "Окей, никто об этом не узнает!{w} А кибернетики робота начали строить."
    kt "Мы посмотрим. Что там?"
    us "Как и в той бумажке.{w} Робот кошкодевочка, так ещё и голая!"
    hide image re_smile4_pioneer
    show image re_laugh_pioneer
    with byso
    "Константин и Рена рассмеялись."
    ren "Какой ужас!"
    kt "Ну ладно, беги, нам тоже надо по делам."
    show us laugh2 pioneer at right with byso
    us "Бегу-бегу, до встречи."
    hide us with byso
    stop music fadeout 2
    "Сказала Ульяна и убежала."
    kt "Ловко. Никто и не догадается."
    hide image re_laugh_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Да, забыла я что это слово англицизм.{w} В СССР такого не было!"
    kt "Хе, иди давай, англичанка."
    hide image re_smile4_pioneer
    scene bg int_house_of_kt_day
    show image re_mad_pioneer
    with fade
    stop ambience
    "Войдя в домик они заметили что на столе появилось зелёное яблоко."
    kt "Откуда?"
    ren "Ни малейшего понятия..."
    play music music_list["no_tresspassing"]
    play sound sfx_punch_medium
    "Константин не долго думая хотел было откусить кусок, но Рена резко выхватила яблоко."
    ren "И сразу в рот?{w} Оно может быть отравлено."
    kt "Я тебе что Белоснежка?"
    "Попытался отшутиться Константин.{w} Рена говорила с полной серьёзностью."
    ren "В лагере есть таблетки цианистого натрия.{w} У меня нет с собой тиосульфата натрия чтоб его нейтрализовать."
    kt "Откуда?.."
    hide image re_mad_pioneer
    show image re_angry_pioneer
    with byso
    ren "Оттуда.{w} Не стоит."
    stop music fadeout 3
    "Рена выкинула яблоко в окно."
    kt "Хорошо..."
    hide image re_angry_pioneer
    show image re_smile4_pioneer
    with byso
    play music exodus fadein 10
    "Ситуация быстро позабылась.{w} Они убрали 4 фотографии в шкафчик."
    ren "Не хочешь сегодня искупаться?"
    kt "Да, было бы славно.{w} Если будет время - сходим."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Обязательно найдём."
    play sound sfx_open_cabinet_2
    "С тёплой улыбкой ответила Рена и закрыла шкафчик."
    play sound sfx_bed_squeak2
    "Константин улёгся на кровать и засмотрелся в потолок."
    ren "О чём задумался?"
    play sound sfx_bed_squeak1
    hide image re_smile_pioneer
    show image re_smile3_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Спросила Рена и легла рядом."
    kt "Да залип просто.{w} А ты чего?"
    hide image re_smile3_pioneer
    show image re_smile2_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    ren "Тоже хочу поваляться.{w}.. А если с тобой то вдвойне."
    kt "Чисто вопрос из любопытсва, а почему я тебе так приглянулся?"
    hide image re_smile2_pioneer
    show image re_smile4_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Рена повернулась к Константину и провела рукой по его щеке."
    ren "А на это нужны причины?"
    kt "Нет, не то что бы, но просто интересно.{w} Я же ничем не отличаюсь от других."
    hide image re_smile4_pioneer
    show image re_smile2_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Рена тихо хихикнула и продолжала гладить Константина по голове."
    ren "А вот тут ты не прав.{w}Как я и говорила."
    ren "Убирая более очевидные на то причины, ты для меня всё равно особенный."
    ren "Твои мысли идентичны моим, убеждения у нас схожие, ты мне визуально приятен, ну и конечно же мне нравится что ты не бросаешь меня и уделяешь внимание."
if rerp > 5:
    ren "Да и такому вниманию завидовали любые другие люди."
    ren "Я это ценю больше дарованной мне жизни и буду рада дать тебе всё что угодно, чтоб хоть немного за него расплатиться."
    jump fdnujiosanviofadsvnasipodfnv
else:
    ren "Я как и ты раньше.{w} Люблю внимание, даже самое незначительное."
    jump fdnujiosanviofadsvnasipodfnv
label fdnujiosanviofadsvnasipodfnv:
    hide image re_smile2_pioneer
    show image re_smile_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    ren "И вчера когда ты сказал что я могу тебя убить, ты очень сильно ошибся."
    hide image re_smile_pioneer
    show image re_sad2_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    ren "Я не могу тебе навредить, так как мне самой будет от этого больно. Морально больно."
    ren "В последний день в том мире я поняла насколько бывает плохо в одиночестве на своей шкуре."
    ren "Для меня это длилось неделями. Хоть и для тебя это показалось одним днём, то для меня это было целое приключение."
    hide image re_sad2_pioneer
    show image re_smile4_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Она легла на плечо Константина и закрыла глаза."
    ren "Приключение, которое я хочу забыть и жить с тобой."
    ren "Только."
    ren "С тобой."
    "Рена расслабленно вздохнула."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    ren "И я порву в клочки любого кто захочет этому помешать."
    ren "Говоря метафорично, мне один бог - ты. Я твоя служительница."
    "Константин усмехнулся."
    kt "Да какой там бог.{w} Я всё тот же болтик из системы того мира..."
    hide image re_smile_pioneer
    show image re_smile4_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    ren "Ты на несколько голов выше того скота.{w} Я помню тех кто был у тебя в последних годах школы и 4 года в вузе."
    "Рена легла на спину."
    hide image re_smile4_pioneer
    show image re_madsmile2_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    ren "Тоже что эти <<Семёны>>, мусор.{w} Мусор у которого нет права на жизнь, но система нашего родного мира постоянно хотела обмануть естественный отбор."
    ren "Сильным мира сего не нужны умные и рассудительные, им нужны тупые и раболепные.{w} Я не такая, ты не такой, вот потому и нередко у нас возникают недопонимания с социумом."
    play sound sfx_dinner_horn_processed
    hide image re_madsmile2_pioneer
    show image re_smile_pioneer
    with byso
    stop music fadeout 3
    "На улице заиграл горн. Рена встала с кровати."
    ren "Выживает сильнейший.{w} Лучше в этой иерархии быть хищником и напоминать скоту его место."
    "Константин тоже встал с кровати и потянулся."
    ren "И я была бы рада, если бы ты меня в этом поддержал."
    hide image re_smile_pioneer
    show image re_smile4_pioneer at center:
        zoom 1.75
        yanchor 0.1
    with byso
    "Она подошла к Константину на расстояние пяти сантиметров."
    ren "Я охотник, ты охотник, а они лишь мясо."
    kt "Ну ладно-ладно, потянуло тебя на ролевые игры. Пошли есть давай!"
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    "Рена поддержала усмешку Константина и пошла за ним."
    play ambience ambience_dining_hall_full
    play music music_list["silhouette_in_sunset"] fadein 3
    hide re_smile_pioneer
    scene bg int_dining_hall_people_day
    show image pov_smile at left
    show image re_smile2_pioneer at right
    with fade
    "В столовой было уже достаточно людно.{w} На раздаче их встретила улыбающаяся Галина Петровна."
    pov "Спасибо за помощь, вы мне сильно помогли. {w}После обеда останетесь?"
    kt "Не за что."
    hide image re_smile2_pioneer
    show image re_smile_pioneer at right
    with byso
    ren "Да, конечно поможем."
    "Повариха улыбнулась и достала им отдельные тарелки с наваристым гороховым супом и мясным рагу."
    pov "Отлично.{w} Вот ваша еда."
    "Долив два стакана рубинового киселя она поставила их по подносам."
    pov "Приятного аппетита."
    kt "Спасибо."
    stop music fadeout 3
    hide image pov_smile with byso
    show image tl_normal at left with byso
    "За столиком их уже ожидал Толик."
    play music music_list["that_s_our_madhouse"] fadein 3
    ren "Ста-арый БДСМщик Терентий..."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    hide image tl_normal
    show image tl_angry at left
    with byso
    play sound sfx_punch_medium
    "Рена поставила свою еду напротив и отобрала у Толика поднос."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer at right
    with byso
    ren "Избушку свою подметает плетью..."
    play sound sfx_water_splash
    "Она вывалила всю еду с тарелок Толика в мусорку и поставила пустые тарелки обратно."
    ren "За крюки себя вешает снова и снова..."
    play sound dvizh
    pause 0.34
    hide image re_smile3_pioneer
    show image re_smile4_pioneer at left
    hide image tl_angry
    show image tl_angry at fleft
    with byso
    "Взяв стул с Толиком, она оттащила его к мусорке и оставила там."
    ren "Ему девяно-осто он не помнит стоп-слова."
    hide image tl_angry with byso
    stop music fadeout 3
    "Толик молча ушёл, Константин тем временем изливался в хохоте."
    hide image re_smile4_pioneer
    show image re_smile2_pioneer
    with byso
    kt "Ух-х, ну ты вспомнила конечно, аплодирую стоя."
    play sound sfx_simon_applause volume 0.5
    "Константин похлопал такому выдающиеся представлению, Рена махнула рукой и кивнула."
    ren "Садись уже, рот порвёшь."
    "Спустя несколько секунд он отсмеялся и сел за стол и начал есть суп."
    hide image re_smile2_pioneer
    show image re_bored_pioneer
    show mt angry pioneer at left
    with byso
    play music music_list["two_glasses_of_melancholy"]
    "Через 5 минут портить аппетит компании пришла вожатая. Недовольная вожатая."
    mt "Вы почему на обход не пошли?"
    kt "А, ой. Забыли."
    ren "Или не очень хотели..."
    "Прошептала Рена. Вожатая колкости не услышала."
    mt "Чтоб такого не было!"
    ren "Да-да, хорошо."
    mt "Славно."
    show mt normal pioneer at left with byso
    mt "Проверьте сегодня все клубы и доложите лично мне. Потом будете свободны."
    kt "Понято-принято."
    hide mt
    show mt surprise pioneer at fleft
    hide image re_bored_pioneer
    show image re_shy_pioneer
    with byso
    "Вожатая уже было молча ушла, но заметив еду в мусорке остановилась."
    mt "Это чьё?"
    "Константин чуть не подавился со смеху.{w} Рена пыталась скрыть улыбку."
    ren "Да это Толик из другого отряда. Он просто выкинул еду и ушёл.{w} Даже тарелки оставил."
    mt "Ясно, я поговорю."
    hide mt
    hide image re_shy_pioneer
    show image re_sad_pioneer
    with byso
    "Пробормотала Сахарова и скрылась из виду."
    kt "Чего-то она сегодня не в настроении."
    ren "Да, я это тоже заметила.{w} Всё ей не так."
    stop music fadeout 3
    hide image re_sad_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Кстати, я ещё одну песенку вспомнила.{w} Только мою любимую."
    play music music_list["trapped_in_dreams"] fadein 2
    "Константин отставил пустую тарелку и с интересом глянул на Рену."
    kt "Какая же?"
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Помнишь того неизвестного исполнителя?{w}.. Bloody art, вот."
    kt "Конечно помню.{w} Он же <<Новый мир>> написал."
    kt "Жаль что у него мало треков было, отличную музыку писал.{w} Просто шикарную, даже более лаконичных слов не подобрать."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    "Рена засмотрелась в окно, про себя напевая мотив песни."
    ren "Так я помню такую песню, <<Незнакомка>>.{w} Она мне больше всего нравится."
    "Константин ухмыльнулся."
    kt "Грустит в печали незнакомка..."
    kt "Рад что у тебя есть вкус."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Спасибо-спасибо."
    "Ехидно проговорила Рена и доела рагу."
    "Константин подпёр голову рукой и тоже засмотрелся в окно."
    kt "Сейчас бы пива холодного..."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "У нас есть портвейн и ликёр. Можем под вечер выпить."
    "Константин оживился."
    kt "Точно! Отличная идея, давно хотел накатить, только никак не мог про запаску вспомнить."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Но это вечером. {w}Сейчас пошли готовить."
    kt "Идём."
    play ambience ambience_dining_hall_empty
    hide image re_smile2_pioneer
    scene bg kitchen
    show image pov_normal at left
    show image re_smile_pioneer at right
    with byso
    "Зайдя за раздачу они вернулись на кухню."
    pov "О, вы уже всё? Как вам супчик?"
    hide image re_smile_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Отлично, очень вкусно. Чего сейчас готовим?"
    hide image pov_normal
    show image pov_smile at left
    with byso
    pov "Так-так."
    play sound sfx_paper_bag
    "Галина Петровна достала свой блокнот и начала его листать."
    play sound sfx_paper_bag
    pov "Где-ж ты там...{w} А, во.{w} Капуста жаренная, минтай в муке и растворимый напиток <<Лимон>>."
    pov "Всё на вас.{w} Рыба нарезана на столе, мука и капуста в кладовке.{w}.. А вот раствор искать надо, я поищу и сделаю."
    hide image pov_smile
    show image pov_normal at left
    with byso
    pov "Не подумайте что я села на вас и поехала, посуды и поставок куда больше."
    stop music fadeout 3
    kt "Да ничего, порядок."
    hide image re_smile4_pioneer
    show image re_smile3_pioneer at right
    with byso
    ren "Справимся."
    hide image pov_normal
    show image pov_smile at left
    with byso
    pov "Отлично, работаем."
    hide image pov_smile
    hide image re_smile3_pioneer
    show image re_smile3_pioneer
    with byso
    $ volume(0.34, "music")
    play sound sfx_radio_tune
    pause 1
    play music wpstar fadein 3
    "Повариха включила радио и ушла на мойку."
    kt "Ты чем займёшься?"
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    ren "Давай я на капусту, ты на рыбу."
    hide image re_smile_pioneer with byso
    "Константин надел перчатки, взял кастрюлю и стал перекладывать в неё рыбу с доски.{w} Рена ушла в кладовку."
    "Сложив всю рыбу в ёмкость, он услышал с кладовки знакомую мелодию."
    th "Я тоже помню эту песню..."
    "Константин мигом вспомнил все слова песни."
    th "Она танцуе-ет под дождём,"
    th "Она рисуе-ет чёрной краской."
    th "Дом, в котором мы живём..."
    th "Жизнь, похожую на сказку."
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    "Рена вывезла тележку с десятком кочанов капусты и пакетом муки."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Держи."
    "Она подала ему белый бумажный пакет с соответствующей подписью."
    kt "Благодарю."
    hide image re_smile4_pioneer
    show image re_sad_pioneer
    with byso
    "Константин нашёл сковородку для жарки, противень для готовой рыбы и тарелку для обвалки в муке.{w} Рена в свою очередь начала шинковать капусту."
    ren "В такие моменты иногда неприятно думать о том кому ты готовишь.{w} Готовим ведь для таких как Толик."
    "Сковорода нагрелась до нужной температуры и Константин преступил к готовке. Воздух в столовой быстро насытился запахом жареной рыбы."
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Не по теме конечно, но я всё вспоминаю препода по философии."
    kt "Ну ты вспомнила конечно. И чего?"
    hide image re_smile4_pioneer
    show image re_smile3_pioneer
    with byso
    ren "На первых лекциях он спросил, мол что же такое мир."
    kt "Ха, да, помню.{w} Странная тема когда на философии есть правильные и неправильные ответы."
    "Константин обжарил первую партию рыбы и начал валять новую. Рена продолжала нарезать капусту."
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    ren "Ты тогда ответил что это совокупность всех явлений происходящих вокруг и что-то там, уже не припомню точной формулировки честно говоря."
    ren "У меня на этот вопрос другое мнение."
    kt "Ну?"
    hide image re_smile_pioneer
    show image re_serious2_pioneer
    with byso
    ren "Мир представляет собой не то что может чувствовать человек.{w} Вымышленные миры, виртуальные миры и тому подобное к тому тоже относятся."
    ren "Абстрактные и иллюзорные в том числе.{w} Мы никогда не сможем их прочувствовать по настоящему, но я не про это."
    kt "И тогда в чём суть?{w} Ты себе противоречишь."
    ren "Дослушай. Был такой философ, Ник Бостром. Можно считать что он и задал ту самую гипотезу симуляции.{w} Суть в том что теперь это не просто представление рандомного человека."
    ren "Теперь это наша нынешняя жизнь.{w} Событием 3 дня назад мы подтвердили то что и наш мир был схожей на эту симуляцией. Нас перенесли словно файлы с одной директории в другую."
    ren "Возможно у неё была своя стабильность, результатом которой были войны, геноциды и прочие причины массового мора."
    ren "Таким образом я хочу привести к тому что общепринятого понятия <<мир>> как такового не существует."
    ren "Я не беру в этом плане <<миры Семёнов>>, это как нарицательное.{w} Пустое подпространство."
    ren "То что у людей нашего родного <<мира>> таковым считалось разрушилось на наших глазах.{w} Нет бога, нет смерти, есть перемещение в другое подпространство."
    ren "И то-ли нам так повезло попасть именно сюда, то-ли это участь каждого."
    "Константин сложил прожаренную рыбу и глянул в сторону."
    kt "Нет, нам именно так повезло.{w} Остальные люди попадают в другое место. Генда говорил мне об этом."
    kt "Выбрал он меня по своим критериям. {w}Как там... Критерий бесполезности обществу."
    kt "Одиночество и отсутствие социальных связей."
    kt "Тебя он захватил сам того не понимая, да и не факт что поймёт, он за нами не следит вроде как."
    kt "Да и честно говоря мне никогда не было страшно покинуть тот мир.{w} Боялся я только наложить на себя руки самостоятельно."
    kt "Мне вот что любопытно, стоит ли кто-то над Гендой?"
    hide image re_serious2_pioneer
    show image re_serious3_pioneer
    with byso
    ren "Хм-м, думаю в этой реальности вряд-ли."
    ren "Зачем иначе кому-либо ему позволять таскать людей из других реальностей."
    hide image re_serious3_pioneer
    show image re_smile2_pioneer
    with byso
    "Рена закончила с капустой и подойдя сзади положила подбородок на плечо Константина."
    ren "У меня нарезано.{w} Когда освободишь сковородку?"
    kt "Через 1-2 прогона. Спроси пока у повариха куда складывать готовое."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Хорошо."
    hide image re_smile_pioneer with byso
    pause 1
    show image re_smile2_pioneer with byso
    "Рена пошла на мойку и быстро вернулась."
    ren "Говорит в духовку на 60."
    kt "Ладно, последний прогон."
    "Сказал он, сложив на сковородку последние кусочки."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Знаешь, философия всё-таки интересная тема."
    kt "Что, теперь не пищепром, а преподавательское дело?"
    hide image re_smile3_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Ну нет, меня вообще в такую сферу нельзя.{w} Выпускники станут экстремистами."
    "Самоиронично усмехнулась Рена, Константин поддержал усмешку."
    kt "Всё, рыба готова. Теперь капуста."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Я займусь, отнеси пока в духовку."
    kt "Уже иду."
    "Константин отнёс противень в духовку и выставил заданные настройки.{w} Вернувшись к Рене, он сел на стул."
    hide image re_smile_pioneer
    show image pov_normal at left
    show image re_smile2_pioneer at right
    with byso
    pov "Ну как у вас там?"
    kt "Да вот, только капуста осталась."
    hide image pov_normal
    show image pov_smile at left
    with byso
    pov "Помоги ей что-ль, чего сел то?"
    hide image re_smile2_pioneer
    show image re_smile_pioneer at right
    with byso
    "С усмешкой спросила повариха.{w} Рена хихинула и повернулась к ней."
    ren "Не нужно, я сама хочу."
    pov "Ну тогда ладно.{w} Не хотите пообщаться? Я всё равно должна ещё напиток развести."
    kt "Давайте, почему нет."
    pov "Вы тут что-то без меня обсуждали, о чём вы там?"
    hide image re_smile_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Да так, философия."
    play sound sfx_open_metal_hatch volume 0.6
    "Повариха открыла огромный чан для компота и начала заливать туда воду из под крана."
    pov "Философия дело хорошее.{w} Какой придерживаетесь?"
    kt "А вы интересуетесь философией?"
    "Галина Петровна с ехидной улыбкой глянула на Константина."
    pov "Да-да. Периодически брала книги с библиотеки взамен на чайники для них."
    pov "Меня больше всего интересует философия Данте."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at right
    with byso
    ren "И в сём же суть?"
    pov "Любовь как учение.{w} Цель такового - достижение счастья жизни при помощи мужества, благоразумия и честности."
    kt "Мы больше философствуем по своему личному опыту.{w} Вот каково ваше мнение на тему добра и зла?"
    pov "Добро это то что совершается во благо людей, зло что против.{w} Вроде ничего сложного."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    with byso
    "Повариха набрала воду и достала жёлтый бумажный пакет с подписью <<Лимон>>.{w} Константин и Рена ухмыльнулись"
    kt "Как по мне нереалистичное представление."
    hide image re_smile2_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Согласна.{w} Нет такого чтоб добро было всем хорошо, а зло всем плохо.{w} Субъективизм."
    pov "Да ладно, вот что плохого в том чтобы помогать например смертельно больным?"
    hide image re_smile4_pioneer
    show image re_smile_pioneer at right
    with byso
    "Константин откинулся на стуле, а Рена с улыбкой обернулась на повариху."
    ren "Не знаю, всё?"
    hide image pov_normal
    show image pov_sad at left
    with byso
    pov "Как так?"
    "Голос поварихи звучал достаточно раздражённо."
    ren "Смотрите, обрисуем ситуацию.{w} Вы <<помогаете>> смертельно больному ребёнку. У него нет шанса на ремиссию."
    "Рена вывалила обжаренную капусту в кастрюлю и накидала новой."
    hide image re_smile_pioneer
    show image re_sad_pioneer at right
    with byso
    ren "Вы тратите на это свои лично заработанные деньги.{w} Тяжёлый труд. А в итоге для чего?"
    pov "Как для чего? Чтоб продлить его жизнь!"
    hide image re_sad_pioneer
    show image re_serious2_pioneer at right
    with byso
    ren "Как бы не так. {w}Вы просто представьте себе, какие боли он испытывает каждый день своей <<жизни>>."
    "Повариху сразили слова Рены."
    ren "А вы в свою очередь снова даруете ему очередной день адской агонии. {w}Более того, вы отдаёте эти деньги через людей-организаторов и они имеют с этого копейку."
    ren "То есть добро вы делаете только для последних, вредя себе и тому ребёнку."
    kt "Угу, гуманизм - палка о двух концах.{w} Так и получается что чистого добра или чистого зла просто не существует."
    "Повариха стояла и смотрела в окно."
    pov "Да-а.{w}.. Может вы и правы, но это всё равно жестоко."
    hide image re_serious2_pioneer
    show image re_serious_pioneer at right
    with byso
    ren "Жизнь такая штука, что сказать то."
    "Повариха засыпала жёлтый порошок в чан и плотно закрыла его."
    pov "Огоньку нет у вас?"
    kt "А вам зачем?"
    "С ехидной улыбкой спросил Константин."
    pov "Не курите?"
    hide image re_serious_pioneer
    show image re_smile_pioneer at right
    with byso
    ren "Курим, а что?"
    hide image pov_sad
    show image pov_normal at left
    with byso
    pov "Эх вы. {w}Ну ладно, есть у кого-то спички, у меня того."
    kt "Держите."
    "Константин протянул свою зажигалку поварихе, та начала её крутить в руках."
    pov "Странно, никогда не видела таких. {w}Импортная?"
    kt "Ага."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    with byso
    "Рена тихо усмехнулась и ссыпала последние куски капусты в кастрюлю."
    play sound2 sfx_open_window
    play sound light_inh
    "Повариха открыла окна, зажгла сигарету и вернула Константину зажигалку."
    pov "Спасибо большое. Если хотите могу поделиться.{w} Всё равно на два часа проветривать, запаха не будет."
    kt "Не, у нас своё есть."
    "Константин достал пачку честерфилда и протянул одну Рене."
    hide image re_smile2_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Спасибо тебе."
    hide image pov_normal
    show image pov_smile at left
    with byso
    pov "Ну вы даёте, даже сигареты импортные.{w} Вот оно новое поколение."
    play sound light_inh
    "Рена и Константин зажглись и сделали по затяжке."
    kt "Да, есть связи просто."
    hide image pov_smile
    show image pov_normal at left
    with byso
    pov "Я так вижу вы давно знакомы?"
    window hide
    menu:
        "Да, уже несколько лет вместе.":
            $ renpy.block_rollback()
            $ rerp += 1
            pov "Вот оно как.{w} Да, <<Совёнок>> сближает. <<Вместе>> в плане отношений?"
            ren "Ещё нет."
            "С комедийной обидой сказала Рена. Константин усмехнулся."
        "Нет, не так давно познакомились.":
            $ renpy.block_rollback()
            pov "Ну я так вижу вы оба хорошо готовите.{w} Да, <<Совёнок>> сближает."
    "Перекурив, они выкинули окурки и Галина Петровна протянула им по одной мятной конфете."
    pov "Держите, а то вожатая запалит - мало не покажется."
    kt "Спасибо."
    pov "Это вам спасибо, второй раз меня на кухне выручаете."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at right
    with byso
    "Константин съел конфету, Рена кивнула."
    ren "Не за что."
    pov "Вы крутые ребята.{w} Ладно, идите. У вас же ещё дела."
    kt "Давайте, до встречи."
    ren "До свидания."
    play ambience ambience_camp_center_day
    play sound door_cl
    stop music fadeout 3
    hide image pov_normal
    hide image re_smile_pioneer
    scene bg ext_dining_hall_near_day
    show image re_smile_pioneer
    with byso
    "Рена и Константин вышли из столовой."
    kt "Меня это поражает.{w} Может это не та женщина?"
    $ volume(1, "music")
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    play music music_list["your_bright_side"] fadein 2
    ren "А почему нет?"
    "Рена обернулась к Константину и села на перила."
    kt "Ну не могу я уложить то что это она же."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Тату на руке, схожие речевые обороты. Очень-очень вряд-ли."
    ren "Люди меняются, тебе ли не знать."
    "Константин почесал затылок и пожал плечами."
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    ren "Ну ладно, обходы.{w} Идём давай к товарищам глиномесам."
    kt "Лады, пошли."
    hide image re_smile_pioneer
    scene bg ext_clubs_day
    show image re_bored_pioneer
    with fade
    stop music fadeout 3
    play sound_loop bolgarka volume 0.6 fadein 3
    "Ещё с площади было слышно как у кибернетиков шла работа.{w} Один из них работал болгаркой."
    kt "М-м, с таким же звуком мою дверь выпиливали."
    hide image re_bored_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Нашёл с чем сравнить."
    "Сказала она с ехидной улыбкой."
    play sound sfx_knock_door2
    "Константин вежливо постучал. Никто не ответил."
    play sound sfx_open_door_clubs_2
    hide image re_smile2_pioneer with byso
    "Рена зашла в клубы, а Константин за ней."
    stop ambience
    play sound door_cl
    play music music_list["gentle_predator"]
    scene bg robot_constr with byso
    "В клубах была любопытная картина.{w} Шурик и Электроник паяли робота-кошкодевочку, а Рома полировал тазовую деталь."
    ren "Ух ты, не знала что вас на девочек тянет."
    stop sound_loop fadeout 1
    "Шурик проигнорировал колкость и продолжал работу, Электроник снял маску для пайки и гипнотизировал Рену взглядом, а Рома отвлёкся от полировки."
    kt "И кто вам вообще такие детали привёз.{w}.. Секс-игрушку себе конструируют, кошмар какой."
    rm "Не для тебя делали!"
    ren "Тебе напомнить кое-что?"
    "В ответ на слова Рены Рома отвернулся."
    ren "Хватит на меня глазеть, бесишь уже!"
    "Электроник быстро натянул на себя паяльную маску и продолжил работать."
    kt "Когда результат?"
    sh "Не сегодня."
    kt "Конкретнее."
    sh "Через день."
    kt "Добро. Рена, пошли."
    "Рена ещё раз глянула на Рому и вышла за Константином."
    scene bg ext_clubs_day
    show image re_smile_pioneer
    with byso
    stop music fadeout 3
    play sound door_cl
    play ambience ambience_camp_center_day
    kt "Следующая остановка музклуб."
    ren "Идём."
    hide image re_smile_pioneer
    show image re_bored_pioneer at left
    show mt smile pioneer panama at right
    with byso
    play music music_list["my_daily_life"]
    "На пересечении их встретила вожатая."
    mt "А вот и вы. Обход делаете как вижу?"
    kt "Так точно."
    ren "Ольга Дмитриевна, подскажите, а чем вообще каждый клуб должен заниматься?"
    show mt surprise pioneer panama at right with byso
    "Сахарова почесала подбородок и посмотрела в землю."
    mt "Кибернетики робота для сбора ягод делают, Мику чистит и разбирает кладовку весь день.{w}.. Литературный вроде принимает долги по книгам и даёт задания младшим.{w}.. Спортивный тренируется перед финалом по футболу."
    show mt normal pioneer panama at right with byso
    mt "Вроде так должно быть. Вы уже были где-то?"
    kt "У кибернетиков. Они как вы и говорили заняты роботом."
    show mt smile pioneer panama at right with byso
    "Вожатая улыбнулась."
    mt "Замечательно. {w}Сегодня у нашего отряда после ужина свечка на сцене, явка обязательна."
    ren "И что там будет?"
    "Без интереса спросила Рена.{w} Константин тяжело вздохнул."
    mt "Там увидите. {w}Всё, идите. После обхода свободны."
    kt "Принято."
    show mt grin pioneer panama at right with byso
    mt "Всё, идите."
    hide mt
    hide image re_bored_pioneer
    show image re_serious3_pioneer
    with byso
    "Сказала вожатая и ушла."
    kt "А так выпить хотелось..."
    hide image re_serious3_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Да нет, порядок.{w} Выпьем значит выпьем."
    "Константин улыбнулся."
    kt "Вот она - целеустремлённость!"
    stop music fadeout 3
    hide image re_smile4_pioneer
    scene bg musclub
    show image re_bored_pioneer
    with fade
    play sound sfx_knock_door2
    "Рена постучала в дверь музклуба."
    mi "Проходите..."
    hide image re_bored_pioneer
    scene bg int_musclub_day
    show image re_serious3_pioneer at right
    show mi upset pioneer at left
    with byso
    play ambience ambience_music_club_day
    play sound door_cl
    play music music_list["smooth_machine"]
    "В клубе сидела Мику и натягивала струны на гитару."
    kt "Привет.{w} Работаешь?"
    show mi sad pioneer at left with byso
    "Мику грустно отложила гитару и глянула на Константина."
    mi "Ага.{w}.. С утра сижу отлаживаю, даже выйти не могу из-за вчерашнего провала."
    show mi dontlike pioneer at left with byso
    mi "Всё этот криворукий Толик!{w} Пусть он со мной теперь этим занимается."
    hide image re_serious3_pioneer
    show image re_serious2_pioneer at right
    with byso
    ren "Он не в нашем отряде.{w} Мы не знаем где он."
    show mi angry pioneer at left with byso
    "Мику недовольно фыркнула и снова взяла гитару."
    mi "Передайте Ольге Дмитриевне мою искреннюю благодарность за испорченные каникулы."
    play sound struna
    "Озлобленно проговорила Мику и подтянула струну."
    hide image re_serious2_pioneer
    hide mi
    scene bg musclub
    show image re_serious3_pioneer
    with byso
    play ambience ambience_camp_center_day
    play sound door_cl
    stop music fadeout 3
    "Константин и Рена вышли из музклуба."
    kt "М-да, Сахарова и осталась Сахаровой."
    hide image re_serious3_pioneer
    show image re_smile_pioneer
    with byso
    ren "Ты про что?"
    kt "Да я более чем уверен что она с кем-то поспорила что Мику выступит и проспорила."
    kt "Теперь я понимаю почему её подчинённые так её ненавидели."
    hide image re_smile_pioneer
    scene bg ext_square_day
    show us grin sport at right
    show image re_smile_pioneer at left
    with byso
    play music music_list["i_want_to_play"]
    "На площади к ним подбежала Ульянка."
    us "Ну чего, видели робота?"
    hide image re_smile_pioneer
    show image re_smile2_pioneer at left
    with byso
    ren "Ага, что-то с чем-то."
    kt "Я бы хотел видеть лицо вожатой когда она его увидит."
    show us laugh sport at right with byso
    us "А то!{w} Самой интересно увидеть какую взбучку она им задаст."
    hide image re_smile2_pioneer
    show image re_smile4_pioneer at left
    with byso
    ren "Как у тебя в клубе дела?"
    show us smile sport at right with byso
    "Ульянка поправила футболку и широко улыбнулась."
    us "Всё хорошо, я размялась и завтра готова играть."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at left
    with byso
    ren "А остальные чего?"
    show us sad sport at right with byso
    "С лица Ульяны пропала улыбка."
    us "Чего-чего, но играть я буду завтра одна.{w} Худший состав из всех что у меня был."
    kt "Ничего, мы в тебя верим."
    show us surp1 sport at right
    hide image re_smile_pioneer
    show image re_smile2_pioneer at left
    with byso
    "Рене и Ульянке понравились слова Константина."
    us "Ой, спасибки.{w} Окей, мне на треню, не скучайте."
    hide image re_smile2_pioneer
    hide us
    show image re_smile2_pioneer
    with byso
    stop music fadeout 3
    "Сказала она и убежала."
    kt "И вечно она куда-то бежит..."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Да-а, все разные были в детстве, ничего не сказать."
    kt "Ну теперь нам уже не нужно идти к спортклубу. {w}Скажем что там готовятся."
    hide image re_smile_pioneer
    scene bg int_library_day
    show image re_bored_pioneer
    with fade
    play ambience ambience_music_club_day
    play sound door_cl
    "Дойдя до библиотеки, они вошли без стука."
    "Рена заметила как Женя с Леной неумело прятали карты."
    play music cirk fadein 1
    hide image re_bored_pioneer
    show mz normal pioneer glasses at fleft
    show un surprise pioneer at cright
    show image re_smile_pioneer at fright
    with byso
    "Она подошла к Лене и опёрлась на спинку стула."
    ren "Встань на секундочку."
    un "З-зачем?.."
    show mz normal pioneer glasses at fleft
    hide image re_smile_pioneer
    show image re_smile4_pioneer at fright
    with byso
    "Рена ухмыльнулась.{w} Женя уже поняла что Лену заметили с картами."
    ren "Надо. Вставай-вставай."
    hide image re_smile_pioneer
    show mz angry pioneer glasses at fleft
    show un shocked pioneer at cright
    show image re_smile4_pioneer at fright
    with byso
    play sound sfx_paper_bag
    play sound2 monety
    "Лена послушно встала, из юбки посыпались игральные карты. На стуле лежали два советских рубля.{w} Женя прикрыла лицо рукой."
    show mz normal pioneer glasses at fleft with byso
    mz "Товарищи надзиратели, давайте поймём и простим?"
    kt "М-м, хорошо.{w}.. Ни я ни она не Славя, не сдадим, но 2 рубля сдайте вы."
    hide image re_smile4_pioneer
    show mz bukal pioneer glasses at fleft
    show un sad pioneer at cright
    show image re_smile2_pioneer at fright
    with byso
    "Лене стало неудобно.{w} Она подняла с пола две монеты по рублю и дала Рене. Рена же забрала деньги и положила в нагрудный карман."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer at fright
    with byso
    ren "Прекрасно.{w} Приятно с вами работать, до свидания."
    hide image re_smile3_pioneer
    hide mz
    hide un
    scene bg ext_library_day
    show image re_smile_pioneer
    with byso
    stop music fadeout 3
    play sound door_cl
    play ambience ambience_camp_center_day
    "Константин и Рена покинули библиотеку."
    mz "Ну Лена, как так можно, на что бы теперь играть будем?"
    un "Что я то? {w}Откуда мне было знать что они именно сейчас нагрянут, с утра же не пришли."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    play sound sfx_knock_glass
    "Рена постучала в окно, голоса в библиотеке стихли."
    ren "Не заставляйте ещё и карты отбирать."
    hide image re_smile4_pioneer
    show image re_smile2_pioneer
    with byso
    play music music_list["silhouette_in_sunset"] fadein 3
    "Отойдя от библиотеки, Рена дала рубль Константину."
    ren "Твоя доля."
    "Константин начал крутить монету в руке."
    kt "Спасибо. Настоящий советский рубль, ещё и юбилейный.{w} 1967 год чеканки, неплохо. {w}В нашем мире бы за такую дали более 200 тысяч..."
    hide image re_smile2_pioneer
    show image re_sad_pioneer
    with byso
    ren "Знаешь, я давно размышляла.{w} По сути деньги это эквивалент помощи обществу."
    kt "Да, я тоже об этом думал.{w} Сколько вносишь в общество - столько и получаешь в денежном эквиваленте."
    hide image re_sad_pioneer
    show image re_serious2_pioneer
    with byso
    ren "Так тогда почему запрещён подкуп?{w} Ты же по сути за это платишь свою цену, сам много помогал людям, заработал и заплатил на обход законодательства."
    kt "Ух, а тут уже не знаю. Мысль то разумная, но тем не менее не ясно почему она не является ходовой."
    hide image re_serious2_pioneer
    scene bg ext_houses_sunset
    show image re_sad_pioneer
    with byso
    "Постепенно начало вечереть."
    ren "М-да, а мы ведь так и не искупались..."
    "Константин махнул рукой."
    kt "Завтра успеем, нормально."
    hide image re_sad_pioneer
    show image re_smile_pioneer
    with byso
    ren "Тоже верно."
    hide image re_smile_pioneer
    scene bg ext_house_of_mt_sunset
    show image re_smile_pioneer
    with byso
    "Дойдя до домика вожатой они застали её лежащей в гамаке и читающей книгу."
    kt "Воу-воу, она решила встать на путь интеллектуального развития, неожиданно."
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    play sound sfx_punch_medium
    "Рена усмехнулась и коснулась плеча вожатой."
    ren "Ольга Дмитриевна, мы всё."
    hide image re_smile3_pioneer
    show image re_smile2_pioneer at left
    show mt surprise pioneer at right
    with byso
    "Сахарова словно по команде вылезла из гамака и встала по стойке смирно."
    mt "А... Ну хорошо.{w}.. сейчас ужин, так что идите."
    kt "Хорошо, спасибо."
    hide image re_smile2_pioneer
    hide mt
    show image re_smile_pioneer
    with byso
    play sound sfx_dinner_horn_processed
    "Заиграл горн, они ушли к столовой, а Сахарова пошла в домик."
    ren "М-да, о чём мы и говорили. Лишь бы самой ничерта не делать."
    hide image re_smile_pioneer
    scene bg int_dining_hall_people_sunset_cust
    show image re_smile_pioneer at right
    show image pov_normal at left
    with fade
    play ambience ambience_dining_hall_full
    "Дойдя до столовой они подошли к поварихе."
    hide image pov_normal
    show image pov_smile at left
    with byso
    pov "А вот и вы. Ваша еда."
    "Галина Петровна подала им макароны по-флотски с томатной пастой и две большие кружки кваса."
    pov "Это вам особенные блюда, отличающиеся даже от наставнических.{w} Приятного аппетита."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Спасибо огромное."
    hide image pov_smile
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    "Все трое обменялись улыбками и Рена с Константином отправились на своё место."
    kt "Вау, а где Толик?"
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Да-а, даже не поиздеваться.{w}.. Печально."
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    "Сев на место, они с улыбкой посмотрели друг на друга."
    kt "Вновь приятного вам аппетита."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "И вам тоже, коллега!"
    stop music fadeout 3
    "Рена и Константин привстали, киношно пожали друг другу руки и усмехнулись, после чего приступили к еде."
    hide image re_smile2_pioneer
    show image re_smile_pioneer at right
    show image tl_angry at left
    with byso
    play music kringe fadeout 3
    "Во время еды к ним с подносом подошёл Толик."
    kt "А вот и наша звёздочка.{w} Как дела солнце?"
    hide image re_smile_pioneer
    show image re_smile4_pioneer at right
    with byso
    "Рена, которая мирно пила квас чуть в нём не захлебнулась со смеху."
    tl "Уйдите с моего места или я буду жаловаться."
    hide image re_smile4_pioneer
    hide image tl_angry
    show image re_smile4_pioneer at fright
    show image tl_angry
    with byso
    "Константин хмыкнул и встал со стула."
    "Положив ему руку на плечо, он нагнулся и заглянул ему в глаза."
    kt "Правда чтоль?{w} И кому?"
    tl "Славе, она вас проучит!"
    hide image re_smile4_pioneer
    show image re_laugh_pioneer at fright
    with byso
    "Рена больше не могла сдерживать смех и звонко рассмеялась."
    "Константин развернул Толика на 180 градусов."
    kt "Ну тогда побежал кабанчиком."
    hide image tl_angry with vpunch
    play sound sfx_pat_shoulder_hard volume 1.4
    "Сказал он и отвесил Толику пинка.{w} Толик потёр пятую точку после упругого удара и сел на другое место."
    hide image re_laugh_pioneer
    show image re_smile2_pioneer
    with byso
    stop music fadeout 3
    "Сев на место, Константин отпил квасу и глянул на Рену."
    kt "Оцените представление от 1 до 10."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Двадцать."
    "Сказала Рена и начала массировать щёки."
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    "Закончили трапезу они без особых происшествий."
    "Сдав тарелки, Рена и Константин благодарно кивнули поварихе и отправились на выход."
    hide image re_smile_pioneer
    scene bg ext_dining_hall_near_sunset
    show image re_smile_pioneer at right
    with byso
    play ambience ambience_camp_center_evening
    "На выходе их ожидал весь отряд кроме Алисы и кибернетиков."
    play music music_list["heather"]
    tl "Это он меня пнул."
    show image tl_angry at fleft
    show sl surprise pioneer at left
    with byso
    "Пожаловался Славе Толик."
    th "М-да..."
    show sl angry pioneer at left with byso
    sl "Это правда?"
    "Недовольно обратилась к Константину Славя."
    kt "Ты о чём?"
    sl "Вы издеваетесь над Толиком?"
    hide image re_smile_pioneer
    show image re_sad_pioneer at right
    with byso
    ren "Кто такой Толик?"
    show sl surprise pioneer at left with byso
    "Славя на несколько секунд выпала из реальности после такого вопроса и потом указала пальцем на Толика."
    show sl angry pioneer at left with byso
    sl "Это он."
    kt "Не знаю, впервые его вижу."
    show sl surprise pioneer at left
    hide image tl_angry
    with byso
    stop music fadeout 3
    "Толик обижено ушёл.{w} Славя ничего не поняла и смотрела ему в след."
    sl "Ладно, забудьте, видимо он соврал."
    ren "Ясно-понятно."
    hide sl
    show us laugh pioneer at left
    hide image re_sad_pioneer
    show image re_smile_pioneer at right
    with byso
    play music music_list["so_good_to_be_careless"]
    "Славя ушла к Ольге, к ним же подошла Ульянка с улыбкой на всё лицо."
    us "Я же говорила что врёт!"
    hide image re_smile_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Хе-хе, молодчина."
    show us shy2 pioneer at left with byso
    "Сказала Рена и погладила Ульяну по голове."
    show us grin pioneer at left
    hide image re_smile4_pioneer
    show image re_smile2_pioneer at right
    with byso
    us "Чего как в лагере?"
    kt "Да всё обычно.{w} Готовка, обходы, медного Генду ещё не украли и так далее."
    mt "Так, мой отряд, идём на сцену!"
    "Константин заметил появившихся Алису и кибернетиков и пошёл за отрядом вместе с Ульянкой и Реной."
    show us smile pioneer at left with byso
    us "А, точно, вы-ж готовили.{w} Отличное мясо на обед было, спасибо."
    hide image re_smile2_pioneer
    show image re_smile_pioneer at right
    with byso
    ren "Да не за что, ничего особо сложного."
    show us laugh2 pioneer at left with byso
    us "Но всё равно вкусно."
    hide us
    hide image re_smile1_pioneer
    scene bg ext_stage_normal_night
    show us grin pioneer at left
    show image re_smile2_pioneer
    with fade
    play ambience ambience_camp_center_night
    "Солнце зашло. Спустя несколько минут разговоров, они дошли до сцены."
    kt "О, а я тут и не разу не был."
    show us laugh2 pioneer at left with byso
    us "Да ладно! А, так вы же первую смену.{w} У нашего отряда тут каждую смену свечки."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Что будет?"
    show us grin pioneer at left with byso
    "Ульянка ухмыльнулась."
    us "Не скажу.{w} Узнаете."
    show mt normal pioneer far at right with byso
    mt "Пионеры, аккуратно поднимайтесь по лестнице и занимайте удобные места на полу."
    hide mt
    hide us
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    "Константин поднялся и подал руку Рене."
    ren "Спасибо."
    show us calml pioneer
    hide image re_smile4_pioneer
    with byso
    us "Эй, а мне?"
    "Константин усмехнулся и подал руку Ульянке."
    show us smile pioneer with byso
    us "Спасибо."
    hide us with byso
    mt "Ребята, кучнее и в круг."
    stop music fadeout 3
    "Константин сел спиной к кулисам сцены, справа от него села Рена, а справа от Рены Ульянка."
    show mt smile pioneer
    show sl smile pioneer at right
    with byso
    "Вожатая достала спички, зажгла толстую свечу и вставила её в фонарь."
    play music warm_evening
    mt "Друзья, исполняя традицию нашего лагеря, сегодня у нас свечка.{w} Каждый может оставить своё слово для остальных."
    hide mt
    hide sl
    show mt grin pioneer at left
    show sl smile2 pioneer
    show mz bukal pioneer glasses at right
    with byso
    "Вожатая передала свечку Славе."
    sl "Говорить может только тот у кого в руках свечка.{w} Остальные могут только тихо похлопать под конец выступления."
    sl "Итак, я начну.{w} Я очень рада что нахожусь тут с вами уже какую смену. Каждый раз я снова и снова влюбляюсь в это место."
    sl "Я рада что нахожусь в нашем прекрасном и дружном отряде..."
    th "Бла-бла-бла.{w}.. Балобольства больше чем сути."
    hide mt
    hide sl
    hide mz
    show sl smile pioneer at left
    show mz angry pioneer glasses
    show un normal pioneer at right
    with byso
    "Как только Славя закончила свою нудную речь, похлопала только вожатая. Свеча перешла к Жене."
    mz "Ну чего мне сказать собственно, я рада быть в этом отряде и бла-бла-бла... Возвращайте книги вовремя."
    hide un
    hide sl
    hide mz
    show mz bukal pioneer glasses at left
    show un shy pioneer
    show sh normal pioneer at right
    with byso
    "Женя передала свечку Лене."
    un "С-спасибо за хорошую смену."
    hide un
    hide mz
    hide sh
    show un shy pioneer at left
    show sh normal_smile pioneer
    show image rm_th at right
    with byso
    "Лена передала свечу Шурику."
    sh "Спасибо. {w}Хочу сказать спасибо своему клубу за удачную работу.{w} Скоро мы представим свою новую разработку и я обещаю, вы все будете приятно удивлены."
    show sh upset pioneer with byso
    sh "Приходите в клуб кибернетики мы ждём всех. {w}Почти.{w} Всех."
    hide un
    hide sh
    hide image rm_th
    show sh upset pioneer at left
    show image rm_th
    show el normal pioneer at right
    with byso
    "Сказал он и передал фонарь Роме."
    hide image rm_th
    show image rm_no
    with byso
    "Рома посмотрел на Рену, которая пилила его взглядом, недвусмысленно намекая что если он ляпнет чего не того, то она его четвертует."
    rm "Мой коллега по цеху сказал всё верно. Приходите."
    hide el
    hide sh
    hide image rm_no
    show image rm_no at left
    show el smile pioneer
    show mi upset pioneer at right
    with byso
    "Рома передал фонарь Электронику."
    el "Хочу поправить моего коллегу, мы ждём всех!"
    hide image rm_no
    show image rm_an at left
    show el surprise pioneer
    with byso
    play sound sfx_punch_medium
    "Рома ткнул Электронику в бок локтём."
    el "В нашем клубе всегда много интересного, так что записывайтесь."
    hide el
    hide image rm_an
    hide mi
    show el sad pioneer at left
    show mi dontlike pioneer
    show dv guilty pioneer at right
    with byso
    "Рена даже не слушала Электроника, тот это заметил и грустно передал свечу Мику."
    mi "Спасибо всем за смену и за доп.работу в музклубе."
    hide el
    hide dv
    hide mi
    show mi angry pioneer at left
    show dv sad pioneer
    show us normal pioneer at right
    with byso
    "Мику передала свечу Алисе."
    hide mi
    hide dv
    hide us
    show dv sad pioneer at left
    show us grin pioneer
    show image re_smile_pioneer at right
    with byso
    "Алиса без каких-либо слов передала свечу Ульянке."
    us "О, наконец я! Я рада быть в этом отряде."
    show dv guilty pioneer at left
    show us laugh pioneer
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    with byso
    "Она глянула на Рену.{w} Алиса грустно посмотрела в сторону."
    us "Тут мои новые друзья и я буду рада приехать на ещё одну смену."
    show us smile pioneer with byso
    us "Завтра у моей команды матч, чтоб были все!"
    hide dv
    hide us
    hide image re_smile2_pioneer
    show us grin pioneer at left
    show image re_smile3_pioneer
    with byso
    "С ухмылкой сказала Ульянка и передала свечку Рене."
    ren "Что-ж.{w}.. Я совершенно не думала что приеду под конец смены, но тем не менее я рада тут находиться."
    hide image re_smile3_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Рада была общаться, может после смены свидимся, а с некоторыми обязательно встретимся."
    show us smile pioneer at left with byso
    "Сказала Рена, глянув направо и налево."
    ren "Спасибо за внимание."
    "Рена передала свечу Константину."
    kt "Хм... Что-ж сказать."
    window hide
    menu:
        "Думаю, все уже всё сказали, мне сказать нечего.":
            $ renpy.block_rollback()
            kt "Всем спасибо за внимание."
        "Эта смена стала лучшей для меня.":
            $ renpy.block_rollback()
            kt "На этой смене было много веселья, я рад что приехал сюда и получил хороший опыт благодаря некоторым людям."
            kt "Возможно я приеду сюда ещё раз. Спасибо за внимание."
        "Очень раз знакомствам, полученным тут.":
            $ renpy.block_rollback()
            $ rerp += 1
            kt "На этой смене я смог встретить старую знакомую с которой давно не виделся и я безусловно рад этой встрече."
            kt "Хочу сказать ей огромное спасибо."
        "Спасибо за интересную смену.":
            $ renpy.block_rollback()
            kt "И за внимание тоже."
    "Константин вернул свечу вожатой."
    hide us
    hide image re_smile2_pioneer
    show mt grin pioneer
    with byso
    mt "Чтож, на этом наша прекрасная свечка заканчивается."
    stop music fadeout 5
    "Вожатая задула свечку в фонаре."
    show mt smile pioneer with byso
    mt "А теперь все по домикам. Всем спокойной ночи."
    hide mt with byso
    "Отряд стал расходиться."
    show image re_smile_pioneer at right
    show us grin pioneer at left
    with byso
    play music proshloe fadein 5
    us "Ну ладно, у меня завтра важный день, я побегу."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    with byso
    ren "Беги, спокойной ночи."
    kt "Доброй ночи."
    show us smile pioneer at left with byso
    us "Споки!"
    hide us 
    hide image re_smile2_pioneer
    scene bg ext_houses_night
    show image re_smile_pioneer
    with byso
    "Ульяна убежала.{w} Рена и Константин пошли в домик."
    kt "Ну вот теперь можно и выпить."
    hide image re_smile_pioneer
    show image re_sad_pioneer
    with byso
    ren "А у нас есть стаканы?"
    "Константин почесал затылок."
    kt "В душе не чаю. Скорее нет чем да."
    kt "Да пофиг, с горла попьём."
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена хмыкнула и взяла Константина под руку."
    ren "Вот он - креативный подход к решению проблемы."
    hide image re_smile4_pioneer
    scene bg int_house_of_kt_night
    show image re_sad_pioneer
    with byso
    play sound door_cl
    stop ambience
    play sound2 door_cl
    play sound sfx_lock_close
    "Дойдя до домика, они решили включить свет."
    ren "Света сегодня нет."
    kt "М-м, с кайфом. Ну ладно, луна нам светило."
    #Блять, Константин же не забрал ебучий рюкзак а-а-а-а, дайте навалить философии!!! 10.02.2023 21:43
    "Рена села на стул, а Константин вспомнил что рюкзак с портвейном остался у вожатой."
    kt "Ёкарный бабай, рюкзак у вожатой..."
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Ну чего сказать, беги."
    hide image re_smile4_pioneer
    scene bg ext_houses_night
    with byso
    play sound door_cl
    play ambience ambience_camp_center_night
    "Константин выбежал из домика и полетел к домику вожатой."
    "Ночная улица была пустынна и чиста. Ни души, лишь ветер, который развевал волосы Константина."
    scene bg ext_house_of_mt_night with byso
    play sound sfx_knock_door2
    "В домике вожатой горел свет, Константин постучал."
    mt "Войдите."
    scene bg int_house_of_mt_night with byso
    play sound door_cl
    stop ambience 
    "Отдышавшись, Константин вошёл."
    show mt surprise pioneer with byso
    "На стуле сидела вожатая и что-то писала. В комнате слегка попахивало куревом."
    mt "Что такое, что ты хотел?"
    "Нервно спросила вожатая."
    kt "Я рюкзак забрать."
    "Константин повесил рюкзак на плечи и пошёл к выходу."
    mt "Ладно, спокойной ночи."
    kt "Доброй."
    play ambience ambience_camp_center_night
    scene bg ext_houses_night 
    show image na_gu at right
    with fade
    "Бежав обратно, он обратил внимание что по дороге шла знакомая ему девочка. Немного затормозив он глянул на неё."
    play sound dissapearance
    hide image na_gu with flash
    "Поймав на себе взгляд Константина, девочка пропала."
    kt "А, ага."
    "Константин перевёл дыхание и побежал дальше."
    scene bg int_house_of_kt_night
    show image re_madsmile2_pioneer
    with fade
    play sound door_cl
    stop music fadeout 3
    stop ambience
    "В домике его ждала Рена, которая крутила в руке зажигалку Константина."
    hide image re_madsmile2_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Ты быстро. Бежал?"
    "Константин достал из рюкзака блок сигарет."
    kt "А, фух. Да, бежал."
    "Тяжело дыша ответил Константин."
    hide image re_smile4_pioneer
    show image re_surprise_pioneer
    with byso
    ren "Что такое?"
    kt "Да Сахарова там с куревом баловалась. Я подумал что с моим."
    hide image re_surprise_pioneer
    show image re_smile_pioneer
    with byso
    play music BlueJetta fadein 3
    play sound sfx_blow_out_candle
    "Константин поставил на стол бутылку портвейна."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Я тут нашла стаканы."
    play sound sfx_open_cabinet_1
    "Рена достала из шкафчика два стакана."
    kt "Откуда?"
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    ren "В тумбочке стояли.{w} Скучно было пока ты бегал."
    "Константин открыл бутылу портвейна и поровну разлил."
    kt "Ну что, за вечер?"
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "За вечер."
    "Они чокнулись и понемногу отпили."
    hide image re_smile_pioneer
    show image re_sad_pioneer
    with byso
    ren "М-да, та ещё гадость..."
    kt "Не нравится - не пей, сам выпью."
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    "С ехидной улыбкой ответил Константин. Рена игриво улыбнулась."
    ren "Теперь выпью из принципа."
    "Рена мигом опустошила стакан."
    kt "Куда-а? Запьянеешь же."
    hide image re_smile4_pioneer
    show image re_smile3_pioneer
    with byso
    ren "А не это ли цель?"
    kt "Ну тоже верно."
    ren "Никогда не могла понять людей которые свой алкоголизм оправдывали вкусом алкоголя.{w} Так и скажи, пью как тварь, но не хочу показаться быдлом."
    "Константин глянул в окно."
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    kt "Да люди-люди.{w} Жаль что человек не может без других людей."
    hide image re_smile_pioneer
    show image re_sad_pioneer
    with byso
    ren "Да... Человек не может полноценно жить, когда вокруг нет других людей."
    ren "Ни один человек не может выжить в одиночестве, несмотря на то, что ты уникален сам по себе."
    ren "Поэтому твоя жизнь и была так тяжела, пуста и печальна."
    ren "Как бы то не скрывалось, каждый хочет любви, физического и духовного присутствия окружающих."
    hide image re_sad_pioneer
    show image re_serious3_pioneer
    with byso
    "Рена посмотрела в окно."
    ren "Но как ты понимаешь у людей теперь нет времени друг для друга.{w} Они тратят время на утешение собственного эго и функцию умножения."
    kt "Да, перенаселение, деградация человеческой души.{w}.. Такими темпами складывается ощущение что бог либо бессилен в изменении человеческого мира, либо не обращает внимание на его королевство."
    "Константин разлил портвейн по стаканам."
    kt "Или его просто нет."
    kt "Будем?"
    hide image re_serious3_pioneer
    show image re_sad_pioneer
    with byso
    ren "Будем."
    kt "Тогда выпьем за беспомощность бога в нашем мире."
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Выпьем."
    "Они снова чокнулись начали опустошать уже второй стакан."
    kt "И всё-таки не перестану повторять.{w} Хорошо что мы тут."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Ух, согласна.{w} После одиночества, которое рухнуло словно кирпич на голову, любая отдушина будет кстати."
    #О да-а-а-а-а, обожаю цитировать рандомную аниму! 10.02.2023 22:13
    kt "Ага... Когда живёшь такой жизнью, тоска пропитывает всё: обои на кухне, монитор компьютера, письма на рабочей почте..."
    hide image re_smile_pioneer
    show image re_sad_pioneer
    with byso
    ren "Всё вспоминается фраза, мол если больной не очень хочет жить, врачи бессильны."
    ren "Бредни да и только.{w} Суицидников откачивают только в путь."
    kt "Как ты думаешь, есть ли в этом смысл? Я думаю нет."
    "Рена залпом допила портвейн из своего стакана."
    hide image re_sad_pioneer
    show image re_serious2_pioneer
    with byso
    ren "Согласна. Если человек живёт в агонии, какой смысл заставлять его испытывать страдания дальше.{w} Безусловно есть участь хуже смерти."
    hide image re_serious2_pioneer
    show image re_serious3_pioneer
    with byso
    ren "Хотя нет, смысл то есть, как я и говорила - потешить своё эго."
    ren "Какая я спасительница, заставила человека страдать куда дольше чем он должен был.{w} Если человек решился, значит он наконец признал то что мир больше не изменится."
    ren "Ну по крайней мере на его веку."
    kt "Далеко не все способны понять что жизнь без цели равно медленная смерть.{w} Миллионы людей живут лишь потому что боятся смерти, но по сути они умирают каждый день когда просыпаются."
    kt "Тут уж говорю по собственному опыту."
    "Константин опустошил свой стакан и разлил последние капли портвейна по стаканам."
    kt "За что?"
    hide image re_serious3_pioneer
    show image re_smile3_pioneer
    with byso
    ren "За нас с тобой."
    "Ответила Рена немного невнятным голосов. Снова стук стаканов."
    hide image re_smile3_pioneer
    show image re_smile2_pioneer
    with byso
    kt "Если уж мы про странные утверждения, то могу впомнить чрезмерное желание некоторых людей оставить после себя след."
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена усмехнулась и откинулась на спинку стула."
    ren "Ха, да только все будут одинаковы в гробу."
    kt "Точно-точно.{w} Все мы надеемся на красивый конец и славу.{w} Слава в свою очередь - главное стремление людей нашего времени."
    kt "Людей уже настолько много что желание показаться хоть немного отличным от других стало почти потребностью."
    hide image re_smile4_pioneer
    show image re_serious3_pioneer
    with byso
    "Рена недовольно посмотрела на полу-пустой стакан."
    ren "Да ладно тебе. Живём в эпохе потреблядства.{w} Иногда такое ощущение что человеческий закат уже близко."
    hide image re_serious3_pioneer
    show image re_smile4_pioneer at center:
        zoom 1
        linear 0.5 zoom 1.5 yanchor 0.1
    play sound glad
    "Рена допила свой портвейн и села на ноги Константина, приобняв его и погладив его по спине."
    kt "Что ты там об меня вытираешь?"
    hide image re_smile4_pioneer
    show image re_smile3_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Рена усмехнулась."
    ren "Свою веру в человечество."
    ren "Я просто хотела ещё раз сказать что у нас новая жизнь, а новую жизнь следует начинать с теми, кто тебе действительно дорог."
    ren "Вот я и с тобой, любимый."
    hide image re_smile3_pioneer
    show image re_smile4_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Рена поцеловала Константина в шею и, обняв ещё крепче, заглянула ему в глаза."
    ren "Что ты думаешь?"
    window hide
    menu:
        "Думаю что ты права.":
            $ renpy.block_rollback()
            $ rerp += 1
            hide image re_smile4_pioneer
            show image re_smile3_pioneer at center:
                zoom 1.5
                yanchor 0.1
            with byso
            ren "Я херни не скажу."
            hide image re_smile3_pioneer
            show image re_smile4_pioneer at center:
                zoom 1.5
                yanchor 0.1
            with byso
            "Константин поцеловал сидевшую на нём Рену."
            kt "Не скажешь.{w} Давай уже на боковую, завтра новый день."
        "Не знаю, ничего, странное утверждение.":
            $ renpy.block_rollback()
            hide image re_smile4_pioneer
            show image re_angry2_pioneer at center:
                zoom 1.5
                yanchor 0.1
            with byso
            "Рена немного обиделась."
            ren "Ну и ладно, ничего, но суть я надеюсь ты уловил."
            hide image re_angry2_pioneer
            show image re_smile4_pioneer at center:
                zoom 1.5
                yanchor 0.1
            with byso
            "Рена поцеловала Константина."
            kt "Давай уже на боковую, завтра новый день."
        "Чего-т тебя по пьяни далеко повело.":
            $ renpy.block_rollback()
            hide image re_smile4_pioneer
            show image re_sad_pioneer at center:
                zoom 1.5
                yanchor 0.1
            with byso
            ren "Да не то что бы далеко, скорее сильно близко."
            ren "Все 2 дня об этом думаю. Без перерыва."
            hide image re_sad_pioneer
            show image re_smile4_pioneer at center:
                zoom 1.5
                yanchor 0.1
            with byso
            "Рена поцеловала Константина."
            ren "Потому что свою жизнь я хочу прожить с тобой."
            kt "Твой выбор.{w} Давай уже на боковую, завтра новый день."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    ren "Да, ты прав, давай."
    hide image re_smile_pioneer with byso
    "Константин быстро разделся, лёг в кровать и начал настраивать будильник на телефончике.{w} Рена потихоньку снимала с себя лишнюю одежду."
    kt "4 дня, 1 час, 27 минут и 41 секунда."
    ren "Чего ты?"
    "Рена легла в плотную к Константину и взяла у него телефон."
    kt "Мы так и не знаем что это за таймер. Даже примерно."
    ren "А не без разницы?"
    kt "Ну да, верно.{w} Спокойной ночи."
    ren "Споки ноки."
    stop music fadeout 2
    show blink
    "Константин закрыл глаза."
    scene bg cafe
    show unblink
    play music music_list["torture"] fadein 2
    "Очнулся он на стуле в уже знакомом зале."
    gg "Здравствуй.{w} Рад меня видеть?"
    kt "Ну привет.{w} Не то что бы."
    show image so_gd with byso
    "Генда поправил очки и через спину глянул на Константина."
    gg "Тебе знакомо понятие стабильность?"
    kt "Да, эмоциональная.{w} То чего тебе не хватает."
    hide image so_gd
    show image so_sm
    with byso
    "Создатель усмехнулся."
    gg "Шутки шутишь? Это хорошо.{w} А теперь слушай меня."
    "Создатель подошёл к стулу на котором сидел Константин."
    gg "С твоим появлением кое-кто попортил мне стабильность инреальности.{w} Не хочешь мне ничего рассказать?"
    kt "Нет."
    hide image so_sm
    show image so_gd
    with byso
    gg "Хм-м, ладно, допустим, но если ты это знаешь, то тебе мало не покажется."
    "Грозно проговорил создатель."
    hide image so_gd
    show image so_sm
    with byso
    "Его выражение лица быстро сменилось на улыбку и он отошёл от Константина."
    gg "Сегодня у нас блекджек.{w} Играешь на фишки.{w} Если до 3й игры у тебя вылетят все фишки то ты не проснёшься."
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
    gg "Это Семён, знакомься.{w} Он наш дилер."
    "Семён лишь молча занял положение у стола."
    me "Вот фишки."
    play sound kosti
    "Он достал из стола 2 фишки и дал их Константину."
    kt "А ты чё без фишек?"
    gg "На твою-ж жизнь играем а не на мою.{w} А он, так уж и быть, умрёт если ты выиграешь."
    me "Тасую колоду."
    play sound card_mix
    "Семён быстро размешал карты и раздал по две каждому. Свои он выложил на стол рубашкой вниз. Валет пики и дама черви."
    "Константин украдкой глянул на карты.{w} У него был бубновый король и четвёрка черви."
    gg "Я возьму одну."
    play sound card_take
    "Семён выдал карту Генде."
    gg "Стоп."
    play sound card_take
    me "Беру карту."
    "Король треф."
    me "На столе перебор."
    kt "Ещё."
    "Генда непрерывно смотрел на Константина.{w} Константин подобрал пятёрку треф."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            play sound card_take
            "Константин получил{w} двойку пик и выложил карты на стол."
            kt "Двадцать одно."
            hide image so_gd
            show image so_sm at cright
            with byso
            "Генда удивлённо посмотрел на Константина, но потом улыбнулся."
            gg "Хм-м, молодец. Мы в пролёте."
        "Стоп.":
            $ renpy.block_rollback()
            $ gameoverr += 1
            me "Игроки, вскрывайтесь."
            hide image so_gd
            show image so_sm at cright
            with byso
            "У Генды была пара десяток. Он улыбнулся."
            gg "Первый кон - первый пролёт.{w} Ну, в следующей жизни повезёт."
            play sound dissapearance
            "Жетон со стола Константина пропал."
    play sound card_mix
    "Семён снова перетасовал колоду."
    "На столе лежала тройка треф и валет буби."
    me "Беру карту."
    play sound card_take
    "На стол попала шестёрка черви."
    me "Всё. Генда?"
    hide image so_sm
    show image so_gd at cright
    with byso
    gg "Я при своих."
    "Сказал он и насмешливо посмотрел на Константина.{w} У него был король и семёрка черви."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            play sound card_take
            "Валет черви.{w} Пролёт."
        "Стоп.":
            $ renpy.block_rollback()
            me "Игроки, вскрывайтесь."
            "У Генды был туз и девятка.{w} Он обошёл Константина."
if gameoverr ==1:
    jump Poker_Death
else:
    jump fycruif6ir7fc6r7f6y7ivtryyvi
label Poker_Death:
    $ renpy.block_rollback()
    hide image so_gd
    show image so_sm at cright
    with byso
    gg "Что-ж, вот как оно закончится.{w} Быстро."
    "Константин начал чувствовать что его тело начинало повышать свою температуру."
    gg "Рад был общаться, прощай."
    kt "Чт...{w} НЕТ!"
    play sound flame_up
    scene bg black with fl_fire
    "Константина охватило пламя и сожгло его до тла."
    "Повествование n-ой души завершено."
    window hide dissolve
    scene bg black with byso
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    $ unlock_ach_root_inreal(1)
    play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
    scene bg ending_burnout_cg:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    show ending_burnout:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    with Dissolve(15)
    scene bg black with byso
    pause 1
    stop sound
    jump after_ending_screen
label fycruif6ir7fc6r7f6y7ivtryyvi:
    hide image so_gd
    show image so_sm at cright
    with byso
    gg "Мало что от тебя зависело, но всё-таки одну фишку ты проиграл."
    play sound card_mix
    me "Тасую колоду."
    hide image me_no
    show image me_su at left
    with byso
    play sound card_take
    "Семён размешал карты и раздал по две. Его руки дрожали.{w} На столе 17."
    hide image so_sm
    show image so_gd at cright
    with byso
    play sound card_take
    me "Б-беру карту."
    "Король треф."
    hide image me_su
    show image me_st at left
    with byso
    me "На столе п-п...{w} Н-нет...{w} Я не хочу!"
    play sound flame_up
    hide image me_st
    hide image so_gd
    show image so_gd at cright
    with flash
    "Семён самовоспламенился, начал в огне кричать и кататься по полу пока не утратил такую способность."
    gg "Если сейчас проиграешь, то тебя ждёт та же участь."
    "Константин, пытаясь не подавать волнения посмотрел в карты. 10 и дама черви."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            play sound card_take
            "Константин вытащил{w} туз черви и выложил карты на стол."
            kt "Двадцать одно."
            hide image so_gd
            show image so_sm
            with byso
            "Генда снова удивлённо посмотрел на Константина, но потом рассмеялся."
            gg "Молодец, отстоял право на жизнь, теперь в кошмар."
            stop music fadeout 3
        "Стоп.":
            $ renpy.block_rollback()
            gg "А я возьму одну."
            "Генда взял карту, рассмеялся и выложил на стол даму буби, короля пики и туза черви."
            jump Poker_Death
    show blink
    pause 1
    hide image so_sm
    scene bg int_house_of_kt_night
    show unblink
    play music nightmare
    "Глаза Константина закрылись и он очнулся в своём домике."
    "На столе записка о том что они увидятся в старом корпусе."
    scene bg ext_houses_night with byso
    play sound door_cl
    "Константин без задней мысли достал подаренную Реной катану и побежал на место встречи."
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
    scene bg ext_houses_night with byso
    "Константин воспользовался отвлечённостью монстра и побежал на место встречи."
    scene bg int_old_building_night
    show image poter_n at left
    show image re_dontlike_casual at right
    with byso
    play music god fadein 2
    "Зайдя в комнату, он встретил Рену и Пионера, которые чем-то были обеспокоены."
    hide image re_dontlike_casual
    show image re_smile_casual at right
    with byso
    pp "Привет. Ты долго."
    ren "Мы заждались уже твоего возвращения."
    play sound sfx_wood_floor_squeak
    "Константин сел на пол."
    kt "Ну как бы то попроще, меня чуть Генда не сжёг заживо."
    hide image re_smile_casual
    show image re_holod_casual at right
    with byso
    ren "Что?!"
    "По глазам Рены было видно её желание разорвать Генду на части."
    kt "Карты, где ставкой является жизнь."
    pp "Ну ты тут, это хорошо. Как ты узнал что именно сожжение?"
    "Константин начал искать по карманам сигареты.{w} Пионер протянул ему и Рене по сигарете и зажёг их всем."
    kt "Благодарю. Он сжёг Семёна до тла. Семён вылетел пока был дилером."
    hide image re_holod_casual
    show image re_dontlike_casual at right
    with byso
    ren "М-да...{w} Такие дела."
    kt "Чего у нас на повестке дня?{w} Точнее ночи."
    pp "Нравится мне твоё хладнокровие. Тебя чуть не убили, а ты сразу к делу."
    hide image re_dontlike_casual
    show image re_smile_casual at right
    with byso
    ren "Да уж, на меня становишься похожим."
    "Мило улыбнувшись сказала Рена."
    pp "Генда зачем-то начал проверять все системы.{w} Зачем? Не знаю.{w} Он давно так не делал."
    kt "Он сказал что проблемы со стабильностью в инреальности."
    pp "Бред.{w=1} Не может быть.{w=1} Снова?"
    hide image re_smile_casual
    show image re_bored_casual at right
    with byso
    ren "Ты о чём?"
    pp "Я похоже кое-что понял, но мне нужно найти тому подтверждение."
    ren "И что же?"
    pp "Не забивай голову, потом скажу."
    kt "Что-то ещё?"
    pp "Создатель что-то мутит. {w}Мне кажется он начал понимать что мы тут строим заговоры."
    pp "Если он найдёт тому доказательство, то начнётся война.{w} Шансы победить у нас в районе 10-20 процентов."
    pp "Ещё я узнал о том что существует некая симуляция куда каждый раз приходит лично. {w}Она является закрытой, невидимой и только он может туда попасть, аутентификация по ДНК, не прохожу."
    kt "Может это и есть та самая симуляция где у него <<дела>>?"
    hide image re_bored_casual
    show image re_dontlike_casual at right
    with byso
    ren "Да я думаю не может а точно."
    pp "Только что там неизвестно. {w}Пункт управления симуляциями? Что-то вроде хоста инреальности? {w}Мир исправленных?{w=1} В душе не чаю, может всё и сразу."
    kt "А что такое инреальность?"
    pp "Система, содержащая в себе все миры.{w} Рухнет она - рухнет и всё остальное."
    hide image re_dontlike_casual
    show image re_bored_casual at right
    with byso
    ren "Корневая папка если проще?"
    pp "Да. На этом пока что всё. {w}Чувствую вскоре что-то изменится в инреальности."
    kt "С чего ты взял?"
    pp "Чуйка редко меня подводит."
    "Пионер выкинул бычок."
    pp "Извините за малое количество новостей.{w} Я просто разузнавал откуда в первый день ты видел труп.{w=1} Результата нет."
    pp "Вы обратно?"
    ren "Я да."
    kt "Я тоже."
    pp "Хорошо, до завтра и удачи."
    hide image re_bored_casual
    hide image poter_n
    show image poter_n
    with byso
    stop music fadeout 1
    play ambience ambience_old_camp_outside
    "Рена превратилась в пыль, а Константин остался с пионером."
    kt "Что такое?"
    pp "Я тут хотел тебе сказать..."
    kt "Что?"
    "Пионер глянул в окно."
    pp "Ты же знаешь как Рена попала к тебе?"
    kt "Да, вроде убила пару человек..."
    hide image poter_n
    show image poter_s
    with byso
    "Пионер рассмеялся."
    pp "Значит смотри...{w} 21 человек порублены в фарш. {w}Отравлено 8 человек.{w} Утоплено 3е.{w} Одного сожгла заживо.{w} Нескольких задушила. А 3х вообще подорвала."
    pp "И это за время твоего первого дня, если не брать болванок!"
    "Пока Константин укладывал информацию в голове Пионер коснулся его лба."
    pp "Посмотри сам."
    play music godrita fadein 10
    stop ambience
    scene bg black
    hide image poter_s
    show shum_white
    with flash
    "Экран загорелся."
    scene bg ext_beach_night
    show shum_white
    with flash
    me "Чего ты тут делаешь?"
    ren "Ой, а я тебя искала."
    "Рена подошла на расстояние вытянутой руки."
    ren "Семён? Какого года?"
    me "В каком смысле?"
    ren "Я тут задаю вопросы!"
    "Ударив с ноги в колено, Рена выбила Семёну коленную чашечку.{w} Нога с хрустом согнулась в обратном направлении и он упал на песок."
    me "Сука-а! Что я тебе сделал?!"
    ren "Счастье нужно завоевать.{w} Я своё завоюю!{w} Твой труп будет лишь каплей в океане крови."
    "Рена достала свой топор и повторила вопрос."
    ren "Какого года? Быстро отвечай!"
    me "Я не знаю!"
    "Хмыкнув, она располовинила голову Семёна."
    scene bg ext_square_sunset
    show shum_white
    with flash
    me "Славь, я хотел тебе кое-что сказать..."
    sl "Да-да?"
    me "Ты мне очень сильно..."
    "Слова Семёна сменились на крик ужаса.{w} Рена шилом продырявила шею Славе, отчего вторая, задыхаясь и истекая кровью упала наземь."
    ren "Чё ты орёшь, свинья?! С тобой так же будет!"
    "В ужасе Семён начал убегать."
    ren "Что-то трупы разбегались... К дождю, наверное."
    "Догнав Семёна, она вонзила топор в его плечо и потянула на себя, чем повалила на спину."
    ren "Хоть подохни с честью!"
    "Сильным ударом сапога Рена раздавила Семёну череп, после чего тот лопнул как арбуз."
    scene bg int_house_of_mt_night2
    show shum_white
    with flash
    "Семён лежал на кровати с Ольгой и курил после бурного секса."
    mt "Дай тоже закурю."
    "Как только вожатая взяла сигарету, в домик вошла Рена и сверлила взглядом Семёна."
    mt "Почему без стука?!"
    me "Ты чё тут забыла?"
    ren "Не я забыла, а ты забыл, лови."
    "Рена кинула в кровать старую гранату Ф-1 и крутя чеку на пальце, вышла из домика."
    ren "Чеку потом отдам."
    "Раздался оглушающий взрыв.{w} Вожатую и Семёна размазало по стенам."
    scene bg ext_boathouse_night
    show shum_white
    with flash
    "Семён проснулся на пирсе."
    me "Что я тут..."
    ren "Она танцует под дождём, она рисует чёрной краской..."
    "Рена завязывала узел на стальной гире."
    ren "О, проснулась свинья..."
    me "Как ты меня назвала?!"
    "В ответ Рена ударила Семёна в лицо с ноги."
    ren "Значит так, сейчас либо ты рассказываешь всё что знаешь, либо идёшь купаться с гирей."
    me "Чё я знаю, ничерта я не знаю и знать не могу!"
    "Рена не стала долго терпеть и столкнула гирю в воду."
    ren "Дом в котором мы живём, жизнь похожую на сказку..."
    "Семён упал за ней и не смог всплыть."
    scene bg int_dining_hall_people_sunset_cust
    show shum_white
    with flash
    ren "Приятного аппетита.{w} Расскажи что знаешь о мирах."
    me "Спасибо. А тебе зачем?"
    "Рена поправила берет, раскручивая в руке столовый ножик."
    ren "Ну ты упомянул - мне стало любопытно."
    me "Как я понял между ними можно перемещаться в случае парадокса.{w} У тебя на выбор будет переход в 3 других мира по годам."
    ren "То есть направленно не получится переместиться?"
    me "Надо знать имя и дату попадания главного элемента симуляции. От этого есть формула."
    ren "У тебя есть такая?"
    "Он усмехнулся."
    me "Уж чего не знаю - того не знаю... Не делал ещё так.{w} Это так написано только в 4ом писании."
    "Семён глотнул компота."
    ren "Где это писание?"
    me "В библиотеке, можешь как нибудь глянуть."
    ren "Спасибо за информацию.{w} Слушай, тут так получается, ты мне больше не нужен."
    "Рена встала со стула, а Семён начал задыхаться."
    me "Тв-арь..."
    ren "Не тварь а цианид."
    scene bg int_old_building_night
    show image poter_n
    with flash
    stop music fadeout 2
    "Константин вернулся к пионеру."
    play music nightmare
    pp "Честно говоря такой кровожадности не видел ни у одного путника.{w} Тут бывали и насильники и убийцы.{w=1} Был случай, когда одна путница выкосила только около 14 симуляций, но она быстро прекратила свою деятельность."
    pp "Даже они не выкашивали людей как на скотобойне.{w} Даже они находили покой, но не она.{w} Я представить боюсь что бы произошло если ей бы пришлось побыть в тех мирах ещё день-другой."
    pp "Ошибки инреальности произошли из-за неё. Около 30 симуляций в день. Несколько дней без вмешательства Генды и вся инреальность превратилась бы в мясорубку."
    pp "Инреальность наделила её сознание и тело построенным тобой образом. Сила, которая превосходит среднюю человеческую в раза 3-4, она сможет вынести даже самые тяжёлые физические повреждения."
    pp "Такой физической подготовке позавидуют даже солдаты, которые всю жизнь провели в тренировках."
    pp "Чрезмерная агрессия к тем кто против тебя или пытается отобрать тебя."
    pp "Вспыльчивость, ненависть и кровожадность, но с другой стороны заботливость и верность. Понимая то что её характер твоя заслуга я не могу сказать точно кого из вас называть ментально больным."
    pp "Единственный к кому она испытывает эмпатию, так это к тебе.{w} Может быть до поры до времени..."
    pp "Она одному черепушку раздавила сапогом, сам видел!{w=1} Для того, чтобы так сделать, нужен удар силой 2300 ньютонов!{w=1} Это удар боксёра тяжеловеса!"
    pp "Я конечно доверяю твоему выбору, но ты будь аккуратнее..."
    show blink
    "Глаза Константина сомкнулись."
    scene bg black with dissolve
    window hide
    jump d4_withre