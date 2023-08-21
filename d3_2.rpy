label d3_withmi:
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
        jump sadfggdsfdsgsdgfdsgfsdgfsdhvcxz
    else:
        scene bg bgcg6
        show load
        with byso
        pause 10
        $ bgcg -= 1
        window show
        jump sadfggdsfdsgsdgfdsgfsdgfsdhvcxz
label sadfggdsfdsgsdgfdsgfsdgfsdhvcxz:
    $ save_name = ('Инреальность.\nДень третий.')
    scene bg int_house_of_mt_day
    play music music_list["sunny_day"]
    show unblink
    th "Угх.{w}.. Привыкать надо к такому утру."
    show mt normal pioneer with byso
    play sound sfx_bed_squeak1
    play sound2 sfx_dinner_horn_processed
    "Константин услышал на улице горн, потому опёрся на спинку кровати.{w} За столом сидела вожатая."
    show mt smile pioneer with byso
    mt "Доброе утро. Как спаслось?"
    kt "Доброе.{w} Порядок."
    show mt grin pioneer with byso
    "В ответ вожатая улыбнулась и отложила блокнот."
    mt "Это хорошо.{w} Поздравляю, у музклуба сегодня свободный день."
    mt "Вы хорошо выступили, теперь можете отдохнуть."
    th "Н-да, реально спор выиграла походу."
    kt "Да, спасибо."
    show mt normal pioneer with byso
    stop music fadeout 2
    "Константин быстро оделся и покинул домик."
    play sound door_cl
    play ambience ambience_camp_entrance_day
    scene bg ext_house_of_mt_day
    show mi normal pioneer
    with byso
    play music music_list["my_daily_life"] fadein 2
    "На выходе его ожидала Мику."
    show mi smile pioneer with byso
    mi "Утречка!{w} Как спалось?"
    kt "Доброе утро. За первые 15 минут уже дважды спросили.{w} Живём-живём. Ты как?"
    show mi upset pioneer with byso
    "Мику потёрла глаза."
    mi "Да не очень, ночью кошмар приснился, плохо выспалась."
    th "Ну, у меня это каждый день."
    kt "Ладно, пойдём позавтракаем."
    show mi happy pioneer with byso
    mi "Идём!"
    scene bg ext_houses_day
    show mi normal pioneer
    with byso
    "Мику несмотря на недосып была как всегда весёлой и активной."
    kt "О чём кошмар то?"
    show mi upset pioneer with byso
    mi "Да вообще бред какой-то. {w}Лагерь, пионеры, монстры, Генда.{w} Просто видимо вчера немного перенервничала."
    th "По описанию походит на мой кошмар, но опустим."
    kt "М-да, неприятно."
    show mi sad pioneer with byso
    mi "Не то слово..."
    "Уныло сказала Мику и поправила резинки на волосах."
    scene bg ext_square_day
    show mi smile pioneer
    with byso
    "На площади пионеры медленно но верно двигались в столовую."
    mi "Чем думаешь сегодня заняться?"
    "Константин, почесав подбородок задумался."
    kt "Не знаю. Вообще нет идей."
    show mi grin pioneer with byso
    mi "У меня зато есть."
    scene bg ext_dining_hall_away_day
    show mi smile pioneer
    with byso
    kt "М-м-м?"
    show mi grin pioneer with byso
    mi "Можем пойти на пляж, посидеть там.{w} Можем посидеть в клубе поиграть. Можем..."
    show mi smile pioneer with byso
    kt "Подожди.{w} Вопрос из вне, ты пьёшь?"
    show mi shy pioneer with byso
    "Мику смутил такой вопрос."
    mi "Ну-у, возможно, а что?"
    kt "Я из дома привёз бутылочку портвейна. {w}Не желаешь?"
    show mi laugh pioneer with byso
    "Мику рассмеялась."
    mi "Бутылка портвейна в пионерском лагере, ты серьёзно?"
    "Константин ехидно усмехнулся."
    kt "Так да или нет?"
    show mi shy pioneer with byso
    stop music fadeout 2
    mi "Давай, отметим наш триумф на сцене."
    kt "Добро."
    play ambience ambience_dining_hall_full
    scene bg int_dining_hall_people_day
    show mi smile pioneer
    with byso
    play sound sfx_concert_applause
    "Войдя в столовую, Мику и Константина встретили аплодисментами."
    show mi shy pioneer with byso
    "Константин и Мику рефлекторно поклонились публике и встали в очередь на раздаче."
    show mi happy pioneer with byso
    mi "Как неожиданно и приятно. Хоть теперь меня немного уважают."
    kt "А то.{w} Ты хорошо вчера выступила."
    show mi grin pioneer with byso
    mi "Ой, да не начинай. Засмущаешь."
    hide mi
    show mi smile pioneer at right
    show sl smile2 pioneer at left
    with byso
    "Как ни странно, на раздаче их сегодня встретила не повариха, а Славя."
    show sl smile pioneer with byso
    sl "Доброго вам утречка.{w} Артистам сегодня еда наставников."
    "Славя мило улыбнулась и открыла пару тарелок с яичницей и аппетитными гренками.{w} В довесок шли два стакана свежего яблочного сока."
    show mi happy pioneer with byso
    mi "Вау, спасибо большое."
    kt "Спасибо."
    hide mi 
    hide sl
    show mi happy pioneer
    with byso
    "Мику радовалась еде как маленький ребёнок новой игрушке."
    "Они сели за свой столик."
    show mi smile pioneer with byso
    mi "Приятного аппетита."
    kt "Спасибо, тебе тоже."
    "Мику приступила к трапезе, Константин в это время за ней наблюдал."
    show mi shy pioneer with byso
    mi "Что такое?"
    kt "Что ты так обрадовалась еде наставников?{w} Та же еда вроде как."
    show mi upset pioneer with byso
    "Мику пожала плечами."
    mi "Ну, радоваться надо мелочам.{w} Тем более мне до жути надоело есть каждый день кашу, а тут тебе вот яичница, вот гренки, вот сок."
    show mi happy pioneer with byso
    mi "Можем считать день уже задался."
    kt "Ну да, может ты и права."
    "Константин тоже потихоньку начал есть."
    th "М-м, гренки.{w} Напоминают мне завтраки по выходным, когда уже ничерта не остаётся поесть."
    stop ambience
    play sound in_vosp
    play music sab
    scene bg kt_room
    show shum_white
    with flash
    "Константин стоял у холодильника.{w} На улице темно.{w} На часах 5 утра.{w} На душе тоска."
    kt "Булка.{w}.. Хмели-сунели.{w}.. Сыр.{w}.. Яйца и вот масло.{w} Снова гренки. Надо бы как-то завязывать с мучным."
    kt "Хотя начерта.{w} Моей фигуре это уже не поможет, да и зачем как то себя лишать чего-то, вроде пока в офисную одежду влезаю."
    "Выйдя к плите, он включил газовую конфорку и прикурил от неё."
    kt "А завтра 22й день рождения.{w} Купить дури чтоль в честь этого?"
    kt "Нет, я завязал."
    "Сделав замес из яиц и сыра, Константин обмакнул в него булку и закинул на сковородку."
    kt "Купить торт?{w} Зачем?"
    kt "Восстановить контакты с вуза?{w} Хуй там."
    kt "Купить этанола?{w} Вот это дело."
    "Константин, обжарив булку со всех сторон, пошёл к компьютеру."
    stop music fadeout 2
    play sound out_vosp
    hide shum_white
    scene bg int_dining_hall_people_day
    show mi upset pioneer
    with flash
    play ambience ambience_dining_hall_full
    mi "Чего завис то?"
    "Спросила Мику, махая рукой перед лицом Константина."
    play music music_list["smooth_machine"] fadein 3
    kt "Я? Что я? Просто вспомнилось кой-что."
    show mi smile pioneer with byso
    mi "И чего вспомнилось?"
    window hide
    menu:
        "Не рассказывать.":
            $ renpy.block_rollback()
            kt "Забей.{w} Ничего такого."
            show mi dontlike pioneer with byso
            mi "Ну ладно, храни свои секретики."
            "С усмешкой ответила Мику."
        "Рассказать.":
            $ renpy.block_rollback()
            $ miscore += 1;
            kt "Просто вспомнилось что я такие гренки дома по утрам делал.{w} Рецепт прост: булка, яйца, хмели-сунели, сыр и масло."
            show mi laugh pioneer with byso
            "Мику улыбнулась."
            mi "Хм-хм, хороший рецепт, повторю как-нибудь."
    show mi smile pioneer with byso
    "Закончив с едой, Константин сидел и допивал яблочный сок."
    mi "Ну чего, пойдём на пляж?"
    kt "Почему нет, идём."
    scene bg ext_dining_hall_near_day
    show mi happy pioneer
    with byso
    play ambience ambience_camp_entrance_day fadein 2
    "Сдав тарелки они вышли из столовой."
    stop music fadeout 3
    kt "Давай, через 20 минут на пляже."
    show mi smile pioneer with byso
    mi "Хорошо, увидимся."
    hide mi
    scene bg ext_dining_hall_away_day
    with byso
    play music Gallow fadein 4
    "Мику и Константин разошлись.{w} Константин задумался."
    th "Вспоминая слова пионера, в кошмар попадают только те, кто является игроком.{w} Мику сегодня видела идентичный сон..."
    th "Хотя нет, бред.{w} Слишком много думаю.{w} Она просто назвала обычные черты лагеря."
    scene bg ext_square_day with byso
    "Константин вышел к статуе Генды."
    th "Ну да, выступали мы у памятника, монстрами в её подсознании скорее всего отложилась публика, а лагерь и без того очевидно."
    scene bg ext_house_of_mt_day with byso
    "У домика в гамаке лежала вожатая.{w} Константин незаметно забрал плавки и полотенце, после чего ушёл к пляжу."
    scene bg ext_square_day
    show el normal pioneer far at fleft
    show sh serious pioneer far at left
    with byso
    "Со стороны столовой шли кибернетики, которые тащили с собой деревянную коробку."
    th "Что теперь у этих товарищей, еду воруют со столовой?"
    scene bg ext_playground_day
    show us grin sport far at right
    show dv smile pioneer2 far at left
    with byso
    "На поле Константин заметил Алису и Ульяну, которые играли в футбол."
    us "Эй, Костя, пошли в футбол поиграем?"
    kt "Нет, спасибо.{w} Мне больше плаванье по душе."
    show us dontlike sport far at right
    show dv grin pioneer2 far at left
    with byso
    us "Фу, зануда."
    hide dv
    hide us
    with byso
    "Константин не обратил внимания на слова Ульяны и продолжил движение."
    play ambience ambience_boat_station_day
    stop music fadeout 3
    scene bg ext_beach_day with byso
    "Выйдя на пляж, Константин почувствовал тёплый летний бриз и пошёл в кабинку."
    show mi normal swim with fade
    "Быстро сменив комплект одежды, он заметил Мику, которая сидела на полотенце и взглядом провожала грузовой поезд."
    play music music_list["reflection_on_water"]
    "Константин обозначил своё присутствие демонстративным кашлем."
    show mi smile swim with byso
    mi "О, ты уже тут.{w} Ну что, купаться?"
    kt "Да, идём."
    "Константин и Мику постепенно заходили в прохладную воду."
    kt "Водичка с утреца то похолоднее."
    show mi upset swim with byso
    mi "Ну а что ты хотел, ночью у нас достаточно холодно."
    kt "Не знаю, я по ночам обычно сплю."
    "С едкой ухмылкой ответил Константин."
    show mi grin swim with byso
    mi "Ой, всё."
    show mi happy swim with byso
    play sound sfx_water_emerge
    "Демонстративно возмутилась Мику и прыгнула в прохладную воду."
    mi "Зато бодрит."
    kt "Это да, не плохо бывает поплавать."
    kt "Кстати в детстве я занимался плаваньем."
    show mi grin swim with byso
    mi "Да? Я тоже. И как тебе оно?"
    play sound sfx_borshtch
    "Константин умылся."
    kt "Так себе.{w} Я занимался спортивным плаваньем и водным поло.{w} Мало что весёлого."
    show mi upset swim with byso
    mi "Водное поло же игра, да?"
    "Спросила Мику, поправив косы."
    kt "Да-а, при том достаточно травматичная чтоб в неё не играть."
    show mi normal swim with byso
    mi "А чего ты в спортклуб не думал записаться?"
    "Константин хмыкнул."
    kt "Не-а, нет. Не люблю спорт как таковой.{w} Одно дело упражнение, другое конкретное направление."
    show mi smile swim with byso
    mi "М-м, поняла. Поплыли на сушу?"
    kt "Давай."
    play sound sfx_water_emerge
    show mi normal swim with byso
    "Выйдя на сушу, они сели на свои полотенца."
    show mi grin swim with byso
    mi "Слушай, а у тебя на памяти нет других песен?"
    kt "Ты про что?"
    show mi smile swim with byso
    mi "Ну по типу вчерашней.{w} Хотелось бы сыграть сегодня чего-то нового."
    "Константин пожал плечами."
    kt "Не могу сказать.{w} Если вспомню - скажу."
    hide mi 
    show mi normal swim at right
    show mt smile pioneer panama at left
    with byso
    "На пляж пришла вожатая."
    mt "Ну как вы, отдыхаете?"
    show mi happy swim with byso
    mi "Да, всё прекрасно!"
    "С милой улыбкой ответила Мику."
    show mt grin pioneer panama with byso
    mt "Замечательно.{w} Сейчас надо вернуться на площадь в пионерской форме."
    show mi dontlike swim with byso
    kt "И зачем же?"
    th "Она решила нас всё-таки чем-то да озадачить?"
    mt "Сюрприз. Приходите - сами увидите."
    hide mt
    hide mi
    show mi dontlike swim
    with byso
    "Вожатая поправила панаму и ушла."
    mi "Ну да, не вовремя мы пошли искупаться. Только окунулись, так нас уже обратно зовут."
    kt "Да пофигу, оставим плавательные принадлежности тут, потом вернёмся."
    mi "Хорошая идея."
    scene bg ext_playground_day
    show mi upset pioneer
    with byso
    play ambience ambience_camp_entrance_day
    stop music fadeout 3
    "Переодевшись, они пошли к площади."
    mi "Слушай, а мы точно с тобой до смены не были знакомы?"
    "Константин развёл руками."
    kt "Не могу сказать, хотя может и в правду так..."
    show mi normal pioneer with byso
    "Мику неловко почесала затылок.{w} Константин ухмыльнулся."
    kt "Лысина будет."
    show mi dontlike pioneer with byso
    mi "Ну нет, это немного не так работает."
    play sound sfx_punch_medium
    "Обиженно сказала Мику и ткнула Константина локтём в бок."
    scene bg ext_square_day
    show mi dontlike pioneer at right
    show mt smile pioneer panama
    show un smile2 pioneer at fleft
    show mz smile pioneer at left
    with byso
    play music music_list["your_bright_side"] fadein 3
    "На площади был весь отряд."
    "Славя стояла рядом с Ольгой, которая фотографировала Лену и Женю на новенький <<Киев-80>>."
    mt "А вот и оставшиеся из музклуба."
    hide mz 
    hide un 
    with byso
    "Сказала Ольга и передала 2 листа быстропроявляющейся плёнки членам литературного клуба."
    th "Я конечно не уверен, но мне кажется в это время не должны были такую фотопечать изобрести..."
    mt "Сегодня нам доставили фотоаппарат вместе с запчастями для кибернетиков.{w} Каждому по две фотографии."
    hide mi
    show mi sad pioneer
    hide mt
    with byso
    mi "Блин, у меня волосы же мокрые..."
    kt "Мы на равных, пошли фоткаться."
    show mi shy pioneer with byso
    mi "Пойдём."
    "Смущенно сказала Мику и встала на фоне медного Генды."
    "Константин встал рядом."
    show mi smile pioneer with byso
    mi "Как позировать будем?"
    kt "Есть идея, сделай вид что играешь на гитаре."
    "Мику улыбнулась."
    mi "Давай попробуем."
    show mi happy pioneer with byso
    "Мику изобразила игру на гитаре, а Константин приобнял Мику и свободной рукой показал <<козу>>."
    mt "Два кадра, стойте смирно."
    play sound fotoapparat
    show mi dontlike pioneer with flash
    "Константина ослепила вспышка фотоаппарата."
    th "На кой чёрт днём снимать со вспышкой..."
    "Подумал он и потёр глаза."
    mi "Ух, светло."
    show mi happy pioneer with byso
    mt "Так, вторая фотография, снова смирно."
    play sound fotoapparat
    show mi upset pioneer with flash
    "Константина снова ослепила вспышка фотоаппарата."
    "Вожатая достала второй лист и раздала по одному."
    mt "Вот ваши фотографии.{w} А теперь давайте все вместе, кучкуйтесь."
    hide mi with byso
    "Весь отряд встал в плотную шеренгу.{w} Ульяна и Шурик сели на корточки поодаль друг от друга."
    mt "Итак.{w} Раз. Два. Три."
    play sound fotoapparat
    scene bg ext_square_day with fade
    "Спустя 5 минут вожатая наделала фотографий на всех и раздала их каждому."
    show mt grin pioneer panama with byso
    mt "Так, а теперь по делам. До обеда чтоб никто не бездельничал, я всё вижу."
    th "Да-да, ага."
    hide mt 
    show mi smile pioneer
    with byso
    stop music fadeout 3
    mi "Ну что, обратно на пляж?"
    kt "Да, идём."
    scene bg ext_playground_day
    show mi shy pioneer
    with byso
    play music music_list["trapped_in_dreams"] fadein 3
    "По дороге на пляж, Мику разглядывала фотографию."
    mi "Ну мы артисты конечно."
    kt "А как же, музклуб, чего сказать."
    show mi upset pioneer with byso
    "Мику хмыкнула и убрала фотографии в грудной кармашек."
    mi "Слушай, а твоего дедушку Валерий Юрьевич звали?"
    "Константина поразила точность догадки Мику."
    kt "Ну да.{w}.. Откуда ты знаешь?"
    mi "Вспоминаю как мы впервые виделись."
    kt "И я вижу успешно."
    scene bg ext_beach_day
    show mi smile swim
    with fade
    play ambience ambience_boat_station_day
    "Они вернулись на пляж и переодевшись прыгнули в воду."
    show mi happy swim with byso
    mi "Вот уже вода немного теплее."
    kt "Слушай, а как живётся в Японии?"
    show mi upset swim with byso
    play sound sfx_borshtch
    "Мику плеснула водой в сторону и посмотрела на Константина."
    mi "Не так как тут.{w} Площадь меньше, население больше, люди другие.{w} Не то что бы я скучаю, но вернуться на время было бы неплохо."
    kt "А чего так?"
    mi "Давно я не виделась с мамой, бабушкой и дедушкой.{w} Уже около двух лет."
    show mi sad swim with byso
    mi "Честно говоря я уже и не помню как попала в СССР.{w} Слишком давно это было.{w} Помню только что сидела одна в своей панельке в Японии."
    kt "Может в кой-то мере это хорошо."
    play sound sfx_water_emerge
    "Мику и Константин сели на берег."
    mi "В каком смысле?"
    kt "Не всегда хорошо всё помнить, уж поверь."
    kt "Я бы многое хотел позабыть."
    mi "Ну да, ты рассказывал вчера..."
    show mi smile swim with byso
    mi "Ладно, давай не о грустном.{w} Сегодня вроде как свечка будет."
    kt "Свечка-свечка.{w}.. Что-то знакомое."
    "Мику опёрлась на локти."
    mi "Небольшое событие к концу смены, где каждый может выразить свои мысли про смену и отряд."
    "Отчеканила Мику.{w} Константина смутила точность и принуждённость ответа."
    kt "А, я вспомнил. Муть."
    show mi normal swim with byso
    mi "Чего так?"
    kt "Не знаю, не особо люблю подобные изложения мысли."
    show mi upset swim with byso
    mi "Поняла. Ну да, каждому своё."
    "Константин встал на ноги."
    kt "Ну что, пойдём в клуб."
    show mi smile swim with byso
    mi "Ну-у.{w}.. Ладно пошли."
    "Сказала Мику, прогибаясь в спине."
    play ambience ambience_camp_entrance_day
    stop music fadeout 2
    scene bg ext_houses_day
    show mi happy pioneer
    with byso
    "Переодевшись, они направились к жилым корпусам."
    play music music_list["farewell_to_the_past_edit"] fadein 3
    mi "А всё-таки хорошо вот так в лагере когда ничего делать не требуют."
    "Мику на ходу пыталась выжать свои косы."
    kt "Всегда хорошо когда есть свободное время."
    show mi upset pioneer with byso
    mi "Да уж, отвыкла я уже от таких деньков."
    mi "Постоянно разные унылые истории."
    mi "Мику, настрой гитару."
    mi "Мику, дай гитару."
    mi "Мику, не шуми."
    mi "Временами мне кажется что мне в этом обществе нет места."
    kt "Хм-хм, а это уже знакомая мысль."
    show mi sad pioneer with byso
    mi "Просто меня почти всё общество не хочет принимать из-за моей излишней говорливости в первое время."
    kt "Ну да, мы это обсуждали."
    mi "А ты как думаешь, найдёшь ли себе место в этом обществе?"
    window hide
    menu:
        "Да":
            $ renpy.block_rollback()
            $ miscore += 1;
            mi "Ясно."
        "Нет":
            $ renpy.block_rollback()
            mi "Ясно."
    show mi upset pioneer with byso
    "Безэмоционально сказала Мику."
    scene bg ext_house_of_mt_day
    show mi upset pioneer
    with byso
    "Они дошли до домика вожатой.{w} Константин повесил свои плавки и полотенце."
    kt "И чего тебе ясно?"
    show mi sad pioneer with byso
    mi "Да нет, ничего."
    "Константин заметил что настроение Мику пошло на спад."
    kt "Что-то не так?"
    show mi upset pioneer with byso
    "Она немного оживилась."
    mi "Нет-нет, просто видимо дистресс после вчерашнего прошёл."
    kt "Ладно."
    play sound sfx_dinner_horn_processed
    "Заиграл горн на обед."
    show mi surprise pioneer with byso
    mi "Как, уже?{w} Только что же завтракали."
    kt "Не знаю, мы уже дважды искупались, пофоткались и прогулялись по лагерю, вроде всё в порядке."
    show mi upset pioneer with byso
    "Мику задумалась. По её глазам было видно, что с ней что-то не так."
    mi "Может и в правду. Ход времени совсем изменился для меня в последние 2 дня..."
    scene bg ext_house_of_un_day
    show mi upset pioneer
    with byso
    play sound sfx_open_door_1
    hide mi with byso
    "Мику зашла в свой домик.{w} Константин сел на ступени и начал ждать."
    th "Где же сегодня засесть для выпивки можно..."
    show mi smile pioneer with byso
    "Из домика вышла Мику и махнула рукой Константину."
    mi "Пошли есть."
    stop music fadeout 3
    scene bg ext_dining_hall_near_day
    show sl smile2 pioneer at right
    show mi upset pioneer
    with byso
    "У столовой из стороны в сторону ходила Славя и словно кого-то ждала."
    th "Не по нашу же душу я надеюсь."
    "Мику посмотрела в сторону Слави и скорее всего подумала о том же."
    scene bg int_dining_hall_people_day
    show mi smile pioneer
    with byso
    play ambience ambience_dining_hall_full
    "В столовой они встали в очередь."
    mi "После обеда поиграем?"
    kt "Давай, почему нет."
    "Очередь на раздаче дошла до них.{w} Повариха выдала наваристый гороховый суп и мясное рагу с двумя стаканами киселя."
    show mi happy pioneer with byso
    mi "Спасибо."
    pov "Не за что."
    "Мику села за столик музклуба."
    kt "Вот такая еда уже ближе к делу.{w} Давно не ел горохового супа."
    show mi upset pioneer with byso
    mi "Я тоже.{w} Достаточно редко тут готовят такой супчик."
    show mi happy pioneer with byso
    mi "Сейчас я не по теме, но мне кажется я кое-что придумала!"
    "Константин вопросительно посмотрел на Мику."
    show mi smile pioneer with byso
    mi "Благодаря вчерашнему успеху у нас может появиться возможность расширить клуб."
    mi "Просто немного рекламы и у нас уже будет побольше народу.{w} Из того следует что у нас будет больше рук для игры на инструментах."
    kt "Ни слова больше."
    play sound dvizh
    "Константин доел суп и встал с места."
    play music music_list["that_s_our_madhouse"]
    show mi surprise pioneer with byso
    kt "Товарищи!!!"
    "Внимание всей столовой было направлено на Константина.{w} Мику покраснела и прикрылась рукой."
    kt "Сегодня уникальное предложение!{w} Те кто умеет играть на музыкальных инструментах может попробовать себя в игре с нами!"
    kt "Акция только для двух-трёх человек!"
    kt "Всем приятного аппетита и хорошего дня."
    "Константин сел обратно на своё место, где его ожидала Мику, готовая сгореть от смущения.{w} Разговоры в столовой возобновились."
    show mi upset pioneer with byso
    mi "Ты немного меня не понял..."
    hide mi
    show mi surprise pioneer at right
    show image di_smile at left
    with byso
    dip "Здарово! Приятного."
    "К ним пришёл специфично одетый парень с рыжими волосами и пирсингом, после чего запрыгнул за свободный стул."
    hide image di_smile
    show image di_smile2 at left
    with byso
    dimas "Меня Дима.{w} Можете не представляться, я ещё вчера вас узнал. Мику и Константин.{w} Хочу играть с вами."
    "Мику сильно удивилась тому что на предложение Константина кто-то откликнулся."
    kt "Здравствуй."
    "Они обменялись рукопожатиями."
    show mi smile pioneer with byso
    mi "Привет. На чём играть умеешь?"
    hide image di_smile2
    show image di_dontlike at left
    with byso
    dimas "Ударные, электрогитара и по мелочи пою."
    hide image di_dontlike
    show image di_smile at left
    with byso
    dimas "Сам думал вступить в музклуб, но раз уж такая пьянка, то я с вами хочу потусить."
    "Несмотря что образ нового знакомого в обычных условиях оттолкнул бы Константина, в этот раз Дима произвёл на него впечатление."
    kt "Окей, у меня как раз явилось несколько идей по поводу песен."
    show mi grin pioneer with byso
    "Мику радостно улыбнулась, Дима поправил волосы и ухмыльнулся."
    hide image di_smile
    show image di_smile2 at left
    with byso
    dimas "Это шикарно.{w} Как раз давно не брал в руки музыкальники."
    kt "Осмелюсь предположить что ты фанат панк-направления в музыке."
    show mi upset pioneer
    hide image di_smile2
    show image di_smile at left
    with byso
    "Мику задумалась о словах Константина, Дима утвердительно кивнул."
    dimas "Агась.{w} Думаю по мне заметно. Любимая группа Sex Pistols."
    hide image di_smile
    show image di_rage at left
    with byso
    dimas "No future, no future, no future for you."
    "В слух напел Дима изображая игру на гитаре."
    hide image di_rage
    hide mi
    show mt surprise pioneer at cright
    show image di_smile at left
    show mi normal pioneer
    with byso
    stop music fadeout 3
    "К ним подошла вожатая и кинула удивлённый взгляд на Диму."
    mt "Приятного аппетита.{w}.. пионеры."
    mi "Спасибо."
    show mt smile pioneer with byso
    mt "Молодцы что организуете лагерный досуг даже в свободное время.{w} Хорошая идея продвижения для вашего клуба."
    kt "Да, спасибо."
    "Вожатая ухмыльнулась."
    mt "У нас сегодня свечка, если хотите то сегодня до него может быть ваше выступление."
    mt "Если сделаете то будет замечательно!"
    show mi smile pioneer with byso
    "Мику с улыбкой глянула на Константина, потом на Диму."
    mi "Не можем обещать.{w} К ужину скажем."
    hide image di_smile2
    show image di_smile at left
    with byso
    dimas "Да-а, устроим чёткую музыку."
    kt "Вполне может быть."
    show mt grin pioneer with byso
    mt "Замечательно!"
    "С улыбкой сказала вожатая."
    show mt smile pioneer with byso
    mt "Тогда если чего-то надумаете - оповестите."
    hide image di_smile
    show mi upset pioneer
    show image di_smile2 at left
    hide mt
    with byso
    "Вожатая ушла.{w} Дима продолжил напевать про себя английскую песню, а Мику с недоумением смотрела на Константина."
    mi "Я надеюсь у тебя всё-таки есть идеи..."
    "Константин улыбнулся и допил свой кисель."
    kt "Идём в клуб?"
    hide image di_smile2
    show image di_smile at left
    with byso
    dimas "Погнали!"
    show mi smile pioneer with byso
    mi "Ну идём."
    hide image di_smile
    scene bg ext_dining_hall_near_day
    show us grin pioneer
    show mi smile pioneer at left
    show image di_smile at right
    with byso
    play music music_list["awakening_power"]
    play ambience ambience_camp_entrance_day
    "На выходе из столовой они встретили Ульяну."
    dimas "Ломать мой лысый череп!{w} Здорова Уля!"
    us "О-о, Димас, здорова!"
    "Дима и Ульяна стукнулись кулаками."
    hide image di_smile
    show image di_smile2 at right
    with byso
    dimas "Чтоб не пропустила сегодня свечку, у нас сегодня панк-рок будет."
    show us laugh pioneer with byso
    "Ульяна, несмотря на то что явно не поняла ничего из того что ей озвучил Дима, заулыбалась."
    us "Зачёт!{w} Конечно же буду!"
    dimas "Ну я поскакал, брошу кости в музклуб."
    us "Удачи!"
    hide us
    show mi happy pioneer at left
    with byso
    "Ульянка скрылась в столовой."
    mi "Ты в контакте с Ульяной?"
    hide image di_smile2
    show image di_smile at right
    with byso
    dimas "Конешн.{w} Она крутая."
    kt "Ну, не удивительно."
    stop music fadeout 3
    play sound door_cl
    play ambience ambience_music_club_day
    hide image di_smile
    scene bg int_musclub_day
    show mi smile pioneer at right
    show image di_smile2 at left
    with byso
    "В музклубе было как всегда пустынно.{w} Дима уселся на стуле и осмотрел окружающие его инструменты."
    dimas "Неплохой у вас арсенал.{w}.. Ну чё играть будем?"
    kt "А это надо придумать.{w} На этот раз хотелось бы чего-то русского..."
    hide image di_smile2
    show image di_smile at left
    with byso
    dimas "М-м, русский панк, неплохая идея!"
    kt "Не обещаю что это будет панк но выйти должно неплохо."
    "Константин взял блокнот и начал стучать карандашом по столу."
    kt "Думай-думай-думай."
    show mi smile pioneer close
    hide image di_smile
    show image di_think at left
    with byso
    "Рядом с ним встала Мику, а Дима стал ковыряться в оборудовании электрогитары."
    mi "Чего, какие мысли?"
    kt "Да есть парочка..."
    show mi angry pioneer close
    hide image di_think
    show image di_smile at left
    with byso
    play music music_list["kostry"]
    "Позади зазвучал оглушающий рёв гитары."
    kt "Дима-а!"
    hide image di_smile
    show image di_angry2 at left
    with byso
    dimas "Нахер иди!"
    mi "Дима!"
    hide image di_angry2
    show image di_rage at left
    with byso
    dimas "Ламповая голова, дай поиграть, нахер иди!"
    show mi angry pioneer at cleft
    hide image di_rage
    show image di_smile at left
    with byso
    $ volume(0.2, "music")
    play sound sfx_lock_close
    show mi angry pioneer at right with byso
    "Мику подошла к нему и уменьшила громкость выходного звука."
    kt "Так, ладно, продолжаем..."
    show mi smile pioneer with byso
    "Константин начал выцарапывать на листе текст."
    kt "По ту сторону весны..."
    kt "Я смотрю цветные сны..."
    kt "По ту сторону решетки."
    kt "Смотрите в анфас, а я смотрю на вас сквозь перспективу, вдоль тротуаров и машин, людей, их лиц немного хмурых."
    kt "Я смотрю цветные сны."
    hide image di_smile
    show image di_think at left
    with byso
    stop music fadeout 3
    "Дима закончил баловаться с гитарой и подошёл к Константину и Мику."
    dimas "Из моих больших ботинок ускользает перспектива."
    dimas "Все идет в прямом эфире я смотрю цветные сны."
    hide image di_think
    show image di_smile at left
    with byso
    dimas "Я знаю эту песню!"
    $ volume(1, "music")
    play music music_list["smooth_machine"] fadein 3
    "Константин, понимая что песня была записана в 2018м году не поверил своим ушам."
    dimas "Слышал чёт такое. По радио какой-то чувак играл, я даже аккорды знаю."
    th "Хм-м."
    kt "Ну будь добр тогда записать. Я помню наизусть как играется, напиши для Мику. Сам сядешь за барабаны."
    hide image di_smile
    show image di_think at left
    with byso
    "Дима взял у Константина ручку и начал писать аккорды для Мику."
    th "Знает аккорды этой песни.{w}.. Странно.{w} Начиная с того что сами аккорды как таковые запомнить сложно, так он ещё и наизусть их помнит. Это странно..."
    th "Даже очень..."
    kt "А как ты аккорды пишешь?"
    hide image di_think
    show image di_smile2 at left
    with byso
    "Дима ухмыльнулся."
    dimas "Да дар у меня такой.{w} Видимо я писака с роду."
    show mi dontlike pioneer with byso
    mi "И где-ж ты был пока клуб пустовал?"
    hide image di_smile2
    show image di_smile at left
    with byso
    "Недовольно поинтересовалась Мику.{w} Дима захохотал."
    dimas "Я панк. Меня не устраивают устои советского тоталитаризма.{w} Я тем самым показывал слепой протест на всё эту лабуду."
    dimas "Потому извиняй, подруга, не нравится мне такое."
    mi "Ну ладно..."
    scene bg int_musclub_day
    show image di_smile at left
    show mi normal pioneer at right
    with fade
    "Спустя 5 минут Дима всё написал."
    dimas "На, попробуй."
    show mi upset pioneer far at right with byso
    "Выдав бумажку Мику, он снова завалился на стул."
    "Мику пошла к гитаре и включив минимальную громкость стала перебирать струны."
    kt "Хм-м, раз ты такой нонконформист, то почему ты не протестуешь против музыки?"
    hide image di_smile
    show image di_angry at left
    with byso
    dimas "Почему не протестую, протестую.{w} Предпочитаю рок и панк-рок. Остальное шелуха.{w}.. Но если по правде..."
    dimas "В этом плане я немного позёр.{w} Люблю почти всю музыку.{w} Музыка — это всегда человечность.{w} Нечто человеческое вообще, в принципе, я бы сказал, один из врожденных, несущих элементов духа в человеческой душе."
    dimas "Музыка будет вечно и всюду.{w}.. Потому что музыка по ту сторону бытия, истории и политики, она вне богатства и бедности, вне жизни и смерти."
    dimas "Музыка — вечна.{w} Любая музыка."
    hide image di_angry
    show image di_smile at left
    with byso
    "Договорив, Дима натянул на себя свою стандартную лыбу."
    hide image di_smile
    show image di_smile2 at left
    with byso
    dimas "Ну лады.{w} Это так, между нами."
    th "А до этого мне казалось, что я - человек диссонанс..."
    kt "Мику, ты чего там?"
    show mi smile pioneer far at right with byso
    "Мику отвлеклась от струн и с улыбкой посмотрела на Константина."
    mi "Да так, аккорд пытаюсь поставить."
    kt "Слушайте, давайте так.{w} Димас на барабаны и вокал, Мику на гитару, я просто на вокал."
    mi "Мне нравится."
    hide image di_smile2
    show image di_smile at left
    with byso
    dimas "Ух-ух-у-у, поющий барабанщик, новое слово в музыкальном исполнении, я обе руки за!"
    th "Не понять мне этих..."
    kt "Ладно, тогда давайте начнём разучивать."
    kt "Мику, дай ещё пару листов, сейчас сделаем текст для всех."
    show mi happy pioneer at right with byso
    mi "Так точно."
    hide mi with byso
    stop music fadeout 3
    "Мику пошла в кладовку.{w} Дима подошёл поближе к Константину."
    hide image di_smile
    show image di_smile2
    with byso
    dimas "Она тебе нравится, да?"
    kt "С чего ты это взял?"
    dimas "Просто скажи, да-а или не-ет."
    window hide
    menu:
        "Допустим.":
            $ renpy.block_rollback()
            $ miscore += 1;
            kt "Тебе то чего с того?"
            dimas "Да просто любопытно."
            hide image di_smile2
            show image di_smile at right
            with byso
            "С хитрой лыбой сказал Дима и подошёл к окну."
        "Нет":
            $ renpy.block_rollback()
            dimas "М-м, понимаю."
            hide image di_smile2
            show image di_smile at right
            with byso
            "С хитрой лыбой сказал Дима и подошёл к окну."
    show mi normal pioneer at left with byso
    "Мику вышла из кладовки и судя по всему не слышала их диалог."
    show mi happy pioneer at left with byso
    mi "Вот листочки.{w} Вот карандаши.{w} Давайте переписывать."
    show mi smile pioneer at left with byso
    play sound sfx_paper_bag
    "Дима и Константин начали переписывать текст на другие два листа."
    scene bg int_musclub_day
    show mi smile pioneer at left
    show image di_smile at right
    with fade
    #Ых-ых-ыыы, заебался я это писать, помогите. Хочу писать про Реночку кровавую резню а тут какие-то текста досвидоши. 09.02.2023 03:18
    "Переписав они распределились по музклубу у соответствующих инструментов."
    kt "Справишься хоть с голосом и барабанами одновременно?"
    hide image di_smile
    show image di_smile2 at right
    with byso
    dimas "Спрашиваешь!{w} И не такую хрень вытворяли."
    show mi grin pioneer at left with byso
    mi "Хорошо, ну поехали?.."
    show mi smile pioneer at left
    show mt smile pioneer
    hide image di_smile2
    show image di_dontlike at right
    with byso
    play sound door_cl
    "В этот момент вошла вожатая."
    mt "Готовитесь?"
    kt "По крайней мере только начали."
    show mt grin pioneer with byso
    mt "Это хорошо, покажете?"
    show mi dontlike pioneer at left with byso
    mi "Нет, ещё не можем.{w} Первый прогон."
    hide image di_dontlike
    show image di_smile2 at right
    with byso
    dimas "Да ладно вам, чё?{w} Исполним!"
    show mi normal pioneer at left with byso
    mi "Хотя ладно."
    kt "Только мы это в первый раз.{w} Не спешите тапками закидывать."
    show mt normal pioneer with byso
    "Вожатая приняла серьёзное выражение лица и села на стул."
    mt "Будто я так делаю.{w} Давайте, если мне понравится, то исполните перед свечкой."
    th "Как же хорошо что я с этой не общался вне работы.{w} Высокомерию нет предела. {w}Тут на равных правах, а что уж там о подчинённых говорить?..."
    kt "Давайте, раз, два, три, начали."
    show mt grin pioneer
    hide image di_smile2
    show image di_smile at right
    show mi smile pioneer at left
    with byso
    play music dosvidosh fadein 3
    "Мику, смотря в бумажку начала наигрывать на гитаре.{w} Подключился Константин, а затем Дима на барабанах."
    window hide
    $ set_mode_nvl()
    window show
    "По ту сторону весны.{w}.. Знакомая песня для Константина.{w} Для него она ознаменовала понимание того что он совершенно никчёмен в ВУЗовском обществе."
    "Пересоциализация в ВУЗе могла бы стать единственным ключом к адекватному существованию, но не удалось."
    "Первый семестр был весьма занимательным.{w} Несколько новых людей, отсутствие школьных учитилей-самодуров и быдла в лице одноклассников."
    "Со второго семестра Константин осознал одну простую истину.{w} Его жизнь не станет нормальной.{w} Он так и будет козлом отпущения."
    "Что в школе, что в ВУЗе, а в дальнейшем и на работе всё будет точно так же.{w} Надежда как и в поговорке ушла напоследок - третий семестр."
    "Людей там он возненавидел на том же уровне что и в школе, правда причин на то было уже куда меньше."
    "Константин, несмотря на вполне стандартные размеры тела был слепой зоной для однокурсников.{w} Им было совершенно плевать на его существование."
    "Его это сильно раздражало, потому он решил не оставаться в ВУЗе дольше чем на 2-3 пары, после чего ехал домой."
    window hide
    $ set_mode_adv()
    window show
    show mt smile pioneer
    hide image di_smile
    show image di_smile2 at right
    show mi happy pioneer at left
    with byso
    stop music fadeout 3
    "Мику завершила песню последним аккордом.{w} Вожатая улыбнулась и похлопала."
    mt "Замечательная песня!{w} Сегодня выступаете."
    hide image di_smile2
    show image di_smile at right
    with byso
    dimas "Конечно выступаем!"
    show mt angry pioneer with byso
    "Вожатая строго посмотрела на Диму."
    mt "Это не вопрос.{w} Всё, репетируйте, я пошлю кого-то настроить технику на сцене и сделаю объявления о вашем выступлении."
    hide mt
    hide image di_smile
    show image di_angry2 at right
    show mi smile pioneer at left
    with byso
    play sound door_cl
    "С этими словами вожатая удалилась."
    dimas "Вот стерва!{w} Чё я такого сказал что-б мне хамить?"
    kt "Да она всегда была такой."
    hide image di_angry2
    show image di_think at right
    show mi upset pioneer at left
    with byso
    "Озвучил вслух свои мысли Константин.{w} Мику и Дима с сомнением посмотрели на Константина."
    mi "Ты же первую смену в лагере..."
    kt "Я в смысле видел её до этого.{w}.. Когда только не помню."
    hide image di_think
    show image di_angry at right
    show mi normal pioneer at left
    with byso
    "Константин понял что был близок к тому чтобы заложить сомнения в их головах, но его ярко-выраженная ложь прошла мимо ушей."
    dimas "Н-да-а...{w} Походу все вожатые такие."
    show mi dontlike pioneer at left with byso
    mi "Ну что поделать, работа такая."
    hide image di_angry
    show image di_smile at right
    with byso
    dimas "Да какая работа, такую как она вошпе нельзя к людям подпускать."
    th "Тут ты как-никак прав."
    show mi upset pioneer at left with byso
    mi "Может она в будущем ещё изменится."
    th "А вот тут уже чёрта с два."
    kt "Ну что, погнали ещё несколько раз."
    hide image di_smile
    show image di_smile2 at right
    with byso
    dimas "Так точно!"
    "Ответил Дима, раскручивая барабанные палочки в руках."
    show mi smile pioneer at left with byso
    mi "Начинаем!"
    play music dosvidosh fadein 3
    "Музыканты снова начали исполнение."
    window hide
    $ set_mode_nvl()
    window show
    "Константина во время обучения в ВУЗе неоднократно посещали мысли о самоубийстве.{w} Он в этом видел наиболее корректный выход из положения."
    "Неоднократно он думал о том что по нему никто не будет скучать, в чём и был прав.{w} Родители выперли, единственная девушка убилась, однокурсникам плевать, в школе забыли."
    "Но в один момент его ненависть к миру начала вытеснять депрессивные мысли.{w} Печаль сменилась на злобу и он уже не хотел умирать.{w} Он хотел понять на какое дно может упасть человечество."
    "Пред ним люди изливаясь желчью твердить что нет ничего важнее жизни человека.{w} Константину это казалось смешным."
    "<<Вместо того чтобы финансировать реально важные проблемы человек идёт буквально на самоуничтожение по тропе гуманности>>."
    "Эта его цитата и характеризовала его отношение к обществу."
    window hide
    $ set_mode_adv()
    window show
    stop music fadeout 3
    "Снова засолировав последний аккорд, Мику села на стул."
    show mi happy pioneer at left with byso
    play music music_list["i_want_to_play"] fadein 3
    mi "Фух, на этот раз без ошибок."
    hide image di_smile2
    show image di_dontlike at right
    with byso
    dimas "А чё, в тот раз были?"
    show mi upset pioneer at left with byso
    mi "Да, ты не слышал?"
    hide image di_dontlike
    show image di_smile at right
    with byso
    "Дима махнул рукой и кинул палочки на стул."
    dimas "Да пофигу.{w} Они не особо придирчивая публика, так прокатит."
    "Константин же прокашлялся и поправил волосы."
    kt "Думаю Дима прав, не стоит накручиваться."
    show mi happy pioneer at left with byso
    mi "Постараюсь."
    "Выдохнула Мику с милой улыбкой."
    hide image di_smile
    show image di_smile2 at right
    with byso
    dimas "Лады, друзья, ещё разок и я пойду манатки собирать."
    kt "Куда это ты собрался?"
    hide image di_smile2
    show image di_smile at right
    with byso
    "Дима поднял барабанные палочки и поправил куртку."
    dimas "Как куда, сваливаю домой.{w} Друзья автостопом дать предложили."
    show mi upset pioneer at left with byso
    mi "Что такое автостопом?"
    hide image di_smile
    show image di_think at right
    with byso
    dimas "Э-эх ты.{w} Просто просить каждого второго подкинуть куда по пути."
    show mi dontlike pioneer at left with byso
    mi "И чего, тебя просто так отпустят?"
    hide image di_think
    show image di_smile at right
    with byso
    dimas "Пф-ф, ещё бы, если будут против я бате скажу, он меня сам подберёт отсюда."
    th "А чё так можно было чтоль..."
    kt "Понятно.{w} Когда отчалишь?"
    hide image di_smile
    show image di_smile2 at right
    with byso
    dimas "Завтра с утреца.{w} Приятно будет приехать и пивка навернуть."
    kt "М-м, понимаю, ладно погнали."
    show mi smile pioneer at left with byso
    mi "Раз, два, три, четыре."
    show mi happy pioneer at left
    hide image di_smile2
    show image di_smile at right
    with fade
    "Прогнав песню ещё раз, они сложили инструменты."
    dimas "Фух, ну всё ребят, я побегу.{w} Не скучайте!"
    play sound door_cl
    stop music fadeout 3
    hide image di_smile
    hide mi
    show mi upset pioneer
    with byso
    "Выкрикнул Дима и скрылся."
    mi "Странный он, не думаешь?"
    kt "Возможно. {w}Смотря про что ты говоришь."
    show mi dontlike pioneer with byso
    play music music_list["lightness"] fadein 10
    "Мику начала перевязывать волосы и с недоумением посмотрела на Константина."
    mi "В каком смысле?{w} Во всём."
    mi "Волосы, железки, манера речи, убеждения в жизни."
    kt "Да не, в порядке вещей. Бывало и хуже."
    mi "Ну не знаю."
    play sound sfx_knock_door2
    "В дверь постучали."
    th "Кого теперь..."
    show mi normal pioneer with byso
    mi "Войдите."
    show image rm_no at right with byso
    play sound door_cl
    "Вошёл Рома и осмотрел клуб."
    hide image rm_no
    show image rm_th2 at right
    with byso
    rm "Вожатая нас запрягла на сцене звукотехнику установить."
    "Рома достал листок."
    rm "Сейчас подойдёт Шурик и Электроник.{w} Нужно взять пару звукоусилителей, шнурки и сами гитары. Телеги сейчас привезут."
    show mi upset pioneer with byso
    mi "Барабанная установка на сцене?"
    hide image rm_th2
    show image rm_an at right
    with byso
    rm "Уж чего не знаю того не знаю, сами разберётесь."
    show mi dontlike pioneer with byso
    "Мику поморщилась и взяла гитары." 
    play sound door_cl
    show el smile pioneer at left
    show sh serious pioneer at fleft
    with byso
    "В клуб вошли остальные кибернетики."
    el "Всем привет."
    "Сказал Электроник и взял у Мику гитары."
    kt "Не сломай."
    show el normal pioneer at left with byso
    el "Да-да, без проблем."
    show mi normal pioneer with byso
    "Мику достала из кладовки два ящика, которыми оказались те самые звукоусилители."
    kt "А чего мы тот не возьмём на котором играли?"
    show mi smile pioneer with byso
    mi "А ты попробуй, он к полу приколочен."
    kt "М-м-м, со вкусом жить не запретишь."
    show mi happy pioneer with byso
    play sound sfx_put_sugar_cart
    "В ответ Мику хихикнула и поставила ко входу коробки и кабели."
    show mi normal pioneer with byso
    mi "Несите, мы потом подойдём."
    rm "Угу..."
    stop music fadeout 2
    play sound door_cl
    hide image rm_an
    hide el
    hide sh
    show mi smile pioneer
    with byso
    "Недовольно ответил Рома и с остальными кибернетиками отправился на сцену."
    play music music_list["your_bright_side"]
    show mi happy pioneer with byso
    mi "Слушай, помнишь что ты предлагал сегодня утром?"
    "Константин сел на подоконник и улыбнулся."
    kt "Ещё бы, а что?"
    show mi shy pioneer with byso
    mi "Сходи за портвейном сейчас.{w} После свечки мы сюда зайдём и посидим."
    kt "У тебя есть пакет?"
    show mi normal pioneer with byso
    mi "Есть авоська."
    "Мику достала из кладовки старую авоську из зелёных нитей.{w} С такими дырами оттуда бутылка выпадет."
    kt "А, ага. Ты мне её ещё предложи надеть вместо колготок."
    show mi laugh pioneer with byso
    "В ответ Мику рассмеялась."
    mi "Ну ты даёшь."
    kt "Мне пакет был нужен чтоб никто не видел что я несу."
    show mi happy pioneer with byso
    mi "А-а-а..."
    show mi laugh pioneer with byso
    "Мику рассмеялась ещё сильнее и убрала авоську."
    show mi grin pioneer with byso
    mi "Фух, ну тогда не знаю что тебе предложить."
    kt "Ладно, иду.{w} За пазухой пронесу."
    show mi normal pioneer with byso
    mi "Иди, у сцены встретимся.{w} Вот, возьми ключи, откроешь, закроешь, сам понимаешь."
    play sound sfx_keys_rattle
    "Мику дала Константину связку ключей.{w} Константин осмотрел пару ключей на кольце и положил в карман."
    kt "Понял, принял."
    scene bg musclub
    show mi normal pioneer
    with byso
    play ambience ambience_camp_entrance_day
    play sound sfx_key_drawer
    "Мику вышла с Константином и он закрыл музклуб."
    show mi dontlike pioneer with byso
    mi "Как бы ещё с Димой встретиться. Напомнить что он сегодня с нами играет."
    kt "Да я думаю он сам к нам прибежит. Он любит музыку, вряд-ли пропустит."
    mi "Если это музыкой назвать можно..."
    kt "Он мне говорил что любит всю музыку, потому в этом плане не нагоняй на него."
    show mi upset pioneer with byso
    mi "Когда это?"
    "Непритворно удивилась Мику."
    kt "Ну он так мне на ухо шепнул."
    show mi dontlike pioneer with byso
    "Мику немного обиделась."
    mi "Да, а я в музклубе должна была быть несколько смен одна."
    scene bg ext_houses_day
    show mi smile pioneer
    with byso
    stop music fadeout 3
    hide mi with byso
    "Выйдя к домикам, они по плану разошлись.{w} Константин направился к вожатой."
    scene bg ext_house_of_mt_day with byso
    play sound sfx_knock_door2
    play music music_list["lightness"] fadein 10
    "Постучав, Константин понял что в домике нет вожатой."
    th "Замечательно."
    scene bg int_house_of_mt_day with byso
    "Константин взял бутылку и спрятал за рубашку."
    scene bg ext_house_of_mt_day
    show mt surprise pioneer panama
    with byso
    play sound door_cl
    "Выйдя из домика, он встретил вожатую."
    mt "Чего ты тут делаешь?"
    kt "Вас искал. {w}Мы хотели спросить, есть ли на сцене освещение?"
    show mt normal pioneer panama with byso
    "Константин вывалил первую попавшуюся мысль. Вожатая задумалась."
    show mt surprise pioneer panama with byso
    mt "Не знаю, пощёлкайте выключатели, может что и заработает.{w} Вопрос не ко мне. Мне бумаги писать, так что я пойду."
    hide mt with byso
    play sound door_cl
    "Сказала вожатая и зашла в домик."
    th "Фух-х, мимо."
    scene bg ext_houses_day with byso
    "Константин побежал до клуба."
    scene bg musclub with byso
    play sound sfx_key_drawer
    "Добежав до дверей, он начал подбирать ключ."
    us "Чё бежал то?"
    show us smile pioneer with byso
    "Как оказалось за ним следила Ульяна."
    kt "А чего догоняла?"
    play ambience ambience_music_club_day
    scene bg int_musclub_day with byso
    play sound sfx_medpunkt_door_open
    "Вопросом на вопрос ответил Константин, открыв дверь клуба."
    us "Да я от нечем заняться."
    kt "А мне надо было кое-что положить в кладовку."
    scene bg int_wardrobe with byso
    "Сказал Константин и молниеносно кинул стеклянную бутылку на кучу сценической одежды на полу."
    th "Ну хоть не разбилась."
    kt "А так мы готовимся к выступлению."
    scene bg int_musclub_day with byso
    play sound sfx_key_drawer
    "Константин запер кладовку."
    us "Выступление это классно."
    scene bg musclub
    show us laugh pioneer
    with byso
    play ambience ambience_camp_entrance_day
    kt "Ну да."
    play sound sfx_key_drawer
    play sound2 door_cl
    "Сухо ответил он, запирая музклуб."
    us "Ну ладно, я убежала тогда."
    kt "Убегай."
    hide us with byso
    "Ульянка дала лыбу и побежала в сторону клубов."
    th "Без происшествий.{w} Хотя могли быть."
    th "Хм-м, а действительно, я не пил 3 дня.{w} Прогресс, ЗОЖ и прочие лозунги позитивизма."
    scene bg ext_square_day with byso
    stop music fadeout 3
    "Константин вышел на площадь."
    th "Даже вот спортом начал заниматься.{w} Бегаю как дурак туда-сюда."
    "Он про себя улыбнулся."
    th "Да и наконец научился играть на гитаре на высшем уровне.{w} Не сам конечно, но это без разницы."
    scene bg ext_stage_normal_day
    show mi normal pioneer far
    with byso
    "Дойдя до сцены, он заметил кибернетиков, которые подключали оборудование в сеть и Мику, которая его настраивала."
    show mi smile pioneer with byso
    play music music_list["silhouette_in_sunset"]
    mi "О, вернулся не запылился.{w} Успешно?"
    kt "Ага, могли бы быть проблемы, но обошлось.{w} Диму не видела?"
    show mi upset pioneer
    show el smile pioneer at right
    with byso
    el "А что, с вами играет Дима из 3го отряда?"
    kt "Допустим, тебе то что?"
    el "Он живёт по-соседству. {w}Круто на гитаре играет."
    kt "Сегодня он на барабанах."
    hide el with byso
    "Сказал Константин и вернулся в разговор с Мику."
    kt "Так что Дима?"
    show mi smile pioneer with byso
    mi "Видела.{w} Он сказал что через минут 20 ещё раз отрепетируем."
    kt "Класс. {w}Как техника?"
    rm "Угу, порядок.{w} Вы всё?"
    sh "Я да."
    el "Я тоже."
    rm "Всё, пошли отсюда, нам ещё паять и паять."
    el "Ладно, идём."
    hide mi
    show mi smile pioneer at right
    show image di_smile at left
    with byso
    "Кибернетики кучно ушли.{w} С их стороны пробежал Дима и тактично облетел их."
    dimas "Фух. На месте."
    kt "Чё как, собрался?"
    hide image di_smile
    show image di_angry2 at left
    with byso
    dimas "Ага, не без геморроя.{w} Начала вожатая по ушам кататься мол не положено сваливать."
    show mi normal pioneer at right with byso
    mi "И чего?"
    hide image di_angry2
    show image di_smile at left
    with byso
    dimas "Да ничего, меня завтра в 6 отец заберёт."
    "Сказал Дима, запрыгнув на сцену."
    hide image di_smile
    show image di_smile2 at left
    with byso
    dimas "Барабашки тут есть?"
    show mi surprise pioneer at right with byso
    mi "Чего?"
    dimas "Барабаны, ну чё ты."
    show mi dontlike pioneer at right 
    hide image di_smile2
    show image di_smile at left
    with byso
    kt "Сами не знаем."
    dimas "Тогда мы сами проверим."
    hide image di_smile with byso
    "Сказал Дима и зашёл за кулисы."
    mi "Скоро уже ужин, так что давай быстро там."
    dimas "А вот и она."
    play sound dvizh
    "Сказал Дима, волоча за собой установку. Вытащив установку, он забежал обратно."
    show mi angry pioneer at right with byso
    mi "Куда?.."
    dimas "А я чего, стоя играть буду, щас всё организую."
    show mi normal pioneer at right with byso
    mi "Ладно..."
    "Мику прицепила к гитаре ремень и надела на себя, сыграв пару аккордов."
    show image di_smile2 at left with byso
    "Дима вышел из-за кулис с табуретом."
    dimas "Вот это дело. Играем."
    show mi smile pioneer at right with byso
    kt "Момент."
    "Константин надел на себя гитару."
    kt "Раз, два, три, начали!"
    scene bg ext_stage_normal_day
    show image di_smile at left
    show mi laugh pioneer at right
    with fade
    play sound sfx_face_slap
    "Сыграв 1 прогон, они дали друг другу пять."
    dimas "Та-ак то. Взорвём сцену!"
    kt "Так точно!"
    mi "Взорвём!"
    play sound sfx_dinner_horn_processed
    "В подтверждение их слов заиграл горн."
    kt "А теперь за едой."
    hide image di_smile
    scene bg ext_dining_hall_near_sunset
    show mi smile pioneer at right
    show us smile pioneer
    show image di_smile at left
    with byso
    "У столовой их встретила весёлая Ульянка."
    us "Ничего себе вы играете!{w} Шикарно!"
    show mi dontlike pioneer at right with byso
    mi "А зачем ты подслушивала?"
    show us calml pioneer with byso
    "Ульяна на такие слова скорчила недовольное лицо."
    us "А вот захотелось мне."
    play ambience ambience_dining_hall_full
    stop music fadeout 3
    hide image di_smile2
    show image di_smile at left
    show mi normal pioneer at right
    with byso
    dimas "Да ладно вам.{w} На сцене будет ещё круче!"
    show us grin pioneer with byso
    us "Верю!"
    hide image di_smile
    scene bg int_dining_hall_people_sunset_cust
    show image di_smile2 at left
    show mi normal pioneer
    with byso
    "Весь коллектив зашёл в столовую."
    dimas "Ладно, тут сами, мне со своими ещё проститься надо."
    kt "Иди."
    hide image di_smile2 with byso
    "Нейтрально сказал Константин и подошёл к раздаче."
    "Повариха подала Мику и Константину макароны по-флотски с томатной пастой и стакан бледно-жёлтого напитка."
    show mi upset pioneer with byso
    "Поблагодарив повариху, они сели за свой столик."
    mi "Знаешь, рядом с Димой мне немного некомфортно."
    kt "Что, слишком активный?"
    mi "В точку.{w} Плюс эта его культура...{w} Как её... {w}Панк."
    kt "Ой, да ладно тебе, он завтра уедет."
    show mi smile pioneer with byso
    mi "Ну да, ты тоже прав.{w} Приятного аппетита."
    kt "Спасибо, тебе тоже."
    "Пока они если их никто не побеспокоил."
    show mi upset pioneer with byso
    "Константин допил свой лимонный напиток и начал сверлить взглядом Мику, которая задумчиво смотрела в окно."
    show mi serious pioneer with byso
    "Заметив на себе взгляд Константина, Мику начала смотреть в ответ с серьёзным лицом."
    show mi laugh pioneer with byso
    "Не выдержав долгого состязания в гляделки, она рассмеялась, Константин улыбнулся."
    kt "Ну чего, ты готова?"
    show mi smile pioneer with byso
    mi "Конечно!"
    kt "Ну тогда пошли."
    scene bg ext_dining_hall_near_sunset
    show mi happy pioneer
    with byso
    play ambience ambience_camp_entrance_evening
    "Сдав тарелки, они вышли на улицу, там стояло 3-4 отряда."
    show mt smile pioneer panama at right with byso
    "К ним подошла Ольга."
    mt "Идите вперёд. Дима вас там ждёт.{w} Как стемнеет вы начнёте концерт."
    kt "Принято."
    scene bg ext_square_sunset
    show mi normal pioneer
    with byso
    play music music_list["sweet_darkness"] fadein 5
    "Они вышли из толпы и пошли на сцену."
    show mi happy pioneer with byso
    mi "Может быть ещё раз сыграем вчерашнюю заодно?"
    kt "Хе, откуда у тебя вдруг такое желание?"
    show mi smile pioneer with byso
    "Мику глянула на закатывающееся солнце."
    mi "Да всё никак из головы не выходит.{w} Весь день напеваю."
    kt "М-м, ну давай, почему нет."
    play ambience ambience_camp_entrance_night
    scene bg ext_stage_big_night
    show mi smile pioneer at right
    show image di_think at left
    with byso
    "Солнце зашло.{w} На сцене они встретили Диму, который репетировал свою роль."
    hide image di_think
    show image di_smile at left
    with byso
    dimas "О, вы как раз!"
    show mi happy pioneer at right with byso
    mi "Да-да. Мы хотим ещё вчерашнюю песню сыграть, ты не против?"
    hide image di_smile
    show image di_smile2 at left
    with byso
    dimas "Я? Нет конечно.{w} Уступлю вам сцену. {w}Только не опозорьтесь там."
    "С ехидной улыбкой сказал Дима, раскрутив палочку в руке."
    stop music fadeout 3
    kt "Класс. Ну чего, ждём?"
    show mi shy pioneer at right with byso
    mi "Да, только настройки проверю."
    show mi smile pioneer at right with byso
    "Мику начала ковыряться в музыкальной карте."
    hide image di_smile2
    show image di_smile at left
    with byso
    play music music_list["a_promise_from_distant_days"] fadein 5
    dimas "А вы чего, какие планы на смену?"
    window hide
    menu:
        "Спокойная деятельность в клубе. Перерыв.":
            $ renpy.block_rollback()
            hide image di_smile
            show image di_angry2 at left
            with byso
            dimas "Бе-е, скучняк."
        "Поиграем ещё пару раз. От слова почему бы и нет.":
            $ renpy.block_rollback()
            $ miscore += 1;
            hide image di_smile
            show image di_smile2 at left
            with byso
            dimas "Во-о, это подход!"
    mi "Согласна с Костей."
    "Сказала Мику, достав старую гитарку."
    show mi happy pioneer at right with byso
    mi "Не хочешь вчерашнюю повторить?"
    kt "Не, так нормально.{w} Пусть пальцы хоть немного отдохнут."
    hide image di_angry2
    hide image di_smile2
    show image di_smile at left
    with byso
    dimas "Да, вот это правильно, а то без медиатора играть жуть жуткая."
    show mi smile pioneer at right with byso
    mi "Ну как хочешь."
    "Сказала Мику, отложив гитарку."
    "Спустя 15 минут, отряды уже начали рассаживаться."
    mi "Давайте, по позициям."
    "Мику поставила Константину микрофон на штативе."
    kt "{image=inrealnost/Pic/Spec/japan.png}{font=inrealnost/font/Naganoshi.ttf}ありがとう。{/font} \nСпасибо."
    show mi happy pioneer at right with byso
    mi "{image=inrealnost/Pic/Spec/japan.png}{font=inrealnost/font/Naganoshi.ttf}大丈夫ですよ。{/font} \nНе за что."
    hide image di_smile
    scene bg ext_scene_party
    show mi smile pioneer at right
    show image di_smile at left
    with byso
    "С улыбкой ответила Мику, включила освящение на сцене и встала на позицию."
    kt "Дим, напомни свой отряд."
    dimas "Третий."
    "Поправив волосы ответил Дима."
    kt "Хорошо, все готовы?"
    show mi happy pioneer at right with byso
    mi "Да!"
    dimas "Естественно!"
    "Константин подождал пока все усядутся и подошёл к микрофону."
    kt "Так, эта штука работает?.."
    pions "Да!"
    kt "Класс. {w}Итак, всем привет, дорогие товарищи.{w} Сегодня мы выступаем с особым гостем для нашего музклуба - Дима из третьего отряда!"
    hide image di_smile
    show image di_smile2 at left
    with byso
    dimas "Да-а-а, всем здарова, чуваки."
    play sound sfx_concert_applause
    "Пионеры похлопали Диме."
    kt "А так же Мику, глава нашего клуба!"
    show mi shy pioneer at right with byso
    play sound2 sfx_concert_applause
    "Публика захлопала.{w} Мику раскраснелась и молча поклонилась."
    kt "И сейчас мы исполним песню под названием <<По ту сторону весны>>. Аплодисменты!"
    stop music fadeout 2
    kt "Раз-два-три, полетели!"
    show mi happy pioneer at right with byso
    play music dosvidosh fadein 3
    "Мику начала наигрывать первые аккорды."
    kt "Ла-ла, ла-ла, ла-ла-ла-ла-ла..." 
    "Константин уже второй раз выступал на сцене. {w}Несмотря на свою прошлую жизнь он разошёлся не на шутку."
    "Именно о таком он думал в зимние вечера, мечтал о таком и думал почему его жизнь никогда не была таковой."
    "Однако она стала.{w} Теперь Константин чувствует себя совершенно иначе."
    "Сейчас всё изменилось.{w} Есть клуб, есть интересные дела и веселье. Теперь у него не осталось злобы на жизнь." 
    "Последний аккорд."
    stop music fadeout 3
    th "И-и, аплодисменты!"
    play sound sfx_concert_applause
    show mi shy pioneer at right
    hide image di_smile2
    show image di_smile at left
    with byso
    "Зал, несмотря на меньшее количество народу хлопал пуще вчерашнего."
    kt "А теперь в повторение вчерашнего сейчас для вас прозвучит <<Моя оборона>>!"
    hide mi
    hide image di_smile
    show mi smile pioneer
    with byso
    "Константин снял с себя гитару и взял другую.{w} Мику встала на место Константина, а Дима показал зрителям <<козу>> и прыгнул в их ряды."
    play music "<from 3>inrealnost/Music/Music/mi_sing.mp3" fadein 1
    "Зал замолчал. Константин начал наигрывать аккорды."
    scene bg mi_scene with byso
    "Мику пела текст лучше чем вчера, попадая в каждую ноту, которую Константин воспроизводил гитарой."
    "Они сыгрались настолько хорошо, что их игра не сильно отличалась от оригинальной.{w} Как так вышло неизвестно, остаётся загадкой этого мира."
    "Тем не менее это ни в коем разе не смущало Константина.{w} Он сильно сократил количество своих пожирающих мыслей, благодаря чему ему стало проще жить."
    "И он наконец понял что его жизнь стала больше чем простое существование."
    scene bg ext_scene_party
    show mi happy pioneer
    with byso
    stop music fadeout 3
    play sound sfx_concert_applause
    "Последний аккорд.{w} Сцена снова осыпалась градом аплодисментов."
    hide mi
    show mi smile pioneer at right
    with byso
    "На сцену двигалась вожатая.{w} Мику взяла микрофон в руки."
    play music warm_evening fadein 3
    mi "Спасибо за внимание и всем хорошего вечера!"
    "Подошла Сахарова и взяла микрофон."
    show mt smile pioneer at right with byso
    mt "Пионеры и пионерки, наш мини-концерт окончен. {w}Собирайтесь со своими вожатыми и идите на свечку. Мой отряд, поднимайтесь на сцену."
    scene bg ext_stage_normal_night
    hide mt
    hide mi
    show mi happy pioneer at right
    show image di_smile2
    with byso
    "Началась суета.{w} Дима подбежал к Мику и Константину."
    dimas "Друзья, спасибо вам огромное, я рад что смог так круто провести время в вашей тусе.{w} Мы скорее всего больше не увидимся, так что прощайте!"
    "Дима подошёл и обнял их обоих."
    show mi smile pioneer at right with byso
    mi "Тебе спасибо, будем скучать!"
    kt "Давай, друг, рад был поболтать!"
    hide image di_smile2
    show image di_smile at left
    with byso
    hide image di_smile
    hide mi
    show mi happy pioneer
    with byso
    "Дима отпустил Мику и Константина, после чего отдал честь и убежал за своим отрядом.{w} Весь отряд Константина уже собрался на сцене."
    pions "Молодцы.{w}.. Ваше выступление класс.{w}.. И как вы успели."
    show mi shy pioneer with byso
    "Почти в один голос спрашивали участники других клубов.{w} В ответ Мику взяла Константина за руку и они поклонились."
    hide mi
    show mt grin pioneer
    with byso
    mt "Так, располагайтесь поудобнее."
    "Пионеры других отрядов уже ушли.{w} Ольга села на доски и достала фонарь."
    mt "Ребята, кучнее и в круг."
    show mt smile pioneer
    show sl smile pioneer at right
    with byso
    "Константин сел спиной к кулисам сцены, справа от него села Мику, а слева вожатая."
    "Вожатая достала спички, зажгла толстую свечу и вставила её в фонарь."
    mt "Итак друзья.{w} Исполняя традицию нашего лагеря, сегодня у нас свечка.{w} Каждый может оставить своё слово для остальных."
    hide mt
    hide sl
    show mt grin pioneer at left
    show sl smile2 pioneer
    show mz bukal pioneer glasses at right
    with byso
    "Вожатая передала свечку Славе."
    sl "Говорить может только тот у кого в руках свечка.{w} Остальные могут только тихо похлопать под конец выступления."
    sl "Итак, я начну.{w} Я очень рада что нахожусь тут с вами уже какую смену.{w} Каждый раз я снова и снова влюбляюсь в это место."
    sl "Я рада что нахожусь в нашем прекрасном и дружном отряде..."
    th "Бла-бла-бла...{w} Балобольства больше чем сути."
    hide mt
    hide sl
    hide mz
    show sl smile pioneer at left
    show mz angry pioneer glasses
    show un normal pioneer at right
    with byso
    "Как только Славя закончила свою нудную речь, похлопала только вожатая.{w} Свеча перешла к Жене."
    mz "Ну чего мне сказать собственно, я рада быть в этом отряде и бла-бла-бла.{w}.. Возвращайте книги вовремя."
    hide un
    hide sl
    hide mz
    show mz bukal pioneer glasses at left
    show un shy pioneer
    show sh normal pioneer at right
    with byso
    "Женя передала Свечку Лене."
    un "С-спасибо за хорошую смену."
    hide un
    hide mz
    hide sh
    show un shy pioneer at left
    show sh normal_smile pioneer
    show image rm_th at right
    with byso
    "Лена передала свечу Шурику."
    sh "Спасибо.{w} Хочу сказать спасибо своему клубу за удачную работу.{w} Скоро мы представим свою новую разработку и я обещаю, вы все будете приятно удивлены."
    sh "Приходите в клуб кибернетики мы ждём всех."
    hide un
    hide sh
    hide image rm_th
    show sh upset pioneer at left
    show image rm_sm
    show el normal pioneer at right
    with byso
    "Сказал он и передал фонарь Роме."
    rm "Мой коллега по цеху сказал всё верно.{w} Приходите.{w} Ещё я рад за наш талантливый музклуб. {w}Не знал что некоторые могут быть настолько талантливыми."
    hide el
    hide sh
    hide image rm_sm
    show image rm_sm at left
    show el smile pioneer
    show dv smile pioneer at right
    with byso
    "Рома с едкой лыбой передал фонарь Электронику."
    el "В нашем клубе всегда много интересного, так что записывайтесь."
    hide el
    hide dv
    hide image rm_sm
    show el normal pioneer at left
    show dv grin pioneer
    show us normal pioneer at right
    with byso
    "Электроник передал фонарь Алисе."
    dv "Я рада что у нас в музклубе есть ребята со вкусом!{w} Если нужны будут лишние руки - зовите!"
    hide el
    hide dv
    hide us
    show dv smile pioneer at left
    show us grin pioneer
    show mi normal pioneer at right
    with byso
    "Алиса передала свечу Ульянке."
    us "О, наконец я! Я рада быть в этом отряде."
    "Она глянула на Алису."
    us "Тут мои друзья, матчи, много всего весёлого и я буду рада приехать на ещё одну смену."
    show us smile pioneer with byso
    us "Завтра у моей команды матч, чтоб были все!"
    hide dv
    hide us
    hide mi
    show mi smile pioneer
    with byso
    "С ухмылкой сказала Ульянка и передала свечку Мику."
    mi "Я думаю я всё сказала в своей песне.{w} Спасибо что поддержали на таком тяжёлом выступлении, а отдельное спасибо Константину, без него бы то всё не вышло."
    show mi happy pioneer with byso
    "Мику с милой улыбкой передала свечу Константину."
    kt "Хм.{w}.. Что-ж сказать."
    window hide
    menu:
        "Думаю, все уже всё сказали, мне сказать нечего.":
            $ renpy.block_rollback()
            kt "Всем спасибо за внимание."
        "Спасибо за интересную смену.":
            $ renpy.block_rollback()
            kt "И за внимание тоже."
        "Очень раз новым знакомствам, полученным тут.":
            $ renpy.block_rollback()
            $ miscore += 1;
            kt "На этой смене я смог познакомиться с классной девочкой и я безусловно рад этой встрече."
            kt "Хочу сказать ей огромное спасибо."
        "Эта смена стала лучшей для меня.":
            $ renpy.block_rollback()
            kt "На этой смене было много веселья, я рад что приехал сюда и получил хороший опыт благодаря некоторым людям."
            kt "Возможно я приеду сюда ещё раз. {w}Спасибо за внимание."
    hide mi
    show mt grin pioneer
    with byso
    "Константин вернул свечу вожатой."
    mt "Чтож, на этом наша прекрасная свечка заканчивается."
    stop music fadeout 3
    "Вожатая задула свечку в фонаре."
    show mt smile pioneer with byso
    mt "А теперь все по домикам. {w}Всем спокойной ночи."
    "Отряд стал расходиться."
    kt "Ольга Дмитриевна!"
    mt "Да-да?"
    kt "У нас в клубе дела, ничего если мы чуть позже на отбой пойдём?"
    show mt grin pioneer with byso
    "Вожатая разулыбалась."
    mt "Конечно.{w} Вы молодцы, представление высший класс."
    kt "Это значит что мы можем рассчитывать на отдых завтра?"
    show mt smile pioneer with byso
    "Вожатая хитро ухмыльнулась." 
    mt "А вот это не факт.{w} Вы отдыхали сегодня и не просили ничего в замен."
    th "М-м-м, да-да, да-а."
    show mi upset pioneer at right with byso
    mi "Ладно, мы пойдём."
    mt "Идите. В половину двенадцатого в домик."
    scene bg ext_houses_night
    show mi upset pioneer
    with byso
    play music music_list["sweet_darkness"] fadein 10
    "Мику и Константин пошли к клубу."
    kt "Вот же меркантильная..."
    show mi dontlike pioneer with byso
    mi "... сучка."
    "Константин усмехнулся."
    kt "С языка сняла. Ну, портвейн нас точно не обидит."
    show mi happy pioneer with byso
    mi "Согласна."
    scene bg int_wardrobe
    show mi normal pioneer
    with byso
    play sound sfx_lock_close
    play sound2 door_cl
    play ambience ambience_music_club_night
    stop music fadeout 3
    "Константин открыл дверь и вошёл, а Мику щёлкнула кнопкой выключателя."
    kt "Слушай, а о ёмкостях мы не подумали..."
    show mi happy pioneer with byso
    mi "Почему же не подумали?{w} У меня есть пара-тройка чашек."
    "Константин с удивлённым видом потёр подбородок."
    kt "Солидно.{w} Ну куда сядем?"
    show mi shy pioneer with byso
    mi "Тут.{w} Мало ли кто в клуб нагрянет."
    kt "Разумно."
    show mi smile pioneer with byso
    play music Gallow
    "Они сели за небольшой столик что стоял в углу."
    "Константин достал из тряпок бутылку портвейна."
    show mi happy pioneer with byso
    mi "М-м-м, <<777>>"
    kt "Он самый!"
    "Константин вскрыл бутылку и разлил поровну."
    show mi grin pioneer with byso
    mi "Ух, давно я не пила алкоголя."
    "Сказала Мику, взяв в руку чашку."
    kt "Да, у вас же в Японии можно курить и пить только с 21 года."
    show mi happy pioneer with byso
    mi "Не-а, не угадал, с 20ти."
    "Константин пожал плечами."
    kt "Ладно, ну что, за вечер?"
    show mi smile pioneer with byso
    mi "Давай."
    "Раздался стук кружек."
    show mi upset pioneer with byso
    "Константин выпил часть кружки словно это была вода, а Мику напротив, отпила немного и тяжело выдохнула."
    show mi grin pioneer with byso
    mi "Ух, ядрёный.{w} А ты я смотрю как лимонадик пьёшь."
    "Константин улыбнулся."
    kt "Да, есть такое. Ты не куришь кстати?"
    show mi normal pioneer with byso
    mi "Пробовала, но нет."
    kt "М-м, понятно."
    kt "Кстати, тебя никогда не посещало чувство что ты немного не в своём мире?"
    show mi upset pioneer with byso
    "Мику сильно удивилась вопросу и отпила ещё немного портвейна."
    mi "Как не странно, но да.{w} Каждый день. Только об этом и думаю.{w} Сегодня особое обострение."
    mi "Как вариант из-за появления Димы."
    kt "А чего так?"
    show mi sad pioneer with byso
    "Мику заглянула Константину в глаза."
    mi "Он говорит что уже не первую смену тут, но до этого я его ни разу не видела..."
    mi "Ну вот вообще."
    kt "Да уж, такого хрен забудешь..."
    mi "Вот а я о чём.{w} Да и осложняется это тем что у меня есть проблема с многоуровневыми снами."
    kt "О-о, у меня так-же было в городе."
    mi "Тогда ты понимаешь какого это так спать."
    "Мику и Константин почти синхронно допили портвейн и Константин долил в обе кружки."
    kt "За что на этот раз."
    show mi smile pioneer with byso
    mi "Давай за правду."
    kt "Прекрасно.{w} За правду."
    "Они снова чокнулись."
    show mi upset pioneer with byso
    mi "Знаешь.{w}.. Мне надо кое-что тебе рассказать..."
    th "Давно я не слышал таких слов."
    kt "И что же?"
    show mi sad pioneer with byso
    "Мику грустно посмотрела в пол."
    mi "Это про сегодняшний кошмар.{w} Весь день из-за него не могу в себя прийти."
    mi "Ты не подумай, я не сумасшедшая, но этот мир не мой."
    "Константин услышав это взял кружку портвейна."
    mi "Я родилась не там где СССР, а где Россия..."
    mi "И знаю я тебя именно в том детстве."
    "Константин залпом допил."
    kt "То есть, ты мне хочешь сказать ты тоже путница?.."
    show mi shocked pioneer with byso
    mi "Дай дог... Стоп, всмысле <<тоже>>?!"
    "Мику пришла в шок от услышанного."
    kt "Брусков Константин Павлович."
    kt "1997 год рождения."
    kt "Должность - бухгалтер среднего звена."
    kt "Год попадания сюда 2022."
    show mi scared pioneer with byso
    hide mi with byso
    play sound sfx_bodyfall_1
    play music the_date_of_death fadein 1
    "Мику в шоковом состоянии посмотрела сначала на портвейн, где стояла дата изготовления 14.08.2022, затем на Константина и упала в обморок."
    kt "Мику!"
    "Константин вскочил со стула и потряс Мику за плечо."
    show mi sad pioneer with byso
    "Взяв лежащий рядом пульверизатор и попшикал на Мику. В ответ она вскочила на ноги, осмотрелась и села за стол."
    kt "Что с тобой?"
    mi "Я вспомнила.{w}.. Всё вспомнила..."
    "Константин сел напротив и долил портвейн."
    mi "Я поняла почему ты меня не помнишь..."
    mi "Моё имя.{w}.. Маша."
    kt "Маша?!"
    #Рандомный вброс. Во флешбеке реальные события из моей жизни. С днем казни Чикатило кста 14.02.2023
    stop ambience
    play sound in_vosp
    scene bg ext_bathhouse_night
    show shum_white
    with flash
    ks "Деда, кто там?"
    de "Это к тебе."
    ks "Ко мне? Кто?"
    de "Выходи, увидишь."
    "Костя вышел на веранду и увидел низкую девочку с чёрными волосами и желтоватой кожей."
    de "Это Маша.{w} Внучка наших соседей, она приехала из Японии."
    ma "{image=inrealnost/Pic/Spec/japan.png}{font=inrealnost/font/Naganoshi.ttf}こんにちは。"
    ma "Ой...{w} То есть привет."
    "Девочка сильно раскраснелась и засмотрелась в пол.{w} Костя протянул руку."
    ks "Привет, я Костя, рад знакомству."
    hide shum_white
    scene bg les
    show shum_white
    with flash
    "Спустя год. Костя гуляет с Машей по лесу."
    ma "Тут такое дело...{w} Я уезжаю. И не вернусь больше."
    ks "Что? Почему?"
    ma "Мой отец поссорился с моей мамой... Теперь она хочет чтобы я вернулась в Японию."
    "Костя пнул камень под ногой."
    ks "А помириться они не хотят?"
    ma "Кажется что нет, это конец..."
    "Костя взял Машу за плечи."
    ks "Ну.{w}.. Раз так, то не унывай.{w} Тебе ещё только 14 лет, всё впереди."
    "Маша обняла Костю."
    ma "Спасибо тебе."
    hide shum_white
    scene bg int_wardrobe
    show mi sad pioneer
    with flash
    "Константин ошеломлённо смотрел в пол."
    ma "В ноябре 2022го я покончила с собой. Я хотела просто нормально жить, но мои однокурсницы меня унижали.{w} Меня били, меня высмеивали и даже преподаватели надо мной издевались."
    ma "Вместо того чтобы умереть я встретилась с Гендой.{w}.. Он меня исправлял, но сделал вид что не вышло и стёр всю память..."
    show mi upset pioneer with byso
    stop music fadeout 2
    ma "И теперь я тут.{w}.. Это не моё тело.{w}.. Я не красила волосы, но мой натуральный цвет всё ещё чёрный, это видно по корням."
    show mi sad pioneer with byso
    play music Gallow
    ma "Но... Как ты попал сюда?"
    "Константин рассмеялся."
    kt "Ты не поверишь, но я был признан самым бесчеловечным террористом в городе..."
    "Константин кратко пересказал встречу с Гендой и всё что ему удалось пережить."
    show mi upset pioneer with byso
    ma "Да-а... И как мы до такого докатились..."
    "Константин и Маша допили портвейн и Константин налил последние две кружки."
    kt "Общество... Всё общество."
    kt "Тебя унижали за то что ты наполовину русская и на другую японка, меня унижали за многое другое."
    kt "Знаешь что? Ты не видела во снах пионера?"
    show mi scared pioneer with byso
    ma "Какого пионера?"
    kt "Потерянный пионер.{w} Он со мной с первого дня."
    show mi sad pioneer with byso
    "Маша отпила портвейна."
    ma "Нет.{w} До сегодняшнего дня я не видела снов."
    kt "Понятно... Но видимо тебя сегодня тоже ожидает кошмар."
    ma "Кошмар?"
    kt "Долгая история.{w}.. Узнаешь."
    "Константин мигом опустошил свой стакан."
    kt "Интересно, что скажет Генда, узнав про то что ты вернула себе память."
    show mi upset pioneer with byso
    ma "Боюсь даже думать.{w}.. Он достаточно вспыльчив."
    "Константин встал со стула, его слегка пошатывало.{w} Маша допила свой портвейн и пошла прятать бутылку."
    show mi sad pioneer with byso
    ma "Поверить не могу.{w} Я жила столько времени без собственной памяти даже того не осознавая.{w}.. Да и вообще... <<Мику>>... Жуть какая."
    "Константин повернулся к Маше."
    kt "Да-а... Представляю."
    show mi cry_smile pioneer close with byso
    "Маша заглянула в глаза Константину и крепко обняла его."
    ma "Знаешь... В Японии я нередко про тебя вспоминала.{w} Ты был единственным, кто не отвергал меня."
    ma "Осталась бы я с папой, возможно многое бы изменилось."
    kt "Возможно в моей жизни бы тоже..."
    "Маша поцеловала Константина.{w} Константин такого совершенно не ожидал."
    show mi shy pioneer with byso
    "Она отошла и покраснела."
    ma "Прости, не знаю что на меня нашло..."
    window hide
    menu:
        "Подойти и обнять.":
            $ renpy.block_rollback()
            $ miscore += 1;
            show mi shy pioneer close with byso
            "Маша не ожидала ответной реакции от Константина."
            kt "Нет ничего страшного в том чтобы проявлять эмоции.{w} Я понимаю что общество учило тебя другому, но забудь.{w} У нас обоих новая жизнь."
            show mi cry_smile pioneer close with byso
            "Маша обняла Константина."
            ma "Спасибо.{w}.. Спасибо, Костя..."
            "Спустя пол-минуты они отлипли друг от друга."
        "Простить.":
            $ renpy.block_rollback()
            kt "Ничего, забудь."
    show mi smile pioneer with byso
    kt "Ладно.{w} Надо по домам. Завтра ещё наговоримся."
    scene bg ext_square_night
    show mi upset pioneer
    with fade
    play ambience ambience_camp_entrance_night
    ma "А ты никогда не думал про мотивацию Генды нас тут содержать?"
    "Константин почесал подбородок."
    kt "Не могу сказать.{w} По сути он просто чувак с комплексом спасателя в крайне искажённой форме."
    kt "Сказал бы более исчерпывающим определением, но я просто не знаю."
    kt "Кстати, ты на кого училась?"
    show mi sad pioneer with byso
    ma "Я так и училась в консерватории классической музыки.{w} Хотела стать певицей. {w}Справедливо будет заметить что не вышло."
    kt "Да нет, почему? Поёшь вроде хорошо."
    show mi smile pioneer with byso
    "Маша улыбнулась."
    ma "Рада что тебе нравится."
    scene bg ext_house_of_mi_night
    show mi upset pioneer
    show un shy pioneer far at right
    with byso
    "Константин с Машей дошли до домика.{w} На ступеньках сидела Лена."
    kt "Ладно, {i}Мику{/i}, увидимся."
    show mi dontlike pioneer close with byso
    "Маша обняла Константина."
    ma "Очень смешно.{w} Спокойной ночи."
    kt "Спокойной."
    hide mi with byso
    hide un with byso
    stop music fadeout 3
    play sound door_cl
    "Маша вошла в домик а за ней и удивлённая Лена."
    scene bg ext_house_of_mt_night with byso
    "Константин дошёл до домика."
    scene bg int_house_of_mt_night
    show mt smile pioneer
    with byso
    play sound door_cl
    play ambience ambience_int_cabin_night
    "Войдя в домик он заметил Ольгу, которая писала бумаги."
    mt "Ты вовремя. {w}Ложись спи, я тоже сейчас пойду."
    kt "Угу."
    scene bg int_house_of_mt_night2 with byso
    "Вожатая выключила свет."
    stop ambience fadeout 3
    show blink
    "Константин снял рубашку и шорты, после чего лёг и моментом уснул."
    scene bg cafe
    show unblink
    play music music_list["torture"] fadein 2
    "Очнулся он на стуле в уже знакомом зале."
    gg "Здравствуй.{w} Рад меня видеть?"
    kt "Ну привет.{w} Не то что бы."
    show image so_gd with byso
    "Генда поправил очки и через спину глянул на Константина."
    gg "Тебе знакомо понятие стабильность?"
    kt "Да, эмоциональная.{w} То чего у тебя нет."
    hide image so_gd
    show image so_sm
    with byso
    "Создатель усмехнулся."
    gg "Шутки шутишь?{w} Это хорошо.."
    hide image so_sm
    show image so_gd
    with byso
    "Создатель подошёл к стулу на котором сидел Константин."
    gg "Но если тебе это понятие знакомо то слушай. С твоим появлением кое-кто портит мне стабильность инреальности. Не хочешь мне ничего рассказать?"
    kt "Нет, знать бы ещё чего ты опять несёшь."
    gg "Хм-м, ладно, допустим, но если ты это знаешь, то тебе мало не покажется."
    "Грозно проговорил создатель."
    hide image so_gd
    show image so_sm
    with byso
    "Его выражение лица быстро сменилось на улыбку и он отошёл от Константина."
    gg "Сегодня у нас блекджек.{w} Играешь на фишки. Если до 3й игры у тебя вылетят все фишки то ты не проснёшься."
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
    th "Ещё один человек."
    kt "Здравствуй."
    "Семён лишь молча занял положение у стола."
    th "Быдло."
    me "Вот фишки."
    play sound kosti
    "Он достал из стола 2 фишки и дал их Константину."
    kt "А вы чё без фишек?"
    gg "На твою-ж жизнь играем а не на мою.{w} А он, так уж и быть, умрёт если ты выиграешь."
    th "М-м..."
    play sound card_mix
    me "Тасую колоду."
    "Семён быстро размешал карты и раздал по две каждому. {w}Свои он выложил на стол рубашкой вниз. Валет черви и король буби."
    play sound card_take
    "Константин украдкой глянул на карты. {w}У него была десятка и четвёрка пики."
    gg "Я возьму одну."
    play sound card_take
    "Семён выдал карту Генде."
    gg "Стоп."
    me "Беру карту."
    play sound card_take
    "Пятёрка черви."
    me "На столе перебор."
    th "Дурак чтоль с 20 карты брать?"
    play sound card_take
    kt "Ещё."
    "Генда непрерывно смотрел на Константина.{w} Константин подобрал шестёрку треф."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            $ gameoverr += 1
            play sound card_take
            "Константин получил двойку пик. Перебор."
            th "Да, я тоже дурак походу."
            hide image so_gd
            show image so_sm at cright
            with byso
            gg "Первый кон - первый пролёт.{w} Ну, в следующей жизни повезёт."
            "Жетон со стола Константина пропал."
        "Стоп.":
            $ renpy.block_rollback()
            me "Игроки, вскрывайтесь."
            play sound card_take
            "У Генды в сумме было 19. Он улыбнулся."
            kt "Выкуси, 20."
            play sound card_take
            "Константин выложил свои карты."
            hide image so_gd
            show image so_sm at cright
            with byso
            gg "Ну, поздравляю, живёшь пока."
    play sound card_mix
    "Семён снова перетасовал колоду."
    play sound card_take
    "На столе лежала четвёрка буби и король буби."
    me "Беру карту."
    play sound card_take
    "На стол попала дама черви."
    me "На столе перебор. Генда?"
    gg "Я при своих."
    "Сказал он и насмешливо посмотрел на Константина. У него был валет и девятка треф."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            $ gameoverr += 1
            play sound card_take
            "Валет пики. Пролёт."
            gg "Хе-хе."
        "Стоп.":
            $ renpy.block_rollback()
            me "Игроки, вскрывайтесь."
            play sound card_take
            "У Генды был туз, тройка и шестёрка. Константин вышел в ничью, но у него было меньше карт."
            gg "А тебе сегодня везёт, ничего не сказать."
