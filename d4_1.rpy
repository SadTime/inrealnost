label d4_withre:
    scene bg black with dissolve
    window hide
    python:
        bgcg = random.randint(1,2)
    if bgcg == 2:
        scene bg bgcg7
        show load
        with byso
        pause 10
        $ bgcg -= 2
        scene bg black with dissolve
        stop music fadeout 2
        window show
        jump bindgjfpbnipsgdjogbnmfvipsbnfibigfpsbipdg
    else:
        scene bg bgcg8
        show load
        with byso
        pause 10
        $ bgcg -= 1
        scene bg black with dissolve
        stop music fadeout 2
        window show
        jump bindgjfpbnipsgdjogbnmfvipsbnfibigfpsbipdg
label bindgjfpbnipsgdjogbnmfvipsbnfibigfpsbipdg:
    $ save_name = ('Инреальность.\nДень четвёртый.')
    $ day_time ()
    play music music_list["drown"]
    scene bg int_house_of_kt_day
    play ambience ambience_int_cabin_day fadein 1
    show unblink
    play sound sfx_bed_squeak1
    "Константин проснулся.{w=1} Как и прошлым утром голова раскалывалась."
    show image re_serious3_pioneer with byso
    play music Aleph fadein 3
    "Рена была уже одета и сидела на кровати напротив, рассматривая ключик что Константин забрал из автобуса."
    ren "Мне кажется пионер тебя немного задержал?..."
    kt "Сколько времени?"
    ren "7:18.{w=1} 18 минут эквивалентно 3м в кошмаре.{w} Так расскажи, о чём вы там беседовали?"
    window hide
    menu:
        "Пионер рассказал мне подробности. Я расстроен.":
            $ renpy.block_rollback()
            hide image re_serious3_pioneer
            show image re_mad_pioneer
            with byso
            ren "Ты мне не доверяешь?"
            play sound sfx_click_2
            "Укоризненно проговорила Рена, отложив ключ на стол."
            kt "Ну как сказать, ты более 30 человек убила нахаляву."
            hide image re_mad_pioneer
            show image re_angry2_pioneer
            with byso
            "Рене явно не понравились слова Константина."
            ren "Что значит нахаляву?!{w=1} То есть ты хочешь сказать что я зря сюда вообще попала?"
            ren "Если ты думаешь что у меня был выбор, то нет, у меня его не было!"
            ren "Это не люди, это скот!{w=1} Даже свиньи будут разумнее и человечнее большинства из них."
            ren "Тебе ли этого не знать?!"
            ren "Лучше бы я осталась гнить с самым первым Семёном, да?!"
            "Константин понял что Рена начинает достигать точки кипения, потому просто встал с кровати и обнял её."
        "Расскажи во всех подробностях как ты попала сюда.":
            $ renpy.block_rollback()
            $ rerp += 1
            hide image re_serious3_pioneer
            show image re_sad3_pioneer
            with byso
            ren "А, понятно.{w=1}.. Он узнал про мои приключения до тебя."
            play sound sfx_click_2
            "Рена немного успокоилась, положив ключик на стол."
            ren "Я убила в общей сложности 70-80 человек до того как нашла тебя."
            ren "Постоянные скачки во времени и пространстве начинали выматывать, потому я сама того не понимания делала это с нарастающей жестокостью"
            "Константин внимательно слушал Рену, она же засмотрелась в пол."
            ren "Мне не было никакого смысла существовать в одиночестве.{w} Я прилагала все усилия к тому чтоб всё закончилось так."
            ren "Я хотела чтоб этот бесконечный кошмар закончился.{w} Вне зависимости от результата и потраченных средств."
            ren "Может ты и ждёшь от меня раскаяния за всё мною содеянное, но нет. Для меня эти жертвы оправданы."
            ren "Знал бы ты, что эти <<люди>> из себя представляли."
            ren "Знаешь, как ты и писал однажды в своём стихотворении.{w=1}.. Человеческого в них нет ничерта."
            ren "Это про них. Я надеюсь ты понимаешь меня..."
            "Константин просто встал с кровати и обнял её."
    hide image re_mad_pioneer
    hide image re_sad3_pioneer
    show image re_shy_pioneer at center:
        zoom 1.5
        yanchor 0.1
    with byso
    kt "Всё хорошо. Я тебе верю. Забудь."
    "Рена обняла Константина в ответ."
    ren "А с пионером я потом пообщаюсь.{w} Интересно почему он меня так недолюбливает."
    hide image re_shy_pioneer
    show image re_shy_pioneer
    with byso
    "Константин отпустил Рену и начал одеваться."
    kt "Пионер просто показал мне некоторые моменты где ты убивала Семёнов, комментируя твои действия как нечто ненормальное.."
    hide image re_shy_pioneer
    show image re_serious2_pioneer
    with byso
    "Рена начала раздражаться."
    kt "Ты узнавала о 4ом писании.{w=1} О чём там речь?"
    ren "Брехня.{w} Тот хрен меня обманул, это папка с чистыми листами бумаги."
    ren "Валяется где-то в подвале библиотеки.{w=1} Можем найти если тебе любопытно."
    kt "Да, думаю что хотелось бы.{w=1} Как говорил пионер, эта симуляция одна из оригинальных, может что-то поменялось."
    hide image re_serious2_pioneer
    show image re_smile3_pioneer
    with byso
    "Рена усмехнулась."
    ren "То что твоя симуляция оригинальна это очевидно."
    ren "Как бы то сказать...{w=1} Насколько я то выяснила, 4ое писание достаточно ценно.{w} Всё-таки да, надо прибрать к рукам."
    ren "Плюс я тут думала, от чего эти ключи."
    hide image re_smile3_pioneer
    show image re_bored_pioneer
    with byso
    "Рена указала на связку ключей и затем на ключ из автобуса."
    kt "Не знаю. Может от чего-то у кибернетиков?"
    hide image re_bored_pioneer
    show image re_smile_pioneer
    with byso
    "Она потянулась и глянула в окно."
    ren "Вряд-ли.{w=1} У них нет закрытых сейфов. Потом узнаем."
    stop music fadeout 3
    kt "Окей, тогда пойдём покурим?"
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Пошли."
    "С немного напряжённой улыбкой ответила Рена, поправив причёску."
    scene bg ext_polyana_day
    show image re_smile4_pioneer
    with fade
    play ambience ambience_forest_day fadein 1
    play sound light_inh
    play music deadrazy2 fadein 3
    "Присев на лесную почву, Константин дал Рене сигаретку и прикурил."
    "Она села, прикурила и засмотрелась в чистое небо."
    hide image re_smile4_pioneer
    show image re_bored_pioneer
    with byso
    ren "Слушай, а посмотри стабильность.{w} Всё равно пока курим."
    "Константин молча достал телефон и выполнил уже привычный ряд действий."
    play sound sfx_radio_squelch_1
    gt "Происходит замер. {w=1}Пожалуйста ожидайте."
    kt "Ожидаем."
    stop music
    play sound pum
    play music the_date_of_death fadein 1
    hide image re_bored_pioneer
    show image re_sad3_pioneer
    with byso
    gt "Стабильность составляет 65 процентов.{w} Вероятность ошибок менее 1 процента."
    kt "Чего?"
    "У Константина отвисла челюсть.{w=1} Рена уныло перевела взгляд на телефон."
    ren "Хреново.{w}.. Это значит что мы можем ждать незванных гостей."
    kt "В каком смысле?"
    hide image re_bored_pioneer
    show image re_sad3_pioneer
    with byso
    ren "Да в прямом.{w} Мир уязвим для кошмара."
    kt "Я надеюсь никому не приспичит сейчас заходить к нам.{w=1} Было бы неприятно."
    hide image re_sad3_pioneer
    show image re_happy_pioneer
    with byso
    "Рена с тёплой улыбкой выкинула окурок и встав погладила Константина по голове."
    ren "Не бойся, я буду с тобой до самого конца."
    kt "Верю..."
    "Выдохнул Константин и выкинул бычок."
    stop music fadeout 3
    hide image re_happy_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Ладно, идём к Сахаровой.{w=1} Уже почти 8."
    kt "Да я думаю уже надо идти в столовую.{w=1} Там её и встретим."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Тоже верно."
    scene bg ext_square_day
    show image re_smile2_pioneer at right
    show mt smile pioneer panama at left
    with fade
    play music music_list["lightness_radio_bus"] fadein 3
    "Выйдя на площадь, они встретили Ольгу Дмитриевну."
    show mt grin pioneer panama at left with byso
    mt "Доброе утро, пионеры.{w} Всё в порядке?"
    hide image re_smile2_pioneer
    show image re_smile_pioneer at right
    with byso
    ren "Доброе.{w=1} Да, всё нормально."
    "Константин кивнул в подтверждение слов Рены."
    show mt smile pioneer panama at left with byso
    mt "Прекрасно.{w=1} Сегодня у нас футбольный матч, потому Рена будет на нём судьёй.{w=1} Константину же другое задание. Сегодня в библиотеку завозят новые книги.{w=1} Задача помочь разгрузить."
    hide image re_smile_pioneer
    show image re_bored_pioneer at right
    with byso
    "Рене не понравились то, что работа будет проходить отдельно от Константина, но она поняла что не может этого поменять."
    mt "Обе работы после обеда.{w=1} До обеда вам нужно будет осмотреть клубы."
    show mt grin pioneer panama at left with byso
    mt "Работа понятна?"
    kt "Да, всё поняли."
    ren "Угу."
    play sound sfx_dinner_horn_processed
    show mt smile pioneer panama at left with byso
    "Вожатая улыбнулась.{w=1} Заиграл горн."
    mt "Тогда хорошо, увидимся на обеде."
    hide mt
    hide image re_bored_pioneer
    show image re_bored_pioneer
    with byso
    stop music fadeout 3
    "Вожатая ушла. Константин глянул на Рену."
    kt "Присядем?"
    hide image re_bored_pioneer
    show image re_sad2_pioneer
    with byso
    ren "Хорошо."
    play music sab fadein 3
    "Покорно сказала Рена и села на скамейку."
    "Константин сел рядом и смотрел на Рену."
    kt "Что такое, на тебе словно нет лица."
    hide image re_sad2_pioneer
    show image re_bored_pioneer
    with byso
    ren "Он нашел меня."
    kt "Кто <<он>>? {w}Генда?"
    hide image re_bored_pioneer
    show image re_sad3_pioneer
    with byso
    ren "Да.{w=1} Он пришел ко мне во сне."
    "Она коснулась лба Константина."
    stop ambience
    play sound in_vosp
    play music nightmare
    scene bg ext_square_night_blood
    show image so_sm
    show shum_red
    with flash
    gg "Не думала что я тебя найду?"
    "Она встала с пола и оглянулась."
    ren "Что?...{w=1} Где я?"
    hide shum_red
    hide image so_sm
    show image so_gd
    show shum_red
    with byso
    gg "Одна из симуляций, которую ты погубила."
    "Генда поправил очки и сурово взглянул на Рену."
    gg "Но это не так важно.{w=1} Как ты сюда попала?"
    gg "Я не переносил тебя в этот мир."
    ren "Не твоё дело, ублюдок."
    play sound sfx_armature_swish volume 0.6
    "Генда хотел было ударить Рену, но та увернулась."
    hide shum_red
    hide image so_gd
    show image so_sm
    show shum_red
    with byso
    gg "Хорошая рекация.{w=1} Кем ты была до инреальности?"
    gg "Так эффектно нарезать моих подчинённых и подчиняемых, просто удивительно..."
    gg "Но почему ты не убила Константина?"
    ren "Я не твоя кукла чтоб отвечать на твои вопросы!"
    play sound par
    "Генда усмехнулся и сел на образовавшийся стул."
    gg "А-а, так ты кукла Константина...{w=1} Но я не видел тебя в его жизни."
    ren "Тебя это не должно волновать!"
    gg "Ладно, не хочешь по-хорошему, будем по-плохому."
    "Генда встал со стула и снял очки."
    gg "Я поговорю с Константином.{w=1} Ты нарушитель, а нарушителей я караю по всей строгости."
    stop music
    hide shum_red
    scene bg ext_square_day
    show image re_sad3_pioneer
    with flash
    play sound out_vosp
    play ambience ambience_camp_entrance_day fadein 1
    play music sab fadein 3
    "Рена сидела и перебирала складки на юбке."
    ren "Я нарушитель, а нарушителей он карает..."
    ren "Это всё что он сказал. {w}Именно поэтому я попросила проверить тебя стабильность."
    ren "Видимо потому стабильность и начала падать."
    "Константин глянул в небо."
    kt "М-да...{w=1} Это плохо..."
    play sound sfx_pat_shoulder_hard volume 0.5
    hide image re_sad3_pioneer
    show image re_shy_pioneer
    with byso
    "Константин взял Рену за руки."
    window hide
    menu:
        "Надо придумать план.":
            $ renpy.block_rollback()
            hide image re_shy_pioneer
            show image re_sad3_pioneer
            with byso
            ren "И что ты предлагаешь?"
        "Мы пройдём это вместе.":
            $ renpy.block_rollback()
            $ rerp += 1
            hide image re_shy_pioneer
            show image re_smile4_pioneer
            with byso
            "Рена заглянула в глаза Константину."
            ren "Мне приятно осознавать что ты меня поддержишь."
            "Она поцеловала Константина."
            hide image re_smile4_pioneer
            show image re_sad3_pioneer
            with byso
            ren "Надо всё равно придумать план. Идеи?"
    kt "Я предлагаю сегодня после лагерных дел разведать старый корпус."
    play sound sfx_keys_rattle
    "Константин отпустил руки Рены и достал связку ключей из кармана."
    kt "У нас целая куча ключей.{w=1} Я не думаю что все из них от внешнего лагеря.{w} Надо осмотреть это заброшенное здание."
    kt "Взять ключи, фонарик и пойти исследовать."
    kt "Главное не начинать суматоху.{w=1} От этого стабильность может упасть ещё сильнее."
    play sound par
    show image poter_n at right
    with byso
    "Материализовался пионер."
    pp "Правда. Генда будет убавлять проценты каждый день. Да, так что симуляция рухнет нахер."
    hide image re_sad3_pioneer
    show image re_mad_pioneer
    with byso
    ren "Ты..."
    pp "С тобой мы потом поговорим."
    pp "Вы можете смело идти в старый корпус."
    pp "Прогнозами завтра у вас последний день нормальной жизни и то если повезёт."
    pp "У Генды явно проблемы с контролем симуляций, но он понимает что всё едет к чертям."
    pp "Короче, у вас осталось в лучшем случае 2 дня.{w=1} Как и сказал Константин, ведите себя как и раньше, так будет лучше."
    pp "Мне надо бежать.{w=1} Потом объясню."
    hide image poter_n with byso
    play sound par
    stop music fadeout 3
    "Пионер быстро растворился."
    hide image re_mad_pioneer
    show image re_bored_pioneer
    with byso
    ren "Дела-дела.{w=1}.. Надо быстро закончить лагерную работу."
    kt "Мы можем не проводить полный обход.{w} Спортклуб точно будет занят, библиотека далеко.{w=1} Зайдём к кибернетикам и в музыкальный."
    kt "После пойдём за снаряжением."
    hide image re_bored_pioneer
    show image re_serious3_pioneer
    with byso
    "Рена кивнула."
    ren "Ладно, я поняла.{w=1} Пойдём поедим."
    ren "Видимо скоро будет что-то великое."
    "Рена и Константин направились к столовой."
    scene bg ext_dining_hall_near_day
    show image re_bored_pioneer
    with byso
    "В то время когда все уже выходили из столовой, Рена с Константином до неё только дошли."
    scene bg int_dining_hall_people_day
    show image re_bored_pioneer
    with byso
    play ambience ambience_dining_hall_full fadein 1
    "Встав на раздачу, они получили по порции овсяных хлопьев с кусочками чернослива, залитые молоком."
    kt "Спасибо."
    pov "Не за что."
    hide image re_bored_pioneer
    show image re_smile_pioneer
    with byso
    "Рена с улыбкой кивнула.{w=1} Повариха улыбнулась в ответ."
    play music music_list["lightness_radio_bus"] fadein 3
    hide image re_smile_pioneer
    show image re_mad_pioneer
    show image tl_normal at right
    with byso
    "На месте их ожидал Толик."
    th "М-да."
    play sound sfx_punch_washstand
    play sound2 sfx_chair_fall
    hide image tl_normal
    show image tl_angry at fright
    with vpunch
    "Рена без церемоний поставила на столик еду и пнула стул Толика."
    "Результатом Толик лежал на полу с тарелкой каши на его рубашке."
    show image re_serious_pioneer
    hide image re_mad_pioneer
    with byso
    ren "Тупость не порок, но если ты сейчас не уйдёшь, то я из тебя всю дурь выбью."
    hide image tl_angry
    show sl angry pioneer at left
    with byso
    "Толик молча встал и ушел.{w=1} Прибежала недовольная Славя."
    sl "Что это за бесчинство со стороны наставников!{w=1} Тебе не стыдно?"
    play sound dvizh
    "Константин сел напротив Рены, которая молча подняла стул и поменяла его на стул с соседнего столика."
    "Сев на него, она заглянула в глаза Славе."
    hide image re_serious_pioneer
    show image re_mad_pioneer
    with byso
    ren "Нет, а должно?"
    show sl surprise pioneer at left with byso
    "Славю сильно обескуражил этот вопрос."
    sl "Как это?!{w=1} Он такой же человек как и ты, ты должна его уважать!"
    show image re_serious_pioneer
    hide image re_mad_pioneer
    with byso
    ren "Это свинья. Чистой воды. Не фиксирую никаких признаков человечности."
    kt "Твой альтруизм это прекрасно, но лично мне плевать.{w} Рене как видишь тоже."
    kt "Он не слушает наставников уже какой день, за что и получает наказание. Вполне справедливо."
    show sl angry pioneer at left with byso
    sl "Но ему же больно..."
    hide image re_serious_pioneer
    show image re_mad_pioneer
    with byso
    ren "А его никто не спрашивал.{w} Уйди и не порти аппетит."
    show sl surprise pioneer at left with byso
    hide sl
    with byso
    "Славя, не найдя что сказать, ушла."
    kt "Приятного аппетита."
    hide image re_mad_pioneer
    show image re_smile_pioneer
    with byso
    ren "Спасибо, тебе тоже."
    "Они начали есть поданные блюда."
    kt "Мне кажется мы сейчас немного загнули."
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    ren "В каком смысле?"
    kt "Славя то очевидно пошла жаловаться."
    us "А вот и нет!"
    hide image re_smile3_pioneer
    show image re_smile2_pioneer at right
    show us grin pioneer at left
    with byso
    "Из неоткуда появилась Ульяна.{w} Рена непроизвольно улыбнулась."
    us "Я скажу что было не так, а она недоглядела.{w=1} Приятного вам кстати."
    hide image re_smile2_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Привет.{w=1} Спасибо."
    kt "Спасибо."
    show us laugh pioneer at left with byso
    us "Ты у нас сегодня вроде как судья. Этот оболтус в противоположной команде, всё правильно делаешь."
    hide image re_smile4_pioneer
    show image re_smile2_pioneer at right
    with byso
    "С ухмылкой сказала Ульяна.{w=1} Рена усмехнулась."
    ren "Да-а, кажется сегодня они проиграют..."
    kt "Где принимаются ставки?"
    show us smile pioneer at left with byso
    us "А вот давайте если моя команда победит, то я прославляюсь по 2 конфеты.{w=1} Если проиграет, то отдам все что есть."
    kt "Идёт!"
    show us laugh2 pioneer at left with byso
    us "Класс, я побегу тогда разминаться.{w=1} Вам там тоже удачи!"
    hide image re_smile2_pioneer
    show image re_smile2_pioneer
    hide us
    with byso
    "Пожелала Ульяна и убежала из столовой."
    kt "Теперь я понимаю почему она тебе так нравится."
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Ага, хорошо поднимает настроение."
    "Закончив с едой они пошли сдали тарелки."
    scene bg ext_dining_hall_near_day
    show image re_smile_pioneer 
    with byso
    play ambience ambience_ext_road_day fadein 1
    stop music fadeout 3
    "Выйдя из столовой они пошли в сторону музклуба."
    kt "Слушай, а зачем нам в музыкалку?{w=1} Пойдём сразу к кибернетикам.{w=1} У них можно раздобыть что-то для нашего похода.{w=1} Они вроде как были в столовой."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Хорошая идея, ускорим шаг."
    scene bg ext_clubs_day
    show image re_smile4_pioneer
    with fade
    play music Gallow fadein 3
    "Уже в пару мгновений они были у кибернетиков."
    scene bg int_clubs_male_day
    show image re_bored_pioneer
    with byso
    play sound sfx_open_door_clubs
    play ambience ambience_clubs_inside_day fadein 1
    "Зайдя в клуб они начали шерудить по клубу в поисках чего-то полезного."
    th "Хлама тут целые кучи."
    kt "Давай разделимся.{w=1} Погляди в кладовке."
    ren "Поняла."
    hide image re_bored_pioneer with byso
    "Рена направилась в кладовку."
    "Константин нашёл дозиметр."
    th "И нахрена им это?{w=1} Ладно, смотрим дальше."
    play sound sfx_open_cabinet_1
    th "Вот это уже ближе."
    "Константин нашёл компас и упрятал его в карман."
    scene bg int_clubs_male_day with fade
    show image re_smile2_pioneer with byso
    "Спустя 5 минут Рена вышла из кладовки и махнула Константину рукой на выход."
    kt "У меня только компас, у тебя?"
    ren "Пошли в домик."
    "Константин пожал плечами и начал уходить с места кражи."
    scene bg ext_clubs_day
    show image re_smile_pioneer
    with byso
    play sound door_cl
    play ambience ambience_ext_road_day fadein 1
    "Выйдя из клубов они отправились окольными путями в домик.{w} Было видно что у Рены за пазухой было спрятано много всего."
    kt "Чего ты так много набрала?"
    hide image re_smile_pioneer
    show image re_serious3_pioneer
    with byso
    ren "Сейчас всё покажу, подожди."
    scene bg int_house_of_kt_day
    show image re_smile2_pioneer
    with fade
    play sound door_cl
    play ambience ambience_int_cabin_day fadein 1
    play sound2 sfx_blow_out_candle
    "Зайдя в домик, Константин положил на стол компас, а Рена начала выкладывать свои ворованные богатства."
    ren "Значит.{w=1} Ещё набор ключей.{w=1} Батарейки, 4 штуки.{w=1} Два фальшфейера.{w=1} Перекись водорода, 200 мл. {w=1}Обезболивающие, одна банка.{w=1} Цианистый натрий, 2 таблетки."
    hide image re_smile_pioneer
    show image re_serious_pioneer
    with byso
    ren "К вопросу о яблоках, таблетки было 3."
    kt "М-да...{w=1} И кто нас убить хотел?.."
    play sound sfx_unzip_sleepbag
    "Константин вспомнил что в его рюкзаке были перевязочные материалы и, достав их, поставив на стол."
    "Пока Константин разбирал награбленное, Рена начала сравнивать ключи."
    th "Да-а, старая автомобильная аптечка."
    stop ambience
    play sound in_vosp
    scene bg semen_room
    show shum_white
    with flash
    moth "Мы рады что ты наконец сдал на права!{w=1} У нас с отцом тебе подарок!"
    th "Вау, неужели это машина?!"
    "Отец вытащил из шкафа автомобильную аптечку и знак аварийной остановки."
    moth "Вот, теперь когда-нибудь ты купишь себе машину и это будет для тебя жизненно необходимым инвентарём."
    fath "Так точно!{w=1} Возможно эта аптечка когда-нибудь спасёт тебе жизнь."
    th "Да, точно, как я мог забыть..."
    play sound out_vosp
    play ambience ambience_int_cabin_day fadein 1
    hide shum_white
    scene bg int_house_of_kt_day
    show image re_smile_pioneer
    with flash
    ren "На моё удивление дубликатов не так много.{w} Все уникальные на этом кольце.{w=1} Остальные я откладываю."
    "Константин, положив аптечку обратно в рюкзак глянул на ключи."
    kt "Да... {w=1}Я думаю что это точно от чего-то кроме лагерных помещений."
    kt "У меня тут бинт.{w=1} Я сейчас укомплектуюсь, ты отсортируешь ключи и вернёмся в лагерь. {w=1}Лучше не засиживаться, Сахарова начнет беситься."
    hide image re_smile_pioneer
    show image re_bored_pioneer
    with byso
    ren "Да, это понятно..."
    ren "Мне вот интересно, не мог ли пионер дать на меня наводку Генде?"
    kt "Пионер вроде не санкционирован создателем.{w=1} Вряд-ли."
    hide image re_bored_pioneer
    show image re_serious3_pioneer
    with byso
    ren "Да я не про это, может он и не специально..."
    hide image re_serious3_pioneer
    show image re_angry_pioneer
    with byso
    ren "Хотя, если он хотел испортить моё отношение к нему - он испортил."
    play sound sfx_close_cabinet
    "Константин сложил самое необходимое в рюкзак и поставил его в шкаф."
    kt "Тебе помочь с ключами?"
    hide image re_angry_pioneer
    show image re_bored_pioneer
    with byso
    ren "Да, убери дубли в тумбочку пожалуйста."
    play sound sfx_open_table
    "Константин убрал горстку из ключей в тумбочку.{w=1} Рена нацепила последние на кольцо."
    hide image re_bored_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Готово. Можем идти."
    scene bg ext_house_of_sl_day
    show image re_smile_pioneer
    with byso
    play ambience ambience_ext_road_day fadein 1
    play sound sfx_close_door_1
    "Константин и Рена вышли из домика."
    kt "Куда идём?"
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Походим кругами до обеда.{w} У меня нет желания ходить по клубам."
    kt "Верю.{w=1} Аналогично."
    play sound sfx_key_drawer
    pause 0.75
    stop sound
    stop music fadeout 3
    "Закрыв дверь на ключ, Константин пошёл за Реной."
    scene bg ext_houses_day
    show image re_sad3_pioneer
    with byso
    ren "Не знаю как тебе, но мне почему то некомфортно."
    kt "Хах, верю.{w=1} Генда не самый лицеприятный человек."
    hide image re_sad3_pioneer
    show image re_bored_pioneer
    with byso
    ren "Мне вот интересно, знает ли он природу моего происхождения?"
    kt "Понятия не имею, да и я тебе уже говорил по этому поводу.{w} Ты человек и иное представление меня не волнует."
    hide image re_bored_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена искренне улыбнулась."
    ren "Да это то я помню.{w=1} Просто любопытно."
    hide image re_smile4_pioneer
    show image re_bored_pioneer
    with byso
    ren "Я вот думаю. {w=1}Всё таки зайти к кибернетикам придется.{w=1} Снять с себя подозрения за воровство."
    kt "Логично. Идём."
    scene bg ext_clubs_day
    show image re_bored_pioneer
    with byso
    play sound sfx_knock_door7_polite
    "Они дошли до клуба кибернетиков и постучали в дверь."
    sh "Войдите."
    scene bg int_clubs_male_day
    show image re_bored_pioneer at left
    show image rkis_normal
    show sh normal pioneer at fright
    show el normal pioneer at cright
    with byso
    play music god fadein 3
    play ambience ambience_clubs_inside_day fadein 1
    play sound sfx_open_door_clubs_2
    "Константин и Рена вошли в клуб.{w=1} Ромы не было на месте, а Шурик с Электроником стояли возле уже готового робота."
    "Робот представлял из себя цельнометаллическую кошкодевочку с красными светодиодами вместо глаз."
    kt "Я так вижу вы уже закончили."
    show sh serious pioneer with byso
    sh "Угу, представим сегодня после ужина."
    "Кошкодевочка стояла у стола и собирала детский пазл, на котором был изображён волк из <<Ну погоди>>."
    hide image re_bored_pioneer
    show image re_serious2_pioneer at left
    with byso
    ren "Какой функционал?"
    show el smile pioneer with byso
    el "Весьма скудный.{w=1} Сбор ягод, решение базовых логических задач и самооборона."
    kt "Самооборона?"
    show sh upset pioneer with byso
    "Шурик принуждённо кивнул."
    sh "По просьбе Ромы."
    show el surprise pioneer
    hide image re_serious2_pioneer
    show image re_smile3_pioneer at left
    with byso
    "Рена искренне рассмеялась."
    ren "Ха, боюсь это ему не поможет!"
    play sound sfx_open_door_clubs
    hide image re_smile3_pioneer with byso
    "Усмехнулась Рена и вышла из клубов.{w=1} Константин последовал её примеру."
    scene bg ext_clubs_day
    show image re_smile_pioneer at left
    show mt normal pioneer panama at right
    with byso
    play sound door_cl
    play ambience ambience_ext_road_day fadein 1
    "На выходе Константин и Рена встретили вожатую."
    show mt smile pioneer panama at right with byso
    mt "Ну как, все заняты, никто не отлынивает?"
    kt "Нет, эти вроде работают. {w=1}Порядок."
    hide image re_smile_pioneer
    show image re_smile3_pioneer at left
    with byso
    ren "Остальные вроде тоже чем-то да занимаются."
    show mt grin pioneer panama at right with byso
    mt "Хорошо.{w} Скоро обед, а там другие дела, помните?"
    kt "Да-да..."
    play sound sfx_open_door_clubs_2
    hide mt
    hide image re_smile3_pioneer
    show image re_smile2_pioneer
    with byso
    stop music fadeout 3
    "Вожатая улыбнулась и вошла к кибернетикам."
    ren "Пошли на озеро?"
    kt "Какое озеро?"
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена поправила волосы и указала в сторону."
    ren "Тут есть озеро недалеко отсюда.{w} Не думаю что ты там был, но почему бы и не сходить до обеда."
    ren "К тому же там мало ходит и можно ещё поговорить на насущные темы."
    "С явным намёком на вечерние <<диалоги Платона>> сказала она."
    kt "Тогда веди."
    scene bg ext_path2_day
    show image re_smile2_pioneer
    with byso
    "Выйдя на тропу, Константин достал сигаретку и засунул за ухо."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "А мне?"
    "С ехидной улыбкой возмутилась Рена.{w=1} Константин усмехнулся и протянул ей другую сигарету."
    scene bg ext_lake_day
    show image re_smile4_pioneer
    with byso
    play sound light_inh
    play music deadrazy2 fadein 3
    "Выйдя к озеру, они сели на поваленное бревно и закурили."
    kt "А ты была права.{w=1} Действительно красиво."
    stop ambience
    play sound in_vosp
    scene bg ext_lake_day
    show shum_white
    with flash
    "После длительной прогулки, Костя с дедушкой дошёл до озера."
    "Озеро было торфяным, потому вода очень плохо просвечивалась."
    de "Можешь искупаться, я пока пройдусь поищу грибы."
    ks "Конечно!"
    play sound out_vosp
    play ambience ambience_forest_day fadein 1
    hide shum_white
    scene bg ext_lake_day
    show image re_smile_pioneer
    with flash
    kt "Очень похоже на то что было у дачи."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена затянулась и положила голову на плечо Константина."
    ren "Представляю, но по сравнению с городским пейзажем явно лучше."
    "Константин глянул на водную гладь."
    kt "А ты встречала как-нибудь тот самый парадокс?"
    hide image re_smile4_pioneer
    show image re_bored_pioneer
    with byso
    ren "Не-а, нет.{w} Я уходила раньше."
    kt "А как тогда в первый раз сбежала?"
    "Она засмотрелась на тлеющую сигарету."
    hide image re_bored_pioneer
    show image re_serious3_pioneer
    with byso
    ren "Просто открылись два портала на площади.{w=1} Ограниченные по времени судя по всему."
    ren "Насколько я поняла, именно после того как все закроются и начнётся тот самый парадокс."
    ren "Минут 15-30.{w=1} В этом диапазоне."
    hide image re_serious3_pioneer
    show image re_smile4_pioneer
    with byso
    "Засмотревшись на озеро, она взяла Константина за руку."
    ren "Скучаешь ли ты по жизни до инреальности?"
    "Константин затянулся и тяжело выдохнул."
    kt "Странный вопрос.{w=1} Нет конечно, чего уж там размышлять."
    hide image re_smile4_pioneer
    show image re_smile2_pioneer
    with byso
    ren "А я хотела бы туда вернуться.{w} Начать новую жизнь и наконец получить то, что я так давно хотела."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    "Погладив руку Константина, Рена заглянула ему в глаза."
    ren "Счастье."
    kt "Счастье в том мире достаточно абстрактная величина. {w=1}Сама человеческая память так построена."
    kt "Воспоминание о счастливых моментах — это всего лишь приятное воспоминание и не больше, но воспоминание о моменте печали — это уже не память, это чистая и настоящая боль."
    hide image re_smile_pioneer
    show image re_sad3_pioneer
    with byso
    "Рена сделала последнюю затяжку и затушила сигарету о бревно."
    ren "Не спорю, но что мешает изменить этот порядок вещей?"
    "Константин указал на себя."
    kt "Люди.{w} Мы все варимся в одном большом чане с дерьмом.{w} И нет избавления среди тех людей, которые были бы рады ещё глубже тебя в этом дерьме утопить."
    hide image re_sad3_pioneer
    show image re_sad_pioneer
    with byso
    ren "Да уж, люди — самые отвратительные из существ, достигших эволюционного пика."
    kt "А что, у тебя есть другие примеры разумных существ?"
    play sound sfx_pat_shoulder_hard volume 0.5
    hide image re_sad_pioneer
    show image re_smile2_pioneer
    with byso
    "Едко подшутил Константин, Рена ткнула его в бок локтем."
    ren "Вот гад, такую красивую фразу испоганил."
    ren "Но всё-таки, мы тоже люди."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Иногда я бываю счастлива или расстроена, испытываю злость, гнев, раздражение, разочарование и отвращение.{w} Побочный эффект моего естества, как и твоего."
    kt "Только я первого не испытываю."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Но гипотетически ты можешь."
    kt "Логично."
    "Константин потёр глаза."
    kt "Как думаешь у нас есть шанс сбежать?"
    hide image re_smile4_pioneer
    show image re_sad_pioneer
    with byso
    ren "Сомневаюсь.{w} Если Генда будет жив, то он может этого не допустить."
    ren "Вряд-ли ему нужна ещё пачка убитых Семёнов."
    kt "Точно, 4е писание.{w} Я буду сегодня в библиотеке и возьму.{w=1} Напомни как оно выглядит."
    hide image re_sad_pioneer
    show image re_serious3_pioneer
    with byso
    ren "Белая папка с красной пометкой <<#4>>.{w=1} Внутри лежат белые листы бумаги."
    ren "Думаю не ошибёшься."
    kt "Угу, не думаю что там много папок."
    play sound sfx_dinner_horn_processed volume 0.4
    "Спустя некоторое время заиграл горн."
    hide image re_serious3_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Идём на обед.{w} По дороге обсудим как встретиться."
    kt "Ну смотри. Тебе на матч уйдёт в районе часа."
    "Прикинул Константин, вставая с бревна. Рена глянула на озеро и пошла в сторону столовой за Константином."
    kt "Я не могу знать сколько я буду таскать книги, потому как освободишься - иди на площадь.{w=1} Если меня там не будет, то иди к библиотеке."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Хорошо, договорились.{w=1} Так и сделаем."
    scene bg ext_dining_hall_near_day
    show image re_bored_pioneer
    show mz normal pioneer glasses at right
    with byso
    stop music fadeout 3
    "У входа в столовую их ожидала Женя."
    show mz bukal pioneer glasses at right with byso
    mz "Костя, книги выгрузили у входа в лагерь.{w} Там стоит две телеги, их и надо до меня довезти."
    kt "Ясно, без проблем."
    show mz normal pioneer glasses at right with byso
    mz "Жду в библиотеке."
    kt "Угу."
    scene bg int_dining_hall_people_day
    show image re_smile_pioneer
    with byso
    play ambience ambience_dining_hall_full fadein 1
    play music Waijdan fadein 3
    "Войдя в столовую их встретила уникальная картина.{w} За их столиком сидела Славя и Толик."
    hide image re_smile_pioneer
    show image re_mad_pioneer
    with byso
    "Рена встала у входа и стала сверлить взглядом Славю."
    ren "Костя.{w=0.1}.{w=0.1}.{w=0.1} Я понимаю, стабильность, всё такое, но я её сейчас выпотрошу.{w=1} Столовым ребристым ножом.{w=1} {cps=20}Порежу на кубики в 1 сантиметр.{/cps}"
    kt "Спокойно. Судя по падающей и без того стабильности, успеется."
    hide image re_mad_pioneer
    show image re_mad_pioneer at right
    show image tl_angry at fleft
    show sl normal pioneer at cleft
    with byso
    "Взяв еду, Константин и Рена подошли к столику."
    ren "Я вот сейчас не поняла... {w=1}У тебя жизнь запасная?"
    show sl surprise pioneer at cleft with byso
    "Славя была ошарашена происходящим."
    show sl angry pioneer at cleft
    with byso
    sl "Зачем вы так грубо общаетесь, это не хорошо!"
    hide image re_mad_pioneer
    show image re_madsmile_pioneer at right
    with byso
    ren "Ты очень плохо разделяешь понятия грубо и опасно.{w} {cps=15}Со мной конкретно второе.{/cps}"
    ren "Знаешь, у меня отец служил в морской пехоте.{w} Ветеран войны.{w=1} Не так давно его расстреляли за 36 доказанных военных преступлений."
    show sl scared pioneer at cleft with byso
    ren "{cps=15}Пытки с пристрастием, расчленение, сожжение заживо, травление пленников токсинами, обезображивание.{/cps} {w}На его счету более 70 убийств вне правил войны."
    ren "И если ты думаешь что его дочурка ушла далеко, ты ошибаешься. Знакомо понятие генетическая память?"
    ren "Может быть в тайне я хочу показать папочке, как его любимая дочка продолжает его дело?"
    ren "Какая разница кого, это же преступление."
    ren "Так что лучше освободи место...{w} {cps=15}или освобождать его будет некому.{/cps}"
    hide image tl_angry with byso
    "Толик в страхе от услышанного быстро пересел.{w=1} Славя осталась на месте.{w=1} Запуганная, она просто смотрела в глаза Рене."
    hide image re_madsmile_pioneer
    show image re_madsmile2_pioneer
    with byso
    "Она наклонилась к Славе."
    ren "Или ты мне не веришь?{w}.. Хочешь сама в этом убедиться?{w} Мне доказать не сложно."
    "Рена взяла с подноса Слави тупой столовый ножик и засмотрелась на его лезвие."
    stop music fadeout 3
    hide sl with byso
    "Славя не стала медлить и тоже пересела."
    hide image re_madsmile2_pioneer
    show image re_madsmile_pioneer
    with byso
    ren "То-то же."
    play sound sfx_simon_applause volume 0.6
    "Константин, молча наблюдавший за представлением поставил на стол поднос и тихо похлопал."
    hide image re_madsmile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Спасибо."
    "С улыбкой протянула Рена и села на место Слави."
    kt "М-да, интересно ты это преподнесла.{w} Актёрское высший уровень."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Засмущал-засмущал."
    "На обед для наставников был наваристый борщ, рис с мясом и яблочный сок."
    play music god fadein 3
    "Продолжая молча уплетать пищу, Константин задумался."
    th "Мне кажется это реально последний нормальный день в лагере."
    th "Вероятно завтра к вечеру уже случится парадокс.{w=1}.. А что мне ещё расскажет Генда.{w=1}.. Он же теперь знает про Рену."
    th "За один день никто не может так измениться.{w=1} Ещё вчера она была весёлой и жизнерадостной, а сегодня она уже готова к войне."
    th "Не думаю что спрашивать про это лучшая идея, но хотелось бы знать о чём речь..."
    "Мысли Константина прервал любопытный взгляд Рены."
    ren "О чём думаешь?"
    window hide
    menu:
        "О парадоксе.":
            $ renpy.block_rollback()
            hide image re_smile_pioneer
            show image re_bored_pioneer
            with byso
            ren "Честно говоря меня тоже этот феномен напрягает.{w=1} Сама не понимаю что с этим делать..."
            ren "Но у нас есть возможность сбежать из симуляции при 0 стабильности."
            "Константин почесал подбородок."
            kt "Возможно это одна из наиболее разумных идей."
        "О тебе.":
            $ renpy.block_rollback()
            $ rerp += 1
            hide image re_smile_pioneer
            show image re_smile4_pioneer
            with byso
            "Рена улыбнулась."
            ren "Это взаимно."
        "О планах Генды.":
            $ renpy.block_rollback()
            hide image re_smile_pioneer
            show image re_bored_pioneer
            with byso
            ren "Да чего там думать.{w=1} Узнаем мы это сегодня ночью, там деваться уже некуда."
            kt "Да, тоже верно..."
        "О стабильности.":
            $ renpy.block_rollback()
            hide image re_smile_pioneer
            show image re_bored_pioneer
            with byso
            "Рена задумалась."
            ren "Ну, единственное что мы знаем это то что она неуклонно падает."
            kt "Вот потому и задумался."
        "Ни о чём. Просто выпал из реальности.":
            $ renpy.block_rollback()
            hide image re_smile_pioneer
            show image re_bored_pioneer
            with byso
            ren "М-м, бывает."
    "Спустя некоторое время, он покончили с едой и вышли из столовой."
    scene bg ext_dining_hall_near_day
    show image re_smile_pioneer
    with byso
    play ambience ambience_camp_entrance_day fadein 1
    kt "Лады, всё по плану. {w=1}Если я освобожусь раньше, то найду тебя."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Хорошо, тогда удачки тебе."
    hide image re_smile2_pioneer with byso
    "Рена поцеловала Константина и они разошлись."
    scene bg ext_clubs_day
    show image rm_no
    with byso
    "У клубов Константина встретил Рома."
    rm "Иди сюда."
    scene bg ext_camp_entrance_day
    with byso
    play sound light_inh
    "Константин проигнорировал Рому и выйдя из лагеря закурил."
    show image rm_th with byso
    "Рома выйдя за Константином сильно удивился."
    rm "Ты ещё и куришь?"
    kt "А тебе какое нахрен дело?"
    "Пробурчал Константин, осматривая телеги с книгами."
    hide image rm_th
    show image rm_th2
    with byso
    rm "Я не понимаю.{w=1} Почему ты так ко мне относишься?"
    "Сделав очередную затяжку, Константин сел на поребрик."
    kt "Ты ничего не помнишь, твоя память стёрта."
    th "Зачем я это сказал..."
    hide image rm_th2
    show image rm_su
    with byso
    rm "В каком смысле?"
    kt "В прямом.{w} Там и хранятся все причины моей ненависти к тебе."
    hide image rm_su
    show image rm_th2
    with byso
    "Рома сел на корточки и достал свою пачку сигарет."
    rm "Откуда ты знаешь?"
    kt "Совсем идиот чтоль?"
    hide image rm_th2
    show image rm_th
    with byso
    rm "Да нет.{w=1}.. Нет, ладно, глупый вопрос."
    "Рома достал спички и закурил."
    rm "Сегодня ты явно не в духе.{w=1}.. Но Рена..."
    kt "Не смей."
    "Константин заглянул ему в глаза."
    kt "Если ты хоть что-то плохое про неё скажешь, то я тебя прям тут положу."
    hide image rm_th
    show image rm_su
    with byso
    rm "Понятно. Твоя девушка?"
    window hide
    menu:
        "Да.":
            $ renpy.block_rollback()
            $ rerp += 1
            rm "Тогда понятно почему ты так на меня злишься."
        "Нет.":
            $ renpy.block_rollback()
            rm "Понятно..."
    hide image rm_su
    show image rm_th
    with byso
    kt "И что тебе понятно?"
    hide image rm_th
    show image rm_th2
    with byso
    rm "Меня поражает её образ.{w} Я её боюсь.{w=1} Не могу сказать почему."
    th "Да-да, отпинали кое-кого вчера..."
    kt "Ясно."
    hide image rm_th2
    show image rm_sm
    with byso
    rm "Что бы у нас ни было я хочу зарыть топор войны.{w=1} Ты же мой брат."
    play sound sfx_metal_door_handle_rattle
    "Константин затушил сигарету и взял телегу с книгами."
    kt "Нет.{w} За то что ты делал тебе нет прощения."
    scene bg ext_clubs_day with byso
    "Рома остался позади. {w=1}Константин начал волочить книги до библиотеки."
    scene bg ext_square_day
    show image na_no
    with byso
    "На площади он встретил ту же девочку что и в первый день. Она сидела на скамейке и смотрела в небо."
    th "Кого-то она мне напоминает...{w=1} Кого именно я не помню..."
    play sound dissapearance
    hide image na_no with flash 
    "Девочка перевела взгляд на Константина и растворилась."
    th "Пионер может знает что с ней... Надо спросить."
    scene bg ext_library_day with byso
    play sound sfx_knock_door7_polite
    "Константин доехал до библиотеки и постучал в дверь."
    play sound sfx_open_dooor_campus_1
    show mz normal pioneer glasses at right
    show un shy pioneer at left
    with byso
    "Оттуда вышла Лена и Женя."
    show mz bukal pioneer glasses at right with byso
    mz "О, вот и книги.{w=1} Там ещё много?"
    kt "Столько же.{w=1} Сейчас за ними пойду."
    show mz normal pioneer glasses at right with byso
    mz "М-да-а.{w=1} Ладно, иди."
    hide un
    hide mz
    with byso
    "Они взяли по пачке книг и понесли в библиотеку.{w=1} Константин же пошёл обратно."
    scene bg ext_camp_entrance_day with fade
    play sound sfx_metal_door_handle_rattle
    "Спустя некоторое время он уже взялся за вторую телегу и потащил её."
    th "Надо не забыть взять писание из библиотеки."
    scene bg ext_library_day
    show el normal pioneer
    with fade
    stop music fadeout 3
    "Вернувшись обратно, у библиотеки он встретил Электроника."
    kt "Тебя помочь послали?"
    show el upset pioneer with byso
    "Электроник растерялся и отрицательно помотал головой."
    el "Рена не с тобой?"
    kt "Как видишь.{w=1} А теперь либо помогай, либо вали."
    show el sad pioneer with byso
    el "Ладно."
    hide el with byso
    "Опечалено пробормотал Электроник и ушёл."
    scene bg int_library_day
    show mz bukal pioneer glasses at right
    show un normal pioneer far at left
    with byso
    play ambience ambience_library_day fadein 1
    play sound sfx_close_door_1
    play music music_list["lightness_radio_bus"] volume 0.6 fadein 3
    "Девочки уже разобрали половину книг с телеги.{w=1} Константин открыл двери в библиотеку и ввёз в предбанник телегу."
    show mz laugh pioneer glasses at right with byso
    mz "Во, точно, молодец, сообразительный."
    "Константин взял пачку книг и посмотрел на Женю."
    kt "Куда?"
    show mz normal pioneer glasses at right with byso
    mz "С этой телеги в раздел истории.{w} Вторую в подвал."
    kt "Понято."
    hide mz
    hide un
    with byso
    "Константин принялся расставлять книги по полкам."
    th "История нашего времени.{w=1}.. История древнего Египта.{w=1}.. История партии.{w=1}.. М-да.{w} Надо словно кому-то это читать?"
    show mz bukal pioneer glasses with byso
    "Как с историей было покончено, Женя открыла люк в подвал и принялась носить книги туда."
    kt "А зачем книги в подвал тащить?"
    show mz normal pioneer glasses with byso
    mz "Резервы.{w=1} Если с этими будут проблемы, то мы вынесем оттуда."
    kt "Ясно."
    "Константин взял пачку книг и понёс вниз."
    "В подвале стоял стол, а на нём лежала заветная папка с номером 4."
    play sound sfx_paper_bag
    "Взяв её, он бегло пролистал её.{w=1} На ней были прописаны тексты красными чернилами."
    th "Шрифт оставляет желать лучшего.{w=1} Словно врач-терапевт оставил длинный список лекарств для больного."
    show mz bukal pioneer glasses with byso
    mz "И чего встал?"
    kt "Я заберу это?"
    show mz normal pioneer glasses with byso
    "Женя глянула на папку в руках Константина и махнула рукой."
    mz "Да пожалуйста. {w}Она точно никому не нужна."
    kt "Отлично..."
    play sound sfx_blow_out_candle
    show mz bukal pioneer glasses with byso
    "Константин вышел из подвала и положил папку на стул."
    show mz normal pioneer glasses with byso
    "Как с книгами в подвал закончили, Женя села на стул."
    show mz bukal pioneer glasses with byso
    mz "Фух, славно поработали.{w} Телеги надо вернуть к столовой. Отвезёшь?"
    "Спросила Женя, вопросительно посмотрев на Константина."
    kt "Без проблем."
    play sound sfx_paper_bag
    "Константин забрал папку и две телеги."
    show mz laugh pioneer glasses with byso
    mz "Прекрасно.{w=1} Спасибо за помощь, товарищ надзиратель."
    kt "Угу."
    scene bg ext_library_day with byso
    play ambience ambience_camp_entrance_day fadein 1
    play sound sfx_close_door_1
    stop music fadeout 3
    "Константин вышел из библиотеки и направился к столовой."
    th "Видимо Рена ещё на матче."
    scene bg ext_dining_hall_near_day with fade
    "Константин довёз телеги и поставил их у лестницы."
    th "Пойду на площадку.{w=1} Рена должна быть там."
    scene bg ext_playground_day
    show image re_smile4_pioneer
    with fade
    play ambience ambience_soccer_play_background fadein 1
    play music mono fadein 3
    "На спортплощадке вовсю шёл матч.{w=1} Рена стояла со свистком и наблюдала."
    scene cg d3_soccer with byso
    "Ульяна была в нападении и обводила вокруг неуклюжих пионеров."
    play sound sfx_soccer_ball_kick
    "Удар.{w} Мяч попал в рейку.{w=1} Толик, который стоял на воротах даже не среагировал."
    play sound sfx_soccer_ball_catch
    "Мяч направился в сторону команды Ульяны.{w=1} С разбегу она выбивает мяч у пионера и делает повторный удар издалека."
    "Удар пришёлся прямо в лицо Толику, после чего мяч угодил за линию ворот."
    us "Го-ол!"
    ren "Счёт 4-1. В случае ещё одного выигрыша команды <<Слава>>, <<Дружба>> проигрывает."
    "Константин сел на скамью и стал наблюдать за матчем."
    th "Не люблю я футбол конечно, но сейчас почему бы и не посмотреть."
    elp "Ничьей не будет?"
    "Рена нахмурилась."
    ren "Никаких ничьих!{w} Только триумф и победа."
    us "Вот именно, неудачник, учись проигрывать!"
    play sound svistok
    "После такого унижения команды <<Дружба>>, раздался свисток и раунд начался."
    "Рена заметила Константина и помахала.{w=1} Константин ответил тем же."
    "Команду Ульяны начали приминать.{w=1} Мяч так и крутился возле ворот <<Славы>>."
    "Напор был максимален.{w=1} Ульяна многократно пыталась перехватывать мяч, но её команда не могла принять пас и мяч возвращался к противнику."
    play sound svistok
    "Раздался свист."
    ren "Угловой."
    play sound sfx_soccer_ball_kick
    "Игрок <<Славы>> встал в угол и выбил мяч.{w} Мяч улетел на другую половину поля."
    play sound sfx_soccer_ball_catch
    "С размаху Ульяна засадила мяч в ворота, но Толик сам того не понимая предотвратил проигрыш своей команды.{w=1} Своим телом он отбил мяч, после чего <<Дружба>> снова начала вести."
    "Ульяна сделала первоклассный подкат и снова завладела мячом."
    "Рена сделала вид что не заметила ярого нарушения правил."
    play sound sfx_soccer_ball_kick
    "Очередной удар Ульяны пришёлся на светлого пионера.{w=1} Он взял мяч и передал обратно."
    elp "Чёрта с два!"
    us "Хе-хе."
    play sound svistok
    "Раздался свист."
    ren "Штрафной."
    "Ульяна бросила мяч под себя и принялась сама его разыгрывать."
    play sound sfx_soccer_ball_gate
    "Обойдя всю защиту дружбы, она запустила мяч в ворота.{w=1} Мяч снова отскочил от Толика, но Ульяна сделала добивающий и забила в так называемую девятку."
    play sound svistok
    "Раздался свист."
    play ambience ambience_camp_entrance_day fadein 1
    ren "С разгромным счётом в 5-1 команда <<Дружба>> проигрывает.{w=1} Поздравим победителей!"
    scene bg ext_playground_day
    show image re_smile2_pioneer
    with byso
    "Рена выдала каждому члену команды <<Слава>> по грамоте."
    hide image re_smile2_pioneer
    show image re_smile_pioneer at right
    show us grin pioneer at left
    with byso
    "Позже Рена с Ульяной подошли к Константину.{w} <<Дружба>> собиралась вокруг Толика."
    us "Ну как тебе матч?"
    kt "Ты классно сыграла.{w} Чуть ли одна обыграла всю команду."
    show us laugh2 pioneer at left with byso
    us "Да я знаю.{w=1} Вот вам подарок."
    "Ульяна протянула Рене и Константину по 2 конфеты."
    hide image re_smile_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Спасибо. {w=1}Ты хорошо сыграла, Костя прав."
    kt "Спасибо."
    "Константин и Рена убрали конфеты по карманам."
    show us normal pioneer at left with byso
    us "А это что?"
    "Спросила Ульяна Константина, заметив у него в руках 4е писание."
    kt "Отчётные бумаги по поставке в библиотеку.{w=1} Ничего интересного."
    show us sad pioneer at left with byso
    us "Ме-е, скука."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at right
    with byso
    "Рена хихикнула и похлопала Ульяну по спине."
    ren "А в будущем тебе придётся с таким работать."
    show us calml pioneer at left with byso
    "Ульянка скорчилась."
    us "Ну нет, я хочу стать спортсменкой, а этим пусть занимаются другие."
    kt "Как знаешь.{w} Мы с Реной пойдём. {w=1}Дела надзирательские."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at right
    show us grin pioneer at left
    with byso
    "Рена надела свисток на шею Ульяне.{w} Ульяна ухмыльнулась."
    us "Идите, я тоже побегу переодеться."
    hide image re_smile2_pioneer
    show image re_smile2_pioneer
    hide us
    with byso
    stop music fadeout 2
    "Ульянки и след простыл.{w} Константин с Реной направились в сторону своего домика."
    scene bg ext_houses_day
    show image re_smile4_pioneer
    with byso
    play music umted volume 0.8 fadein 3
    kt "Как себя чувствуешь?"
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Хорошо. Надо было сходить на этот матч.{w=1} Весело было посмотреть как Ульяна играла."
    kt "Какие-нибудь хайлайты?"
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Да нет, в основном я наставляла её на матч.{w=1} Как видишь они выиграли."
    ren "Команда и в правду никудышная. {w}Еле-еле сводили концы с концами."
    hide image re_smile2_pioneer
    show image re_bored_pioneer
    with byso
    "Она глянула в небо."
    ren "В этом плане даже жаль что у меня не было такого детства.{w} Веселье, друзья и счастье."
    kt "Далеко не всегда. Палка о двух концах.{w} Явный тому пример - Толик."
    kt "Или я."
    kt "Анатолий Сергеевич и в том мире не отличался красотой. {w}Я думаю именно так его детство прошло. На работе же он просто на мне и Сахаровой отрывался."
    kt "Да и к тому же.{w=1} Генда говорил что <<Полимер>> сбывал наркотики.{w} Толя наверняка это знал, что было его местью."
    kt "На наркотики садятся только <<крутые>>...{w=1} Или неудачники как я."
    hide image re_bored_pioneer
    show image re_smile3_pioneer
    with byso
    play sound sfx_pat_shoulder_hard volume 0.5
    "Рена взяла за руку Константина."
    ren "Ты не неудачник. {w=1}Просто люди вокруг тебя были теми ещё тварями.{w} В кой-то мере не удивительно что ты так думаешь."
    ren "Не забывай.{w=1} Новая жизнь.{w} Хоть она и осложняется некоторыми...{w=1} деталями."
    ren "Но мы с этим должны разобраться."
    ren "Тем не менее ситуация win-win.{w=1} Даже если и не победим, то избавимся от прошлого.{w=1} Навсегда."
    kt "Ты бесспорно права."
    scene bg ext_house_of_sl_day
    show image re_serious3_pioneer
    with byso
    play sound sfx_key_drawer
    pause 0.75
    stop sound
    stop music fadeout 3
    "Они дошли до домика.{w=1} Константин открыл запертую дверь и они вошли."
    scene bg int_house_of_kt_day
    show image re_serious3_pioneer
    with byso
    play ambience ambience_int_cabin_day fadein 1
    play sound sfx_paper_bag
    ren "Итак.{w} Четвёртое писание.{w} Оно хоть не пустое?"
    kt "Нет. Я осмотрел.{w} Почерк ужасный, но это не так страшно."
    show image re_bored_pioneer
    hide image re_serious3_pioneer
    with byso
    ren "Мне зачитать или ты прочтёшь?"
    kt "Да давай я."
    play sound sfx_bed_squeak1
    show image re_smile2_pioneer
    hide image re_serious3_pioneer
    with byso
    "Константин лег на кровать.{w} Рена села на стул рядом."
    play music BlueJetta fadein 5
    window hide
    $ set_mode_nvl()
    "{font=inrealnost/font/NoRules.ttf}Если кто-то это читает значит это не было бесполезной работой."
    "{font=inrealnost/font/NoRules.ttf}Меня зовут Косяков Михаил Анатольевич.{w} 27 лет до попадания сюда.{w} В 2013 году я попал в этот водоворот."
    "{font=inrealnost/font/NoRules.ttf}Я был разнорабочим.{w} Муж на час если угодно.{w} Попал я сюда из-за теракта в городе █████████.{w} Насколько я выяснил, подрыв автобуса."
    "{font=inrealnost/font/NoRules.ttf}Издание я переписываю уже в четвёртый раз я описываю всю суть симуляций.{w} Предыдущие писания не являются корректными по некоторым перестройками в системе создателя."
    "{font=inrealnost/font/NoRules.ttf}В этом сочинении я так же изложу основы логики <<Инреальности>>. То, чего стоит опасаться, то что стоит учесть и то что нужно делать."
    "{font=inrealnost/font/NoRules.ttf}Содержание."
    "{font=inrealnost/font/NoRules.ttf}Введение и терминология, страница 2."
    "{font=inrealnost/font/NoRules.ttf}Силы контроля, страница 3."
    "{font=inrealnost/font/NoRules.ttf}Парадокс, страница 4."
    "{font=inrealnost/font/NoRules.ttf}Существа, страница 5."
    "{font=inrealnost/font/NoRules.ttf}Полезное, страница 6."
    "{font=inrealnost/font/NoRules.ttf}Лирика, страница 7."
    "{font=inrealnost/font/NoRules.ttf}Пометки о прочтении."
    "{font=inrealnost/font/NoRules.ttf}После прочтения прошу поставить отметку для других."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Введение и терминология."
    "{font=inrealnost/font/NoRules.ttf}Симуляции представляет собой отдельные циклы, не имеющий плотной связи между собой.{w} Плотная связь может образоваться только с кошмаром в результате нарушения стабильности."
    "{font=inrealnost/font/NoRules.ttf}Стабильность - величина от 100 до -100, где 100 это абсолютное равновесие, а -100 разрушение мира. 100 присуща только системам <<Семёнов>> и меняется только в случае смерти такого. Для измерения таковой имеется разработанный моим знакомым Нокиа."
    "{font=inrealnost/font/NoRules.ttf}Система <<Семёна>> представляет собой симуляцию инреальности, где ведущим элементом является Семён. Семёном зовут человека, который уже является полноценным элементом пустой симуляции. При изменении таковой может быть замещён в результате разрушения другой симуляции."
    "{font=inrealnost/font/NoRules.ttf}<<Пустышка>> - смотри страницу 5."
    "{font=inrealnost/font/NoRules.ttf}Инреальность - совокупность всех систем, подвластных Генде. Ошибка инреальности равняется ошибке всех систем одновременно, аналогии проводите сами."
    "{font=inrealnost/font/NoRules.ttf}Путник - человек который попадает в инреальность в качестве основного элемента, отличается разумностью. В пустых симуляциях таковыми являются Семёны. При смерти путника стабильность начинает падать по формуле на странице 6."
    "{font=inrealnost/font/NoRules.ttf}Кошмар - подпространство инреальности, которое делится на секторы. Каждый сектор - один лагерь. Количество секторов приблизительно равно 20. Пустышки редко попадают в кошмар из-за нехватки мест."
    "{font=inrealnost/font/NoRules.ttf}Пустышки - смотри страницу 5"
    "{font=inrealnost/font/NoRules.ttf}Оригинальная симуляция - симуляция с новоприбывшим путником из родного мира. Стабильность таковой может быть нарушена достаточно просто. Не полностью подвластны создателю и не содержат Семёнов. Могут содержать более одного путника."
    "{font=inrealnost/font/NoRules.ttf}Парадокс - смотри страницу 4."
    "{font=inrealnost/font/NoRules.ttf}Генда (он же создатель) - смотри страницу 5."
    th "Смотри страницу, смотри страницу... Напиши ты тут, бумаги у тебя там мало? Вот внизу сколько места."
    window hide
    $ set_mode_adv()
    window show
    hide image re_smile2_pioneer
    show image re_bored_pioneer
    with byso
    ren "Уже это многое объясняет.{w=1} Пока я не встретила тебя я, получается, просто оставляла след из симуляций, по которым меня и отследил Генда."
    kt "А я теперь понял момент про Семёнов.{w=1} Как по мне это определение неуместно. Сюда попадают только отбросы."
    hide image re_bored_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Нет уж, по сравнению с теми мы не отбросы."
    "Константин продолжил чтение."
    window hide
    $ set_mode_nvl()
    "{font=inrealnost/font/NoRules.ttf}Силы контроля."
    "{font=inrealnost/font/NoRules.ttf}Если говорить о базовых силах контроля симуляции, то их две: генмод и ЭМ-ограды."
    "{font=inrealnost/font/NoRules.ttf}Так же инреальность позволяет людям проявлять нечеловеческие силы. Происходит это самопроизвольно и/или при смерти. Определяется расположенностью."
    "{font=inrealnost/font/NoRules.ttf}Расположенность - константа, уникальная для каждого субъекта. Определяет возможности к той или иной силе."
    "{font=inrealnost/font/NoRules.ttf}Для принудительного развития силы следует изменить в меньшую сторону стабильность симуляции. Ошибка, развивающая силы в путнике называется дарующей."
    "{font=inrealnost/font/NoRules.ttf}Ошибка является редкой и иногда передаёт способности создателя, смотри Существа, страница 5."
    "{font=inrealnost/font/NoRules.ttf}На способности путников распыляться не имеет смысла. Их много и не все известны."
    window hide
    $ set_mode_adv()
    kt "Кстати, ты вроде как умеешь воплощать оружие."
    hide image re_smile2_pioneer
    show image re_serious3_pioneer
    with byso
    play sound sfx_armature_swish
    "В ответ Рена махнула рукой и образовался огромный топор с угловатым лезвием."
    ren "Есть такое.{w=1} Видимо, убив первого я и вызвала дарующую ошибку, которая наделила меня таким умением."
    play sound sfx_armature_swish
    hide image re_serious3_pioneer
    show image re_smile2_pioneer
    with byso
    "Раскрутив топор в руке, она с такой же лёгкостью его испарила."
    window hide
    $ set_mode_nvl()
    "{font=inrealnost/font/NoRules.ttf}ЭМ-ограды."
    "{font=inrealnost/font/NoRules.ttf}Делят симуляции между собой. Пройти через них не возможно без особой техники или способности. Могут работать в качестве капканов для спектральных сущностей, даруя им материальное тело, в котором они уязвимы для физических воздействий."
    "{font=inrealnost/font/NoRules.ttf}По сути своей это патоген, способный изменить подопытного до неузнаваемости."
    "{font=inrealnost/font/NoRules.ttf}Из-за хаотичности своего влияния является чрезвычайно опасным. При утечке такого все подвергнутые заражению с точки зрения стабильности умирают, чем могут спровоцировать парадокс."
    "{font=inrealnost/font/NoRules.ttf}Заражения делиться на три стадии: излечимая, необратимые изменения, терминальная."
    "{font=inrealnost/font/NoRules.ttf}Излечимая длится около половины дня при низкой дозе в штатном режиме без катализатора. В это время жертву можно излечить методом переливания крови и антибиотиков."
    "{font=inrealnost/font/NoRules.ttf}Необратимые изменения могут травмировать психику и физическое состояние, посредством угнетения работы ЦНС. Излечимо, но уже в несколько раз сложнее. Увечья останутся навсегда."
    "{font=inrealnost/font/NoRules.ttf}Терминальная полностью меняет тело жертвы, превращая его либо в гончую (страница 5), либо в более ужасное создание при воздействии катализаторов."
    "{font=inrealnost/font/NoRules.ttf}Катализатором могут служить иммунодепрессанты или иные средства угнетения иммунной системы тела."
    "{font=inrealnost/font/NoRules.ttf}ВНИМАНИЕ!"
    "{font=inrealnost/font/NoRules.ttf}КАКИМИ БЫ ВЫДАЮЩИМИСЯ НЕ БЫЛИ ВАШИ ПОЗНАНИЯ В МЕДИЦИНЕ, ДАЖЕ НЕ ДУМАЙТЕ ПРОВОДИТЬ ЭКСПЕРИМЕНТЫ НАД ГЕНМОДОМ! САМ ГЕНДА СОЗДАЛ ЕГО ТАК, ЧТОБ В СЛУЧАЕ ЗАРАЖЕНИЯ ВЫЖИВШИХ НЕ ОСТАЛОСЬ!"
    window hide
    $ set_mode_adv()
    window show
    ren "Хм-м...{w=1} Генмод...{w=1} Даже не думала что есть такой эффективный способ устранения Семёнов."
    window hide
    $ set_mode_nvl()
    "{font=inrealnost/font/NoRules.ttf}Парадокс."
    "{font=inrealnost/font/NoRules.ttf}Парадокс - явление, происходящее в результате обнуления стабильности. Миры и кошмар начинают сближаться, провоцируя множество ошибок, благодаря которым симуляция может дойти до -100, где мир просто остановится и исчезнет."
    "{font=inrealnost/font/NoRules.ttf}Исчезновение мира равно полной смерти всех там находящихся. Насчёт самого создателя неизвестно."
    "{font=inrealnost/font/NoRules.ttf}В запущенных случаях обнуления оригинальной симуляции и парадокса может страдать вся инреальность, но Генда старается контролировать этот процесс."
    "{font=inrealnost/font/NoRules.ttf}Мир с обнулённой стабильностью не подвержен реабилитации. Вся нечисть с кошмара начинает пробираться в мир и уничтожать всё на своём пути."
    "{font=inrealnost/font/NoRules.ttf}При обнулении стабильности на некоторое время открываются порталы в количестве от одного до трёх. Ошибка инреальности. Позволяет путнику избежать участи симуляции, но тогда нарушится целостность второго мира."
    "{font=inrealnost/font/NoRules.ttf}Попасть в симуляцию определённого года перемещения можно при помощи формулы, представленной в Полезном, страница 6."
    "{font=inrealnost/font/NoRules.ttf}Создатель вряд-ли оставит это событие без внимания и скорее всего будет искать нарушителя."
    "{font=inrealnost/font/NoRules.ttf}Поскольку инреальность имеет некоторые сходства с <<матрицей>>, Генда способен сканировать все системы на предмет уменьшения стабильности и в особо частых случаях устранять последствия лично."
    "{font=inrealnost/font/NoRules.ttf}Причина по которой Создателю важна стабильность инреальности неизвестна."
    th "Может потому что ему важен конкретный мир?"
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Существа."
    "{font=inrealnost/font/NoRules.ttf}Инреальность имеет собственный бестиарий из монстров, усопших сущностей и формирований. Ниже представлены наиболее популярные из них."
    "{font=inrealnost/font/NoRules.ttf}Более редкие сущности не представлены из-за неопределённости свойств и/или недостаточности информации."
    "{font=inrealnost/font/NoRules.ttf}Гончая. Представляет собой типичного обитателя кошмара. Рост варьируется от одного до трёх метров. Состоит из трупов своих жертв, хотя изначально представляет собой заражённую пустышку."
    "{font=inrealnost/font/NoRules.ttf}Является разносчиком генмода. Порезы, укусы и кровь может занести патоген на других. Кости и мышечная ткань существа способны быстро менять своё положение и форму."
    "{font=inrealnost/font/NoRules.ttf}Способны поедать трупы жертв и себе подобных для регенерации и эволюции."
    "{font=inrealnost/font/NoRules.ttf}Пустышка. Представляет собой типичного обитателя лагеря. Раньше был(а) человеком, но в в силу программы <<исправления>> теряет свой разум, тело становится неузнаваемым, а воспоминания стираются."
    "{font=inrealnost/font/NoRules.ttf}Результатом происходит превращение в одного из базовых элементов лагеря. Наиболее частый - Семён для мужчин и Славя для женщин. После пятого цикла субъект восстановлению не подлежит."
    "{font=inrealnost/font/NoRules.ttf}Создатель. Абсолют инреальности. Реальное имя Гэндо Икари, но предпочитает короткое Генда. Вспыльчив, фанатичен и самолюбив. Именно он производит набор людей в инреальность."
    "{font=inrealnost/font/NoRules.ttf}Не известно, является ли Генда человеком. Он же отрицает своё человеческое происхождение. Целью Генды является частичное порабощение человечества с непонятным мотивом."
    "{font=inrealnost/font/NoRules.ttf}Сопротивление. Основателем является Андрей, который был со мной в первых циклах. Главной целью сопротивления является освобождение инреальности."
    "{font=inrealnost/font/NoRules.ttf}Усопшие. Представляют собой неупокоившихся путников в силу ошибок инреальности. Имеют от одной до нескольки аномальных способностей. Явным примером таковых могу послужить я."
    "{font=inrealnost/font/NoRules.ttf}Из них стоит выделить так называемых <<бестий>>. В отличие от усопших они являются неупокоившимися пустышками. Хаотичны и агрессивны, не могут разговаривать с людьми в силу отсутствия сознания."
    "{font=inrealnost/font/NoRules.ttf}Робокошка. На 5ый день (на 4й при вмешательстве сил других людей) кибернетики собирают робота. Робот начинает безумствовать по мере понижения стабильности."
    "{font=inrealnost/font/NoRules.ttf}Остальные сущности являются либо помесью вышеперечисленных, либо уникальными. Ожидать кого-либо конкретного в инреальности невозможно."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Полезное."
    "{font=inrealnost/font/NoRules.ttf}В каждой симуляции есть некоторые объекты и сущностей, которые могут быть полезны. Также ниже есть несколько формул для определения определённых параметров симуляции."
    "{font=inrealnost/font/NoRules.ttf}Синий Нокиа 6150. В функциях есть возможность определения текущей стабильности инреальности. С начала симуляции начинается таймер, показывающей оставшееся время до перезапуска цикла."
    "{font=inrealnost/font/NoRules.ttf}Внимание! При обнулении стабильности взрывоопасен."
    "{font=inrealnost/font/NoRules.ttf}Ампула мутагена генмод в бункере. Представляет собой ампулу с раствором патогена чёрного цвета с отблеском багряно-красного. Не следует использовать ни в каких целях."
    "{font=inrealnost/font/NoRules.ttf}Радиотехника в бункере. Способна настраивать контакт с другими симуляциями. Механизм работы неизвестен."
    "{font=inrealnost/font/NoRules.ttf}Послевоенный схрон в старом корпусе. Зелёная коробка под лестницей с боеприпасами 9х19 парабеллум в количестве 40 штук, также 3 гранаты Ф-1. Патроны содержат в себе обеднённый уран."
    "{font=inrealnost/font/NoRules.ttf}Патроны не являются действенными в силу отсутствия оружия."
    "{font=inrealnost/font/NoRules.ttf}<<Цена грехов>> в подвале библиотеки. Разработка одного из путников. Способна показывать последние моменты жизни путников в инреальности, но при прочтении ускоряет время вокруг вдвое. Механизм работы неизвестен."
    "{font=inrealnost/font/NoRules.ttf}<<Дневник воли>>. Книга, которую ввозят на 4й день (в редких случаях на пятый). Способна показывать внутренние процессы симуляции. Механизм работы неизвестен."
    "{font=inrealnost/font/NoRules.ttf}Формула, дающая возможность узнать изменение стабильности симуляции. Z=gg-k*(Max-Min), где gg - влияние Генды на стабильность (проценты в час), k - количество влияющих факторов, включая Генду. Max и Min - максимально и минимально влияющие факторы (проценты в час)."
    "{font=inrealnost/font/NoRules.ttf}Пример. Путник устроил мясорубку, а Генда очень сильно пытается восстановить стабильность извне. Факторы: Генда, зверские убийства, паника, агрессия путника. Z=10-4х(20-10). Z=-30 процентов в час."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Формула для перемещения по порталам перед парадоксом. Каждый путник имеет свой год попадания в инреальность. Портал переместит путника в симуляцию с 20xy годом попадания коренного путника."
    "{font=inrealnost/font/NoRules.ttf}X - рандомное число от 1 до 2. Y - первое число факториала от возраста коренного путника первой симуляции."
    "{font=inrealnost/font/NoRules.ttf}Пример. Из симуляции с путником, которому было 25 происходит переход в портал. X равняется 2 по случайности, а y становится равным 1. Переход осуществится в 2021 год попадания."
    "{font=inrealnost/font/NoRules.ttf}Примечания. Порталов бывает 2 или даже 3. Формуле поддаётся только центральный, остальные работают самопроизвольно. Через порталы можно наблюдать за главным элементом симуляции. Переход отнимает у системы от 5 до 25 стабильности за человека."
    th "М-да, вот не в падлу же этому Михаилу было всё это исследовать и описывать."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Лирика."
    "{font=inrealnost/font/NoRules.ttf}Немного лирики для самого себя.{w} Можете пропустить."
    ren "Пропусти. У нас не так много времени."
    kt "Хорошо."
    "{font=inrealnost/font/NoRules.ttf}Пометки о прочтении."
    "{font=inrealnost/font/NoRules.ttf}Если ты прочёл это писание, то оставь пометку. {w}Это позволит вести счёт оригинальных симуляций, которые с текстом ознакомились."
    "Подписей на странице было 6.{w} Михаил, Андрей, Максим, Ирина, Елизавета, Семён."
    window hide
    $ set_mode_adv()
    window show
    stop music fadeout 3
    hide image re_smile2_pioneer
    show image re_serious2_pioneer
    with byso
    "Рена подала Константину карандаш."
    ren "Впиши нас.{w} Оставим след."
    "Константин вписал своё имя и передал Рене."
    play sound sfx_blow_out_candle
    "Она расписалась и положила писание на стол."
    play sound sfx_bed_squeak2
    play music summerdays fadein 3
    "Константин повернулся набок, лицом к Рене."
    kt "М-да...{w=1} Чувствую себя в какой-то фантастике...{w=1} Жесть."
    hide image re_serious2_pioneer
    show image re_serious3_pioneer
    with byso
    ren "Надо было раздобыть <<Цену грехов>>."
    kt "Зачем?"
    ren "Не плохо было бы посмотреть что происходит в других симуляциях.{w=1} Лишняя информация в нашем случае сыграет только на руку."
    play sound sfx_dinner_horn_processed volume 0.8
    "На улице заиграл горн на ужин."
    play sound sfx_bed_squeak1
    "Константин перекатился на спину."
    kt "М-да, быстро день пролетел."
    play sound sfx_bed_squeak2
    hide image re_serious3_pioneer
    show image re_smile3_pioneer
    with byso
    "Рена легла рядом."
    ren "Ну зато он не был потрачен зря.{w} Сегодня мы пойдём в старый корпус. {w=1}Там может найдём чего."
    kt "Представь себе. {w=1}Вся массовка вокруг лишь пустышки."
    hide image re_smile3_pioneer
    show image re_smile2_pioneer
    with byso
    "Рена провела по плечу Константина."
    ren "Словно что-то поменялось.{w=1} Что в твоём мире, что тут.{w=1} {cps=15}Пустышки{/cps}."
    "Протянула она и приняла сидячее положение."
    kt "Ты права.{w} Всего лишь NPC."
    "Константин сел рядом."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Ладно, пойдём есть, а там и на раскопки."
    kt "А ты знаешь планировку?"
    play sound sfx_bed_squeak2
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    "Спросил Константин потянувшись и встав с кровати.{w=1} Рена пошла на выход."
    ren "Угу. Доводилось пару раз побывать."
    scene bg ext_house_of_sl_day
    show image re_smile_pioneer
    with byso
    play ambience ambience_ext_road_day fadein 1
    play sound sfx_close_door_1
    stop music fadeout 3
    "Они вышли из домика."
    kt "При каких обстоятельствах?"
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    ren "На месте расскажу."
    scene bg ext_square_sunset
    show image re_smile2_pioneer at right
    show mt normal pioneer panama at left
    with byso
    play ambience ambience_ext_road_evening fadein 1
    play music music_list["lightness_radio_bus"] volume 0.8 fadein 3
    "На площади их встретила недовольная вожатая."
    mt "Рена.{w} Почему <<Слава>> победила?"
    hide image re_smile_pioneer
    show image re_laugh_pioneer at right
    show us grin pioneer
    with byso
    "Рена и Константин синхронно рассмеялись.{w=1} К ним подошла Ульяна."
    kt "Слава всегда стоит поверх дружбы у большинства людей."
    show us laugh2 pioneer with byso
    "Смеялись все кроме вожатой."
    show mt surprise pioneer panama at left with byso
    mt "Это же дети!{w} Надо было сказать что, победила дружба."
    ren "<<Дружба>> с разгромом в 5-1 проиграла, о чём речь?"
    show mt angry pioneer panama at left with byso
    "Все продолжали смеяться.{w=1} Вожатая продолжала закипать."
    mt "Ничья!{w} Дети же расстроились!"
    hide image re_laugh_pioneer
    show image re_smile2_pioneer at right
    show us grin pioneer
    with byso
    "Как только Рена и Константин отсмеялись, встряла Ульяна."
    us "Ну вот ещё эти неудачники заберут мою славу, фигушки."
    mt "Это что за слова, Ульяна!"
    kt "Да всё в порядке.{w} Дети с раннего возраста должны понимать что они не всегда в выигрыше, иначе потом всё станет куда хуже."
    kt "Они недостаточно старались и проиграли, а их противники постарались и обыграли их."
    show mt surprise pioneer panama at left with byso
    "Вожатая успокоилась."
    mt "Ладно, но судьёй в следующий раз я назначу кого-то другого."
    th "Боюсь следующего раза уже не будет."
    show us calml pioneer with byso
    us "Отстой..."
    hide mt
    hide us
    show us calml pioneer at left
    with byso
    "Тихо пробормотала Ульяна.{w=1} Вожатая ушла."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer at right
    with byso
    ren "Ничего, не расстраивайся.{w} Тоже урок жизни.{w=1} Не всегда судьи будут на твоей стороне."
    show us smile pioneer at left with byso
    us "Ну ладно.{w}.. Но это был самый классный матч за смену."
    stop music fadeout 3
    hide image re_smile3_pioneer
    show image re_smile_pioneer at right
    hide us
    show us shy pioneer at cright
    with byso
    hide us
    hide image re_smile_pioneer
    show image re_smile_pioneer
    with byso
    "Ульяна обняла Рену и быстро убежала в столовую."
    kt "Кажется ты ей нравишься."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    "Рена улыбнулась."
    ren "Я знаю.{w=1} Она тоже классная девчонка.{w} Исключили Дваче из её жизни и она стала приятной."
    hide image re_smile2_pioneer
    show image re_sad3_pioneer
    with byso
    ren "Жаль правда осознавать что её жизнь может закончиться с этим циклом."
    scene bg int_dining_hall_people_sunset_cust
    show image re_smile_pioneer
    with byso
    play ambience ambience_dining_hall_full fadein 1
    "В столовой уже все сидели по своим местам.{w=1} Место Рены и Константина уже никто не занимал, а Толик и Славя вообще сидели в другом конце столовой."
    "На ужин наставникам снова подавали свиное рагу и квас."
    scene bg ext_dining_hall_near_sunset
    show image re_smile2_pioneer
    with byso
    play ambience ambience_ext_road_evening fadein 1
    "Во время еды их никто не побеспокоил и они вышли из столовой."
    kt "Ольга Дмитриевна!"
    show mt normal pioneer panama at left with byso
    "Константин окликнул вожатую после чего та подошла к ним."
    mt "Я слушаю."
    kt "Мы хотели бы пойти спать пораньше.{w} После вчерашней работы мы плохо выспались, потому и ляжем сейчас."
    show mt surprise pioneer panama at left with byso
    "Вожатая почесала затылок."
    mt "Ну-у, ладно.{w} Идите, беспокоить не буду."
    hide mt with byso
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Ловко ты это додумал.{w} Теперь никто и не подумает что мы собрались в экспедицию."
    kt "Я тут чего вспомнил. Когда я таскал книги я пересёкся с Ромой."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "И чего?"
    kt "Его память очень вряд-ли к нему вернётся.{w=1} Да и к тому же теперь он боится тебя."
    hide image re_smile_pioneer
    show image re_laugh_pioneer
    with byso
    "Рена рассмеялась."
    ren "Инстинкт самосохранения у человека проснулся.{w} Чудеса да и только."
    scene bg int_house_of_kt_day
    show image re_smile_swim
    with byso
    play ambience ambience_int_cabin_evening fadein 1
    play music Gallow fadein 3
    "Войдя в домик, Рена начала переодеться в свой обычный наряд."
    kt "Зачем тебе платье?"
    hide image re_smile_swim
    show image re_sad_swim
    with byso
    "Рена достала берет и посмотрела на Константина."
    ren "Боевые сапоги имеют хорошее сцепление с поверхностью и имеет несколько подшитых лезвий, а длинное платье лучше короткой юбки, поскольку не сковывает движения."
    "Константин стал собирать рюкзак."
    kt "Разумно-разумно."
    hide image re_sad_swim
    show image re_smile_casual
    with byso
    ren "Советую шорты сменить на уличные джинсы."
    kt "Точно."
    "Константин снял шорты и достал синие джинсы."
    kt "Так явно будет лучше."
    "Компас и мультитул Константин положил в карман.{w} В портфель он закинул запасные батарейки, фонарик, бинт, перекись и фальшвеер."
    "Рена взяла фонарик и подала Константину его Люгер."
    kt "Зачем мне он нужен?"
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Оружие как презерватив.{w=1} Будет неудобно, если в нужный момент его не окажется под рукой."
    kt "Хе, разумно."
    "Константин убрал Люгер в карман."
    hide image re_grin_casual
    show image re_smile2_casual
    with byso
    ren "Ключи не забудь."
    kt "Помню."
    play sound sfx_keys_rattle
    "Константин повесил связку ключей на пояс и был готов к выходу."
    hide image re_smile2_casual
    show image re_smile_casual
    with byso
    ren "Двинули."
    scene bg ext_polyana_sunset
    show image re_smile_casual
    with byso
    play ambience ambience_forest_evening fadein 1
    play sound light_inh
    "Дойдя до лесистой местности, Константин закурил и протянул сигарету Рене."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Спасибо."
    kt "Наша цель.{w} Найти от чего ключи.{w} Поискать тайники."
    hide image re_grin_casual
    show image re_smile2_casual
    with byso
    ren "Так точно."
    scene bg ext_old_building_night_moonlight
    show image re_smile2_casual
    with byso
    play ambience ambience_forest_night fadein 1
    "Когда они вышли к старому зданию уже стемнело."
    scene bg int_old_building_night with byso
    "В здании веяло гнилым деревом и сыростью."
    hide image re_smile2_casual
    show image re_bored_casual
    with byso
    ren "Секунду."
    play sound sfx_wood_floor_squeak
    "Она сняла первую ступеньку с лестницы и достала оттуда зелёный ящик."
    kt "Откуда ты знаешь?"
    hide image re_bored_casual
    show image re_smile3_casual
    with byso
    ren "Находила его уже.{w} Подай инструмент."
    "Константин достал из кармана мультитул и подал Рене."
    "Она аккуратно вытащила гвозди из ящика и сняла крышку."
    "Внутри было 3 гранаты Ф-1 и коробка с подписью 9х19."
    hide image re_smile3_casual
    show image re_grin_casual
    with byso
    ren "Как только я увидела патроны от того пистолета, я сразу вспомнила про этот тайник.{w} Положи гранаты в рюкзак."
    kt "Ничего себе.{w}.. Я такое оборудование в руках не держал."
    "Удивился Константин, убирая гранаты в рюкзак."
    ren "Патроны тебе закинуть положить?"
    kt "Не, спасибо, разберусь."
    hide image re_grin_casual
    show image re_smile3_casual
    with byso
    ren "Как знаешь."
    play sound ammo volume 0.4
    "Константин положил пули в боковой карман."
    kt "Маленькое здание однако..."
    hide image re_smile3_casual
    show image re_smile4_casual
    with byso
    ren "Нас не столько интересует сам дом, сколько бункер и шахта."
    kt "Чего?{w} Шахта?"
    hide image re_smile4_casual
    show image re_grin_casual
    with byso
    "Рена усмехнулась."
    ren "Агась. {w}Люк тут."
    play sound metal2
    "Указала она и пнула крышку ногой."
    kt "Ну поползли."
    play sound sfx_open_metal_hatch
    "Константин начал откручивать вентиль.{w=1} Люк открылся и раздалось глубокое эхо."
    kt "Дамы вперёд."
    hide image re_grin_casual
    show image re_smile4_casual
    with byso
    ren "Очень мило."
    hide image re_smile4_casual with byso
    "Проговорила Рена и поползла вниз.{w} Константин полез за ней."
    scene bg int_catacombs_entrance
    show image re_bored_casual
    with byso
    play ambience ambience_catacombs fadein 1
    play sound sfx_metal_door_large_close_basement
    "Их встретил огромный бетонный тоннель, который словно не имел конца."
    kt "Нам в какую сторону?"
    hide image re_bored_casual
    show image re_smile2_casual
    with byso
    ren "Честно, без понятия.{w} Идём налево."
    "Рена пошла вперед, а Константин шёл позади."
    "Достав из рюкзака пули, он начал по дороге выцарапывать на их наконечнике кресты."
    hide image re_smile2_casual
    show image re_shy_casual
    with byso
    ren "Ты зачем пули портишь?"
    kt "Почему порчу?{w=1} Я наношу эти кресты для повышения экспансии патронов."
    hide image re_shy_casual
    show image re_smile_casual
    with byso
    ren "А, тогда поняла."
    kt "Так меня ещё дедушка учил для охоты.{w} Для большего ущерба стоит позаботиться о сминании пули в теле противника."
    hide image re_smile_casual
    show image re_bored2_casual
    with byso
    ren "Пули с обеднённым ураном слишком бронебойные.{w=1} Одна херня пройдут навылет."
    kt "Хотя да...{w} Ну, тогда чисто ради шарма."
    hide image re_bored2_casual
    show image re_grin_casual
    with byso
    "В ответ она мило улыбнулась."
    ren "Я вот знаешь чего подумала?"
    kt "Рановато мы начали судить о мирности нашей нынешней жизни?"
    hide image re_grin_casual
    show image re_smile4_casual
    with byso
    ren "В точку. Ещё пару дней назад мы кружились в вальсе и сидели на пирсе, вчера вместе готовили, а сегодня мы исследуем катакомбы и делаем насечки на пули."
    ren "Жизнь ещё вчера была удивительна и приятна.{w} Сегодня мы понимаем что столкновение с Гендой неизбежно."
    kt "Это верно.{w} Заполню пока пустые магазины."
    hide image re_smile4_casual
    show image re_bored_casual
    with byso
    ren "Мы пока что не торопимся.{w} Хотелось бы чтоб всё это закончилось."
    "Константин, сменив пулю усмехнулся."
    kt "Ты озвучила мою ежедневную утреннюю мысль в городе."
    hide image re_bored_casual
    show image re_grin_casual
    with byso
    ren "Да нет, я не про самоубийство.{w} Аккуратно, лужа."
    ren "Я про то что если мы победим, то по факту сможем встать на место Генды."
    kt "И чего, продолжать его деятельность?"
    hide image re_grin_casual
    show image re_kind2_casual
    with byso
    "Рена хмыкнула и обернулась на Константина."
    ren "Да нет, дурачок.{w} Начать свой мир. {w=1}Обустроить собственную реальность.{w} Это ли не счастье?"
    ren "Мир, который можно обернуть в свою песочницу.{w} Стать лучшими версиями себя и наконец полюбить жизнь."
    ren "Или же можно вернуться в тот мир."
    kt "Да ну, второе херня идея."
    "Прокомментировал Константин, нанеся последний крест. Он насчитал 40 патронов."
    kt "Те же проблемы. {w=1}Те же убогие люди. {w=1}Та же серость. {w}Надо тебе это?"
    hide image re_kind2_casual
    show image re_smile2_casual
    with byso
    ren "Узко мыслишь.{w} Мы можем разбогатеть при помощи инреальности.{w=1} Тут мы, скажем, налепим кучу золотых слитков и перенесём их в тот мир."
    kt "И вызовем обвал экономики."
    play sound sfx_body_bump volume 0.5
    "Усмехнувшись, Константин убрал патроны в рюкзак."
    kt "Сама же знаешь этот прикол с рынком.{w} Я в бухгалтерии работал."
    hide image re_smile2_casual
    show image re_kind2_casual
    with byso
    ren "Да я-ж не говорю что мы только золото тоннами будем таскать..."
    kt "А налоговая?{w} А менты?{w} А тюрьма за манипуляции рынком?"
    hide image re_kind2_casual
    show image re_bored_casual
    with byso
    "Рена тяжело вздохнула."
    ren "Ну всё-всё, убил во мне ребёнка.{w=1} Акушер недоделанный..."
    "Константин в ответ рассмеялся."
    kt "О, неужто дверь?"
    hide image re_bored_casual
    show image re_grin_casual
    with byso
    "Рена подняла фонарь и посветила вдаль."
    ren "Действительно.{w} Это похоже тот бункер."
    scene bg int_catacombs_door
    show image re_smile2_casual
    with byso
    stop music fadeout 3
    "Дойдя до двери, они заметили знак радиационной опасности."
    kt "Дверка хорошая конечно.{w} Щас бы её открыть..."
    "Пробормотал Константин, взявшись за вентиль."
    hide image re_smile2_casual
    show image re_kind2_casual
    with byso
    ren "Давай помогу."
    play sound sfx_open_door_mines_metal
    "Двойным напором они смогли сделать три оборота и дверь открылась."
    scene bg int_catacombs_living 
    show image re_bored_casual
    with byso 
    play music god fadein 3
    "На удивление в бункере был свет.{w} Две койки, пара огнетушителей, шкафчики и целые горы радиотехники."
    ren "Бункер на случай ядерной бомбардировки.{w} У нас случай хуже.{w=1} Парадокс."
    kt "Если ты не против, я пороюсь в технике. {w=1}Осмотри шкафы пока что."
    hide image re_bored_casual
    show image re_grin_casual
    with byso
    ren "Поняла."
    hide image re_grin_casual with byso
    play sound sfx_click_2
    "Константин сел за стул радиста и включил питание на приборах."
    ren "Подай ключи, пожалуйста.{w} И инструмент."
    "Константин дал Рене запрошенные вещи и засмотрелся в монитор."
    play sound sfx_radio_tune
    "Надев наушники, Константин выбирал случайную частоту."
    show image re_bored2_casual with byso
    "Не дало результата.{w=1} Константин запустил автосканирование, снял наушники и повернулся к Рене."
    kt "Нашла чего?"
    ren "Похоже да. {w=1}Шкафы закрыты.{w=1} Ищу ключи.{w=1} Не найду - вскрою так."
    kt "Окей.{w=1} Я пока посмотрю радио."
    play sound sfx_radio_tune
    hide image re_bored2_casual with byso
    "Автопоиск увенчался успехом.{w=1} На частоте 87,5 проигрывалось сообщение."
    "В наушниках было плохо слышно, потому Константин вынул штекер наушников из звуковой карты и вставил штекер колонки."
    window hide
    $ set_mode_nvl()
    window show
    "Меня зовут Макс. 2022 год.{w=1} Если ты слышишь это сообщение значит я уже мёртв."
    "Генда узнал про мои попытки побега.{w} Генда лишил меня дарованных Мишей способностей.{w} Бежать мне больше некуда."
    "В шахтах за огромной дверью вы можете найти мой схрон, больше ничего сказать не могу."
    "На заднем плане был слышен стук и скрежет в дверь."
    "Меня загнали в угол. Сейчас я выпью снотворное и попаду в кошмар.{w} У меня нет выбора, гончие уже ломятся в дверь."
    "Оружия у меня нет. Я совершенно беспомощен."
    "Отомсти за меня.{w} Мой труд не должен уйти в никуда."
    "После прослушивания выключи транслятор в электронном шкафу."
    window hide
    $ set_mode_adv()
    window show
    play sound sfx_click_1
    "Сообщение оборвалось и началось заново.{w} Константин выключил радио и транслятор."
    show image re_bored_casual at right
    show image poter_n at left
    with byso
    "В помещении образовался пионер."
    pp "Зайдите в шахты.{w=1} Там вы найдёте мой тайник. {w=1}Извините, нет времени сейчас говорить, что-то странное происходит."
    hide image poter_n
    hide image re_bored_casual
    show image re_bored2_casual
    with byso
    "Пионер растворился.{w=1} Рена и Константин переглянулись."
    kt "Что-то странное?"
    ren "С языка снял.{w} Что именно?..."
    hide image re_bored2_casual
    show image re_grin_casual
    with byso
    ren "Сходим за его тайником?"
    "Константин пожал плечами."
    kt "Почему бы и нет.{w=1} Ты нашла что-нибудь?"
    play sound sfx_drawer_rattle
    hide image re_grin_casual
    show image re_smile_casual
    with byso
    "Рена достала из вскрытого шкафчика небольшую белую коробочку с красным крестом."
    ren "Ампула тут, судя по всему. Стоит взять на всякий случай."
    kt "Опасно."
    hide image re_smile_casual
    show image re_angry_casual
    with byso
    "В ответ она строго посмотрела на Константина."
    ren "Опасно ей тут оставаться.{w=1} Если хоть кто-то неосведомлённый её найдёт, то крышка нашей симуляции."
    kt "Разумно. {w=1}В шахты?"
    hide image re_angry_casual
    show image re_smile4_casual
    with byso
    ren "Идём."
    "Она дала Константину мультитул."
    play sound sfx_fall_metal_door
    scene bg int_catacombs_living_nodoor
    show image re_smile2_casual
    with byso
    stop music fadeout 2
    "Спустя минуту, Константин снял дверь с петель и та с грохотом повалилась на пол."
    scene bg black with byso
    play ambience ambience_catacombs_stones fadein 1
    play sound sfx_body_bump
    play music regret fadein 3
    "Войдя в шахты, они достали фонарики."
    scene bg int_mine_halt
    show image re_shy_casual
    with byso
    play sound sfx_click_1
    ren "Смотри, что это?"
    "Рена нашла на стене план эвакуации.{w=1} На нём была некая комната с пометкой <<Инвентарная>>."
    kt "Видимо нам туда.{w=1} Молодец что заметила."
    hide image re_shy_pioneer
    show image re_kind2_casual
    with byso
    ren "Знаю.{w=1} Направо-направо-налево-прямо-налево-прямо-налево.{w=1} Я запомню."
    scene bg int_mine_crossroad
    show image re_grin_casual
    with byso
    "Они продолжили движение."
    ren "Пионер так и не сказал что в тайнике."
    kt "Ну, в таком случае узнаем сами."
    play sound portal
    scene bg int_mine
    show image re_holod_casual
    with fade
    stop music fadeout 2
    "Спустя 5 минут разговоров раздался странный звук."
    ren "Тихо..."
    "Рена перешла на шёпот."
    kt "Что это?.."
    hide image re_holod_casual
    show image re_holod2_casual
    with byso
    "В ответ она лишь мрачно оглянулась."
    ren "У нас гости из другой симуляции."
    play sound ToxiSector fadein 1
    hide image re_holod2_casual
    show image re_bored_casual
    with vpunch
    vng2 "Ни с места!{w=1} Руки в гору!"
    "Рена и Константин медленно подняли руки."
    th "Что за криминальный триллер?!"
    vng2 "Обернитесь!"
    hide image re_bored_casual
    show image re_holod_casual at right
    show image me_no at left
    with byso
    "Обернувшись, они увидели пионера со странным оружием."
    ren "Чё тебе от нас надо..."
    "Прорычала Рена, прищурив глаза.{w} В них читалась едва заметная жестокость."
    pi "Представьтесь!"
    kt "Константин."
    hide image re_holod_casual
    show image re_holod2_casual at right
    with byso
    ren "Рена..."
    "Семён подошёл ближе."
    pi "Вы пойдёте со мной.{w=1} Я рядовой <<Лазурь>> из сопротивления."
    ridov "Сдайте оружие если у вас оно есть!"
    ren "Отдай ему пистолет."
    th "Зачем..."
    play sound sfx_grate_hand_fall
    "Константин послушно достал пистолет и кинул на землю."
    hide image me_no
    show image me_su at left
    with byso
    ridov "Благодарю за содействие."
    "Парень наклонился забрать пистолет."
    window hide dissolve
    pause 1
    play sound tesak
    pause 0.4
    play sound2 sfx_chair_fall
    play music CowCowCow
    hide image me_su
    hide image re_holod2_casual
    show image re_normal_casual_topor
    with vpunch
    "Рена в момент подлетела к рядовому и отрубила ему правую руку по плечо."
    play sound krik2
    "Семён разразился криком.{w=1} Причудливое оружие вместе с рукой парня упало на пол, а Константин быстро поднял Люгер и прицелился в рядового."
    play sound sfx_punch_washstand
    play sound2 perelom
    "Она стряхнула с топора кровь и ударом сломала пионеру ногу."
    hide image re_normal_casual_topor
    show image re_smile_casual_topor
    with byso
    ren "А теперь рассказывай чего ты от нас хотел!"
    play sound sfx_punch_washstand
    "Усмехнулась она и пнула рядового по рёбрам."
    ren "Пушку он на нас наставляет!{w=1} Кто ты без неё, а?!"
    "В ответ он лишь стиснул зубы и фыркнул, стараясь прикрыть рану и встать."
    hide image re_smile_casual_topor
    show image re_cr_smile2_casual
    with byso
    ren "Костя, подай мультитул.{w=1} Сейчас мы сделаем его чутка более разгорчивым."
    "Константин дал Рене мультитул и поднял с пола оружие пионера."
    play sound sfx_body_bump
    pause 0.7
    play sound2 knife_in
    "Рядовой попытался вырваться, но Рена метким ударом с ноги в колено пионера, вернула его в лежачее положение и вонзила отвёртку ему в пах." with vpunch
    ren "Рассказывай.{w=1} Иначе я тебя этим мультитулом наизнанку выверну."
    ridov "А-а-а!{w=1} Хрена с два!"
    play sound horror1
    play sound2 krik
    hide image re_cr_smile2_casual
    show image re_cr_smile_casual
    with byso
    "После этих слов Рена взяла целую руку пионера и медленно наносила продольный порез мультитулом.{w=1} Раздался жуткий вопль."
    ren "Меня не устраивает такой ответ!{w=1} Отвечай!{w=1} Кто такой и чего тут делаешь?!"
    ridov "Ладно!!!{w=1} Прекрати!{w=1} Олег Колесников, позывной <<Лазурь>>, 2021 год попадания в инреальность, рядовой сопротивления!"
    kt "Чё ты тут забыл?!"
    ridov "Капитан приказал уничтожать все симуляции без путников!"
    hide image re_cr_smile_casual
    show image re_cr_smile2_casual
    with byso
    ren "С какой целью, говори!"
    ridov "Кх...{w=1} Сказано нарушить стабильность инреальности!{w=1} Сопротивление поднимает революцию!"
    kt "У тебя было оружие.{w=1} Что это?"
    ridov "Плазмоинтегратор!"
    kt "Точнее!"
    ridov "Штатное энергетическое оружие."
    hide image re_cr_smile2_casual
    show image re_cr_smile_casual
    with byso
    ren "Почему сопротивление поднимает революцию?"
    ridov "Наших сил хватает для борьбы с Гендой...{w=1} Он уязвим!"
    hide image re_cr_smile_casual
    show image re_cr_smile2_casual
    with byso
    ren "Кто здесь отдаёт команды?!"
    ridov "Дз-зета..."
    "На этих словах рядовой потерял сознание от массовой потери крови."
    hide image re_cr_smile2_casual
    show image re_angry_casual
    with byso
    ren "Вот чёрт!{w=1} Со своими позывными, хрен поймёшь!"
    stop music fadeout 3
    "Константин показал Рене пушку рядового."
    kt "А это ещё что?"
    hide image re_angry_casual
    show image re_bored2_casual
    with byso
    play sound sfx_click_1 volume 1
    "Он случайно нажал одну из кнопок."
    play sound_loop shock volume 0.21
    "Оружие начало шуметь и трястись."
    hide image re_bored2_casual
    show image re_guilty_casual
    with byso
    play sound sfx_dropped_chair
    play sound_loop shock volume 0.51
    "Константин рефлекторно бросил оружие на пол."
    play sound afterdead
    stop sound_loop
    scene bg white with bso
    stop ambience fadeout 3
    show blink
    "Оружие ярко засветилось.{w=1} Константин и Рена потеряли сознание."
    play sound in_vosp
    ren "Костя!{w=1} Вставай!"
    play music ParentIssues fadein 3
    play ambience ambience_forest_night fadein 1
    scene bg ext_square_night
    show image re_bored_casual
    show unblink
    play sound2 glad
    "Очнулись они на площади.{w=1} Рена трясла Константина за плечи."
    kt "Что произошло?.."
    hide image re_bored_casual
    show image re_bored2_casual
    with byso
    ren "Я не знаю... Эта штука просто нас выкинула на поверхность... Не знаю как..."
    "Константин встал на ноги и отряхнулся."
    kt "М-да... Ну это, давай в домик?"
    hide image re_bored2_casual
    show image re_smile4_casual
    with byso
    "Рена пару раз кивнула и указала дорогу."
    ren "Ну идём. Было бы неплохо поспать."
    scene bg zvezda with byso
    "Идя практически нога в ногу, они смотрели на звёздное небо."
    ren "А ещё тот рядовой сдох...{w=1} Стабильность наверняка упала."
    "Засмотревшись в сторону, она поправила берет."
    ren "Конец нашей мирной жизни. Завтра надо будет что-то делать."
    kt "Да, это точно..."
    kt "Слушай, а пионер куда и зачем?"
    ren "Сама не понимаю. Должен же был вернуться?"
    ren "Правда..."
    ren "Мне начинает казаться что он не вернётся."
    scene bg ext_houses_night
    show image re_bored2_casual
    with byso
    "Константин поднял бровь и посмотрел на Рену."
    kt "С чего такие догадки?"
    ren "Мне просто кажется, что он предатель. Со стажем."
    hide image re_bored2_casual
    show image re_bored_casual
    with byso
    ren "По нему видно."
    ren "Отвернись в нужный момент и в твоей спине на одну рану больше."
    kt "Не знаю. Мне казалось что он нормальный человек... Ну или кто он там."
    hide image re_bored_casual
    show image re_bored2_casual
    with byso
    play sound glad
    "Она погладила Константина по плечу и улыбнулась."
    hide image re_bored2_casual
    show image re_kind_casual
    with byso
    ren "Скорее всего твой разум помутили его способности."
    ren "Я поняла что с ним не так ещё во время первого нашего с ним диалога."
    hide image re_kind_casual
    show image re_kind2_casual
    with byso
    play sound2 sfx_pat_shoulder_hard volume 0.4
    play sound glad
    "Взяв Константина под руку, Рена нежно провела пальцами по его руке, и тот даже вздрогнул от удовольствия."
    ren "Не бойся. Что бы не входило в его планы, я тебя защищу."
    hide image re_kind2_casual
    show image re_smile3_casual
    with byso
    ren "Что бы не встало у нас на пути, я ничему не позволю тебе навредить."
    hide image re_smile3_casual
    show image re_bored2_casual
    with byso
    play sound sfx_keys_rattle
    "Дойдя до домика, Рена отпустила Константина и начала искать ключи."
    kt "Но мы так и не определились... что дальше?"
    play sound2 sfx_key_drawer
    pause 1
    stop sound2
    "Она нашла ключи и вставила нужный в дверь."
    hide image re_bored2_casual
    show image re_bored_casual
    with byso
    ren "Давай об этом завтра. Утро вечера мудренее."
    play ambience ambience_int_cabin_night fadein 1
    scene bg int_house_of_kt_night with byso
    play sound door_cl
    play sound2 sfx_key_drawer
    pause 1
    stop sound2
    "Пропустив Константина, Рена закрыла дверь на ключ."
    "В домике царил мрак, среди которого были видны только силуэты."
    play sound glad
    "Рена погладила Константина по плечу."
    ren "Уже час ночи."
    kt "Угу..."
    "Константин на ощупь разделся и лёг в постель. {w}Рена, судя по звукам, тоже начала раздеваться."
    play sound2 sfx_hatch_drop volume 0.6
    stop music fadeout 3
    "Поставив будильник на 7 утра, Константин откинул телефон на стол и лёг на спину."
    play sound glad
    "Рена легла в упор к Константину. Константин телом почувствовал, что Рена без одежды."
    stop ambience fadeout 3
    play music umted fadein 3
    ren "Мирной жизни конец, но не моим чувствам..."
    "Константин повернул голову в сторону Рены."
    kt "Что ты..."
    "Рена приложила палец к губам Константина."
    ren "Тс-с, молчи и получай удовольствие."
    scene bg re_int with byso
    "Рена решила начать агрессивное наступление на тело Константина."
    "У Константина уже много лет не было половой жизни.{w=1} То что случилось сейчас выбило его из колеи."
    "Чувство тепла и доверия.{w=1} Это не шло ни в какое сравнение с тем, что было у него некоторое время назад."
    "История состояла в том что Константин лишился своей девственности не с любимым человеком, а на вписке под веществами."
    "Чувства которые он испытывал тогда были не самыми приятными.{w}.. Отвратная мясная возня с человеком, которого ты видишь впервые."
    "Хоть Рену он и не знал долго, если брать время в симуляции, он понимал что она ему точно не чужой человек."
