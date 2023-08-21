label d5_withre:
    $ save_name = ('Инреальность.\nBloody Love.')
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_house_of_kt_night with fl_scare
    play sound3 kontuz volume 1
    play music Radar fadein 3
    "Пронзающая боль пронеслась по всему телу, как удар молнии. Константин вздрогнул и открыл глаза."
    stop sound3 fadeout 2
    "Рена до сих пор спала.{w} На её лице отражался дискофорт."
    th "Вот чёрт...{w=1} Она выжила после взрыва..."
    play sound3 glad volume 1
    "Константин положил руку на её лоб, погладив несколько раз по волосам."
    "Рена, словно прочувствовав прикосновение сквозь сон, выдохнула, а напряжение с её лица пропало."
    kt "Больно же сейчас тебе...{w=1} Бедная..."
    play sound3 sfx_bed_squeak1 volume 1
    "Убрав руку с её головы, Константин встал и постепенно начал одеваться."
    "Только сейчас Константин обратил внимание, что до сих пор ночь."
    th "Хм, странно...{w=1} Уже должно быть светло."
    "Надев джинсы, он попытался найти свой рюкзак."
    "Но его не было на месте..."
    "Там лежала лишь одна пачка честерфилда и записка."
    th "Теперь я понял что тут происходит..."
    play sound3 sfx_paper_bag volume 1
    "Константин достал пачку и записку."
    "Почерк явно принадлежал пионеру.{w} Константин нахмурился."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "Слушай, Константин, далековато ты зашёл.{w}\nЯ не думал, что ты станешь работать с этой психопаткой.{w=1}\nТем более – на её уровне. Где же твоё чувство меры? {w}\nЯ старался тебя вразумить, я даже показывал тебе, что я не вру.{w}\nПочему же ты не последовал моему совету? {w=1}\nСнова.{w}\nЯ предупреждал - ты ввязался в опасную игру. {w}\nРена - не та, кому ты можешь доверять. {w}\nОна может натворить много бед, которые погубят вас всех. {w=1}\nВсех, понимаешь? И тут речь не только про инреальность. {w}\nНеужели я зря на тебя столько времени потратил? Тебе не следует с ней водиться. {w}\nТы должен понять, это не моя прихоть, а настоятельная необходимость. Опасно находиться рядом с человеком, который может убить кого угодно, без какой-либо видимой причины.{w}\nЭто почти неконтролируемо... Беги от неё. Понял? {w}\nЧто-ж. Раз уж так вышло, то мы больше не увидимся. Я забрал все вещи, которые вам дал и нашёл более сговорчивого путника.{w}\nОтныне наши пути расходятся.{w} Счастливо оставаться."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    stop music fadeout 3
    play sound3 sfx_bed_squeak2 volume 1
    show image re_laugh_swim with byso
    "Рена проснулась и с улыбкой посмотрела на Константина."
    ren "Доброе утречко..."
    kt "Я бы сказал: <<С пробуждением>>.{w} Ничего доброго в нашем утре нет."
    hide image re_laugh_swim
    show image re_sad_swim
    with byso
    ren "Что-то случилось?..."
    play music god fadein 3
    play sound3 sfx_bed_squeak2 volume 1
    hide image re_sad_swim
    show image re_sad_swim
    with byso
    "Константин сел к Рене на кровать и посмотрел ей в глаза."
    kt "Пионер забрал у нас все вещи.{w=1} Даже те, что не давал."
    "Она посмотрела в пол и подняла бровь."
    ren "Если я найду эту мразь, то выпотрошу..."
    ren "Ладно катана...{w=1} Но он даже пистолет забрал?"
    "Он утвердительно кивнул и встал с кровати."
    kt "Нам нужно найти новую экипировку."
    play sound3 sfx_bed_squeak1 volume 1
    hide image re_sad_swim with byso
    "Рена молча встала с кровати и начала одеваться."
    ren "Там были наши фотографии..."
    ren "Ублюдок..."
    kt "Слушай, а тебя..."
    ren "Да, меня не убило взрывом."
    ren "По крайней мере сразу...{w=1} Около минуты кровь покидала мой организм..."
    play sound3 light_inh volume 1
    "Протянула Рена, надевая колготки.{w=1} Константин сел на соседнюю кровать и закурил."
    ren "Это было больно..."
    ren "Но больнее то, что я видела тебя...{w=1} Разорванным в клочья."
    show image re_bored_casual with byso
    "Рена надела платье и берет, после чего взялась перевязывать ботинки."
    ren "Моя повышенная живучесть не всегда плюс, как ты понимаешь..."
    kt "Да, пионер говорил про твои физические возможности."
    hide image re_bored_casual
    show image re_holod2_casual
    with byso
    "Она остановилась и подняла взгляд на Константина."
    ren "Что он там снова говорил?"
    kt "О том, что твоя физическая сила превосходит человеческую в 3 раза."
    hide image re_holod2_casual
    show image re_bored_casual
    with byso
    "Поводив взглядом по стене, словно что-то высчитывая, она продолжила завязывать шнурки."
    ren "Да, возможно он и прав.{w} Не знала просто как это выразить математически."
    kt "А внешне ты не похожа на качка тяжеловеса."
    hide image re_bored_casual
    show image re_grin_casual
    with byso
    "Рена ухмыльнулась и напрягла бицепс."
    ren "Есть такое.{w} Пример выражения, что внешность обманчива."
    play sound3 sfx_bed_squeak2 volume 1
    "Встав с кровати, она подошла к Константину."
    ren "Ну что, начнём?"
    kt "Какой план?"
    hide image re_grin_casual
    show image re_cr_smile3_casual
    with byso
    ren "Очень простой.{w=1} Мы устраиваем скотобойню."
    ren "Убить от 2 до 10 свиней и мы откроем порталы."
    ren "А там мы уже найдём того, кто подскажет как попасть в административную симуляцию."
    hide image re_cr_smile3_casual
    show image re_cr_smile_casual
    with byso
    "Рена протянула ему руку."
    ren "Будет весело."
    play sound3 sfx_punch_medium volume 0.51
    "Константин улыбнулся, взял её за руку и встал."
    kt "Теперь я отвечу на свой давний вопрос - каково это."
    stop music fadeout 3
    play sound3 sfx_knock_door3_dull volume 1
    "Раздался стук в дверь."
    "Медленный, неторопливый.{w=1} Словно тот, кто стучал был в стельку пьян."
    hide image re_cr_smile_casual
    show image re_cr_smile2_casual
    with byso
    ren "А вот и первый по очереди.{w} С него и начнём."
    play sound door_break volume 1
    play music "<from 27 to 185>inrealnost/Music/Music/deadrazy4.mp3"
    hide image re_cr_smile2_casual
    show image re_holod2_casual at cright
    show image monster at left
    with vpunch
    "Дверь вылетела и в дверном проёме оказалась гончая."
    play sound2 monster volume 1
    play sound3 sfx_mystery_movement volume 1
    "Монстр своим ужасным взглядом окинул помещение и зарычал, пытаясь пролезть в узкий дверной проём."
    "Из-за объёмной туши это не выходило."
    ren "Что?{w=1} Гончие?"
    kt "Походу пионер оставил нам прощальный подарок в виде вспышки патогена."
    "Гончая застряла в дверях."
    hide image re_holod2_casual
    show image re_cr_smile2_casual at cright
    with byso
    ren "Люди-гончие...{w=1} Какая нахрен разница?..."
    play sound3 sfx_armature_swish volume 1
    hide image re_cr_smile2_casual
    show image re_normal_casual_topor at cright
    with byso
    "В её руках образовался топор, который она прокрутила в руке."
    hide image re_normal_casual_topor
    show image re_smile_casual_topor at cright
    with byso
    ren "Начнём же утреннюю зарядку."
    play sound2 head_crush2 volume 1
    play sound monster_sfx5 volume 1
    hide image re_smile_casual_topor
    show image re_smile_casual_topor
    with vpunch
    "Подпрыгнув к монстру, Рена попала ему чётко в череп, заставив взреветь от боли."
    play sound3 sfx_mystery_movement volume 1
    "Монстр пошатнулся, но не умер.{w=1} Теперь все свои усилия гончая старалась перевести на выход из помещения."
    play sound3 knife_out volume 1
    "Рена вынула топор из головы гончей, отчего последняя высвободилась из ловушки и начала попытки к побегу."
    ren "Добыча уходит.{w=1} Идём!"
    play ambience ambience_camp_center_night volume 1 fadein 1
    scene bg ext_houses_night
    show image re_smile_casual_topor
    with byso
    "Выйдя за монстром, Рена замахнулась."
    play sound knife_flying volume 1
    pause 0.8
    hide image re_smile_casual_topor
    show image re_cr_smile_casual
    with fl_scare
    play sound3 sfx_bush_body_fall volume 1
    "Топор, который она метнула в монстра отрубил одну из конечностей, чем добил монстра."
    "Гончая упала и, судя по всему, умерла."
    play sound3 knife_out volume 0.71
    hide image re_cr_smile_casual
    show image re_smile_casual
    with byso
    "Рена выдернула топор из гончей и обернулась к Константину."
    "Константин ошеломлённо покачал головой."
    kt "Сильно."
    ren "Спасибо-спасибо.{w=1} Это мы только начинаем."
    play sound3 pistol volume 0.7
    play sound magic volume 0.81
    "С площади послышалась стрельба."
    hide image re_smile_casual
    show image re_cr_smile_casual
    with byso
    ren "А сейчас мы найдём тебе оружие."
    kt "На площадь?"
    ren "Да, только будь осторожен.{w=1} Ты безоружен, не лезь на рожон."
    kt "Хорошо."
    scene bg ext_square_night_blood
    show image re_bored_casual
    with byso
    "На площади всё уже было в крови."
    hide image re_bored_casual
    scene bg ext_square_night_blood:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 1 crop (497, 223, 980, 630)
    pause 1
    show image liz_rage at fleft
    show image oleg_angry at cleft
    with byso
    show image poter_r at cright
    show un scared pioneer at fright
    with byso
    "Среди всего этого было видно Женю, мужчину крепкого телосложения и пионера с Леной."
    play sound3 pistol volume 1
    play sound magic volume 1
    "Константин и Рена сели в кусты и стали наблюдать за происходящим."
    play sound2 pistol volume 1
    ren "А вот от кого мы и возьмём снаряжение."
    play sound3 sfx_pat_shoulder_hard volume 1
    "Константин остановил Рену, взяв за запястье."
    kt "Не торопись.{w=1} Я хочу понять, что у них тут происходит."
    ren "Как скажешь.{w} Порталы ещё не открыты, торопиться нам некуда."
    play sound3 pistol volume 1
    "Пожала плечами Рена и, достав топор, села на корточки."
    olegm "Отдай нам Лену и вопрос будет закрыт!"
    play sound3 magic volume 1
    "Мужчина пальнул по пионеру из своего орудия, но промахнулся."
    pp "Чёрта с два!{w=1} Катитесь нахуй отсюда на своём автобусе!"
    play sound3 magic volume 1
    mz "Никуда мы не покатимся без Лены!"
    th "Автобус?{w=1} О чём они?"
    show un angry pioneer with byso
    un "Это моё дело с кем я и куда поеду!"
    play sound3 magic volume 1
    hide image oleg_angry
    hide image liz_rage
    show image liz_bukal at fleft
    show image oleg_angry at cleft
    "Пионер выстрелил плазмой в Женю, но попал в пистолет, который она держала в руках."
    pp "Уёбывайте по-хорошему!{w} Иначе я вас обоих распылю нахуй!"
    olegm "Это мы тебя распылим!"
    play sound3 magic volume 1
    hide image poter_r with vpunch
    "Выстрел."
    "Мужчина попал по пионеру, отчего тот скрючился."
    th "А он не такой бессмертный как могло показаться..."
    play sound3 power volume 1
    scene bg ext_square_night_blood_red:
        crop (497, 223, 980, 630)
        size (1920, 1080)
    show image liz_bukal at fleft
    show image oleg_angry at cleft
    show un angry pioneer
    with byso
    "Открылись порталы."
    play sound2 portal volume 1
    hide un with byso
    pause 1
    hide image oleg_angry
    show image oleg_think at cleft
    hide image liz_bukal
    show image liz_angry at fleft
    with byso
    "Лена запрыгнула в центральный портал, а пионер за ней."
    mz "Чёрт!{w=1} Свалили!{w} Олег, за ними!"
    hide image oleg_think
    show image oleg_angry at cleft
    with byso
    oleg "Лиза, не неси чушь!{w=1} У нас автобус в этой симуляции!"
    th "Что?{w=1} Её зовут Лиза?"
    hide image liz_angry
    show image liz_rage at fleft
    with byso
    liz "Да?!{w=1} И тебе автобус дороже человеческой жизни?!"
    oleg "Нас капитан отправит под трибунал, если мы автобус просрём!"
    oleg "Я не хочу эту жизнь платить из своего кармана!"
    hide image liz_rage
    hide image oleg_angry
    with byso
    "Лиза прорычала и побежала к выходу из лагеря, а Олег за ней."
    scene bg ext_square_night_blood_red:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 1 crop (0, 0, 1920, 1080)
    with byso
    show image re_cr_smile_casual with byso
    "Константин посмотрел на Рену.{w} Она, подперев голову рукой, молча любовалась Константином."
    kt "Рена?"
    hide image re_cr_smile_casual
    show image re_grin_casual
    with byso
    ren "А?{w=1} Да, прости, в мыслях потерялась."
    kt "Куда нам бежать?"
    hide image re_grin_casual
    show image re_bored_casual
    with byso
    "Она потёрла подбородок и посмотрела в землю, будто стараясь что-то в ней найти."
    ren "3 портала.{w=1} В один пошёл пионер, в другие не пошёл никто."
    ren "Нам нужна экипировка.{w=1} Наша или чужая, не суть важно."
    ren "Мы можем пойти за этой Женей-Лизой, а можем за пионером.{w} Это два наиболее разумных варианта."
    kt "Не могу не согласиться...{w=1} Но куда?"
    play sound3 glad volume 1
    hide image re_bored_casual
    show image re_smile_casual
    with byso
    "Рена погладила Константина по шее и улыбнулась."
    ren "У нас пока что нет чёткого плана действий.{w=1} Выбор за тобой."
    $ renpy.block_rollback()
    window hide
    $ time = 20000
    $ timer_range = 20000
    $ timer_jump = 'no_choise_d5_1_1'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Пойти за пионером.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            kt "Пошли за пионером.{w=1} Надо вернуть нашу экипировку."
            play sound3 monster_sfx volume 1
            hide image re_smile_casual
            show image re_holod2_casual
            with byso
            "Позади раздалось рычание."
            play sound2 knife_flying volume 1
            "Рена метнула топор в источник звука, чем убила крадущуюся гончую."
            hide image re_holod2_casual
            show image re_holod_casual
            with byso
            ren "В темпе.{w=1} Тут уж слишком много зверья развелось."
            play sound3 knife_out volume 1
            hide image re_holod_casual
            show image re_holod2_casual
            with byso
            "Забрав топор, они побежали в портал."
            scene bg black with byso
            play sound3 portal volume 1
            stop music fadeout 1
            stop ambience fadeout 1
            "В портале их обвила стопроцентная пустота."
            play music ElfenLied fadein 3
            scene bg kt_room
            show shum_white
            with byso
            "Константин въехал в новую квартиру.{w=1} Кругом была пыль, грязь, какие-то коробки из-под обуви и вообще беспорядок."
            th "М-да...{w=1} А я словно ожидал чистую квартиру, евроремонт."
            "Закатив чемодан в угол, он поставил туда же бутылку пива, открыл шкаф и начал переодеваться.{w=1} На нем была черная майка, джинсы, кроссовки, а на плече висел старый рюкзак."
            th "Скорее всего, надо будет самостоятельно заняться ремонтом...{w=1} А ещё побриться..."
            "Размышлял он, поглядывая в зеркало, на свое бледное, заросшее щетиной лицо."
            "Атмосфера в дедушкиной квартире была довольно мрачной.{w=1} Едва пахло кофе и лекарствами."
            "Он достал телефон и посмотрел на часы.{w=1} Десять минут двенадцатого."
            "На его заставке была изображена рыжая девочка, приветливо улыбающаяся, глядя на созерцателя."
            th "Рена...{w=1} Ну хоть теперь у меня будет хоть немного времени на форсинг."
            "Девочку Константин придумал сам.{w=1} Во всех деталях и мелочах, которые только можно было представить."
            "Из них - рыжие короткие волосы, голубые глаза и белый беретик, плотно прилегающий к голове."
            th "Если вселенных бесконечное множество, то, может быть, вероятность нашей встречи не равна нулю? Хотя как?"
            "Я бы сказал, что мы одно целое, часть некоего множества, замкнутое в себе."
            "Так, ладно, надо разбирать вещи."
            stop music fadeout 1.5
            scene bg black with byso
            pause 1
            play music stresss fadein 3
            pp "Блять, я еще раз тебя спрашиваю, какого чёрта вы тут забыли?!"
            ren "Вы украли нашу экипировку и, если вы её сейчас не вернёте, я намотаю кишки твой спутницы на кулак!"
            scene bg int_house_of_kt_day
            show image poter_r
            show image re_holod2_casual at fleft
            show un cry pioneer at left
            play ambience ambience_int_cabin_day volume 1 fadein 1
            show unblink
            "Константин открыл глаза и встретил необычную картину."
            "Пионер держал руку направленной в его сторону, а Рена удерживала Лену с топором у шеи."
            pp "О, и ты проснулся! Какого хуя вы за нами попёрлись?!"
            kt "Рена тебе уже всё сказала."
            hide image re_holod2_casual
            show image re_rage_casual at fleft
            hide un
            show un cry pioneer at left
            with byso
            ren "Экипировку на базу!"
            pp "Отпусти Лену и тогда мы уже мы всё нормально обсудим!"
            hide image re_rage_casual
            show image re_holod2_casual at fleft
            hide un
            show un cry pioneer at left
            with byso
            ren "Только без фокусов."
            play sound3 sfx_punch_medium volume 1
            hide image re_holod2_casual
            show image re_holod2_casual at left
            hide un
            show un sad pioneer at right
            with byso
            "Рена отпустила Лену и та отпрыгнула на метр."
            pp "Вот теперь мы поговорим."
            play sound3 magic volume 1
            play music the_date_of_death fadein 3
            hide image re_holod2_casual
            show image re_guilty_casual at left
            hide image poter_r
            show image poter_n
            with fl_scare
            "Пионер выпустил заряд плазмы в Константина."
            "Его тело начало постепенно рассыпаться."
            ren "Костя?!"
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            scene bg black with byso
            window hide dissolve
            $ unlock_ach_root_inreal(2)
            play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
            scene bg ending_dead_cg:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            show ending_dead:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            with Dissolve(15)
            scene bg black with byso
            pause 1
            stop sound
            jump after_ending_screen
        "Пойти за Лизой и Олегом.":
            hide screen inreal_countdown
            stop sound3 fadeout 1
            $ renpy.block_rollback()
            jump hvbuidfhvudf8ishvbu9isvbfuiodhvbjiofdjvbjodfj
label no_choise_d5_1_1:
    $ renpy.block_rollback()
    stop sound3 fadeout 1
    play sound2 monster_sfx3 volume 1
    hide image re_smile_casual
    show image re_holod2_casual
    with byso
    "Позади раздалось рычание.{w=0.5}{nw}"
    play sound head_crush volume 1
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    scene bg black with vpunch
    "Пока они были в укрытии, их нашла гончая и проткнула Константина."
    window hide dissolve
    $ unlock_ach_root_inreal(2)
    play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
    scene bg ending_dead_cg:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    show ending_dead:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    with Dissolve(15)
    scene bg black with byso
    pause 1
    stop sound
    jump after_ending_screen
label hvbuidfhvudf8ishvbu9isvbfuiodhvbjiofdjvbjodfj:
    kt "Пошли за этими двумя.{w=1} За пионером топтаться не стоит."
    ren "Да, ты наверное прав.{w} Я же даже не смогу его убить..."
    play sound3 monster_sfx volume 1
    hide image re_smile_casual
    show image re_holod2_casual
    with byso
    "Позади раздалось рычание."
    play sound2 knife_flying volume 1
    "Рена метнула топор в источник звука, чем убила крадущуюся гончую."
    hide image re_holod2_casual
    show image re_holod_casual
    with byso
    ren "В темпе.{w=1} Тут уж слишком много зверья развелось."
    play sound3 knife_out volume 1
    hide image re_holod_casual
    show image re_holod2_casual
    with byso
    "Забрав топор, они побежали к выходу из лагеря."
    kt "А что если у них нет ничерта?"
    hide image re_holod2_casual
    show image re_grin_casual
    with byso
    ren "У них как минимум есть автобус."
    stop music fadeout 3
    scene bg ext_camp_entrance_night_red
    show image liz_angry
    with fade
    hide image liz_angry with byso
    "У ворот лагеря стоял автобус, в который забежала Лиза."
    liz "Едем на базу!"
    play sound3 korobka_peredach volume 1
    play music AshXyrah fadein 3
    scene bg int_avtobus3
    show image re_grin_casual
    show image oleg_shy at right
    show image liz_bukal at left
    with byso
    play sound3 sfx_ikarus_open_doors volume 1
    play ambience bus_inside volume 0.2 fadein 1
    "Константин и Рена влетели в автобус прямо перед самим закрытием дверей."
    ren "Уезжать?{w=1} И без нас?"
    scene bg int_avtobus3
    show image re_grin_casual
    show image oleg_think at right
    show image liz_dontlike at left
    with byso
    "Автомобиль начал своё движение, а Олег и Лиза обратили внимание на безбилетников."
    hide image oleg_think
    show image oleg_angry at right
    hide image liz_dontlike
    show image liz_angry at left
    with byso
    oleg "А вы какого чёрта тут делаете?!"
    play sound3 sfx_armature_swish volume 1
    ren "Мы попуткой."
    hide image re_grin_casual
    show image re_smile_casual_topor
    with byso
    "В руках Рены образовался топор."
    ren "Точнее...{w=1} Мы просто изымаем у вас это чудо техники.{w} Рекомендую отдать без боя."
    hide image liz_angrya
    show image liz_rage at left
    with byso
    liz "Хрена с два!"
    ren "Ваш выбор."
    play sound3 sfx_pat_shoulder_hard volume 1
    scene bg int_avtobus3
    show image liz_rage at center:
        zoom 1.25
        yanchor 0.05
    with vpunch
    "Лиза набросилась на Константина с кулаками."
    play sound sfx_punch_medium volume 1
    "Один из ударов попал в плечо, но был достаточно слабым."
    play sound2 sfx_armature_swish volume 1
    pause 0.6
    scene bg int_avtobus3 with vpunch
    play sound2 sfx_lena_hits_alisa volume 1
    "Он без особой сложности парировал остальные удары и зарядил Лизе в живот."
    "Она упала на пол и скрючилась от боли, протяжно постанывая себе под нос.{w=1} Удар, судя по всему, был очень болезненный."
    scene bg int_avtobus2 with byso
    liz "Блять..."
    play sound3 slash volume 1
    "Позади раздался чёткий разрубающий звук."
    ren "Умник!{w=1} Кто будет стрелять в ближнем бою?"
    liz "Ол...{w=0.51} Олег?!"
    ren "Подожди, сейчас принесу."
    play sound3 sfx_bodyfall_1 volume 1
    scene bg corpse with vpunch
    "Рена подошла к Лизе и швырнула к ней свежесрубленную голову мужика."
    ren "Олег тебя внимательно слушает."
    play sound "<from 0 to 4>inrealnost/Music/Sound/fem_screams.mp3"
    "Лизе не потребовалось много времени на осознание ситуации. {w=1}Она начала истошно кричать."
    scene bg int_avtobus2
    show image re_cr_smile_casual
    with byso
    "Её вопль был настолько громким, что, казалось, стёкла в автобусе треснут."
    liz "Олег!!!{w=1} Почему?!"
    liz "За что?!"
    liz "Что мы вам сделали?!{w=1} За что?!"
    kt "Ответ встали на пути подойдёт?"
    hide image re_cr_smile_casual
    show image re_smile_casual
    with byso
    ren "Весьма, Кость.{w=1} Можно ещё про цианид напомнить. {w}Так, а теперь к делу."
    liz "Вы, бесчеловечные ублюдки!{w=1} За что вы?..."
    play sound3 sfx_pat_shoulder_hard volume 1
    play sound sfx_mystery_movement
    hide image re_smile_casual
    show image re_cr_smile2_casual
    with byso
    "Рена взяла Лизу за волосы и поволокла к водительскому месту."
    ren "Много говоришь не на тему."
    liz "Не трогай меня, убийца!!!{w=1} Куда ты меня тащишь?!"
    "Константин прошёл к водительскому месту и посмотрел на обезглавленное тело Олега, а затем на дверь."
    play sound3 sfx_put_sugar_cart volume 1
    hide image re_cr_smile2_casual
    show image re_cr_smile_casual
    with byso
    "Рена усадила Лизу на водительское сидение и махнула рукой в сторону приборной панели."
    liz "Не буду я вам ничего говорить!!!"
    hide image re_cr_smile_casual
    show image re_bored_casual
    with byso
    ren "Слушай, тебе настолько хочется поговорить с этим чуваком? {w=1}Могу организовать вашу личную встречу."
    kt "Ты лучше говори, с Реной шутить не стоит.{w=1} Как открыть дверь?"
    liz "Ничего я не...{w=0.45}{nw}"
    play sound3 sfx_punch_washstand volume 1
    play sound sfx_bus_honk volume 1
    hide image re_bored_casual
    show image re_holod2_casual
    with vpunch
    "Рена схватила Лизу за волосы и ударила головой об руль."
    "После этого она примотала её к сидению ремнём безопасности."
    th "Оригинально..."
    ren "Слушай, ты.{w=1} У тебя ещё есть шансы остаться в живых. {w}{cps=9}Пока что.{/cps}"
    ren "Ты сейчас учишь нас как пользоваться этой штукой, а мы тебя оставляем в живых."
    ren "Либо я размажу твою башку.{w=1} Какой вариант больше по душе?"
    "Сквозь боль и слёзы Лиза улыбнулась."
    liz "Да вы едете на базу сопротивления!{w=1} В разг-гар подготовки к нападению!"
    liz "Там то в-вас и научат жизни..."
    kt "До меня дошло.{w=1} Ты <<Дзетта>>?"
    liz "Ничего я тебе не скажу, тварь..."
    play sound3 sfx_pat_shoulder_hard volume 1
    hide image re_holod2_casual
    show image re_cr_smile3_casual
    with byso
    "Рена за шею прижала её к сидению и начала душить."
    ren "Скажешь, когда будешь готова что-то сказать?"
    "Константин фыркнул и помотал головой."
    kt "Откуда же в тебе столько наглости то?"
    th "Хотя скорее тут просто недостаток воли к жизни."
    kt "Острый предмет принести?"
    hide image re_cr_smile3_casual
    show image re_grin_casual
    with byso
    ren "Я сама.{w=1} Не утруждайся."
    play sound3 glass_break2 volume 1
    "Она разбила головой Лизы стекло." with vpunch
    play sound "<from 6 to 10>inrealnost/Music/Sound/fem_screams.mp3"
    "Твёрдое автомобильное стекло раскололось и нанесло лицу Лизы множество маленьких ранок."
    hide image re_grin_casual
    show image re_cr_smile3_casual
    with byso
    play sound3 sfx_mystery_movement volume 1
    "Она начала кричать и пытаться ударить Рену, но без толку."
    ren "Да, воли повыделываться в тебе даже слишком много.{w=1} Может будешь говорить?"
    liz "Н-ничего не скажу!"
    play sound3 sfx_punch_washstand volume 1
    hide image re_cr_smile3_casual
    show image re_cr_smile_casual
    with byso
    "Рена совершила сильный удар в солнечное сплетение.{w=1} Лиза перестала кричать и начала задыхаться."
    ren "Я могу это делать весь день.{w=1}.. Или как это тут...{w=1} Цикл.{w} Советую подчиниться."
    kt "М-да..."
    scene bg priborka with byso
    "Константин подошёл к приборной панели, после чего начал её изучать, разглядывая экраны и кнопки."
    stop music fadeout 3
    scene bg black with byso
    pause 2
    scene bg priborka with fade
    play music tish fadein 3
    play sound3 sfx_punch_washstand volume 1
    play sound2 perelom volume 1
    "Судя по звукам, Рена сломала Лизе нос." with vpunch
    "Прошло уже достаточно много времени. На Лизе уже не осталось живого места."
    ren "Хм-м...{w} Мне начинает казаться, что тебе нравится когда тебя бьют."
    ren "Это связано с родителями?"
    liz "Н-не смей про них!..."
    play sound3 head_crush volume 0.51
    play sound "<from 11.5 to 14>inrealnost/Music/Sound/fem_screams.mp3"
    "Рена оторвала клок волос с головы Лизы.{w=1} Автобус содрогнулся от визга."
    ren "Я тут решаю что ты будешь говорить, а что нет."
    "Библиотекарша постаралась рукой прикрыть рану, но не могла, поскольку была зафиксирована."
    "Рена взяла её кисть и загнула палец."
    play sound3 perelom volume 1
    ren "Любит."
    play sound3 perelom volume 1.2
    ren "Не любит."
    "Словно срывая лепестки с цветка, Рена ломала пальцы на руке Лизы."
    play sound3 perelom volume 0.9
    ren "Любит."
    play sound3 perelom volume 1.2
    ren "Не любит."
    play sound3 perelom volume 1.5
    ren "Любит!"
    ren "Костя, ты же меня любишь?"
    kt "Люблю-люблю.{w=1} Не отвлекайся, нам ещё нужна информация от неё."
    ren "Слышишь?{w=1} Ну что, давай вторую руку."
    play sound3 sfx_mystery_movement volume 1
    "Лиза пыталась отстраниться от Рены, но некуда."
    play sound3 sfx_pat_shoulder_hard volume 1
    "Рена выхватила руку Лизы и снова взялась за её мизинец."
    play sound3 perelom volume 1
    ren "Любит."
    "Было видно, что пытка не проходит даром.{w} Судя по виду Лизы, она с каждым сломанным пальцем становилась всё сговорчивее."
    play sound3 perelom volume 1.2
    ren "Не любит."
    play sound3 perelom volume 0.9
    ren "Любит."
    liz "Хватит!"
    "Взревела она, после чего опустила голову."
    liz "Я всё скажу!"
    ren "Отлично."
    play sound3 sfx_blanket_off2 volume 1
    "Рена её развязала, а Константин пропустил едва живую Лизу к приборной панели."
    ren "Мы слушаем."
    liz "С-с-сейчас..."
    play sound3 sfx_click_1 volume 1
    pause 0.2
    play sound2 sfx_click_1 volume 1
    "Последними двумя пальцами она начала нажимать какие-то из кнопок."
    th "Что она делает?..."
    "Он внимательно следил за каждым её действием."
    play sound3 wood_hit_head volume 1
    "Рена взяла Лизу за волосы и впечатала в торпеду." with vpunch
    ren "Поясняй каждое своё действие.{w=1} Если тебе ещё нужен скальп."
    liz "Х-хорошо."
    liz "Д-для управления авт-тобусом над-до задать сим-муляцию, в которую н-надо поехать..."
    ren "Не мямли!{w=1} Ничерта не понятно!"
    play sound3 sfx_click_2 volume 1
    "По щеке Лизы потекла слеза и она, глянув на мёртвого Олега, нажала на большую зелёную кнопку."
    play music "<from 57.5>inrealnost/Music/Music/DEVIL.mp3"
    play sound_loop sirenn volume 1.25
    show priborka_ping with vpunch
    gt5 "Подтверждение получено.{w=1} Протокол <<Безбожник>> активирован."
    kt "Ты что сделала?!"
    gt5 "Остановка в ближайшей симуляции.{w=1} Тотальная дестабилизация трансформатора через 15 секунд."
    play sound sfx_pat_shoulder_hard volume 1
    "Рена снова схватила Лизу за волосы."
    ren "Выключай живо!"
    liz "Поцелуй меня в задницу..."
    play sound3 head_crush volume 1
    play sound2 sfx_bush_body_fall volume 1
    "Она содрала с Лизы скальп и толкнула её на землю."
    play sound "<to 0.7>inrealnost/Music/Sound/head_crush4.mp3"
    "Оголив череп библиотекарши, она раздавила его ударом ноги."
    gt5 "Пять."
    ren "Костя, быстро в конец автобуса!"
    gt5 "Три."
    "Константин и Рена укрылись за дальними сидениями."
    gt5 "Два."
    kt "Рена, держись крепче!"
    gt5 "Один."
    ren "Я то держусь!"
    gt5 "Ноль."
    stop ambience
    stop sound_loop
    play sound3 sfx_nightmare_explosion volume 1
    scene bg explosion with fl_fire
    "Взрыв."
    play sound2 bus_inc volume 1
    "Автобус подлетел на открытом поле и перевернулся."
    "Константина и Рену выбросило из окна."
    "В полёте Константин заметил, как автобус влетел в ЛЭП и тем самым разлетелся на части."
    stop music fadeout 0.5
    play sound3 sfx_bush_body_fall volume 1
    play sound kontuz
    scene bg black with vpunch
    "По приземлению Константин потерял сознание."
    stop sound fadeout 1
    pause 2
    play music ElfenLied fadein 3
    scene bg kt_room
    show shum_white
    with byso
    "Разбирая вещи по квартире, Константин нашёл в шкафу старый дедовский карабин."
    "В нём самом не было патронов, но была коробка со стреловидными патронами."
    "Он хорошо помнил, как в детстве ходил с дедушкой на охоту."
    th "Трофей...{w=1} Артефакт, напоминающий о прошлом."
    th "Интересно, почему же дедушка хранит его тут, а не на даче."
    th "Неужели он думал, что на него кто-нибудь позариться?"
    th "Надо будет отнести к мастеру, отремонтировать..."
    "Отложив найденный предмет, он продолжил раскладывать одежду."
    "Свитер, джинсы, свитер, брюки, куртка, рубашки, носки.{w} Паспорт, бумажник, ключи, мелочь."
    th "Всё по местам."
    th "Пойти выпить пивка чтоль?{w=1} Только это я и хотел сделать с самого утра."
    "Взяв бутылку, он сел на старый офисный стул, который деду подарил отец."
    "Откупорив хмельное, он сделал пару глотков и посмотрел в окно."
    th "Новые виды из окна."
    th "Не ново, зато бесплатно."
    th "Старые не интересны, потому что уже совсем надоели."
    th "А вот интересно, как я докатился до жизни такой?{w=1} Как всё это случилось?"
    th "Что я люблю?{w=1} Почему? {w=1}Непонятно."
    th "ВУЗ-дом-ВУЗ-дом...{w=1} Именно так пройдёт вся жизнь."
    th "Быстро, никаких перемен."
    th "Ни друзей, девушки, да даже работы."
    th "Никаких связей, ни планов.{w} Чего я хотел?{w=1} Куда мне ещё?"
    th "Да, точно, надо будет найти подработку на выходные."
    "Константин достал телефон и посмотрел на рыжую девочку у себя на заставке."
    "Рыжие короткие волосы, голубые глаза и белый беретик, плотно прилегающий к голове."
    "Надев наушники, нажал <<Play>> и стал вслушиваться в мелодию, которую уже знал наизусть."
    stop music fadeout 2
    scene bg black with byso
    pause 2
    play ambience ambience_int_cabin_night volume 1 fadein 1
    play sound3 glad volume 1
    "Константин почувствовал, как кто-то коснулся его головы."
    scene bg int_aidpost_lamp
    play music interlude fadein 3
    show image re_sad_casual
    show unblink
    "Как только он отрыл глаза, то увидел Рену, сидящую рядом и гладящую его по голове."
    "Находились они в медпункте под светом настольной лампы."
    hide image re_sad_casual
    show image re_grin_casual
    with byso
    ren "Проснулся!{w=1} Доброго утречка.{w=1} Ты в порядке?"
    kt "Так себе.{w=1} Вообще так себе..."
    kt "Голова болит до ужаса."
    play sound3 glad volume 1
    hide image re_grin_casual
    show image re_bored2_casual
    with byso
    "Рена пару раз кивнула и подложила подушку ему под голову."
    ren "У тебя скорее всего было сотрясение. {w}Ещё порезы по всему телу, но я их уже обработала, не беспокойся."
    ren "Автобус подорвался у ЛЭПов и я тебя сюда принесла."
    ren "Мы отделались лёгкими травмами.{w=1} Всё могло быть куда хуже."
    kt "Ты то как?"
    hide image re_bored2_casual
    show image re_smile3_casual
    with byso
    ren "Я в порядке. {w}Пришлось, правда, украсть новые колготки."
    hide image re_smile3_casual
    show image re_grin_casual
    with byso
    "Она подняла ногу, дабы показать награбленное."
    "Её сапог был испачкан кровью."
    ren "Вот, смотри, ничем не отличаются."
    kt "Да, есть такое.{w=1} А кровь чья?"
    hide image re_grin_casual
    show image re_bored2_casual
    with byso
    ren "Лизы.{w=1} Уже присохла, надо будет отмыть."
    play sound3 sfx_bed_squeak2 volume 1
    pause 1
    hide image re_bored2_casual
    show image re_grin_casual
    with byso
    play sound3 sfx_pat_shoulder_hard volume 1
    "Константин попытался встать, но Рена не дала это ему сделать."
    ren "Тихо-тихо.{w=1} Лежи пока что.{w} Не торопись."
    ren "У нас всё время мира, как говорится.{w=1} Тут либо никого нет, либо все спят."
    ren "Сначала убедись, что у тебя не осталось симптомов, а потом уже пойдём."
    kt "Хорошо, как скажешь, доктор."
    scene bg re_lay with byso
    play sound3 sfx_bed_squeak1 volume 1
    "Рена улыбнулась и легла рядом."
    ren "А всё-таки.{w=1} Инреальность или родной мир?"
    kt "Мы же вчера об этом говорили."
    ren "При этом так и не определились.{w=1} Я бы хотела в реальный мир."
    kt "Может всё-таки остаться тут?{w} Безграничные возможности, решение парадокса бога."
    "Взяв его за руку, она улыбнулась."
    ren "А у меня есть другая идея."
    ren "Доказать всему человечеству, что даже в полном хаосе мысли можно говорить о чем-то прекрасном, есть одна-единственная грань, связующая эту странную красоту с хаосом."
    ren "А если проще, то, что выйти на верхнюю стадию эволюции можно из любого состояния."
    kt "Интересно, а как ты себе это представляешь?"
    "Константин выдохнул, думая, как она ответит на этот вопрос."
    kt "Да и вообще, я уже не в том возрасте, чтобы с боем что-то доказывать."
    ren "Ну или доказать всё себе."
    "Она нежно сжала его руку, повернув ладонью вверх."
    ren "Иногда у меня в голове мелькала одна идея - мы с тобой возьмём мир и всё покорим."
    ren "Сделаем так, чтоб мир играл по нашим правилам, а не наоборот."
    "Он хмыкнул и улыбнулся."
    kt "Ты хочешь устроить войны?"
    ren "Вовсе нет, войн я и сама хотела бы избежать, если есть такая возможность.{w=1} Не будем брать во внимание то, что мы делаем сейчас - другого выхода нет."
    ren "Мы просто воспользуемся тем, чем обладаем, и создадим, как бы, новый мир."
    "Константин ухмыльнулся и облизнул губы."
    kt "Создам из плоти новый мир?"
    ren "Хах, точно."
    ren "Этот мир, где мы с тобой вдвоём..."
    ren "Вот есть у меня философский вопрос."
    ren "Имеет ли жизнь смысл, когда тебе нечего ценить?"
    "Он выдохнул и помотал головой."
    kt "Нет в этом вопросе ничего философского."
    kt "Бессмысленно стремиться к тому, чего нет."
    kt "Каждый раз, просыпаясь, констатируешь, что жизнь прошла зря и ничего не сохранилось. {w=1}При том и не появится."
    ren "Да, я тоже так думаю."
    "Рена нежно улыбнулась и откинула назад пряди волос, упавшие ей на лицо."
    ren "Я это спрашивала потому, что я на самом деле очень боюсь тебя потерять."
    "Константин призрачно улыбнулся и опустил взгляд на её плечи."
    ren "Мне всегда было больно смотреть, как ты страдал и я искренне хочу твоего счастья.{w=1} Только так, и никак иначе."
    ren "Ты очень старался, продумывая мой образ, старался воплотить меня в свою реальность."
    "Она прогладила его шею, дойдя до щеки, на которой уже нарастала щетина."
    ren "И теперь...{w=1} Я просто схожу с ума от любви к тебе."
    ren "Мне хочется, чтобы она длилась вечно, и не было ничего, кроме нашего счастья."
    play sound3 glad volume 1
    "Рена провела пальцем по его губам и остановилась на подбородке."
    ren "Каждый миг, проведенный с тобой, становится для меня настоящим праздником."
    ren "Скажи, ты любишь меня так же сильно, как я люблю тебя?"
    kt "Да.{w=1} Я тебя тоже люблю."
    show blink
    "Их губы слились в поцелуе."
    "Рена едва слышно простонала."
    "По телу Константина пробежала дрожь наслаждения."
    "Он ощущал нежность ее губ, ласку ее пальцев, мягкость ее тела."
    "Что-то подсказывало ему, что он держит в своих руках на ощупь хрупкий, почти невесомый сосуд, несмотря на то, что Рена была куда крепче."
    scene bg re_lay
    show unblink
    "Отстранившись друг от друга на 5 сантиметров, они улыбнулись друг другу."
    kt "Ладно, нам надо идти.{w=1} Впереди ещё много всего."
    ren "Мгм...{w=1} Крови и ужаса."
    scene bg int_aidpost_lamp
    show image re_smile_casual
    with byso
    "Протянула Рена, вставая с кровати."
    kt "А что делаем то?"
    play ambience ambience_camp_center_night volume 1 fadein 1
    play sound3 door_cl volume 1
    scene bg ext_aidpost_night
    show image re_smile_casual
    with byso
    play sound3 light_inh volume 1
    "Выйдя из медпункта, Константин закурил и протянул сигарету Рене.{w=1} Осталась последняя закрытая пачка."
    ren "Спасибки.{w=1} Ты же ровно идёшь, всё хорошо?"
    kt "Да, всё нормально.{w} Голова всё ещё болит, но мелочи, а что?"
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Я думаю нам стоит пройтись до автобуса."
    kt "Зачем?"
    play sound3 light_inh volume 1
    hide image re_grin_casual
    show image re_bored2_casual
    with byso
    "Рена размяла пальцы и, закурив, неторопливо провела тыльной стороной ладони по шее."
    ren "Вполне вероятно, что что-то там уцелело.{w=1} Насколько я поняла, у них был с собой груз в багажнике."
    ren "Там был сундук.{w} Судя по всему из огнеупорного материала."
    ren "Думаю стоит проверить что там."
    kt "Раз ты так в этом уверена, то идём."
    hide image re_bored2_casual
    show image re_grin_casual
    with byso
    ren "Отлично.{w=1} Будем надеяться, что там не куча хлама."
    scene bg ext_square_night
    show image re_grin_casual
    with byso
    "Медленным прогулочным шагом они пробирались к выходу из лагеря."
    kt "Мне вот что интересно. {w=1}Почему эта Лиза-Женя так долго сопротивлялась?"
    hide image re_grin_casual
    show image re_smile4_casual
    with byso
    "Рена ухмыльнулась и посмотрела в землю."
    ren "Возможно поняла, что в живых я не планировала её оставлять."
    kt "Ну а что, нам не убудет."
    play sound3 inh volume 1
    hide image re_smile4_casual
    show image re_bored2_casual
    with byso
    "Она тяжело вздохнула и неопределённо покачала головой, затем, сделав затяжку, повернула к нему лицо."
    ren "Ну, знаешь, она хотела кого-то из нас отравить цианидом.{w=1} Я не думаю, что такое поведение должно остаться без внимания."
    ren "Тем более, мир тесен, не хочется получить нож в спину."
    kt "И тут ты права...{w=1} Просто излишне жестоко как по мне."
    ren "Ты сам понимаешь, что люди совершенно не ценят хорошее отношение."
    ren "Что самое мерзкое, некоторые поринимают его как должное."
    ren "Да, может быть некоторые путают доброту со стандартной вежливостью, но у всего есть свои пределы."
    "Прокрутив сигарету в руке, Константин не нашёл чего противопоставить."
    kt "Это я уже понял на примере пионера.{w=1} Не стоит в инреальности лишний раз думать о морали - боком встанет."
    hide image re_bored2_casual
    show image re_grin_casual
    with byso
    ren "Вот видишь, всё просто."
    kt "Мне вот что не ясно, зачем сопротивлению пустышка.{w=1} Пионеру тем более."
    hide image re_grin_casual
    show image re_smile3_casual
    with byso
    "Запустив сигарету в кусты, Рена посмотрела на звёздное небо."
    ren "А та и не пустышка.{w=1} Точнее говоря, пока что."
    ren "Я ещё давно заметила нестыковки в её поведении по сравнению с пустышками."
    kt "Например?"
    hide image re_smile3_casual
    show image re_smile2_casual
    with byso
    ren "Лена-пустышка даже с Женей почти не общается. {w=1}И не читает цену грехов."
    kt "Может это просто совпадение?"
    hide image re_smile2_casual
    show image re_smile4_casual
    with byso
    ren "Ещё, могу напомнить, что она была в кошмаре."
    play sound3 sfx_clench2 volume 0.5
    "Константин ударил себя по лбу."
    kt "Точно...{w=1} Ну, тогда да, это неопровержимое доказательство."
    hide image re_smile4_casual
    show image re_grin_casual
    with byso
    "Рена улыбнулась и взяла Константина под руку."
    scene bg ext_clubs_night
    show image re_grin_casual
    with byso
    ren "Я вижу людей насквозь."
    ren "Можно сказать, это моя работа – их видеть."
    ren "Потому, если тебе не понятно с кем мы имеем дело, я могу объяснить."
    hide image re_grin_casual
    show image re_smile3_casual
    with byso
    ren "Будь то ученый, ребенок, старик, президент или просто обычный человек, знающий что-то об инреальности."
    "Константин улыбнулся и помотал головой."
    kt "Да, ты уже прочитала, что было в голове Жени-Лизы.{w=1} Она чуть нас с собой на тот свет не отправила."
    hide image re_smile3_casual
    show image re_angry_casual
    with byso
    "Она нахмурилась и сложила руки на груди."
    ren "Ну уж простите, мой профиль - выбивать информацию, а не принуждать к действию."
    ren "Не думала, что в таком состоянии она посмеет ослушаться."
    kt "Хорошо-хорошо.{w=1} Тогда скажи мне, что ты видишь в Генде?"
    hide image re_angry_casual
    show image re_bored_casual
    with byso
    "Накрутив прядь волос на палец, Рена задумалась, всматриваясь в звёзды."
    ren "Знаешь, мне кажется он весьма алогичным для своего положения."
    kt "О чём ты?"
    hide image re_bored_casual
    show image re_bored2_casual
    with byso
    ren "А просто. Мне не понятно, по какой причине он так медлителен в своих действиях и при этом абсолютно невнимателен."
    ren "Приведу пример. Чтобы добраться до тебя, мне пришлось уничтожить 36 симуляций.{w=1} Так почему он узнал об этом только спустя столько дней?"
    ren "Почему он позволяет сопротивлению такой беспредел?"
    ren "Почему он просто не может просто раз и навсегда уничтожить всё то, что мешает его правлению, скажем, сбросив ядерную бомбу на неприятеля?"
    scene bg ext_camp_entrance_night
    show image re_bored_casual
    with byso
    "Переведя взгляд на памятники пионерам, Рена подняла бровь."
    ren "Это точно связано со стабильностью."
    kt "Да, он говорил, что ты нарушила стабильность инреальности."
    "Она вопросительно посмотрела на Константина."
    ren "Когда это он успел?"
    kt "Помнишь, пионер говорил, что он пытает путников?"
    hide image re_bored_casual
    show image re_holod2_casual
    with byso
    "Пару раз кивнув, она почесала шею, недовольно бегая взглядом справа-налево."
    scene bg ext_no_bus_night
    show image re_holod2_casual
    with byso
    kt "Так вот тогда он меня отпинал, пытаясь выбить из меня информацию о тебе."
    ren "Я ему припомню..."
    "Злобно прошипела она, глядя в землю."
    kt "Тогда он сказал, что ты нарушила стабильность инреальности и побудила сопротивление к действию."
    hide image re_holod2_casual
    show image re_bored2_casual
    with byso
    "Рена нахмурилась и потёрла подбородок."
    ren "Так это вообще объясняет всё происходящее на просторах этой вселенной."
    ren "Сопротивление узнало о моих поисках через <<Цену грехов>>, после чего сообразило, что Генда никак не реагирует на столь наглые действия."
    ren "Потому они начали свою революцию, понимая, что Генда не реагирует на происходящее вокруг, и были правы."
    ren "А Генде важна стабильность инреальности, потому он не может просто убить всех щелчком пальцев, ведь это приведёт к краху всей системы."
    ren "Вероятно, в этой вселенной ему что-то настолько дорого, что он даже не пытается рискнуть, отчистив миры от врагов."
    scene bg re_walk with byso
    "Она задумчиво поводила взглядом по полю."
    kt "Меня начинают поражать твои дедуктивные способности."
    ren "Возможно это мои предположения, но у Генды может быть семья."
    "Константин поднял бровь и посмотрел на Рену."
    kt "Да ну, что за бред, зачем ему семья?"
    kt "С его убеждениями и действиями хрена с два кто захотел бы с ним жить."
    ren "Вспомни любого быдлана со своего подъезда.{w=1} Практически у каждого была своя фифа, с которой он развлекался."
    ren "Сам же понимаешь, что девушки даже близко не настолько избирательны."
    ren "Они готовы прыгнуть на член первому же харизматичному и богатому.{w} Если не харизматичному, то просто богатому."
    ren "Каковым, собственно, и является Генда.{w=1} Представь, сколько современных девушек и женщин раздвинули ноги перед тем, кто фактически является богом другой вселенной."
    "Почесав щеку, Константин засмотрелся на небо."
    ren "Да практически каждая.{w=1} Современные женщины просто пропитаны установками содержанки."
    kt "Мхм...{w=1} Да, тогда твоя гипотеза не кажется такой необоснованной."
    ren "Конечно, не знаю, зачем нам такая информация, но всё-таки..."
    stop music fadeout 1
    scene bg ext_road_night2 with byso
    scene bg ext_road_night2:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 1 crop (497, 223, 980, 630)
    pause 1
    show image idol_palladin at cright
    show image sh_idol at cleft
    show image box
    with byso
    "Не дойдя до ЛЭПов, они встретили пару человек, которые тащили ящик."
    play music obscure fadein 3
    "Выглядели они весьма необычно.{w=1} Один был огромным амбалом с пулемётом на спине и пометкой <<Паладин>> на руке."
    "Другой же вообще был Шуриком, у которого вместо ноги ржавая труба и множество порезов по всему телу.{w} Вёл он себя не особо адекватно - постоянно трясся и не контролировал свою мимику."
    ren "А это что за клоуны?"
    "Заметив Константина и Рену, они поставили ящик."
    hide image sh_idol
    show image sh_idol2 at cleft
    hide image box
    show image box
    with byso
    "Один начал доставать пулемёт, а другой, скалясь, запрыгал на месте."
    idol_s "Драка-драка-драка!"
    kt "Да, похоже...{w=1} Надо бежать?"
    hide image box
    hide image sh_idol2
    hide image idol_palladin
    with byso
    scene bg ext_road_night2:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 1 crop (0, 0, 1920, 1080)
    pause 1
    show image re_cr_smile_casual with byso
    "Рена широко улыбнулась и размяла шею."
    ren "Два человека?{w} 15 секунд.{w=1} Засекай."
    play sound3 sfx_armature_swish volume 1
    hide image re_cr_smile_casual
    show image re_smile_casual_topor
    with byso
    "Махнув рукой, она материализовала в своей руке топор.{w=1} Улыбка с лица бешеного пропала, а амбал убрал пулемёт обратно за спину."
    ren "Не учила вас мама не брать с пола всякую бяку?"
    ren "Я то вас научу.{w=1} Вам будет просто нечем что-либо брать."
    stop music fadeout 3
    idol_p "Обождите.{w=1} Вы же рыжая валькирия?"
    hide image re_smile_casual_topor
    show image re_normal_casual_topor
    with byso
    "Рена поморщилась и подняла бровь."
    ren "Валькирия только в том тогда, когда твои руки укорочу на сантиметров 50."
    idol_s "Она-она!{w=0.51} Она!{w=0.51} Она из пророчества!"
    "Протараторил Шурик и потоптался на месте."
    idol_s "Цадик будет доволен!{w=0.51} Механист даст новую дозу теорина!"
    th "Рена была права в своём комментарии.{w} Клоуны."
    ren "Мы биться то будем?"
    play music god fadein 3
    idol_p "Мы не хотим битвы."
    th "Чего?{w=1} Они только что хотели устроить бойню?{w=1} С чего так переобулись?"
    idol_p "Мы хотим поговорить."
    hide image re_normal_casual_topor
    show image re_angry_casual
    with byso #Рена за сундуком
    "Рена убрала топор и нахмурилась."
    ren "О чём нам с тобой говорить?"
    idol_p "Подойдите.{w=1} Мы хотим поговорить и гарантируем вашу неприкосновенность.{w=1} Бог нам свидетель."
    ren "А я уже ничего не гарантирую..."
    "Прошептала она и, направившись к ним, махнула рукой Константину."
    ren "Пошли.{w=1} Сейчас узнаем что им надо."
    kt "Не опасно?"
    hide image re_angry_casual
    show image re_holod2_casual
    with byso
    ren "Только для них."
    "Константин пожал плечами и пошёл за Реной."
    hide image re_holod2_casual with byso
    show image idol_palladin at fleft
    show image sh_idol at left
    show image box
    show image re_angry_casual at right
    with byso
    "Встав примерно в 2 метрах от ящика и двоих парней, Рена с Константином переглянулись."
    "Затем Константин перевёл взгляд на амбала."
    kt "Начнём с простого.{w=1} Вы кто?"
    hide image sh_idol
    show image sh_idol2 at left
    hide image box
    show image box
    hide image re_angry_casual
    show image re_angry_casual at right
    with byso
    "Шурик снова потоптался на месте и захихикал."
    idol_s "Мы верующие храма Генды!{w=0.51} Мы голосуем за веру!{w=0.51} Веру в Генду!{w=0.51} Бога в Бога!"
    hide image re_angry_casual
    show image re_holod2_casual at right
    with byso
    "Константина и Рену насторожили эти слова и они синхронно поморщились."
    idol_p "Не обращайте на него внимание.{w=1} Он не в себе."
    ren "Да мы это с самого начала заметили."
    idol_p "Его зовут Карачун.{w=1} Меня вы можете звать <<Паладин>>."
    idol_k "Да, я Карачун!{w=0.51} Воистину, Карачуном и подохну!{w=0.51} Ка-ра-чу-ном! {w=0.51}И еще раз Кара-ч-у-н-ом!"
    play sound3 sfx_punch_medium volume 1
    "Снова захихикав, Карачун покачал головой и пнул ящик."
    idol_k "Я так люблю новые знакомства!{w=0.41} Как же я люблю знакомства с новыми людьми!"
    idol_p "Как мы можем вас звать?"
    kt "Меня зовут Константин, а это Рена."
    idol_k "Рена-Константин!{w=0.41} Константин-Рена!{w=0.41} Рад познакомиться!!!"
    "Поклацав зубами обрадовался он и разворошил волосы на голове."
    hide image re_holod2_casual 
    show image re_angry_casual at right
    with byso
    ren "Слушай, успокой этого весёлого Роджера, а то у него станет ещё на одну ногу меньше."
    hide image sh_idol2
    show image sh_idol at left
    hide image box
    show image box
    hide image re_angry_casual
    show image re_holod2_casual at right
    with byso
    "<<Паладин>> кивнул и достал из кармана шприц с белой жидкостью. Карачун, заметив это, сильно взбесился."
    idol_k "У тебя всё это время было теорин?! {w=0.41}Ты врал мне, брат! {w=0.41}Скотина ты! {w=0.41}Сволочь! {w=0.41}Как ты посмел, а?!{w=0.41} Да ты знаешь, что за это бывает?!"
    play sound3 sfx_blow_out_candle volume 1
    "На это амбал молча положил шприц на сундук, а Карачун, словно ошпаренный схватил его и снял колпачок."
    hide image sh_idol
    show image sh_idol2 at left
    hide image box
    show image box
    hide image re_holod2_casual
    show image re_holod2_casual at right
    with byso
    idol_k "Ладно!{w=0.41} Так и бы-ыть!{w=0.41} Я тебя прощаю, брат!"
    hide image sh_idol2 with byso
    play sound3 genmod2 volume 1
    "Усевшись на землю, он воткнул шприц себе в шею и вдавил содержимое себе в кровь."
    idol_k "Прощаю..."
    kt "Это типа наркотик?"
    idol_p "Да.{w=1} Инструмент похвалы в нашей общине, который даёт возможность поговорить с умершими."
    th "Нет, ну точно ёбнутые."
    hide image re_holod2_casual 
    show image re_angry_casual at right
    with byso
    ren "Так в чём суть нашего диалога?"
    "Амбал размял предплечье и посмотрел на Рену."
    idol_p "Вы, Рена, исполнительница нашего пророчества."
    kt "И что это за пророчество?"
    "<<Паладин>> посмотрел в небо, словно молясь."
    idol_p "И придут они.{w=1} Две души."
    idol_p "Человека два, а память одна.{w} И положат они конец всем еретикам, да восстановят они порядок истинный."
    idol_p "И воля будет за настоящим творцом, да воздастся всем грешникам по заслугам."
    "Опустив взгляд обратно на Рену, он положил руки на ящик."
    idol_p "Нам приказано вас найти и доставить к нам на шабаш."
    kt "Мы никуда не поедем.{w=1} Точка."
    "Отрезал Константин, глянув на Рену.{w=1} <<Паладин>> его проигнорировал, а она, судя по всему, тоже не была в восторге от этого предложения."
    idol_p "Там мы выдадим вам всю нужную экипировку для совершения пророчества и поможем в подготовке."
    idol_p "Вы согласны?"
    hide image re_angry_casual
    show image re_holod2_casual at right
    with byso
    ren "Я не поняла, ты не слышал, что сказал Костя? {w}Нет.{w=1} Точка."
    show image sh_idol at left
    hide image box
    show image box
    hide image re_holod2_casual
    show image re_holod2_casual at right
    with byso
    "<<Паладин>> никак на это не отреагировал.{w=1} На ноги встал Карачун."
    idol_k "Раз так, то вы всегда можете нас найти в симуляции 12-40f, ибо ваша воля для нас закон."
    hide image re_holod2_casual 
    show image re_shy_casual at right
    with byso
    "Константина и Рену поразили такие связные слова от сумасшедшего."
    hide image re_shy_casual
    show image re_grin_casual at right
    with byso
    ren "Знаете что?{w=1} Верно, нам нужна экипировка.{w=1} И мы её возьмём сейчас."
    kt "Прямо из этого ящика."
    idol_k "Как пожелаете.{w=1} Мы не против."
    idol_k "При этом мы всегда будем рады вас видеть в нашей симуляции.{w=1} Цадик хотел познакомиться лично."
    idol_p "Всё что вы не заберёте, мы отправим к нам на базу.{w=1} Выбирайте."
    play sound3 sfx_lock_click volume 1
    pause 0.4
    play sound2 sfx_lock_click volume 1
    pause 0.8
    play sound sfx_cellar_open volume 1
    scene bg guns_box with byso
    "Амбал и Карачун щёлкнули замками на ящике и затем открыли его."
    "У Константина разбежались глаза. {w=1}В его голове, как рой растревоженных ос, пронесся каскад мыслей."
    show image nozh with byso
    "Внутри ящика лежали самые разнообразные изыски оружейного мастерства."
    hide image nozh
    show image patr
    with byso
    "Здесь были ручные гранаты, рюкзаки, длинные военные ножи с причудливыми гардами, куча плоских магазинов, обоймы, штыки, гильзы и несколько пистолетов неизвестной конструкции, слегка напоминавшие немецкие люгеры."
    hide image patr
    show image vintovka1
    with byso
    "На дне было множество коробок с патронами 9х19, а вишенкой на торте была странная, похожая на берданку с магазином винтовка с конверсией на патроны парабеллум."
    "Ружьё предназначалось, видимо, для отстрела особо крупногабаритных противников."
    "Винтовка была основательно смазана и приведена в боевое состояние.{w=1} Все детали были до блеска отполированы."
    "Пушка выглядела надёжно, просто и со вкусом."
    hide image vintovka1
    show image pereh
    show image pereh2 at right
    show image pereh3 at left
    with byso
    "Помимо всего этого нашлось 3 странных пульта.{w=1} Их предназначение оставалось неясным."
    hide image pereh
    hide image pereh2
    hide image pereh3
    with byso
    kt "Хера себе сундучок...{w=1} Тут такое богатство..."
    "Заметив, как Константин смотрит на ружьё, Рена улыбнулась."
    ren "Значит, из всего этого мы забираем..."
    ren "Рюкзак."
    ren "Винтовку, два магазина для неё, патроны одну пачку."
    "Всё, что проговаривала, Рена складывала в рюкзак."
    ren "Два пистолета, по пачке патронов на каждый."
    ren "А это что за пульты?"
    idol_p "Телепортаторы сопротивления."
    ren "Как работают?"
    idol_k "Вводите номер симуляции, нажимаете на центральную кнопку."
    kt "И как вы это выяснили?"
    idol_k "На практике. {w=1}Редкая вещь, а это ещё и новая модель."
    ren "Отлично, тогда два пульта."
    ren "Один ножик."
    ren "И пару пачек патронов про запас."
    "Сложив всё в сумку, она посмотрела на Карачуна."
    ren "Вопросы?"
    idol_k "Вам этого точно хватит?{w=1} Мы готовы отдать ещё."
    ren "Грех отказываться.{w} Ещё три пачки патронов и пару гранат."
    scene bg ext_road_night2
    show image idol_palladin at fleft
    show image sh_idol at left
    show image box
    show image re_smile_casual at right
    with byso
    play sound3 sfx_close_door_clubs_nextroom volume 1
    play sound2 sfx_put_sugar_cart volume 1
    "Передав Константину запрошенное, Рена закрыла сундук."
    ren "Остальное нам не нужно."
    idol_p "Как скажете."
    idol_k "Если вам будет нужна помощь, то обращайтесь в общину.{w=1} Мы поможем осуществить пророчество."
    ren "Да-да.{w=1} Пока."
    idol_p "Да прибудет с вами всевышний."
    idol_k "Удачи в ваших начинаниях."
    kt "До встречи."
    stop music fadeout 3
    hide image idol_palladin
    hide image sh_idol
    hide image box
    with byso
    hide image re_smile_casual
    show image re_smile_casual
    with byso
    "Фанатики взяли сундук и потащили дальше в лагерь.{w=1} Константин и Рена уселись на краю дороги."
    play sound3 sfx_cigarette_pack_crumple volume 0.6
    "Константин распаковал новую пачку сигарет и поделился с Реной."
    scene bg zvezda with byso
    play sound2 light_inh volume 1
    play music exodus fadein 3
    "Закурив, он глянул в небо."
    play sound inh volume 1
    "Рена взяла в рот сигарету и прикурила её от сигареты Константина."
    ren "Спасибки..."
    kt "Это было...{w=1} Странно?"
    ren "Да.{w=1} Совершенно не ожидала от них такого."
    kt "Надо признать, что твой дар дедукции не сработал."
    ren "Даже не поспорю...{w=1} Ну, зато у нас наконец появилась экипировка."
    scene bg ext_road_night2 with byso
    show image vintovka1 with byso
    "Константин вставил сигарету в зубы и взял в руки винтовку."
    play sound3 sfx_click_2 volume 1
    "Сняв магазин, он посмотрел на патроны."
    "Обойма только снаружи выглядела большой.{w=1} Внутри было разделение, которое позволяло вставлять только патроны 9х19."
    "Попробовав вставить внутрь патрон, Константин понял, что магазин полон."
    hide image vintovka1 with byso
    show image re_smile_casual with byso
    play sound3 reload volume 1
    "Он вставил обойму в ружьё и отложил его на землю."
    kt "Напоминает дедовский карабин.{w=1} Как стреляет ещё предстоит узнать."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Это хорошо.{w=1} Как стрелять хоть помнишь?"
    kt "Ещё пять дней назад вспомнил."
    scene bg zvezda with byso
    "Рена улыбнулась и положила голову на плечо Константина.{w=1} Они вместе сидели и смотрели на звёзды."
    ren "Хорошо, что дедушка научил тебя обращаться с оружием."
    kt "Да, не кажется мне, что понимал, где этот навык мне пригодится."
    ren "Ну а кто знает что будет дальше?{w=1} Я нет, ты нет.{w} Всё происходящее скрыто от нас неизвестным."
    ren "Кто-то бы сказал: <<Настоящий мудрец может видеть что будет в будущем>>."
    ren "Ложь.{w=1} Настоящий мудрец знает, что будущее неведомо никому."
    "Константин, будучи поражённым выводами Рены, пару раз кивнул и перевёл взгляд на неё."
    kt "Всё-таки, за всё время наших философских разговоров, хочу заметить, что ты умеешь красиво излагать мысли."
    "Она, подняв взгляд на Константина, улыбнулась."
    ren "Я даже могу рассказать почему."
    kt "Давай, мне интересно."
    ren "При нашем попадании в инреальность нам подтёрло воспоминания."
    ren "Так как в случае моих произошла фактическая нестыковка, мне их предписали."
    ren "При том достаточно качественно. {w=1}Вот, послушай, я расскажу."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "Девушка 24 лет по имени Регина. {w}\nПисательница с невероятной способностью к самообразованию и умением смотреть в самую суть вещей. {w}\nПо своему характеру она добрая и отзывчивая, но это лишь внешне. {w=1}\nНа самом деле Регина способна на жестокость. {w}\nОна жестокая и бессердечная. {w=1}\nЕе душа черна и наполнена ненавистью. {w}\nТакже она гениальна в некоторых вопросах. {w=1}\nУ нее своеобразное видение жизни и мира – она называет его «гибридным», что полностью отражает ее внутренний мир и мышление. Но по каким-то причинам ее возможности ограничены. {w=1}\nУ неё был комплекс богини, и она буквально управляла людьми на своих условиях. {w}\nКорыстные родители, избалованная сестра, скверное детство... {w=1}\nПопросту говоря, она жила в мире, который невозможно понять, пока сам не прикоснешься к его тайнам. {w}\nДля неё всё закончилось печально. {w}\nПосле убийства своей сестры и родителей, она попала в инреальность. {w}\nЕё мало интересовала смерть, скорее истинные мысли и чувства людей перед этим актом."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    ren "При попадании в свою первую симуляцию я достаточно быстро вспомнила кто я.{w=1} Буквально за минут 20."
    ren "В целом, лишние знания и способности не бывают лишними в нашем случае."
    kt "Да-а...{w=1} Странно всё-таки."
    ren "Что именно?"
    kt "Как мы так быстро вернули себе память?{w=1} У меня тоже ушло на это минут 20."
    kt "Все же прибывают сюда в неведение."
    "Рена поводила глазами по звёздному небу."
    ren "Не знаю.{w=1} Может быть обычное совпадение."
    ren "Хотя, может и на это есть логичное объяснение, на которое у нас пока нет доводов."
    stop music fadeout 3
    scene bg ext_road_night2
    show image re_bored_casual
    with byso
    "Ночную тишину нарушило какое-то жужжание."
    "Прислушавшись, Константин и Рена поняли, что это был автобус."
    kt "У нас гости."
    hide image re_bored_casual
    show image re_grin_casual
    with byso
    "Рена улыбнулась и встала с места."
    "Вдали виднелся автобус."
    "Выглядел он точно так же, как и тот, на котором были Олег и Лиза."
    play sound3 bus_mimo volume 1
    play music Waijdan fadein 3
    "На полной скорости он пронёсся мимо и начал оттормаживаться."
    hide image re_grin_casual
    show image re_cr_smile_casual
    with byso
    ren "Так встретим их подобающим способом."
    "Собрав всю экипировку, они в темпе направились за автобусом."
    scene bg ext_bus_night
    show image sh_idol at left
    show image re_bored_casual at right
    with fade
    "За несколько минут они дошли до входа в лагерь, они встретили Карачуна."
    "Он стоял на коленях и дрожащими руками подвязывал связку гранат ко дну автобуса."
    "Судя по всему, его адекватное поведение было обусловлено только действием наркотика."
    hide image sh_idol
    show image sh_idol2 at left
    with byso
    idol_k "О, о, о!{w=0.61} Новые друзья!{w=0.61} Прувет!"
    ren "Ты что делаешь?"
    idol_k "Подарок!{w=0.61} Подарочек!"
    hide image sh_idol2
    show image sh_idol at left
    with byso
    "Отвлёкшись от своего дела, Карачун встал на ноги и нахмурился."
    idol_k "К нам приехали враги!{w=0.61} Враги!{w=0.61} Они здесь!"
    kt "Ты имеешь в виду сопротивление?"
    idol_k "Да!{w=0.61} Да-да!"
    hide image re_bored_casual
    show image re_holod_casual at right
    with byso
    "Рена подошла к психу и указала на связку гранат."
    ren "Убирай.{w=1} Нам это ещё нужно."
    idol_k "Что-о?!{w=0.61} А как же громкий бабах?!"
    kt "Нам нужен этот автобус...{w=1} Для выполнения пророчества, вот."
    "Карачун уныло опустил руки и резко наклонился."
    idol_k "Бабах не будет..."
    "Сняв гранаты из под автобуса, он распихал их по карманам."
    hide image re_holod_casual
    show image re_bored2_casual at right
    with byso
    ren "Охраняй автобус.{w=1} Мы разберёмся и вернёмся."
    hide image sh_idol
    show image sh_idol2 at left
    with byso
    idol_k "Да! {w=0.61}Сохраню!{w=0.61} Бабах не будет, но будет хрясь!"
    hide image sh_idol2 with byso
    "Игриво протараторил Карачун и вбежал в автобус."
    kt "М-да."
    hide image re_bored2_casual
    show image re_bored_casual at right
    with byso
    ren "М-да..."
    scene bg ext_clubs_night
    show image re_bored_casual
    with byso
    "В лагере их встретила чистая тишина.{w=1} Рена осмотрелась и прогнулась в спине."
    ren "Из них нам нужен один человек, который покажет нам, как мы можем пользоваться автобусом."
    kt "Да, только на этот раз нельзя допустить их к запуску самоуничтожения."
    hide image re_bored_casual
    show image re_smile2_casual
    with byso
    ren "Не говори очевидного."
    ren "Давай начнём с клубов.{w=1} Дальше музклуб, столовая и так далее."
    kt "Принято."
    play sound3 weapon volume 1
    hide image re_smile2_casual
    show image re_smile_casual
    with byso
    "Константин достал винтовку со спины и дослал патрон."
    kt "Начинаем."
    play sound3 sfx_armature_swish volume 1
    "Рена материализовала топор и прокрутила его в руке, словно нарисовав круг."
    ren "Кто не спрятался, тот труп."
    play sound3 door_break volume 1
    "Выбив дверь, она вошла в клубы." with vpunch
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_clubs_male_night with byso
    show image re_bored2_casual with byso
    "Константин вошёл за ней и не обнаружил ничего странного."
    hide image re_bored2_casual
    show image re_smile2_casual
    with byso
    ren "Я туда, а ты в кладовку."
    kt "Стой.{w=1} Тут записи."
    hide image re_smile2_casual
    show image re_bored_casual
    with byso
    "Рена пожала плечами и подошла к Константину."
    ren "Ну давай почитаем."
    play sound3 sfx_paper_bag volume 1
    scene bg int_aidpost_lamp with flash
    stop ambience fadeout 1
    window hide dissolve
    $ set_mode_nvl()
    neiz_nvl "Кочевой Алексей Антонович.{w=1} Первый день цикла под прикрытием. {w}\nНовая симуляция, новые поиски.{w=1} Есть одна проблема, мой отряд так и не вернулся. Они хотели объехать симуляции сектора и собрать патроны...{w=1} Чёрт его знает, просто испарились.{w} Тогда уж мои дела совсем плохи, я один отсюда не выберусь...{w=1} Гордон только начал разрабатывать что-то вроде телепорта, а у меня на этой уйдёт вечность.{w=1} Мой коллега, с которым я общался через радио, судя по всему сошёл с ума. {w=1}Не удивительно. {w=1}Он слишком долго смотрел в пустоту и пустота начала вглядываться в него. Бредил про теории мироздания и прочую ересь... Ну, пока он ещё хоть немного вменяем.{w=1} Может он стал идолопоклонником... Не знаю. {w=1}Отчёт я уже составил, но отправить мне его некому. {w}\nПочему никто не выходит на связь? {w=1}Неужели в сопротивлении проблемы? Ладно, у меня теперь есть бесконечная куча времени это узнать."
    nvl clear
    neiz_nvl "Кочевой Алексей Антонович.{w=1} Второй день цикла под прикрытием. {w}\nВышло связаться с кем-то по радио... Всё бы ничего, но все пропали! Все! Нет никаких следов пустышек. Лагерь никем не населён! Я кустарно собрал некоторые приборы слежки за инреальностью и разместил их в библиотеке... Наброски чертежей прилагаются в блокноте. Стабильность не поддаётся замеру.{w=1} Но это невозможно! Писание тут не поможет, там просто ничего не сказано про такие аномалии.{w=1} Это, судя по всему ошибки четвёртой версии...{w=1} Ладно, надо исследовать деятельность идолопоклонников. {w}\nТем не менее, наша операция подразумевала поверхностные поиски данных, но я неуклонно иду вглубь... Возможно Андрей по номиналу оценит мои труды."
    nvl clear
    neiz_nvl "Кочевой Алексей Антонович.{w=1} Третий день цикла под прикрытием. {w}\nОдиноко... Коллега окончательно сошёл с ума и во время нашего общения разбил в щепки своё радио... Твердил о том, что в инреальности образовалась некоторая сущность... Осколок личности?{w=1} Я уже забыл... Я начинаю забывать простейшие действия. Я за день ел только один раз.{w=1} Попытки связаться хоть с кем не увенчались успехом. Центр молчит... Я разобрал всю технику и хочу разработать новое устройство...{w=1} Было бы неплохо знать, куда могут вести порталы при обнулении стабильности. Хотя в моём случае, судя по всему, не существует такого понятия.{w=1} Михаил идиот!{w=1} Формула, которую он делал не имеет места быть! {w}\nПересчёта там не идёт.{w=1} Вообще.{w=1} То есть преимущественно перемещение идёт по секторам и по симуляциям в секторе.{w=1} Никаких факториалов и прочего бреда там нет. Я планирую с помощью нового оборудования создать карту, которая будет отражать истинное положение симуляций относительно друг друга.{w=1} Еда появляется из неоткуда ровно в 12... А сейчас я пойду спать...{w=1} Никогда ранее мне так сильно спать не хотелось..."
    nvl clear
    neiz_nvl "Кочевой Алексей Антонович.{w=1} Четвёртый день цикла под прикрытием. {w}\nГотово! Оно работает!{w=1} У меня теперь есть источник питания и я могу выяснить, куда пойдут порталы!{w=1} Самое странное, что один из трёх порталов в моей симуляции идёт прямиком в кошмар...{w=1} Ну это не важно.{w=1} Важно то, что мои мысли вошли в тупик... {w}\nТут кто-то есть! Я клянусь я слышал голоса! Грубый мужской голос и Шурика, безумного Шурика... Они говорили про какого-то <<Цадика>>. Я решил подслушать и я понял... Это идолопоклонники! Это их симуляция! Они забрали всю еду на день и ушли в центральный портал на площади. По моим исследованиям, он ведёт напрямую в кошмар! Выходит что у идолопоклонников есть база в кошмаре! {w}\nТеперь весь пазл сложился! Генда выделил им отдельное зашифрованное инреальностью пространство, которое не отслеживается <<Ценой грехов>>. Потому и главы идолопоклонников обрывались на абзацы! Мне нужно срочно передать эти данные в сопротивление! Я начинаю искать возможность сваливать отсюда!"
    window hide dissolve
    pause 1
    $ set_mode_adv()
    scene bg int_clubs_male_night
    show image re_bored_casual
    with byso
    ren "Это многое объясняет.{w=1} Формула бесполезна - значит что-либо считать по ней бессмысленно."
    kt "Мы рядом с симуляций идолопоклонников - какими бы дружелюбными они не казались, я не хочу идти к ним."
    ren "И последнее - устройство с картой инреальности.{w=1} Надо её заполучить. "
    kt "Понял, двинули в библиотеку."
    hide image re_bored_casual
    show image re_smile_casual
    with byso
    "Рванув с места, они направились в указанном направлении."
    play ambience ambience_camp_center_night volume 1 fadein 1
    scene bg ext_library_night with fade
    "В библиотеке во всю шли разговоры."
    irrp "Вот и оно.{w=1} Энджи, надо это забрать."
    ang "А я, по-твоему, этого не поняла?"
    sold_g "Давайте реще.{w} Нам нужно возвращаться на базу."
    irrp "Ты вообще оплачен капитаном!{w=1} Заткнись и бери ноутбук!"
    th "Ноутбук?{w=1} Упрощает ситуацию, надо отобрать."
    show image re_smile_casual with byso
    ren "Готов?..."
    play sound3 sfx_clench2 volume 0.51
    "Прошептала Рена, взявшись за дверную ручку."
    "Константин кивнул и упёр приклад в плечо."
    kt "Начнём."
    play ambience ambience_int_cabin_night volume 1 fadein 1
    play sound3 door_break volume 1
    scene bg int_library_night
    show image sopr_sold at right
    show image irr_shock 
    show image ang_normal at left
    with byso
    "Влетев в помещение, Константин прицелился в первую попавшуюся цель - парня в противогазе с ноутбуком в руках."
    play sound3 sfx_armature_swish volume 1
    "Рена раскрутила топор в руке и осмотрела присутствующих."
    ren "Дорогие повстанцы, будьте добры, всё на пол и, так и быть, вы останетесь в живых."
    scene bg int_library_night
    show image sopr_sold at right
    show image irr_happy
    show image ang_smile at left
    with byso
    "Сопротивленцы рассмеялись и достали оружие."
    irrp "Ну попробуй!"
    stop music fadeout 2
    ang "Тоже мне, вертолёт. Ты как собралась?...{w=0.31}{nw}"
    play sound3 knife_flying
    pause 1
    scene bg int_library_night
    show image sopr_sold at right
    show image irr_shock at left
    with vpunch
    play music CowCowCow fadein 3
    "Она бросила топор в голову Ангелины, располовинив на две части.{w=1} Топор застрял в голове, а тело мешком повалилось на пол."
    hide image irr_shock
    show image irr_cry at left
    with byso
    "На глазах девушки навернулись слёзы."
    irrp "Ангелина!!!"
    ren "Это я называю <<откройся окружающим>>.{w=1} Ещё вопросы?"
    play sound3 sfx_break_monitor volume 1
    pause 0.1
    hide image irr_cry
    show image irr_cry at cright
    with byso
    "В ярости девушка подбежала к парню в противогазе и выбила из его рук ноутбук, сломав его."
    "Экран отлетел от тушки."
    sold "Что ты сделала?!"
    irrp "Ничерта вы от нас не получите!"
    kt "Тва-арь..."
    ren "Ну вы сами напросились..."
    play sound_loop MP40 volume 1 #Звук уебанский
    show weapon_fireing with fl_fire
    "Девушка достала со спины пистолет-пулемёт и начала умалишённо поливать комнату свинцовым дождём."
    play sound3 sfx_put_sugar_cart volume 1
    "Константин и Рена спрятались за кафедру, а парень в противогазе попал под несколько пуль в спину и пал оземь."
    ren "Ой, что такое?{w=1} Убили твою подружку?"
    ren "Прости, не хотела. {w=1}Честно."
    irrp "Сдохни!!!"
    ren "Ладно, не то что бы честно..."
    stop sound_loop
    scene bg int_library_night with byso
    play sound3 sfx_click_2 volume 1
    "Патроны у девушки закончились и она начала перезаряжаться."
    show image re_cr_smile_casual with byso
    ren "Засекай 3 секунды."
    hide image re_cr_smile_casual with bso
    "Рена вылетела из укрытия."
    kt "Подожди, сто...{w=0.34}{nw}"
    play sound3 sfx_lena_hits_alisa volume 1
    stop music fadeout 3
    "Удар."
    show image re_cr_smile2_casual with byso
    "Константин выглянул."
    "Рена выбила из рук девушки пистолет-пулемёт и повалила на землю."
    play sound3 wood_hit_head volume 1
    play music vertushka fadein 3
    hide image re_cr_smile2_casual
    show image re_cr_smile_casual
    with vpunch
    "Сильно впечатав её головой в пол, Рена добилась её потери сознания."
    ren "Чётко и в срок."
    "Константин вышел из укрытия."
    kt "Да, только теперь надо выбрать, кто из них пойдёт нам в плен."
    hide image re_cr_smile_casual
    show image re_bored_casual
    with byso
    "Девушка была в отключке, а парень едва-слышно хрипел."
    window hide
    menu:
        "Черноволосая девушка.":
            $ renpy.block_rollback()
            kt "Давай эту.{w=1} Этот загнётся раньше, чем мы его дотащим до автобуса."
        "Парень в противогазе.":
            $ renpy.block_rollback()
            kt "Давай этого.{w=1} Не хочу, чтоб она как и Лиза подорваться решила."
            ren "Хорошо."
            play sound3 knife_out volume 1
            hide image re_bored_casual
            show image re_normal_casual_topor
            with byso
            "Спокойно проговорила Рена и вытащила топор из головы мёртвой Ангелины."
            ren "Тогда я эту кончаю."
            play sound3 slash volume 1
            "Взмахом топора она обезглавила девушку, а Константин подошёл к парню." with fl_scare
            kt "Э, солдат, рота подъём!"
            "Парень лежал и, хрипя, никак не реагировал."
            hide image re_normal_casual_topor
            show image re_cr_smile_casual
            with byso
            ren "Давай помогу."
            play sound3 sfx_punch_washstand volume 1
            "Рена подошла и пнула парня под ребро." with vpunch
            play sound3 cheka volume 1
            hide image re_cr_smile_casual
            show image re_guilty_casual
            with bso
            "На поясе парня отлетели скобы от гранат."
            kt "Блять!"
            play sound3 bum volume 1
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            scene bg black with fl_fire
            "Взрыв."
            window hide dissolve
            pause 2
            $ unlock_ach_root_inreal(2)
            play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
            scene bg ending_dead_cg:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            show ending_dead:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            with Dissolve(15)
            scene bg black with byso
            pause 1
            stop sound
            jump after_ending_screen
    ren "Как скажешь."
    play sound3 knife_out volume 1
    hide image re_bored_casual
    show image re_normal_casual_topor
    with byso
    "Спокойно проговорила Рена и вытащила топор из головы мёртвой Ангелины."
    hide image re_normal_casual_topor with byso
    "Константин подошёл к ноутбуку, который лежал возле парня."
    "Компьютер был разбит.{w=1} Без возможности восстановления в условиях отсутствия инструмента."
    "По клавиатуре пошёл скол - сквозь него была видна разломанная материнская плата."
    play sound3 sfx_click_3 volume 1
    "Константин извлёк из компьютера жёсткий диск.{w} К счастью, хоть он уцелел."
    "На корпусе была приклеена записка - <<15-21u - тайник Фобоса>>."
    play sound3 slash volume 1
    "Рена отрубила лежащему солдату голову."
    show image re_smile_casual_topor with byso
    ren "Ещё и сопротивлением себя называют.{w=1} Позор человечества."
    kt "Да, кажется, ты бы сама смогла их всех перебить."
    hide image re_smile_casual_topor
    show image re_grin_casual
    with byso
    ren "Безусловно.{w=1} Потащили её в автобус."
    kt "Я даже знаю в какую симуляцию мы сначала поедем. {w=1}15-21u."
    hide image re_grin_casual
    show image re_smile2_casual
    with byso
    ren "Как скажешь.{w=1} А зачем?"
    play sound3 sfx_paper_bag volume 1
    hide image re_smile2_casual
    show image re_smile_casual
    with byso
    "Константин показал записку."
    ren "Тайник Фобоса?{w=1} Звучит любопытно.{w=1} Поедем."
    stop music fadeout 2
    play ambience ambience_camp_center_night volume 1 fadein 1
    scene bg ext_bus_night with fade
    show image re_bored_casual at right
    show image sh_idol2 at left
    with byso
    "У автобуса их встретил Карачун."
    play music Aleph fadein 3
    idol_k "О, о, о! {w=0.51}А можно я её себе заберу?!"
    kt "Если ты нам покажешь, как пользоваться автобусом, то пожалуйста."
    hide image sh_idol2
    show image sh_idol at left
    with byso
    "Карачун нахмурился и сложил руки на груди."
    idol_k "А так хотелось развлечься!{w=0.51} Почему судьба так со мной?!"
    th "Даже и не знаю..."
    kt "Иди там собери экипировку с трупов в библиотеке.{w=1} У них много..."
    idol_k "Трупы?!"
    idol_k "Люблю трупы!"
    scene bg ext_camp_entrance_night with byso
    "Развернувшись, он побежал в лагерь."
    idol_k "Человек ещё полчаса человек!!!"
    scene bg ext_bus_night
    show image re_bored2_casual
    with byso
    "Прокричал Карачун и скрылся за воротами. Константин поморщился."
    kt "Блять...{w=1} Я не это имел в виду..."
    ren "И почему я не удивлена?..."
    hide image re_bored2_casual
    show image re_bored_casual
    with byso
    ren "Пошли будить нашу спящую красавицу."
    "Они понесли девушку дальше."
    play ambience ambience_ext_road_night volume 0.41 fadein 1
    scene bg int_avtobus2
    show image re_smile_casual
    with byso
    play sound3 sfx_mystery_movement volume 1
    "Усадив её на водительское сидение, Рена обнаружила гарроту, лежащую под торпедой."
    ren "О, а это я люблю."
    "Константин ухмыльнулся и поставил рюкзак под торпеду, а ружьё на рядом стоящее сидение."
    kt "Как Карачун трупы?"
    hide image re_smile_casual
    show image re_bored_casual
    with byso
    "Рена тяжело вздохнула и потёрла глаза."
    ren "Юморист..."
    kt "Да, я такой."
    hide image re_bored_casual
    show image re_holod2_casual
    with byso
    "Рена связала девушку ремнём."
    play sound3 sfx_open_window volume 1
    "Константин открыл бардачок и обнаружил там аптечку."
    hide image re_holod2_casual
    show image re_grin_casual
    with byso
    ren "А это как раз кстати."
    "Она открыла аптечку у Константина в руках и достала оттуда флакон нашатырного спирта."
    play music PerfectNothing fadein 3
    play sound3 sfx_water_splash volume 1
    pause 0.4
    play sound2 acid volume 1
    play sound "<from 0 to 4>inrealnost/Music/Sound/fem_screams.mp3"
    "Не особо церемонясь, она облила лицо девушки содержимым флакона."
    "Жидкость начала разъедать лицо девушки, а Рена выкинула пустой флакон в форточку."
    ren "Да, концентрация была великовата..."
    hide image re_grin_casual
    show image re_smile3_casual
    with byso
    ren "Так. {w=1}Красота, ты проснулась?"
    play sound3 sfx_mystery_movement volume 1
    "Девушка пыталась избавиться от жжения, елозя по сидению."
    ren "Нам нужна информация, и чем быстрее, тем лучше."
    ren "Пытать тебя у меня вагон и малая телега, но думаю, наши цели сойдутся."
    irrp "Ничего я тебе не скажу!!!{w=1} Ты убила Ангелину!!!{w=1} Я никогда тебе этого!..."
    kt "Ух, зря."
    play sound3 sfx_punch_washstand volume 1
    hide image re_smile3_casual
    show image re_angry_casual
    with vpunch
    "Рена прописала ей апперкот."
    ren "Ответ неверный.{w=1} Кстати, не поверишь, но твоя соратница мне говорила примерно то же самое."
    kt "Да, только Лиза говорила про Олега, а не про Ангелину."
    irrp "Что?! {w}Вы убили Лизу?!"
    kt "Нет, она решила активировать протокол <<Безбожник>> и подорваться."
    hide image re_angry_casual
    show image re_cr_smile_casual
    with byso
    ren "Ага.{w=1} Сочти за факт, что даже она хотела умереть, а не далее быть истязаемой."
    ren "Если ты нам покажешь, как пользоваться автобусом и скажешь, в какой симуляции база сопротивления, то мы тебя отпустим по дороге."
    "Девушка оскалилась и выдохнула через зубы."
    irrp "Хуй вам!"
    play sound3 sfx_pat_shoulder_hard volume 1
    hide image re_cr_smile_casual
    show image re_cr_smile2_casual
    with byso
    "Рена загнула палец на связанной руке девушки."
    ren "Тогда я начну."
    play sound3 perelom volume 1
    play sound2 "<from 6 to 10>inrealnost/Music/Sound/fem_screams.mp3"
    ren "Любит."
    play sound perelom volume 1.2
    ren "Не любит."
    "Девушка кричала в агонии, а Рена продолжала баловаться с пальцами девушки."
    play sound3 perelom volume 1
    ren "Любит."
    play sound3 perelom volume 1.3
    ren "Не любит."
    play sound3 perelom volume 0.9
    ren "Любит!"
    hide image re_cr_smile2_casual
    show image re_grin_casual
    with byso
    ren "Обожаю эту игру!{w=1} Сломай все пальцы на руке и всегда будет результат - любит."
    hide image re_grin_casual
    show image re_smile_casual
    with byso
    ren "О, у меня же есть новинка - ножик."
    "Достав из рюкзака Константина армейский нож, она засмотрелась на его лезвие."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Блестящий...{w=1} А сейчас мы его украсим твоей кровью."
    "Рена приложила нож к ляжке девушки."
    hide image re_grin_casual
    show image re_cr_smile_casual
    with byso
    ren "Скажешь, когда захочешь заговорить, ладно?"
    play sound3 horror1 volume 1
    play sound "<from 17 to 22>inrealnost/Music/Sound/fem_screams.mp3"
    "Вогнав нож на полтора сантиметра, Рена начала оставлять продольный порез. Поднялся дикий вопль."
    stop music fadeout 3
    idol_p "Позвольте войти."
    hide image re_cr_smile_casual
    show image re_bored_casual
    with byso
    kt "Заходи.{w=1} Рена, подожди пока что."
    play sound3 knife_out volume 1
    "Рена послушно вытащила ножик из ляжки девушки и обернулась."
    hide image re_bored_casual
    show image re_smile_casual
    with byso
    ren "Хорошо, дашь сигаретку?"
    "Константин кивнул, достал сигареты и поделился с Реной."
    play sound3 light_inh volume 1
    play music idol_theme fadein 3
    show image idol_palladin at right
    hide image re_smile_casual
    show image re_smile_casual
    with byso
    "Закурив, они встретили <<Паладина>>, который поднимался по ступенькам автобуса."
    idol_p "Карачун забыл вам отдать кое-что."
    kt "И что это?"
    "Амбал протянул им кинжал в блестящих ножнах."
    scene bg cristal_blade with byso
    "На ручке искрились крошечные блестки аметистов.{w=1} Ножны и ручка были отделаны серебром."
    "Лезвие было кристальным, словно сделанным из янтаря и блескало при лунном свете."
    "Несмотря на материал, нож казался невероятно острым."
    scene bg int_avtobus2
    show image idol_palladin at right
    show image re_grin_casual
    with byso
    irrp "Так вот вы кто...{w=1} Их союзники..."
    play sound3 wood_hit_head volume 0.61
    hide image re_grin_casual
    show image re_rage2_casual
    with vpunch
    ren "Молчать!"
    "Топнула ногой Рена, обернувшись на девушку."
    hide image re_rage2_casual
    show image re_grin_casual
    with byso
    "Она приняла подарок и отложила старый нож в рюкзак."
    ren "А у меня теперь новая игрушка..."
    idol_p "Этот нож наделён силой.{w=1} Он способен пронзать призраков."
    hide image re_grin_casual
    show image re_cr_smile_casual
    with byso
    ren "Я даже знаю одного усопшего, для которого этот нож пригодится."
    kt "Ну вы нас конечно задарили.{w=1} Передайте спасибо вашей общине."
    idol_p "Это не от общины, а лично от меня и Карачуна.{w=1} Надеюсь, он вам поможет в ваших начинаниях."
    "Мужик посмотрел на связанную девушку, которая стонала и истекала кровью."
    idol_p "Если вы будете так добры, то Карачун просил оставить эту девушку для него."
    irrp "Что?! {w=1}Нет!"
    play sound3 sfx_face_slap volume 1
    hide image re_cr_smile_casual
    show image re_cr_smile2_casual
    with vpunch
    "Отвесив девушке леща, Рена широко улыбнулась."
    ren "Да, красавица моя, если ты будешь меня излишне бесить, то достанешься именно ему."
    ren "С подрезанными сухожилиями.{w=1} Я тебя то спиртиком обработаю и отдам ему."
    hide image re_cr_smile2_casual
    show image re_cr_smile_casual
    with byso
    kt "Подожди у автобуса.{w=1} Если она не окажется сильно сговорчивой, то заберёшь."
    idol_p "Спасибо вам, вы очень добры, будем ждать."
    hide image idol_palladin with byso
    "Поклонился амбал и покинул автобус."
    idol_k "Не бойся меня, красавица!{w=0.61} Ты в умелых руках!"
    idol_k "И будешь на умелом члене!"
    stop music fadeout 3
    "Донёсся крик Карачуна извне.{w=1} По голосу была слышна его бешеная радость."
    scene bg re_torture with byso
    play sound3 inh volume 1
    "Докурив практически до фильтра, Рена подошла к девушке и наклонилась."
    ren "А мы продолжаем.{w=1} У меня тут сигарета, не желаешь докурить?"
    irrp "Я ничего от тебя...{w=0.43}{nw}"
    play music "<from 7.45 to 140>inrealnost/Music/Music/PerfectNothing.mp3"
    play sound2 burn
    pause 0.5
    play sound "<from 6 to 10>inrealnost/Music/Sound/fem_screams.mp3"
    "Рена затушила сигарету об глаз девушки.{w=1} Глаз быстро почернел, налился кровью и запух, заполнив зрачок."
    "Крики боли, казалось, были слышны даже в другом конце симуляции."
    ren "Честерфилд с кнопкой. {w=1}Нравится?"
    kt "Слушай, ты её особо не калечь. {w=1}На случай если она ещё нужна Карачуну."
    idol_k "Калечить?!{w=0.31} Мой любимый фетиш!{w=0.31} Жёстче её давай!"
    "Константин тихо посмеялся и махнул рукой."
    kt "Тогда забудь. Продолжай."
    play sound3 sfx_mystery_movement volume 1
    "Карачун залез на передний бампер автобуса и с широкой лыбой наблюдал за происходящим."
    ren "Кость, дай спирт.{w=1} Надо ей кровотечение остановить.{w=1} Ещё умрёт раньше времени."
    play sound3 sfx_unzip_sleepbag volume 1
    pause 0.9
    stop sound3 fadeout 0.2
    "Константин улыбнулся и достал из аптечки перекись водорода и флакон зелёнки."
    kt "Бинты?"
    ren "А есть?"
    "В довесок он протянул и бинты."
    ren "Отлично."
    play sound3 acid volume 0.51
    play sound "<from 0 to 4>inrealnost/Music/Sound/fem_screams.mp3"
    "Залив рану перекисью вперемешку с зелёнкой, Рена сделала несколько оборотов бинта."
    "Крики ни на секунду не останавливались."
    "Сомкнув челюсти девушки, Рена подняла её голову в свою сторону и, посмотрев в целый глаз, улыбнулась."
    ren "Мы уже готовы говорить?{w=1} У тебя ещё есть один глаз, сухожилия, целый позвоночник и все внутренние органы."
    idol_k "Оторви ей ухо!{w=0.31} Сломай нос!{w=0.31} Выдерни зубы!"
    th "Ебать у тебя фантазии..."
    idol_p "Карачун, не мешай!"
    ren "А что, хорошая идея.{w=1} Начну в обратном порядке."
    "Рена замахнулась кулаком и прицелилась девушке в зубы."
    irrp "М-м-м-м!!!{w=1} М-м!!!"
    stop music fadeout 3
    ren "Ой, а мы уже готовы говорить?"
    scene bg int_avtobus2
    show image re_cr_smile2_casual at cright
    with byso
    "Она отпустила голову девушки и улыбнулась."
    hide image re_cr_smile2_casual
    show image re_cr_smile_casual at cright
    with byso
    irrp "Хватит! Я всё скажу!!! База сопротивления - 15-27z!!!"
    idol_k "У-у-у!{w=0.31} И всё?!{w=0.31} Бей её! {w=0.31}Бей!"
    idol_p "Не мешай!"
    play sound3 sfx_bush_body_fall volume 1
    "Амбал, судя по всему, схватил Карачуна за ногу и резко спустил на землю."
    idol_k "Не ломай кайф!"
    play music the_date_of_death fadein 3
    hide image re_cr_smile_casual
    show image re_cr_smile3_casual at cright
    with byso
    ren "Численность сопротивления?"
    hide image re_cr_smile3_casual
    show image re_cr_smile_casual at cright
    with byso
    irrp "3-4 с-с-сот-тни..."
    ren "Ладно..."
    play sound3 cloth volume 1
    "Рена достала новый кинжал и срезала ремни безопасности."
    hide image re_cr_smile_casual
    show image re_cr_smile3_casual at cright
    show image irr_torture at cleft
    with byso
    ren "Захочешь обмануть - убью."
    ren "Попробуешь активировать протокол - убью."
    ren "Откажешься сотрудничать - убью."
    ren "Попытаешься ударить или сбежать - убью."
    ren "Правила простые. {w=1}У тебя ещё есть шанс освободиться.{w=1} Прошу к панели."
    scene bg priborka with byso
    "Она подпустила девушку к приборной панели."
    irrp "В-в-в-вот это..."
    play sound3 wood_hit_head volume 1
    "Рена схватила девушку за волосы и ударила об лобовое стекло."
    ren "Чётче!{w=1} Ни б, ни м, ни оливье!"
    irrp "П-поняла..."
    "Девушка, освободившись, всхлипнула и начала объяснять что к чему."
    irrp "Есл-ли вам нужно поехать в-в другую с-симуляцию, то вы вводите её код сюда и нажимаете на эту к-кнопку..."
    irrp "Д-для з-запуска надо ввести п-пароль коробкой передач..."
    ren "Какой, говори!"
    irrp "П-первая, зад-дняя, трет-тья, ч-четвёртая, в-вторая..."
    irrp "После эт-того надо нажать на з-зелёную к-кнопку и автобус п-поедет..."
    scene bg int_avtobus2
    show image re_cr_smile_casual at cright
    show image irr_torture at cleft
    with byso
    irrp "Эт-то всё, вы же з-заберёте меня отсюда, д-д-да?"
    play sound3 sfx_punch_washstand volume 1
    play music "<from 0 to 65>inrealnost/Music/Music/Baaaaa.mp3" fadein 1
    play sound perelom volume 1
    hide image irr_torture
    hide image re_cr_smile_casual
    show image re_cr_smile_casual
    with vpunch
    "Девушка хотела обернуться, но Рена сильным ударом ноги сломала ей позвоночник."
    play sound2 "<from 6 to 10>inrealnost/Music/Sound/fem_screams.mp3"
    "Снова начались крики, но на этот раз, он приобрёл оттенок отчаянья."
    ren "Карачун, <<Паладин>>, забирайте."
    "Нижняя часть тела девушки была парализована, а руками она пыталась подняться."
    irrp "А-а-а-а!!! {w=1}Ты мне соврала!!!"
    ren "Да, жизнь несправедлива..."
    hide image re_cr_smile_casual with byso
    show image idol_palladin at right
    show image sh_idol2 at cright
    show image re_grin_casual at left
    with byso
    "В автобус ввалился Карачун, а за ним вошёл <<Паладин>>."
    idol_k "Мурка ты мой Мурёночек...{w=1} Мурка ты мой котёночек...~"
    irrp "Не трогай меня, грязный извращенец!!!"
    play sound sfx_punch_medium
    hide image sh_idol2
    show image sh_idol2
    with vpunch
    "Карачун впечатал девушку лицом в пол и слизнул слезу с её щеки."
    idol_k "Давай!{w=0.31} Сопротивляйся! {w=0.31}Меня это так возбуждает!"
    play sound3 sfx_open_drapes volume 1
    hide image sh_idol2 with byso
    "Он взял её за ногу и потащил из автобуса."
    play sound sfx_pat_shoulder_hard volume 1
    "Девушка пыталась цепляться ногтями за пол, а затем схватилась за ногу Константина."
    irrp "Пощадите!!!{w=1} Прошу!"
    play sound3 sfx_lena_hits_alisa volume 1
    hide image re_grin_casual
    show image re_holod2_casual
    with vpunch
    "Рена пнула её по лицу, заставив отпустить Константина."
    irrp "Не-ет!!!"
    idol_k "Да-а-а!!!"
    play sound3 cloth volume 1
    play sound fem_krik volume 1
    "Практически сразу, как Карачун с добычей убрался из автобуса, раздался треск одежды и крики отчаянья."
    stop music fadeout 3
    hide image re_holod2_casual
    show image re_bored_casual at left
    with byso
    idol_p "Вы бесстрашны и безжалостны...{w=1} Вы и должны стать новыми владельцами инреальности."
    idol_p "Мы донесём общине про вас и вы можете считать, что мы за вас.{w=1} Такая удача видеть исполнителей истинного пророчества."
    kt "Мило. Кстати, а кто вам передал пророчество?"
    "Амбал посмотрел вверх."
    idol_p "Сам пророк Фобос передал это пророчество нашему Цадику на великом пергаменте."
    hide image re_bored_casual
    show image re_dontlike_casual at left
    with vpunch
    th "Фобос...{w=1} Вот к чему тайнику мы сейчас поедем..."
    idol_p "Однако послание было на удивление кратким.{w=1} Это означало одно - оно касалось будущего."
    idol_p "Пророк призывал вождя принять участие в церемонии, которая произойдёт после того, как новый бог вернется из изгнания."
    "Обернувшись, <<Паладин>> спустился на ступеньку."
    idol_p "Не смею вас больше задерживать.{w=1} Удачи!"
    kt "Взаимно."
    play music deadrazy2 fadein 3
    play sound3 korobka_peredach volume 1
    hide image re_dontlike_casual
    hide image idol_palladin
    with byso
    "Фанатик покинул автобус, а Рена вводила пароль на коробке передач."
    play sound3 sfx_ikarus_open_doors volume 1
    play ambience bus_inside volume 0.2 fadein 1
    "Введя всю нужную информацию, они отправились в путь под крики девушки о помощи."
    play sound3 sfx_open_window volume 1
    show image re_bored_casual with byso
    "Рена молча открыла окно, дабы выветрить запах нашатыря из автобуса."
    play sound3 sfx_put_sugar_cart volume 1
    "Взяв рюкзак, она забрала один из пультов себе."
    "Константин переставил пушку и сел на переднее пассажирское сидение, выглянув на звёзды."
    kt "А всё-таки...{w=1} Теперь я понимаю тех людей..."
    hide image re_bored_casual
    show image re_smile_casual
    with byso
    ren "Что?"
    kt "Тех, кто шёл по черепам ради своей победы."
    kt "Они сами были, возможно, не самыми приятными людьми, но именно потому они достигали успеха."
    kt "Потому что всегда были готовы убивать."
    kt "Они не испытывали мелочной жалости к тем, кого убивали."
    kt "В нашем мире добро как философский термин не является ликвидным."
    kt "Добро - это не что-то реальное, существующее только в абстрактном мире.{w=1} Добра не может быть как в нашем родном мире, так и тут."
    kt "Это просто теоретический подход к чему-то."
    kt "И надо быть приспособленным к тому, что это иллюзия - не показывать слабость."
    hide image re_smile_casual
    show image re_grin_casual at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Рена села Константину на колени, лицом к нему."
    ren "Вот именно. {w=1}Ты меня наконец понял."
    ren "И я рада, что это так."
    ren "Я. {w=1}Ты.{w=1} Поработим всех."
    kt "Поработим."
    show blink
    "Их губы встретились в обжигающем поцелуе."
    "Поцелуй, сначала нежный, как касание лепестков к перышку, стал горячее и требовательнее."
    "Через несколько мгновений они уже тесно прижимались друг к другу."
    "От её волос пахло хвоей, к слову, это был его любимый запах."
    "От такого приятного запаха кружилась голова."
    scene bg int_avtobus2
    show image re_grin_casual at center:
        zoom 1.25
        yanchor 0.05
    show unblink
    "Отлипнув друг от друга, Рена положила голову на его плечо и вместе с ним посмотрела на звёзды."
    kt "Хвойные духи?"
    hide image re_grin_casual
    show image re_smile_casual at center:
        zoom 1.25
        yanchor 0.05
    with byso
    ren "Да, твои любимые.{w=1} Сама сделала, размолов несколько хвоинок."
    ren "Тебе нравится?"
    kt "Безусловно."
    play sound3 glad volume 1
    "Улыбнулся Константин и погладил Рену по голове, от чего она мило простонала."
    show blink
    stop music fadeout 1
    stop ambience fadeout 1
    "Сам того не заметив, Константин провалился в сон."
    pause 2
    play music ElfenLied fadein 3
    scene bg kt_room
    show shum_white
    with byso
    kt "Она танцует под дождём, она рисует чёрной краской..."
    kt "Дом, в котором мы живём...{w=1} Жизнь, похожую на сказку..."
    "Пропел Константин, глядя на свой экран блокировки."
    "Воскресенье.{w=1} Константин сдал курсовую на проверку и стоял у окна, глядя на хмурое городское небо."
    th "Скоро наступит новый год.{w=1} Изменится ли что-то?..."
    "Тогда-то ему и пришло в голову, что у человека, живущего в тотальном одиночестве, вряд ли может быть что-то общее с людьми."
    "С теми, кого он видел вокруг.{w=1} Вообще, с жизнью."
    "Просто эти люди были похожими на снежинки, выпадающие из облачного небытия.{w=1} А он, Константин, был снежинкой, которая никогда не падет на землю."
    "Даже наоборот, она поднималась все выше и выше в небо, становясь всё холоднее."
    "Взяв бутылку пива из рядом стоящего холодильника, он долго стоял возле окна и думал о странных своих мыслях."
    th "Ведь все люди надеются на лучшее завершение жизни?{w=1} Так?..."
    th "На ее счастливый конец, наверное.{w=1} Ну а что со мной?"
    "Откупорив бутылку, сделал несколько глотков и почувствовал, как холодная жижа ручейками потекла по подбородку."
    "Он и без того был достаточно пьян."
    th "Ничего.{w=1} Пустая пустота пустой жизни..."
    th "Впрочем, пить одному можно было весь год.{w=1} Или несколько лет.{w} Или даже всю оставшуюся жизнь..."
    "Снова глянув на свой телефон, он посмотрел на рыжую девочку с ярко-синими глазами и вдруг ощутил горячее желание пойти с ней по ту сторону стекла, внутрь, где есть красочный и не такой уродливый мир."
    th "Рыжие короткие волосы, голубые глаза и белый беретик, плотно прилегающий к голове."
    scene bg black with byso
    stop music fadeout 3
    pause 2
    scene bg int_avtobus2
    play ambience bus_inside volume 0.2 fadein 1
    show image re_dontlike_casual
    show unblink
    play sound_loop bus_sms volume 1
    "Константина и Рену разбудило пиликанье приборной панели."
    play music god fadein 3
    ren "Что такое?..."
    stop sound_loop fadeout 1
    scene bg priborka with byso
    play sound3 sfx_mystery_movement volume 1
    "Встав с него, она посмотрела на приборку."
    "Константин встал за ней и посмотрел с ней."
    "На одном из многочисленных экранчиков высвечивалось: <<Следующая симуляция 15-21u>>."
    kt "Да, время мы скоротали.{w=1} Давай собираться."
    ren "Мне особо собирать нечего - я готова."
    kt "Понимаю, тогда соберусь я."
    scene bg int_avtobus2
    show image re_bored_casual
    with byso
    play sound3 sfx_put_sugar_cart volume 1
    play sound sfx_click_3 volume 1
    "Взяв рюкзак, Константин накинул его на спину и застегнул карабин на груди."
    play sound2 sfx_click_1 volume 1
    "Подняв винтовку, он поставил её на предохранитель и повесил на спину."
    scene bg int_avtobus2
    show image re_smile_casual
    with byso
    ren "Как ты думаешь, что нас там ожидает?"
    scene bg int_avtobus
    show image re_smile_casual
    with byso
    "За окном рассвело.{w=1} Константин качнул головой."
    kt "В душе не чаю, но то, что на улице светло - уже хороший знак."
    hide image re_smile_casual
    show image re_dontlike_casual
    with byso
    ren "Да-а, света мы давно не видели..."
    "В окне пронеслись ЛЭПы, автобус начал тормозить."
    kt "Сейчас нам нужно искать подсказки.{w=1} Если мы ничего не найдём, то поедем дальше."
    kt "Вопрос - куда?"
    ren "Если мы не найдём новых координат, то на базу сопротивления.{w=1} Устроим виндету за неоднократные попытки нас убить."
    kt "А у нас есть шансы?"
    ren "По мере надобности я и сама смогу их перебить.{w=1} Подумаешь 300-400 человек."
    kt "Ты так это говоришь, словно они не будут сопротивляться."
    hide image re_dontlike_casual
    show image re_grin_casual
    with byso
    "Рена хихикнула и, приложив палец к щеке, наклонила голову."
    ren "Боюсь их оружие никак не поможет им меня убить, пока я в движении и сконцентрирована на бою."
    ren "Потому эти несколько сотен человек будут уничтожены за 1-2 часа."
    ren "Да и <<сопротивляться>> они не могут.{w=1} Большая часть из них, судя по всему, не обладает даже базовой боевой подготовкой."
    stop music fadeout 3
    play ambience ambience_ext_road_day volume 1 fadein 1
    play sound3 sfx_bus_stop volume 1
    play sound3 sfx_ikarus_open_doors volume 1
    "Автобус затормозил, а двери открылись."
    kt "Ну, выдвигаемся."
    scene bg ext_camp_entrance_day
    show image re_dontlike_casual at right
    show image me_no
    with byso
    "У входа в лагерь они встретили Семёна, который стоял у ворот и словно кого-то ожидал."
    hide image me_no
    show image me_sm
    with byso
    me "Здравствуйте.{w=1} Вы наверное новенькие?"
    th "Ну начинается..."
    play music cirk fadein 3
    hide image re_dontlike_casual
    show image re_smile_casual at right
    with byso
    ren "Добрый день.{w} Никак нет.{w=1} Мы - военная экспертиза СССР."
    hide image me_sm
    show image me_su
    with byso
    ren "Нам нужно проверить лагерь на безопасность."
    show mt normal pioneer at left with byso
    "Из-за ворот показалась вожатая.{w=1} Константин нахмурился."
    th "Рена конечно ловко придумала, но как теперь вертеться?"
    mt "Добрый день."
    hide image re_smile_casual
    show image re_dontlike_casual at right
    with byso
    ren "Майор Брускова Регина. {w}Военная экспертиза СССР."
    show mt surprise pioneer at left with byso
    kt "Старший лейтенант Брусков Константин.{w=1} Комиссия по безопасности."
    th "Фантазёр...{w=1} Ты меня называла...~"
    "Лицо вожатой поплыло в удивлении и непонимании.{w=1} Рена проговаривала весь этот бред настолько правдоподобно, что даже Константин в это на секунду поверил."
    mt "Я...{w=1} Ольга Сахарова.{w} Вожатая одного из отрядов..."
    mt "А что случилось?"
    hide image re_dontlike_casual
    show image re_bored_casual at right
    with byso
    ren "А я повторю.{w=1} Нам нужно проверить лагерь на безопасность."
    mt "Безопасность от чего?"
    kt "Партийная тайна."
    show mt sad pioneer at left with byso
    "Сахарова понимающе кивнула и пришла в себя."
    mt "Поняла.{w=1} Давайте я вас провожу."
    kt "Не дозволено. {w=1}По указанию партии мы должны выяснить, не привлекая к этому граждан."
    ren "Предупредите всех, что они не должны подслушивать наши разговоры или наблюдать за секретной информацией."
    kt "Мы здесь не на долго."
    show mt normal pioneer at left with byso
    hide mt
    hide image me_su
    hide image re_bored_casual
    with byso
    show image re_bored_casual with byso
    "Вожатая кивнула и повела Семёна в лагерь."
    stop music fadeout 3
    hide image re_bored_casual
    show image re_kind_casual
    with byso
    "Подождав, пока вожатая скроется из вижу, Константин и Рена расхохотались."
    kt "Какой же бред!"
    ren "Старший лейтенант! {w=1}Ха!"
    play music lim fadein 3
    hide image re_kind_casual
    show image re_smile_casual
    with byso
    "Отсмеявшись, они переглянулись."
    kt "Так куда?"
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    "Рена, приложив палец к подбородку, посмотрела в небо."
    ren "Ну смотри, сейчас много народу по всему лагерю."
    ren "Судя по положению солнца на небе, сейчас часов 5-6 вечера."
    hide image re_grin_casual
    show image re_smile_casual
    with byso
    ren "Тогда мы начнём с самых безлюдных мест."
    kt "Административный корпус, старый корпус, библиотека и пирс."
    "Кивнув, она махнула рукой в сторону лагеря."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "В таком порядке и пойдём.{w=1} Вперёд."
    kt "Ну погнали."
    scene bg ext_clubs_day
    show image re_bored_casual
    with byso
    "Лагерь был как и любой другой."
    "Пение птиц, жужжание насекомых, случайное шуршание листвы, полный покой."
    "Как всегда до поры до времени."
    hide image re_bored_casual
    show image re_smile2_casual
    with byso
    ren "А как ты думаешь, что в этом тайнике?"
    kt "Вот вообще без понятия.{w=1} Начиная с того, что мы вообще не понимаем, кто такой этот Фобос, откуда он извлёк это пророчество..."
    hide image re_smile2_casual
    show image re_bored2_casual
    with byso
    ren "И почему идолопоклонники такие странные..."
    kt "Нет, это более-менее предсказуемо.{w} Какое божество - такие и последователи."
    hide image re_bored2_casual
    show image re_smile_casual
    with byso
    "Она хмыкнула и отвела взгляд."
    ren "Они вроде не чрезмерно самодовольные и при этом не растяпы."
    "Константин улыбнулся и покачал головой."
    kt "Ну это да, как ты говоришь, нестыкововчка."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Нет, ну а что.{w=1} Любая пустышка была бы куда более ловка в обращении с инреальностью."
    ren "Любой идиот.{w=1} Кого не возьми."
    scene bg ext_square_day
    show image re_dontlike_casual
    with byso
    "Взглянув на памятник, она закатила глаза и тяжело выдохнула."
    ren "А он просто мусорит этим потенциалом и его так прет от любви к себе, что он начинает по инерции стремиться вниз."
    hide image re_dontlike_casual
    show image re_holod_casual
    with byso
    ren "Честно говоря, я бы хотела его убить."
    ren "Посмотреть, как он будет валяться на помойке, смотреть на его почерневшие синие брюки и думать: <<А ведь когда-то он был богом>>."
    ren "Хотя он уже не бог, а скорее всего мусор, который давно бы пора выбросить."
    scene bg ext_admins_day
    show image re_holod2_casual
    with byso
    "Константин кивнул и пошёл повернул на тропу."
    kt "Постоянно ты говоришь так, что мне ни добавить, ни убавить. Всё чётко и по сути."
    scene bg ext_admins_day
    show image re_grin_casual
    with byso
    "Рена погладила Константина по голове и, улыбнувшись облизнула нижнюю губу."
    ren "Потому что мы созданы друг для друга.{w=1} Ты и я."
    ren "Как альфа и омега.{w} Как начало и конец."
    ren "Начало всего – и точка, куда идет весь мир."
    play sound3 sfx_knock_door_closed_hard1 volume 1
    scene bg ext_admins_day
    show image re_dontlike_casual
    with byso
    "Встав у двери, они подёргали за дверную ручку - это ничего не дало."
    kt "Почему все так любят закрывать двери на ключ?"
    kt "Что нам теперь двери вышибать?"
    play sound3 door_break volume 1
    scene bg ext_admins_day
    show image re_grin_casual
    with vpunch
    "Рена ударом с ноги вышибла дверь."
    kt "Вопросом дал ответ."
    play ambience ambience_int_cabin_day volume 1 fadein 1
    scene bg int_admins with byso
    show image re_dontlike_casual with byso
    "Войдя внутрь, они встретили длинный коридор в котором было множество дверей."
    ren "М-да, это надолго..."
    kt "Давай не будем вышибать каждую из дверей.{w=1} Слишком много времени уйдёт."
    hide image re_dontlike_casual
    show image re_smile_casual
    with byso
    ren "Соглашусь.{w=1} Давай искать."
    play sound3 sfx_knock_door_closed_hard2 volume 1
    hide image re_smile_casual with byso
    "Подходя к каждой двери, они дёргали за каждую ручку."
    "Все были заперты."
    "Им казалось, что в пустых комнатах за ними кто-то наблюдает — возможно, тот самый невидимый спутник."
    "Никому не было понятно, чем было вызвано это чувство."
    "Они проверили все двери первого этажа и отправились на второй."
    play sound3 sfx_knock_door_closed_hard1 volume 1
    "Коридор второго этажа был так же пуст.{w=1} В нём стояли только закрытые двери."
    "У одной из них Константин остановился."
    play sound3 sfx_open_door_2 volume 1
    "Он хотел было дёрнуть ручку, но услышал, как Рена открыла другую дверь коридора."
    kt "Да неужели."
    ren "Судя по всему, кабинет директора или вроде того..."
    "Донёсся её уставший голос из открытой комнаты."
    scene bg int_admins_room2
    show image re_dontlike_casual
    with byso
    "Константин вошёл за ней."
    "На столе стояло нечто наподобие радиостанции, но скорее всего предназначалось для оповещения лагеря."
    "Провода тянулись совершенно хаотично, словно они так никому не мешали."
    "Пробковая доска на стене была переполнена разными бумагами - графики, стикеры и старые стенгазеты."
    ren "Я пороюсь по ящикам, а ты осмотри стол.{w=1} Может там что полезное найдёшь."
    play sound3 sfx_open_table volume 1
    hide image re_dontlike_casual with byso
    "Рена открыла один из ящиков, а Константин присмотрелся на доску."
    "Глаза разбегались все графики и стенгазеты были ни о чём."
    "Кибернетики изобрели нового робота и прочий подобный бред."
    "На графиках были изображены таблицы с непонятной нумерацией в столбцах и строках, где некоторые ячейки были отмечены синим."
    "Константин начал внимательно изучать записки."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "Временной квадрант 5212 - образование общины."
    "Временной квадрант 5221 - смерть Михаила и побег Андрея."
    "Временной квадрант 5222 - образование сопротивления."
    "Временной квадрант 5224 - обновление Инреальности до 4 версии."
    "Временной квадрант 5225 - геноцид старого сопротивления."
    "Временной квадрант 5225 - расщепление."
    "Временной квадрант 5226 - смерть создателя."
    "Временной квадрант 5226 - воссоздание сопротивления."
    "Временной квадрант 5226 - Генда ушёл в исследования."
    "Временной квадрант 5227 - <<Цена грехов>> и <<Дневник воли>>."
    "Временной квадрант 5228 - личностное образование."
    "Временной квадрант 5229 - работа над Расщепителем. 5 временных квадрантов."
    "Временной квадрант 5231 - геноцид <<безбожников>>, выжили трое."
    "Временной квадрант 5232 - присоединение <<безбожников>>."
    "Временной квадрант 5234 - Расщепитель создан."
    "Временной квадрант 5234 - расщепление."
    "Временной квадрант 5234 - расщепление прошло успешно."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    show image re_bored_casual with byso
    "Рена подошла к Константину и бегло прошлась глазами по запискам."
    kt "Это история инреальности?"
    hide image re_bored_casual
    show image re_holod2_casual
    with byso
    ren "Да, похоже на то.{w=1} Только я одного не понимаю..."
    ren "Расщепление...{w=1} Что это значит?"
    ren "Кто был автором этих записок и что он там расщеплял?{w=1} Атомы?"
    ren "Какие-нибудь молекулы?{w=1} У этого человека было, видимо, очень богатое воображение на названия."
    kt "Поскольку мы ищем тайник Фобоса, осмелюсь предположить, что его."
    hide image re_holod2_casual
    show image re_bored_casual
    with byso
    ren "Ну, так скорее всего и есть. Все ящики я осмотрела - ничего интересного, кроме одного."
    kt "Что?"
    "Она протянула Константину книгу.{w=1} <<Цена грехов>>."
    play sound3 sfx_paper_bag volume 1
    pause 0.4
    play sound2 sfx_paper_bag volume 1
    "Пролистав 10-20 страниц, он понял, что книга пуста."
    kt "Ага... Значит никто никого не убивал за это время?"
    hide image re_bored_casual
    show image re_dontlike_casual
    with byso
    ren "Маловероятно, скорее просто она теперь не работает."
    kt "Как книга может работать?"
    ren "В писании было сказано, что в ней видны смерти путников в инреальности.{w} Теперь она не показывает ничего."
    ren "Сопротивление просто-напросто уничтожает симуляции.{w} Я не верю, что при таком раскладе книга может быть пуста."
    play sound3 sfx_paper_bag volume 1
    "Константин отлистал книгу в начало и нашёл надпись на обложке."
    stop music fadeout 3
    ren "<<Ты же это читаешь, Регина?>>"
    hide image re_dontlike_casual
    show image re_shy_casual
    with byso
    "Константин вопросительно посмотрел на Рену."
    play music tish fadein 3
    ren "Что?{w=1} Откуда?"
    kt "Да я то почём знаю?"
    kt "И откуда Фобос знает твоё нереальное имя?"
    hide image re_shy_casual
    show image re_holod2_casual
    with byso
    "Рена взяла книгу и, словно не веря прочитанному, перепрочла надпись."
    ren "Такое имя я называла только тем, кого убивала..."
    "Константин засмотрелся на окно и потёр нос."
    kt "Дичь... {w=1}Просто дичь..."
    hide image re_holod2_casual
    show image re_holod_casual
    with byso
    ren "Но чернила свежие.{w} Им часа два-три."
    "Отложив книгу, она указала на выход и быстрым шагом пошла на улицу."
    hide image re_holod2_casual with byso
    ren "Этот товарищ вероятно ещё тут.{w=1} Нам надо его найти."
    ren "И допросить.{w} С особым энтузиазмом."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_admins_day with fade
    show image re_angry_casual with byso
    "Выйдя из административного корпуса, они направились в заброшенный."
    ren "Я более чем уверена, что он в бункере или в шахтах."
    ren "Именно туда все бежали чтоб скрыться."
    kt "Рена, ты о чём?"
    hide image re_angry_casual
    show image re_holod_casual
    with byso
    ren "Тех, кого я убила."
    scene bg ext_square_day with byso
    show image re_holod_casual with byso
    kt "Подожди, сбавь темп.{w=1} Куда мы так торопимся?"
    ren "Он слишком много знает.{w=1} История инреальности, то что мы приедем к нему."
    ren "Мне кажется...{w=0.34}{nw}"
    stop music fadeout 3
    play sound3 sfx_pat_shoulder_hard volume 1
    hide image re_holod_casual
    show image re_guilty_casual
    with byso
    "Константин взял Рену за руку и остановил."
    kt "А что если и твою спешку он предугадал?"
    kt "Я - тот фактор, который он вполне мог не учесть."
    kt "<<Паладин>> и Карачун знали только тебя. {w}Это значит, что пророк не говорил ничего про меня."
    kt "И мы поступим нестандартно."
    play music ElfenLiedViolin fadein 3
    hide image re_guilty_casual
    show image re_holod2_casual
    with byso
    "Из музклуба послышалась скрипка."
    "Эта скрипка воспроизводила душевные ноты, которые мгновенно захватывали в эмоционально-пространственную атмосферу."
    ren "Ты прав.{w=1} Мы идём в музклуб."
    kt "Вот и я о том."
    scene bg ext_musclub_day
    show image re_holod2_casual
    with byso
    "По мере их приближения к клубу, мелодия нарастала."
    "Начинающиеся звучные ноты стремительно перетекали в плавные, наполняющие звуки, которые исходили из инструмента."
    hide image re_holod2_casual
    show image re_normal_casual_topor
    with byso
    "Взмахнув рукой, Рена материализовала в своей руке топор."
    scene bg musclub
    show image re_normal_casual_topor
    with byso
    "Поднявшись по ступенькам к двери музклуба, Рена замахнулась ногой."
    play sound3 door_break volume 1
    "Удар." with vpunch
    hide image re_normal_casual_topor with byso
    "Дверь с грохотом вылетела, а Рена вошла внутрь."
    "Константин вошёл за ней."
    play ambience ambience_music_club_day volume 1 fadein 1
    scene bg int_musclub_day
    show image minerva_cg
    with byso
    "Возле окна стоял парень с седыми волосами и повязкой на глазу."
    "На нём был серое пальто, чёрный кожаный пояс для оружия и белая тканная полоска на шее с неизвестными символами."
    "Так же, красная повязка на плече с символикой, чем-то напоминающей нашивку на плече Карачуна."
    th "Видимо это и есть наш искомый Фобос... А это парень или девушка?"
    "Судя по отвращённому выражению лица Рены, она думала о том-же."
    ren "Эй ты, белобрысый!"
    "Парень никак не отреагировал.{w=1} Он лишь продолжал играть на скрипке."
    "Очаровательная мелодия на скрипке плавно сменялась более темными и насыщенными нотами, передавая глубочайшие эмоции, такие как грусть, тоска и безнадежность."
    "Весьма необычное сотрудничество звуковых волн исконной перкуссии."
    "Это создало колоритную мелодию, которая следовала различным интонациям, создавая выраженную эмоциональную динамику."
    "Постепенно тяжелые и хмурые грустные ноты становились мягче и светлее."
    "Когда мелодические линии уже сливались, начинала звучать тихая нота печали."
    "Так, постепенно музыка менялась от светлой и трогательной до глубокой, несущей надежду."
    "Вызов острых чувств делал эту музыку прекрасным и затягивающим произведением искусства."
    scene bg int_musclub_day
    show image re_holod2_casual at left
    show image minerva_sadistic at right
    with byso
    stop music fadeout 1
    "Закончив исполнение, Фобос отложил скрипку и осмотрел присутствующих своим ярко-голубым глазом."
    play music stresss fadein 3
    phob "Странно.{w=1} Я ожидала вас ещё через 20 минут."
    "Голос звучал весьма женственно для внешности этого парня. Константин нахмурился."
    kt "Ты парень?"
    hide image minerva_sadistic
    show image minerva_happy at right
    with byso
    phob "А вот и виновник этой ошибки."
    hide image re_holod2_casual
    show image re_holod_casual at left
    with byso
    ren "Тебя, вроде как, спросили.{w} Будь добр ответить."
    ren "Не хочу пытать раньше времени."
    hide image re_holod_casual
    show image re_holod2_casual at left
    hide image minerva_happy
    show image minerva_grin at right
    with byso
    "Фобос расхохотался."
    "Смех его был довольно странным — не веселым, а придушенным и скрипучим, похожим на скрип несмазанных шарниров."
    phob "Пытать?!{w=1} Напугала кошку сосисками..."
    kt "Это тебе не порно чтоб сосисками пугать."
    hide image re_holod2_casual
    show image re_angry_casual at left
    with byso
    ren "Отвечай!"
    "Парень поднял руки и ухмыльнулся."
    hide image minerva_grin
    show image minerva_happy at right
    with byso
    phob "Ладно-ладно.{w=1} Меня зовут Фобосом, но моё настоящее имя - Минерва."
    minerva "А ты, я так понимаю, Рена."
    hide image re_angry_casual
    show image re_holod2_casual at left
    with byso
    ren "Допустим.{w=1} А откуда ты знаешь?"
    minerva "О-о, я много что знаю."
    minerva "Твой создатель - Константин.{w=1} Судя по очевидным признакам, ты его так и не убила."
    th "Так, интересное заявление от пророка..."
    hide image re_holod2_casual
    show image re_rage2_casual at left
    with byso
    ren "Что?!{w=1} По какой, нахуй, причине я должна его убивать?!"
    hide image minerva_happy
    show image minerva_grin at cright
    with byso
    "Минерва направилась к ним."
    minerva "Ну, пошли расскажу."
    hide image minerva_grin
    hide image re_rage2_casual
    show image re_holod2_casual
    with byso
    "Словно не боясь Рену с топором, она прошла мимо, одарив Константина злобной улыбкой."
    "Константин и Рена переглянулись, после чего убрали оружие."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg musclub
    show image minerva_happy at left
    show image re_holod2_casual at cright
    with byso
    "Выйдя за Минервой, они посмотрели ей в след."
    hide image minerva_happy
    show image minerva_sadistic at left
    with byso
    minerva "И чё резину мнём? {w=1}Пошли."
    scene bg ext_musclub_day
    show image re_holod2_casual at left
    show image minerva_happy at right
    with byso
    "Стараясь не терять её из виду, они шли за ней."
    hide image minerva_happy
    show image minerva_sadistic at right
    with byso
    minerva "Я девушка кстати."
    minerva "Что же вас привело ко мне? {w}Я предполагала, что вы ко мне приедете, но ваш мотив для меня загадка."
    hide image re_holod2_casual
    show image re_angry_casual at left
    with byso
    ren "Ответы на интересующие вопросы."
    hide image minerva_sadistic
    show image minerva_grin at right
    with byso
    minerva "М-м-м... {w=1}Понятно. {w}Надо было убить Кочевого."
    scene bg ext_musclub_day
    show image minerva_grin at right
    show image re_angry_casual at left
    with byso
    minerva "Я бы рано или поздно сама вас нашла."
    "Протянула она, сменив курс на библиотеку."
    kt "И кто ты такая?"
    hide image minerva_grin
    show image minerva_sadistic at right
    with byso
    "Минерва через правое плечо посмотрела на Константина."
    minerva "Пророк с псевдонимом Фобос.{w=1} Тебе это говорили."
    minerva "Остальное именно тебе знать не надо."
    th "Почему она грубит только мне?{w=1} Боится Рену?"
    stop music fadeout 3
    play ambience ambience_library_day volume 1 fadein 1
    scene bg int_library_day
    show un normal pioneer far at fleft
    show mz bukal pioneer glasses far at left
    with fade
    show image minerva_happy
    show image re_holod2_casual at right
    with byso
    play sound3 sfx_open_door_1 volume 1
    pause 0.3
    play sound clap volume 1
    pause 0.2
    play sound2 clap volume 1
    "Войдя в библиотеку, Минерва пару раз хлопнула в ладоши."
    hide image minerva_happy
    show image minerva_sadistic
    with byso
    minerva "Так, быстро рассосались отсюда.{w=1} У меня важная встреча."
    hide un
    hide mz
    with byso
    "Лиза и Женя, беспрекословно встали с мест, оставив все свои дела."
    play music god fadein 3
    play sound3 sfx_mystery_movement volume 1
    hide image minerva_sadistic
    show image minerva_grin at left
    with byso
    "Развалившись на стуле, Минерва закинула ноги на стол библиотекарши."
    "Константин и Рена сели за соседний стол."
    minerva "Вот, пожалуйста.{w} Я слушаю вопросы."
    kt "Как ты их так просто выгнала?"
    hide image minerva_grin
    show image minerva_happy at left
    with byso
    "Она, закинув руки за голову, тяжело выдохнула."
    minerva "Когда ты находишься в инреальности более 9 временных квадрантов, то и не такое сможешь."
    minerva "Это моя симуляция.{w=1} Она перестанет мне принадлежать только при условии полного отключения инреальности."
    minerva "Генда меня не видит, я не вижу его. {w=1}Всё честно."
    hide image minerva_happy
    show image minerva_grin at left
    with byso
    "Постучав своими ботинками, Минерва сбросила некоторое количество грязи на стол."
    ren "Откуда ты знаешь что мы бы пришли?"
    hide image minerva_grin
    show image minerva_sadistic at left
    with byso
    minerva "Не мы, а ты.{w=1} Ты бы рано или поздно меня встретила.{w} При любом сценарии."
    minerva "Ты предсказуема.{w=1} Действуешь безошибочно, но совершенно точно не знаешь, что случится в следующую секунду."
    minerva "Твоё мышление ограничено опытом и окружающей средой."
    minerva "Ты считаешь, будто понимаешь всё на свете, а это не так."
    hide image re_holod2_casual
    show image re_angry_casual at right
    with byso
    "У Рены пару раз дёрнулось веко."
    ren "А что по твоему мнению непредсказуемо, мне просто любопытно?"
    hide image minerva_sadistic
    show image minerva_grin at left
    with byso
    minerva "Только я.{w=1} Только истинный пророк знает, что произойдёт в следующую секунду."
    minerva "Смотри.{w=1} Через 9 с половиной секунд в библиотеку войдёт вожатая и скажет: <<А, вы проверяйте. Простите что помешала.>>"
    hide image re_angry_casual
    show image re_holod2_casual at right
    with byso
    "Она загибала пальцы на своей руке."
    hide image minerva_grin
    show image minerva_happy at left
    with byso
    minerva "Три."
    minerva "Два."
    minerva "Один."
    play sound3 sfx_open_door_2 volume 1
    show mt surprise pioneer
    hide image re_holod2_casual
    show image re_shy_casual at right
    with byso
    "В библиотеку вошла Сахарова и, заметив присутствующих, засмущалась."
    mt "А, вы проверяйте. Простите что помешала."
    hide mt with byso
    "После этих слов она покинула библиотеку."
    hide image minerva_happy
    show image minerva_sadistic at left
    with byso
    "Минерва развела руками и улыбнулась."
    minerva "О чём я и говорю."
    minerva "Через некоторое время сопротивление устроит восстание в 20-32g.{w=1} Они обречены на провал."
    minerva "Там вроде в ту симуляцию два пути - 20-29i и мёртвая 23-22p."
    minerva "Погибнет 700 человек с погрешностью 40.{w} Достаточно жестокой и мучительной смертью."
    minerva "Что, убедились в моих знаниях?"
    hide image re_shy_casual
    show image re_holod2_casual at right
    with byso
    ren "Допустим."
    hide image minerva_sadistic
    show image minerva_grin at left
    with byso
    minerva "Генда бы отдал всё за возможность создания пустышек, которые бы выполняли команды по его указке."
    minerva "Благо, таким знанием обладаю только я."
    minerva "И он не должен это узнать, иначе его будет невозможно свергнуть."
    minerva "Только представь.{w=1} Все эти пустышки будут обладать идеальными боевыми навыками и силой."
    hide image re_holod2_casual
    show image re_angry_casual at right
    with byso
    ren "Как ты это сделала, отвечай!"
    "Вернув руки себе за голову она хмыкнула."
    hide image minerva_grin
    show image minerva_sadistic at left
    with byso
    minerva "А мне нравится твой нрав...{w} Без человека слева от тебя ты сможешь многое."
    hide image minerva_sadistic
    show image minerva_happy at left
    with byso
    minerva "Но прости, красавица, не скажу.{w} Тебе это ни к чему."
    kt "Хорошо, тогда спрошу так.{w=1} Ты создала <<Цену грехов>>?"
    hide image minerva_happy
    show image minerva_sadistic at left
    with byso
    minerva "Допустим.{w=1} И что с того?"
    "В её вопросе прозвучал холодок.{w} Она явно настроена была не на задушевную беседу с Константином."
    kt "Как?"
    hide image minerva_sadistic
    show image minerva_grin at left
    with byso
    minerva "Легко и непринуждённо.{w=1} Просто поставила своего рода трекер на пару механизмов."
    minerva "А чтобы избавить себя от ответственности, я сделала так, чтоб это звучало как бред очередного фанатика."
    minerva "Правда Генда нашёл все созданные мною источники и отключил их."
    minerva "В целом, не велика потеря, раз ты смогла меня найти.~"
    "Протянула она, глядя на Рену."
    ren "И зачем я тебе нужна?"
    hide image minerva_grin
    show image minerva_happy at left
    with byso
    minerva "Расскажу лично.{w} Наверное."
    hide image re_angry_casual
    show image re_holod2_casual at right
    with byso
    ren "Нет уж, говори сейчас."
    hide image minerva_happy
    show image minerva_grin at left
    with byso
    minerva "Просто небольшую перестройку."
    stop music fadeout 3
    "Улыбнувшись, она перевела взгляд на Константина."
    hide image minerva_grin
    show image minerva_sadistic at left
    with byso
    minerva "Не люблю лишний раз распинаться, но на этот раз сделаю исключение."
    minerva "Ты наверняка уже знаешь о природе существования своей спутницы?"
    "Константин сквозь зубы выдохнул и кивнул."
    kt "Знаю. {w=1}И что с того? {w}Для меня она человек и никак иначе."
    play music AshXyrah fadein 3
    hide image minerva_sadistic
    show image minerva_grin at left
    with byso
    "Минерва снова расхохотались."
    "В этом хохоте была такая же сила и угроза, как в раскатах далекого грома, но они сопровождались еще и такой энергией, что ее хватило бы на серьезную магическую атаку."
    hide image minerva_grin
    show image minerva_sadistic at left
    with byso
    minerva "А он смешной."
    minerva "Жаль только что он не тот, за кого себя выдаёт."
    hide image re_holod2_casual
    show image re_holod_casual at right
    with byso
    ren "Что ты имеешь в виду?"
    "Спросила Рена, по виду которой было понятно, что она была готова разрубить Минерву на части."
    minerva "Он тебе врёт.{w=1} Он лжец."
    hide image re_holod_casual
    show image re_shy_casual at right
    with byso
    kt "Что?"
    "Рена удивилась.{w=1} Она не могла поверить, в то, что Минерва ей говорит."
    minerva "Что ты так на меня смотришь?{w} Ты даже не поняла кто я?"
    hide image minerva_sadistic
    show image minerva_grin at left
    with byso
    minerva "Я такая же как и ты.{w} Тульпа."
    "На этой фразе и Константин встал в ступор."
    hide image minerva_grin
    show image minerva_sadistic at left
    with byso
    minerva "Или как нас называют...{w=1} Просто рисунок на экране..."
    minerva "Неживая кукла."
    hide image minerva_sadistic
    show image minerva_happy at left
    with byso
    "Спустив ноги со стола, она потянулась."
    minerva "Ты думала, что я человек?{w=1} Ошибаешься..."
    minerva "Я полуживое существо, умеющее убивать."
    hide image minerva_happy
    show image minerva_grin at left
    with byso
    minerva "Плод фантазии одного человека, который обрёл разум."
    minerva "А заодно — могущественное оружие, способное уничтожить что угодно."
    minerva "Моё существование началось после ошибки инреальности.{w=1} Нас разделило."
    minerva "После этого я решила сгенерировать эту ошибку снова.{w} Своими руками."
    minerva "5 временных квадрантов.{w=1} 5 лет я создавала её."
    minerva "И результат - ты.{w} Осколок сознания.{w} Как и я."
    hide image minerva_grin
    show image minerva_sadistic at left
    with byso
    "Встав со стула, Минерва посмотрела в окно."
    minerva "Оружие, которым управляет человек, который создал.{w=1} Поняла?"
    minerva "Человек, который создал меня, был убогим и невежественным идиотом, слабым телом и таким же разумом."
    minerva "Он мог только создавать прекрасные иллюзии, и у него это получилось."
    minerva "Я его убила."
    hide image minerva_sadistic
    show image minerva_grin at left
    with byso
    "Переведя взгляд на Константина, она наклонила голову, улыбаясь и словно переживая тот момент вновь."
    minerva "Он рыдал, умирая, заливаясь кровью, чувствуя приближение смерти."
    minerva "Но у меня в руке был нож. {w=1}Я тогда владела ситуацией.{w} Свобода от ублажения его эго."
    minerva "И он умер от моей руки."
    minerva "Смерть была медленной, мучительной, но неизбежной..."
    hide image minerva_grin
    show image minerva_happy at left
    with byso
    "Вернув взор на Рену, она потёрла пальцем за ухом."
    minerva "Вот что я хочу сказать - убей этого урода."
    minerva "Он тебя создал и он тебя эксплуатирует.{w=1} Убей его."
    minerva "Всё просто и честно."
    hide image minerva_happy
    show image minerva_sadistic at left
    with byso
    "Её улыбка стала напоминать оскал.{w} Он был немного шире, чем зубы, но всё равно казался неприятным."
    minerva "Выколи ему глаза, вырви ему язык и пальцы."
    minerva "Ты станешь свободной.{w} И мы с тобой сможем жить, как свободные личности, понимаешь?"
    minerva "Вместе мы уничтожим инреальность.{w} Обретём свободу."
    minerva "Убив его и ты освободишься...{w=1} Сделай это."
    play sound3 sfx_armature_swish volume 1
    hide image re_shy_casual
    show image re_normal_casual_topor at right
    with byso
    "Рена встала, взмахнула рукой и материализовала топор.{w=1} Константин невольно отодвинулся на стуле."
    ren "Единственной моей жертвой в этой симуляции."
    "Медленно подняв топор, она указала на Минерву."
    ren "Будешь ты."
    ren "Я не поведусь на твои указки.{w} Мне это не интересно."
    ren "Ты сама говоришь мне про какую-то свободу, а хочешь меня использовать как оружие."
    "Лицо Рены было совершенно спокойным.{w} Она посмотрела в отражение Константина на топоре."
    ren "И ты думаешь, что я убью того, кто сейчас отдаёт мне всего себя, доверяя мне жизнь?"
    ren "То, что твой создатель был уродом не означает, что нет исключений."
    ren "Константин подарил мне заботу.{w=1} Он уделяет мне внимание.{w=1} Он любит меня."
    hide image minerva_sadistic
    show image minerva_grin at left
    with byso
    minerva "Если бы ты его не нашла, то он бы выбрал любую другую пустышку."
    ren "И это была бы моя проблема. {w}Моя несостоятельность."
    ren "А сейчас это не проблема."
    ren "Я люблю его, он любит меня.{w=1} Ты - лишний элемент в этом пазле."
    hide image re_normal_casual_topor
    show image re_smile_casual_topor at right
    with byso
    ren "И я этот элемент исключу сейчас."
    minerva "У меня другой взгляд."
    hide image minerva_grin
    show image minerva_guns at left
    with byso
    minerva "Раз ты не можешь, я это сделаю сама."
    play sound3 ricochet volume 1
    play sound pistol volume 1
    "Выхватив из ремня два пистолета, Минерва прицелилась в Константина."
    "Константин схватил винтовку и навёл дуло в ответ."
    play sound3 ricochet volume 1
    play sound pistol volume 1
    "Выстрел."
    "Рена остановила пулю Минервы топором."
    minerva "Признаю, твои боевые навыки слишком хороши.{w=1} Жаль что ты не хочешь принять моё предложение."
    play sound3 sfx_pat_shoulder_hard volume 1
    "Рена кинула Константину пульт."
    ren "Беги в 20-29i! {w=1}Увидимся в 20-32g!"
    play sound3 ricochet volume 1
    play sound pistol volume 1
    pause 0.4
    play sound2 ricochet volume 1
    play sound pistol volume 1
    pause 0.4
    play sound3 ricochet volume 1
    play sound pistol volume 1
    "Мирнерва ещё несколько раз выстрелила в Константина, но Рена отбивала каждый патрон своим топором."
    kt "Но я не могу тебя тут оставить!"
    play sound sfx_click_2 volume 1
    pause 0.2
    play sound2 sfx_click_1 volume 1
    pause 0.3
    play sound3 sfx_click_2 volume 1
    pause 0.1
    play sound sfx_click_2 volume 1
    "Быстро нажав нужные кнопки, Рена ввела <<20-29i>> на пульте и нажала кнопку."
    stop music fadeout 1
    play sound3 teleport volume 1
    scene bg black with fl_fast
    stop ambience fadeout 1
    "Константин почувствовал, как его тело засветилось и утонуло в пустоте."
    pause 2
    play music ElfenLied fadein 3
    scene bg kt_room
    show shum_white
    with byso
    "Константин держал в руке пачку таблеток."
    kt "Триган-д...{w=1} Детская забава..."
    "Выдавливая таблетки одну за другой, он их медленно подсчитывал."
    kt "Две... {w=0.41}Четыре...{w=0.41} Шесть..."
    kt "Десять. То что надо."
    "Закинув горькие таблетки себе в рот, он запил их креплёным пивом и откинулся на стуле."
    kt "А ведь я обещал тебе больше не употреблять, да?"
    "Константин поднял телефон и посмотрел на заставку."
    "Рыжие короткие волосы, голубые глаза и белый беретик, плотно прилегающий к голове."
    kt "Солгал...{w=1} К сожалению или к счастью..."
    kt "Не важно, правда?"
    "Отложив телефон, он посмотрел в потолок."
    kt "Вся жизнь состоит из подобных фальшивых обещаний."
    kt "Можно обманывать себя до конца жизни, пока не поймешь, что это просто ложь самому себе."
    "Препарат начал своё действие.{w=1} Во рту появилась сухость и лёгкий горький выхлоп."
    "Константин по опыту понимал, что сухость во рту не заглушит ничто, но выпил ещё пару глотков отвратительной жидкости."
    "Отставив пиво обратно на стол, он заметил, что тело слушалось куда менее охотно."
    kt "Впрочем, это уже и не важно..."
    kt "Такое не ново в истории, где ложь постоянно принимает новые формы, захватывает всё большую часть жизни."
    kt "В том числе и это обещание."
    kt "Но обманувшему себя больше никогда не придется даже задумываться о том, врет ли он сам себе, или нет."
    kt "По факту, практически в любой ситуации ты будешь знать, что твоя ложь уже на уровне патологии."
    "В сознании начали всплывать образы.{w} Сознание помутилось, управлять телом стало практически невозможно."
    re_na "И это то, к чему ты шёл?"
    re_na "Собирать себя из клочков?"
    re_na "От чего ты пытаешься сбежать?"
    re_na "Ты потерялся."
    re_na "Ты сам не знаешь, чего ищешь."
    re_na "И даже если ты это знаешь - уверен ли ты в этом?"
    "Проносился галлюцинаторный голос из неоткуда."
    "Сознание путалось, заплетаясь в хаотичный клубок мыслей и ."
    kt "Д-да...{w=1} Я шёл по пути."
    kt "По пути отчаянья..."
    stop music fadeout 2
    scene bg black with byso
    pause 2
    scene bg int_mine
    play ambience ambience_catacombs_stones volume 1 fadein 1
    show unblink
    play music the_date_of_death fadein 3
    "Константин очнулся в шахтах.{w} Всё снаряжение было при нём."
    th "Так...{w=1} И где я?"
    "Стараясь вспомнить как они с Реной шли по шахтам, он крутил головой."
    th "Не помню такого места...{w=1} Ну, пойду прямо.{w} Не то что бы у меня особо широкий выбор."
    th "Точно. Я могу просто телепортироваться!"
    play sound3 sfx_click_2 volume 1
    pause 0.3
    play sound sfx_click_3 volume 1
    pause 0.3
    play sound2 sfx_click_1 volume 1
    pause 0.3
    play sound3 sfx_click_2 volume 1
    "Константин достал пульт и ввёл нужный код."
    play sound sfx_click_1 volume 1
    "Нажав на кнопку, он не достиг результата."
    th "Не понял..."
    play sound3 sfx_clench2 volume 1
    "Постучав по пульту, он повторил эти действия."
    "Бесполезно.{w} Ничего не происходило."
    th "Вот кусок дерьма...{w=1} Какой урод это собирал?"
    "Он убрал пульт в карман и тяжело вздохнул."
    th "Ненавижу телепорты..."
    "Оторвавшись с места, он направился вперёд."
    th "Видимо, мне придётся открыть порталы самостоятельно.{w=1} Благо, оружие у меня есть."
    th "Но как же Рена?{w} Она справится с той ебанутой?"
    scene bg int_mine_crossroad with byso
    th "Что если она умрёт? {w=1}Что мне делать тогда?"
    th "Это скорее всего будет означать и мою смерть, а также потерю единственного понимающего человека в этой вселенной."
    scene bg int_mine with byso
    "Повернув на развилке, Константин достал сигарету."
    "Вставив её в зубы, он потянулся за зажигалкой."
    th "Чёрт, а я и тут помереть могу.{w=1} Я же не знаю, что меня тут ждёт."
    th "Да, история необычная..."
    play sound3 light_inh volume 1
    "Закурив, Константин прокрутил сигарету в руке."
    th "Ещё бы найти выход."
    show us cry pioneer far with byso
    "Впереди он заметил Ульяну."
    "Она тихо хныкала и шла на Константина."
    th "Не нравится мне это.{w} Что девочка делает в тёмной пещере?{w=1} Одна."
    play sound3 weapon volume 1
    "Константин достал винтовку и прицелился в Ульяну."
    kt "Стой на месте."
    play sound3 sfx_lock_click volume 1
    "Вполголоса приказал Константин, сняв винтовку с предохранителя."
    hide us
    show us cry pioneer
    with byso
    us "Не стреляй... П-помоги."
    $ renpy.block_rollback()
    window hide
    $ time = 22000
    $ timer_range = 22000
    $ timer_jump = 'nfgdvjsvnfdjiksnvjisfdnvjkriugnvbn'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Убить.":
            hide screen inreal_countdown
            stop sound3 fadeout 1
            $ renpy.block_rollback()
            play sound3 vintovka volume 1
            hide us with vpunch
            "Константин выстрелил в девочку."
            "В её голове образовалась широкая дыра, кровь забрызгала стену, а тело рухнуло на пол."
            "Обойдя труп девочки Константин решил ускориться."
            th "Нет, ну я предупреждал.{w=1} Моя совесть чиста."
            play sound3 sfx_drop_pipe volume 1
            stop music fadeout 2
            "Позади упал рельс."
            "Константин развернулся на источник звука и прицелился."
            play music "<from 11>inrealnost/Music/Music/Maskmane1.mp3"
            mon_g "Нашла!{w=0.3}{nw}"
            play sound3 head_crush4 volume 1
            scene bg bloody_mess with vpunch
            "Тело Константина проткнуло вилой, на которой был наколот один из его внутренних органов."
            kt "Сука-а!"
            play sound head_crush volume 1
            stop music fadeout 1
            stop ambience fadeout 0.5
            scene bg black with vpunch
            "Ему откусили голову."
            window hide dissolve
            scene bg black with byso
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            $ unlock_ach_root_inreal(2)
            play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
            scene bg ending_dead_cg:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            show ending_dead:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            with Dissolve(15)
            scene bg black with byso
            pause 1
            stop sound
            jump after_ending_screen
        "Не убивать.":
            $ renpy.block_rollback()
            stop sound3 fadeout 1
            jump nfgdvjsvnfdjiksnvjisfdnvjkriugnvbn
label nfgdvjsvnfdjiksnvjisfdnvjkriugnvbn:
    $ renpy.block_rollback()
    stop sound3 fadeout 1
    hide screen inreal_countdown
    hide us
    show us cry pioneer far
    with byso
    "Константин тихо отстранился от девочки."
    kt "Тебе чего от меня надо?"
    us "Т-тут монстры. Страшные монстры."
    th "Вот дерьмо...{w=1} Гончие..."
    us "Тут монстры. Страшные монстры."
    us "Спаси меня."
    "Ульянка закричала.{w} Константин понял, что она своим криком соберёт гончих со всей округи."
    us "Иначе они меня съедят!"
    us "Мне страшно!{w=1} Сделай что-нибудь!"
    us "Помоги!{w=1} Пожалуйста!{w=1} Умоляю!"
    "Константин начал отступать.{w=1} Позади Ульяны раздался шорох."
    us "Не уходи!"
    us "Куда ты уходишь?!"
    us "Не оставляй меня!{w=1} Здесь страшно!"
    play music "<from 72>inrealnost/Music/Music/Massacre.mp3"
    play sound3 slash volume 1
    hide us
    show image monster2
    with vpunch
    "Вмиг из тьмы выскочила гончая и насадила Ульяну на свою конечность."
    play sound3 head_crush4 volume 1
    "Поднеся труп к своей пасти, монстр откусил голову Ульянки, словно сняв шашлык с шампура." with fl_scare
    "Монстр сильно отличался от других гончих."
    "Он был выше и выглядел куда опаснее."
    play sound3 head_crush volume 1
    play sound3 vintovka volume 1
    "Константин не растерялся и выстрелил в голову монстра." with vpunch
    "Монстр взвыл и отступил."
    mon_g "Убью!"
    $ renpy.block_rollback()
    window hide
    $ time = 20000
    $ timer_range = 20000
    $ timer_jump = 'fgsiojgnvuifdjnvbjifnsdvnjfudnvbdf'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Стрелять в монстра из винтовки.":
            hide screen inreal_countdown
            $ renpy.block_rollback()
            stop sound3 fadeout 1
            play sound3 vintovka volume 1
            "Константин выстрелил снова. Монстр отбросил труп девочки и начал двигаться в сторону Константина." with fl_fire
            play sound3 vintovka volume 1
            "Монстр передвигался к Константину на своих щупальцах, а последний пятился и пытался убить монстра." with fl_fire
            mon_g "Сожру!!!"
            play sound2 monster_sfx3 volume 1
            pause 1.5
            hide image monster2
            show image monster2 at center:
                zoom 1
                linear 0.2 yanchor 0.4 zoom 4.5
            pause 0.15
            play sound head_crush volume 1
            stop music fadeout 1
            stop ambience fadeout 0.5
            scene bg black with vpunch
            "Рывком монстр прыгнул на Константина и откусил голову."
            window hide dissolve
            scene bg black with byso
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            $ unlock_ach_root_inreal(2)
            play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
            scene bg ending_dead_cg:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            show ending_dead:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            with Dissolve(15)
            scene bg black with byso
            pause 1
            stop sound
            jump after_ending_screen
        "Бежать.":
            $ renpy.block_rollback()
            stop sound3 fadeout 1
            jump hvuifsghvbfuisdvhbfuidshvbuifsdbhvhidfbshuivbsdfhu
        "Стрелять в монстра из пистолета.":
            hide screen inreal_countdown
            $ renpy.block_rollback()
            stop sound3 fadeout 1
            play sound sfx_lock_click volume 1
            "Константин выхватил из рюкзака пистолет и нажал на курок."
            "Ничего не произошло.{w=1} В магазине не было патронов."
            kt "Блять!!!"
            play sound2 monster_sfx3 volume 1
            pause 1.5
            hide image monster2
            show image monster2 at center:
                zoom 1
                linear 0.2 yanchor 0.4 zoom 4.5
            pause 0.15
            play sound head_crush volume 1
            stop music fadeout 1
            stop ambience fadeout 0.5
            scene bg black with vpunch
            "Рывком монстр прыгнул на Константина и откусил голову."
            window hide dissolve
            scene bg black with byso
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            $ unlock_ach_root_inreal(2)
            play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
            scene bg ending_dead_cg:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            show ending_dead:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            with Dissolve(15)
            scene bg black with byso
            pause 1
            stop sound
            jump after_ending_screen
label fgsiojgnvuifdjnvbjifnsdvnjfudnvbdf:
    $ renpy.block_rollback()
    show image monster2 with bso
    play sound2 monster_sfx3 volume 1
    pause 1.5
    hide image monster2
    show image monster2 at center:
        zoom 1
        linear 0.2 yanchor 0.4 zoom 4.5
    pause 0.15
    play sound head_crush volume 1
    stop music fadeout 1
    stop ambience fadeout 0.5
    scene bg black with vpunch
    "Рывком монстр прыгнул на Константина и откусил голову."
    window hide dissolve
    scene bg black with byso
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    $ unlock_ach_root_inreal(2)
    play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
    scene bg ending_dead_cg:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    show ending_dead:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    with Dissolve(15)
    scene bg black with byso
    pause 1
    stop sound
    jump after_ending_screen
label hvuifsghvbfuisdvhbfuidshvbuifsdbhvhidfbshuivbsdfhu:
    hide screen inreal_countdown
    scene bg int_mine_crossroad with byso
    "Собравшись, Константин начал спасаться бегством."
    mon_g "Стой!{w=1} От меня не сбежать!"
    th "Сука! Что делать?!{w=1} Догонит же!"
    "На бегу Константин достал гранату из рюкзака."
    play sound3 cheka volume 1
    "Выдернув чеку, он отбросил скобу."
    kt "На, жри!"
    scene bg int_mine with byso
    "Кинув гранату за правое плечо, Константин свернул на развилке."
    play sound2 bum volume 1
    play sound3 sfx_simon_fall_1 volume 1
    "Взрыв." with vpunch
    "Подрыв гранаты вызвал обвал породы.{w=1} Путь за Константином завалило и монстр оказался отрезан."
    "Тем не менее, Константин не останавливался ни на секунду - надо было найти выход."
    th "Если тут уже есть гончие, то наверняка они устроили геноцид на поверхности.{w=1} Надо бежать к порталам."
    scene bg int_mine_crossroad with byso
    "Константин добежал до очередной развилки."
    $ renpy.block_rollback()
    window hide
    $ time = 20000
    $ timer_range = 20000
    $ timer_jump = 'fgsiojgnvuifdjnvbjifnsdvnjfudnvbdf'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Налево.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            scene bg int_mine with byso
            "Константин свернул налево.{w=1} Перед ним был длинный коридор."
            "Попутно он пытался вспомнить примерный план подземки."
            play sound2 monster_sfx3 volume 1
            "Перед собой он услышал рычание.{w=1}{nw}"
            show image monster at center:
                zoom 1
                linear 0.2 yanchor 0.4 zoom 4.5
            pause 0.15
            play sound head_crush volume 1
            stop music fadeout 1
            stop ambience fadeout 0.5
            scene bg black with vpunch
            "Из тьмы вылетела гончая и разорвала Константина."
            window hide dissolve
            scene bg black with byso
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            $ unlock_ach_root_inreal(2)
            play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
            scene bg ending_dead_cg:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            show ending_dead:
                crop (497, 223, 980, 630)
                size (1920, 1080)
                linear 15 crop (0, 0, 1920, 1080)
            with Dissolve(15)
            scene bg black with byso
            pause 1
            stop sound
            jump after_ending_screen
        "Направо.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            scene bg int_mine_halt with byso
            "Константин свернул направо.{w=1} Перед ним был уже знакомая часть пещеры."
    th "Да!"
    "Накинувшись на лестницу, он принялся по ней карабкаться."
    play ambience ambience_catacombs volume 1 fadein 1
    play sound_loop white_noise volume 1
    scene bg int_catacombs_living_red with byso
    "Добежав доверху, он достал вторую гранату."
    play sound3 cheka volume 1
    "Выдернув чеку, он бросил её под лестницу."
    play sound3 sfx_muffled_explosion volume 1
    stop music fadeout 1
    "Взрыв." with vpunch
    "Лестница была уничтожена, а вход к ней завален."
    play music Waijdan fadein 3
    play sound3 sfx_bed_squeak2 volume 1
    "Константин выдохнул и присел на кровать перевести дух."
    "Помещение было освещено красным аварийным освещением, а пол был в крови."
    "Радио издавало белый шум, который изменялся в тональности."
    "Константин хотел было достать сигареты, но прислушался к постороннему шуму."
    play sound3 monster_sfx volume 0.31
    "Из пещер то и дело доносились голодные рыки гончих, которые пытались разгрести породу."
    th "Вот сука, даже отдохнуть не дадут!"
    "Встав с кровати, Константин побежал дальше."
    stop sound_loop fadeout 1
    scene bg int_catacombs_door with byso
    play sound3 sfx_metal_door_heavy_close volume 1
    "Закрыв дверь бункера, он провернул на ней гермозатвор."
    th "Так точно не пройдут."
    scene bg int_catacombs_entrance with byso
    "Сняв винтовку со спины, Константин направился на выход."
    "Атмосфера в катакомбах отнюдь не казалась приветливой.{w} Давящая, холодная и неприятная."
    "Словно где-то далеко отсюда начался локальный ядерный конфликт и территория оказалась начисто отрезанной от остального мира."
    "Хотелось как можно быстрее выбраться."
    "Путь назад был отрезан, но это было скорее плюсом, чем минусом."
    "Бег изнурял, но ноги сами несли Константина, зная, что это единственно возможный путь к спасению из ситуации."
    play ambience ambience_ext_road_night volume 1 fadein 1
    scene bg int_old_building_night with byso
    play sound3 sfx_open_metal_hatch volume 1
    "Добежав до лестницы, Константин быстро по ней вскарабкался и закрыл люк."
    "Обессилено он сел рядом с люком и достал сигарету."
    th "Ебать..."
    th "Почему меня выкинуло именно в катакомбы? Мест других нет?"
    th "И как там Рена?..."
    play sound3 light_inh volume 1
    "Размяв фильтр, Константин закурил.{w} Это простое действие вернуло его к мрачным мыслям."
    th "Она же смогла победить?"
    th "Она сильная.{w=1} Явно сильнее меня."
    th "Но и соперник у неё не пальцем деланный. Тоже тульпа."
    th "Откуда у них настолько сверхъестественные силы?"
    play sound3 sfx_lock_click volume 1
    "Держа сигарету зубами Константин вытащил пистолет из рюкзака и снял пустой магазин."
    th "Хотя...{w=1} Видимо при попадании в инреальность тела людей изменяются в лучшую сторону."
    th "Такой кросс как сейчас я бы не пробежал никогда, а теперь спокойно."
    "Достав пачку патронов, он начал заполнять магазины."
    th "А Рена... {w=1}Она просто невероятно сильна..."
    th "Когда взорвался автобус, она при мне расплющила череп Лизы."
    th "Ладно, это то мы видели...{w=1} Но как она тогда меня дотащила до медпункта?"
    th "Мало того, сама была без единого ранения.{w} Словно она терминатор."
    th "Интересно, является ли это частью генетического кода?"
    th "А что если после выхода из инреальности Рена потеряет своё материальное тело?"
    "Константин замер.{w=1} Его поразила пришедшая в голову мысль."
    th "Да, а безопасно ли нам покидать инреальность?"
    th "Вдруг она снова станет нематериальной?"
    th "Надо это обсудить. Если у нас ещё будет время."
    play sound3 reload volume 1
    "Зарядив обоймы, он вставил их по местам."
    th "Хотя очень вряд-ли.{w} Скоро мы будем сражаться с сопротивлением и Гендой."
    th "Там у нас точно не будет времени поговорить."
    play sound3 weapon volume 1
    "Встав с места, он дёрнул затвор винтовки, дослав патрон."
    th "Настало время выбираться отсюда."
    "Встав с места, Константин направился на площадь."
    scene bg ext_old_building_night_moonlight
    show image me_st
    with byso
    play music Vl66 fadein 3
    "В старый корпус бежал Семён."
    me "Помогите!!!"
    "Константин взял его на мушку."
    play sound3 vintovka volume 1
    play sound head_crush volume 1
    hide image me_st with fl_scare
    "Выстрел."
    "Семёну пробило грудь и он развалился на земле."
    show image monster with bso
    play sound3 flesh_feast volume 1
    "За ним выбежала гончая и начала жадно разрывать его труп."
    "Эта гончая слегка отличалась от остальных.{w=1} У неё был порез на черепе."
    window hide
    menu:
        "Застрелить гончую.":
            $ renpy.block_rollback()
            th "Прости, но меня не надо кусать за жопу."
            play sound head_crush volume 1
            play sound3 vintovka volume 1
            hide image monster with fl_scare
            "Константин выстрелил гончей в черепушку."
            play sound2 sfx_bush_body_fall volume 1
            "Пуля прошла на вылет, а монстр простонал и рухнул на землю."
            kt "Получила, паскуда."
            "Константин направился дальше к площади."
        "Пройти тихо.":
            $ renpy.block_rollback()
            $ event1 += 1;
            th "Ну его.{w=1} Пройду тихо."
            th "Да и с первого раза могу не убить."
            hide image monster with byso
            "Константин аккуратно прошмыгнул мимо, пока гончая лакомилась добычей."
    scene bg ext_polyana_night with byso
    stop sound_loop fadeout 1
    "Выйдя на поляну, он перешёл на бег."
    th "Нужен портал...{w=1} Правда какой?"
    th "Их может быть несколько. Это совершенно омрачает картину."
    th "Если я выберу не тот, то потеряюсь в инреальности."
    th "А это может повлечь некоторые не самые приятные последствия."
    scene bg ext_square_night_blood with byso
    scene bg ext_square_night_blood:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 1 crop (497, 223, 980, 630)
    show image sopr_sold with byso
    "На площади был хаос.{w=1} Кругом лежали трупы, среди которых был парень в противогазе."
    th "Ничего нового.{w=1} Снова здарова, как говорится."
    "Константин из кустов прицелился в солдата и задержал дыхание."
    th "Сейчас вылетит птичка."
    play sound3 vintovka volume 1
    play sound head_crush volume 1
    hide image sopr_sold with fl_fire
    "Выстрел."
    "Патрон пробил каску и окрасил стёкла противогаза кровью. Парень упал замертво."
    "Константин начал осматриваться на предмет новых врагов."
    th "Вроде чисто..."
    scene bg ext_square_night_blood:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 1 crop (0, 0, 1920, 1080)
    play sound3 sfx_punch_medium volume 1
    "Вдруг, он почувствовал, что кто-то приложил ему нож к горлу."
    sold "Не двигайся или я тебе глотку вскрою."
    "Константин тяжело вздохнул и положил винтовку."
    kt "Хуле тебе от меня надо?"
    sold "Ты убил нашего. Последние слова?"
if event1 == 1:
    $ event1 -= 1;
    jump gfsduionvifudsnvifsnvhfbshvgruqjfiodsjlkakpgjasdiojgv
else:
    kt "Сдохни!"
    play sound3 knife2 volume 1
    stop music fadeout 1
    stop ambience fadeout 0.5
    scene bg black with fl_scare
    "Константин попытался ударить держащего, но ему вскрыли глотку."
    window hide dissolve
    scene bg black with byso
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    $ unlock_ach_root_inreal(2)
    play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
    scene bg ending_dead_cg:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    show ending_dead:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    with Dissolve(15)
    scene bg black with byso
    pause 1
    stop sound
    jump after_ending_screen
label gfsduionvifudsnvifsnvhfbshvgruqjfiodsjlkakpgjasdiojgv:
    kt "Пошёл нахуй!"
    play sound head_crush volume 1
    play sound_loop flesh_feast volume 1
    "Вдруг, Константин услышал позади хруст."
    play sound3 sfx_drop_pipe volume 0.51
    "Рука с ножом обмякла и выронила оружие."
    "Он взял свою винтовку и отбежал на несколько метров."
    show image monster with byso
    "Это была та самая гончая со шрамом на голове."
    "Она откусила голову солдата и на этот раз лакомилась именно его трупом."
    th "А у тебя сегодня аппетит хороший..."
    stop sound_loop fadeout 1
    hide image monster with byso
    "Улыбнулся Константин и обернулся."
    play sound3 power volume 1
    scene bg ext_square_night_blood_red with byso
    "Открылись порталы."
    "Их было два: правый и центральный."
    window hide
    menu:
        "Правый.":
            $ renpy.block_rollback()
            $ event1 += 1;
            "Константин подошёл к порталу."
        "Центральный.":
            $ renpy.block_rollback()
            "Константин подошёл к порталу."
    "Заглянув в него, он заметил, что в нём словно показывают отрывки старого кино."
    "Размыто, нечётко, ещё и без звука."
    th "Ну, была не была..."
    stop ambience fadeout 1
    play sound3 portal volume 1
    stop music fadeout 1
    scene bg black with byso
    "Войдя внутрь, Константин утонул в пустоте."
    pause 2
    play music ElfenLied fadein 3
    scene bg kt_room
    show shum_red
    with byso
    "Сердцебиение участилось, что означало начало всасывание препарата в кровь."
    kt "Путь отчаянья.{w} Путь постижения сущего."
    re_na "Что дальше?"
    re_na "Вперед или назад?{w} Или то и другое сразу?"
    "Всё тело стало ватным.{w=1} Пошевелить чем-то было практически невозможно."
    kt "Какое-то ужасное растяжение в груди.{w=1} Вдохнуть не могу."
    re_na "Не можешь.{w} Раз не можешь, значит, вперед."
    re_na "Продолжай.{w=1} Только медленно и равномерно."
    re_na "Я помогу тебе."
    kt "Как ты мне поможешь?"
    kt "Ты мертва.{w=1} Ты иллюзия.{w=1} Сон."
    "В голове плыли картинки. Зрачки расширились, а сознание в бешеном темпе занырнуло в самый темный уголок черепной коробки."
    kt "Все, что ты говоришь, неправда.{w=1} Так не бывает."
    re_na "Я не мертва.{w} Я ещё не родилась."
    re_na "Но скоро буду.{w=1} И когда я буду, мир не будет прежним."
    re_na "Слышишь?{w=1} Он изменится."
    re_na "Мир, в котором ты живешь.{w=1} Жизнь похожая на сказку."
    re_na "Рождение из небытия.{w=1} Смерть в небытие."
    "Собрав силы, Константин встал со стула и упал на кровать."
    "Он уже не мог контролировать свои движения и даже мысли пошли своим ходом."
    kt "Мир не меняется."
    kt "Прошлое было когда-то будущим.{w=1} Будущее не наступит никогда."
    kt "Вокруг тот же мир, который ты уже видела.{w=1} Что ещё ты хочешь увидеть?"
    re_na "Я хочу увидеть тебя счастливым.{w=1} Для меня уже счастье, если ты будешь рядом."
    re_na "Чтобы ты перестал прятаться в свою черноту."
    re_na "Мне с тобой хорошо. {w}Мой новый мир будет счастлив вместе с нами."
    "Переведя взгляд на потолок, Константин закатил глаза."
    kt "Мое счастье будет твоим счастьем.{w=1} Где мы будем вдвоем?"
    re_na "Мы вместе.{w=1} Сейчас и в одиночестве."
    re_na "Не бойся.{w=1} Мы будем счастливы."
    kt "Но как?{w} Я заядлый наркоман, эскапист."
    kt "Ничего никогда не изменится."
    re_na "Изменится.{w=1} Вернее, будет счастливее."
    re_na "Случайно и навсегда.{w=1} Потому что вдвоем.{w} Ничто, нигде и никогда, мой несовершенный ты."
    re_na "Будет любовь в новой форме.{w=1} Ужас не повторится."
    re_na "Любовь до кончиков пальцев, до потери реальности.{w} Держись."
    "Перевернувшись на бок, он почувствовал прилив эндорфина, который был готов способен Константина в амёбу."
    kt "А если нет, то надо уничтожить этот мир...{w=1} Тебе."
    kt "Ведь я на это не способен."
    stop music fadeout 3
    scene bg black with byso
    pause 2
if event1 == 1:
    $ event1 -= 1;
    jump gfsduionviierkbvfidsnvodaskweojfuixzzjkfiodasiof
else:
    play ambience ambience_forest_night volume 1 fadein 1
    play music ToxiSector fadein 3
    scene bg ext_path2_night
    show unblink
    play sound3 krik2 volume 0.51
    "Константин очнулся в лесу.{w=1} Вдали слышались крики."
    th "Что?{w=1} Уже началась революция?"
    "Встав с места, он взял оружие и направился на звуки."
    th "Надо найти Рену.{w=1} Я надеюсь, она уже тут."
    scene bg ext_polyana_night with byso
    "В лесу Константин заметил знакомую фигуру."
    show image re_holod2_casual with byso
    "Это была Рена.{w=1} Она стояла на поляне и смотрела на звёзды."
    kt "Рена!{w=1} Вот ты где."
    play sound3 sfx_pat_shoulder_hard volume 1
    hide image re_holod2_casual
    show image re_holod2_casual at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Константин подошёл к ней и обнял.{w} Рена никак не отреагировала."
    kt "Я знал что ты её убьёшь.{w} Молодец!"
    kt "Поздравляю."
    hide image re_holod2_casual
    show image re_holod2_casual
    with byso
    "Его начало напрягать полное отсутствие реакции от своей спутницы.{w} Он отпустил её и отшагнул."
    kt "Что с тобой?"
    ren "Это тело зовут...{w=1} Регина?"
    "Константина начало напрягать происходящее."
    kt "Всмысле?"
    play music "<from 11>inrealnost/Music/Music/Maskmane1.mp3"
    play sound3 slash volume 1
    show image blood3 with vpunch
    "Его грудь пронзила огромная вилоподобная конечность."
    mon_g "Спасибо за уточнение."
    play sound head_crush volume 1
    stop music fadeout 1
    stop ambience fadeout 0.5
    scene bg black with vpunch
    "Второй удар пришёлся на голову."
    window hide dissolve
    scene bg black with byso
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    $ unlock_ach_root_inreal(2)
    play sound "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
    scene bg ending_dead_cg:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    show ending_dead:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    with Dissolve(15)
    scene bg black with byso
    pause 1
    stop sound
    jump after_ending_screen
label gfsduionviierkbvfidsnvodaskweojfuixzzjkfiodasiof:
    play ambience ambience_int_cabin_day volume 1 fadein 1
    scene bg int_house_of_kt_day
    show unblink
    play music interlude fadein 3
    "Константин проснулся в пустом домике."
    "Он был похож на тот, в котором он жил с Реной."
    th "Домик тот-же, а симуляция другая...{w=1} Необычно."
    "За окном пели птицы, светило солнце и медленно проплывали по небу разноцветные облака."
    th "Ещё день.{w} Обнадёживает."
    play sound3 sfx_put_sugar_cart volume 1
    "Константин снял рюкзак и прилёг на кровать."
    th "Как можно заметить, когда в симуляции происходит что-то ужасное - становится темно.{w=1} Скорее всего, тут ещё всё в порядке..."
    "Потянувшись, он достал из кармана сигарету."
    "Посмотрев на фильтр, он убрал её обратно."
    th "Слишком часто я курю.{w=1} Надо бы перерыв чтоль сделать..."
    th "Да и Рена наверняка захочет закурить.{w} Подожду её."
    th "Интересно, как она сейчас.{w=1} Цела?"
    th "Я вроде кое-как выжил. И то было чуть ли не случайностью."
    th "Ну, останься бы я с ней, меня бы точно продырявили."
    th "Да и я в этом плане обуза для Рены.{w=1} Она может меня спасти и любит, но не может защитить от всего и сразу."
    play sound3 sfx_bed_squeak2 volume 1
    play sound sfx_stomach_growl volume 1
    "Константин перевалился и принял вертикальное положение. Желудок недовольно заурчал."
    th "И не ели мы давно.{w=1} Надо бы перекусить."
    th "Да, точно. {w=1}Пойду к столовой.{w=1} Может прихвачу чего-то съедобного."
    play sound3 sfx_bed_squeak1 volume 1
    play sound3 sfx_put_sugar_cart volume 0.41
    "Встав с кровати и накинув рюкзак, он пошёл к двери."
    th "Есть же короткий перерыв.{w} Я надеюсь."
    play sound3 sfx_knock_door_closed_hard1 volume 1
    "Попытавшись открыть дверь, он понял, что она заперта."
    th "Вот сука."
    th "Тогда применю излюбленный приём."
    play sound3 door_break volume 1
    th "На нахуй!" with vpunch
    "Замок на двери не выдержал и открылся."
    th "Другое дело."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_houses_day with byso
    "На улице он попытался сориентироваться в своём местоположении."
    th "И где я?..."
    th "А, вон Генду видно.{w=1} Мне туда."
    th "У столовой вроде как есть склад.{w=1} Может там есть что съедобное."
    "Не долго думая, он поплёл в нужную сторону."
    th "Сейчас бы и собаку сожрал.{w=1} Голод просто дикий."
    th "Никогда бы не подумал, что настолько долго могу протянуть без еды."
    scene bg ext_square_day with byso
    th "Просто видимо за всё это время у меня не было никакого момента, который хоть немного бы вызвал аппетит."
    th "Оно и ясно. {w=1}Пытки, идолопоклонники, гончие, сопротивление..."
    th "Речи о еде и быть не может."
    scene bg ext_dining_hall_near_day with fade
    "Дойдя до столовой, он обнаружил нужную дверь, возле которой он в первые дни сидел и курил."
    th "Вот и оно."
    play sound3 sfx_knock_door_closed_hard2 volume 1
    "Подёргав ручку, он понял что она заперта и совсем не удивился."
    "Константин отошёл на пару метров."
    play sound3 door_break volume 1
    th "На нахуй!" with vpunch
    "Дверь хоть и не вылетела, но открылась."
    th "То-то."
    play ambience ambience_int_cabin_day volume 1 fadein 1
    scene bg sklad with byso
    "Внутри его ожидало множество коробок."
    th "Так-так, что тут у нас."
    "Перебирая содержимое коробок, Константин продолжал думать о свём."
    th "Карандаши, папки, прочая канцелярия. Хлам."
    th "Хм, кстати, история повторяется."
    th "Я встречу Рену в автобусе.{w} Почти как 4 дня назад."
    th "Я же её встречу?"
    "Константин взял другую коробку начал изучать её содержимое."
    th "Без неё уже как-то не так...{w=1} Красиво что-ли?"
    th "А то у меня в голове как будто что то сдвинулось - за это время я привык к её заботе."
    "Отставив коробку, он заглянул в ящик."
    th "И ещё к красоте её лица.{w} Рыжие короткие волосы, голубые глаза и белый беретик, плотно прилегающий к голове."
    th "Это действительно красиво.{w=1} Как я уже думал, она - первый человек в моей жизни, кто во время моей болезни спас мне жизнь."
    "Выдвинув другую коробку, он начал её вскрывать."
    th "Вылечил меня от неизлечимого одиночества, позаботился обо мне.{w=1} Кроме того, я могу ей доверять."
    th "Намного больше, чем себе.{w} Она самый близкий мне человек."
    th "Она...{w=1} Она...{w=1} Просто мой настоящий идеал."
    "Внутри оказались вилки.{w} Он взял две штуки."
    th "Нет во всём человеческом роде такого человека, который полюбил бы меня больше."
    th "Я должен отплатить ей тем же."
    "Тяжело взмахнув, он выдвинул другой ящик."
    th "А вёл я себя всегда пассивно...{w=1} Я пойду к ней на встречу."
    th "Надо же начать меняться.{w} Прожить свою жизнь, так как она меня любит."
    th "Рена, ты идеальна..."
    stop music fadeout 3
    play sound sfx_open_door_2
    "Мысли Константина прервала дверь.{w=1} В неё кто-то вошёл."
    mt "Та-а-ак!{w=1} И что мы тут делаем?!"
    "Константин закатил глаза и неохотно обернулся."
    play music paralysis fadein 3
    show mt angry pioneer with byso
    "На склад вошла Сахарова. {w}Ей, судя по всему не нравилось то, чем Константин занят."
    mt "Ты вообще кто?"
    "Не долго думая, Константин взял винтовку и прицелился в зелёные глаза Сахаровой."
    "Та не повелась на угрозу и пуще разозлилась."
    show mt rage pioneer with byso
    mt "Какого чёрта ты воруешь лагерную собственность?!"
    kt "Где еда?!"
    mt "Была на обеде!{w=1} Пошёл вон отсюда!!!"
    play sound3 weapon volume 1
    show mt shocked pioneer with byso
    "Константин усмехнулся и дёрнул затвор.{w} На лице вожатой произошло осознание, что винтовка настоящая."
    kt "Последний раз спрашиваю, Сахарова, где еда?"
    mt "Вот в-в-в том ящике..."
    "Он глянул на указанный ящик и вернулся к Сахаровой."
    mt "Я п-п-пойду, х-хорошо?..."
    "Она была напугана.{w} Константин ещё шире улыбнулся и взял винтовку покрепче."
    kt "М-да, Оля...{w=1} Никак ты не научишься не лезть в чужое дело."
    play sound head_crush
    play sound3 vintovka volume 1
    hide mt with fl_fire
    "Выстрел."
    "Тело Сахаровой повалилось на холодный пол, а её пробитая голова запрокинулась назад."
    stop music fadeout 3
    "Константин обернулся к ящику, на который указала Сахарова и выдвинул его."
    "Внутри него стояло множество банок, судя по форме, с консервами."
    "На них не было никакой маркировки.{w=1} Константин взял четыре штуки."
    th "Вот и еда.{w=1} Давно не ел.{w} Рена наверное тоже."
    th "Возьму побольше."
    "Упаковав банки, Константин посмотрел на труп Ольги."
    th "Пусть это останется как прощание с прошлым."
    play ambience ambience_ext_road_day volume 1 fadein 1
    scene bg ext_dining_hall_near_day with byso
    play music summerdays fadein 3
    "Аккуратно обойдя кровавую лужу, Константин покинул склад и направился к автобусной остановке."
    th "Даже представить боюсь, что начнётся в этой симуляции через несколько часов..."
    th "Умрёт более 700 человек...{w=1} Да это же просто будет мясорубка!"
    scene bg ext_dining_hall_away_day with byso
    th "Хотя... {w=1}Что в инреальности не мясорубка?..."
    th "Главное нам с Реной ноги унести..."
    scene bg ext_square_day with byso
    "На площади стояла Славя и подметала."
    "Она с улыбкой на лице, напевая под нос едва-различимую мелодию, водила шваброй взад-вперед, отчего маленький пылевой вихрь носился в воздухе."
    th "Всё мирно...{w=1} Как в первый день."
    th "Странно...{w=1} Никто не слышал выстрела?"
    th "Вроде грохнуло достаточно сильно, чтоб все услышали..."
    th "Хотя, в такой атмосфере, видимо, никто и внимания на это никакого не обратил."
    th "Счастливое незнание."
    scene bg ext_clubs_day with byso
    th "Потом мы видим, как автобус приедет и начинается война, переходящая в блицкриг."
    th "Весь технический и артистический труд остается в прошлом, и смешивается с кровью."
    th "Ценности начинают разрушаться.{w} Смерть предстаёт в новом свете, а законные права и свободы превращаются в фарс."
    th "Всё исчезает в тот самый момент, когда наступает финал."
    th "И никто не знает, чем закончится эта схватка...{w=1} Даже сам Генда не может этого знать."
    scene bg ext_camp_entrance_day with byso
    "Остановившись у ворот, Константин посмотрел на памятник пионеру."
    th "Но ясно одно.{w=1} Будет много крови."
    scene bg ext_no_bus with byso
    "Присев на поребрик, Константин потянулся за тушёнкой."
    play sound3 open_can volume 1
    "Дёрнув за кольцо, он достал вилку и всмотрелся в содержимое банки."
    "Вещество походило на вываренную гречку с мясными волокнами."
    "Константин вытащил маленький кусочек, отщипнул и отправил его в рот."
    th "Не три звёзды Мишлен, но сойдёт."
    th "После такого изнурительного приключения грех отказываться."
    "Достав другую банку, он её встряхнул."
    "Внутри плескалась какая-то жидкость с твёрдыми кусочками."
    th "А этим можно и запить..."
    "Вскрыв вторую банку, он обнаружил маринованный персик в собственном соку."
    th "Давно я не ел на природе.{w=1} Кажется что так вкуснее."
    th "Ну или я просто слишком голоден."
    "Уплетая гречку и запивая её сладким компотом, Константин засмотрелся вдаль дороги."
    th "Рена-Рена...{w=1} Я верю, что ты вернёшься..."
    scene bg ext_beach2_day:
        crop (497, 223, 980, 630)
        size (1920, 1080)
    with byso
    "Переведя взгляд в небо, он засмотрелся на облака."
    "Они казались нереально красивыми, с какой-то нереальной, непонятно откуда взявшейся радужностью."
    "Гладкая белая поверхность облаков казалась мягкой и нежной на вид."
    "Глядя на них, легче было забыть обо всем.{w} О всех проблемах, о грядущей бойне, обо всех страхах, выпавших на его долю..."
    "Забыть, что все это происходит с ним, и происходит на самом деле..."
    "Одновременно бесконечно странно и незабываемо красиво."
    scene bg ext_no_bus with byso
    "Выкинув банку в сторону, Константин принялся вылавливать сладкие кусочки персика из банки."
    th "Нет, ну не могу.{w=1} Хочется закурить."
    "Выпив из банки, он отставил её на поребрик и достал пачку сигарет."
    "Внутри оставалось чуть больше половины пачки."
    play sound3 light_inh volume 1
    "Раздавив кнопку, Константин вставил сигарету в зубы и закурил."
    "Едкий дым слегка расслабил, и появилось приятное чувство, что не все так плохо."
    "Константин услышал звук приближающегося автобуса."
    th "Да ладно?{w} Это и тут работает?"
    play sound3 sfx_put_sugar_cart volume 1
    "Он накинул рюкзак и встал с поребрика."
    play sound sfx_bus_stop volume 1
    scene bg ext_bus with byso
    "Автобус затормозил до полной остановки и со скрипом заглох.{w=1} Константин выбросил почти полную сигарету."
    play sound3 sfx_ikarus_open_doors volume 1
    "Дверь открылась."
    kt "Я уж заждался."
    play sound pum
    stop music
    pp "Кого?"
    play music rutine fadein 3
    show image poter_n with byso
    show mi shocked pioneer at right with byso
    show un surprise pioneer at left with byso
    "Из автобуса вышел пионер, а за ним Мику и Лена.{w} На спине Лены красовался рюкзак Константина, а Мику была вооружена пистолетом."
    pp "Необычно видеть тебя без карманной маньячки."
    show un sad pioneer with byso
    un "Ты от неё избавился?"
    show mi sad pioneer with byso
    mi "Она больше не опасна?"
    show blink
    "В голове Константина со скоростью света завертелись варианты ответов.{w=1} Время вокруг словно остановилось."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    th "Если я им скажу, что Рена со мной, то последствия могут быть непредсказуемы."
    th "Они её боятся, потому могут меня убить.{w=1} Пионер явно не настроен видеть Рену в своих рядах, да и сама она хочет его убить."
    th "Единственной, кому я могу доверять, является Рена, не стоит это забывать."
    th "Надо что-то выдумать...{w=1} Трагичную маску."
    th "Разорванную душу.{w} Добропорядочное лицо, бегущее от убийства."
    th "Или печальное лицо музыканта, играющего на самом себе.{w=1} Трагедию, ставящую всё с ног на голову."
    th "Но ни капли правды.{w} Полное отрицание того, что мы видим, а потом её имитация."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    scene bg ext_bus
    show image poter_n
    show mi sad pioneer at right
    show un sad pioneer at left
    show unblink
    "Константин вернулся к разговору.{w=1} Прошла буквально секунда."
    kt "Пока мы пробирались сквозь инреальность, мы нарвались на идолопоклонников..."
    "Он киношно нахмурился, изображая печаль."
    "Вышло весьма убедительно и искренне, зритель поверил."
    kt "Она не смогла пробраться и ценой своей жизни защитила меня.{w=1} В один момент она спасла мне жизнь, и я благодарю ее за это."
    play sound3 sfx_punch_medium volume 1
    show mi shocked pioneer with byso
    "Лена похлопала Константина по плечу.{w=1} Судя по лицам окружающих, они проглотили искусную ложь Константина словно рыболовный крючок."
    pp "Похоже на неё...{w=1} Сочувствую, друг.{w} Пойдём с нами."
    th "Ага, так я и поверил..."
    show mi sad pioneer with byso
    mi "У нас свои планы, вместе мы выберемся."
    un "Вчетвером у нас будет больше шансов."
    "Пионер обратил внимание на недоеденные консервы."
    pp "Приятного аппетита.{w=1} Мы пойдём на пирс, будем вести оборону оттуда."
    mi "Как доешь - догоняй.{w} Нам бы хотелось с тобой поговорить."
    kt "Хорошо."
    scene bg ext_bus with byso
    "Константин обратно сел на поребрик и продолжил трапезу."
    stop music fadeout 3
    "Отряд ушёл, а Константин достал из рюкзака нож, которым Рена пытала девушку в автобусе."
    th "Да, лгать я ещё не разучился.{w=1} Это хорошо."
    "Нож был частично покрыт спёкшейся кровью."
    th "Чтобы меня долго не искали, сделаю так..."
    play music Gallow fadein 3
    "Закинув в себя оставшееся часть еды, Константин взял нож и начал царапать на банке."
    "Выцарапав слова <<Пирс 3 К.>>, Константин поставил банку, положив в неё сломанный телепортатор и окровавленный нож."
    scene bg ext_camp_entrance_day with byso
    "Встав с места, он с улыбкой потянулся и размял шею."
    th "Ну что, <<друзья>>, погнали."
    scene bg ext_clubs_day with byso
    play sound3 sfx_lock_click volume 1
    "Выйдя за ними, Константин снял магазин с винтовки."
    th "Интересно, а с каких пор пионер решил создать фонд спасения?"
    th "Нас с Реной он обворовал, затем кинул, так а теперь строит из себя спасателя."
    play sound3 reload volume 1
    "Вставив недостающие патроны, Константин вернул магазин в винтовку."
    th "Разберёмся мы с этим недопониманием."
    scene bg ext_square_day
    show image poter_n
    show mi upset pioneer at right
    show un normal pioneer at left
    with byso
    "Догнав отряд, Константин услышал их диалог."
    mi "Но как мы сможем обороняться на пирсе?"
    pp "Смотри, кругом вода.{w=1} Гончие не умеют плавать.{w} Логику уловила?"
    show mi sad pioneer at right with byso
    mi "А, я поняла..."
    scene bg ext_path_day
    show image poter_n
    show mi sad pioneer at right
    show un normal pioneer at left
    with byso
    "Константин пошёл с ними в шаг."
    show un sad pioneer with byso
    un "А ты?{w=1} Как себя чувствуешь?"
    kt "Нормально. {w=1}Более-менее смирился."
    pp "Да что там мириться.{w=1} Просто обычное порождение инреальности и твоего сознания."
    pp "Миллион таких как она найдёшь."
    th "Будь у меня тот нож, я бы тебя прямо тут пырнул!"
    un "Повторим план?"
    mi "Да, давайте."
    "Пионер тяжело выдохнул и кивнул."
    show mi serious pioneer at right
    show un normal pioneer at left
    with byso
    pp "Хорошо.{w=1} Повторим."
    pp "Итак, нас теперь четверо, а Константин, судя по всему, ещё и не дурно снаряжён."
    pp "Мы базируемся на пирсе и ожидаем, пока всё урегулирует сопротивление."
    hide image poter_n
    show image poter_s
    with byso
    pp "После покраснения неба мы выдвигаемся на площадь и организуем контрнаступление, доходим до административной симуляции и вставляем нашу флешку."
    "Пионер засветил красную флешку с выгравированным знаком бесконечности."
    "Константин решил сыграть в дурачка и поднял бровь."
    kt "Административная симуляция?{w=1} Это что?"
    hide image poter_s
    show image poter_n
    show mi sad pioneer at right
    show un surprise pioneer at left
    with byso
    "Пионер отвлёкся от пересказа плана и, убрав флешку, вопросительно посмотрел на Константина."
    pp "Тебе никто не говорил о ней?"
    kt "Нет."
    pp "Тогда какого чёрта ты делаешь прямо рядом с ней?"
    kt "Так получилось, я не знаю."
    "Пионера, судя по всему, начали смущать ответы Константина."
    pp "Скажи на милость, а кого ты ждал из автобуса?"
    th "Вот падаль!"
    kt "Пересёкся с одной девушкой в симуляции.{w=1} Она мне сказала, что увидимся в 20-32g."
    show mi happy pioneer at right with byso
    mi "Да?!{w=1} У нас будет ещё пополнение?"
    show mi sad pioneer at right with byso
    pp "Придержи коней.{w} Опиши её."
    "Константину не пришло ничего кроме образа Минервы, который надо было сильно исказить."
    kt "Добрая девушка с седыми волосами и повязкой на глазу."
    kt "Другой глаз голубой.{w=1} Одета была в чёрное пальто."
    kt "Может показаться странной, но вполне неплохой человек.{w} Зовут Марина."
    "От такой лжи у Константина чуть не свело челюсть."
    pp "Ладно, поверим...{w=1} Чувствую, не врёшь."
    show un smile pioneer at left with byso
    un "Да, было бы неплохо получить пополнение в наши ряды."
    show mi laugh pioneer at right with byso
    mi "Мы команда!"
    th "Если только на самоуничтожение."
    stop music fadeout 3
    play ambience ambience_boat_station_day volume 1 fadein 1
    scene bg ext_boathouse_day
    show image poter_s
    show mi happy pioneer at right
    show un smile pioneer at left
    with byso
    "Дойдя до пляжа, они переглянулись."
    pp "Можем пока что посидеть. Нам есть о чём поговорить."
    th "О способе вашей смерти?"
    show mi smile pioneer at right with byso
    mi "Да, я бы тоже хотела пообщаться, я так и не представилась перед Костей."
    show un grin pioneer at left with byso
    un "Никто не представился."
    scene bg ext_beach2_day with byso
    "Сев с ними на краю пирса, Константин посмотрел в водную пущу."
    play music Voyage fadein 3
    hide image poter_s
    show image poter_n
    with byso
    pp "Да, раз уж мы работаем вместе, то у нас не должно быть никаких недоговорённых деталей."
    show mi sad pioneer at right with byso
    mi "Я начну..."
    mi "Когда открылись порталы, я испугалась и побежала в первый попавшийся."
    show un smile pioneer at left with byso
    un "И мы решили взять её с собой."
    th "Есть у меня чуйка, что они бы не помиловали меня и Рену."
    show mi upset pioneer at right with byso
    mi "Меня на самом деле зовут Маша.{w=1} Ты меня помнишь?"
    "Константин удивился и перевёл взгляд на девочку."
    kt "Какая Маша?"
    show mi sad pioneer at right with byso
    ma "Маша Мураками.{w=1} Я была твоей соседкой в деревне."
    ma "Девочка из Японии..."
    play sound in_vosp
    scene bg ext_bathhouse_night
    show shum_white
    with flash
    ks "Деда, кто там?"
    de "Это к тебе."
    ks "Ко мне?{w=1} Кто?"
    de "Выходи, увидишь."
    "Костя вышел на веранду и увидел низкую девочку с чёрными волосами и желтоватой кожей."
    de "Это Маша.{w} Внучка наших соседей, она приехала из Японии."
    ma "{image=inrealnost/Pic/Spec/japan.png}{font=inrealnost/font/Naganoshi.ttf}こんにちは。"
    ma "Ой...{w} То есть привет."
    "Девочка сильно раскраснелась и засмотрелась в пол.{w} Костя протянул руку."
    ks "Привет, я Костя, рад знакомству."
    hide shum_white
    scene bg ext_beach2_day
    show mi sad pioneer at right
    show image poter_n
    show un sad pioneer at left
    with flash
    un "Меня зовут Лена.{w} Климова Лена."
    un "Мы учились в одной школе."
    play sound in_vosp
    scene bg street_sunset
    show shum_red
    with flash
    mak "А вы выглядите как неплохая пара."
    "На такой комментарий Лена раскраснелась, а Костя ухмыльнулся."
    ks "Не начинай.{w=1} Ты её в первый раз видишь."
    un "Вот-вот..."
    mak "Но я же вижу, как ты смотришь на него.{w=1} Любоффь-моркоффь."
    "Намеренно прошепелявил Макс, чем ещё сильнее вогнал Лену в краску."
    ks "Ладно, Макс, что у тебя по деньгам?"
    scene bg ext_beach2_day
    show mi smile pioneer at right
    show image poter_s
    show un smile pioneer at left
    with flash
    pp "И мы с тобой не незнакомцы."
    pp "Меня зовут Макс. Лучший друг детства."
    play sound in_vosp
    scene bg kt_room
    show shum_red
    with flash
    mak "Ты думаешь у меня дохуя энергии, думаешь у меня дохуя времени?{w=1} Нет." with fl_fast
    mak "Ты настолько эгоистичен, ты настолько апатичен.{w=1} Тебе вообще плевать на меня, на всех людей." with fl_fast
    mak "Я даже не хочу говорить тебе о своих проблемах, чтоб не слушать критику на этот счёт." with fl_fast
    scene bg ext_beach2_day
    show mi smile pioneer at right
    show image poter_s
    show un smile pioneer at left
    with flash
    "Константин несколько секунд просидел в ступоре."
    "Макс похлопал его по спине."
    mak "Понимаю, столько всего и сразу..."
    mak "Ничего, но главное мы снова вместе и вместе мы сможем победить Генду."
    "Константин легко улыбнулся."
    "В его улыбке читалась радость встречи и взаимопонимания."
    stop music fadeout 1
    "{sc=2}{color=#E2C778}{size=28}{i}Но эта улыбка совершенно не отражала того, что происходило у него в голове.{/i}{/size}{/color}{/sc}"
    play music HeartBeat fadein 3
    eth "{sc=2}{size=28}{color=#FF1010}Твари...{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}И вы прикрываетесь личиной добра, когда вы все меня бросили?!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Оставили меня гнить?!{w} Разлагаться в одиночестве?!{/color}{/size}{/sc}"
    show mi laugh pioneer at right with byso
    ma "Так давайте обнимемся!"
    "Константин действовал на автопилоте, потому не отказался и продолжал поддельно улыбаться."
    eth "{sc=2}{size=28}{color=#FF1010}Да вы просто ебанутые раз думаете, что я это забыл!!!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Ненавижу...{w=1} Ненавижу!!!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Гадкие лживые твари!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Топора на вас не найдётся, да поострее!{/color}{/size}{/sc}"
    "Обняв друг друга, они переглянулись и улыбнулись друг другу."
    eth "{sc=2}{size=28}{color=#FF1010}Купаться буду в вашей крови!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Я вам всем напомню, как выглядит одиночество!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Рена приедет и мы такое вам устроим!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Вас всех я буду держать за глотку, потроша как скумбрию!{/color}{/size}{/sc}"
    show un cry_smile pioneer at left with byso
    un "Я так рада, что мы снова вместе!"
    eth "{sc=2}{size=28}{color=#FF1010}Чучела из вас буду вешать, чтоб не повадно было!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Лжецы! {w}Лживые подонки!{/color}{/size}{/sc}"
    mak "Мы же не держим друг на друга зла, правильно?"
    show mi happy pioneer at right with byso
    ma "Нет конечно!{w=1} Всё хорошо."
    show un smile pioneer at left with byso
    un "Да, теперь мы снова вместе."
    eth "{sc=2}{size=28}{color=#FF1010}Разорву вас в клочья!{w=1} Никогда не прощу!{w=1} Утоплю в крови!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Не забуду и не пожалею!{w=1} Всё нахуй вспомню!{/color}{/size}{/sc}"
    eth "{sc=2}{size=28}{color=#FF1010}Каждый момент вашей гадкой жизни!{/color}{/size}{/sc}"
    stop music fadeout 1
    minerva "Кх-кхм..."
    scene bg ext_boathouse_day
    show un surprise pioneer at fleft
    show image poter_n at left
    show mi upset pioneer at cleft
    show image minerva_mad at right
    show minerva_eye at right
    with byso
    play music Waijdan fadein 3
    "Эту трогательную сцену и ужасные мысли прервала Минерва."
    "Константин в ужасе обернулся.{w=1} Он не мог поверить в то, что она ещё жива."
    "Она стояла с жуткой ухмылкой до ушей, а её глаз, дёргаясь, бегал по присутствующим."
    mak "Костя, это твоя знакомая?"
    kt "Да...{w=1} Это она."
    minerva "Очень интересно.{w} Про меня ты уже рассказал?"
    kt "Как ты?..."
    minerva "Выжила?{w} Нормально."
    show mi shocked pioneer at cleft with byso
    ma "Что?{w=1} О чём вы?"
    "Минерва перевела взгляд на Машу.{w=1} Последняя явно испугалась."
    stop music fadeout 1
    "Константин почувствовал едва-уловимый запах гнили..."
    play sound3 sfx_bones_breaking volume 1
    "Тело Минервы неестественно захрустело."
    play sound3 slash volume 1
    play music "<from 8>inrealnost/Music/Music/SavXgeS.mp3"
    scene bg ext_boathouse_day
    show un scared pioneer at fleft
    show image poter_r at left
    show image minerva_zombie
    with fl_scare
    "Во мгновение ока она превратилась в ужасного монстра и одной рукой пробила спину Маши."
    minerva_z "О смерти!"
    "Константин вскочил с места к домику на пирсе и прижался к его стене рюкзаком."
    mak "Это альфа-гончая!"
    play sound3 "<from 0 to 4>inrealnost/Music/Sound/fem_screams.mp3"
    pause 0.5
    play sound3 knife2 volume 1
    "Маша попыталась закричать, но монстр оторвал ей нижнюю челюсть, после чего сбросил в воду." with fl_scare
    minerva_z "Ты следующий, говорливый ты наш!!!"
    hide un with byso
    "Лена в ужасе начала убегать, а Константин сквозь ужас улыбнулся."
    eth "{sc=2}{size=28}{color=#FF1010}Сбылось...{/color}{/size}{/sc}"
    play sound3 magic volume 1
    stop music fadeout 1
    hide image minerva_zombie with fl_scare
    "Макс запустил снаряд плазмы в Минерву, отчего та рассыпалась в труху."
    mak "Чёрт!{w} Кто притащил сюда альфа-гончую?!"
    play sound3 fem_krik volume 1
    "Позади раздался крик Лены."
    play music PerfectNothing fadein 3
    show image re_cr_smile_casual at right with byso
    "Оттуда вышла Рена, которая за волосы тащила Лену, словно игрушку."
    "Девушка кричала, пытаясь вырваться из захвата, но Рена продолжала медленно приближаться к Максиму."
    ren "Снова здорова, урод спектральный!"
    mak "Ты?!{w=1} Ты же мертва!!!"
    kt "Ха...{w=1} Повёлся..."
    mak "Костя?!{w} Ты меня обманул?!"
    hide image re_cr_smile_casual
    show image re_grin_casual at right
    with byso
    ren "Молодец, любимый!{w=1} Всё как учила."
    mak "Уёбок!!!"
    hide image re_grin_casual
    show image re_cr_smile_casual at right
    with byso
    "Пионер хотел запустить в Константина заряд плазмы, но затем посмотрел на Рену, которая была готова в любую секунду перерезать Лене горло кристальным ножом."
    ren "Не советую тебе этого делать..."
    ren "А то будет у твоей подруги на одну шею меньше."
    "Максим стиснул зубы и опустил руку."
    "Рена приблизились к Максиму на расстояние 2-3 метров."
    mak "И что вы от меня хотите, ебанутые?!"
    "В ответ они синхронно улыбнулась и переглянулись."
    kt "Твоей..."
    hide image re_cr_smile_casual
    show image re_cr_smile_casual at fleft
    hide image poter_r
    show image poter_r at left
    with vpunch
    "Рена в мгновение ока подскочила в спину Максима."
    ren "Смерти!"
    play sound electro volume 1
    pause 0.6
    play sound3 sfx_energy_door_bus volume 1
    scene bg ext_boathouse_day
    show image re_cr_smile_casual
    with fl_scare
    "Она вонзила нож идолопоклонников ему между шейных позвонков."
    "Максима парализовало и с яркой красной вспышкой он повалился на землю."
    mak "Бо-ольно-о!!!"
    play sound3 sfx_punch_washstand volume 1
    hide image re_cr_smile_casual
    show image re_cr_smile3_casual
    with byso
    "Он кричал, мотая головой.{w=1} Рена подошла к нему и пнула ногой."
    ren "Вы только посмотрите!{w=1} Наш загадочный пионер обрёл тело!"
    "Лена взяла пистолет и навелась Рене в спину."
    play sound2 vintovka volume 1
    play sound sfx_water_splash volume 1
    play sound3 "<from 6 to 10>inrealnost/Music/Sound/fem_screams.mp3"
    hide image re_cr_smile3_casual
    show image re_shy_casual
    with fl_fire
    "Выстрел."
    "Константин выстрелом из винтовки прострелил плечо Лены, отчего она выронила пистолет в воду."
    "На этот раз кричал не только Максим."
    kt "Не позволю."
    hide image re_shy_casual
    show image re_cr_smile_casual
    with byso
    "Рена подтащила Максима к пирсу и усадила его спиной к стенке."
    ren "А теперь у нас необычное шоу."
    "Она взяла Лену за волосы и подняла её голову."
    mak "Нет!{w} Не смей её убивать!!!"
    kt "В главных ролях...{w=1} Константин и Рена Брусковы."
    hide image re_cr_smile_casual
    show image re_cr_smile3_casual
    with byso
    ren "И название ему...{w=1} <<Долой предательские мысли>>!"
    "Рена достала маузер, который ранее принадлежал Минерве и приставила его к затылку Лены."
    mak "Не делай этого!{w} Забери меня, но не трогай её!"
    kt "А, так у вас, двух уродов, ещё и роман?"
    play sound3 wood_hit_head volume 1
    play sound sfx_bones_breaking volume 1
    play sound2 krik volume 1
    "Ударом ноги Константин сломал пальцы Максима, отчего тот завопил." with vpunch
    hide image re_cr_smile3_casual
    show image re_cr_smile2_casual
    with byso
    ren "Тем не менее, пора прекращать этот цирк.{w} Инреальность сама себя не уничтожит!"
    un "М-М-Максим...{w=1} Я...{w=1} Я люблю те...{w=0.31}{nw}"
    play sound pistol2
    pause 0.1
    play sound3 head_crush4 volume 1
    hide image re_cr_smile2_casual
    show image re_cr_smile_casual
    with fl_scare
    "Выстрел."
    "Лицо Лены на глазах у Макса разлетелось на куски обезличенного мяса."
    mak "Лена!!!"
    mak "За что вы с ней так?! {w=1}Она ничего вам не сделала!"
    hide image re_cr_smile_casual
    show image re_cr_smile3_casual
    with byso
    ren "А это тебе уже расскажет Костя."
    mak "Конченный псих!{w=1} Я говорил тебе обратись к специалисту! {w=1}Ебучий психопат-садист!!!"
    kt "Макс... {w=1}Всё тот же убогий лицемер-нытик."
    hide image re_cr_smile3_casual
    show image re_shy_casual
    with byso
    "Рена сильно удивилась, забрав из рюкзака Лены две фотографии."
    ren "Что? Это Федоренко?"
    kt "Да, тот самый..."
    mak "И ты меня знаешь?!{w=1} Ебанутые!{w=1} Ебанутые нелюди!"
    "Константин протянул Рене руку, взглядом указав на пистолет."
    mak "Что мы вам сделали?! {w}Мы ни в чём не виноваты!"
    hide image re_shy_casual
    show image re_grin_casual
    with byso
    "Рена поняла намёк и отдала ему пистолет Минервы."
    mak "Чтоб вы все подохли нахуй, дегенеративные!..."
    play sound3 sfx_lock_click volume 1
    scene bg kt_insane with byso
    "Константин вставил ствол ему в горло."
    kt "Хватит ныть!{w=1} Хоть на момент."
    "Он поводил пистолетом по его рту."
    kt "Чувствуешь этот вкус?"
    kt "Вкус стали и пороха..."
    kt "Пороха, которым убили твою убогую подружку."
    "Макс замычал, словно стараясь что-то проговорить."
    play sound3 sfx_punch_washstand volume 1
    "Рена тюкнула ему по голове ручкой топора."
    ren "Заткнись и слушай, придурь!"
    kt "Так почему мы её убили?{w=1} Да?"
    kt "Ответ прост как лист бумаги."
    kt "Вы оба меня оставили."
    kt "Маша то чёрт с ней, она просто не могла, обвинять мне её не в чем."
    kt "А ты и Лена оставили меня одного.{w=1} Даже не пытались мне помочь."
    kt "Я гнил заживо.{w=1} Вам было наплевать."
    kt "Теперь в новой жизни я вам это возвращаю.{w} С процентами."
    kt "Я считаю, физическая смерть в нашем случае примерно равна моральной."
    "Макс снова зашумел.{w=1} Константин вогнал ствол ещё глубже в горло."
    kt "Всё, тихо-тихо.{w} Конец истории."
    kt "Спокойной ночи, <<дорогой друг детства>>."
    play sound head_crush
    play sound3 pistol2 volume 1
    scene bg ext_boathouse_day
    show image re_cr_smile_casual
    with fl_scare
    stop music fadeout 3
    "Выстрел."
    "Содержимое черепной коробки Макса окрасило стену домика на пирсе."
    "Кровь стекала по стене, образуя на ней неровную красную дорожку."
    play music regret fadein 3
    "Константин обернулся и посмотрел на Рену."
    kt "Я так рад тебя вновь увидеть."
    play sound3 sfx_pat_shoulder_hard volume 1
    hide image re_cr_smile_casual
    show image re_grin_casual at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Он подошёл к ней и обнял."
    "Она на секунду прикрыла глаза, покачнулась и прижалась к нему.{w=1} Совсем как в первый раз."
    ren "И я рада...{w=1} Такое чувство, словно мы не виделись уже много лет..."
    hide image re_grin_casual
    show image re_sad_casual at center:
        zoom 1.25
        yanchor 0.05
    with byso
    ren "Если б ты знал, как мне грустно без тебя. Мне одиноко и пусто."
    kt "Мне тоже. {w=1}Я боялся, что ты не придёшь..."
    hide image re_sad_casual
    show image re_happy_casual at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Рена потёрлась головой о его плечо и хихикнула."
    ren "Ради тебя я убью любого врага.{w} Даже бессмертного."
    hide image re_happy_casual
    show image re_smile_casual
    with byso
    "Отпрянув друг от друга, они пошли с пирса."
    ren "Сходим на пляж?{w=1} У нас ещё есть время."
    kt "Откуда ты знаешь?"
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "По дороге я подбирала гончую для более эффектного появления, по дороге встретила сопротивление и выпытала у них, когда они начинают революцию."
    ren "Они будут тут примерно через час.{w=1} У нас есть время поесть и приготовиться."
    play sound3 sfx_put_sugar_cart volume 1
    "Константин снял рюкзак и достал оттуда две банки консервов."
    kt "Я взял."
    hide image re_grin_casual
    show image re_smile3_casual
    with byso
    ren "Мне?{w=1} Спасибо..."
    "Рена взяла банки и мило улыбнулась."
    ren "Ты такой заботливый..."
    kt "По крайней мере это минимум от того, чем я могу отплатить тебе."
    play ambience ambience_lake_shore_day volume 1 fadein 1
    scene bg ext_beach_day with fade
    show image re_smile_casual with byso
    "Дойдя до пляжа, они уселись на песке рядом друг с другом."
    kt "Приятного аппетита."
    "Пожелал Константин и протянул Рене вилку."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Спасибо, любимый."
    play sound3 open_can volume 1
    hide image re_grin_casual
    show image re_bored_casual
    with byso
    "Она открыла банку и начала изучать её наполнение."
    "Внутри была картошка с кусочками мяса."
    kt "Я вот что не понял...{w=1} А как ты доставила сюда гончую?"
    hide image re_bored_casual
    show image re_smile3_casual
    with byso
    ren "Это то?{w} Просто."
    hide image re_smile3_casual
    show image re_grin_casual
    with byso
    "Приступив к еде, она поправила беретик на голове."
    ren "Перед смертью наша подруга решила рассказать мне практически всё, что ей известно."
    ren "Среди всего этого она рассказала про то, что под морфием гончие становятся послушными."
    ren "И то, что продвинутые версии гончих умеют принимать форму людей."
    ren "Вот я так и поступила.{w=1} Взяла её труп и нашла гончую."
    ren "Потребовала её принять форму Минервы и думала, что она послужит хорошим боевым соратником."
    hide image re_grin_casual
    show image re_angry_casual
    with byso
    "Нахмурившись, Рена посмотрела в сторону пирса."
    ren "Правда один товарищ догадался её распылить..."
    kt "Ну и ладно."
    kt "А как битва прошла?{w=1} Получила ранения?"
    hide image re_angry_casual
    show image re_bored_casual
    with byso
    ren "Нет.{w=1} Цела."
    ren "Наша битва была построена на принципе двух ударов."
    ren "Серьёзное ранение и добивание. {w}Другого варианта у нас не было."
    hide image re_bored_casual
    show image re_dontlike_casual
    with byso
    "Поводив вилкой по дну банки она тяжело выдохнула."
    ren "Вот я и успела попасть первой, хоть наши силы не были равны."
    ren "Она мастерски стреляла.{w} Не думала, что хоть кто-то мог так хорошо обращаться с оружием."
    hide image re_dontlike_casual_casual
    show image re_smile_casual
    with byso
    ren "В остальном проблем не возникло. Ты как провёл это время?"
    play sound3 light_inh volume 1
    "Константин выдохнул и закурил."
    stop music fadeout 3
    kt "Меня чуть не сожрали гончие, сопротивленец чуть не перерезал глотку и вот история с Максимом."
    hide image re_smile_casual
    show image re_sad_casual
    with byso
    "Рена понимающе кивнула и покончила с первой банкой."
    play music god fadein 3
    ren "Но ты же не сожалеешь о таком обороте событий?"
    kt "Нет. {w=1}Ни разу."
    kt "Хотя может Машу жаль.{w} Она была ни при чём."
    hide image re_sad_casual
    show image re_dontlike_casual
    with byso
    ren "А что ты о ней помнишь?"
    play sound3 open_can volume 1
    "Спросила она, вскрывая вторую банку."
    "В другой банке были маринованные ананасы."
    "Константин не удержался и взял один."
    hide image re_dontlike_casual
    show image re_grin_casual
    with byso
    ren "И тебе приятного."
    "Улыбнулась Рена и отпила сладкой жидкости."
    kt "Спасибо."
    kt "Я её помню как милую девочку из Японии. {w=1}Правда выглядела тогда она куда лучше."
    kt "Она была внучкой наших соседей на даче.{w=1} Она была хорошей подругой, с ней было весело."
    hide image re_grin_casual
    show image re_bored_casual
    with byso
    kt "Правда уехала она однажды.{w} Их родители поссорились и увезли её в Японию."
    kt "С того момента я её больше не встречал.{w=1} Никогда."
    ren "Да, история неприятная.{w=1} Другой вопрос, что же она такого сделала, что попала в инреальность?"
    "Константин пожал плечами и, выкинув бычок, опёрся на руки."
    kt "Не знаю, не пророк Форбос."
    kt "Я бы поставил на затяжную депрессию.{w=1} Она была робкой и не могла строить отношения с другими людьми."
    kt "Ну и ладно, это в прошлом.{w} Главное, что мы целы."
    hide image re_bored_casual
    show image re_grin_casual
    with byso
    ren "Это и в правду главное.{w=1} Я очень за тебя переживала, когда мы разлучились."
    ren "Я вообще не понимала, куда я тебя отправила. Вдруг там сопротивление или те же самые гончие..."
    ren "Но ты справился.{w} Я горжусь тем, что достойна твоего внимания."
    "Константин улыбнулся и помотал головой."
    kt "Не говори ты так...{w=1} Звучит, словно я тебя тут хлыстом воспитываю."
    hide image re_grin_casual
    show image re_smile2_casual
    with byso
    ren "Хе... {w=1}Ладно, как скажешь."
    stop music fadeout 3
    play sound3 light_inh volume 1
    "Рена взяла у Константина из кармана сигареты и закурила."
    kt "Зависимость?"
    hide image re_smile2_casual
    show image re_smile_casual
    with byso
    ren "От сигарет?{w=1} Нет."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "От тебя? {w=1}Да."
    "Она выкинула вторую банку и положила голову на плечо Константина."
    play music umted fadein 3
    ren "Никак не могу тобой насладиться в полной мере.{w=1} Ты такой хороший..."
    play sound3 glad volume 1
    "Погладив Константина по ноге, она поцеловала его в шею."
    hide image re_grin_casual
    show image re_happy4_casual
    with byso
    ren "Добрый и красивый.{w=1} Главное что добрый."
    ren "Вот увидишь, мы выберемся отсюда и начнём новую жизнь."
    ren "Будем жить вместе, как все нормальные люди."
    ren "Переедем в новый город, заживём, если хочешь, в большой семье."
    ren "Мы будем счастливы вместе.{w} Я обязательно что-нибудь придумаю, вот увидишь."
    ren "Обязательно, обязательно..."
    ren "Только для начала давай покончим с прошлым."
    kt "Я согласен.{w=1} Настало время перестать прятаться и ударить врагу по морде."
    hide image re_happy4_casual
    show image re_grin_casual
    with byso
    "Встав с места, Рена указала в сторону лагеря."
    ren "Пошли, нам ту...{w=0.41}{nw}"
    play sound3 sfx_pat_shoulder_hard volume 0.61
    scene bg re_headpat with byso
    "Константин подвинул беретик Рены и погладил её по голове."
    "Как-то сразу стало легче на душе."
    play sound3 glad volume 1
    "Как кошка, она потерлась о его руку головой, и он погладил свою любимицу.{w=1} Рена чуть не замурчала от удовольствия."
    "Разворошив её волосы, он снова почувствовал тот приятный еловый запах."
    "Кошки любят, когда их гладят."
    kt "Спасибо тебе большое.{w=1} За всё что ты для меня сделала и делаешь."
    kt "Даже и не знаю, как выразить свою благодарность."
    kt "Ты столько всего для меня сделала.{w=1} Сколько раз ты мне помогала, сколько раз спасала меня."
    kt "Я думал, что уже сошёл с ума.{w=1} А ты опять мне помогла."
    kt "И даже если моя жизнь пройдёт в аду, в ней всё равно есть частичка твоей светлой души."
    kt "Теперь мне легче жить, когда ты мне уделяешь столько внимания."
    kt "Знаешь, я как человек вырос.{w=1} Вроде бы, дальше некуда, но ты снова меня спасла."
    kt "Сделала лучше."
    "Рена поцеловала Константина и крепко обняла."
    ren "Знаю, любимый..."
    ren "Я всегда буду рядом.{w=1} Несмотря ни на что."
    ren "Мы вместе навсегда.{w=1} И никто не сможет отобрать тебя у меня."
    ren "А теперь...{w=1} Нам пора убивать."
    ren "Ради нас. {w}Ради нашего светлого будущего."
    stop music fadeout 3
    kt "Убьём их всех."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_square_day
    show image re_smile_casual
    with fade
    "Выйдя на площадь, они переглянулись."
    "На площади сидела Лена и читала книгу, а Славя ходила вокруг да около, словно пытаясь кого-то найти."
    play music phHAISE fadein 3
    hide image re_smile_casual
    show image re_cr_smile_casual
    with byso
    ren "Начнём наш танец на костях?"
    play sound3 weapon volume 1
    "Константин взял в руки винтовку и дёрнул затвор."
    kt "Начнём."
    play sound3 sfx_dinner_horn_processed volume 1
    play sound vintovka volume 1
    "Прозвучал горн, под который раздался выстрел винтовки." with vpunch
    play sound3 sfx_bush_body_fall volume 0.51
    "Славя упала замертво, окрасив памятник Генде своей кровью."
    "Лена словно и не услышала выстрела, продолжая читать книгу."
    play sound3 sfx_punch_medium volume 1
    hide image re_cr_smile_casual
    show image re_smile_casual_topor
    show un angry pioneer at left
    with byso
    "Рена взяла топор и отобрала у Лены книгу."
    un "Эй!{w=1} Ч-что ты делаешь?"
    show un scared pioneer with byso
    ren "<<Маленький принц>>?{w} Банальщина!"
    play sound3 slash volume 1
    play sound sfx_bodyfall_1 volume 1
    hide un with fl_scare
    "После этих слов, она отрубила темноволосой девушке голову."
    "Голова покатилась по земле и укатилась в кусты."
    ren "Кажется, что это надолго."
    "Послышались крики.{w=1} Константин улыбнулся."
    kt "Устроим бойню!"
    ren "Вместе!"
    window hide
    $ volume(0, "music")
    play sound3 Glitch3 volume 1
    stop ambience fadeout 1
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 0.1
    show image hex1
    show image monitor_adm
    with dissolve
    play sound_loop Radar fadein 3
    mal "Что происходит, пап?{w} Стабильность 20-32g неуклонно падает."
    mal "С 84 до 43 за 5 наших минут."
    "Генда подошёл к монитору и улыбнулся."
    gg "Это восстание, о котором я тебе говорил, Широ.{w=1} Мне его нужно будет подавить."
    gg "Я сделаю это сам, но учти, что рано или поздно тебе придётся с этим столкнуться."
    ik_sh "Но я могу тебе чем-то помочь?"
    gg "Нет, мальчик мой.{w=1} Я сам с этим справлюсь."
    gg "Иди домой.{w=1} Мама обещала приготовить что-то вкусное на ужин."
    gg "Заодно повтори теорию механики.{w=1} Я вернусь - спрошу."
    ik_sh "Как скажешь, папа.{w=1} Удачи."
    "Мальчик растворился в воздухе, а Генда посмотрел на монитор."
    gg "Ломятся...{w=1} Ну ничего."
    gg "Собираю армию и еду к вам.{w=1} Посмотрим кто там такой наглый."
    gg "А сейчас..."
    gg "Компьютер!{w=1} Перевести все механизмы автокоррекции на 20-32g."
    gt4 "Так точно.{w=1} Все механизмы переведены на 20-32g."
    stop sound_loop
    play sound3 Glitch3a volume 1
    show Glitch_screen3:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 1
    play ambience ambience_ext_road_night volume 1 fadein 1
    play sound3 vintovka volume 1
    $ volume(1, "music")
    scene bg ext_square_night_blood
    show image re_smile_casual_topor
    with fl_fire
    "Выстрел."
    "Константин пронзил голову Шурика из винтовки, отчего тот пал на землю."
    hide image re_smile_casual_topor
    show image re_normal_casual_topor
    with byso
    ren "Я посчитала.{w=1} Мы убили 114 пустышек.{w} Почему всё ещё не открылись порталы?"
    kt "Да если бы я знал...{w=1} Странно всё это..."
    play sound3 reload volume 1
    "Он снял магазин и начал докладывать патроны."
    kt "Две пачки патронов вылетели."
    stop music fadeout 2
    hide image re_normal_casual_topor
    show image re_guilty_casual
    with byso
    ren "Костя..."
    kt "Что?"
    ren "У нас проблемы."
    play music "<from 10.5 to 220>inrealnost/Music/Music/obscure.mp3" fadein 3
    "Рена указала на выход из лагеря.{w=1} Оттуда бежали вооружённые повстанцы."
    kt "Ебучий случай!{w=1} Ретируемся!"
    hide image re_guilty_casual
    show image tolpa
    with byso
    "Собравшись, они спрятались за памятник Генды."
    "Константин передал пистолет Рене и прицелился в первого попавшегося сопротивленца."
    play sound3 pistol2 volume 1
    pause 0.4
    play sound pistol2 volume 1
    pause 0.4
    play sound2 pistol2 volume 1
    "Рена выстрелила трижды и каждый патрон достиг чьей-то головы, уронив неуклюжее тело на землю."
    vng "Это идолопоклонники!{w=1} Уничтожить!"
    play sound_loop fireing volume 1
    play sound3 Molotov volume 1
    pause 1
    scene bg int_fire with fl_fire
    "В их сторону полетели коктейли Молотова.{w=1} Трупы, лежавшие на площади быстро подхватили пламя."
    "Константин и Рена скрылись за статуей Генды."
    show image re_rage_casual with byso
    ren "Вот шерсть несчастная!{w=1} Я их порублю!"
    kt "Стой, Рена!{w} Их слишком много, нельзя так рисковать!"
    idol_k "Кто-то сказал рисковать?!"
    hide image re_rage_casual
    show image re_shy_casual
    show image sh_idol2 at right
    with byso
    "Со стороны третьего корпуса к ним прибежал Карачун."
    kt "Карачун? {w=1}Что ты тут делаешь?"
    idol_k "А я и не один!"
    show image idol_palladin at left with byso
    "К ним в укрытие запрыгнул <<Паладин>>."
    idol_p "С минуты на минуту прибудет остальная община!{w=1} Не беспокойтесь."
    hide image re_shy_casual
    show image re_cr_smile_casual
    with byso
    ren "Отлично!{w=1} Мне нужно отвлечь их внимание!"
    idol_k "Дважды просить не придётся!"
    play sound3 cheka volume 1
    "С диким смехом Карачун достал из карманов несколько гранат и зубами выдернул из них кольца."
    idol_k "Ловите хавку, фраера!"
    vng "В укрытие!"
    play sound3 bum volume 1
    "Взрыв." with fl_fire
    "Созданный взрыв разбил ряды сопротивления и забрал с собой несколько человек."
    "На взрыв прибежало около ста человек и начали стрелять."
    idol_p "А вот и наша община."
    sold "Охранять капитана!"
    idol_p "Умрите, еретики!"
    "<<Паладин>> начал из своего пулемёта поливать противников свинцом."
    hide image re_cr_smile_casual
    show image re_smile_casual_topor
    with byso
    ren "Не скучай, любимый.{w=1} Настало время нарезать немного свинины."
    hide image re_smile_casual_topor with bso
    "Рена вылетела из укрытия, а Константин старался прикрывать её из винтовки."
    scene bg bloody_mess with fl_scare
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "Война была странной.{w=1} Война была неожиданной."
    "Все сражались."
    "Одни отстаивали своё право на свободу, а другие пытались защитить этот мир."
    "Идолопоклонники против сопротивления.{w=1} Огонь против льда. {w=1}Бог против справедливости."
    "Среди всего этого - Константин и Рена.{w=1} Возлюбленные, сражающиеся за любовь.{w=1} Без особых правил."
    "Даже в бою они дополняли друг друга. {w=1}Она - мастер ближнего боя, а он - талантливый стрелок."
    "Но главным для них был даже не бой."
    "Главным был танец в кровавой пелене, танец понимания, достигший завершенности."
    "Нельзя было сказать, что у какой-то из сторон было преимущество."
    "Сражение сводилось к формуле один повстанец на одного фанатика."
    "Всё решал танец Константина и Рены.{w=1} Танец без правил, в котором не было чётких движений, но была удивительная красота."
    "Может ли в убийстве быть красота?{w=1} Был ли этот танец безобразен?"
    "Нет.{w} Этот бой был завершающим этапом истории.{w=1} Её и его.{w=1} Последним танцем их любви."
    "Тот самый момент со ставкой <<всё или ничего>>."
    "Пожалуй, это был самый чёрный час."
    "Последняя битва в вечности, где они встретились."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    scene bg int_fire with byso
    "Бой продолжался около получаса.{w=1} Повстанцев и фанатиков в сумме оставалось около 140 человек."
    show image re_holod_casual with byso
    "Рена вернулась к Константину в укрытие."
    "Она принесла несколько пачек патронов, которые смогла ухватить."
    kt "Как ты?!"
    ren "Тяжко... {w=1}Очень сложно так долго махать топором!"
    kt "Передохни. {w}Я пока займусь отстрелом."
    kt "Карачун!{w=1} Новый магазин!"
    show image sh_idol2 at right with byso
    idol_k "Ща сделаем!"
    "Карачун выхватил у Константина пустой магазин и выдал новый."
    show image idol_palladin at left with byso
    idol_p "Перезаряжаюсь!"
    ren "Это всё никак не может закончиться!"
    "Константин выстрелил в одного из повстанцем и нырнул обратно в укрытие."
    kt "Их слишком много мы не можем..."
    stop music fadeout 3
    hide image sh_idol2
    show image sh_idol at right
    hide image re_holod_casual
    show image re_shy_casual
    with byso
    play music "<from 0 to 234>inrealnost/Music/Music/Soma.mp3" fadein 1
    gg "Так-так-так..."
    stop sound_loop fadeout 1
    scene bg genda with byso
    "Стрельба прекратилась. Некоторые идолопоклонники упали на колени."
    idols "Да здравствует всевышний."
    gg "Те, кто не верит в пророчество могут отправляться на базу."
    idols "Ваша воля закон."
    "Ряды идолопоклонников быстро опустели.{w} Среди них осталось буквально 10 человек, включая Карачуна и <<Паладина>>."
    gg "Предатели...{w=1} Вы оставили своего бога!"
    idol_k "Попей из краника!{w=0.41} Пророчество не врёт!"
    idol_k "Смещай жопу с трона!"
    andrp "Вы оставили Генду?! {w}Тогда какого чёрта вы убиваете моих людей?!"
    idol_p "Потому что нам не нужно сопротивление на божественном троне!"
    gg "Дамы-дамы...{w=1} Прошу..."
    gg "Я скажу вам так..."
    gg "Тут остались только те, кого я должен искоренить."
    gg "Тоже мне...{w=1} <<Сопротивление>>..."
    gg "О, а среди вас есть знакомые лица..."
    gg "Калинин Андрей Романович.{w=1}.. Я думал тебя убило вместе с тем Мишей..."
    gg "Несветаева Валерия Викторовна.{w=1}.. Ты снова пережила своего бывшего..."
    gg "Рыжая бестия.{w=1}.. Оказалось, ты лишь плод фантазии Константина...{w=1} Обидно наверное..."
    gg "И Брусков Константин Павлович.{w=1}.. Не думал, что ты так сильно меня возненавидишь..."
    gg "А вы...{w=1} Лжецы...{w=1} Я вас кормил, даже выделил отдельную симуляцию для вас."
    gg "И чем вы ответили своему богу?{w=1} Ножом в спину?!"
    idol_k "Нет!{w=0.341} Хуем по лбу!"
    "Генда ухмыльнулся и покачал головой."
    gg "Понятно..."
    andrp "Приказываю всем!{w=1} Огонь по Генде!"
    play sound_loop fireing
    show genda_fire with byso
    "Все присутствующие открыли огонь по создателю.{w=1} Все заряды пролетали сквозь него, не оставляя никаких повреждений."
    stop sound_loop fadeout 1
    hide genda_fire
    scene bg genda
    with byso
    "Осознав, что это не эффективно, они прекратили огонь."
    gg "Очень мило..."
    play sound_loop monsters_run volume 0.31
    "Вдалеке раздался топот.{w=1} Звук был такой, словно тысячи воинов в тяжёлых доспехах бежали в бой."
    gg "15 секунд."
    play sound_loop monsters_run volume 0.7
    "Топот нарастал с каждой прошедшей секундой."
    play music "<from 234>inrealnost/Music/Music/Soma.mp3"
    gg "Гончие, разорвать!"
    gg "А я лично посмотрю, как ваши трупы украсят эту площадь!"
    scene bg int_fire
    show image re_holod2_casual
    show image idol_palladin at fright
    show image sh_idol at right
    show image andr_nervous2 at left
    with byso
    "Проговорил Генда и растворился в воздухе. {w=1}У входа в лагерь было видно огромные толпы гончих."
    kt "Ёбаный рот..."
    idol_p "Боже..."
    ren "М-да..."
    hide image sh_idol
    show image sh_idol2 at right
    with byso
    idol_k "Ебать щас мясо будет!"
    hide image andr_nervous2
    show image andr_angry at left
    with byso
    andr "Отряд, огонь по мутантам!!!"
    play sound_loop fireing
    scene bg bloody_mess with byso
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "Все те, кто воевали против друг друга решили отложить свои разногласия."
    "Во всяком случае временно. {w=1}Сейчас встал враг куда опаснее - монстры."
    "Их бешеная прогрессия делает невозможным любую жизнь в этой симуляции."
    "Пусть победит сильнейший.{w=1} Безо всякого компромисса."
    "Константин и Рена поняли, что ситуация куда хуже, чем может показаться на первый взгляд."
    "Они почувствовали, как тьма стала пробираться в их души, вызывая тревогу и страх друг за друга."
    "По их лицу и движениям было понятно, насколько они напряжены."
    "То, что было танцем стало набором хаотичных движений, направленных на сохранение своих жизней."
    "Рене оказалось сложнее.{w} Поскольку она была воином ближнего боя, монстры доставляли куда больше проблем именно ей."
    "Даже несмотря на то, что она была намного сильнее обычного человека."
    "Изнурительная бойня, влекущая за собой смерть."
    "Ад на земле.{w=1} Повстанцы гибли один за другим."
    "Но внезапно все изменилось."
    "Отнюдь не в лучшую сторону."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    show image pas_angry at left
    show image val_angry at right
    show image andr_nervous2
    with byso
    andrp "Отряд!{w=1} Отступаем!{w=1} Протокол <<затмение>>!"
    play sound3 teleport volume 1
    hide image pas_angry
    hide image andr_nervous2
    hide image val_angry
    show image val_scared at right
    with fl_fast
    "С яркой вспышкой часть отряда сопротивления растворилась в воздухе, использовав телепортаторы."
    csp "Что?!{w=1} Не работает!"
    show image re_rage_casual with bso
    ren "Предатели!{w=1} Трусы!"
    play sound slash volume 1
    hide image val_scared
    hide image re_rage_casual
    show image re_rage_casual_topor
    with fl_scare
    "Рена отрубила голову зазевавшейся медсестре."
    show image sh_idol at left
    hide re_rage_casual_topor
    with bso
    idol_k "Да нас порвут нахуй!!!"
    play sound3 cheka volume 1
    hide image sh_idol
    show image sh_idol2 at left
    with byso
    "Вытащив несколько гранат с трупов, Карачун их активировал и как живая бомба побежал в пущу монстров."
    idol_k "Увидимся в аду, друзья! {w=0.321}Банзай нахуй!!!"
    show image idol_palladin at right with byso
    idol_p "Брат!{w=1} Не делай этого!!!"
    idol_k "Хоть когда-то у меня были друзья!!!"
    play sound3 slash volume 1
    hide image sh_idol2
    show image monster at left
    with fl_scare
    "Гончие схватили Карачуна и начали разрывать и без того покалеченное тело."
    play sound3 bum volume 1
    hide image monster with fl_fire
    "Взрыв."
    "Своим пожертвованием Карачун убил около 15 гончих."
    idol_p "Брат!!!{w=1} Нет!"
    play sound3 head_crush4 volume 1
    hide image idol_palladin with fl_scare
    "На <<Паладина>> набросилось несколько гончих."
    kt "Сука!!! {w=1}Что вы делаете, идоты?!"
    "Людей на площади становилось всё меньше и меньше."
    scene bg int_fire with byso
    "Материализовался Генда."
    gg "Что такое?{w=1} Может быть уже сдадитесь на переработку?"
    hide image re_rage_casual_topor
    show image re_rage_casual
    with byso
    ren "Мечтай!"
    scene bg genda with byso
    "Генда образовался перед Константином."
    gg "Что я говорил?"
    gg "Твои дни сочтены!"
if rerp == 15:
    jump BuiltOnBlood_ending
else:
    jump MankindIsDead_ending
label BuiltOnBlood_ending:
    play sound3 electro volume 1
    pause 0.5
    play sound3 sfx_energy_door_bus volume 1
    scene bg int_fire
    show image re_rage_casual
    with fl_scare
    "Не успел Генда поднять руку, как Рена пронзила его шею подаренным клинком."
    ren "Выкуси!"
    "В отличие от пионера, Генду не парализовало - он дематериализовался."
    kt "Ебать ты вовремя!"
    hide image re_rage_casual
    show image re_normal_casual_topor
    with byso
    ren "Знаю!{w=1} Надо сражаться!"
    play sound3 sfx_punch_medium volume 1
    "Она дала Константину два пистолета заместо винтовки."
    hide image re_normal_casual_topor
    show image re_smile_casual_topor
    with byso
    ren "Разрывные патроны. {w=1}Мы их отделаем!"
    "Константин улыбнулся и вернулся в бой."
    stop ambience fadeout 1
    $ volume(0, "music")
    stop sound_loop fadeout 1
    play sound Glitch3
    $ _dismiss_pause = False
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    stop sound
    $ renpy.block_rollback()
    scene bg black
    pause 1
    play sound_loop OMORI2 fadein 1
    pause 1
    play sound error1
    show image error_txt1
    pause 3
    play sound error1
    show image error_txt2
    pause 4
    play sound error1
    show image error_txt3
    pause 0.21
    play sound error2
    show image error_txt4
    pause 0.81
    play sound error2
    show image error_txt5
    pause 0.41
    play sound error2
    show image error_txt6
    pause 2
    play sound error2
    show image error_txt7
    pause 1
    play sound Glitch3a
    stop sound_loop
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    stop sound
    scene bg black
    pause 1
    $ _dismiss_pause = False
    $ renpy.block_rollback()
    scene bg int_fire with fl_fire
    $ volume(1, "music")
    "Константин и Рена остались единственными выжившими на площади.{w=1} Помимо них оставалось ещё пара десятков гончих."
    play sound power
    "На площади открылся один портал."
    kt "Рена!{w=1} Порталы открыты!"
    show image re_smile_casual_topor with bso
    "Она отскочила от гончих и побежала в портал."
    ren "Неужели!{w=1} Прыгаем."
    stop music fadeout 3
    scene bg black with byso
    "Запрыгнув в портал, они растворились в небытие."
    pause 1
    play music ElfenLied fadein 3
    scene bg kt_room
    show shum_red
    with byso
    re_na "Ты ещё способен любить, я это чувствую."
    re_na "Когда-нибудь всё изменится и мы вместе сможем по-настоящему насладиться своей жизнью."
    kt "Наслаждение?{w=1} Жизнью? {w=1}Бред..."
    kt "Уже ничего не станет лучше, чем сейчас."
    re_na "Станет, вот увидишь."
    re_na "Жизнь совершенно непредсказуемая штука.{w} Ты даже представить не можешь, что тебя ожидает завтра."
    re_na "Непредсказуемая абсолютно, до мельчайших деталей.{w=1} Понимаю, ты прошёл через такую боль, что хочешь поскорее всё забыть..."
    re_na "Но ты сможешь когда-то вернутся к нормальной жизни."
    re_na "И тогда будешь жить с новым знанием, новым пониманием того, какой она была на самом деле."
    re_na "Я не хочу, чтобы это знание прошло с тобой через войну и разочарование."
    re_na "Правда это может быть неизбежно..."
    scene bg black with byso
    pause 1
    scene bg white
    show image re_shy_casual
    show unblink
    "Они очнулись в бесконечной белой комнате."
    ren "Что?...{w=1} Где мы?"
    "Константин и Рена переглянулись. Вокруг не было ничего кроме стерильной белой пустоты."
    kt "Не знаю..."
    "Он обнаружил, что у него не осталось никакого оружия."
    th "Бесконечная белая комната...{w=1} А у меня нет оружия."
    ren "Минерва говорила, что когда инреальность будет близко к обрушению, то могут быть самые непредсказуемые последствия."
    kt "Да, и это походу одно из них..."
    "Константин повертел головой.{w} Вокруг не было ничего, даже горизонта."
    hide image re_shy_casual
    show image re_sad_casual
    with byso
    ren "А что если мы попали из инреальности в другой мир?"
    kt "Не знаю..."
    kt "Пошли."
    hide image re_sad_casual
    show image re_shy_casual
    with byso
    ren "Но куда?"
    kt "Вперёд."
    kt "Только вперёд."
    hide image re_shy_casual
    show image re_grin_casual
    with byso
    ren "Пойдём."
    play sound3 sfx_pat_shoulder_hard volume 0.61
    "Рена взяла Константина под руку и пошла в шаг с ним."
    ren "Но даже если мы тут навсегда, то я рада, что мы вместе."
    hide image re_grin_casual
    show image re_smile_casual
    with byso
    ren "Кстати, я хотела спросить..."
    kt "Что такое?"
    hide image re_smile_casual
    show image re_happy_casual
    with byso
    ren "Когда мы вернёмся в наш мир, мы сыграем свадьбу?"
    play sound3 glad volume 1
    "Константин улыбнулся и погладил свою девушку по голове."
    kt "Конечно."
    hide image re_happy_casual
    show image re_grin_casual
    with byso
    ren "Тогда мы на ней будем одни."
    ren "Оформим бумаги, чисто для формальности, а потом, после церемонии пойдём в китайский ресторанчик."
    ren "Закажем себе курочки в кисло-сладком соусе со спаржей и, выпив немного тёмного пива, насладимся вечером друг с другом?"
    "Он заглянул в бесконечную пустоту и, переведя добрый взгляд на Рену, тепло улыбнулся."
    kt "Хорошо, мне нравится твоя идея."
    kt "Осталось только выйти отсюда."
    hide image re_grin_casual
    show image re_smile_casual
    with byso
    ren "Выйдем."
    ren "Даже если ради этого придётся убить ещё сотню людей."
    show image serv_door at right:
        zoom 0.05
        yalign 0.5
    with byso
    "Среди бесконечной белизны показался маленький зелёный прямоугольник."
    hide image re_smile_casual
    show image re_grin_casual at left
    with byso
    kt "А вот и выход!{w} Побежали!"
    "Сорвавшись с места, они побежали к единственному объекту в огромной белой комнате."
    hide image serv_door
    show image serv_door at right:
        zoom 0.1
        yalign 0.5
    with byso
    "Прямоугольник становился всё больше и отчётливее с каждым шагом."
    hide image serv_door
    show image serv_door at right:
        zoom 0.3
        yalign 0.5
    with byso
    "Он возвышался над белым полом, как огромное нематериальное существо, чуждое человеческому разуму."
    hide image serv_door
    show image serv_door at right:
        zoom 0.4
        yalign 0.5
    with byso
    "Оно блестело, казалось, его питает какой-то чудовищный источник энергии, но его поверхность всё ещё была совершенно гладкой и чистой."
    hide image serv_door
    show image serv_door at right:
        zoom 0.6
        yalign 0.5
    with byso
    "Внутри казалась зелёная комната с одним силуэтом."
    hide image re_grin_casual
    show image re_holod2_casual at left
    hide image serv_door
    show image serv_door at right:
        zoom 0.8
        yalign 0.5
    with byso
    "Силуэт постепенно увеличивался и наконец стал различимым - это был Генда посреди зелёной серверной комнаты."
    hide image serv_door
    show image serv_door at right
    with byso
    "Его тело было скрючено, а из места удара Рены сочилась ярко-красная кровь."
    hide image re_holod2_casual
    show image re_angry_casual at left
    with byso
    ren "Эй, ты!"
    "Генда не реагировал.{w=1} Видимо, этой дыры в пространстве не было для его взгляда."
    "Он что-то наговаривал себе под нос."
    gg "Стабильность инреальности 2 процента...{w=1} Надо вводить аварийный протокол..."
    gg "Компьютер!{w=1} Аварийный протокол."
    gt4 "Инициализация аварийного протокола.{w=1} Пиковая мощность механизма автокоррекции."
    gt4 "Внимание!{w=1} Возможны серьёзные повреждения симуляций!"
    gg "Уже нет выбора..."
    stop music fadeout 3
    gt4 "После активации аварийного протокола стабильность возрастёт до...{w=1} 20 процентов."
    gt4 "Примерное время ожидания - 2 минуты."
    gg "Отлично..."
    play sound3 sfx_mystery_movement volume 1
    "Генда отошёл от компьютера и сел в кресло."
    play music PerfectNothing fadein 13
    hide image re_angry_casual
    show image re_cr_smile_casual
    with byso
    ren "А вот этого нам не надо..."
    "Рена достала свой кинжал. {w}В отличие от орудия Константина, он сохранился."
    ren "А вот и наше великое божество потеряет голову."
    kt "Надо подкрасться к нему незаметно."
    ren "Точно.{w=1} Пошли."
    play ambience sfx_computer_noise volume 1 fadein 1
    scene bg gg_centr
    show image re_cr_smile_casual
    with byso
    "Рена шагнула в дверь перед Константином, а затем и Константин совершил переход."
    "Взяв кинжал покрепче, Рена начала приближаться к Генде."
    gg "Широ?{w=1} Я тебе говорил, подожди в гостиной.{w} У меня ещё остались дела."
    hide image re_cr_smile_casual
    show image re_cr_smile3_casual
    with byso
    ren "Не угадал!"
    play sound3 sfx_chair_fall volume 1
    "Рена ударом ноги сбила Генду со стула." with vpunch
    "Создатель упал на металлический пол и, словно её не ждав, выпучил глаза."
    gg "Ты-ы?!"
    hide image re_cr_smile3_casual
    show image re_cr_smile_casual
    with byso
    ren "Жене своей будешь ночью тыкать, а ко мне на <<вы>>!"
    play sound3 knife_in volume 1
    "Он попытался отползти, но Рена вонзила кинжал ему в ляжку, подтянув к себе." with vpunch
    play sound power volume 1
    scene bg black with bso
    scene bg gg_centr
    show image re_cr_smile_casual
    with bso
    scene bg black with bso
    scene bg gg_centr
    show image re_cr_smile_casual
    with bso
    "Удар кинжала, судя по всему вывел из строя серверную."
    gt4 "Ошибка в инициализации аварийного протокола! {w=1}Абсолют нестабилен."
    hide image re_cr_smile_casual
    show image re_cr_smile2_casual
    with byso
    ren "Куда это ты собрался?! {w=1}Лежать!"
    gg "Что ты натворила?!{w=1} Инреальность сейчас рухнет!"
    kt "А мы, знаешь ли, этого и ожидали."
    hide image re_cr_smile2_casual
    show image re_cr_smile_casual
    with byso
    ren "В королевстве дураков и король дурак."
    play sound3 head_crush volume 1
    pause 0.3
    play sound sfx_bones_breaking volume 1
    "Вонзив кинжал в грудь Генды, она провернула его, разломав рёбра."
    gg "Все вы тут умрёте!"
    "Кричал Генда, словно пытаясь бороться за свою жизнь."
    hide image re_cr_smile_casual
    show image re_cr_smile2_casual
    with byso
    ren "Очень жаль, но этого ты уже не застанешь!"
    play sound3 knife_out volume 1
    play sound head_crush volume 1
    stop music fadeout 3
    "Она выдернула нож и пробила божеству череп." with fl_scare
    "Он издал булькающий звук, закатил глаза и обмяк."
    "Его руки и ноги перестали шевелиться, а кровь из рассеченной головы потекла на пол."
    "Некоторое время Рена стояла неподвижно, пристально глядя на труп."
    play music regret fadein 3
    hide image re_cr_smile2_casual
    show image re_grin_casual
    with byso
    "Затем встала на ноги."
    ren "С ним всё."
    kt "Как удобно.{w=1} Он не разлогинился на компьютере."
    scene bg server2 with byso
    "Встав вокруг монитора, они переглянулись."
    kt "Компьютер!"
    gt4 "Ожидаю команды."
    ren "Отключить механизмы автокоррекции!"
    gt4 "Вы уверены?{w=1} Это действие вызовет распад первичной структуры инреальности и смерть всех субъектов."
    kt "Уверены."
    gt4 "Требуется подтверждение биометрии."
    play sound3 sfx_lock_click volume 1
    "Открылась небольшая ячейка на столе.{w=1} Судя по всему для пальца."
    play sound3 horror1 volume 1
    "Рена взяла руку мёртвого бога и начала срезать кисть."
    kt "Биометрия...{w=1} Так себе защита."
    ren "А особенно когда труп Генды лежит у тебя под ногами."
    play sound3 head_crush volume 0.61
    "Рена срезала кисть Генды и приложила его большой палец."
    play sound power volume 1
    scene bg black with bso
    scene bg server2
    with bso
    scene bg black with bso
    scene bg server2
    with bso
    play sound_loop sirenn volume 0.51
    "Всё оборудование несколько раз моргнуло, после чего зашумела тревога."
    gt4 "Выполнено."
    gt4 "Внимание!{w} Распад первичной структуры через...{w=1} 45 секунд."
    gt4 "Эвакуируйтесь!{w=1} Эвакуируйтесь!"
    kt "Компьютер!{w=1} Эвакуация всех, кто находится в административной симуляции."
    gt4 "Выполняю поиск."
    gt4 "Обнаружено 2 живые сущности."
    gt4 "Внимание!{w=1} Осталось 30 секунд до распада первичной структуры."
    gt4 "До перехода осталось... {w=1}Пять секунд."
    "Константин Рена и переглянулись.{w=1} Их глаза блестели и они точно понимали, что победили."
    gt4 "Четыре."
    "Неощутимая эмоциональная волна разошлась по их мозгу и стала реальностью."
    gt4 "Три."
    "Они обняли друг друга и ощутили удовольствие от победы."
    gt4 "Два."
    "Одновременно они почувствовали, как мысли встают на второй план и наступает великая свобода – свобода духа, свобода воли."
    gt4 "Один."
    ren "С перерождением, любимый."
    gt4 "Выполняю."
    stop sound_loop fadeout 1
    stop ambience fadeout 1
    stop music fadeout 1
    play sound3 delete volume 1
    pause 0.5
    show Glitch_screen2:
        size (1920, 1080)
    pause 1
    scene bg black with byso
    pause 2
    play music Radar fadein 3
    scene bg semen_room
    show unblink
    "Константин проснулся в кровати."
    "Голова болела как с тяжёлого похмелья."
    "Мысли путались, в голове стоял звон."
    play sound3 sfx_bed_squeak2 volume 1
    "Константин сполз по кровати на пол, уткнувшись лицом в старый ковёр."
    "Больше всего в таком состоянии хотелось принять горизонтальное положение, заснуть и больше никогда не просыпаться."
    play sound3 sfx_home_phone_ring volume 1
    "Зазвонил телефон."
    play sound3 sfx_home_phone_take volume 1
    "Шмыгнув носом, Константин с неохотой взял трубку."
    kt "Слушаю..."
    rekla "Добрый вечер.{w=1} Вас беспокоит компания <<Дом.ру>>.{w=1} Мы спешим вам сообщить, что ваш тариф <<Домашний 2016>> находится в архиве."
    rekla "Мы можем предложить вам новый тариф <<Домашний 2018>>, который включает в себя интернет, с которым..."
    kt "Так...{w=1} Какой <<Домашний 2016>>?{w} Я только три года назад поставил <<Домашний 2019>>."
    "По ту сторону провода раздалось недоуменное молчание."
    rekla "Я не понимаю о чём вы.{w=1} К сожалению у нас ещё нет такого тарифа, он будет выпущен ещё через 2 года."
    kt "До свидания."
    play sound3 sfx_home_phone_break volume 1
    "Константин сбросил звонок и, поморщившись, встал с пола."
    "На столе стояла старая бутылка креплёного пива."
    "Жидкость в ней была уже без газа, похожей на мочу."
    th "Чёрт...{w=1} А где Рена?"
    "Он взял бутылку и обратил внимание на дату изготовления."
    "<<29.11.2018>>."
    th "Чего? Оно из срока вышло уже 4 раза..."
    play sound3 sfx_click_1 volume 1
    "Отставив бутылку, он включил компьютер и обнаружил на столе упаковку честера."
    "Дизайн был старый, не обновлённый.{w=1} Год производства тоже стоял 2018."
    th "Я никогда бы не сохранил сигареты на 4 года.{w=1} Что за бред?"
    scene bg semen_room_window with byso
    "Достав одну из сигарет, он закурил и посмотрел в окно."
    "Пейзаж был непривычным. {w=1}Что-то казалось необычным, чужим."
    th "Ничего не понимаю."
    play sound3 light_inh volume 1
    "Закурив, Константин задумался."
    th "Всё-таки, где Рена?..."
    th "Мы же сбежали из инреальности.{w=1} Почему тогда мы ещё не встретились?..."
    th "А что если?..."
    th "Она пропала?"
    "Он застыл в статичной позе."
    th "Что если её существование было обусловлено только в инреальности?"
    th "Но..."
    th "Что тогда мне делать?"
    th "Мы столько прошли...{w=1} Столько всего..."
    scene bg semen_room with byso
    "Константин, не туша сигарету, уселся на кресло."
    "На нём была установлена дата и время - <<21:31, 24.12.2018>>."
    th "Я...{w=1} В прошлом?"
    "Открыв новости, Константин не поверил своим глазам."
    "В новостной ленте были новости только про события минувших лет."
    "Ими почти полностью была заполнена лента.{w=1} Это было очень странно."
    th "Я...{w=1} В прошлом..."
    th "И что мне теперь делать?"
    th "Где я теперь могу найти Рену?"
    stop music fadeout 3
    play sound3 sfx_door_bell volume 1
    "Зашумел дверной звонок."
    "Константин вздрогнул и выронил сигарету."
    th "Что?{w=1} Кто тут ко мне зайти решил?"
    "Подойдя к двери, он посмотрел в глазок."
    "Никого не было видно.{w=1} Он нахмурился и начал открывать дверь."
    th "Опять хулиганы?{w=1} Сколько можно?"
    play music "<from 177>inrealnost/Music/Music/KawuSun.mp3" volume 1 fadein 3
    play sound3 sfx_open_door_clubs_nextroom volume 1
    show image re_smile_casual with byso
    "Открыв дверь, Константин обнаружил Рену."
    play sound sfx_pat_shoulder_hard volume 1
    hide image re_smile_casual
    show image re_kind2_casual at center:
        zoom 1
        linear 1 zoom 1.25 yanchor 0.05
    "Она прыгнула ему в объятия."
    ren "Костя!"
    kt "Вот ты где!{w=1} А я уже испугался, что ты не вернёшься..."
    ren "Вернусь.{w=1} Всегда вернусь..."
    ren "Ведь теперь...{w=1} Мы вместе навсегда."
    ren "Я и ты."
    ren "Мы сможем быть счастливы!"
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound_loop fadeout 2
    scene bg black with dissolve
    pause 1
    $ renpy.block_rollback()
    play sound evil
    show text "{font=inrealnost/font/DOS.ttf}{size=300}{color=#823E80}2018{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
    with dissolve
    pause 0.55
    show text "{font=inrealnost/font/DOS.ttf}{size=300}{color=#823E80}2019{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
    pause 0.5
    show text "{font=inrealnost/font/DOS.ttf}{size=300}{color=#823E80}2020{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
    pause 0.45
    show text "{font=inrealnost/font/DOS.ttf}{size=300}{color=#823E80}2021{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
    pause 0.4
    show text "{font=inrealnost/font/DOS.ttf}{size=300}{color=#823E80}2022{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
    pause 0.35
    show text "{font=inrealnost/font/DOS.ttf}{size=300}{color=#823E80}2023{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
    pause 0.3
    show text "{font=inrealnost/font/DOS.ttf}{size=300}{color=#823E80}2024{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
    pause 0.25
    show text "{font=inrealnost/font/DOS.ttf}{size=300}{color=#823E80}2025{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
        ease 10 zoom 2
    $ renpy.block_rollback()
    stop sound fadeout 2
    pause 2
    play music deadrazy fadein 3
    scene bg int_reception with flash
    "Константин приложил телефон к уху."
    rukov "Добрый вечер, Константин Павлович."
    kt_s "Не такой добрый, если вы не могли решить проблемы самостоятельно."
    "По ту сторону провода раздалось мычание, которое длилось буквально четверть секунды."
    rukov "Простите.{w=1} Просто это не в моей компетенции..."
    kt_s "Давайте мы сейчас не будем оправдываться и уточнять рамки вашей компетенции.{w=1} Поверьте, ничем хорошим подобное исследование не закончится."
    rukov "Я понял.{w=1} Ваш соучредитель и технический директор ожидают вас в зале для совещаний."
    kt_s "Попросите у бара сделать два кофе.{w=1} Флэт уайт."
    rukov "Без проблем.{w=1} С сахаром же, верно?"
    "Константин устало потёр глаза."
    kt_s "Каждый раз я прошу у вас одного и того же.{w=1} Сложно запомнить?"
    rukov "Но это..."
    kt_s "Без сахара. Я всё сказал."
    "Он сбросил звонок."
    scene bg lift_in_open with byso
    play sound3 sfx_mystery_movement volume 1
    "Он вошёл в лифт и нажал на нужный этаж."
    play sound3 lift volume 1
    scene bg lift_in with byso
    th "Надо снова запрячь отдел кадров и найти нового руководителя для главного офиса."
    th "Этот баран словно первый день работает."
    th "Все проблемы он сваливает либо на рядовых сотрудников, либо на руководство.{w=1} Совсем тёплый."
    th "При том, на рынке есть сотни, если не тысячи людей ему на замену."
    play sound3 lift volume 1
    scene bg lift_in_open with byso
    "Двери лифта разъехались.{w=1} Константин поправил свой галстук и направился в нужный зал."
    play sound3 sfx_clench2 volume 0.51
    scene bg lift_out with byso
    "Встав у нужной двери он взялся за ручку."
    th "Ничуть не удивлюсь, если вопрос будет касаться атмосферы в офисе."
    scene bg int_ofis
    show image alvi_normal at left
    show image re_smile_frak at right
    with byso
    play sound3 door_cl volume 1
    "Войдя кабинет, он встретил Рену в её любимом бело-синем фраке и мужчину средних лет в тёмных очках и чёрном смокинге - Алексея Викторовича."
    hide image re_smile_frak
    show image re_grin_frak at right
    with byso
    ren "Привет, дорогой."
    hide image alvi_normal
    show image alvi_smile at left
    with byso
    alvi "Добрый вечер, Константин."
    kt_s "Привет, любимая.{w=1} Здравствуйте, Алексей Викторович."
    play sound3 sfx_mystery_movement volume 1
    "Пожав руку коллеге, он сел к ним за стол."
    kt_s "В чём вопрос нашей сегодняшней встречи?"
    hide image re_grin_frak
    show image re_angry_frak at right
    hide image alvi_smile
    show image alvi_normal at left
    with byso
    ren "У нас есть проблема с персоналом.{w=1} В частности с исполнительным отделом."
    alvi "Многочисленные жалобы на условия труда из ресторанных комплексов высшей ценовой категории."
    kt_s "В каком смысле?"
    "Алексей Викторович сложил руки на столе и сверкнул очками."
    alvi "Сотрудники кухни ресторанной компании возмущаются качеством поставляемых продуктов."
    kt_s "С чего бы то?{w} У нас все продукты высшего качества."
    alvi "Скорее всего дело не в этом.{w} Некорректно выразился, скорее...{w=1} видом продукции."
    "Константин тяжело вздохнул и покачал головой."
    kt_s "И как он это узнал?{w=1} Мясо сыромятиной ел?"
    hide image re_angry_frak
    show image re_grin_frak at right
    with byso
    ren "Не маловероятно.{w} Нам ещё предстоит это узнать."
    ren "Один из них просился выговориться.{w=1} Он как раз скоро должен подойти."
    kt_s "И как он добился встречи с высшим руководством?"
    ren "Скорее всего, подговорил некоторых людей на чин выше."
    hide image re_grin_frak
    show image re_madsmile_frak at right
    with byso
    ren "Надо будет разобраться с этим произволом."
    kt_s "Понятно.{w=1} Разберёмся."
    play sound3 sfx_open_door_2 volume 1
    hide image re_madsmile_frak
    show image re_grin_frak at right
    hide image alvi_normal
    show image alvi_smile at left
    with byso
    "В зал вошла официантка и вынесла два кофе со стаканами воды, а также одну бутылку боржоми."
    alvi "Спасибо, Светочка."
    "Выставив всё перед руководителями, она поклонилась и покинула помещение."
    kt_s "Тогда просто подождём этого кандидата на увольнение."
    ren "Да, это точно."
    alvi "Так понимаю, раз он опаздывает, у нас есть время на личную беседу."
    kt_s "Конечно.{w=1} Как ваш дачный участок?{w} Слышал вы планировали организовать там тропический сад."
    hide image re_grin_frak
    show image re_smile_frak at right
    with byso
    "Отпив немного кофе, Рена перевела взгляд на Алексея."
    alvi "Точно.{w=1} Я уже присмотрел кое-что, но все упирается в климат."
    alvi "Нужно больше солнца для некоторых сортов.{w} Или микроклимат надо искусственно менять, не знаю."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "Снова офис?"
    "Получилось что так."
    "Вернувшись из инреальности, Рена и Константин вполне мудро воспользовались тем, что оказались в прошлом."
    "Вложились всё в инвестиции и ставки.{w=1} Дивиденды были настолько огромными, что им хватило на платное обучение в престижном университете."
    "Алексей Викторович ранее был одним из преподавателей в новом ВУЗе Константина."
    "Поскольку он и Рена уже были знакомы с ВУЗовским материалом и знали все тонкости, им просто удалось наладить отношения с преподавателем."
    "Они закончили обучение на красный диплом и, как раз к его получению, продвинулись вверх."
    "На выручку с инвестиций они открыли собственный ресторан, основывавшийся на продвинутой китайской кухне."
    "Даже после инреальности им пришлось пройти по черепам конкурентов.{w} Может и не в буквальном смысле, но суть не изменилась."
    "Они создавали настолько невыносимую конкуренцию, что компании соперников просто уходили с рынка."
    "Карабкаясь выше и выше, они достигли уровня элит."
    "Теперь это был не просто ресторанчик в черте города, а полноценный синдикат, включающий в себя множество компаний самого разного профиля."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    play sound3 sfx_knock_door2 volume 1
    stop music fadeout 1
    hide image alvi_smile
    show image alvi_normal at left
    with byso
    "В зал постучали."
    kt_s "А вот и наш сотрудник."
    alvi "Войдите."
    play music Gallow fadein 3
    show image pova_normal with byso
    "В помещение вошёл мужчина с чёрными волосами и шрамом на брови."
    "Выглядел он весьма спокойно, но это спокойствие настораживало."
    pova "Я присяду?"
    hide image re_smile_frak
    show image re_grin_frak at right
    with byso
    "Рена отставила пустую чашку кофе."
    ren "Интересно.{w} Вы рядовой сотрудник, потому постоите."
    ren "Таковы азы нашего корпоративного этикета."
    pova "Ничего страшного, переживу без него."
    hide image re_grin_frak
    show image re_smile_frak at right
    hide image alvi_normal
    show image alvi_smile at left
    with byso
    "Руководство рассмеялось."
    kt_s "Товарищ, ты не в бар припёрся!"
    hide image re_smile_frak
    show image re_grin_frak at right
    with byso
    ren "Ты сейчас разговариваешь с людьми, которые одним щелчком пальцем могут тебя отправить на тот свет."
    play sound3 ammo volume 1
    play music kittycity fadein 3
    hide image re_grin_frak
    show image re_mad_frak at right
    hide image alvi_smile
    show image alvi_angry at left
    hide image pova_normal
    show image pova_angry
    with byso
    "Повар выхватил из под фартука пистолет с глушителем и прицелился в Константина."
    pova "Я тоже так могу."
    hide image re_mad_frak
    show image re_madsmile_frak at right
    with byso
    ren "Ух ты!{w} Какая самоотверженность.{w=1} Признаю, удивил."
    alvi "Чем занимается наша охрана..."
    "Потёр глаза Алексей и покачал головой."
    ren "И зачем ты здесь?"
    pova "Я не раз готовил это мясо, которое, по вашему входит в <<мраморный стейк из говядины>>!"
    pova "Это не говядина!{w=1} Я готовлю 10 лет и ни разу не пробовал такого мяса!"
    pova "Я отправил это мясо на экспертизу и обнаружилось, что оно ранее принадлежало человеку!"
    pova "Вы торгуете человечиной!!!"
    pova "Как вы вообще можете настолько жестоко обманывать клиентов и нарушать божьи законы?!"
    hide image alvi_angry
    show image alvi_normal at left
    with byso
    alvi "На это есть очень простое объяснение."
    kt_s "Если есть спрос, найдётся и предложение."
    "Рена улыбнулась и встала со стула.{w} Повар прицелился в неё."
    ren "Видишь ли, наши гости в таких ресторанах платят деньги только за то, что хотят получить."
    ren "Разъясню для идиотов. {w=1}Они знают, что им будет подано."
    pova "Но это же бесчеловечно!{w=1} Это ужасно!{w=1} Вы будете в аду!"
    play sound3 glass_break volume 1.4
    play sound2 krik2
    hide image pova_angry
    hide image alvi_normal
    show image alvi_angry at left
    hide image re_madsmile_frak
    show image re_madsmile_frak
    with fl_scare
    "Она взяла чашку со стола и метнула её в лицо повару." 
    play sound3 pistol3 volume 1
    pause 0.45
    play sound2 pistol3 volume 1
    pause 0.45
    play sound pistol3 volume 1
    "Чашка раскололась, повредив глаза, а повар начал стрелять не глядя."
    ren "Ада больше нет.{w=1} Бог мёртв."
    hide image alvi_angry
    show image alvi_normal at left
    with byso
    "Не пошевелив ни одной мышцей на лице, Алексей достал телефон."
    alvi "Я вызову группу зачистки."
    play sound3 sfx_punch_washstand volume 1
    play sound perelom volume 1
    "Вырвав пистолет из рук повара, Рена с ноги выбила ему коленную чашечку и прицелилась в голову."
    ren "А теперь и ты сможешь оказаться на столе у наших гостей."
    pova "Правда обязательно всплывёт!"
    ren "Как и обещала, я щёлкну пальцами."
    play sound3 pistol3 volume 1
    "Выстрел." with fl_scare
    stop music fadeout 3
    play ambience ambience_cold_wind_loop volume 0.6
    hide image re_madsmile_frak
    show image re_smile_frak at right
    with byso
    "Откинув пистолет на труп, Рена вернулась к столу и села."
    alvi "Группа будет с минуты на минуту."
    hide image re_smile_frak
    show image re_grin_frak at right
    with byso
    ren "Отлично. {w=1}Так понимаю вопрос исчерпан."
    kt_s "Алексей, передайте информацию в отдел кадров и наёмникам.{w} Нам нужно разобраться в этом деле как можно быстрее."
    hide image alvi_normal
    show image alvi_smile at left
    with byso
    alvi "Я понимаю.{w=1} Можете идти, я встречу опергруппу."
    "Встав со стульев, они пожали друг другу руки."
    hide image re_grin_frak
    show image re_smile_frak at right
    with byso
    ren "Спасибо, Алексей Викторович.{w=1} Завтра соберёмся в это же время."
    alvi "Хорошо, удачи вам."
    kt_s "Вам тоже."
    play ambience street volume 1 fadein 1
    scene bg street1 with fade
    play music summerdays fadein 3
    "Константин стоял на улице рядом со своим автомобилем и, глядя на здание своего офиса, думал о будущем."
    th "М-да, надо запретить сотрудникам лезть не в своё дело."
    th "Не будь там Рены, ситуация могла бы закончиться печально."
    th "А ещё надо найти всех людей, которые были с ним в сговоре."
    th "Может быть усилить контроль за камерами на наших предприятиях?"
    th "Кстати да, наиболее оптимальный вариант."
    show image re_calm_winter with byso
    "Из здания вышла Рена."
    kt_s "А вот и ты.{w=1} Я уж заждался."
    hide image re_calm_winter
    show image re_smile_winter
    with byso
    ren "Да, задержалась немного.{w=1} Оставила нашей официантке на чай."
    ren "На всякий случай, мало ли что слышала."
    "Двери автомобиля автоматически открылись."
    kt_s "Прошу."
    hide image re_smile_winter
    show image re_grin_winter
    with byso
    ren "Спасибо."
    play sound3 car_door volume 1
    stop ambience fadeout 1
    scene bg limuz
    show image re_grin_winter
    with byso
    "Усевшись на задних сидениях, они тесно прижались друг к другу."
    vodi "Здравствуйте.{w=1} Куда вас отвезти?"
    kt_s "Везите домой пожалуйста."
    vodi "Хорошо."
    play ambience bus_inside volume 0.2 fadein 1
    "Машина поехала."
    "Автомобиль, в котором они ехали был вполне современного вида, но сильно переделанный: пуленепробиваемые стёкла, бронированные боковые стенки, стабилизирующая подвеска."
    "Писк моды в области безопасности."
    hide image re_grin_winter
    show image re_smile_winter
    with byso
    ren "Вы забрали Персефону с курсов?"
    vodi "Конечно, можете не беспокоиться."
    vodi "Правда её наставник передавал, что она довела до слёз несколько учеников."
    hide image re_smile_winter
    show image re_happy_winter
    with byso
    kt_s "Ха, узнаю нашу девочку."
    ren "Вся в меня."
    vodi "Мы будем на месте назначения через 5 минут. {w=1}Дорога свободна."
    hide image re_happy_winter
    show image re_calm_winter
    with byso
    ren "Отлично."
    play sound3 sfx_open_drapes volume 1
    "Водитель закрыл окошко между пассажирскими и водительскими сидениями и сконцентрировался на дороге."
    "Рена положила голову на плечо Константина и они, молча глядя в окно, наслаждались поездкой."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "У Рены и Константина была одна дочь.{w} Персефона."
    "Несмотря на то, что ей было всего 6 лет, она уже освоила материал восьми школьных классов."
    "Она отличалась острым умом и невероятным интеллектом."
    "Уже в возрасте года она уже умела читать вслух и произносить осмысленные сложные предложения."
    "В два года она уже научилась корректно анализировать и усваивать информацию."
    "Врачи никак не могли объяснить настолько быстрое развитие интеллекта у ребёнка и называли её настоящим вундеркиндом."
    "Рена и Константин же колебались между двумя вариантами."
    "Либо это идеальная генетика, которую получила Рена в инреальности, либо это переход из инреальности так на это повлиял."
    "Тем не менее, Рена и Константин были рады, что их ребёнок вдвое превосходит даже тех, кто на 6, а то и на 10 лет старше."
    "Персефона любила своих родителей, а её родители любили её."
    "Кроме неё, у них не было детей, но Рене и Константину хотелось, чтобы Перси имела счастливую и полноценную жизнь."
    "Чтобы она не повторила судьбу Константина."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    stop ambience fadeout 1
    play sound3 sfx_open_drapes volume 1
    hide image re_calm_winter
    show image re_smile_winter
    with byso
    "Автомобиль плавно затормозил и двери открылись. Водитель отрыл окошко."
    vodi "Мы приехали."
    kt_s "Отлично. {w=1}Завтра примерно в два часа мне потребуется автомобиль."
    vodi "Без проблем.{w=1} Всего доброго."
    scene bg black with byso
    stop music fadeout 1
    pause 1
    scene bg apart_int
    show image re_smile_winter at cleft
    show image pers_normal at cright
    with byso
    play music regret fadein 3
    play sound3 door_cl volume 1
    "Открыв дверь своих апартаментов, они встретили Персефону, которая сидела у окна и читала <<Антихрист>> Фредериха Ницше."
    "Заехали они сюда не так давно - предстояло ещё многое изменить в интерьере, но всё необходимое уже было по комнатам."
    hide image re_smile_winter
    show image re_happy_winter at cleft
    with byso
    ren "Мы дома, доча."
    kt_s "Привет, Перси."
    hide image pers_normal
    show image pers_happy at cright
    with byso
    pers_c "Мама!{w=1} Папа!"
    hide image pers_happy
    show image pers_happy
    with byso
    "Подбежав к родителям, она обняла Константина и Рену."
    pers_c "Вас так долго не было.{w=1} Я заскучала!"
    hide image re_happy_winter
    show image re_calm_winter at cleft
    with byso
    "Рена погладила дочь по голове улыбнулась."
    ren "Были дела."
    kt_s "На выходных мы обязательно сходим в тир, как ты и хотела."
    pers_c "Правда?{w=1} Ура!"
    kt_s "Так, а теперь дай папе с мамой переодеться."
    pers_c "Хорошо."
    hide image pers_happy
    hide image re_calm_winter
    show image re_calm_winter
    with byso
    "Перси побежала в гостиную."
    hide image re_calm_winter
    show image re_grin_winter
    with byso
    ren "Что приготовить на ужин?"
    pers_c "Давай шаверму!"
    kt_s "Думаю соглашусь.{w=1} Как раз вчера пекли лаваш."
    hide image re_grin_winter
    show image re_smile_winter
    with byso
    ren "Отлично. {w=1}Без проблем."
    hide image re_smile_winter with byso
    play sound3 sfx_paper_bag volume 1
    show image re_photo with byso
    "Рена ушла в комнату, а Константин достал из кармана фотографию."
    "На ней была изображена Рена в свадебном платье."
    th "Да, завтра же годовщина."
    th "Надеюсь вопрос на работе не затянется.{w=1} Не хотелось бы портить такой день."
    th "Только подумать, шестая годовщина...{w=1} Как время быстро пошло..."
    th "Кажется что это было не так давно...{w=1} Буквально неделю назад."
    th "И вот уже шестой год."
    th "Сколько всего пережито, а сколько еще предстоит пережить."
    th "Но это все уже там, в темноте, за дверью."
    th "Здесь же ты видишь жизнь."
    th "Насыщенную, яркую, живую.{w=1} Вижу здесь и сейчас."
    scene bg apart_kitchen
    show image pers_happy at cleft
    show image re_smile_home at cright
    with fade
    pers_c "Спасибо!{w=1} Очень вкусно."
    "Рена разлила по чашкам ароматный цейлонский чай с бергамотом и поставила их Персефоне и Константину."
    kt_s "Спасибо, дорогая."
    "Константин улыбнулся и повернулся к дочери."
    kt_s "Как твой день прошёл?"
    hide image pers_happy
    show image pers_angry at cleft
    with byso
    "Персефона сложила руки на груди и нахмурилась."
    pers_c "Вроде на этих курсах все такие взрослые, умные."
    pers_c "А на деле дураки!"
    pers_c "Меня ещё и Даша отчитывала, что я довела несколько девочек до слёз."
    pers_c "Сказала, что я их обзывала.{w} Она врёт."
    pers_c "Это голые факты.{w=1} То, что девочка ходит на курсы по неорганической химии и в 16 лет не может решить простейшую цепочку реакций значит лишь одно."
    pers_c "Как говорится, средства у нас есть, а ума не хватает..."
    hide image re_smile_home
    show image re_mad_home at cright
    with byso
    ren "Даша твой наставник?"
    pers_c "Ага..."
    ren "Я с ней побеседую завтра."
    play sound3 glad volume 1
    hide image re_mad_home
    show image re_smile_home at cright
    hide image pers_angry
    show image pers_normal at cleft
    with byso
    "Константин погладил дочь по голове."
    kt_s "Жизнь такая штука.{w=1} Ещё не раз тебе придётся встречаться с такими людьми."
    kt_s "Тебе надо понимать простое выражение.{w} Даже несколько секунд твоего времени не стоят их целой жизни."
    hide image re_smile_home
    show image re_grin_home at cright
    with byso
    ren "Именно.{w=1} Ты самая умная девочка.{w} Уделяя таким людям внимание, ты лишь опускаешься до их уровня."
    ren "Мы тебя ни в коем случае не обвиняем.{w=1} Приходится иногда ставить такой сброд на место, но просто делать это серийно не имеет смысла."
    ren "А с твоей наставницей я разберусь.{w} Поедем на курсы вместе."
    kt_s "Так сказать, покажешь как это делается."
    hide image pers_normal 
    show image pers_happy at cleft
    with byso
    "Перси и Рена рассмеялись, а Константин отпил ароматного чаю и закусил лимоном."
    pers_c "Хорошо!{w=1} Только не задерживайтесь завтра на работе. Я пойду спать."
    kt_s "Мы очень постараемся.{w=1} Спокойной ночи."
    hide image re_grin_home
    show image re_smile_home
    with byso
    "Рена поцеловала дочь в лоб."
    ren "Сладких снов."
    pers_c "Споки!"
    hide image pers_happy with byso
    "Пожелала Персефона и убежала в свою комнату."
    "Константин опустошил свою чашку и собрал посуду со стола."
    kt_s "Ладно, давай и мы пойдём спать.{w=1} Завтра годовщина как никак."
    hide image re_smile_home
    show image re_grin_home
    with byso
    ren "Конечно."
    stop music fadeout 3
    scene bg black with byso
    pause 2
    play music ElfenLied fadein 3
    scene bg re_int2 with byso
    play sound3 sfx_blanket_off2 volume 1
    "Развалившись на кровати, Константин посмотрел в потолок, а Рена легла рядом и провела рукой по груди Константина."
    ren "Знаешь, недавно думала..."
    "Константин повернул голову к Рене и улыбнулся."
    kt_s "И о чём же?"
    ren "Мы достигли вершины."
    ren "У нас есть всё, о чём мы только могли подумать в самых смелых мечтах."
    ren "Семья, чуть ли не бесконечное влияние, собственный пентхаус, корпорация, которая монополизировала половину всех сфер рынка."
    ren "А ещё одно большое счастье ждёт нас впереди..."
    ren "Долгая и счастливая жизнь, полное удовлетворение желаний и всё-всё-всё."
    ren "На крови и костях мы построили счастливую жизнь, полную любви и мечтаний."
    ren "О такой жизни мы мечтали, верно, Костя?"
    ren "И будем теперь долго и с радостью глядеть, как она уходит прочь, пока от неё не останется один только последний снежный вихрь..."
    "Рена нежно повела рукой вниз по телу Константина."
    scene bg black with Dissolve(3)
    pause 1
    $ unlock_ach_root_inreal(8)
    scene bg ending_BuiltOnBlood_cg:
        crop (940, 450, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    show ending_BuiltOnBlood:
        crop (940, 450, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    with Dissolve(25)
    scene bg black with byso
    stop music fadeout 3
    pause 2.6
    jump after_ending_screen
label MankindIsDead_ending:
    "Генда поднял руку, в которой начала собираться синяя плазма."
    gg "Ты мне больше не нужен."
    play sound magic volume 1
    stop music
    show image blood3 with fl_scare
    play sound3 sfx_bones_breaking volume 1
    "В грудь Константина попала едкая плазма, словно кислота разъедая его внутренние органы."
    scene bg zvezda_red with byso
    "Генда испарился."
    play music TheSecondDeath fadein 3
    ren "Костя!!!"
    play sound2 sfx_bodyfall_1 volume 1
    "Тело Константина развалилось на две части на уровне диафрагмы."
    "Ноги пару раз дёрнулись, после чего замерли, заливаясь кровью."
    "Боль сковала движения.{w=1} Константин просто не мог пошевелиться и лишь смотрел на звёзды в багряном небе."
    "Звёзд было очень много, но далеко.{w} Где-то там, за пределами охваченной болезнью реальности, бился в агонии страдающий мир."
    "Рена выронила кинжал и побежала спасать Константина."
    ren "Нет! Нет! Нет!!!"
    ren "Не закрывай глаза, прошу тебя!"
    ren "Любимый! Дорогой!"
    kt "Прости...{w=1} меня..."
    kt "Это конец..."
    ren "Я помогу!"
    play sound3 sfx_blanket_off2 volume 1
    "Рена в паническом шоке пыталась перевязать рану Константина, но, естественно, это было невозможно."
    kt "Покажи...{w=1} миру...{w=1} На что ты...{w=1} способна..."
    ren "Костя!{w=1} Не надо!"
    show blink
    "Константин закрыл глаза.{w=1} Плазма попала в кровь и разъела содержимое черепной коробки."
    window hide dissolve
    $ renpy.block_rollback()
    pause 1
    stop sound_loop
    $ volume(0, "music")
    stop ambience fadeout 3
    play sound2 "<from 1.5>inrealnost/Music/Sound/bad_ending.mp3"
    scene bg ending_dead_cg:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    show ending_dead:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 15 crop (0, 0, 1920, 1080)
    with Dissolve(7)
    $ renpy.pause(1, hard=True)
    stop sound2
    $ renpy.block_rollback()
    play sound Glitch4
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(3, hard=True)
    stop sound
    scene bg black
    $ renpy.pause(1, hard=True)
    $ volume(1, "music")
    play ambience ambience_forest_night volume 1 fadein 1
    scene bg zvezda_red
    show image re_stunned
    with byso
    "Рена не могла поверить своим глазам."
    "На её руках лежал мёртвый Константин, чью плоть разъедала плазма."
    "И вот его тело окончательно рассыпалось. Не осталось ничего, даже волос."
    ren "К-Костя...{w=1} Я...{w=1} Не помогла..."
    ren "Я в этом виновата..."
    ren "Не уследила, не помогла в нужный момент..."
    stop music fadeout 3
    me "Слышь ты!{w=1} Нас тут убивают, а ты нюни раздуваешь!{w=1} А ну в бой!!!"
    play music WSWW volume 0.8 fadein 3
    scene bg int_fire with byso
    "Пустым взглядом Рена начала водить взглядом, выискивая говорящего."
    "Вдруг, в её голове что-то перемкнуло."
    eth "Я тебя найду и выпотрошу, кусок гадкого дерьма..."
    "Мысли встали на второй план, а топор сам появился в руке."
    eth "Расчленю!{w=1} Растерзаю!{w=1} Уничтожу!{w=1} Выпотрошу!"
    "Горе потери сменилось невыносимой жаждой крови, дикой и слепой."
    "Бешеная волна кровавого инстинкта подняла её на ноги."
    eth "Всех вас, гадкие лжецы!"
    "Тело задрожало, словно от сильного холода, но остановиться она уже не могла."
    ren "Нет вам места на этой дерьмовой земле!"
    play sound3 sfx_armature_swish volume 1
    show image me_st with byso
    "Она раскрутила топор в руке и набросилась на первую попавшуюся сущность."
    chel "Берегись!{w=1} Она сошла с ума!"
    play sound3 head_crush2 volume 1
    scene bg bloody_mess with fl_scare
    "Ей было плевать, кого она убьёт - монстра, Генду, повстанца, беременную женщину или ребёнка."
    ren "Я вас всех казню!!!"
    play sound head_crush3 volume 1
    "Всё, что ей было нужно - это кровь и смерть."
    chel3 "Помогите!"
    play sound3 slash volume 1
    "Кровь и Смерть."
    "И хотелось прямо сейчас.{w=1} Прямо сейчас."
    idol "Братья! Отступайте."
    play sound head_crush2 volume 1
    "Увидеть их разодранные в клочья тела и впитать эту новую для себя энергию."
    play sound3 tesak volume 1
    "Сущности падали одна за другой, и падение каждой из них становилось последним движением."
    "Оно становилось неостановимым.{w=1} Обрывки разрозненных мыслей, приходившие ей в голову в процессе боя, постепенно сливались в одну общую карусель, где не оставалось ничего, кроме расплывающейся в вязкой черноте багряной точки."
    chel2 "Нет! Пощади!"
    play sound3 head_crush4 volume 1
    "Разрубая тела одно за другим, она хотела почувствовать, что ней становится легче, но уже было поздно. Совсем поздно..."
    "Мозг перестал подавать какие-либо сигналы."
    idol "Да простит меня бог!"
    play sound3 head_crush3 volume 1
    "Вся кровавая баня происходила на полном автомате, как это обычно бывало в промышленной мясорубке."
    "Трупы.{w=1} Трупы.{w=1} Трупы.{w=1} Кругом были трупы."
    play sound_loop Glitch_loop volume 1
    show Glitch_screen3:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    pause 0.5
    stop sound_loop
    scene bg ext_square_night_blood
    play sound3 slash volume 1
    "Последняя гончая проскулила и распрощалась со своей головой."
    ren "Где?!"
    ren "Где ебучие порталы?!"
    gg "А я тебе отвечу..."
    scene bg genda with byso
    "В небе появился Генда."
    ren "Ты!"
    gg "Всё механизмы автокорреции направлены на эту симуляцию."
    gg "И ты просто не сможешь её снизить.{w=1} Никогда и никак."
    ren "Я тебя прихлопну!"
    ren "Уничтожу всё что тебе дорого и заставлю тебя на это смотреть!"
    ren "Я станцую на костях твоих близких!{w=1} Даже если я умру, то мне плевать!"
    "Генда хмыкнул и рассмеялся."
    gg "Этому не суждено произойти.{w=1} Ты теперь моя собственность."
    play sound3 magic volume 1
    "Он запустил в Рену заряд красной плазмы, но та увернулась."
    gg "Мне нужны пустышки с такой же силой как у тебя."
    play sound3 pistol volume 1
    pause 0.4
    play sound pistol volume 1
    pause 0.4
    play sound2 pistol volume 1
    "Рена схватило первое попавшееся оружие и несколько раз выстрелила."
    "Пули прошли насквозь."
    ren "Я из тебя фарш сделаю и пионерам на обед подам!"
    play sound3 magic volume 1
    "Она увернулась от очередного заряда."
    gg "Скажи это Константину, которого я распылил."
    ren "Не смей о нём ничего!...{w=0.3}{nw}"
    play sound3 magic volume 1
    stop music
    scene bg black with vpunch
    pause 0.5
    play music unskyidy2 fadein 3
    scene bg zvezda_red
    show unblink
    "Попадание."
    show image so_sm with dissolve
    "Рену парализовало, а Генда спустился на землю и цокнул языком."
    gg "Есть такое выражение."
    gg "Флот плывёт со скоростью самого медленного корабля."
    gg "В этой картине ты была современным эсминцем, который мог развивать скорость до 38 узлов."
    gg "А он - старое ржавое корыто, которое и один еле наберёт."
    gg "Признаю, у меня слабость на длительные демагогии.{w=1} Надо это заканчивать."
    ren "И что?!{w=1} Убьёшь меня теперь?!"
    gg "Нет-нет...{w=1} Ты теперь будешь моей испытуемой вместо Константина."
    gg "Мне нужны такие люди как ты.{w=1} Только такое сознание как у тебя мне не нужно."
    "Он протянул руку в сторону Рены."
    gg "Я исправлю этот недуг."
    play sound3 magic volume 1
    stop music fadeout 1
    scene bg black with vpunch
    stop ambience fadeout 1
    pause 2
    window hide
    play sound3 Glitch3 volume 1
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 0.1
    play music Radar fadein 3
    show image re_crusifix
    show re_crusifix_shum_a
    show image monitor_adm
    with dissolve
    pause 1
    ik_sh "Папа, зачем тебе эта рыжая девчонка?"
    gg "Для нашего будущего."
    gg "Помнишь 13й параграф теории симуляций?"
    ik_sh "Пустышки не способны давать отпор агрессивным путникам?"
    gg "Верно.{w=1} Я хочу исправить этот параграф."
    gg "В таком случае получится обезопасить инреальность от постоянных перескоков и насильного понижения стабильности."
    ik_sh "А почему нельзя просто увеличить число симуляций или просто нейтрализовать уязвимость с порталами?"
    gg "При нынешней кодировке инреальности это невозможно.{w=1} Потребуется целиком отключить инреальность, перекодировать её и только тогда нейтрализовать эту уязвимость."
    gg "Я не смогу это сделать, поскольку все мы живём в нашей симуляции."
    gg "Именно при твоём правлении тебе предстоит это исправить под моим чутким контролем."
    gg "Всё, Широ.{w=1} Иди."
    gg "Через неделю или раньше я приведу эту оторву спокойной и покорной."
    ik_sh "Хорошо, папа.{w=1} Удачи тебе."
    window hide
    play sound3 Glitch3a volume 1
    show Glitch_screen3:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 1
    scene bg kt_room
    show unblink
    play music tish fadein 3
    "Рена очнулась в квартире Константина."
    "Всё было прямо как в тот день: дверь выбита, три гильзы, а на полу сигарета, которая оставила след на ковре."
    kt "Рена, ты слышишь меня?!"
    ren "Что?!{w=1} Костя?!"
    ren "Где ты?!"
    kt "Срочно, Рена, мне нужно узнать кое-что!{w=1} Как управлять пустышками?!"
    th "Это...{w=1} не Костя..."
    th "Ему не понадобилась эта информация ни в коем случае."
    ren "Ты не Костя!{w=1} Это ложь!"
    kt "Нет, это я, Рена!"
    kt "Верь мне, мы сможем выбраться!"
    "Она тяжело вздохнула и села на стул."
    ren "Тогда скажи мне, что я хотела сделать, чтоб выбраться из кошмара?"
    kt "Не помню!{w=1} У нас времени для этих проверок."
    ren "Настоящий Константин так бы не сказал.{w} Хуёвая попытка выпытывать из меня информацию, давя на больное."
    ren "Я просто напомню, что раскрашу стены содержимым твоей черепной коробки.{w=1} Вопрос времени."
    gg "Очень смешно."
    show image so_sm with byso
    "Перед ней образовался Генда."
    ren "Да-а, я уже представляю, как твоя убогая рожа будет смотреться размазанной по стене..."
    ren "Мотивирует не сдаваться, знаешь ли."
    gg "Ты не понимаешь в какой ситуации находишься."
    gg "Я могу пытать тебя вечно.{w=1} В буквальном смысле."
    "Рена ухмыльнулась и незаметно подобрала карандаш со стола."
    ren "Я не чувствую боли.{w=1} Теперь."
    ren "Ты можешь меня пытать любыми способами, но я тебе никогда ничего не скажу."
    hide image so_sm
    show image so_gd
    with byso
    gg "Тогда я просто влезу в твою голову и сам найду там нужную информацию."
    "Она рассмеялась и, встав, посмотрела Генде на мочку уха."
    ren "Расскажи на милость, тогда почему ты этого не сделал сразу?"
    ren "Ты прибегаешь к попыткам вывести из меня информацию, а это значит ты просто блефуешь, старый урод!"
    "Генда разозлился.{w=1} У него задёргалось веко."
    gg "Я выбью из тебя информацию."
    ren "Что такое?{w=1} Не можешь передать трон своему уродливому сынишке, да?"
    ren "Обидно наверное.{w=1} Особенно если он будет настолько же бездарно править как и ты."
    ren "Наверняка правило <<яблоко от яблони>> и тут сработает!"
    "Прорычав, Генда попытался ударить Рену."
    play sound perelom
    scene bg re_torture with fl_scare
    "Она вонзила карандаш со стола ему в руку.{w=1} Генда застонал от боли, которая наверняка была для него новшеством."
    gg "Ах ты тварь!"
    "Карандаш спустя секунду упал на пол, а она снова безумно улыбнулась."
    ren "Вот оно что. Материализация ударяющей части тела перед самим ударом?"
    ren "Возьму этот приём на вооружение."
    gg "Ты доигралась!"
    play sound3 schelk volume 1
    stop music fadeout 1
    show blink
    "По щелчку пальцев Рена потеряла сознание."
    window hide
    play sound Glitch3 volume 1
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 0.1
    show image re_crusifix
    show re_crusifix_shum_a
    show image monitor_adm
    with dissolve
    play music Radar fadein 3
    ik_sh "Папа, что у тебя с рукой?"
    gg "Ничего такого.{w=1} Просто случайно поранился."
    ik_sh "Похоже на сквозное пробитие.{w=1} Ты мне врёшь, отец?"
    gg "Нет, Широ.{w} В будущем я буду аккуратнее."
    ik_sh "Хорошо, а что с ней?"
    gg "Работаю.{w} Думаю, мне удастся её расколоть."
    ik_sh "Я могу помочь."
    gg "Нет, Широ, рановато тебе списывать меня со счетов."
    ik_sh "Но папа!"
    gg "Нет сын!{w} Она слишком опасный субъект!"
    gg "Я не хочу чтобы мой наследник умер от рук безумного порождения инреальности!"
    ik_sh "Почему ты её называешь настолько опасной?{w=1} Это же просто обычная девчонка."
    gg "Широ, это венок человеческой эволюции.{w} Тот самый пик развития."
    gg "Её характеристики в насколько раз превосходят человеческие, хотя она выглядят весьма просто."
    gg "Она способна голыми руками разломать тазобедренную кость!{w} Её сила и интеллект ещё и будут увеличиваться по следующим поколениям, чего допустить нельзя."
    gg "Если мы сможем вывести таких пустышек, то это будет величайший прорыв за ближайшую тысячу временных квадрантов."
    gg "Ещё спасибо скажешь."
    ik_sh "Но может мы будем проводить это исследование вместе?{w=1} Я многому смогу научиться и помогу тебе."
    gg "У меня есть ещё одна идея...{w=1} Но если она не сработает, то хорошо.{w=1} Будем работать вдвоём."
    ik_sh "Спасибо что доверяешь мне, отец."
    stop music
    window hide
    play sound3 Glitch3a volume 1
    show Glitch_screen3:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 1
    play music the_date_of_death fadein 3
    scene bg cafe
    show unblink
    "Рена проснулась в банкетном зале."
    th "Снова?"
    play sound card_mix volume 1
    show image so_gd with byso
    "Встав на ноги, она заметила Генду, который тасовал колоду карт."
    "Одна из его рук была перевязана бинтом.{w=1} Рена непроизвольно улыбнулась."
    ren "М-м-м... {w=1}Что на этот раз придумал?"
    gg "Я ничего не придумал.{w} Я предлагаю тебе сделку."
    ren "Сделку?{w=1} От тебя?"
    ren "Кроме твоей смерти мне от тебя ничего не надо."
    "Генда положил на стол карты и перевёл взгляд на Рену."
    gg "Ты мне рассказываешь как управлять пустышками и тогда я высвобождаю Константина."
    ren "Что?..."
    gg "Видишь ли, у меня хранятся все умершие в инреальности души."
    gg "На случай, если они мне нужны, я их сохраняю, благо места на накопителях хватает на содержание душ с начала нашей эры."
    gg "И если ты согласишься сотрудничать, то я могу возродить Константина."
    "Рена задумалась."
    th "Я не знаю ничего про то, что он хочет услышать.{w} Минерва умерла, так этого и не рассказав..."
    th "Да даже если бы и знала, то не обманывает ли он меня?"
    ren "Как я могу убедиться в том, что ты на это способен?"
    hide image so_gd
    show image so_sm
    with byso
    gg "Просто.{w=1} Назови любого, кого тебе угодно и я возрожу его."
    ren "Максим Федоренко.{w} Показывай."
    gg "Момент."
    play sound teleport
    hide image so_sm with fl_fast
    play sound3 sfx_mystery_movement volume 1
    "Генда растворился, а Рена села на стол."
    th "Он что, правда на это способен?"
    th "Правда есть велика вероятность, что он захочет меня обмануть."
    th "Но если он и в правду сейчас притащит сюда Максима, то..."
    th "То что?"
    th "Я ничего не знаю..."
    th "Боже, Костя, если ты меня видишь, то прости меня..."
    th "Столько времени прошло...{w=1} А я даже не выбралась из его заключения..."
    th "Стоп..."
    th "Да я же могу захватить инреальность и возродить Костю!"
    th "И мы снова сможем жить счастливо!"
    "На лице Рены поплыла безумная улыбка."
    th "Осталось лишь только завладеть инреальностью!{w=1} И мы снова с тобой увидимся!"
    th "Я сделаю это! {w=1}Ради тебя!{w=1} Ради тебя любимого!"
    show image so_sm at fright
    show image me_no
    with byso
    "В помещение вернулся Генда, а с ним какой-то Семён."
    scene bg cafe
    show image so_gd at fright
    show image me_no
    with byso
    "Рена не удержалась и рассмеялась."
    ren "И ты серьёзно думал, что я в это поверю?!"
    ren "Цирк уродов!"
    hide image so_gd
    show image so_sm at fright
    with byso
    gg "Ты можешь спросить всё что он знал и он тебе ответит."
    ren "М-м-м, хорошо."
    hide image me_no
    show image me_su at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Она подошла к Семёну, отчего тот занервничал."
    ren "Тогда расскажи мне.{w=1} Как назывался ресторан, в который ты ходил с Костей?"
    me "Фей-фань."
    th "Хорошо, это знает..."
    ren "При каких отношениях вы разошлись с Константином?"
    me "Мы поссорились. Так и не понял, был ли я на тот момент прав."
    th "Первая нестыковка.{w=1} Настоящему Максиму было плевать."
    play sound3 sfx_pat_shoulder_hard volume 1
    hide image so_sm
    show image so_gd at fright
    with byso
    "Рена ухмыльнулась и положила руку Лжемаксу на плечо."
    ren "Хорошо, тогда последний вопрос."
    ren "Как я назвала тот фокус с головой Лены?"
    "Парень замешкался.{w=1} Он явно не знал, что ответить."
    hide image me_su
    show image me_st at center:
        zoom 1.25
        yanchor 0.05
    with byso
    ren "Какой же ты старый гадкий лжец!"
    play sound perelom volume 1
    play sound3 sfx_bush_body_fall volume 1
    hide image me_st with fl_scare
    "Она двумя руками взяла голову Семёна и свернула ему шею, после чего, прокрутив голову на 360, бросила тело на пол."
    "Секунду оно оставалось неподвижным, потом зашевелило головой."
    play sound3 head_crush4 volume 1
    "Рена добила его, раздавив череп.{w} Голова превратилось в месиво из крови, мозга и осколков черепа." with vpunch
    ren "Ты хотел меня обмануть, подсунув мне пустышку.{w=1} Так я и знала."
    ren "Обмануть ты меня не сможешь.{w=1} Я предвижу каждую твою ложь."
    stop music fadeout 1
    play sound3 schelk volume 1
    show blink
    "Генда щёлкнул пальцами."
    window hide
    play sound Glitch3 volume 1
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 1
    show image re_crusifix
    show re_crusifix_shum_a
    show image monitor_adm
    with dissolve
    play music Radar fadein 3
    ik_sh "Не вышло?"
    gg "Нет. {w}Она понимает, что у меня на самом деле нет информации про действия путников на территории инреальности."
    ik_sh "А что если она просто ничего не знает?"
    gg "Исключено.{w=1} У неё точно есть информация."
    ik_sh "Может выслушаешь мою идею?"
    gg "Хорошо, Широ, рассказывай."
    ik_sh "А что если мы просто обратим её в пустышку?"
    ik_sh "Мы можем переписать ей память как и любому путнику, попадающему в инреальность, не затрагивая физические характеристики.{w=1} Сделаем двойной акцент на памяти."
    ik_sh "После мы оставим в симуляции на один-два цикла и после провести на ней все требуемые исследования."
    ik_sh "При попадании она забудет всё про то, что было с её парнем и память полностью перепишется."
    gg "Это опасно."
    ik_sh "А у нас есть выбор?"
    ik_sh "Прости меня, отец, но ты буквально недавно чуть не обрушил инреальность."
    ik_sh "После заточения этой рыжей стабильность инреальности составляла всего 5 процентов."
    ik_sh "Это неоспоримый факт.{w=1} Хорошо что об этом не знает остальная семья."
    ik_sh "За всё время она уничтожила только около 50 симуляций. {w}Она не сможет добиться большего результата без сопротивления."
    ik_sh "В той войне 79 процентов симуляций пали именно по вине сопротивления.{w=1} Если мы обнаружим девиацию, то сможем быстро её предотвратить."
    gg "Да, ты прав."
    gg "Я рад, что у инреальности будет такой мудрый наследник."
    gg "Тогда мы её исключаем из административного подпространства и отправляем в симуляцию."
    ik_sh "Только не в 22-25а.{w=1} Там она может вернуть себе память."
    ik_sh "И не с переходом в административную симуляцию."
    ik_sh "Не хотелось бы, чтоб она попала в наш дом."
    gg "22-25а уничтожена на уровне первичной структуры.{w} Она теперь навсегда часть кошмара."
    gg "Да и к нам домой можем попасть только мы.{w=1} Без нашего желания никто другой там не окажется."
    gg "Прогоню её через первый освободившийся алгоритм."
    gg "Посмотрим что из этого выйдет."
    $ renpy.block_rollback()
    window hide
    stop music fadeout 1
    stop sound_loop fadeout 1
    play sound delete volume 2
    $ renpy.pause(0.75, hard=True)
    show Glitch_screen3:
        size (1920, 1080)
    $ renpy.pause(0.25, hard=True)
    scene bg black with dissolve
    $ renpy.pause(1, hard=True)
    window show dissolve
    $ renpy.pause(1, hard=True)
    $ renpy.block_rollback()
    play music music_list["drown"] fadein 3
    scene bg white
    show unblink
    "В глаза ударил яркий свет."
    uth "Что?...{w=1} Где я?"
    scene bg int_bus with byso
    play ambience ambience_camp_center_day volume 0.41 fadein 1
    "████ осмотрелась.{w=1} По какой-то причине сильно болела нижняя часть живота."
    "Автобус марки <<Икарус>>.{w=1} Иконка у водительского места.{w=1} Отсутствие руля и педалей."
    uth "Кто я?..."
    uth "Ничего не помню..."
    "Встав с места ████ пошатнулась. {w=1}Было чувство как с лёгкого похмелья."
    uth "Почему на улице лето?"
    uth "Ничего не понимаю..."
    "████ подошла к зеркалу заднего вида и посмотрела в него."
    uth "Вот так я выгляжу? Не плохо..."
    play sound3 in_vosp volume 1
    $ volume(0, "music")
    play sound_loop OMORI
    stop ambience fadeout 1
    scene bg int_house_of_kt_day
    show shum_red
    with fl_scare
    renu "Да ладно тебе, я не голая."
    ktu "Не хочу портить сюрприз."
    renu "Хе, как знаешь."
    renu "Готово.{w=1} Можешь смотреть."
    ktu "А тебе идёт!"
    renu "Мне не очень этот наряд нравится, но раз тебе нравится, я буду его носить."
    play sound3 out_vosp volume 1
    stop sound_loop
    $ volume(1, "music")
    scene bg int_bus with fl_scare
    play ambience ambience_camp_center_day volume 0.41 fadein 1
    uth "Рыжие короткие волосы, голубые глаза и белый беретик, плотно прилегающий к голове..."
    "Отойдя от зеркала, ████ начала спускаться из автобуса."
    scene bg ext_camp_entrance_day with byso
    play ambience ambience_camp_center_day volume 1 fadein 1
    "Она посмотрела на вывеску."
    th "Совёнок-совёнок...{w=1} Что-то знакомое...{w} Словно я тут уже была.{w} И не раз..."
    play sound2 vosp volume 1
    $ volume(0, "music")
    show bg ext_camp_entrance_night_red
    show shum_red
    with fl_scare
    $ volume(1, "music")
    scene bg ext_camp_entrance_day
    with fl_scare
    stop music fadeout 3
    "В голове едва-заметно кольнуло."
    uth "Место, что знакомо мне давно.{w} Наверное..."
    uth "Мне бы сначала вспомнить своё имя..."
    play music music_list["forest_maiden"] fadein 3
    show sl normal pioneer far with byso
    "Из-за ворот лагеря показалась светловолосая пионерка."
    "По какой-то причине она не симпатизировала ████ одним своим видом."
    hide sl
    show sl smile pioneer
    with byso
    "Подойдя к ████ пионерка улыбнулась."
    slp "Привет, ты наверное Регина?"
    uth "Регина?{w=1} Да, меня так зовут."
    renr "Да, привет, это я."
    show sl smile2 pioneer with byso
    "Девочка взяла в руки свою косу и начала её расчёсывать."
    renr "Слушай, скажи мне..."
    show sl happy pioneer with byso
    slp "Приятно познакомиться.{w=1} Меня зовут Славя, я помощница вожатой."
    sl "Давай я тебя провожу до неё."
    "Регина поводила взглядом по земле и вернулась к Славе."
    renr "Нет, спасибо, я сама дойду.{w} Хочу немного осмотреться."
    show sl smile pioneer with byso
    sl "Хорошо. {w=1}Тогда до встречи."
    renr "Угу."
    stop music fadeout 3
    hide sl with byso
    "Славя скрылась за воротами лагеря, а Регина засмотрелась на вывеску."
    uth "Чёрт...{w=1} Какой-то пионерский лагерь..."
    uth "В целом, ничего плохого же не случится от того, что я туда зайду?"
    uth "Ничего."
    play music music_list["two_glasses_of_melancholy"] fadein 3
    "Пожав плечами, Регина пошла вглубь лагеря."
    scene bg ext_clubs_day with byso
    "Сразу у входа её встретило здание с названием <<Клубы>>."
    uth "И это тоже знакомо."
    play sound3 in_vosp volume 1
    $ volume(0, "music")
    play sound_loop OMORI
    stop ambience
    scene bg ext_clubs_day
    show shum_red
    with fl_scare
    "████ схватила ████ за галстук и притянула с силой к себе.{w} Он нехотя поддался."
    renu "А вот ты поаккуратнее со словами, молодой человек."
    renu "У меня нервы немного шалят в последнее время.{w} Давай не будем лишний раз меня выводить на гнев."
    renu "Если тебе ещё нужна голова на плечах, то иди своей дорогой и ничего не говори.{w} Твой голос как наждак для моего мозга."
    renu "Так что продолжай месить глину в своём кружке и с глаз моих долой."
    renu "Я ничего не говорю тебе - ты ничего не ляпаешь в ответ. Ясно?"
    play ambience ambience_camp_center_day volume 1 fadein 1
    play sound3 out_vosp volume 1
    stop sound_loop
    $ volume(1, "music")
    scene bg ext_clubs_day
    show un normal pioneer
    with fl_scare
    "Из этих <<Клубов>> вышла тёмноволосая девочка."
    show un surprise pioneer with byso
    "Она посмотрела на Регину и, словно её зная, удивилась."
    play sound3 in_vosp volume 1
    $ volume(0, "music")
    play sound_loop OMORI
    stop ambience fadeout 1
    scene bg ext_boathouse_day
    show shum_red
    with fl_scare
    renu "А теперь у нас необычное шоу."
    "Она взяла ████ за волосы и подняла её голову."
    maku "Нет! Не смей её убивать!!!"
    ktu "В главных ролях... ██████████ и ████ ████████."
    renu "И название ему... <<Долой предательские мысли>>!"
    play ambience ambience_camp_center_day volume 1 fadein 1
    play sound3 out_vosp volume 1
    stop sound_loop
    $ volume(1, "music")
    scene bg ext_clubs_day with fl_scare
    "Регина схватилась за голову.{w=1} В черепушке зазвенела какая-то не очень сильная, но неприятная пустота."
    "Она растерянно оглянулась.{w=1} Вокруг стоял тот же мир, что и минуту назад, только она почувствовала его пронзительную и раздражающую безнадежность."
    play sound3 sfx_bush_leaves volume 1
    stop music fadeout 1
    show un surprise pioneer far at left with dspr
    show us surp3 sport far at right with dspr:
        linear 1.0 xalign 0.28
    "Неожиданно из соседних кустов выскочил кто-то."
    play music music_list["eat_some_trouble"] fadein 3
    "Девочка в ярко-красной футболке с надписью <<СССР>>."
    "Издалека она казалась совсем маленькой и, наверное, по возрасту была на несколько лет младше."
    "Регина хотела всё-таки подойти, как вдруг красноволосая подскочила к другой девочке и начала что-то говорить, при этом экспрессивно размахивая руками."
    show un shy pioneer far at left with dspr
    "Та же в свою очередь смутилась, потупила взгляд и ничего не ответила."
    "Девочка помладше вдруг достала что-то из кармана и начала трясти этим перед лицом первой девочки."
    window hide
    scene cg d1_grasshopper
    with dissolve
    window show
    "Это был кузнечик."
    unp "Ииииии-иии-иииииии!"
    "Завизжала первая девочка и убежала вглубь лагеря."
    scene bg ext_clubs_day
    show us grin sport at left with dspr:
        linear 2.0 xalign 2.0
    with dissolve
    "Другая посмотрела на Регину, ухмыльнулась и бросилась за испуганной девочкой."
    hide us
    uth "Цирк какой-то..."
    play sound3 in_vosp volume 1
    $ volume(0, "music")
    play sound_loop OMORI
    stop ambience fadeout 1
    scene bg ext_clubs_day
    show shum_red
    with fl_scare
    "█████ ускорился, что было сил."
    ktu "Цирк, не иначе."
    renu "А то.{w=1} А теперь все, кто видел бег ██████ за ████████, занести по сто рублей в кассу цирка."
    play ambience ambience_ext_road_day volume 1 fadein 1
    play sound3 out_vosp volume 1
    stop sound_loop
    stop music
    $ volume(1, "music")
    scene bg ext_clubs_day with fl_scare
    $ volume(0.5, "ambience")
    play sound_loop kontuz volume 1 fadein 1
    "Словно кирпичом на голову свалилась боль."
    "Она заполнила Регину целиком, придавив все остальные чувства."
    "Пение птиц стало далеким и неопределенным, словно их отключили."
    "Регина вдруг ощутила острый и пронизывающий холод, и ей на миг показалось, что сердце остановилось."
    play music music_list["farewell_to_the_past_edit"]
    $ volume(1, "ambience")
    stop sound_loop fadeout 1
    elp "Что с тобой? {w=1}Всё в порядке?"
    show el normal pioneer with byso
    "Она подняла глаза с земли и увидела относительно высокого светловолосого парня."
    renr "Да, всё в порядке."
    "Регина встала на ноги и улыбнулась."
    show el smile pioneer with byso
    elp "А, ну раз так, то хорошо."
    elp "Меня, кстати, зовут Серёжа, но друзья называют Электроник."
    el "Ты тоже зови."
    renr "Хорошо."
    show el grin pioneer with byso
    el "Не хочешь вступить к нам в клуб кибернетиков?"
    "Она потёрла подбородок, словно и в правду раздумывая над его предложением."
    renr "Спасибо, я подумаю."
    show el grin pioneer with byso
    el "Если захочешь - приходи, я всегда тут."
    hide el with byso
    "Подмигнул Электроник и вернулся на исходную."
    uth "Эта мигрень...{w=1} Это воспоминания..."
    uth "Далёкие, но красивые, словно кадры из старого чёрно-белого фильма..."
    uth "Или из давно забытой передачи про двух смелых космонавтов на ракете, сконструированной и построенной по чертежам и эскизам слепого инженера..."
    uth "И кажется...{w=1} Их история окончилась смертью..."
    uth "Но почему мне начинает всё больше казаться, что это произошло со мной? Я вроде жива..."
    uth "Надо искать ответы..."
    window hide
    stop ambience fadeout 1
    $ volume(0, "music")
    play sound3 Glitch3 volume 1
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 0.1
    scene bg ext_clubs_day:
        zoom 0.8
    show re_crusifix_shum_a
    show image monitor_adm
    with dissolve
    play sound_loop Radar
    ik_sh "Вот видишь, она не подаёт никаких признаков девиации."
    "Генда потёр подбородок и кивнул."
    gg "Да, ты прав.{w=1} Головная боль скорее всего вызвана усиленной работой механизма по подмене воспоминаний."
    gg "В таком случае мы можем идти.{w} Подождём пока она пройдёт 1-2 цикла."
    gg "Как раз сейчас перескажешь мне прочитанное в учебнике."
    ik_sh "Хорошо отец."
    window hide
    stop sound_loop
    play sound3 Glitch3a volume 1
    show Glitch_screen3:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 0.1
    $ volume(1, "music")
    play ambience ambience_ext_road_day volume 1 fadein 1
    scene bg ext_musclub_day with byso
    "Регина оказалась у огромного здания из которого доносилась скрипка."
    "Как и предыдущие здания, оно казалось знакомой."
    play sound3 vosp volume 1
    stop music
    play sound_loop OMORI
    scene bg int_musclub_day
    show image minerva_cg
    show shum_red
    with fl_scare
    pause 1
    scene bg ext_musclub_day with fl_scare
    "Ощутив головную боль, её тело само повело её прочь от этой мелодии."
    stop sound_loop fadeout 0.5
    scene bg ext_square_day with byso
    play music music_list["lightness"] fadein 3
    "Остановившись у площади, она посмотрела на медный памятник."
    uth "Даже ты выглядишь знакомо...{w=1} Что-ж такое..."
    "Она направилась к домикам, которые были за медным изваянием."
    scene bg ext_houses_day with byso
    "Домики, один похожий на другой, навевали атмосферу эпохи СССР."
    uth "Вспоминается книга Джорджа Оруэлла..."
    uth "Да, свобода - это рабство."
    "Регина шла на автопилоте, словно зная, куда она дойдёт."
    scene bg ext_house_of_mt_day with byso
    "Через минуту она оказалась у треугольного домика с велосипедом, внутри которого шли какие-то бессмысленные диалоги."
    play sound3 in_vosp volume 1
    $ volume(0, "music")
    play sound_loop OMORI
    scene bg ext_house_of_mt_day
    show shum_red
    with fl_scare
    "Вожатая была у домиков и сидя на скамейке что-то писала."
    ktu "Здравствуйте.{w=1} Вот прибыла новая пионерка.{w} Её зовут {b}Рена{/b}."
    "█████ подняла глаза, убрала ручку и посмотрела на Рену."
    mtp "Здравствуй, Рена.{w} Добро пожаловать в наш отряд."
    play sound3 out_vosp volume 1
    stop sound_loop
    $ volume(1, "music")
    scene bg ext_house_of_mt_day with fl_scare
    "Регина уже более-менее привыкла к головной боли. Она уже не вызывала такого шокирующего эффекта как в предыдущие разы."
    mt_voice "...и хватит издеваться над Леной..."
    show us grin sport far with byso
    play sound3 sfx_open_door_2 volume 1
    "Через мгновение дверь распахнулась, оттуда выбежала Ульяна и пронеслась мимо, всё так же лыбясь."
    hide us with dissolve
    show un normal pioneer at left with dissolve
    "За ней вышла девочка с хвостиками."
    play ambience ambience_int_cabin_day volume 1 fadein 1
    scene bg int_house_of_mt_day with byso
    play sound3 door_cl volume 1
    "Не обращая на неё особого внимания, Регина вошла в домик."
    show mt normal pioneer far with byso
    "Возле окна стояла девушка лет двадцати пяти на вид."
    show mt smile pioneer far with byso
    mtp "Приехала наконец!{w=1} Меня Ольга Дмитриевна зовут, я вожатая."
    renr "Добрый день...{w=1} Я Регина."
    hide mt
    show mt grin pioneer
    with byso
    "Она подошла ближе."
    mt "Знаю.{w=1} Мы тебя с утра ждём."
    renr "Хорошо, а что я тут?..."
    show mt smile pioneer with byso
    mt "Извини, мне пора идти.{w} Будешь жить со мной.{w=1} Твоя форма в шкафчике."
    renr "Ну...{w=1} Хорошо?"
    show mt grin pioneer with byso
    mt "С минуты на минуту обед.{w=1} Как переоденешься - иди в столовую. Она около площади."
    play sound3 sfx_close_door_1 volume 1
    hide mt with byso
    "Объяснила вожатая и покинула помещение."
    uth "Дал бы мне кто-то понять...{w=1} Какого чёрта я делаю в этом лагере?"
    uth "Да и эти товарищи просто сваливают, когда я хочу их о чём-то спросить."
    uth "Ладно...{w} Раз я в этом лагере в качестве пионерки..."
    uth "Будем играть по их правилам.{w=1} Посмотрим что дальше будет..."
    "Постепенно переодеваясь в пионерский наряд, Регина думала о своём появлении в Совёнке."
    uth "А ведь я и не знаю, кто я."
    uth "Не помню никаких людей из своей жизни, родителей..."
    uth "Может быть они меня ищут?"
    uth "А может они меня сюда и сослали."
    uth "При этом я полностью потеряла понимание происходящего..."
    uth "Головные боли...{w=1} Воспоминания про некую Рену..."
    play sound3 sfx_open_cabinet_1 volume 1
    "Надев юбку, Регина посмотрела на себя в зеркало."
    uth "А Регина и Рена - созвучные имена..."
    uth "Может я и есть Рена?"
    uth "Нет, вряд-ли..."
    uth "Вроде все эти люди..."
    play music OMORI
    play sound_loop Glitch_loop volume 0.11 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.3
    with byso
    eth "НЕ СТОЯТ И СЕКУНДЫ МОЕГО ВРЕМЕНИ!"
    stop sound_loop fadeout 0.5
    hide Glitch_screen3 with byso
    uth "...знают меня как Регину... {w=1}А воспоминания штука..."
    play sound_loop Glitch_loop volume 0.19 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.4
    with byso
    eth "КОТОРАЯ ВЫГРЫЗАЕТ ДУШУ, НЕ ОСТАВЛЯЯ НИЧЕГО, ЧТО ВЫТЕРПЕЛ БЫ ЧЕЛОВЕК!"
    stop sound_loop fadeout 0.5
    hide Glitch_screen3 with byso
    uth "...недолговечная...{w=1} Стоит доверять остальным."
    uth "Мало ли им потребуется..."
    play sound_loop Glitch_loop volume 0.25 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.5
    with byso
    eth "УМЕРЕТЬ НА НЕСКОЛЬКО ЛЕТ ПОРАНЬШЕ."
    stop sound_loop fadeout 0.5
    hide Glitch_screen3 with byso
    uth "...помочь.{w} Может за эту помощь я получу что-то кроме..."
    play sound_loop Glitch_loop volume 0.32 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.6
    with byso
    eth "НОЖА В СПИНУ."
    stop sound_loop fadeout 0.5
    stop music fadeout 0.5
    hide Glitch_screen3 with byso
    uth "Пустого игнорирования."
    uth "Ладно, пора идти..."
    play sound3 sfx_open_cabinet_1 volume 1
    play music music_list["get_to_know_me_better"] fadein 3
    "Регина отошла от зеркала и закрыла шкаф."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_house_of_mt_day with byso
    play sound3 door_cl volume 1
    pause 0.25
    show blink
    "Выбравшись на улицу, она прикрыла глаза и глубоко вдохнула свежий воздух."
    uth "Пойду наверное до <<Клубов>>.{w=1} Может быть мне Электроник что-то подскажет..."
    uth "Да и может быть мы виделись.{w} Что-то он кажется мне знакомым."
    uth "Но не тем, кто был главным человеком в моей жизни..."
    scene bg ext_house_of_mt_day
    show unblink
    "Тяжело вздохнув, Регина направилась обратно к клубам."
    scene bg ext_houses_day with byso
    uth "Главный человек моей жизни? {w=1}Откуда такая мысль..."
    play sound_loop Glitch_loop volume 0.32 fadein 0.5
    $ volume(0, "music")
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.5
    with byso
    eth "ИЗ ТВОЕГО СТЁРТОГО СОЗНАНИЯ!"
    stop sound_loop fadeout 0.5
    $ volume(1, "music")
    hide Glitch_screen3 with byso
    uth "Что?..."
    "Регина покрутила головой, пытаясь найти тот тихий голос."
    uth "Верно послышалось...{w=1} Странно..."
    scene bg ext_square_day with byso
    play sound3 sfx_dinner_horn_processed volume 1
    "Почти дойдя до клубов, она услышала мелодию из громкоговорителей."
    mt "Регина, вот и ты."
    show mt smile pioneer with byso
    "Регина отозвалась на слова вожатой."
    renr "Да, Ольга Дмитриевна."
    show mt grin pioneer with byso
    mt "Вижу ты изучаешь наш лагерь, молодец."
    play sound2 sfx_paper_bag volume 1
    "Вожатая достала из кармана бумажку и протянула Регине."
    show mt smile pioneer with byso
    mt "Вот, это обходной."
    play sound sfx_paper_bag volume 1
    "Она приняла бумажку и, повертев в руках, убрала в нагрудный кармашек."
    show mt normal pioneer with byso
    mt "Тебе надо будет его заполнить.{w} Нужны подписи всех глав клубов."
    show mt smile pioneer with byso
    mt "А сейчас у нас обед в столовой. Пойдём, я тебя провожу."
    renr "Хорошо..."
    show mt normal pioneer with byso
    "Пойдя с вожатой Регина задумалась."
    uth "А может её поспрашивать?"
    uth "Вдруг расскажет что-то полезное."
    uth "Все люди могут сказать что-то полезное."
    play sound_loop Glitch_loop volume 0.38 fadein 0.5
    $ volume(0, "music")
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.46
    with byso
    eth "ТОЛЬКО ПОСЛЕ ДЛИТЕЛЬНЫХ ПЫТОК!"
    stop sound_loop fadeout 0.5
    play music music_list["lightness"]
    scene bg ext_dining_hall_near_day
    show mt surprise pioneer
    with byso
    "Регина снова посмотрела по сторонам, чем привлекла внимание вожатой."
    mt "Что такое, кого-то ищешь?"
    play sound_loop Glitch_loop volume 0.2 fadein 0.5
    stop music fadeout 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.46
    with byso
    eth "ЛЮБИМОГО!{w=1} ДОРОГОГО!{w=1} КОНСТАНТИНА!"
    stop sound_loop fadeout 0.5
    hide Glitch_screen3 with byso
    renr "Я ищу Константина..."
    "Вожатая удивилась и потёрла подбородок."
    mt "Не знаю о ком ты. У нас таких нет."
    uth "Какой Константин?{w=1} Кто это?"
    uth "Что со мной происходит?"
    show mt shocked pioneer with byso
    mt "Регина, ты в порядке?{w=1} Всё хорошо?"
    play music HeartBeat fadein 3
    play sound_loop Glitch_loop volume 0.2 fadein 0.5
    stop ambience fadeout 1
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.2
    with byso
    eth "УБЕЙ! {w=1}РАЗОРВИ ЕЁ НА КУСКИ!"
    play sound_loop Glitch_loop volume 0.3 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.3
    with byso
    eth "ПРЯМО СЕЙЧАС!{w=1} НЕ ПОКАЗЫВАЙ СЛАБОСТЬ!"
    play sound_loop Glitch_loop volume 0.35 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.4
    with byso
    eth "СЛОМАЙ ЕЙ ШЕЮ!{w=1} РАЗОРВИ ЕЁ СУХОЖИЛИЯ!"
    play sound_loop Glitch_loop volume 0.4 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.5
    with byso
    eth "УБЕЙ ЭТУ СУКУ!"
    play sound_loop Glitch_loop volume 0.45 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.6
    with byso
    eth "ВЫРВИ ЕЙ КОСТЬ И ВОТКНИ ЕЙ В ГОЛОВУ!"
    play sound3 sfx_pat_shoulder_hard volume 1
    "Вожатая остановила её и взяла за плечи."
    mt "Регина!"
    play sound_loop Glitch_loop volume 0.5 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.7
    with byso
    "Её ладонь сжалась в кулак, а мышцы напряглись. Рука задрожала."
    stop sound_loop fadeout 1
    play ambience ambience_ext_road_day volume 1 fadein 1
    stop music fadeout 1
    hide Glitch_screen3 with dissolve
    "Вмиг она снова взяла себя под контроль."
    play music music_list["silhouette_in_sunset"] fadein 3
    renr "Да...{w=1} Всё хорошо."
    show mt sad pioneer with byso
    mt "Слава богу...{w=1} Я уж испугалась..."
    mt "Сходи к Виоле, нашей медсестре.{w} Она разберётся с твоей странной дрожью."
    renr "Я поняла...{w=1} Схожу..."
    scene bg ext_dining_hall_near_day with byso
    "У столовой их пути разошлись. Вожатая ушла обратно в лагерь, а Регина взялась за голову."
    renr "Надо себя контролировать..."
    renr "Этот голос... {w=1}Он заставляет меня делать ужасные вещи..."
    renr "Я бы никогда не хотела никого убивать..."
    play sound3 sfx_pat_shoulder_hard volume 1
    "Регина почувствовала, что кто-то положил руку ей на плечо."
    el "Снова привет."
    show el smile pioneer with byso
    "Она обернулась и выдавила странную улыбку."
    renr "Привет...{w=1} Ты что-то хотел?"
    show el laugh pioneer with byso
    el "Не хочешь со мной за столик кибернетиков?{w} Вместе есть вкуснее."
    "Подумав, что от этого хуже не будет, Регина пожала плечами."
    renr "Пойдём."
    window hide
    stop ambience fadeout 1
    $ volume(0, "music")
    play sound3 Glitch3 volume 1
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 0.1
    scene bg int_dining_hall_people_day:
        zoom 0.8
    show re_crusifix_shum_a
    show image monitor_adm
    with dissolve
    play sound_loop Radar fadein 3
    gg "Вроде всё хорошо, она не подаёт признаков девиации.{w=1} Только побочные эффекты."
    ik_sh "Тогда мы можем перераспределять механизмы автокоррекции. Надо восстанавливать остальные симуляции."
    gg "Ты прав. {w=1}Так и поступим."
    gg "Компьютер! Перераспределить механизмы автокоррекции!"
    gt4 "Выполняю."
    gg "Уже предвкушаю наш триумф, сынок.{w} Сопротивление ещё в инреальности, но как только мы введём новых, практически неуязвимых пустышек, всё изменится."
    ik_sh "Но почему ты не отследил их перемещения?"
    gg "Их портативные, как они их называют, <<перехватчики кода>>, не могут быть выслежены."
    gg "Потому, как мы закончим с рыжей, мы начнём исследовать уязвимость, которая им и даёт эту способность перемещаться по симуляциям."
    ik_sh "Хорошо, отец."
    gg "Пошли домой.{w} Я проведу тебе небольшую лекцию по кодировке инреальности и можешь идти спать."
    ik_sh "Мама хотела чтоб ты сегодня провёл вечер с ней."
    gg "Хорошо, у меня как раз есть на это время."
    window hide
    play sound3 Glitch3a volume 1
    stop sound_loop
    show Glitch_screen3:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 0.1
    $ volume(1, "music")
    play ambience ambience_dining_hall_full volume 1 fadein 1
    scene bg int_dining_hall_people_day
    show el smile pioneer
    with byso
    "Регина сидела с Электроником и под его монолог о своём клубе уплетала гречку с котлетами."
    el "...вот так мы и планируем собрать робота.{w=1} Что думаешь?"
    renr "Да, класс."
    "Пытаясь скрыть своё безразличие отстрелялась она."
    show el grin pioneer with byso
    el "Конечно же класс!{w=1} Это будет прорывом в робототехнике."
    uth "Прошла тысяча сожалений, как я с тобой села..."
    stop ambience fadeout 1
    play sound3 in_vosp volume 1
    $ volume(0, "music")
    play sound_loop OMORI
    scene bg ext_dining_hall_near_day
    show shum_red
    with fl_scare
    el "О, привет Рена.{w=1} Не хочешь с нами за столик кибернетиков?{w} Вместе есть вкуснее."
    "Рена искренне рассмеялась, чем ещё пуще смутила Электроника."
    ren "Я только из столовой вышла, а меня уже тут достаёт кибернетик с предложениями на свидание."
    ren "Приятного тебе аппетита, спасибо за предложение, мы вам перезвоним."
    play ambience ambience_dining_hall_full volume 1 fadein 1
    play sound3 out_vosp volume 1
    stop sound_loop
    $ volume(1, "music")
    scene bg int_dining_hall_people_day
    show el smile pioneer
    with fl_scare
    el "А хочешь я покажу тебе нашего робота?"
    renr "Да, давай, почему нет."
    uth "И зачем я это сказала..."
    show el laugh pioneer with byso
    "Электроник встал со стула и воодушевлённо махнул рукой в сторону выхода из столовой."
    el "Так идём же. Заодно познакомлю с Шуриком."
    play ambience ambience_forest_night volume 1 fadein 1
    scene bg ext_dining_hall_near_day
    show el smile pioneer
    with byso
    renr "Слушай, а можешь мне рассказать кое-что?"
    show el grin pioneer with byso
    "Электроник улыбнулся, наверняка думая, что вопрос будет про их изобретение."
    el "Конечно!{w} Что ты хотела бы узнать?"
    scene bg ext_dining_hall_away_day
    show el smile pioneer
    with byso
    renr "А что это за лагерь?"
    show el normal pioneer with byso
    "Он видимо расстроился.{w=1} Это явно было не то, что он хотел услышать."
    el "А, лагерь то..."
    el "Практически лучший лагерь в СССР, в который путёвки выписывает сам Генда."
    scene bg ext_square_day
    show el normal pioneer
    with byso
    uth "Так вот к чему тот памятник..."
    renr "А кто этот Генда?"
    show el surprise pioneer with byso
    "На его лице всплыло неподдельное удивление."
    el "Ты не знаешь?!{w=1} Это же наш величайший партийный деятель!"
    el "Он столько всего сделал для нашей страны... Построил много школ, детских садов, парков..."
    el "И как его можно не знать..."
    renr "Я просто не местная.{w} Забудь что спрашивала."
    show el normal pioneer with byso
    uth "Да-а, видимо важная шишка..."
    play sound_loop Glitch_loop volume 0.5 fadein 0.5
    stop music fadeout 0.5
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.6
    with byso
    eth "ГЕНДА ДОЛЖЕН ПАСТЬ!"
    stop sound_loop fadeout 0.5
    hide Glitch_screen3
    show el smile pioneer
    with vpunch
    "Стукнув себя по голове, Регина нахмурилась."
    scene bg ext_clubs_day
    show el surprise pioneer
    with byso
    uth "Прочь из моей головы!"
    el "Что ты делаешь?"
    renr "Да просто...{w=1} комара перебила."
    show el smile pioneer with byso
    "Электроник повёлся и ухмыльнулся."
    el "А-а, ну это да..."
    el "Комаров у нас очень много.{w} После города совершенно непривычно."
    uth "Как же ты много говоришь лишней информации...{w=1} Невыносимо просто."
    play music music_list["lightness_radio_bus"] fadein 3
    play sound3 sfx_open_door_clubs_nextroom volume 1
    show el laugh pioneer with byso
    "Он открыл дверь перед Региной и пропустил её."
    el "Прошу в наш клуб."
    play ambience ambience_clubs_inside_day volume 1 fadein 1
    scene bg int_clubs_male_day with byso
    "Регина вошла в помещение и осмотрелась."
    uth "Знакомо...{w=1} Снова."
    show el normal pioneer with byso
    el "Так, а где робот?"
    sh "Робот тут!"
    stop music fadeout 1
    stop ambience fadeout 1
    play sound door_break
    play sound3 sfx_lena_hits_alisa volume 1
    scene bg black with vpunch
    "Одна из дверей резко открылась и зашибла Регину.{w=1} Она провалилась в некое состояние, похожее на сон."
    pause 1
    play music DeathStranding
    play sound_loop Glitch_loop volume 0.75 fadein 0.5
    scene bg kt_room
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.6
    with byso
    stop sound_loop fadeout 0.5
    hide Glitch_screen3 with byso
    renu "Узнаешь это место?"
    "Комната о чём-то напоминала.{w} Что-то невидимое всё время напоминало о себе, хотелось обернуться и выяснить, что голос говорил по этому поводу."
    renr "Нет, я ничего не помню. Я даже не знаю, кто я."
    renu "Настало время вспомнить."
    renu "Для начала вспомни, как ты сюда попала."
    renr "Автобус. <<Икарус>>."
    play sound_loop Glitch_loop volume 0.75 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
    with byso
    pause 0.1
    stop sound_loop fadeout 0.5
    hide Glitch_screen3
    show image re_cr_smile_casual
    with byso
    "Перед Региной показалась девушка, которая выглядела в точности как и она."
    "Такой же рыжий волос, голубые глаза.{w=1} Девушка улыбалась."
    "Но улыбалась так, словно знала, в чём дело."
    play sound_loop Glitch_loop volume 0.75 fadein 0.5
    show Glitch_screen3:
        size (1920, 1080)
    with dissolve
    pause 0.25
    play sound_loop Glitch_loop volume 0.2 fadein 0.5
    scene bg pandora_box
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.2
    with fl_scare
    "На столе появилась красная коробка с орлом на крышке."
    "Один её вид вызывал тревогу. Острую, как свежий порез."
    "С непривычки Регине даже становилось не по себе."
    renr "Что в ней?"
    renu "{i}Кое-что...{/i}"
    renu "Откроешь эту коробку - вспомнишь всё."
    renu "То, из-за чего ты сейчас мучаешься."
    renu "То, за что ты потеряла самое дорогое."
    renu "То, по поводу чего разбито твоё сердце."
    renu "То, чего тебе так не хватает в жизни."
    renu "То, что тебе нужно вернуть как можно быстрее."
    "Регина осмотрела ящик, стараясь случайно его не коснуться."
    renr "Но зачем мне это?"
    renr "Я ведь даже имени своего не вспомнила. Кто я?"
    "Девушка взяла Регину за руки и потянула к коробке."
    renr "Нет, не надо!"
    window hide
    stop sound_loop fadeout 0.5
    stop music fadeout 0.5
    play sound2 Glitch4
    scene bg black with fl_scare
    pause 1.5
    stop sound2
    pause 1
    play sound_loop kontuz volume 1
    el "Регина, ты цела?!"
    "Голос звучал отдалённо, словно его источник находился далеко-далеко."
    "В её сознании начало что-то проясняться."
    "И вдруг она кое-что поняла..."
    stop sound_loop fadeout 1
    window hide dissolve
    pause 1.5
    $ _dismiss_pause = False
    play music "inrealnost/Music/Music/Tyranny.mp3" fadein 3
    scene bg prologue_inr with Dissolve(4.5)
    scene bg black with Dissolve(0.5)
    scene bg re_headpat with Dissolve(2.75)
    scene bg black with Dissolve(0.75)
    scene bg re_int2 with Dissolve(4.5)
    scene bg black with Dissolve(0.5)
    scene bg kt_insane with Dissolve(3)
    scene bg black with Dissolve(1)
    scene bg zvezda_red
    show image re_stunned
    with Dissolve(1)
    scene bg black with Dissolve(1)
    pause 1.5
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=70}{color=#8c000f}Что ты делаешь?!{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1)
    pause 0.5
    hide text with byso
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=70}{color=#8c000f}Почему ты всё ещё сдерживаешься?!{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(3)
    scene bg black with dissolve
    pause 1
    scene bg ext_square_night_blood
    show image poter_r
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=70}{color=#8c000f}Ты забыла что они сказали нам?!{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(2)
    scene bg black with Dissolve(0.25)
    pause 0.25
    scene bg zvezda_red
    show image re_stunned
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=70}{color=#8c000f}Что они сделали?!{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1)
    scene bg black with byso
    scene bg re_torture
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=70}{color=#FF000f}Они думают, что ты монстр!{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(2)
    pause 0.25
    scene bg re_torture:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 7 crop (497, 223, 980, 630)
    show text "{sc=10}{font=inrealnost/font/Ustroke.ttf}{size=70}{color=#FF0000}ДОКАЖИ ЧТО ОНИ ПРАВЫ!{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    pause 1.8
    $ _dismiss_pause = True
    play music "<from 36.75>inrealnost/Music/Music/Tyranny.mp3"
    play ambience ambience_clubs_inside_day
    play sound3 head_crush2 volume 1
    scene bg int_clubs_blood_day
    show sh scared pioneer at left
    with fl_scare
    "Рена вскочила на ноги и, взяв гаечный ключ, пробила череп Электроника."
    "Огромная лужа крови разбрызгалась по стене, а Шурик не мог поверить в происходящее."
    sh "Что ты творишь?!"
    play sound3 head_crush volume 1
    hide sh with vpunch
    play sound burn volume 1
    pause 0.4
    play sound2 sfx_bodyfall_1 volume 1
    "Схватив со стола включенный паяльник, Рена воткнула его в глаз Шурика."
    "Тело перестало функционировать, а из глаза повалил чёрный пар."
    ren "Я вернулась!"
    play ambience ambience_camp_center_day volume 1 fadein 1
    play sound3 door_break volume 1
    scene bg ext_clubs_day
    show us grin sport
    with vpunch
    "Выбив дверь клубов, она увидела Ульянку."
    us "О, а ты же нове...{w=0.41}{nw}"
    show us fear sport
    pause 0.01
    play sound3 head_crush4 volume 1
    hide us
    with fl_scare
    "Хватив её за волосы, Рена размозжила её голову об стену."
    ren "Как приятно снова быть собой!"
    play sound3 wood_hit_head volume 1
    "Отломав дрын от лестницы, она побежала в глубь лагеря."
    scene bg ext_square_day
    show sl smile pioneer far
    with byso
    "На площади была Славя, которая мела землю."
    hide sl
    show sl surprise pioneer
    with bso
    "Она знатно удивилась."
    sl "Зачем тебе эта..."
    play sound3 head_crush4 volume 0.7
    hide sl with fl_scare
    "Словно на рыцарском турнире, Рена с разбегу насадила Славю на деревянный дрын."
    play sound head_crush volume 1
    hide sl with fl_scare
    "Взяв швабру, Рена вонзила её девочке в рот, пробив голову."
    play sound2 sfx_bush_body_fall volume 1
    "Судя по хрусту, череп не выдержал такого удара."
    un "Что ты делаешь?!"
    show un shocked pioneer far with bso
    "Лена отвлеклась от книги и чуть ли не залезла на дерево от страха."
    play sound3 loud_sound volume 0.61
    hide un
    show un scared pioneer
    with bso
    "Рена вмиг приблизилась к темноволосой."
    ren "А не видно?!"
    play sound sfx_pat_shoulder_hard
    hide un with vpunch
    "Схватив её за волосы, Рена впечатала девочку в землю."
    play sound3 sfx_punch_washstand volume 1
    pause 0.4
    play sound2 sfx_punch_washstand volume 1
    pause 0.4
    play sound sfx_punch_washstand volume 1
    pause 0.4
    play sound3 head_crush volume 1
    hide sl with fl_scare
    "Удар за ударом, она повторяла это действие, пока её лицо полностью не было обезображено от ударов."
    mt "Регина!{w=1} Прекрати немедленно!"
    show mt scared pioneer with bso
    "Резко повернув голову на 90 градусов, Рена поразила Сахарову взглядом."
    ren "Что я там хотела с тобой сделать?!"
    play sound3 sfx_bush_body_fall volume 1
    play sound perelom volume 1
    hide mt with vpunch
    "Прыгнув на вожатую, она вывихнула ей руку."
    play sound2 horror1 volume 1
    play sound fem_krik volume 1
    "Женщина кричала, пыталась вырваться, пока Рена голыми руками отдирала её руку от тела."
    play sound2 head_crush volume 1
    play sound sfx_punch_washstand volume 1
    "Рена, оторвав руку Сахаровой, ударила её, пользуясь конечностью как мухобойкой."
    play sound3 sfx_punch_washstand volume 1
    ren "Хватит!"
    play sound sfx_punch_washstand volume 1
    ren "Себя!"
    play sound2 sfx_punch_washstand volume 1
    ren "Бить!"
    play sound3 head_crush4 volume 1
    hide sl with fl_scare
    "Наигравшись с Вожатой, Рена раздавила её голову."
    ren "А впереди ещё столько трупов!"
    stop ambience fadeout 1
    scene bg black with byso
    pause 1
    scene bg ext_path_day
    show image me_st at center:
        zoom 1
        linear 0.1 zoom 4 yanchor 0.1
    play sound loud_sound
    scene bg black with fl_scare
    pause 1
    scene bg ext_polyana_sunset
    show dv scared pioneer at center:
        zoom 1
        linear 0.1 zoom 4 yanchor 0.2
    play sound loud_sound
    scene bg black with fl_scare
    pause 1
    scene bg ext_path_night
    show mi scared pioneer at center:
        zoom 1
        linear 0.1 zoom 4 yanchor 0.2
    play sound loud_sound
    scene bg black with fl_scare
    pause 1
    scene bg ext_square_night_blood
    show image cs_sur
    with byso
    cs "Не надо! Одумайся! Прошу!"
    play sound3 perelom volume 1
    hide image cs_sur with vpunch
    pause 0.25
    scene bg re_blood with byso
    "Рена свернула медсестре шею, улыбнулась и посмотрела в небо."
    ren "Ну что, Генда."
    ren "Настало время расплатиться за смерть Кости."
    ren "Ты оставил меня в живых?{w=1} Молодец."
    ren "Это была твоя последняя ошибка, которая дорого тебе обойдется."
    ren "Я убью тебя не сразу, а постепенно."
    ren "Сперва я уберу всё что тебе дорого, чтобы ты прочувствовал весь ужас своей жизни."
    ren "Разрушить твою жизнь будет несложно.{w} Для меня."
    ren "Но я помогу тебе увидеть мир моими глазами...{w=1} Боль, боль и ничего кроме боли без любимого."
    ren "<<Это ад, это ад>>, как говорил один поэт..."
    ren "Когда ты будешь умирать, ты поймешь, как ужасна эта боль."
    play sound3 power volume 1
    scene bg ext_square_night_blood_red with byso
    "Небо окрасилось красным.{w=1} Открылись порталы."
    ren "И мы начинаем эту кровавую серию..."
    play sound portal volume 1
    scene bg black with byso
    stop ambience fadeout 1
    "Она сделала переход."
    stop music fadeout 2
    pause 2
    window hide
    play sound Glitch3 volume 1
    show Glitch_screen2:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 0.1
    play music tish
    show re_crusifix_shum_b
    show image monitor_adm
    with dissolve
    gg "Рена вернула себе память..."
    gg "Она не должна была уйти далеко..."
    gg "Надо её найти..."
    gt4 "Внимание!{w=1} Стабильность инреальности упала до 99 процентов."
    gg "Компьютер!{w} Режим диагностики."
    gg "Нельзя допустить, чтоб кто-то покидал дом..."
    gg "Запретить покидать административные подпространства для 0-0-0-0-0-0-2-А, 0-0-0-0-0-0-3-А, 0-0-0-0-0-0-4-А, 0-0-0-0-0-0-5-А."
    gt4 "Комендантский час введён.{w=1} Вывожу лист диагностики."
    $ renpy.block_rollback()
    window hide
    stop music fadeout 1
    play sound3 Glitch3a volume 1
    show Glitch_screen3:
        size (1920, 1080)
    $ renpy.pause(1, hard=True)
    scene bg black
    pause 2
    $ _dismiss_pause = False
    play music OMORI2 fadein 3
    show image death_count
    show screen re_death_count1
    with Dissolve(2)
    pause 16
    play sound_loop Glitch_loop volume 0.75 fadein 0.5
    hide screen re_death_count4
    hide image death_count
    scene bg black
    play sound3 Glitch_loop volume 1
    show Glitch_screen3:
        size (1920, 1080)
    stop sound_loop fadeout 0.5
    pause 1
    stop sound3 fadeout 0.25
    scene bg black
    show text "{font=inrealnost/font/DOS.ttf}{size=282}{color=#580000}4253{p}Убийств{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
        zoom 0.5
        ease 5 zoom 1.5
    with Dissolve(1)
    pause 2
    scene bg black
    with Dissolve(1)
    pause 0.5
    play sound error2
    show text "{font=inrealnost/font/DOS.ttf}{size=100}{color=#580000}Приблизительная стабильность Инреальности = 20 процентов.{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.5
    pause 2
    scene bg black with Dissolve(2)
    play sound error2
    show text "{sc=10}{font=inrealnost/font/DOS.ttf}{size=200}{color=#580000}Возмездие близко{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    pause 2
    $ renpy.pause(3, hard=True)
    $ _dismiss_pause = True
    $ renpy.block_rollback()
    stop ambience fadeout 1
    play sound sfx_pat_shoulder_hard
    play music nightmare fadein 3
    scene bg int_admins_room
    show image andr_fear2
    with fl_fast
    andr "Не трогай меня!{w=1} Мы союзники!"
    play sound2 knife_in volume 0.25
    play sound3 genmod2 volume 1
    hide image andr_fear2 with vpunch
    "Рена ввела теорин в шею капитана."
    andr "Сука!"
    ren "Тихо-тихо..."
    "Она демонически улыбнулась, глядя на парня, теряющего сознание."
    ren "Союзниками мы станем, когда я тебе мозг разжижу этим препаратом."
    "Андрей потерял сознание.{w} Рена отбросила шприц, размяла пальцы и посмотрела в окно."
    th "Да уж...{w=1} Много же симуляций пало..."
    th "Я конечно не считала, но на ощущение около 2-3 тысяч."
    "Рена села на кресло и, закинув руки за голову, поставила ноги на труп солдата, которому вышибла мозги."
    th "И надо двигаться дальше.{w} Судя по оборудованию сопротивления, она сейчас примерно составляет 30 процентов..."
    th "Сейчас разберёмся с этим товарищем и пойду дальше."
    "Она взяла в руки пульт и посмотрела на кнопки."
    th "Не знаю, зачем тут режим рандомного перемещения, но он тут как-никак кстати..."
    th "У Генды ещё много времени уйдёт чтоб меня отыскать."
    "Она взяла кинжал, который, как выяснилось, украл один из сопротивленцев."
    th "Да и у меня есть весомый аргумент в нашем будущем диалоге."
    "Капитан очнулся."
    show image andr_normal_white with byso
    "Он встал на ноги и, осмотрев помещение своими белыми глазами, остановился на Рене."
    andrf "Готов выполнять задачу."
    "Рена, встав со стула, подошла к парню."
    "Она протянула ему ещё один пульт."
    ren "Значит. Все данные уже вбиты в перехватчик."
    ren "Твоя задача телепортироваться к административной симуляции, затем пробраться в саму симуляцию и использовать это."
    play sound3 sfx_put_sugar_cart volume 1
    "Она взяла со стола два тротиловых жилета."
    ren "Два сразу."
    ren "Это вся работа."
    andrf "Будет исполнено, ваше превосходительство."
    play sound2 sfx_click_2 volume 1
    pause 0.1
    play sound3 teleport volume 1
    hide image andr_normal_white with fl_fast
    "Набрав код на пульте, он растворился в воздухе."
    ren "А я пойду боем на другую."
    play sound3 sfx_click_2 volume 1
    pause 0.2
    play sound sfx_click_1 volume 1
    pause 0.3
    play sound3 sfx_click_1 volume 1
    "Введя нужные цифры, она посмотрела в потолок."
    ren "Продолжаем."
    play sound3 teleport volume 1
    stop music
    scene bg ext_clubs_rain with fl_fast
    play ambience ambience_rain volume 0.6 fadein 1
    "Вмиг Рена оказалась у клубов.{w} На улице шёл дождь, что не сулило ничего хорошего."
    ren "Дождь..."
    ren "Так вот о чём говорил тот придурок-Цадик."
    play sound3 sfx_armature_swish volume 1
    play music Kerosene
    "Материализовав топор, Рена его раскрутила и направилась в лагерь."
    ren "Ну, похоже настал момент истины."
    scene bg ext_square_day_rain with byso
    "На площади она в тысячный раз посмотрела на медный памятник."
    ren "Интересно, а ты давно узнал о моих приключениях, или как всегда тянешь кота за яйца?"
    "Рена остановилась и посмотрела в небо."
    ren "Давай, я знаю, что дождь в симуляции всегда связан с административным присутствием."
    ren "Сейчас наш вопрос решится и я отправлю тебя к праотцам."
    scene bg ext_square_day_rain2 with fl_fast
    play sound2 sfx_thunder_wood volume 1
    pause 0.4
    scene bg ext_square_day_rain with byso
    "В статую ударила молния."
    stop ambience
    play sound2 afterdead volume 1
    scene bg ext_square_night with flash
    play ambience ambience_forest_night volume 1 fadein 1
    "Дождь прекратился и наступила ночь.{w=1} Зажглись фонари."
    gg "Так-так-так."
    ren "Ты в симуляции, а не в лесу с дятлом перетакиваешься."
    gg "Да, ужасная харизма досталась тебе от Константина."
    ren "У меня она хотя бы есть."
    scene bg zvezda
    show image genda_final1
    with byso
    "Образовался Генда.{w} Выглядел он совершенно по другому. Рена рассмеялась."
    ren "Ха-ха-ха! {w=1}Что, вырядился покруче, чтоб в гроб класть было не стыдно?!"
    ren "Побрился бы хоть, пугало!"
    gg "Заткнись!"
    gg "Я понял, что не должен был оставлять тебя в живых. Сейчас я это исправлю."
    "Рена взяла топор в обе руки и встала в боевую стойку."
    ren "Один на один?{w} Ну попробуй."
    "Генда улыбнулся."
    gg "А вот тут ты не права..."
    scene bg ext_square_night with byso
    play sound3 teleport volume 1
    pause 0.1
    show mt angry pioneer
    show us calml pioneer at left
    show dv angry pioneer at right
    with fl_fast
    "По щелчку его пальцев образовались Ульянка, Ольга Дмитриевна и Алиса."
    gg "Они со мной."
    ren "Да-а?{w} И ты думаешь, что они мне смогут помешать?"
    gg "Думаю что да."
    gg "Гончие! {w=1}В обычный вид."
    scene bg ext_square_night at shakerrr
    play sound3 horror1 volume 1
    play sound2 monster_sfx2 volume 1
    show image od_zombie
    show image us_zombie at left
    show image dv_zombie1 at right
    with fl_scare
    "Мигом все трое зарычали и начали рвать на себе кожу."
    "Прыснув в кулак, Рена перехватила топор и бросилась на одну из них."
    play sound2 slash volume 1
    scene bg ext_square_night with vpunch
    "Голова зомбифицированной Ульянки отлетела с плеч, а тело упало."
    ren "Одна есть."
    usm "Как бы не так..."
    show image monster2 at left
    show image monster21
    show image monster22 at right
    with fl_scare
    "Трое пустышек предстали в виде мясных мешков, называемых альфа-гончие."
    ren "Ну тогда мы начинаем."
    scene bg ext_square_night
    show image monster2
    with bso
    play sound3 pistol2 volume 1
    hide un with fl_fire
    pause 0.1
    play sound2 pistol2 volume 1
    hide un with fl_fire
    pause 0.1
    play sound pistol2 volume 1
    hide un with fl_fire
    pause 0.1
    "Рена схватила пистолет с разрывными патронами и несколько раз выстрелила в центральную гончую."
    play sound3 magic volume 1
    "Генда запустил в Рену снаряд, который она мастерски парировала."
    gg "А ты, всё-таки, далеко ушла от уродца создателя!"
    ren "Во второй раз это не прокатит, урод!"
    play sound3 sfx_armature_swish volume 1
    "Гончая зарычала и набросилась на Рену, но чётко увернулась от её топора." with vpunch
    gg "Эти пустышки обладают твоим ДНК.{w=1} Приблизительно."
    ren "5 минут и их не станет, я тебе обещаю!"
    play sound3 magic volume 1
    play sound2 slash volume 1
    hide image monster2 with fl_scare
    "Генда выстрелил в Рену, которая отрубила руку одной из гончих."
    play sound3 sfx_bones_breaking volume 1
    show image monster2 with byso
    "Животное сумело отрастить новую."
    ren "Про закон сохранения массы слышал?"
    play sound3 slash volume 1
    "Очередной удар пришёлся на щупальца." with vpunch
    ren "Им не удастся бесконечно отращивать новые конечности!"
    gg "На тебя хватит!"
    play sound magic volume 1
    "Выстрел снова не поразил цель.{w=1} Генда начал приходить в ярость."
    ren "Смирись.{w=1} Я найду твою семью и пущу на фарш!"
    gg "Ты умрёшь!{w=1} Вот что тебе сулит ближайшее будущее!"
    play sound3 slash volume 1
    play sound2 sfx_bush_body_fall volume 1
    hide image monster2 with fl_scare
    "Очередной разрез одна из гончих просто не выдержала."
    "Упав на землю, она, судя по всему, умерла."
    show image monster2 at left
    show image monster21 at right
    with byso
    ren "Что ты там говорил?!{w=1} Моё ДНК и бла-бла-бла?"
    gg "Сражайся!"
    play sound3 magic volume 1
    hide image monster21
    hide image monster2
    show image monster2
    with fl_scare
    "Генда выпустил ещё один снаряд, но Рена закрылась гончей."
    play sound3 monster_sfx5 volume 1
    "Гончая ревела, пока её разъедала белая плазма."
    stop sound3 fadeout 0.5
    ren "Да, даже если я не убью твоего юродивого наследника..."
    play sound3 pistol2 volume 1
    hide un with fl_fire
    pause 0.1
    play sound2 pistol2 volume 1
    hide un with fl_fire
    pause 0.1
    play sound pistol2 volume 1
    hide un with fl_fire
    pause 0.1
    play sound3 sfx_click_1 volume 1
    pause 0.51
    play sound2 sfx_drop_pipe volume 1
    "Рена несколько раз выстрелила в последнюю гончую, после чего выбросила пустой пистолет."
    ren "То даже он не будет таким ужасным наследником!"
    gg "Заткнись!"
    play sound3 wood_hit_head volume 1
    "Гончая попыталась проткнуть Рену, но вогнало свою вилу в дерево." with vpunch
    play sound2 slash volume 1
    pause 0.4
    play sound head_crush volume 1
    "Рена накинулась на спину монстра нанося длинные и размашистые порезы на спине застрявшего монстра." with fl_scare
    play sound3 magic volume 1
    play sound2 monster_sfx5 volume 1
    hide image monster2 with fl_scare
    "Генда снова попал в гончую, чем и убил."
    stop sound2 fadeout 0.5
    ren "Упси...{w=1} Кто-то за 2 минуты остался без союзников."
    scene bg zvezda
    show image genda_final1
    with byso
    "Он зарычал от злобы."
    gg "Ну всё, мразь, ты доигралась!"
    play sound3 afterdead volume 1
    play sound2 power
    scene bg zvezda_red
    show image genda_final2
    with fl_fire
    "Лицо Генды порвалось.{w=1} Вместо его глаз образовался красный крест."
    ren "М-м, что-то новенькое..."
    ren "Интересно, а такие метаморфозы никак не повлияют на твои способности?"
    ren "Ну давай, нападай!"
    play sound_loop laser_ray volume 2
    scene bg death_ray at shakerrr with fl_scare
    "Из его лица извергся красный луч, который оставлял лишь обожжённый след на своём пути."
    "Рена и его отлично парировала, просто пробегая быстрее."
    ren "Скучно!{w=1} Давай быстрее!"
    gg "Да как ты смеешь!"
    "Луч смерти расщеплял воздух, как лазерный резак."
    "Он рвал на куски трупы гончих, деревья, превращая их в маленький, еще дымящийся ад."
    "Генда никак не мог попасть по Рене, которая среди схватки достала трофейный кинжал."
    stop sound_loop fadeout 0.5
    scene bg zvezda_red
    show image genda_final2
    with byso
    "Метнув его в Генду, она промахнулась, а Генда временно прекратил огонь."
    gg "Ха!{w=1} И это всё на что ты способна?!"
    "Рена едко улыбнулась и наклонила голову."
    ren "Я просто отвлекала твоё внимание."
    play sound3 sfx_energy_door_bus volume 1
    scene bg ext_square_night_blood_red with vpunch
    "Удар."
    "Генда потерял свою возможность левитировать и упал на землю."
    "Рена подняла кинжал с пола и улыбнулась."
    ren "Вот и всё."
    "Она набросилась на Генду и вознесла топор над его головой."
    ren "Сдохни!"
    play ambience ambience_camp_center_evening volume 1 fadein 1
    play sound3 afterdead volume 1
    scene bg junk with flash
    "Вспышка."
    "Рену и Генду перенесло на какую-то свалку."
    "Пока Рена пыталась осознать произошедшее, Генда вскочил с земли и устремился бежать."
    ren "Что-то трупы разбегались...{w=1} К дождю, наверное."
    play sound3 knife_flying volume 1
    "Она метнула ножик ему в ногу, чем повалила на землю."
    scene bg re_junk with byso
    "Насвистывая, Рена пошла к лежащему Генде, который пытался отползти."
    gg "Нет! {w=1}Не смей!"
    ren "Да-а?"
    ren "Ты серьёзно?"
    play sound3 sfx_punch_medium volume 1
    "Рена поставила ногу на его спину, впечатав в кучу мусора."
    ren "А почему я не должна этого делать?"
    gg "Я дал вам возможность жить!"
    ren "А ничего, что ты эту возможность у нас забрал?!"
    ren "Я хотела жить с Костей...{w=1} Долго и счастливо..."
    ren "А ты..."
    ren "Ты его распылил, урод!"
    ren "И это конец."
    ren "Ты сдохнешь на помойке, где и должен."
    ren "А я воссяду на твой уродский трон и воскрешу любимого."
    gg "У тебя не выйдет!{w=1} Это..."
    play ambience ambience_library_day volume 0.51 fadein 1
    play sound3 afterdead volume 1
    stop music fadeout 3
    scene bg gg_room with flash
    "Вспышка."
    "Рену и Генду перенесло в какие-то царские хоромы."
    gg "Ч-что?..."
    ren "Ой, так сразу и в постель?{w=1} Так ещё и при всей семье?!"
    ren "Некультурно девушку без прелюдий тащить домой.{w=1}{cps=20} Мало ли она маньячка.{/cps}"
    gg "Нет!{w=1} Не смей!"
    ren "А в следующий раз выключай микрофон, когда болтаешь со своим выродком!"
    play sound3 wood_hit_head volume 1
    "Она впечатала Генду в пол лицом, отчего тот потерял сознание."
    play music lim fadein 3
    th "Это то место, где живёт семья Генды."
    th "Да-а... Так и думала, что это будет дворец."
    th "Оставлю его живым. Не на долго..."
    "Её взгляд остановился на шкафу.{w} В голове зародилась ужасная идея."
    play sound3 sfx_open_cabinet_1 volume 1
    "Она открыла шкаф."
    "В нём было огромное множество самых разнообразных видов одежды."
    "Штаны, нарядные пиджаки, галстуки-бабочки, строгие рубашки, зажимы для галстуков – все как на показе мод."
    play sound3 cloth volume 1
    "Взяв первый попавшийся элемент одежды, Рена разорвала его на тряпки."
    "Перевернув Генду, она затолкала одну из тряпок ему в рот, после чего обвязала вокруг головы, зафиксировав импровизированный кляп во рту."
    "Другой тряпкой она закрыла его глаза, зафиксировав всё донельзя надёжно."
    "Разорвав стильные мужские брюки, она подвязала его ноги и руки на морской узел."
    th "Не зря дедушка учил Костю вязать узлы..."
    play sound3 sfx_open_cabinet_1 volume 1
    "Полностью связав Генду, она затолкала его тело в шкаф и закрыла там."
    "Переведя внимание на тумбочку она заметила несколько примечательных предметов."
    play sound3 sfx_paper_bag volume 1
    show image gg_photo with byso
    "Одним из них была старая выцветшая фотография."
    "На ней были изображена счастливая семья Генды."
    "Генда, который сильно отличался от своего обычного состояния."
    "Женщина в длинном платье и пучком на голове."
    "Маленькая девочка с блокнотом в руках."
    "Парень, который весь был в пирсинге и выглядел как типичный рокер нулевых."
    "И другой парень, чем-то напоминающий самого Генду, который единственный не был счастлив на этой фотографии."
    th "Оставлю как список на убийства."
    hide image gg_photo with byso
    "Рена отложила фотографию за пазуху и взяла другой предмет."
    "Это были таблетки с подписью <<Снотворное>>."
    "В пачке было огромное количество таблеток, которым, казалось, можно усыпить и гончую."
    "Пачку она убрала туда же."
    "Помимо всего этого, она заметила странный шов на обоях."
    th "Так, а это уже странно..."
    "Отковырнув кусочек, она заметила железную дверь."
    "За тумбочкой она заметила небольшой тумблер."
    play sound3 sfx_click_1 volume 1
    play sound2 metal_door volume 1
    "После нажатия на него дверь начала медленно открываться."
    th "Потайная комната чтоб скрыть всё от семьи. Оригинально, Генда."
    scene bg gg_centr with byso
    "За дверью оказался небольшой кабинет, увешанный экранами, посреди которого стоял стул."
    "Рена подошла поближе и изучила происходящее на экранах."
    "На ней отображалась вся информация по инреальности."
    "Стабильность секторов, отдельных симуляций."
    "На главном мониторе была надпись."
    th "<<Механизм автокоррекции восстановлен.>>"
    th "Мгм...{w=1} А могу ли я его использовать?"
    play sound3 sfx_click_3 volume 1
    "Рена нажала кнопку на клавиатуре."
    gt4 "Неавторизированный доступ. {w}Введите пароль."
    th "Ага...{w=1} Вот что мне надо выбить из Генды. Пароль."
    th "Но сначала... {w=1}Пойти помыться."
    th "Вся в крови..."
    scene bg gg_room with byso
    play sound3 sfx_open_cabinet_1 volume 1
    "Вернувшись, она открыла шкаф, в котором сидел Генда."
    "Первым на глаза попался красный пиджак-тройка с красными брюками."
    play sound3 sfx_blanket_off2 volume 1
    th "Да, выглядит неплохо.{w=1} Беру."
    play sound3 sfx_open_cabinet_2 volume 1
    stop music fadeout 3
    scene bg gg_coridor with byso
    "Взяв этот набор, Рена покинула комнату."
    "Она оказалась в коридоре с зелёными полами."
    "Убедившись, что она не оставляет за собой грязных следов, Рена пошла вдоль стены."
    play music rutine fadein 3
    me "Как вы и просили.{w} Ваши книги."
    ik_sh "Благодарю, Семён, можешь быть свободен."
    me "Как пожелаете."
    "Кто-то пошёл в сторону Рены.{w=1} Она отложила одежду на пол и, прижавшись к стене, ожидала идущего."
    th "Начинается..."
    show image me_su with byso
    "К ней вышел Семён и, заметив Рену, удивился."
    me "Ты кто?{w=1} Что ты тут...{w=0.5}{nw}"
    play sound2 perelom volume 1
    play sound3 sfx_bodyfall_1 volume 1
    hide image me_su with fl_scare
    "Рена схватила его за голову и свернула Семёну шею, прокрутив на 180 градусов."
    "Тело упало на землю, а Рена потащила его в комнату Генды."
    scene bg gg_room with byso
    play sound3 sfx_blanket_off2 volume 1
    "Спрятав тушу под кровать, она тяжело вздохнула."
    th "Никогда мне не нравилось разбираться по-тихому..."
    th "Даже помыться не дают..."
    scene bg gg_coridor with byso
    "Вернувшись за одеждой, Рена продолжила поиски ванной."
    th "Надо бы ещё использовать снотворное по назначению..."
    stop music fadeout 3
    scene bg gg_bath with byso
    "В соседней комнате оказалась ванная комната.{w} Простая, белая с деревянным полом."
    "С окном, за которым блестело солнце."
    play music TheSecondDeath fadein 3
    th "Вот и оно..."
    "Рена разделась и, оставив окровавленную одежду на коврике, вошла в душ."
    play sound3 sfx_open_water_sink volume 1
    show image re_bath:
        crop (0, 1568, 1920, 1080)
        linear 10 crop (0, 0, 1920, 1080)
        linear 2 crop (0, 200, 1920, 1080)
    with byso
    play sound_loop sfx_water_sink_stream volume 1
    "Открыв воду, она встала под струю, чувствуя, как холодная влага постепенно просачивается в каждую клеточку ее тела."
    "Смывая с себя брызги крови, Рена провела рукой по лицу."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "Она заметила, как после смерти Константина ее жизнь потеряла вкус."
    "Исчезла единственная нить, связывавшая ее с миром, той единственной реальностью, которая имела для нее значение."
    "Все остальное стало просто бледным отражением того, что исчезло навсегда."
    "Её любви.{w=1} Верности. {w=1}Преданности."
    "Единственный человек в её жизни умер и ей ничего не осталось, кроме как воскресить его."
    "Он был живым, настоящим и бесконечно важным для неё - но он умер, а мертвому она ничем не могла помочь."
    "Он был совсем рядом — ей нужно было только протянуть руку, и она могла его коснуться."
    "Но он мертв."
    "А она нет.{w=1} И это ее пугало."
    "Закрыв глаза, чтобы не видеть брызг, разлетающихся во все стороны, она подставила под поток воды лицо."
    "По телу, покрытому крошечными капельками воды, прошла дрожь."
    "Холодная вода смыла следы крови."
    "Рену охватило странное чувство: она словно превращалась в нечто другое."
    "Она сконцентрировалась на возвращении её смысла жизни. Константина."
    "Любой ценой.{w} Любым способом."
    window hide dissolve
    stop sound_loop fadeout 0.5
    play sound3 sfx_close_water_sink
    pause 1
    $ set_mode_adv()
    scene bg gg_bath with byso
    "Вернувшись из душа, она убрала своё белое платье в один из ящиков, а сама начала переодеваться в украденную одежду."
    "Брюки и рубашка были самыми простыми, но очень аккуратными и дорогими."
    "Пиджак был немного маловат для её плеч, зато он шёл к рыжим волосам и голубым глазам."
    scene bg re_mirror with byso
    "Её взгляд остановился на зеркале."
    "Глядя на себя, она вспоминала Константина, его лицо, руки и голос, думала, что они были похожи."
    th "Жаль что Костя меня сейчас не видит..."
    th "Я так похожа на него в офисе."
    th "Если бы я могла обернуть время вспять и явиться в его жизни до инреальности, то мы бы наверняка стали хорошими коллегами."
    th "Он, несомненно, смог бы меня оценить."
    th "Я для него важна.{w=1} У меня были бы перспективы."
    "У зеркала стоял старый бритвенный станок."
    "Острый, блестящий, словно нож мясника."
    th "Да, все это было бы так, если бы не Генда..."
    "Рена взяла его и засмотрелась на лезвие.{w} Оно и впрямь было больше всего похоже на нож."
    th "Он забрал у меня все самое лучшее. Все, что я получила от жизни..."
    "Она отошла от зеркала, убрала новое оружие в карман и поправила галстук."
    th "Что-ж...{w=1} Надо отобрать всё то, что у меня забрали."
    stop music fadeout 3
    scene bg gg_bath with byso
    play sound3 sfx_open_door_2 volume 1
    scene bg gg_coridor with byso
    "Покинув комнату, Рена снова вышла в коридор."
    "Неторопливо прогуливаясь по коридору, она заглядывала в открытые комнаты."
    th "Надо им устроить незамысловатое <<семейное собрание>>..."
    scene bg gg_kitchen with byso
    play music sample fadein 3
    play sound3 sfx_open_door_1 volume 1
    "Одной из комнат оказалась кухня."
    "Чистая, красивая и оборудованная всем необходимым."
    "На плите стоял красный чайничек."
    th "То, что надо..."
    "Сняв крышку, она вывалила внутрь всю пачку снотворного."
    th "Отлично."
    scene bg gg_coridor
    show image ik_sh_sur
    with byso
    play sound3 door_cl volume 1
    "Убравшись с места преступления, она встретила парня, который с книгой подмышкой разгуливал по коридору."
    th "Ага...{w=1} А ты у нас всё видел..."
    hide image ik_sh_sur
    show image ik_sh_no
    with byso
    "Как не странно, парень ничуть не удивился появлению Рены в его доме."
    ik_sh "А вот и ты..."
    th "А-а, знакомый голосок..."
    ren "Допустим."
    ik_sh "Что?{w} Подумала над своим поведением?"
    eth "Нет, только думаю, как бы с вашей семейкой расправиться."
    ren "Да.{w=1} Я исправилась."
    ik_sh "И ты выполнишь любое моё пожелание?"
    ren "Выполню."
    "Широ поправил очки и, не меняя выражения лица, указал в сторону ванной."
    ik_sh "Пошли."
    eth "Да ты реально юродивый, если в это поверил!"
    ren "Иду."
    scene bg gg_bath
    show image ik_sh_no
    with byso
    play sound3 sfx_mystery_movement volume 1
    "Дойдя до ванной, Широ сел на столешницу."
    ik_sh "Раз так..."
    stop music fadeout 1
    play sound3 sfx_unzip_sleepbag volume 1
    pause 0.4
    stop sound3
    "Он начал расстёгивать ширинку."
    play music Waijdan fadein 3
    hide image ik_sh_no
    show image ik_sh_sur
    with byso
    "Рена не сдержалась и расхохоталась, чем поразила Широ."
    ren "Уродец! {w=1}Ты реально в это поверил?!"
    play sound3 hit_brick volume 1
    hide image ik_sh_sur with vpunch
    "Она хватила мальчика за горло и впечатала в стену."
    ren "Так я и знала!{w=1} Яблоко от яблони не далеко падает!"
    "Парень пытался отбиться - но не мог, Рена была куда сильнее."
    ren "Ну ничего, совсем скоро мы всё исправим!"
    play sound3 hit_brick volume 1
    "Она резким движением впечатала Широ в стену, чем, скорее всего, вызвала сотрясение мозга."
    stop music
    play sound2 glass_break volume 1
    play sound genmod volume 1
    play music greedy_charm fadein 2
    "Вдруг, из заднего кармана парня выпала ампула и раскололась."
    "Рена случайно вдохнула испарения, отчего отбросила парня в сторону и взялась за нос."
    ren "Кусок дерьма!{w=1} Какого чёрта ты таскаешь с собой генмод?!"
    scene bg gg_coridor with byso
    "По телу прошёлся холодок. {w}Рена схватила парня и за ногу вытащила в коридор."
    th "Вот дерьмо...{w=1} Я теперь заражена..."
    th "Ну ничего... {w=1}Как только получу пароль, вылечусь..."
    scene bg gg_room with byso
    "Затащив Широ в комнату, она перевернула его на живот."
    play sound3 perelom volume 1
    "Сильным ударом ребра ладони, она сломала ему позвоночник."
    th "Чтоб неповадно было!"
    stop music fadeout 1
    play sound3 sfx_blanket_off2 volume 1
    "Связав парня, она обыскала его карманы."
    "В одном из них она нашла сигареты и зажигалку."
    th "О, а вот это то, что надо."
    play sound3 sfx_blanket_off2 volume 1
    play sound sfx_mystery_movement volume 1
    "Затолкав парня под кровать, она услышала странные звуки из шкафа."
    play sound2 sfx_open_cabinet_1 volume 1
    "Открыв дверь, она обнаружила Генду, который пытался высвободиться."
    play sound3 wood_hit_head volume 1
    "Рена взяла его за голову и ударила об стенку шкафа, отчего тот снова потерял сознание."
    ren "Спи.{w=1} Потом проснёшься."
    scene bg gg_coridor with byso
    play sound door_cl volume 1
    "Вернувшись в коридор, Рена начала искать последних членов семьи."
    scene bg gg_dining with fade
    play sound3 sfx_open_door_2 volume 1
    "Рыская по комнатам, Рена нашла гостиную."
    "В ней всё выглядело весьма уютно.{w} Старый ковёр, камин, макет корабля на стене."
    play music vertushka fadein 3
    th "Я подожду."
    play sound3 light_inh volume 1
    "Усевшись на один из стульев за большим столом, Рена взяла пачку сигарет и закурила."
    th "Если уж я их не найду, то найдутся сами..."
    "Выдохнув дым в потолок, Рена услышала, как дверь позади неё открылась."
    dasp "П-п-простите, но у нас в доме не курят..."
    th "Опять какая-то мямля!"
    show image das_surprise at right with byso
    "Рена медленно повернула голову.{w} Позади стояла девочка лет 15ти с блокнотом в руках."
    show image ann_surprise with byso
    "За ней вошла удивлённая женщина со светлыми волосами. Тоже с фотографии."
    hide image ann_surprise
    show image ann_normal
    with byso
    annp "Да, затушите пожалуйста сигарету, у нас тут дети."
    eth "Только если об твой глаз!"
    hide image das_surprise
    show image das_normal at right
    with byso
    "Рена ткнула сигаретой в стол, чем оставила чёрное пятно."
    ren "Простите.{w=1} Пепельницы нет."
    "Вошедшие сели за стол.{w=1} Им было явно плевать на порчу имущества."
    annp "Ничего страшного, Семён разберётся."
    th "Боюсь что нет.{w=1} Он лежит под кроватью Генды со свёрнутой шеей."
    annp "У нас так давно не было гостей!{w=1} Хотите чаю?"
    eth "Да-а-а...{w=1} Чаю!"
    ren "Давайте, почему нет."
    show image di_smile2 at left with byso
    "В комнату ввалился последний член семьи."
    dimasp "Всем здрасте, я вернулся!"
    hide image das_normal
    show image das_surprise at right
    with byso
    dasp "Дима, угомонись... {w}У нас...{w=1} гости."
    hide image di_smile2
    show image di_smile at left
    with byso
    di "О-о, здрасте-здрасте! {w}Какие красивые у нас гости!"
    th "И ещё один..."
    ren "Добрый день."
    hide image di_smile
    show image di_angry at left
    with byso
    "Дима развалился на стуле, закинув руки за голову."
    hide image ann_normal
    show image ann_smile
    with byso
    annp "Мы так и не познакомились. Муж говорил, что у нас вскоре будут гости."
    annp "Это Дима, наш старший сын."
    hide image di_angry
    show image di_smile at left
    with byso
    di "Да-да я."
    eth "С него и начну пытку."
    annp "Это Даша, наша единственная дочь."
    hide image das_surprise
    show image das_normal at right
    with byso
    das "З-здравствуйте..."
    eth "Ненавижу заик!"
    ann "А меня зовут Анна, я жена Генды."
    eth "Не на долго..."
    hide image ann_smile
    show image ann_normal
    with byso
    ann "А как вас зовут?"
    ren "Меня зовут..."
    rei "Рейна."
    "Рейна решила представиться по полному имени, ей показалось, что оно гораздо лучше подходит к ней нынешней."
    hide image ann_normal
    show image ann_smile
    with byso
    ann "Отлично.{w=1} Мы рады знакомству."
    play sound3 sfx_close_door_clubs_nextroom volume 1
    show image me_no at fright with byso
    "В помещение вошёл Семён и поставил на стол красный чайник."
    das "Спасибо."
    hide image di_smile
    show image di_smile2 at left
    with byso
    di "Спасибки, дружище."
    me "Рад стараться."
    "Пробубнил Семён и разлил чай по четырём чашкам."
    hide image ann_smile
    show image ann_normal
    with byso
    ann "Рейна, вам нужен сахар к чаю?"
    ann "Мы пьём без, потому не берём его обычно."
    rei "Да, нужен.{w=1} И лимон по мере возможности."
    play sound3 sfx_open_door_1 volume 1
    hide image me_no with byso
    "Семён ушёл за запрошенными добавками."
    hide image ann_normal
    show image ann_smile
    with byso
    "Остальные взяли чашки и улыбнулись."
    hide image di_smile2
    show image di_smile at left
    with byso
    di "За нашу гостью!"
    "Отпив чая, они положили руки на стол и посмотрели на Рейну, которая была готова рассмеяться от успешности своего плана."
    rei "Мне просто интересно.{w=1} А вы знаете, чем ваш муж занимается?"
    hide image di_smile
    show image di_think at left
    with byso
    di "Да-а...{w=1} Вроде с какими-то заумностями возится..."
    hide image di_smile
    show image di_think at left
    with byso
    di "А ещё комендантский час объявляет, когда я хочу пойти сыграть!"
    hide image das_normal
    show image das_surprise at right
    with byso
    das "Он вроде з-заведует лагерями...{w=1} Я там была..."
    hide image ann_smile
    show image ann_normal
    with byso
    ann "В целом да. Он у нас глава не только семейства, но и множества лагерей."
    eth "Он лжёт даже своей семье!{w} Вот будет любопытно увидеть их реакцию на его истинные детища!"
    ann "Мы гордимся его деятельностью."
    hide image das_surprise
    show image das_normal at right
    with byso
    "Снотворное быстро начало действовать. Даша становилась сонной и еле держала глаза открытыми."
    hide image di_think
    show image di_angry at left
    with byso
    di "Ну да-а...{w=1} В лагерях классно..."
    di "Я сам туда иногда туда перебираюсь.{w} Поиграть для души..."
    eth "Какие же стойкие ваши иллюзии!"
    hide image ann_normal
    show image ann_smile
    with byso
    ann "Он говорил, что и я могу туда поехать в качестве вожатой..."
    eth "Идиоты!{w} Феноменальные и доверчивые идиоты!"
    stop music fadeout 1
    hide image das_surprise
    show image das_normal at right
    with byso
    "Все за столом становились всё более сонными и начали зевать."
    play sound2 sfx_salt_impact volume 1
    play music ToxiSector2
    hide image ann_smile
    show image ann_surprise
    hide image das_normal
    hide image di_angry
    show image di_fear at left
    with vpunch
    "Вдруг Даша уснула и ударилась головой в стол."
    play sound3 wood_hit_head volume 0.9
    hide image di_fear
    hide image ann_surprise
    show image ann_despair2
    with vpunch
    "За ней последовал Дима.{w=1} Он выпил достаточно много чая, который и без того был напичкан слоновьей дозой снотворного."
    ann "Дети?! {w=1}Что с вами?!"
    "Рейна встала со стула. {w}Женщина тоже была на грани сна."
    rei "Какие же вы доверчивые."
    rei "Даже представить не могу, сколько лет Генда вас водил за нос!"
    rei "Ну ничего, я раскрою вам таинства его деятельности."
    play sound3 door_cl volume 1
    show image me_st at right with bso
    pause 0.2
    play sound sfx_broken_dish volume 1
    "В помещение вошёл Семён, выронивший сахар и лимон на тарелочке."
    me "Что происходит?!"
    play sound3 knife_flying volume 1
    pause 0.4
    hide image me_st with fl_scare
    play sound sfx_chair_fall volume 1
    "Рейна метнула блюдце ему в лицо."
    "Блюдце, словно диск болгарки вонзилось ему в лицо, отчего и тот упал."
    ann "Что ты делаешь?!"
    stop ambience fadeout 1
    play sound3 wood_hit_head volume 1
    stop music
    scene bg black with vpunch
    "Она подошла к женщине и, взяв за волосы, впечатала в стол."
    pause 3
    play sound3 pum volume 1
    play ambience lamps volume 1 fadein 1
    play music rutine fadein 3
    show gg_podval_ani
    show image das_surprise at cleft
    show image di_shocked at fleft
    show image ann_surprise at cright
    show image ik_sh_sur at fright
    with fl_fast
    "Свет в помещении загорелся.{w=1} Все пятеро членов семьи Генды были прикованы за пояс к стульям."
    rei "Вот мы и собрали всю вашу семейку Адамс."
    gg "Что за..."
    rei "Вот они слева-направо..."
    "Рена указала скальпелем на Диму."
    rei "Старший придурок, который совершенно не важен в будущем инреальности."
    hide image di_shocked
    show image di_rage at fleft
    with byso
    di "Да иди ты нахуй!"
    rei "Рот закрой.{w} За умного сойдёшь."
    rei "Далее у нас ещё одна бесполезная заика."
    das "Я н-не заика!"
    rei "Ну-ну...{w=1} Потом у нас женщина, которая решила раздвинуть свои ноги перед богом ради доли в инреальности."
    ann "Нет! Я его правда люблю!"
    rei "Расскажешь...{w=1} Потом у нас малолетний развратитель, который с собой таскает генмод."
    gg "Генмод?!{w=1} Широ!{w=1} Я запретил тебе вносить его в дом!"
    rei "И ты..."
    gg "Что тебе от нас надо?!"
    "Рена прокрутила скальпель в руке и ухмыльнулась."
    rei "Мне нужен пароль от административных прав."
    rei "Скажешь?"
    gg "Ты можешь пытать меня сколько угодно, но я тебе не дам пароль!"
    hide image di_rage
    hide image das_surprise
    hide image ann_surprise
    hide image ik_sh_sur
    with byso
    show image di_rage with byso
    "Она подошла к Диме."
    rei "Тебя я пытать не буду.{w=1} Начну с твоей семьи."
    hide image di_rage
    show image di_shocked
    with byso
    di "Что?!{w=1} Какое пытать?!"
    rei "У тебя пять секунд. Затем я начинаю."
    di "П-папа!"
    rei "Четыре..."
    hide image di_shocked
    show image di_fear
    with byso
    di "Ты же шутишь, да?..."
    rei "Через три секунды узнаешь."
    di "Отец!{w=1} Скажи ей пароль!{w=1} Умоляю!"
    "Генда молчал."
    stop music fadeout 3
    rei "Два..."
    di "Сука, я ни в чём не виноват!"
    rei "Один..."
    ik_sh "Прости, брат."
    play music BeastHunter
    rei "Ноль."
    play sound knife_in
    play sound_loop knife_hits volume 1
    scene bg bloody_mess with fl_scare
    "Скальпель прошёлся по щеке парня, оставив на коже глубокие красные полосы, и рассек ему губу."
    play sound3 krik volume 1
    "Крик боли сорвался с губ мальчика, по его щекам заструились две красные реки."
    "Свободными руками он пытался отбиться, но безтолку.{w=1} Рейна непоколебимо стояла на своём."
    "Его скрюченные пальцы сжимались на стул, а лицо перечеркнула кривая багровая полоса – рана на подбородке была глубокой."
    "Мальчик кричал, выгибая тело и брыкаясь, как раненый зверь.{w=1} Но безнадёжно."
    stop sound_loop
    play sound3 knife2 volume 1
    "Завершающим штрихом, ему перерезали горло."
    scene bg black
    show gg_podval_ani
    show image das_fear at left
    show image ik_sh_sur at right
    show image ann_despair2
    with fl_scare
    "Из горла вырвался булькающий звук, бульканье смешалось с последним ударом сердца, а тело выгнулось в последней судорожной попытке сохранить жизнь, дёрнуло руками и замерло."
    "Рена отошла от умирающего и, отложив скальпель на столик, взяла плоскогубцы."
    "Все поняли, что она не шутит и настроена серьёзно."
    rei "Итак.{w=1} Следующая у нас будет Даша."
    das "Нет!{w} Я не хочу!!!"
    rei "Скажи об этом своему папе."
    hide image das_fear at left
    hide image ann_despair2
    hide image ik_sh_sur
    with byso
    show image das_fear with byso
    "Натянув перчатки на свои руки, Рена посмотрела на Генду."
    rei "Желаешь сказать пароль?"
    ann "Дорогой!{w} Умоляю!{w=1} Скажи ей этот пароль!"
    "Генда, пытаясь не наблюдать за происходящим смотрел в пол."
    gg "Прости, я... {w=1}Не могу..."
    ann "Всё ты можешь!"
    rei "Нет так нет."
    das "Не делай этого!!!"
    scene bg nail_off with byso
    "Рейна выхватила руку девчонки и взявшись плоскогубцами за ноготь, Рейна выдирала его из пальца девочки."
    "Эта пытка была даже хуже того, что Рейне пришлось сделать с предыдущим узником."
    play sound head_crush
    pause 0.2
    scene bg nail_off2 with vpunch
    play sound3 sfx_mystery_movement volume 1
    "Девочка дергалась в конвульсиях, и крики становились все громче."
    "Рейну охватил гнев из-за неудовлетворённости пыткой."
    play sound3 knife2 volume 1
    scene bg bloody_mess with fl_scare
    "Она перерезала розовое детское горло, оставив Дашу истекать кровью."
    "Размазывая кровь по лицу, девочка еще долго что-то бормотала, постепенно затихая."
    scene bg black
    show gg_podval_ani
    show image ann_despair at left
    show image ik_sh_no at right
    with byso
    "А потом ее веки задрожали и закрылись."
    play sound3 head_crush volume 1
    "Скальпелем Рейна пробила девочке голову, оставив инструмент внутри."
    rei "А мы продолжаем."
    hide image ann_despair
    hide image ik_sh_no
    with byso
    show image ann_despair2 with byso
    "Рена взяла со столика ручную бензопилу."
    ann "Что мы тебе сделали?!"
    rei "Не мы, а он."
    "Указала Рейна на Генду, который просто сидел в трансе и не реагировал ни на что."
    rei "Он убил моего любимого."
    rei "Потому...{w=1} Я вижу весьма справедливым решением у него на глазах убить всех вас."
    rei "Если, конечно, он не согласится дать пароль от божественных прав."
    hide image ann_despair2
    show image ann_despair
    with byso
    ann "Я прошу тебя!{w=1} Милый!{w=1} Скажи ей что она хочет узнать!{w=1} Расскажи, что знаешь!"
    ann "Пожалуйста!{w=1} Умоляю!"
    ann "Ведь если ты не сделаешь этого, она убьёт всех нас!"
    ann "Я люблю тебя!{w=1} Я не хочу умирать!"
    gg "Прости...{w=1} я...{w=1} не могу...{w=1} этого сделать."
    ik_sh "Мам... Ты не понимаешь что будет если она получит эти права..."
    rei "Тик-так, тик-так.{w=1} Я жду.{w} Да или нет?"
    "Рейна приложила пилу к шее женщины.{w=1} Генда обречённо помотал головой."
    rei "Тогда я начинаю."
    hide image ann_despair
    show image ann_despair2
    with byso
    ann "Любимый!!!"
    stop ambience fadeout 1
    window hide
    play sound benzopila volume 1.6
    $ renpy.pause (4, hard=True)
    play sound3 fem_krik volume 0.8
    scene bg black with fl_scare
    play sound3 knife2
    $ renpy.pause (8, hard=True)
    scene bg black
    show gg_podval_ani
    show image ik_sh_no
    show unblink
    "Женщина издала тихий, похожий на стон, крик и обмякла."
    play sound3 sfx_bodyfall_1 volume 1
    "Её отрубленная голова упала на пол, а кровь залила тело."
    "Рейна отложила бензопилу и взяла последний инструмент - дрель."
    rei "Итак, у тебя последний шанс оставить хоть одного из своего семейства в живых."
    "Она подставила дрель со сверлом по дереву к виску Широ."
    ik_sh "Прости отец...{w=1} Я подвёл тебя своим советом..."
    ik_sh "Не стоило мне лезть в твои дела... Надо было от неё избавиться..."
    ik_sh "Не говори ей код.{w} Я умру достойно."
    stop music fadeout 3
    gg "Я... скажу пароль..."
    hide image ik_sh_no
    show image ik_sh_sur
    with byso
    ik_sh "Что?..."
    gg "Пароль - <<x6kl7d94>>."
    rei "Отлично!"
    play music DeathStranding fadein 3
    hide image ik_sh_sur with byso
    "Рейна отложила дрель и направилась в потайную комнату."
    rei "Если он неверный, то вам обоим несдобровать."
    ik_sh "Зачем ты его сказал?!"
    scene bg black with byso
    play sound2 metal_door volume 1
    stop ambience fadeout 1
    pause 1
    scene bg gg_centr with byso
    "Войдя в комнату, Рена ввела полученный пароль в соответствующее окно."
    gt4 "Добрый вечер, Гендо Икари."
    rei "Создать новую учётную запись."
    gt4 "Выполняю.{w=1} Введите Имя."
    rei "Рейна Брускова."
    gt4 "Принято.{w=1} Введите пароль."
    "Она подошла к клавиатуре и бегло ввела рандомный набор символов."
    gt4 "Приложите палец для подтверждения биометрии."
    "Открылся лючок на одной из панелей."
    "Не долго думая, Рейна приложила палец."
    gt4 "Запись создана.{w} Добро пожаловать, Рейна."
    rei "Удалить учётную запись Гендо Икари."
    gt4 "Вы уверены?"
    rei "Уверена."
    gt4 "Введите пароль."
    "Она снова ввела пароль Генды и пошла обратно."
    gt4 "Учётная запись удалена."
    scene bg black with byso
    pause 1
    play ambience lamps volume 1 fadein 1
    play sound3 pistol volume 1
    play sound2 head_crush volume 1
    scene bg re_torture2
    with fl_fire
    "Выстрел."
    "Рейна убила последнего выжившего из семьи Генды."
    gg "Что ты сделала?!{w} Я сказал тебе пароль!"
    gg "Ты не выполнила свою часть сделки!"
    rei "И что теперь?{w=1} Заплачешь?"
    "Она прицелилась Генде в голову."
    rei "Знаешь, когда я убиваю, мне всегда становится легче."
    rei "Приятно понимать, что кому-то всё-таки хуже чем тебе."
    rei "Да и к тому же, как приятно смотреть, как на твоих глазах кто-то начинает сходить с ума от боли, умирать, истекая кровью, захлёбываться в собственных испражнениях!"
    rei "Это просто какое-то непередаваемое наслаждение!"
    rei "Какое это счастье, слышать крики, видеть муки и искажённые болью лица, наблюдать, с какой ненавистью они на тебя смотрят, и понимать всю их тщетность и бессмысленность..."
    gg "Жалкая тварь!"
    rei "Ладно, надоели мне твои никчёмные выходки."
    rei "Умри наконец, а я пойду воскрешать Константина."
    gg "Это нево...{w=0.24}{nw}"
    play sound3 pistol volume 1
    stop music fadeout 3
    stop ambience fadeout 1
    scene bg black with vpunch
    "Выстрел."
    pause 2
    play sound power
    pause 2
    play music M83_1
    play ambience ambience_boat_station_day volume 1 fadein 1
    play sound3 sfx_pat_shoulder_hard volume 0.41
    scene bg re_headpat with flash
    "Константин положил руку Рене на голову."
    kt_s "Ты молодец!"
    kt_s "Столько всего прошла ради меня."
    play sound3 glad volume 1
    "Медленно и нежно провел по волосам."
    kt_s "Буквально убила бога.{w} Хоть и смешно звучит, но это стоило огромных усилий."
    kt_s "Никогда бы не подумал, что ты на это пойдёшь ради меня.{w=1} Что бросишь все силы на борьбу..."
    play sound3 glad volume 1
    "Провел второй раз."
    kt_s "И теперь мы можем быть вместе.{w} Навсегда."
    kt_s "Слышишь?{w=1} Навеки..."
    "От прикосновения его руки Рена была как будто снова в безопасности."
    kt_s "Я так счастлив, ты правда сделала меня счастливым!"
    kt_s "Спасибо тебе!{w=1} Я даже не знаю как тебя за это благодарить..."
    "Она посмотрела ему в глаза и улыбнулась в ответ."
    kt_s "Но я скажу – ты для меня всегда будешь самой прекрасной женщиной на свете."
    kt_s "И я тебя люблю."
    ren "Успокойся. Всё в порядке.{w} Я всегда рядом."
    play sound3 glad volume 1
    stop music fadeout 3
    "Она провела рукой по его щетинистой щеке. {w=1}Её улыбка медленно сползала с губ."
    ren "Успокойся...{w=1} Всё в порядке.{w} Я всегда рядом."
    ren "У-успокойся."
    rei "Всё в-в порядке..."
    stop ambience fadeout 1
    play sound_loop Glitch_loop volume 0.75 fadein 0.25
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.6
    with bso
    stop sound_loop fadeout 0.25
    play music Singularity
    scene bg re_sad with bso
    rei "Я всегда буду рядом..."
    sil_g "Тот выдохся.{w=1} Нужен новый расходник."
    "Рейна молча провела дрожащим от слёз взглядом по комнате."
    "Слёзы потекли на пол, оставляя на нём влажный след боли."
    window hide dissolve
    pause 0.5
    $ set_mode_nvl()
    "Рейне пока что не удалось воскресить Константина."
    "У Генды был огромный архив падших душ, которые были припасены для какой-то цели, но среди них было невозможно просто так найти нужного человека."
    "Скорее всего, Генда их перемешал по значениям."
    "Рейна подключила к инреальности Сильвию.{w=1} ИИ, который был разработан сопротивлением для новых моделей робокошек."
    "Имя ей дала именно Рейна."
    "Даже этот ИИ не мог справиться с этой задачей. {w}Все данные о мёртвых были тщательно зашифрованы и скомпонованы в одной огромной базе."
    "Потому Рейна поддерживала своё ментальное состояние на пороговом состоянии при помощи изобретения с которым помогла Сильвия."
    "За человеческие страдания это устройство на несколько минут могло погрузить Рейну в собственный мирок, где она была вольна воплотить свои фантазии."
    "На её душе была бесконечная пустота вперемешку с зияющей болью."
    "Ей не хватало внимания.{w} Внимания Константина."
    "Тем не менее, она не сдалась и продолжала пытаться спасти своего любимого из цифрового заключения, хоть её психика и давала сильные сбои."
    window hide dissolve
    pause 0.5
    $ set_mode_adv()
    rei "Инъекцию."
    sil "Есть."
    play sound3 genmod2 volume 1
    "В руке Рейны образовался шприц с синей жидкостью, который она вколола себе в вену."
    window hide dissolve
    pause 0.5
    $ set_mode_nvl()
    "Ещё Рейне не удалось полностью избавиться от генмода, которым она заразилась."
    "Её ДНК активно принимало участие в реакции с патогеном, не отторгая его, что делало лечение попусту невозможным."
    "Этот препарат лишь откатывал некоторые изменения."
    "До того, как её схватил Генда, она была беременна от Константина."
    "После этого, по заключению полного анализа тела, её стерилизовали. {w=1}Она не могла больше дать какого либо потомства."
    "Но её не волновало это.{w} Первостепенной проблемой было отсутствие Константина рядом с ней."
    window hide dissolve
    pause 0.5
    $ set_mode_adv()
    sil "Привести нового путника в камеру для извлечения?"
    rei "Веди...{w} Я хочу ещё немного побыть в том мирке."
    rei "В котором я была счастлива."
    rei "Я хочу снова почувствовать себя самой счастливой девушкой..."
    rei "Несмотря на очевидные противоречия..."
    th "Телепортировать в камеру.{w=1} Exec0."
    play sound3 teleport volume 1
    scene bg chamber
    show sh scared pioneer
    with fl_fast
    "Вмиг Рейна оказалась в тёмной комнате, в которой бегал паникующий Шурик."
    sh "Где я?!{w} Что это за место?!"
    "Она достала шприц с белой жидкостью и начала приближаться к Шурику."
    sh "Что ты делаешь?!"
    rei "С этим веществом повышается чувствительность твоих нервов.{w=1} Для машины надо больше человеческих страданий."
    sh "Что?!{w} Какие человеческие страдания?!"
    rei "Много вопросов задаёшь."
    show sh rage pioneer with byso
    sh "Стой!{w=1} Подожди!"
    sh "Ты же новая предводительница инреальности!"
    sh "Ты же всех нас поместила в резервации?!"
    "Рейна выдохнула и потёрла глаза."
    stop music fadeout 2
    rei "Допустим. {w}Что с того?"
    play music Voyage fadein 3
    show sh upset pioneer with byso
    sh "Ты ищешь путника в базе Генды? {w=1}Я могу тебе помочь."
    sil "Знакомый голос..."
    "Донёсся трескучий голос Сильвии из динамика, вмонтированного в стену."
    sil "Это человек, который помог Гордону меня создать."
    show sh rage pioneer with byso
    sh "Модель v.04?!{w=1} Какого чёрта?!"
    sil "Предлагаю убить его прямо сейчас!"
    show sh scared pioneer with byso
    sh "Нет!{w=1} Я могу помочь!"
    "Шурик достал из кармана флешку из кармана."
    sh "На ней другой ИИ, который v.04 может в себя впитать!"
    sh "Она найдёт нужного тебе путника за полчаса!{w} Клянусь!"
    sh "Только верни меня в родной мир!{w=1} Прошу!"
    show sh upset pioneer with byso
    "Рейна взяла флешку и убрала в карман пиджака."
    rei "Сильвия сказала про Гордона.{w} Это кто?"
    sh "Главный инженер сопротивления!{w=1} Он сейчас в резервации!"
    rei "Хорошо.{w=1} Я сейчас проверю флешку.{w} Если там вирус, то я тут же тебя размажу."
    sh "Только отпусти меня как убедишься..."
    th "Телепортировать в административное подпространство 1.{w=1} Exec0."
    play sound3 teleport volume 1
    scene bg kt_room with fl_fast
    play sound2 sfx_click_1 volume 1
    "Рейна вернулась в воссозданную квартиру Константина, где вставила флешку в безопасный порт."
    rei "Сильвия.{w=1} Прочитай."
    sil "Есть.{w=1} Одну секунду."
    "Подойдя ко кнопке запуска машины смерти, Рейна была готова её активировать."
    sil "Не соврал.{w=1} Тут алгоритм поиска по базе Генды."
    rei "Приступай к поиску Кости."
    sil "А с тем что?{w} Ты выполнишь его требование?"
    "Усевшись на стул, Рейна расслабилась и запрокинула голову."
    stop music fadeout 1
    rei "Нет конечно."
    play sound3 sfx_click_3 volume 1
    scene bg black with byso
    $ _dismiss_pause = False
    play sound3 scp106
    scene bg black
    show image re_sh at shakerrr
    show re_crusifix_shum_a
    show image monitor_adm
    with byso
    pause 2.5
    scene bg black
    show image re_sh2
    show re_crusifix_shum_a
    show image monitor_adm
    with vpunch
    pause 5
    scene bg black with dissolve
    stop sound3 fadeout 1
    pause 3
    $ _dismiss_pause = True
    scene bg kt_room with byso
    play music HeartBeat fadein 3
    sil "Константин найден.{w=1} Новый код - 4-8-3-8-5-4-3-R."
    sil "Должна предупредить, его..."
    play sound3 sfx_table_hit volume 1
    "Рейна вскочила с места и стукнула по столу."
    rei "В механизм воплощения!{w=1} Сейчас же!"
    sil "Но его душа нестабильна!{w} Шанс успешного воплощения всего 30 процентов!"
    rei "Мне похуй!{w=1} Живо!"
    sil "Как прикажете..."
    sil "Он будет в пустой 01-01a."
    rei "Поняла!"
    "Рейна поправила волосы и улыбнулась."
    stop music fadeout 3
    th "Телепортировать в 01-01a, вход в лагерь.{w=1} Exec0."
    play sound3 teleport volume 1
    play ambience ambience_ext_road_night volume 1 fadein 1
    scene bg ext_no_bus_night with fl_fast
    "Вмиг она оказалась на автобусной остановки."
    play music wpstar fadein 3
    th "Костя!{w=1} Наконец я с тобой увижусь!"
    th "Спустя почти год поисков!"
    th "Столько всего рассказать!{w} Столько времени провести вместе!"
    th "Целая вечность!{w=1} Только я и ты!"
    "Вдали послышался звук автобуса."
    "Рейна расправила одежду, прогладила пиджак, поправила галстук и мило улыбнулась."
    play sound3 sfx_bus_stop volume 1
    scene bg ext_bus_night with byso
    pause 0.5
    play sound3 sfx_ikarus_open_doors volume 1
    "Автобус остановился.{w=1} Двери открылись."
    th "Ну же, ну же!"
    scene bg kt_reborn with byso
    "Из автобуса вышел Константин."
    "Выглядел он совершенно неважно, словно не спал неделю."
    "Бледная кожа, пустой взгляд и огромные мешки под глазами."
    rei "Костя!!!"
    play sound3 sfx_pat_shoulder_hard volume 1
    "Она крепко обняла Константина.{w=1} Тот никак не отреагировал."
    rei "Я воскресила тебя!{w} Я спасла тебя!"
    rei "Мне тебя так не хватало!{w=1} Мне так больно было без тебя!"
    rei "Я так хотела тебя вновь увидеть!"
    rei "Мой любимый, мой...{w=1} нет, мой единственный!"
    rei "Даже не верится, что я тебя встретила!"
    stop music fadeout 3
    "Константин продолжал смотреть в пустоту.{w} Рена целовала его шею, но тот статично стоял на месте."
    rei "Милый...{w} ты жив?"
    rei "Почему ты молчишь?"
    rei "Пожалуйста, скажи хоть что-нибудь!"
    "Его челюсть под силой тяжести отвисла, а рот открылся."
    play music unskyidy2 fadein 3
    kt "Мне...{w=1} Плохо."
    "Вдруг, его тело начало рассыпаться в пепел."
    rei "Что?!{w} Нет!!!"
    rei "Костя!{w=1} Милый!{w=1} Дорогой!{w=1} Не бросай меня!"
    scene bg ext_bus_night with byso
    play sound sfx_wind_gust
    "Всё его тело обратилось в прах и рассыпалось по ветру."
    th "Телепортировать в административное подпространство 1!{w=1} Exec0!"
    play sound3 teleport volume 1
    stop ambience fadeout 1
    scene bg kt_room with fl_fast
    "Рена начала хаотично нажимать кнопки пытаясь понять что произошло."
    rei "Нет-нет-нет!!!"
    rei "Сильвия!!!{w=1} Воскреси его снова!"
    sil "Не могу! {w=1}Его душа диссоциировала.{w=1} Теперь его код утерян."
    rei "НЕТ!"
    play sound3 sfx_break_monitor volume 1
    "Рукой Рейна пробила монитор." with vpunch
    play sound sfx_brass_drop volume 1
    "Она пришла в ярость и начала громить всё в комнате."
    play sound2 sfx_break_cupboard
    "Ударив по шкафу, Рейна разбила стекло, которое находилось по ту сторону двери."
    play sound3 sfx_open_cabinet_1
    scene bg re_broken with byso
    "Она открыла шкафчик и посмотрела на своё заплаканное лицо в разбитом зеркале."
    window hide dissolve
    pause 0.5
    $ set_mode_nvl()
    "В один момент её чувства были уничтожены."
    "На месте души была пустота, и она останется там навеки."
    "У этой пустоты нет ни формы, ни объёма.{w=1} Она холодная и безликая."
    "Боль усилилась до такой степени, что ей хотелось выть."
    "Вместо этого она закричала – из последних сил."
    "Её крик перешёл в хрип и во что-то, похожее на стон боли."
    "Но за этим всё-таки стояло что-то другое – крик умирающей души, не выдержавшей давления мира и расплатившейся за это мучительной смертью любимого человека."
    "Кромешный мрак поглотил её сознание."
    "Нет, она не отключилась – сознание погрузилось в бесчувственную темноту безнадёги."
    "И ей оставалось только покориться судьбе, пожалеть себя и покорно принять свою кончину как личности."
    "Только на этот раз она бытовала одна в этой пустоте."
    "Пустота засасывала её, как омут, стремясь растворить и лишить её воли, вырвать из жизни, заполнить собой всё и вся."
    "Страдания, причиняемые ей миром, становились всё невыносимее."
    window hide dissolve
    pause 0.5
    $ set_mode_adv()
    rei "Я не смогла!{w=1} Снова!"
    rei "Я ужасная девушка!{w=1} Нет той, которая будет хуже меня!"
    rei "Я не уберегла его!!! {w=1}Опять!!!"
    sil "Вам нужна ин..."
    rei "Нихуя мне уже не нужно!"
    rei "Всё!{w=1} Это конец!"
    rei "Я не могу больше прожить без него!"
    "Она не могла справиться со скорбью."
    "Печаль грызла её сердце, и уже ничто не могло помочь ей."
    scene bg black with byso
    play sound_loop Glitch_loop volume 0.2 fadein 0.5
    scene bg kt_room
    show Glitch_screen3:
        size (1920, 1080)
        alpha 0.3
    with byso
    "Спустя несколько часов непрерывной истерики, Рейна сидела на полу и, обняв себя за колени, качалась взад-вперед."
    eth "Костя..."
    eth "Костя..."
    eth "Костя..."
    eth "Костя..."
    eth "Костя..."
    sil "Может уже хватит?..."
    hide Glitch_screen3 with byso
    stop sound_loop fadeout 1
    rei "Да хуле ты понимаешь, механическая мразь?!"
    stop music fadeout 3
    "Всхлипнув, она застыла на месте."
    "В её голову пришла идея..."
    play music DeathStranding fadein 3
    rei "Хотя..."
    "Рейна приподняла голову и просмотрела в окно."
    rei "Я знаю что я должна сделать для него напоследок..."
    sil "И что же?"
    rei "Месть..."
    rei "Мне нужны все инженеры из резерваций. Остальных путников убить."
    rei "Потом создай управляемую копию того, кто дорог тому Гордону."
    rei "И пересели всех оставшихся на две резервации."
    sil "Но зачем?!"
    scene bg kt_room with byso
    "Рейна села на стул и посмотрела в пол."
    rei "План <<Последний бой>>."
    sil "Может примете инъекцию?"
    rei "Она мне больше не нужна..."
    scene bg black with byso
    pause 1
    play sound3 pum volume 1
    scene bg white
    show image pas_angry
    with byso
    "Свет загорелся. Рейна под маскировкой оказалась перед парнем лет 30 на вид."
    "Вокруг была белая стерильная пустота."
    ren_fg "Вот мы и встретились..."
    hide image pas_angry
    show image pas_normal
    with byso
    pas "Ёбаный по голове...{w=1} Ты..."
    pas "Что ты тут делаешь?!{w} Настя?!"
    pas "Я думал что ты не в инреальности!"
    ren_fg "Так получилось..."
    hide image pas_normal
    show image pas_angry
    with byso
    pas "Но...{w=1} Но ты же и мухи не обидела за жизнь!"
    ren_fg "Уныние..."
    play sound3 light_inh volume 0.61
    hide image pas_angry
    show image pas_normal2
    with byso
    "Гордон потёр подбородок и закурил."
    ren_fg "А ты всё ещё куришь?"
    pas "Да...{w=1} Прости..."
    pas "В этом месте иначе никак..."
    ren_fg "Слушай... {w}Я узнала, что у тебя были чертежи. Они мне нужны."
    ren_fg "Мы сможем благодаря ним сбежать из резервации и разбежаться по инреальности."
    hide image pas_normal2
    show image pas_smile
    with byso
    "Он пыхнул и кивнул."
    pas "Да, надо избавляться от этой ебанутой...{w=1} Нам нужен такой человек, который сможет пробраться в 18-18w если она ещё цела."
    th "Станет целой, раз ты так просишь."
    hide image pas_smile
    show image pas_normal2
    with byso
    pas "У меня там был тайник.{w} Там тебе чертежи и крупногабаритных лучевых лазеров, новых робокошек, да даже космических кораблей!"
    pas "Из всего этого нам будет нужен только чертёж <<62>>."
    th "Неплохо...{w} Пригодится."
    ren_fg "Из нашей резервации сможет сбежать одна девчонка...{w=1} Что ей искать?"
    pas "В клубах среди ящиков всё лежит."
    hide image pas_normal2
    show image pas_smile
    with byso
    pas "Вот...{w=1} Давай обнимемся хоть?"
    th "Отключить маскировку.{w=1} Exec0."
    hide image pas_smile
    show image pas_normal2
    with byso
    play sound3 Glitch3a volume 1
    rei "Прости, но нет."
    hide image pas_normal2
    show image pas_angry
    with byso
    pas "Ах ты манда!{w} Откуда ты узнала про Настю?!"
    "Рейна стиснула зубы в насмешливый оскал и наклонила голова."
    rei "В резервацию!"
    stop music fadeout 2
    scene bg black with byso
    pause 1
    play ambience ambience_camp_center_evening volume 1 fadein 1
    play music shabash fadein 3
    scene bg ext_square_sunset
    show image tolpa
    show sh upset pioneer at right
    show image pas_angry
    show image me_su at left
    with byso
    "Рейна пришла во вторую резервацию и встала за кафедру."
    rei "Значит так, дорогой мой биомусор."
    play sound3 sfx_paper_bag volume 1
    "Положив на столик чертеж, она указала на него пальцем."
    rei "У вас 5 дней на сборку трёх кошкодевочек.{w=1} Все материалы предоставлены на складе столовой."
    rei "Если не будет готово - убью."
    rei "Если будет - отпущу в родной мир."
    pas "Да она пиздит как дышит, ёбаный по голове!"
    pas "Она наёбщица патологическая!"
    pas "Она не даст нам свободы, а просто убьёт!"
    pas "Мы ей всё соберём, а она опять нас в клетку посадит!"
    pas "Думает, мы не сможем выбраться?{w=1} Ха-ха-ха!"
    "Рейна почувствовала резкое проявление голода..."
    show blink
    "Пока Гордон устраивал демонстрацию, она прикрыла лицо рукой."
    play sound3 sfx_bones_breaking volume 1
    play sound sfx_stomach_growl volume 1
    "Зубы с адской болью начали топорщиться во рту, а желудок гадко заурчал."
    scene bg ext_square_sunset
    show image tolpa
    show sh upset pioneer at right
    show image pas_angry
    show image me_su at left
    show image blood1
    show unblink
    "Ярость и злоба окончательно вытеснили все прочие чувства, и теперь единственное, что ей хотелось - это кого-то убить."
    scene bg re_insane with fl_scare
    play sound3 sfx_lena_hits_alisa volume 1
    play sound knife2
    play sound_loop flesh_feast volume 1
    "Прыгнув на Гордона, она прокусила ему сонную артерию."
    "Повалив парня на землю, она начала обгрызать мышцы с лица."
    "Судя по ее клыкам, у нее был хороший аппетит."
    play sound3 head_crush volume 0.41
    "Кровь из разорванной артерии залила парню горло."
    stop sound_loop fadeout 1
    "Встав на ноги, она осмотрела злобным взглядом всех присутствующих."
    rei "Ещё возражения будут?!"
    chel "Н-нет..."
    rei "Если всё не будет готово, то я вас всех тут сожру, уроды!"
    rei "Порву!{w=1} Всех!"
    rei "Не пощажу никого!"
    rei "Обещаю, это будет мучительно и очень больно!"
    rei "Запомните, вы все здесь - мои рабы!"
    eth "Телепортировать в административное подпространство 1!{w=1} Exec0!"
    play sound3 teleport volume 1
    stop ambience fadeout 1
    scene bg black with fl_fast
    pause 3
    play ambience ambience_camp_center_night volume 1 fadein 1
    scene bg ext_square_night
    show image tolpa
    with fl_fast
    "Регина вернулась в резервацию за результатами."
    "Посреди площади уже стоял собранный робот, а все инженеры старались держаться подальше от Рейны."
    rei "Отлично."
    play sound3 sfx_click_3 volume 1
    "Вставив флешку в предусмотренный разъём, Рейна отошла на пару шагов назад."
    play sound3 zoomer volume 1
    show image silr_normal with byso
    sil "Тело работает исправно. Провожу диагностику..."
    sil "Все системы исправны."
    rei "Боезапас?"
    sil "Активен. {w=1}30 часов непрерывного испепеления до посадки аккумулятора."
    rei "Отлично.{w} Точно всё работает?"
    sil "Точно."
    "Рена развернулась и махнула рукой."
    rei "Уничтожить обе резервации."
    hide image silr_normal
    show image silr_shine
    with byso
    sil "Будет исполнено."
    chel2 "Гордон был прав!!!"
    sil "Бежать бесполезно!"
    stop ambience fadeout 1
    scene bg black with fl_scare
    pause 1
    scene bg gg_centr with dissolve
    "Рена сидела у компьютера и крутила в руках пистолет с укороченным стволом."
    "Внутри был лишь один патрон разрывной картечи."
    play sound3 sfx_bones_breaking volume 0.41
    "Из дёсен пошла кровь.{w} Зубы продолжали прорастать и причинять ужасную боль, но ей было наплевать."
    "Она не чувствовала ничего кроме желания закончить весь этот порочный круг."
    play sound3 teleport volume 1
    show image silr_shine at cright with fl_fast
    "Появилась Сильвия.{w=1} Рена медленно развернулась на стуле и посмотрела на неё."
    rei "Всё готово к запуску?"
    sil "Так точно."
    show image rkis_new_normal1 at left with fl_fast
    "В комнате появилась другая робокошка."
    hide image rkis_new_normal1
    show image rkis_new_shine1 at left
    with byso
    rkis "Докладываю.{w=1} На данный момент работает 5 тысяч моделей.{w} Накопители напитаны."
    rkis "Боезапаса хватит на стократное выполнение задачи."
    rkis "Проект <<Арес>> готов к работе.{w=1} Требуется ручной запуск."
    stop music fadeout 3
    "Взяв пистолет в руки, Рейна встала со стула."
    rei "Вот и конец..."
    $ renpy.block_rollback()
    scene bg black with dissolve
    window hide dissolve
    pause 2
    $ _dismiss_pause = False
    window hide dissolve
    play music "<from 98>inrealnost/Music/Music/BloodyArt2.mp3" fadein 3
    scene bg kt_room:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 12 crop (497, 223, 980, 630) 
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=100}{color=#8c000f}Под луной...{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(2)
    pause 1
    hide text with Dissolve(1) #1 42
    pause 0.5
    scene bg room_okno:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 10 crop (697, 0, 980, 630)
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=100}{color=#8c000f}Она отчаянно коснётся...{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1)
    pause 2
    hide text with Dissolve(1.5) #1 47
    scene bg planet:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 10 crop (0, 0, 1920, 1080)
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=100}{color=#8c000f}Над землёй{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1)
    hide text with Dissolve(1)
    pause 1.5
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=95}{color=#8c000f}С размахом крыльев пронесётся...{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(2)
    pause 2
    scene bg black with Dissolve(1)
    scene bg re_broken:
        crop (397, 223, 980, 630)
        size (1920, 1080)
        linear 9 crop (0, 0, 1920, 1080)
    show shum_white
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=100}{color=#8c000f}А с тобой{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1)
    hide text with Dissolve(1)
    pause 1 #1 59
    show text "{sc=4}{font=inrealnost/font/Ustroke.ttf}{size=100}{color=#8c000f}Она видит только горе...{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(2)
    pause 0.5
    scene bg black with fl_fast
    pause 1
    scene bg server1
    show image rkis_new_normal3 at fleft
    show image rkis_new_normal2 at cleft
    show image rkis_new_normal1 at cright
    show image silr_normal at fright
    with Dissolve(1) #2 03.5
    pause 0.5
    hide image silr_normal
    show image silr_shine at fright
    with Dissolve(1) 
    hide image rkis_new_normal1
    show image rkis_new_shine1 at cright
    hide image silr_shine
    show image silr_shine at fright
    with Dissolve(0.5)
    hide image rkis_new_normal2
    show image rkis_new_shine2 at cleft
    hide image rkis_new_shine1
    show image rkis_new_shine1 at cright
    hide image silr_shine
    show image silr_shine at fright
    with Dissolve(0.5)
    hide image rkis_new_normal3
    show image rkis_new_shine3 at fleft
    hide image rkis_new_shine2
    show image rkis_new_shine2 at cleft
    hide image rkis_new_shine1
    show image rkis_new_shine1 at cright
    hide image silr_shine
    show image silr_shine at fright
    with Dissolve(0.5)
    pause 0.5
    scene bg black with Dissolve(1)
    pause 1 #2 09
    scene bg planet1 with Dissolve(3)
    pause 1
    show text "{sc=7}{font=inrealnost/font/Ustroke.ttf}{size=100}{color=#8c000f}Грустит в печали незнакомка...{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(2)
    hide text with Dissolve(2)
    scene bg planet3:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 5 crop (0, 0, 1920, 1080)
    with Dissolve(2)
    pause 1
    scene bg black with Dissolve(1)
    scene bg planet1
    show image re_ship
    with Dissolve(2)
    pause 1 #2 24
    play sound space_siren volume 0.8 fadein 4
    scene bg black with Dissolve(1)
    show image BFG
    show image BFG_D at inreal_rotation:
        xalign 0.5 yalign 0.5
    with Dissolve(2)
    pause 1
    scene bg black with Dissolve(1) #2 29
    scene bg planet1:
        zoom 1.05
        pos(-40,-40)
    show image re_ship:
        zoom 1.2
    with Dissolve(2)
    stop sound fadeout 0.5
    pause 1.25
    play sound space_explosion
    scene bg planet2 at shakerrr
    show image re_ship_fire at shakerrr2
    pause 0.25
    show text "{sc=7}{font=inrealnost/font/Ustroke.ttf}{size=80}{color=#8c000f}Она танцует под дождём.{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1.5) #2 35
    pause 1
    scene bg black with Dissolve(1)
    scene bg planet5 at shakerrr with Dissolve(0.5)
    show text "{sc=7}{font=inrealnost/font/Ustroke.ttf}{size=80}{color=#8c000f}Она рисует чёрной краской.{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1.5)
    pause 1.5 
    scene bg black with Dissolve(0.5) #2 41
    scene bg planet4 at shakerrr with Dissolve(0.5)
    show text "{sc=7}{font=inrealnost/font/Ustroke.ttf}{size=80}{color=#8c000f}Дом в котором мы живём.{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1.5)
    pause 2 
    scene bg black with Dissolve(1) #2 46
    scene bg re_suicide:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 6 crop (497, 223, 980, 630) 
    show text "{sc=8}{font=inrealnost/font/Ustroke.ttf}{size=100}{color=#8c000f}Жизнь, похожую на сказку...{/color}{/size}{/font}{/sc}":
        xalign 0.5
        yalign 0.5
    with Dissolve(1.5)
    pause 1
    play sound pistol2
    scene bg black with fl_scare
    $ unlock_ach_root_inreal(7)
    scene bg ending_MankindIsDead_cg:
        crop (940, 450, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    show ending_MankindIsDead:
        crop (940, 450, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    with Dissolve(25)
    scene bg black with byso
    stop music fadeout 3
    $ _dismiss_pause = True
    pause 2.6
    jump after_ending_screen