if gameoverr ==2:
    jump Poker_Death
else:
    jump fgk0pdsgjsdfopigjsfuiodjguiosjdguiosfjgoui
label fgk0pdsgjsdfopigjsfuiodjguiosjdguiosfjgoui:
    hide image so_sm
    show image so_gd at cright
    with byso
    play sound card_mix
    me "Тасую колоду."
    hide image me_no
    show image me_su at left
    with byso
    play sound card_take
    play sound card_take
    "Семён размешал карты и раздал по две.{w} Его руки дрожали. На столе 12."
    me "Б-беру карту."
    play sound card_take
    "Дама пик."
    hide image me_su
    show image me_st at left
    with byso
    me "На столе п-п...{w} Н-нет...{w} Я не хочу!"
    play sound flame_up
    hide image me_st
    hide image so_gd
    show image so_gd at cright
    with flash
    "Семён самовоспламенился и начал в огне кричать и кататься по полу пока не утратил такую способность."
    hide image so_gd
    show image so_sm at cright
    with byso
    gg "Ну дурак, нет?{w} Не бери ты карты постоянно...{w} Ничего вас людей не учит."
    "Константин, пытаясь не подавать волнения посмотрел в карты. 9 и 2 черви."
    window hide
    menu:
        "Ещё.":
            $ renpy.block_rollback()
            "Константин вытащил даму черви и выложил карты на стол."
            play sound card_take
            kt "Двадцать одно."
            "Генда снова удивлённо посмотрел на Константина, но потом рассмеялся."
        "Стоп.":
            $ renpy.block_rollback()
            $ gameoverr += 1
            gg "А я возьму одну."
            play sound card_take
            "Генда взял карту, рассмеялся и выложил на стол даму черви, короля пики и туза черви."