if rerp > 10:
    "Сказать больше, он полюбил её.{w} Полюбил больше себя."
    "Хоть и любовь к себе была достаточно абстрактным для него явлением, но всё-же. {w}Их любовь оказалась взаимной."
    jump nbdfui9sbnidspobnvmisdjbnvsdiuop
else:
    "По крайней мере он мог ей доверять, ведь у неё нет причины его предавать.{w} Она любит его."
    jump nbdfui9sbnidspobnvmisdjbnvsdiuop
label nbdfui9sbnidspobnvmisdjbnvsdiuop:
    "Этот секс был для Рены больше чем просто излияние похоти.{w} Скорее это напоминание, что ей никто не нужен кроме Константина."
    "Она живёт{w=0.5} ради него."
    "Она просыпается{w=0.5} ради него."
    "Она пожертвует собой{w=0.5} ради него."
    "Она убивала{w=0.5} ради него."
    "Она убьёт{w=0.5} ради него."
    scene bg re_int2 with fade
    play sound light_inh
    "Спустя 20 минут Константин достал из джинс пачку сигарет и закурил.{w} Рена сделала то же самое."
    kt "Это... было прекрасно..."
    play sound inh
    "Протянул Константин, затянувшись.{w=1} Рена положила голову ему на плечо."
    ren "Согласна...{w=1} Я люблю тебя!"
    "Рена снова поцеловала Константина в шею."
    ren "Жаль что завтра всё закончится.{w=1} Я только начала наслаждаться жизнью."
    kt "М-да.{w}.. Это точно.{w} Полностью с тобой согласен."
    "Константин взял со стола маленькое блюдце и скинул на него пепел."
    ren "Столько мы бы могли вместе сделать.{w=1} Гонять пионеров по клубам. {w=1}Плясать на дискотеках."
    ren "Да что угодно.{w} Сейчас, похоже нет возможности так жить."
    "Рена закинула окурок туда же, а Константин поставил блюдце на стол."
    kt "Что-ж...{w=1} В кошмар?"
    play sound glad
    "Рена легла на плечо Константина."
    ren "В кошмар..."
    show blink
    stop ambience fadeout 2
    stop music fadeout 2
    "Константин закрыл глаза и окунулся в сон."
    pause 2
    play music unskyidy fadein 3
    play ambience ambience_forest_night fadein 1
    scene bg ext_path_night
    show image so_gd
    show unblink
    "Проснулся он в лесу на земле.{w} Спиной к нему стоял Генда."
    gg "Вот дай тебе хоть немного человеческого отношения..."
    "Генда обернулся, надел очки и начал приближаться. {w=1}Константин тем временем встал с пола."
    gg "Как ты всё начнёшь портить!"
    gg "Ты откуда её притащил?!" with vpunch
    "Генда перешёл на крик."
    kt "А тебя ебать не должно."
    play sound sfx_punch_washstand
    "В ответ создатель настолько сильно дал Константину в лицо, что он отлетел на пару метров." with vpunch
    gg "Твоя эта подружка разрушила 36 симуляций!{w} Погибло более тысячи исправляемых и исправленных людей, так ещё и пробудила сопротивление!"
    gg "Сопротивление...{w=1} А может ты с ним на связи?!"
    gg "Ты же уже наверное вышел на контакт с Мишей или Андреем!{w} Они были такими же дегенератами как и ты!"
    play sound hit_brick
    play sound2 perelom
    show image blood1
    with vpunch
    "Создатель пнул Константина ногой по рёбрам.{w=1} Раздался хруст в грудной клетке.{w} Подступила адская боль, но Константин лишь еле сопел."
    gg "Да-а, какой-то урод сказал как тут всё устроено!"
    gg "Я ведь хотел тебе помочь...{w=1} Сделать человеком.{w=1}.. А ты!"
    "Генда одной рукой поднял Константина."
    gg "Ты лишь плюёшь мне в лицо.{w=1} Жалкий, неблагодарный скот!"
    play sound sfx_punch_washstand
    "Очередной удар снова пришёлся по лицу." with vpunch
    "Нос как и челюсть с черепом были сломаны, Константин не был в состоянии говорить."
    gg "Ты и твоя подруга нарушили стабильность инреальности!"
    gg "Да чёрт с ней, со стабильностью!{w} Сопротивление!..."
    play sound head_crush
    hide image so_gd
    show image so_sm
    hide image blood1
    show image blood2
    with vpunch
    "Генда ногой сломал Константину позвоночник."
    gg "Ну ты обожди...{w=1} Скоро тебя ждёт такой ад..."
    gg "Никогда не забудешь."
    gg "Говорили тебе, наверное, не нужно кусать руку, которая тебя кормит."
    gg "И не нужно портить имущество того, кто даёт тебе жизнь."
    play sound wood_hit_head
    play sound2 sfx_bones_breaking
    "Создатель наступил на кисть Константина и каблуком туфель раздавил все пальцы."
    gg "Ты сейчас даже понять не можешь, что я был готов тебе предложить."
    gg "Но...{w=1} нет так нет."
    "Генда наклонился к еле-живому Константину."
    gg "Найду другого."
    gg "А тебя обреку на вечные страдания."
    play sound head_crush
    hide image blood2
    show image blood3
    with vpunch
    "Генда голыми руками разорвал Константину плечевой сустав."
    gg "И ты будешь молить о том чтобы я тебя добил."
    hide image blood3
    hide image so_sm
    show image so_gd
    show image blood3
    with byso
    gg "Твои дни сочтены.{w=1} Прощай."
    play sound schelk
    hide image so_gd with byso
    "Прорычал он и отошёл от избитого Константина, после чего щёлкнул пальцами."
    stop music fadeout 1.5
    stop ambience fadeout 1.5
    show blink
    "Константин снова уснул."
    pause 1
    hide image blood3
    play ambience ambience_int_cabin_night fadein 1
    scene bg int_house_of_kt_night
    show unblink
    play music nightmare fadein 3
    play sound sfx_bed_squeak1
    "Очутившись в кошмаре он вскочил с кровати.{w} Боль утихла."
    play sound sfx_paper_bag
    "Рены не было рядом.{w=1} На столе лежала записка."
    "На этот раз почерк был другой. Он явно не принадлежал пионеру."
    th "Пионер не объявился. Я пошла до старого корпуса."
    th "Катану можешь не искать - её нет. Жду где и всегда."
    th "М-м-м... Любопытно. Пионера так и нет."
    play sound sfx_paper_bag
    "Константин монотонно промычал и убрал записку в карман."
    "Пистолет был у него и он направился на выход."
    play sound sfx_open_door_1
    play ambience ambience_forest_night fadein 1
    scene bg ext_houses_night with byso
    th "А что если Рена права? Пионер нас оставил."
    stop music fadeout 3
    th "Так, нашёл о чём подумать... Надо бежать!"
    scene bg ext_path2_night with byso
    "Сорвавшись с места, Константин побежал в старый корпус."
    play sound monster_sfx volume 0.6
    play sound2 krik volume 0.4
    play music deadrazy4 fadein 2
    "Выбрав лесную дорогу, Константин, судя по звукам, миновал одну гончую."
    "Ему не сильно хотелось задерживаться в кошмаре, потому он прибавил темп."
    scene bg ext_old_building_night_moonlight:
        crop (497, 223, 980, 630)
        size (1920, 1080)
    show image monster
    with byso
    play sound_loop flesh_feast
    "У старого корпуса он встретил другую гончую, которая жадно грызла чей-то труп."
    "На несколько секунд он позволил себе более длительное рассмотрение существа."
    "Монстр представлял собой сильно искорёженную кучу трупов. Некоторые человеческие кости использовались совершенно с другими функциями."
    "Бедренные мышцы были распределены на плечах, а на ногах наоборот мышцы с плеч."
    "Череп был сильно вытянут и видоизменён.{w} Сразу было видно что бог не прилагал свою заботу к этому существу."
    stop sound_loop fadeout 1
    play sound "<to 1.1>inrealnost/Music/Sound/monster_sfx3.mp3"
    "Гончая его заметила и зарычала."
    kt "Жри патрон, падаль!"
    play sound pistol
    pause 0.4
    play sound2 pistol
    pause 0.4
    play sound3 pistol
    pause 0.4
    play sound pistol
    "Выхватив пистолет, Константин совершил несколько выстрелов."
    "Пара патронов попала в грудь, а один в правую конечность."
    scene bg ext_old_building_night_moonlight:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 1 crop (0, 0, 1920, 1080)
    show image monster
    play sound monster_sfx
    "Монстр взревел и бросился на Константина."
    play sound pistol
    pause 0.4
    play sound2 pistol
    pause 0.4
    play sound3 sfx_click_2
    pause 0.4
    play sound3 sfx_click_2
    "Сделав ещё два выстрела, Константин понял, что у него кончились патроны, а гончая вовсе не спешила останавливаться."
    th "Вот дерьмо!"
    play sound knife_flying volume 2
    pause 1
    hide image monster with fl_scare
    play sound2 sfx_bush_body_fall
    stop music fadeout 3
    "Хотел было Константин спасаться бегством, как в голову прилетел знакомый топор."
    "Гончая рухнула на землю и выдала предсмертный стон."
    play music god fadein 2
    show image re_kind_casual with byso
    "Из старого корпуса вышла Рена и помахала рукой Константину."
    ren "Долго ты. Я вот уже пошла тебе на помощь."
    play sound knife_out
    hide image re_kind_casual
    show image re_smile_casual
    with byso
    "Вытащив топор из головы монстра, Рена его дематериализовала."
    kt "Ты вовремя. Очень вовремя."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Я заметила. Пойдём в корпус."
    scene bg int_old_building_night with byso
    show image re_bored_casual with byso
    "Войдя в старый корпус, Рена указала на люк."
    hide image re_bored_casual
    show image re_bored2_casual
    with byso
    ren "Глянь. Увидишь кое-кого."
    kt "Кое-кого?"
    hide image re_bored2_casual
    show image re_bored_casual
    with byso
    "Она кивнула и тяжело вздохнула."
    ren "Кое-кого."
    play sound sfx_ghost_children_laugh
    scene bg un_dead with fade
    "Константин опустил голову в люк и увидел тело."
    "Это была Лена."
    "Нижняя часть её тела была отрублена, на спине отпечатался след крупного топора, но кисти рук сохранялись."
    "На стене была ещё кровь, больше похожая на битум."
    "По её застывшему лицу было ясно, что она уже не жива, хотя видны следы борьбы за жизнь."
    "На полу было множество мелких брызг крови и кровавых отпечатков её рук."
    scene bg int_old_building_night
    show image re_bored_casual
    with byso
    stop music fadeout 3
    "Константин вытащил голову из люка и посмотрел на Рену."
    kt "У меня два вопроса: <<Зачем ты её убила?>> и <<Откуда она тут?>>."
    hide image re_bored_casual
    show image re_bored2_casual
    with byso
    play music Radar fadein 3
    ren "А я отвечу на два сразу."
    play sound sfx_mystery_movement
    "Выдохнула Рена, присев на пол."
    hide image re_bored2_casual
    show image re_angry_casual
    with byso
    ren "Пионер нас променял на эту Лену."
    ren "Я его тут встретила.{w=1} Они тут шушукались, вот я и подрезала Лену."
    hide image re_angry_casual
    show image re_bored_casual
    with byso
    ren "Но часть их диалога я подслушала."
    ren "Он рассказывал про дальнейший план действий и много нелестных отзывов про нас с тобой."
    ren "Что я успела подслушать - у сопротивления есть флешка, которая позволит снять права бога с Генды."
    kt "Как понять?"
    hide image re_bored_casual
    show image re_smile_casual
    with byso
    "Рена улыбнулась и жестом попросила присесть Константина рядом."
    ren "Так и понимать. Есть административная симуляция."
    "Константин сел рядом и поделился с Реной сигаретой."
    hide image re_smile_casual
    show image re_kind_casual
    with byso
    play sound light_inh
    "Они закурили и Рена кивнула."
    ren "Спасибо."
    ren "Тот алгоритм, который есть у сопротивления, может сделать главного в сопротивлении богом."
    hide image re_kind_casual
    show image re_bored_casual
    with byso
    ren "Всё тут построено на административных правах. У кого они есть - тот бог."
    ren "Как сказал пионер, их можно перехватить и стать богами."
    ren "И только так можно будет покончить с нашим заточением."
    ren "Я думаю, что нам надо будет с завтрашнего дня отправляться в административную симуляцию."
    "Константин задумчиво потёр подбородок и посмотрел на стену."
    kt "Хм-м... И что для этого надо сделать?"
    hide image re_bored_casual
    show image re_bored2_casual
    with byso
    "Рена прокрутила сигарету в руке и указала на люк."
    ren "Убивать."
    ren "Достаточно много убивать."
    kt "Опасная эта затея. Может нам будут давать отпор."
    hide image re_bored2_casual
    show image re_bored_casual
    with byso
    ren "Будут. Но только путники."
    ren "Как я заметила по опыту предыдущих 36 симуляций, пустышки не способны давать отпор. Вообще."
    ren "Они будут бежать и прятаться, но в драку точно не полезут."
    "Он затушил сигарету и повернулся к Рене."
    kt "И сколько нам надо убить?"
    hide image re_bored_casual
    show image re_holod2_casual
    with byso
    "Она наклонила голову и посмотрела в стену."
    ren "От 10 человек до 8 миллиардов."
    "На лице Константина поплыла улыбка."
    "Убийство никогда не казалось ему чем-то ужасным. Наоборот – это был довольно позитивный аспект в жизни."
    hide image re_holod2_casual
    show image re_smile_casual
    with byso
    ren "Я вижу, ты не против?"
    kt "Ты это знаешь..."
    kt "Мир без законов... Без понятий о добре и зле."
    kt "Мир, где каждый волен делать что угодно и с кем угодно. Согласись, идея захватывающая."
    hide image re_smile_casual
    show image re_smile4_casual
    with byso
    ren "Так жить гораздо интереснее, чем в том сером мире, в котором мы все жили, да?"
    hide image re_smile4_casual
    show image re_happy4_casual
    with byso
    play sound glad
    "Константин взял в руку прядь волос Рены и перебрал пальцами. Волосы были мягкими и шелковистыми, приятно холодили руку."
    kt "Это точно."
    kt "Никогда бы не подумал, что найду того, кто действительно меня поймёт и поддержит."
    kt "Того, для кого это не абстрактные слова, а не очень далёкая реальность."
    hide image re_happy4_casual
    show image re_smile3_casual
    with byso
    ren "Того, от чьей поддержки я сама во многом зависима."
    kt "Того, чьё понимание и поддержка являются моим спасением."
    hide image re_smile3_casual
    show image re_happy_casual
    with byso
    ren "И от этого спасенья зависит моя жизнь, я постараюсь сделать его приятным."
    "Они поцеловались."
    "Медленно, мягко, как-то неестественно ласково, словно каждый из них уже давно постиг, что жизни друг без друга не существует."
    hide image re_happy_casual
    show image re_smile2_casual
    with byso
    "Отстранившись, они поглядели друг на друга."
    "Она – нежной улыбкой, он – еле уловимым и ничем не объяснимым блеском в глазах."
    "Это длилось несколько секунд."
    kt "Нам надо выбираться из кошмара."
    hide image re_smile2_casual
    show image re_bored_casual
    with byso
    ren "Надо..."
    play sound ammo volume 0.3
    "Выдохнула Рена и подобрала длинный осколок стекла с пола."
    "Приложив его к горлу, она посмотрела на Константина."
    hide image re_bored_casual
    show image re_kind_casual
    with byso
    ren "Увидимся утром, любимый."
    play sound sfx_pat_shoulder_hard
    hide image re_kind_casual
    show image re_guilty_casual at center:
        zoom 1.25
        yanchor 0.1
    with vpunch
    "Константин схватил её за руку."
    kt "Подожди. Не надо."
    ren "Что такое?"
    hide image re_guilty_casual
    show image re_guilty_casual
    with byso
    play sound wood_hit_head volume 0.7
    "Он подошёл к лестнице и снял ступеньку."
    kt "Я не хочу видеть, как ты убиваешь себя. В буквальном смысле."
    play sound sfx_wood_floor_squeak
    "Достав зелёный ящик, он попробовал оторвать крышку."
    hide image re_guilty_casual
    show image re_sad_casual
    with byso
    ren "Я... Поняла."
    play sound glass_break
    "Осознав, какое зрелище увидел бы Константин, Рена отбросила кусок стекла в сторону."
    hide image re_sad_casual
    show image re_sad2_casual
    with byso
    ren "Прости, я... не подумала..."
    play sound sfx_break_monitor
    pause 0.5
    "Константин швырнул ящик в стену." with vpunch
    hide image re_sad2_casual
    show image re_sad_casual
    with byso
    "Ящик раскололся и его содержимое вывалилось наружу."
    "Константин достал зелёную гранату."
    kt "Не будем шатать друг другу психику."
    play sound sfx_click_3
    "Он выдернул чеку гранаты."
    play sound2 sfx_pat_shoulder_hard
    hide image re_sad_casual
    show image re_kind2_casual at center:
        zoom 1
        linear 0.5 zoom 1.5 yanchor 0.1
    "Рена прыгнула ему в объятия."
    play sound3 bum
    scene bg black with fl_fire
    stop ambience fadeout 3
    stop music fadeout 3
    "Взрыв."
    window hide
    pause 3
    play music dark fadein 1
    scene bg bgcg_d5
    show load
    with dissolve
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt.png" with dissolve
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt1.png" with dissolve
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt2.png" with byso
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt3a.png" with byso
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt4.png" with dissolve
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt5.png" with byso
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt_end2.png" with dissolve5
    pause 10
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt1.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt2.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt3a.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt4.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt5.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt_end2.png"
    hide load
    scene bg black
    with dissolve
    stop music fadeout 2
    pause 1
    jump d5_withre