if gameoverr == 2:
    jump Poker_Death
else:
    jump ga9usfjgjfa9uosghnjuaofspghjni9ogpaaafnujgi
label ga9usfjgjfa9uosghnjuaofspghjni9ogpaaafnujgi:
    gg "Молодец, отстоял право на жизнь, теперь в кошмар."
    stop music fadeout 1
    show blink
    pause 1
    hide image so_sm
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
    scene bg ext_house_of_mt_night_without_light with vpunch
    "Константин вышиб дверь и побежал в указанном направлении."
    scene bg ext_square_night_blood
    show image me_st at left
    show image monster at right
    with fade
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
    "Череп был сильно вытянут и видоизменён.{w} Сразу было видно что бог не прилагал свою заботу к этому существу."
    scene bg ext_houses_night with byso
    "Константин решил не задерживаться и побежал дальше."
    scene bg int_old_building_night with byso
    stop music fadeout 3
    "Добежав до старого корпуса, он быстро забежал по лестнице."
    th "Второй этаж.{w}.. Комната слева..."
    show image poter_n at left
    show mi cry pioneer at right
    with byso
    play music ToxiSector fadein 10
    "Зайдя в нужную комнату он встретил Машу и Пионера."
    "Маша сидела в углу и плакала, а пионер задумчиво курил сигарету."
    kt "Я пришёл."
    show mi cry_smile pioneer at right with byso
    ma "Костя?!"
    show mi cry_smile pioneer close at right with byso
    "Маша вскочила с места и обняла Константина."
    pp "Если ты думашь что это твой сон, то ты ошибаешься, он всё это запомнит.{w} Здравствуй, Константин."
    kt "Ничего, я её понимаю. Привет вам."
    "Константин обнял трясущуюся Машу."
    kt "Ты ей чего такого нарассказывал?"
    pp "Я? Ничего. {w}Просто пока я вёл её до сюда, монстр разорвал в клочья Семёна.{w} Как мы с тобой в первый день встретились."
    "Константин поглаживал Машу по спине, она стала дрожать чуть меньше."
    kt "Генда сегодня сжёг его. {w}Кто вообще этот Семён?"
    pp "Поправочка. Семён-ы.{w} Это безвольные существа, которые как и вы, скорее всего ранее были путниками, но с моей точки зрения не факт.{w} Возможно это порождения инреальности."
    ma "Т-то есть... Он бы сделал нас Семёнами?"
    pp "Не-а, тебя бы он сделал Мику.{w} Тоже стандартный персонаж."
    show mi sad pioneer at right with byso
    "Маша немного успокоилась и отлипнув от Константина села на пол."
    kt "Так, а что такое инреальность и стабильность?"
    "Пионер достал мальбро голд и закурил."
    pp "По порядку. Это кошмар - место пыток путников.{w} Сюда попадают все кроме потерявших самосознание Семёнов и других обитателей лагеря."
    pp "Симуляция - ваш мир с вашими пустышками и возможно путниками."
    pp "Для Маши.{w} Путник - человек который всё ещё способен осознать то что находится не в родном мире.{w} Пустышка - антоним путника или просто население пустых симуляций."
    pp "Далее.{w} Инреальность - совокупность всех симуляций Генды."
    pp "Потом.{w} Стабильность представляет собой величину от 100 до -100, где 100 это абсолютное равновесие, а -100 разрушение мира.{w} В нуле мир соединяется с кошмаром."
    "Пионер затянулся."
    pp "С того момента можно считать что мир утерян."
    pp "Ладно, мы ушли от темы."
    pp "Не знаю как, но это и в правду твоя знакомая.{w} 2022 год попадания, ноябрь."
    pp "Либо вам ужасно повезло встретиться, либо это не случайность и Генда намеренно вас сселил."
    show mi scared pioneer at right with byso
    ma "И такое будет каждую ночь?"
    show mi sad pioneer at right with byso
    pp "Ага, правда боюсь продлится это не долго."
    kt "В каком смысле?"
    pp "С твоим днём попадания нечто начало ломать симуляции.{w} Яростно... Ломать."
    pp "Чтоб обнулить стабильность достаточно убить хотя бы одного путника или Семёна на территории симуляции."
    pp "После чего может появиться возможность перепрыгнуть в другую симуляцию."
    th "Вот представим, одна бактерия стала обладать несвойственными качествами.{w}.. Как не странно я думал об этом на работе..."
    pp "Так и вот.{w} Некая рыжая девочка скачет по симуляциям и крошит всё и вся."
    "Пионер выкинул бычок и в его руках образовалась багряная книжечка с названием <<Цена грехов>>."
    pp "Я зачитаю."
    pp "Влад Козлов. Пропустим немного шелухи, короче в 2020м попал в инреальность."
    stop ambience
    scene bg ext_bus_night
    show shum_white
    with flash
    "Очнулся он в пустоте. {w}Пред ним был лишь образ девочки."
    deva "Ты пойдёшь со мной?"
    vlad "Да, почему нет..."
    "Влад проснулся в автобусе."
    pp "Знакомство с лагерем, бла-бла-бла..."
    hide shum_white
    scene bg ext_washstand_day
    show shum_white
    with flash
    slp "Физкульт-привет!"
    vlad "О, хай... То есть, бобр... Доброе утро!{w} Вот..."
    "Приветствие ему удалось подобрать не сразу."
    slp "Почему на завтрак не пришёл?"
    vlad "Проспал."
    "Он сказал это так, словно гордился своим достижением."
    vlad "Но мне вожатая бутерброды принесла."
    slp "А, ну отлично тогда! Не забудь про линейку!"
    vlad "Да, конечно."
    "Пионерка ушла, Влад продолжал умываться."
    "Закончив умываться, он засмотрелся в стену, как вдруг кто-то схватил его за плечо."
    gren "А ты не похож на Семёна... Обернись. М-е-д-л-е-н-н-о."
    "Влад киношно поднял руки и обернулся. Перед ним стояла девочка в белом платье и берете.{w} На её коричневых кожаных сапогах было подшиты округлые лезвия, которые были испачканы чем-то красным."
    vlad "Воу-воу, ты к апокалипсису чтоль готовишься?"
    rep "Возможно. Давай не будем тянуть резину. Имя, дата попадания и пожелания."
    "Влад опустил руки и почесал затылок."
    vlad "Та-ак, зовут Влад, 20 лет, не женат, но хотел бы быть.{w}.. Сейчас вроде как 2020, но не похоже... А что за пожелания?"
    rep "Оригинальная симуляция, я похоже совсем близко..."
    "Пробормотала про себя девочка и достала длинный нож, Влад начал пятиться."
    rep "Пожелания опционально, сама уже придумаю как тебя порезать."
    "Девочка в миг подлетела к Владу и ударом ноги повалила его на спину."
    vlad "Помогите! Убивают!!!"
    "Она лишь с истеричным смехом начала вознать нож в тело Влада."
    "Грудь, плечи, шея.{w} Нож не оставил ни одного места на теле влада без внимания."
    "Вспоров Владу живот, она сделала хирургически точный удар в сердце, пробив рёбра."
    rep "Прощай, рада была что это не затянулось."
    "Обтрев нож об рубашку Влада, она встала и убежала в сторону площади."
    "Спустя 10 секунд Влад отключился.{w} Навсегда."
    hide shum_white
    scene bg int_old_building_night
    show mi scared pioneer at right
    show image poter_n at left
    with flash
    pp "Повествование 23ей души завершено."
    kt "Жуть..."
    "Сказал Константин и почесал затылок."
    ma "Она... {w}Безумна..."
    pp "Ага, её и разыскивает Генда.{w} Она уничтожила на данный момент..."
    play sound sfx_paper_bag
    "Пионер пролистал книжку и она испарилась."
    pp "548 симуляций. За три наших дня!"
    show mi sad pioneer at right with byso
    ma "А сколько их всего?.."
    pp "В районе 10000.{w} Вероятность попадания к вам сами подумайте."
    kt "Плохо..."
    pp "Завтра вам просто необходимо взять из подвала библиотеки четвёртое писание."
    kt "Что это?"
    pp "Белая папочка с пометкой <<#4>>. В ней кратко изложены истины инреальности."
    pp "А мне надо думать... Вас вернуть из кошмара?"
    show mi scared pioneer at right with byso
    ma "Как?"
    pp "Увидишь."
    "Пионер протянул руки в сторону Константина и Маши."
    pp "Удачи!"
    show blink
    "Глаза Константина сомкнулись."
    jump d4_withma