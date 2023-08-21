label d4_withspr:
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
        jump gmoivfdsmbvfdmbivjogsnfdmbigpfdnbigdpbngpdf
    else:
        scene bg bgcg8
        show load
        with byso
        pause 10
        $ bgcg -= 1
        scene bg black with dissolve
        stop music fadeout 2
        window show
        jump gmoivfdsmbvfdmbivjogsnfdmbigpfdnbigdpbngpdf
label gmoivfdsmbvfdmbivjogsnfdmbigpfdnbigdpbngpdf:
    $ save_name = ('Инреальность.\nДень четвёртый.')
    scene bg int_house_of_kt_day
    play music regret fadein 3
    play ambience ambience_int_cabin_day fadein 1
    show unblink
    play sound sfx_bed_squeak1
    "Константин открыл глаза и лениво потянулся."
    th "Вот оно...{w=1} Утро без головной боли."
    th "Несмотря на то что раньше я так просыпался только с похмелья, это хоть какая-то отдушина от кошмара."
if irrscore == 1:
    play sound sfx_bed_squeak2
    "Константин почувствовал, что на его кровать кто-то подсел."
    show image irr_normal with byso
    irr "Утречка!{w=1} Как спалось?"
    "Спросила у него Ира, завязывая волосы.{w} Константин облокотился на спинку кровати."
    kt "Да, я отлично, а ты как?"
    hide image irr_normal
    show image irr_grin
    with byso
    "В ответ она кивнула."
    irr "Весьма неплохо.{w} Тебе вроде как нужно сегодня к капитану зайти?"
    "Константин утвердительно кивнул."
    kt "А что?"
    hide image irr_grin
    show image irr_happy
    with byso
    "Ира улыбнулась и встала с кровати."
    irr "Буду рада если ты от бесполезного отряда перейдёшь ко мне.{w=1} Мне понадобится помощь."
    irr "Просто тех кто мне ранее помогал увезли с <<Прорывом>>."
    kt "Это перехват Батори?"
    hide image irr_happy
    show image irr_normal
    with byso
    irr "Угу. Ладненько, я побежала.{w} Сделай правильный выбор, пожалуйста."
    play sound sfx_close_door_1
    hide image irr_normal with byso
    "С усмешкой попросила Ира и вышла из домика."
    th "Хм-м. Может мне и стоит пойти в разведку...{w=1} По крайней мере там риска меньше."
    jump vifdnubhvfidsnuvfsdniuowiopdklsvpck
else:
    "Константин сел на кровать. Иры в домике не было."
    th "Вроде как мне стоит зайти к Андрею, он что-то вчера хотел сказать."
    th "Интересно ещё где тут позавтракать...{w=1} Да и вообще, откуда в симуляциях берётся еда."
    th "Ну, это я у Андрея и уточню."
    th "Мне же ещё надо выбрать между разведкой и спасательным отрядом.{w}.. Думаю что второе."
    th "По крайней мере мне не охота рыться в архивах, а так у меня есть возможность узнать что-то новое."
    jump vifdnubhvfidsnuvfsdniuowiopdklsvpck
label vifdnubhvfidsnuvfsdniuowiopdklsvpck:
    play sound sfx_bed_squeak2
    "Константин встал с кровати и начал одеваться."
    th "Ещё Олег говорил что мне могут выдать плазмоинтегратор."
    th "Было бы неплохо.{w=1} Заодно у местного техника спрошу как он работает."
    scene bg ext_house_of_un_day with byso
    play ambience ambience_ext_road_day fadein 1
    play sound door_cl
    stop music fadeout 3
    "Взяв ключи, Константин вышел из домика и закрыл дверь."
    th "Неужто симуляции настолько походят друг на друга?{w} Тот же лагерь, те же птички..."
    play sound light_inh
    "Достав сигареты, Константин закурил."
    th "По видимому да.{w=1} Ну, пойду в админку."
    "Константин направился в административный корпус, покуривая честерфилд."
    th "Что-то тут безлюдно.{w} Вроде как народу то в сопротивлении много...{w=1} Спят ещё все чтоль?"
    scene bg ext_square_day with byso
    "Выйдя на площадь, Константин заметил толпу людей возле медного Генды."
    play music cirk fadein 3
    show sl surprise pioneer at fright
    show dv guilty pioneer at left
    show image pas_normal
    with byso
    "Подойдя поближе, Константин встретил Славю, Алису и неизвестного ему парня."
    pasp "Ёбанный по голове, Наташа, ты прикалываешься чтоль надо мной?"
    show sl angry pioneer at right with byso
    sl "Откуда мне было знать, что тебе были нужны эти детали?{w=1} Они не были никак подмечены!"
    pasp "Ну ебанёшься! Молодая, ты издеваешься?!{w=1} Сколько раз я тебе говорил!"
    pasp "Не!"
    pasp "Трогать!"
    pasp "Мои!"
    pasp "Вещи!" with vpunch
    hide image pas_normal
    show image pas_normal2
    with byso
    play sound inh
    "Парень тяжело выдохнул и затянулся."
    pasp "Ну ладно она просто тупая, а ты куда смотрела, молодая?"
    "Константина, который наблюдал за этим сюрром, смутило то что парень был сам достаточно молод, чтоб называть так пионерок."
    natasha "Да не тупая я!"
    show dv angry pioneer at left with byso
    dv "А я ей что, нянька чтоль?!"
    "Парень выкинул сигарету и прикрыл лицо рукой."
    hide image pas_normal2
    show image pas_normal
    with byso
    pasp "Сучий потрох, вот пришло же в голову Андрею мне вас, двух куриц на попечение отдать!"
    pasp "Чтоб глаза мои вас до конца дня не видели!{w=1} И пока вы мне не отработаете стоимость тех деталей, вы от меня нихуя не получите!"
    show sl smile pioneer at right
    show dv grin pioneer at fleft
    with byso
    "Гаркнул парень и обратил внимание на Константина.{w=1} Девочки, заметив Константина улыбнулись."
    dv "О, салам-пополам, ты же новенький?"
    kt "Да, привет, Алиса..."
    show sl angry pioneer at right
    show dv angry pioneer at fleft
    show image pas_normal2
    hide image pas_normal
    with byso
    "По привычке вырвалось у Константина.{w=1} Девочке явно не понравилось такое именование."
    natasha "Ну грубиян!{w} Её Рита зовут!"
    hide sl
    hide dv
    with byso
    "Озвучила Наташа и взяв Риту за руку, ушла."
    stop music fadeout 2
    "Парень почесал затылок и подошёл к Константину."
    hide image pas_normal2
    show image pas_smile
    with byso
    pasp "Ну говорю же две курицы, блять...{w=1} Меня Гордон, это же тебя вчера Лиза привезла?"
    play music sanari volume 0.7 fadein 3
    "Константин протянул руку, а Гордон её пожал."
    kt "Меня Константин, рад знакомству. {w=1}Ты тут главный техник?"
    hide image pas_smile
    show image pas_normal
    with byso
    pas "Вроде того... {w}Правда наличие у меня двух этих куриц меня сильно раздражает."
    "Гордон поправил волосы и глянул на монумент."
    pas "Сколько Андрею не повторяй..."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Короче, если тебе нужно будет чего, заходи.{w=1} Если ты в отряд спасения наведаешься, то я выдам тебе свободный лучевой лазер."
    kt "Плазмоинтегратор?"
    hide image pas_smile
    show image pas_angry
    with byso
    "В ответ его перекорёжило."
    pas "Ну начинается, ёбанный по голове!{w=1} Сказал им что это плазматический лучевой лазер, а Олег такой:<<хуле бы мне дегенерату не назвать это плазмоинтегратор>>!"
    "Нелестно процитировал Гордон Олега."
    pas "Хоть ты называй его нормально, а?"
    kt "Окей-окей.{w=1} Прости, не знал."
    hide image pas_angry
    show image pas_smile
    with byso
    pas "Да ладно, ничего, иди."
    hide image pas_smile with byso
    "Выдохнул Гордон, махнув рукой.{w=1} Константин продолжил путь до административного корпуса."
    th "Своеобразный чувак, ничего не сказать.{w=1} Молодая, мат через слово...{w=1} Пообщаюсь ещё с ним."
    scene bg ext_admins_day
    show image rkis_normal
    with byso
    stop music fadeout 3
    "Дойдя до дверей административного корпуса, Константин встретил робокошку."
    rkis "Приветствую, <<Корсар>>, проходите, капитан вас ждёт."
    kt "Угу, спасибо."
    scene bg int_admins with byso
    play ambience ambience_int_cabin_day volume 0.7 fadein 1
    play sound sfx_close_door_1
    "Проговорил Константин и вошёл в корпус."
    th "Я же не спросил какая каба...{w=1} Ну, думаю та что и вчера."
    play sound sfx_knock_door7_polite
    "Константин поднялся на второй этаж и постучал в дверь 203го кабинета."
    play music Waijdan fadein 3
    andr "Подождите, не сейчас!"
    "Прокричал в ответ Андрей."
    "Константин сел на пол и прислушался."
    liz "В каком смысле вы хотите переквалифицировать нас?!"
    oleg "Да, убивать людей - плохо!"
    andr "А людей вас убивать никто и не просит!{w} По данным <<Эриды>> сейчас идеальное время для нападения на корневые системы инреальности."
    andr "Ваша задача лишь убрать пустышек и нарушить стабильность наибольшего количества систем инреальности."
    liz "То есть вас не смущает то что <<Эрида>> - ебанутая сука, как и Валери?!{w=1} Им бы лишь кого-то убить!"
    th "<<Эрида>>?{w=1} Валери?{w} Кто это?"
    oleg "Вот именно!{w} Мы вчера читали с ней <<Цену грехов>> и вы бы слышали, как она отзывалась о Диме!"
    th "Ира?"
    andr "Отставить беспочвенные оскорбления!!!{w} Этот Дима - дезертир!{w=1} Нет ничего плохого в том, чтобы презирать подобное поведение!"
    liz "Да?!{w=1} А вас не смущает что она относится так ко всем, кто похож на пустышку?!"
    andr "Хватит отлынивать!{w=1} Собирайте экипировку и после обеда вы едете в 22-25a!{w} Разговор окончен!"
    th "Что такое 22-25a?"
    liz "Я поняла, вы уже заняли сторону..."
    andr "Что ты сказала?!"
    play sound sfx_table_hit volume 0.8
    "Выкрикнул Андрей и стукнул по столу."
    andr "Если ты не будешь выполнять приказ, то я вас обоих под трибунал отправлю!{w} Собираться, живо!"
    play sound sfx_open_door_2
    stop music fadeout 3
    show image liz_angry at right
    show image oleg_think at left
    with byso
    "Дверь кабинета открылась и оттуда вышли Олег и Лиза."
    liz "Доброе утро.{w=1} Иди, потом поговорим."
    hide image oleg_think
    show image oleg_happy
    with byso
    oleg "Утра, друже!"
    hide image oleg_happy
    hide image liz_angry
    with byso
    "Выкрикнул Олег и с Лизой направился на выход."
    scene bg int_admins_room2
    show image andr_rage
    with byso
    play sound door_cl
    play music god fadein 3
    "Константин вошёл в кабинет.{w=1} Внутри его ожидал обозлённый Андрей."
    hide image andr_rage
    show image andr_normal
    with byso
    "Буквально в момент он успокоился и опустился на стул."
    andr "Доброе утро, сержант.{w=1} Садитесь."
    "Отчеканил Андрей, указав на диван."
    "Константин сел и облокотившись, закинул ногу на ногу."
    kt "Доброе-доброе.{w} О чём вы так агрессивно спорили с Лизой?"
    hide image andr_normal
    show image andr_angry2
    with byso
    "Андрей немного поморщился."
    andr "Оспаривание приказов..."
    kt "О чём именно?"
    andr "Требуется перевести сопротивление в боевой режим. {w}Настало время действовать."
    "Константин сильно удивился словам капитана."
    kt "Чего это вы так решили?"
    hide image andr_angry2
    show image andr_normal2
    with byso
    andr "<<Эрида>> сообщила что при слепой поддержке Батори мы можем проникнуть в корневые симуляции и устроить переворот."
    andr "В таком случае мы сможем захватить контроль над инреальностью."
    kt "Чего это вдруг так быстро?"
    hide image andr_normal2
    show image andr_smile
    with byso
    "Андрей в ответ улыбнулся."
    andr "По твоему, как ты говорил, 9 лет это мало?"
    kt "Да нет, просто интересуюсь.{w} А как вы хотите перехватить контроль?"
    "Ответа не последовало."
    hide image andr_smile
    show image andr_normal3
    with byso
    andr "Уж прости, но тебе знать не положено.{w} Это могут узнать только лейтенанты и старше."
    kt "Хорошо, я понял. Для чего я пришёл?"
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "У тебя было время подумать.{w} Ты решил с кем будешь работать?"
    andr "В разведке или в карательный отряд?"
if irrscore == 1:
    window hide
    menu:
        "Разведка.":
            $ renpy.block_rollback()
            jump razvedfjdsvnifosdvhnisfnvisfdnvinifdn
        "Карательный отряд.":
            $ renpy.block_rollback()
            jump otryadifsdvbhnvfisbvbhsfsfvbhidsdfvbf
        "Что такое карательный отряд?":
            andr "Отряд <<Дзетты>>."
            window hide
            menu:
                "Разведка.":
                    $ renpy.block_rollback()
                    jump razvedfjdsvnifosdvhnisfnvisfdnvinifdn
                "Карательный отряд.":
                    $ renpy.block_rollback()
                    jump otryadifsdvbhnvfisbvbhsfsfvbhidsdfvbf
else:
    kt "Что такое карательный отряд?"
    andr "Отряд <<Дзетты>>."
    th "Думаю, лучше мне пойти к Лизе.{w=1} Её я хотя бы знаю."
    kt "Карательный отряд."
    jump otryadifsdvbhnvfisbvbhsfsfvbhidsdfvbf
label otryadifsdvbhnvfisbvbhsfsfvbhidsdfvbf:
    hide image andr_normal2
    show image andr_smile
    with byso
    andr "Отлично, хвалю за героизм."
    th "Героизм?"
    play sound sfx_open_table
    hide image andr_smile
    show image andr_normal
    with byso
    "Андрей что-то записал и убрал листик в ящик тумбочки."
    andr "Ваша задача будет вывезти пару путников из 22-25a, после чего ехать и чистить симуляции.{w=1} Гордон выдаст снаряжение."
    kt "Что значит 22-25а?"
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "Номер симуляции в системе инреальности.{w} Первые два числа - год попадания, вторые два - возраст главного путника, буква в конце - серия."
    play sound sfx_paper_bag
    hide image andr_normal3
    show image andr_normal
    with byso
    "Андрей достал из кармана листок."
    andr "Отдашь это технику.{w=1} Так-же можешь на свои средства докупить у него дополнительные элементы снаряжения."
    kt "А зачем нам двое путников?"
    hide image andr_normal
    show image andr_normal2
    with byso
    "Андрей поправил очки и глянул в окно."
    andr "Одного в разведку, другого для нашей медсестры - Валентайн."
    kt "А зачем ей путник?"
    andr "Не могу сказать, тайна."
    th "Любопытно..."
    kt "Ладно."
    stop music fadeout 7
    play sound sfx_dinner_horn_processed volume 0.4
    "На улице зазвучал горн."
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Кстати да, у нас тут тоже трёхразовое питание.{w} За сигареты можно запросить абонемент на улучшенное питание."
    kt "Понял. На этом всё?"
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "Да, можешь идти.{w=1} Вы отбываете после обеда."
    kt "Понял, до встречи."
    scene bg int_admins with byso
    play sound sfx_close_door_1
    play music music_list["two_glasses_of_melancholy"] fadein 3
    "Проговорил Константин и покинул кабинет капитана."
    th "Да уж...{w=1} Фантастика...{w} К сожалению, не в хорошем смысле слова."
    th "Может всё-таки стоило пойти в разведку?"
    scene bg ext_admins_day with byso
    play sound door_cl
    play ambience ambience_ext_road_day fadein 1
    "Константин вышел из административного корпуса."
    th "Да нет, переживу."
    th "К тому же у меня будет нужное снаряжение, да и со своим запасом я могу купить что-то интересное."
    th "Ну, приключение начинается."
    scene bg ext_dining_hall_away_day with fade
    "Со стороны столовая ничем не отличалась от лагерной.{w} Всё те же <<пионеры>> шли поесть, но только в меньшем количестве."
    th "Интересно, неужели у них такие проблемы с одеждой?{w} Все так и ходят в пионерских нарядах."
    th "Хотя чем я лучше...{w=1} Та же форма, только вместо шорт джинсы."
    th "Не, ну если подумать то реально, где тут найти другую одежду?"
    th "Кто с чем попал сюда, тот в том и ходит."
    th "Олег в тельняшке и джинсах, Лиза в бежевом свитере, Андрей в зелёной тройке."
    scene bg ext_dining_hall_near_day
    show image oleg_think at left
    show image liz_bukal at right
    with byso
    "У входа Константина встретила Женя и Олег."
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "О, ты вовремя.{w=1} Пошли с нами есть."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Ну чего, ты с нами остался?"
    kt "Да-да. {w=1}Я с вами.{w=1} Андрей передал."
    play sound sfx_paper_bag
    "Константин достал бумажку, которую ему вручил Андрей и передал её Лизе."
    hide image liz_normal
    show image liz_smile at right
    with byso
    liz "Вот это уже хорошо!"
    "Олег из любопытства заглянул в бумажку."
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Ого!{w} Новые интеграторы, починка табельного оружия и три перехватчика кода?!"
    liz "Да уж, Андрей на нас не поскупился.{w=1} Ладно, идём есть."
    scene bg int_dining_hall_day
    show mi normal pioneer
    show image oleg_smile at left
    show image liz_smile at right
    with byso
    play ambience ambience_dining_hall_empty fadein 1
    "Столовая была практически безлюдной.{w=1} На раздаче их встретила Мику."
    oleg "О, здорова, Мику, чего сегодня?"
    play sound sfx_tennis_serve_1
    show mi rage pioneer
    hide image oleg_smile
    show image oleg_shy at left
    with byso
    "В ответ девочка дала поварёшкой по голове Олега."
    show mi angry pioneer with byso
    mip "Я те дам, Мику!{w} Куролесить дохрена будешь - голодный останешься!{w} Базовая - кабачковая каша, продвинутая - яичница.{w=1} Напиток - лимонный."
    hide image liz_smile
    show image liz_grin at right
    with byso
    liz "Ладно-ладно, прости дурака.{w=1} Мне продвинутую порцию."
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Мне стандартную."
    show mi normal pioneer with byso
    mip "А ты чего изволишь?"
    "Константин достал сигарету и положил на раздачу."
    kt "Тоже продвинутую."
    "Девочка взяла сигарету и осмотрела."
    show mi grin pioneer with byso
    mip "О-о, с кнопкой!{w=1} Отлично, уговор."
    "Она разложила по тарелкам порцию коричневой каши и две яичницы."
    mip "Садитесь жрать, пожалуйста."
    "Иронично проговорила девочка и указала на свободные столики."
    hide mi with byso
    "Все трое кивнули и направились к столику."
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "Всем приятного."
    kt "Приятного."
    hide image liz_grin
    show image liz_smile at right
    with byso
    "Лиза в ответ кивнула и приступила к еде."
    hide image liz_smile
    show image liz_grin at right
    with byso
    liz "Кстати, Кость, тебе надо бы зайти к Валери и сдать кровь."
    kt "А, точно.{w=1} Сейчас?"
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Ага, иди как поешь.{w=1} Мы пока с Лизой разгрузим автобус."
    kt "А чего у вас там?"
    hide image liz_grin
    show image liz_bukal at right
    with byso
    liz "Да так, по мелочи.{w=1} Мы были всё-таки не поставщиками, а спасателями, потому иногда по просьбам Гордона и Андрея таскали всякие вещи из других симуляций."
    kt "Например?"
    "Лиза достала из кармана очки."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Такого плана оптика например.{w=1} У пустышки-Жени зрение +5, потому даже пара рассеивающих линз могут стать хорошим дополнением для плазмоинтеграторов."
    kt "И что, вы тоннами возите линзы?"
    "С усмешкой уточнил Константин, попивая лимонный напиток."
    hide image liz_normal
    show image liz_smile at right
    with byso
    liz "Запчасти для робокошки, расходники для пайки, семена для агроцеха, короче всё то, чем реже озадачены поставщики."
    kt "А что за агроцех?"
    hide image oleg_happy
    show image oleg_shy at left
    with byso
    oleg "Это ребята, которые выращивают еду. {w=1}Вот сижу тут и ем кабачковую кашу..."
    "Уныло перемешивая содержимое своей тарелки пробурчал Олег."
    hide image liz_smile
    show image liz_normal at right
    with byso
    liz "В условиях инреальности вся растительность растёт многократно быстрее."
    hide image oleg_shy
    show image oleg_smile at left
    with byso
    oleg "Ага, иногда даже если понаблюдать час, то заметишь как одно семечко вырастет в малюсенький кустик."
    hide image liz_normal
    show image liz_angry at right
    with byso
    liz "Ну-ну, у кого-то видимо времени много свободного..."
    "Укоризненно произнесла Женя, поглядывая на Олега."
    hide image oleg_smile
    show image oleg_shy at left
    with byso
    oleg "Исключительно в свободное время."
    liz "Да-да..."
    "Константин доел свою порцию и стал допивать лимонный напиток."
    hide image liz_angry
    show image liz_normal at right
    with byso
    liz "Ладно, иди к Валери, встретимся у входа в лагерь.{w} Главное ни на какие тесты у неё не соглашайся!"
    kt "Хорошо.{w=1} А что с тестами то?"
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Да она хоть и умная, но отбитая на всю голову!"
    liz "Точно. Скажу тебе по секрету."
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Она проводит эксперименты с генмодом."
    kt "И чего с ним?"
    oleg "Я возьму нам с собой писание почитать."
    kt "Ладно, не откажусь.{w=1} Встретимся у ворот лагеря."
    hide image liz_bukal
    show image liz_smile at right
    with byso
    liz "Отлично, удачи."
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "Бывай."
    "Константин сдал тарелки и пошёл на выход."
    scene bg ext_dining_hall_near_day with byso
    play ambience ambience_ext_road_day fadein 1
    play sound light_inh
    stop music fadeout 3
    "Выйдя из столовой, он закурил."
    th "Что-то по рассказам окружающих эта Валери странная дама."
    th "Ну, увидим собственно."
    th "Олег метко подметил про писание. Я не против ознакомиться..."
    scene bg ext_square_day
    show image pas_normal2
    with byso
    play music everyday fadein 3
    "На площади он встретился с Гордоном."
    hide image pas_normal2
    show image pas_normal
    with byso
    pas "Снова здорова, молодой.{w=1} Когда твои дойдут до меня?"
    kt "Понятия не имею."
    pas "Ну лады, я сказал Наташе, чтоб вас встретила.{w=1} Сам то куда путь держишь?"
    kt "Я сейчас к Валери."
    hide image pas_normal
    show image pas_smile
    with byso
    "Гордон усмехнулся и махнув рукой пошёл дальше."
    pas "Хах, в добрый путь."
    hide image pas_smile with byso
    th "Н-да...{w=1} Уже навевает некоторую неприязнь..."
    scene bg ext_aidpost_day with byso
    "Дойдя до медпункта, он собрался с силами."
    th "Ну, посмотрим..."
    stop music fadeout 3
    play sound sfx_knock_door7_polite
    "Константин вежливо постучал."
    csp "О, гости...{w} Заходите!"
    scene bg int_aidpost_day_apple
    show image val_calm
    with byso
    play sound door_cl
    play ambience ambience_medstation_inside_day fadein 1
    play music lim fadein 3
    "Войдя, он встретил девушку лет 30ти с синими волосами, повязкой на глазе и оружием на спине."
    th "Йо-хо-хо и бутылка формалина."
    play sound sfx_bus_window_hit
    hide image val_calm
    show image val_smile2
    with byso
    "Откинув на кушетку книжку <<Половая психопатия>>, она глянула на Константина."
    csp "Новенький...{w=1} Привет...{w=1} Я Валери.{w} Чего же тебя ко мне занесло?"
    "Константин засмотрелся на повязку, которая была на глазу у Валери."
    kt "Здравствуй.{w=1}Кровь сдать хотел.{w} Точнее надо."
    hide image val_smile2
    show image val_smile
    with byso
    val "Надо-надо...{w=1} Нам не нужно вспышек генмода в симуляции."
    val "А тут подумаешь, уколоть пальчик..."
    hide image val_smile
    show image val_smile2
    with byso
    val "Кстати, у меня тут есть экспериментик, не хочешь поучаствовать?"
    "С едкой ухмылкой спросила Валери, в кой-то мере похотливо глядя на Константина."
    kt "Нет, откажусь, крови достаточно."
    hide image val_smile2
    show image val_sad
    with byso
    val "М-м-м..."
    play sound sfx_open_table
    "Недовольно промычала Валери и начала что-то искать в ящиках."
    val "Все оставляют даму одну в столь тяжёлый период...{w=1} А ведь мне просто хочется чу-уточку мужского внимания."
    "Протянула Валери, достав небольшое лезвие. В целом её речь была весьма неторопливой и со множеством пауз."
    hide image val_sad
    show image val_calm
    with byso
    val "Ну подумаешь человечка под катализаторами патогеном заразить...{w} Я ведь за всем прослежу...{w=1} Зато весело будет!"
    val "Давай лапку."
    "Константин сел на кушетку и протянул руку Валери."
    "Она сделала небольшой надрез и начала собирать кровь в пробирку."
    hide image val_calm
    show image val_normal
    with byso
    val "Чего это тебя к нам в сопротивление занесло?"
    kt "Познакомился с первым лейтенантом под прикрытием и теперь в их отряде."
    hide image val_normal
    show image val_smile2
    with byso
    val "А, Лиза то...{w=1} Скучная девочка.{w} Может ты останешься со мной?{w=1} Поможешь мне чуток..."
    "Предложила Валери, глядя Константину прямо в душу."
    kt "Нет, я уже в карательном отряде, меня всё устраивает."
    hide image val_smile2
    show image val_smile
    with byso
    val "А-а, так вас же просили привести мне человечка для экспериментов..."
    val "Буду ждать красивого и выносливого мальчика, шатена по мере возможности..."
    th "Насчёт красивого не уверен, но Рома подходит по описанию..."
    val "Ты бы неплохо подошёл...{w=1} Но нельзя..."
    hide image val_smile
    show image val_sad
    with byso
    val "Запретный плод сладок..."
    "Усмехнулась Валери, закрыв подписанную пробирку с кровью и отставив на штатив."
    hide image val_sad
    show image val_smile2
    with byso
    play sound sfx_pat_shoulder_hard
    "Константин было хотел встать, но Валери схватила его за руку."
    val "Но ты мне привезёшь же достойную замену?..."
    hide image val_smile2
    show image val_madsmile
    with byso
    "Проговорила она, слизнув кровь с пальца Константина."
    play sound sfx_punch_medium
    "Константин выдернул руку и потёр о рубашку."
    kt "Хорошо-хорошо, жди."
    hide image val_madsmile
    show image val_smile
    with byso
    val "Хороший мальчик, жду."
    scene bg ext_aidpost_day with byso
    play ambience ambience_ext_road_day fadein 1
    play sound sfx_close_door_1
    stop music fadeout 3
    "Константин вышел из медпункта."
    th "Ну видимо бытующее мнение в кой-то мере оправдано..."
    th "Либидо поверх чего угодно...{w=1} Жуть..."
    scene bg ext_square_day with byso
    play sound light_inh
    "Достав сигарету, он закурил и направился к воротам лагеря."
    th "Чем-то напоминает мне торчалую, с которой я по объёбу лишился девственности."
    stop ambience
    play sound in_vosp
    play music sab
    scene bg semen_room
    show shum_white
    with flash
    "Вещества в теле Константина превышали практически любой допустимый ПДК.{w=1} Он молча сидел и залипал в стену."
    chel "Ух, блять, хорошо пошла..."
    nap "Мне хоть оставь, нарколыга ебучий!"
    "Константин лёг на спину и засмотрелся на люстру."
    th "Красиво...{w=1} Новый год..."
    th "Новый год - новые места..."
    th "Что я тут делаю...{w=1} Зачем я тут делаю..."
    th "Сраная моя жизнь...{w=1} Хотя сейчас мне хорошо..."
    th "Хорошо... {w=1}Ведь в экзистенциальном смысле я победил?"
    th "Я же родился - значит победа."
    th "А может и поражение...{w=1} Сильно ли вообще победа отличается от поражения?"
    th "Поражение - плохо или поражение - хорошо...{w=1} Сложно сказать вне контекста..."
    th "Да и победа не так чиста...{w=1} Чиста как стекло на новеньком Nikon-е..."
    th "Я же занимался фотографией...{w=1} Куда это пропало..."
    th "Пропало вдохновение...{w=1} Вдохновение?{w=1} Кто же мне его давал?..."
    th "Настя...{w=1} Настя мертва..."
    th "Была ли это победа или поражение?..."
    chel "Всё, не наю как вы, н-н я прилягу..."
    "Парень распластался на полу и захрапел."
    nap "А ты чё такой грустный?"
    kt "Скучаю..."
    nap "По кому это?"
    kt "По Насте."
    "Девочка села на Константина и начала расстёгивать его ремень."
    nap "Так и быть, избавлю тебя от печали."
    stop music
    play sound out_vosp
    play ambience ambience_ext_road_day fadein 1
    hide shum_white
    scene bg ext_square_day
    with flash
    "Константин передёрнуло от неприятности этого воспоминания."
    th "Нет, не она, но похожа...{w=1} Ту точно не Валери звали..."
    th "Мне кажется, лучше бы у меня никогда не было секса, чем так..."
    th "Может тогда бы я думал что это нечто чудесное... {w=1}То, ради чего Адам и Ева покинули чертоги райского острова."
    th "А на деле это просто первобытная мясная возня..."
    th "Говорили... {w=1}Пестики и тычинки нам даны не для того, чтобы утопать в своей похоти..."
    th "Дегенерация, да и только..."
    scene bg ext_clubs_day
    show image oleg_happy
    with byso
    play music everyday fadein 3
    "Дойдя до клубов, он встретил Олега, который тащил деревянную коробку."
    oleg "Дор-рогу педагогу..."
    play sound sfx_slam_door_campus
    hide image oleg_happy with byso
    "Насмешливо прокричал Олег и по инерции влетел в клуб."
    liz "О, ты уже тут?"
    show image liz_normal with byso
    "Константин обернулся и встретил Лизу."
    kt "Да, уже закончил с кровью. Где Гордон?"
    hide image liz_normal
    show image liz_smile
    with byso
    liz "А, ты с ним уже пересекался...{w} Не знаю, Рита сказала что свалил в агроцех на время."
    kt "Понял. А вы чего?"
    hide image liz_smile
    show image liz_bukal
    with byso
    liz "Разгружаем.{w=1} Там не много осталось, потому помоги Олегу."
    kt "Без проблем."
    scene bg ext_camp_entrance_day with byso
    "Константин направился к автобусу."
    pi "Да нормально. {w}Перехватчик кода работает штатно."
    chel "Ну ты смотри.{w=1} Чаще используй позывной, мало ли с тобой что случится."
    pi "Ну...{w=1} Не нравится мне мой позывной... {w=1}<<Лазурь>>... {w=1}Жуть какая!"
    chel "Ничего переживешь, зато если тебя Батори схватит, то мы первые об этом узнаем."
    pi "Спасибо, успокоил. {w}Почему мне просто не называть себя Олегом?"
    chel "Так в книге твоего имени в третьем лице не будет!"
    pi "Обидно..."
    scene bg ext_bus with byso
    "Константин перестал слушать диалог стоящих у ворот людей и открыл багажник автобуса."
    play sound2 sfx_metal_door_handle_rattle
    play sound sfx_click_1
    "Дверка со скрипом поднялась вверх и защёлкнулась.{w} В багажнике лежало ещё 2 коробки и пара сумок."
    play sound sfx_put_sugar_cart
    "Достав самую дальнюю коробку, Константин взял её на руки и понёс в клубы."
    th "Тяжёленькая...{w=1} Они там кирпичи возят?..."
    scene bg ext_camp_entrance_day with byso
    play sound portal
    "Раздался странный звук и парень с позывным <<Лазурь>> растворился в воздухе."
    th "Вот это технологии...{w=1} Куда он только отправился?..."
    th "Ещё из старых футуристических игр недолюбливал телепортацию."
    th "Тебя же по сути расщепляет на молекулы и собирает снова, только уже в другом месте."
    th "Это по сути своей означает неминуемую смерть, так ещё и просто ради поржать."
    th "Хотя может это и не телепортация вовсе, а просто перемещение в другую симуляцию..."
    th "Не могу понять как это работает...{w=1} Может Гордон сможет объяснить, он же создатель?"
    scene bg int_clubs_male_day with byso
    play ambience ambience_clubs_inside_day fadein 1
    play sound sfx_open_door_clubs
    "Константин вошёл в клубы и поставил коробку на пол."
    show dv normal pioneer with byso
    kt "Куда?"
    "Спросил он у рядом стоящей Риты."
    show dv smile pioneer with byso
    rita "Тащи в кладовку, Семён разберётся."
    kt "Понял."
    hide dv with byso
    play sound sfx_put_sugar_cart
    show image oleg_smile with byso
    "Оставив коробку, он пересёкся в пути с Олегом."
    oleg "Там осталось две коробки, отнесём?"
    kt "Ну а что делать то, пошли."
    scene bg ext_clubs_day
    show image oleg_smile
    with byso
    play ambience ambience_camp_center_day fadein 1
    "Константин с Олегом вышли из клубов."
    scene bg ext_bus
    show image oleg_smile
    with byso
    "Дойдя с Олегом до автобуса, Константин начал доставать коробки."
    hide image oleg_smile
    show image oleg_happy
    with byso
    oleg "Хочешь анекдот?"
    "Константин в ответ тяжело выдохнул."
    kt "Ну давай, жги."
    oleg "Как называют тюрьму, в которой очень дружный коллектив?"
    kt "М-м?"
    oleg "Френдзона."
    hide image oleg_happy
    show image oleg_smile
    with byso
    "Олег заржал как конь, а Константин улыбнулся."
    kt "Неплохо.{w=1} Вот ящик."
    hide image oleg_smile
    show image oleg_happy
    with byso
    oleg "Ага!{w=1} Знаешь какой-нибудь анекдот?"
    window hide
    menu:
        "Рассказать анекдот про серную кислоту.":
            $ renpy.block_rollback()
            kt "Что ты почувствуешь, если сунешь руку в банку с серной кислотой?"
            oleg "Ну?"
            "Ожидая развязки шутки спросил Олег."
            kt "Что у банки нет дна."
        "Рассказать анекдот про инвалида.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            kt "Как называют глухонемого с тремором рук?"
            oleg "Ну?"
            "Ожидая развязки шутки спросил Олег."
            kt "Заика."
        "Рассказать анекдот про многодетных.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            kt "Тоня всегда путала противозачаточные таблетки с успокоительными."
            kt "Теперь у неё 15 детей, но ей похуй."
        "Рассказать анекдот про слона.":
            $ renpy.block_rollback()
            kt "Чем слон отличается от рояля?"
            oleg "Ну?"
            "Ожидая развязки шутки спросил Олег."
            kt "К роялю можно прислониться, а к слону прироялиться нельзя."
        "Рассказать анекдот про Льва Толстого.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            kt "Ебёт Лев Толстой Горького:"
            kt "Кто ж тебя Горьким-то назвал, сладенький ты мой?"
            kt "А-а-а, блять! Говорящий лев!"
        "Рассказать анекдот про мотоциклиста.":
            $ renpy.block_rollback()
            kt "Что написали на могиле мотоциклиста?"
            oleg "Ну?"
            "Ожидая развязки шутки спросил Олег."
            kt "<<Родился и умер от дырки в резине>>."
        "Рассказать анекдот про карлика.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            kt "Как называют карлика, которого ударило током?"
            oleg "Ну?"
            "Ожидая развязки шутки спросил Олег."
            kt "Полупроводник."
    hide image oleg_happy
    show image oleg_smile
    with byso
    "Несмотря на то что шутка была достаточно заезженной, она понравилась Олегу и тот, встав на месте, расхохотался."
    hide image oleg_smile
    show image oleg_happy
    with byso
    oleg "А хорошая шутка, мне нравится.{w=1} Лизе расскажу как-нибудь."
    scene bg int_clubs_male_day
    show image oleg_smile
    with byso
    play ambience ambience_clubs_inside_day fadein 1
    play sound sfx_open_door_clubs_2
    "Войдя в клубы, они поставили последние коробки."
    kt "Вот и всё."
    hide image oleg_smile
    show image oleg_think at right
    show image liz_normal
    show image pas_smile at left
    with byso
    "Сказал Константин, прогнув спину.{w=1} В помещение вошёл Гордон и Лиза."
    pas "О, молодые, спасибо, выручили.{w} Так, теперь талон..."
    hide image pas_smile
    show image pas_normal at left
    with byso
    "Проговорил Гордон, достав из кармана бумажку, которую Константину выдал Андрей."
    kt "Слушай, нескромный вопрос, а почему ты всех зовёшь молодыми?"
    "Гордон отвлёкся от бумажки и глянул на Константина."
    pas "Мне до попадания в сюда было 42, да и работал я инженером, так, профессиАнальная привычка."
    "Расчленив слово на два рассказал он и продолжил вчитываться в бумажку."
    hide image pas_normal
    show image pas_angry at left
    with byso
    pas "Ну ёбаный по голове, сколько Андрею не повторяй чтоб он писал нормально, ему похуй...{w=1} Врач в пятом колене..."
    "В ответ на слова Гордона, Олег рассмеялся, а Лиза немного улыбнулась."
    hide image liz_normal
    show image liz_grin
    with byso
    liz "Да словно у тебя почерк идеальный."
    pas "Не выделывайся, а то без экипировки останешься."
    "Лиза лишь усмехнулась в ответ."
    hide image pas_angry
    show image pas_normal at left
    with byso
    pas "Так, ну что там...{w=1} Лучевые лазеры новой модели... {w}Верните старые потом, я их переберу."
    kt "А чем новые от старых отличаются?"
    hide image liz_grin
    show image liz_smile
    with byso
    liz "Ёмкость накопителя, выходная мощность и дальность действия."
    hide image pas_normal
    show image pas_angry at left
    with byso
    "Встряла Лиза, Гордону это не понравилось."
    pas "Самая умная чтоль? Профессор по электродинамике небось?"
    "Лиза показательно вздохнула и размахнула руками.{w=1} Гордон достал из под стола три плазмоинтегратора."
    play sound sfx_punch_medium
    hide image pas_angry
    show image pas_normal at left
    with byso
    pas "Вот...{w=1} Чё там ещё...{w=1} Перехватчики?"
    "Гордон достал из под стола ещё три странных пульта."
    pas "И починка табельного. С собой?"
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "У меня его вообще нет."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "А я тебя и не спрашиваю."
    "Едко подметил Гордон и глянул на Лизу."
    hide image liz_grin
    show image liz_smile
    with byso
    liz "У меня порядок, так и не пользовалась."
    pas "А ты?{w=1} Завести не хочешь?"
    kt "Цена вопроса?"
    hide image pas_smile
    show image pas_normal at left
    with byso
    pas "Тебе в рублях или сигаретах?"
    kt "В сигаретах."
    pas "Пачка. Тебе как новоприбывшему сделаю скидку - пятнадцать."
    hide image oleg_shy
    show image oleg_angry at right
    with byso
    oleg "Эй!{w=1} А мне ты скидку никогда не делал!"
    hide image pas_normal
    show image pas_smile at left
    with byso
    "Вспылил Олег, Гордон улыбнулся."
    pas "А из-за кого всё сопротивление называет плазматический лучевой лазер плазмоинтегратором? Вот и сиди!"
    hide image oleg_angry
    show image oleg_shy at right
    with byso
    "Олег недовольно фыркнул."
    pas "Так что?"
    kt "А что за оружие?"
    pas "Маузер С96 с модификацией.{w=1} По факту, это скорее похоже на люгер. {w=1}От оригинала отличается съёмностью магазина и улучшенным спуском."
    kt "И откуда вы таковой раздобыли?"
    play sound light_inh
    hide image pas_smile
    show image pas_normal2 at left
    with byso
    "Гордон сел на стол и закурил."
    pas "Запчасти валяются по старому корпусу, а магазин пришиваю от люгера."
    pas "К делу. Да или нет?"
    kt "Возьму. Сейчас правда нет столько сигарет с собой."
    play sound sfx_paper_bag 
    hide image pas_normal2
    show image pas_smile at left
    with byso
    "Константин достал пачку в которой оставалось 12 сигарет.{w=1} Гордон махнул рукой."
    pas "С кнопкой?{w} Пойдёт.{w=1} Давай сюда."
    play sound sfx_pat_shoulder_hard
    hide image oleg_shy
    show image oleg_angry at right
    with byso
    "Олег ещё больше разозлился, а Гордон убрал пачку в карман и достал отполированный пистолет."
    pas "Вот ещё кобура."
    play sound sfx_punch_medium
    "Достав кожаный ремень с двумя магазинами, он протянул его Константину.{w=1} Константин убрал пистолет в кобуру и надел её на пояс."
    pas "Отлично.{w=1} Приятно иметь дело."
    hide image liz_smile
    show image liz_bukal
    with byso
    liz "Слушай, а перевязка у тебя продаётся?"
    hide image pas_smile
    show image pas_normal2 at left
    with byso
    "Гордон отрицательно помотал головой."
    hide image oleg_angry
    show image oleg_shy at right
    with byso
    pas "Не-е.{w=1} Я всё барахло на продажу сбагрил Валери.{w} Пусть она этим занимается."
    hide image pas_normal2
    show image pas_smile at left
    with byso
    "Проговорил он и немного улыбнулся."
    pas "По крайней мере не каждый захочет к ней идти.{w} Меньше расход."
    hide image liz_bukal
    show image liz_smile
    hide image oleg_shy
    show image oleg_smile at right
    with byso
    "Лиза и Олег тяжело вздохнули и посмотрели на Константина.{w=1} Гордон рассмеялся."
    kt "А я то чё?"
    pas "Это они тебе так недвусмысленно намекают на то, что к сестричке пойдёшь ты."
    hide image liz_smile
    show image liz_grin
    with byso
    liz "Угу."
    hide image oleg_smile
    show image oleg_happy at right
    with byso
    oleg "Да-да."
    "Константин отвёл взгляд в сторону и усмехнулся."
    kt "Ладно, схожу."
    hide image oleg_smile
    show image oleg_happy at right
    with byso
    oleg "Окей, потом топай в разведку, нам там надо с логистами поболтать."
    hide image liz_grin
    show image liz_smile
    with byso
    liz "Нам нужны три бинта, один обезбол и перекись. {w}Ну если не будет, то зелёнки бутыль."
    "Лиза дала Константину 10 советских рублей, а Олег достал из кармана целлофановый пакет."
    hide image pas_smile
    show image pas_normal2 at left
    with byso
    pas "Ебаный по голове, сто лет таких не видел, ты где его взял?"
    hide image oleg_happy
    show image oleg_shy at right
    with byso
    oleg "А вот нет скидки - нет ответа."
    hide image pas_normal2
    show image pas_smile at left
    hide image liz_smile
    show image liz_laugh
    with byso
    "Обиженно проговорил Олег.{w} Остальные трое рассмеялись и Константин взял пакет."
    kt "Ладно, иду.{w=1} До встречи."
    pas "Чао-бамбино."
    hide image liz_laugh
    show image liz_smile
    with byso
    liz "Увидимся."
    scene bg ext_clubs_day with byso
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 1
    play sound sfx_close_door_1
    "Константин вышел из клубов и пошёл в домик за новой пачкой сигарет."
    th "И снова к Валери...{w=1} Не нравятся мне такие, но я знаю кому нравятся..."
    scene bg ext_aidpost_day with byso
    play sound sfx_knock_door3_dull
    play music Gallow fadein 3
    "Взяв сигареты из домика, Константин дошёл до медункта и постучал."
    val "Проходи..."
    play sound sfx_open_door_2
    scene bg int_aidpost_day_apple
    show image val_calm
    with byso
    play ambience ambience_medstation_inside_day fadein 1
    "Он вошёл и заметил лежащую на кушетке Валери.{w} В воздухе царил запах жжёных тряпок, который неоднозначно напоминал что-то из прошлой жизни."
    kt "Чего лежим?"
    hide image val_calm
    show image val_normal
    with byso
    "В ответ она лениво подняла голову и, спустя секунду, опустила."
    val "А чего бы и не полежать.{w=1} Если хочешь - ложись рядом, не кусаюсь."
    hide image val_normal
    show image val_calm
    with byso
    val "Почти..."
    kt "Нет, спасибо.{w=1} Мне бы медикаменты купить."
    play sound monety
    "Проговорил Константин и достал деньги, которые ему дала Лиза."
    hide image val_calm
    show image val_sad
    with byso
    val "Хорошо-хорошо.{w=1} Только давай поговорим, а?"
    play sound sfx_ikarus_open_doors
    "Константин пожал плечами и сел на стул."
    kt "Ну поговорим.{w} Чего расскажешь?"
    hide image val_sad
    show image val_smile2
    with byso
    val "Чего-чего...{w=1} Хрен его знает.{w} Расскажи чего там нового в родном мире."
    kt "Ничего особенного, никаких таких интересных новостей.{w=1} Всё обыденно и уныло."
    hide image val_smile2
    show image val_sad
    with byso
    val "М-м-м...{w=1} Печалька.{w} Я то думала что хоть что-то изменится."
    val "Разрешат эксперименты над людьми... {w=1}Или может введут эвтаназию..."
    val "Скучно жить в мире, который не ценит талантов...{w=1} Зато тут есть генмод, хоть какая-то радость."
    val "Ну подумаешь четверо подопытных умерли, всего-то."
    val "На многие исследования уходили массы человеческих жертв."
    hide image val_sad
    show image val_calm
    with byso
    val "Опыты над людьми в Гватемале...{w=1} Эксперименты отряда 731...{w} Не все увенчались успехом конечно..."
    kt "А, то есть врачебный такт и клятва Гиппократа тебя вообще не волнуют?"
    hide image val_calm
    show image val_smile2
    with byso
    "Валери улыбнулась и повернула голову в сторону Константина."
    val "Врачебный такт - чушь, а клятву Гиппократа я не давала."
    val "Да даже если бы и давала...{w=1} Насилие это приятно..."
    "Перевалившись набок к Константину, она продолжила."
    hide image val_smile2
    show image val_calm
    with byso
    val "Иногда приходится потерпеть небольшую боль, чтобы достичь наслаждения."
    val "Многие просто считают боль чем-то страшным... {w=1}Но это не так, боль может быть прекрасна."
    val "Самая прекрасная боль - это боль свободная от страха, печали и волнений.{w=1} Лучшая боль - это чистая боль."
    kt "Тут уж мне стало интересно, кем ты была до инреальности?"
    "Сев на кушетку, Валери поправила маску."
    hide image val_calm
    show image val_smile
    with byso
    val "Я то? Студентка меда."
    kt "Не особо мне верится, что вот такой может быть студентка."
    hide image val_smile
    show image val_smile2
    with byso
    "Валери улыбнулась и, достав ручку, начала раскручивать её в руке."
    val "Неужели?{w=1} Ну слушай тогда."
    val "Сказочка о девочке со шрамом..."
    stop ambience fadeout 1
    scene bg valeri_cg with byso
    val "Послушная и талантливая девочка, отличница, которая училась первый курс на патологоанатома."
    val "За спиной 11 лет унижений за шрам на губе, который остался благодаря папочке."
    val "Мамочка, которая бухала как не в себя и избивала свою дочурку."
    scene bg semen_room
    show shum_white
    with flash
    nap "Папа, не бей меня, пожалуйста!"
    fath "Знать будешь, как с такими общаться, дура!"
    scene bg semen_room
    show shum_white
    with flash
    nap "Мама!{w=1} Не надо!"
    moth "Да-а, тройка и не бей?! {w=1}Нет, сука, будешь знать!"
    "Девочка пыталась укрыться от кулаков матери, но безуспешно."
    scene bg valeri_cg with flash
    val "Религиозные бабушка и дедушка, которые хотели воспитать из внучки покорную тварь божью."
    val "Девочку били...{w=1} Её высмеивали...{w=1} На её чувства все плевали..."
    scene bg street
    show shum_white
    with flash
    dnokl "На тебе!{w=1} Нечего было с Дашей пререкаться!"
    nap "Нет, хватит, пожалуйста!"
    dnokl "Нет уж, блядь, ты не отвертишься!"
    scene bg valeri_cg with flash
    "Валери отложила ручку и закинула ногу на ногу."
    val "И, конечно же, любовь к мальчику с атлетичной фигурой, красивыми и шелковистыми волосами коричневого цвета.{w=1} Казалось бы, девочка нашла сокровище прямо на межвузовском конкурсе..."
    scene bg bus_stop
    show shum_white
    with flash
    nap "Ты мне нравишься..."
    rmp "Знаешь, ты мне тоже!"
    scene bg valeri_cg with flash
    val "Это был плохой мальчик.{w=1} Накачав девочку наркотиками, он воспользовался ей."
    val "Психика её начала страдать, девочка начала употреблять и вести странную половую жизнь."
    val "Исходом стал очередной поход к тому-самому мальчику..."
    scene bg pados
    show shum_white
    with flash
    rmp "Чё ты припёрлась?"
    nap "Дашь немного-немного марочек?..."
    scene bg valeri_cg with flash
    val "Где он, к сожалению, не смог удовлетворить потребность девочки."
    val "За что эта девочка и расчленила мальчика...{w=1} По всем правилам патологоанатома."
    "Она с удовольствием растягивала каждое слово, словно вспоминая и переживая эти чувства вновь."
    scene bg semen_room
    show shum_white
    with flash
    "Девочка при помощи скальпеля извлекала из груди мальчика все органы."
    nap "Потому что у моей любви...{w=1} Нет здоровой головы."
    "Напевала девочка, оперируя скальпелем."
    scene bg valeri_cg with flash
    val "Сердечко в одну ёмкость, лёгкие во вторую и ЖКТ в третью..."
    val "И хотелось девочке видеть, что бы почувствовали родные и любимые мальчика, когда у них под дверью оказался мясной конструктор..."
    val "Но девочку забрал мужчина в овальных очках и белом халате."
    scene bg semen_room
    show shum_white
    with flash
    so "Ты пойдёшь со мной...{w=1} как и он..."
    nap "У меня будет шанс на второй раунд?!"
    scene bg valeri_cg with flash
    val "А сейчас девочка знает, что мальчик который с ней в этом мире переродился, когда-нибудь с ней снова встретится."
    val "И в этот раз она не позволит ему так быстро умереть..."
    val "Вот и сказочке конец..."
    kt "Н-да...{w=1} Неприятная история...{w=1} Не позавидуешь..."
    scene bg int_aidpost_day_apple
    show image val_calm
    with byso
    play ambience ambience_medstation_inside_day fadein 1
    "Валери сильно удивилась призрачному сочувствию Константина."
    val "Хм-м, ты первый мальчик за всё время, кто мне посочувствовал."
    kt "Да не то что бы, просто я понимаю то, что ты в этом плане виновата частично."
    hide image val_calm
    show image val_surprise
    with byso
    val "Это в каком смысле?"
    "Ещё сильнее удивилась она."
    kt "У меня в кой-то мере похожая история.{w=1} В том что ты стала такой ты не виновата, потому я тебя не виню в содеянном."
    kt "Не то что бы я отец крёстный и прощаю твои грехи, я скорее про то, что могу тебя понять."
    hide image val_surprise
    show image val_smile
    with byso
    "Пытался сформулировать мысль Константин.{w=1} Валери улыбнулась."
    val "Я поняла.{w} Что сказать...{w=1} ты хороший мальчик.{w=1} Первый кто меня выслушал..."
    val "И я тебе благодарна.{w} Тебе там припасы были нужны?"
    kt "Да, не за что.{w=1} Перекись, три бинта, обезболивающие."
    play sound sfx_open_table
    hide image val_smile
    show image val_sad
    with byso
    "Она наклонилась к ящикам и начала в них копаться."
    hide image val_sad
    show image val_smile2
    with byso
    val "Я даже знаю кому нужны обезболы - Олегу."
    kt "С чего ты взяла?"
    play sound sfx_clench2
    play sound2 sfx_blow_out_candle
    "Валери достала все нужные Константину припасы и поставила на стол."
    hide image val_smile2
    show image val_smile
    with byso
    val "Да ты бы видел его моську, когда я у него кровь брала... Он аж расплакался."
    "Константин усмехнулся и достал пакет."
    kt "Прикольно. Сколько с меня?"
    play sound sfx_cigarette_pack_crumple
    "Валери положила все медикаменты в пакет Константина."
    hide image val_smile
    show image val_sad
    with byso
    val "Не надо мне денег, только обещай что ещё зайдёшь ко мне поболтать."
    window hide
    menu:
        "Хорошо, обещаю.":
            $ renpy.block_rollback()
            $ valeri += 1;
            hide image val_sad
            show image val_smile2
            with byso
            val "Хорошо. Приходи, буду ждать."
            play sound glad
            "Протянула Валери и погладила Константина по шее."
            kt "До встречи."
            "Константин пошёл на выход."
        "Не уверен.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            kt "Я в отряде зачистки, ничего не могу знать наперёд."
            val "Тоже верно... Но ты заходи..."
            "Опечалено проговорила Валери. Константин отправился на выход."
    val "До встречи."
    scene bg ext_aidpost_day with byso
    play ambience ambience_ext_road_day fadein 1
    play sound door_cl
    play sound2 light_inh
    stop music fadeout 3
    "Он вышел из медпункта и закурил."
    play music BlueJetta fadein 3
    th "М-да..."
    th "Инреальность, всё-таки, сборник огромного количества людей, несчастных по судьбе."
    th "Валери чем-то похожа на Батори, правда <<почерк>> у них разный."
    th "От медсестры веет психопатей.{w=1} Она не убивает просто так, иначе она бы давно была врагом сопротивления."
    th "Хоть нормальной её не назвать, но её такой сделала жизнь."
    th "Можно провести параллель с моей..."
    th "А Батори полноценная психопатка, без установленных на то причин."
    th "Хотя как сказать...{w=1} Я ничего не знаю практически.{w} Всё что я помню, так это то, что она кого-то ищет."
    th "Неизвестно с какой целью, но судя по методам поиска не с самой благоприятной..."
    scene bg ext_library_day with fade
    "Дойдя до библиотеки, он услышал громкие споры."
    irr "...что такое?{w=1} Пустышичек безмозглых жалко?!"
    oleg "Это люди, Ира!"
    liz "Сколько раз тебе это повторяли!{w=1} Из-за твоих рекомендаций капитану мы вынуждены марать руки кровью."
    irr "Боже, дайте табельное, я застрелю вас обоих и себя!"
    play sound door_break
    show image oleg_angry at left
    show image liz_angry at right
    with byso
    "Из библиотеки вышла разъярённая Лиза и Олег."
    "Заметив Константина, Лиза немного успокоилась."
    hide image oleg_angry
    show image oleg_shy at left
    with byso
    oleg "Долго ты..."
    hide image liz_angry
    show image liz_bukal at right
    with byso
    liz "Ага, мы думали тебя уже в чёрном мешке вынесут.{w=1} Чего задержался то?"
    kt "Да так, по мелочи.{w} Поболтал с Валери."
    hide image liz_bukal
    show image liz_surp at right
    hide image oleg_shy
    show image oleg_think at left
    with byso
    "Лизу и Олега поразили слова Константина."
    oleg "Поболтал?!{w} Ну ничего себе ты зверь!"
    liz "Олег имел ввиду...{w=1} Как?!{w} Как ты вообще нашёл с ней общий язык?"
if valeri == 1:
    kt "Ну, просто пообщались как человек с человеком.{w=1} Просила меня как-нибудь вернуться."
    hide image liz_surp
    show image liz_angry at right
    with byso
    "Олег ещё больше удивился, а Лиза разозлилась."
    oleg "Ну ты даёшь!"
    liz "Человек?!{w=1} Это?!{w} Нет, это монстр!"
    kt "Почему ты так считаешь?"
    hide image liz_angry
    show image liz_rage at right
    with byso
    liz "Тебя не смущает что она своими руками, своими <<экспериментиками>> убила четверых?!"
    kt "А ты хоть что-то из её прошлой жизни знаешь?"
    hide image liz_rage
    show image liz_surp at right
    with byso
    play sound sfx_dinner_horn_processed
    "Лиза сильно удивилась подобному вопросу.{w=1} Заиграл горн."
    kt "Вот именно, потому не делай поспешных суждений. А теперь пошли в столовую."
    jump fniwujonidfsanidfsaifnoasdifbnasd
else:
    kt "Ну просто.{w=1} Слово за слово... {w=1}Ну так и поговорили."
    hide image liz_surp
    show image liz_normal at right
    with byso
    liz "Ладно...{w=1} Но уважаю, даже с таким монстром нашёл общий язык."
    th "Ну...{w=1} Монстр не особо корректное определение..."
    oleg "Да уж, мастер переговоров."
    play sound sfx_dinner_horn_processed
    "Заиграл горн."
    kt "В столовую."
    jump fniwujonidfsanidfsaifnoasdifbnasd
label fniwujonidfsanidfsaifnoasdifbnasd:
    liz "Ладно, идём..."
    scene bg ext_houses_day
    show image oleg_think at left
    show image liz_bukal at right
    with byso
    "Пройдя небольшое расстояние, Олег перебил неловкое молчание."
    oleg "Кость, а ты принёс медикаменты?"
    "Константин протянул мешок в котором лежали все нужные медикаменты."
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "Отлично."
    play sound monety
    "Олег взял у него пакет, а Константин протянул Лизе деньги."
    kt "Возвращаю."
    hide image liz_bukal
    show image liz_surp at right
    with byso
    liz "Как?"
    kt "Коммуникабельность."
    hide image liz_surp
    show image liz_smile at right
    with byso
    liz "Ладно, оставь себе.{w=1} Может у Гордона чего ухватишь."
    kt "Хорошо."
    "Ответил Константин и вернул монеты в карман."
    stop music fadeout 3
    scene bg int_dining_hall_day
    show mi happy pioneer
    show image oleg_think at left
    show image liz_normal at right
    with fade
    play ambience ambience_dining_hall_empty fadein 1
    play music cirk fadein 3
    "В столовой на раздаче снова стояла девочка похожая на Мику.{w=1} Заметив отряд, она улыбнулась."
    mip "А вот и моя зарплата пришла...{w} Вам чего?{w} Стандартная - картошка с грибами.{w=1} Продвинутая - макароны по-флотски."
    kt "Продвинутая."
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Мне тоже."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "А мне стандартную..."
    hide image liz_bukal
    show image liz_grin at right
    with byso
    "Уныло выдохнул Олег.{w=1} Женя и Константин усмехнулись."
    show mi grin pioneer with byso
    mip "Да чего вы...{w=1} Это не смешно это грустно..."
    hide image oleg_shy
    show image oleg_angry at left
    with byso
    "С усмешкой ответила девочка за стойкой.{w=1} Олег разозлился."
    oleg "Ну я хотя-б не Мику!"
    show mi rage pioneer with byso
    hide mi with byso
    "Все трое пошли за столик под отборный мат из-за раздачи."
    hide image liz_grin
    show image liz_dontlike at right
    with byso
    stop music fadeout 3
    liz "Ну ты перегнул.{w=1} Это было обидно."
    oleg "Мне тоже вообще-то!"
    play music god fadein 3
    "В столовую вошла Валери и осмотрелась."
    hide image liz_dontlike
    hide image oleg_angry
    show image oleg_shy at left
    show image liz_bukal at right
    with byso
    "Олег опустил глаза в свою тарелку, а Лиза отвернулась."
    "Найдя глазами Константина, она направилась к нему."
    show image val_smile with byso
    val "Вот, держи."
    play sound sfx_paper_bag
    "Валери передала ему письмо."
    kt "Что это?"
    hide image val_smile
    show image val_sad
    with byso
    "В ответ она покраснела и отмахнулась."
    val "Когда доедешь до той симуляции, прочитай.{w} Сейчас нельзя. {w=1}Просто мне кажется что я что-то поняла."
    kt "Ладно, понял."
if valeri == 1:
    hide image val_sad
    show image val_smile2
    with byso
    val "Отлично!"
    hide image liz_bukal
    show image liz_dontlike at right
    with byso
    play sound glad
    "Подметила Валери и разворошила волосы на голове Константина, чем вогнала Лизу в ступор."
    val "Я пойду. Увидимся."
    kt "Пока."
    hide image val_smile2
    hide image oleg_shy
    show image oleg_think at left
    with byso
    "Валери ушла.{w=1} Олег поднял голову, а Лиза укоризненно смотрела на Константина."
    kt "Ничего не было, не подумай."
    liz "Да это я поняла что <<не было>>, так бы твой труп по симуляции уже искали..."
    oleg "М-да...{w} Хорошо ты её к себе расположил..."
    hide image liz_dontlike
    show image liz_angry at right
    with byso
    liz "Не то слово...{w=1} Жуть какая..."
    jump gnisdnujisfsgnpfgsfnjipfgsnjpsfgjn
else:
    hide image val_sad
    show image val_calm
    with byso
    val "Хорошо.{w} Не заразитесь там никакой гадостью, а то у меня на столе окажетесь."
    hide image val_calm
    hide image liz_bukal
    hide image oleg_shy
    show image oleg_think at left
    show image liz_angry at right
    with byso
    "Поучила Валери и ушла.{w=1} Лиза гневно провожала её взглядом, а Олег поднял глаза."
    liz "Ну ты на неё посмотри.{w=1} Несмотря на то что она наш союзник, она нам всё равно угрожает."
    oleg "Да-да...{w=1} Так даже кажется что Батори лучше..."
    liz "Не то слово...{w=1} Жуть..."
    jump gnisdnujisfsgnpfgsfnjipfgsnjpsfgjn
label gnisdnujisfsgnpfgsfnjipfgsnjpsfgjn:
    stop music fadeout 2
    play sound dvizh
    hide image oleg_think
    hide image liz_angry
    show image pas_smile
    show image liz_bukal at right
    show image oleg_shy at left
    with byso
    "К их столику подошёл Гордон и сел на пододвинутый стул."
    play music music_list["silhouette_in_sunset"] fadein 3
    pas "Ну что, молодые, чё как?"
    kt "Порядок.{w=1} Слушай, а что у тебя есть полезного на 10 рублей?"
    oleg "Не думаю что что-то полезное..."
    hide image pas_smile
    show image pas_angry
    with byso
    pas "А я себе менеджера не нанимал."
    "Ответил Гордон Олегу. Лиза усмехнулась."
    hide image pas_angry
    show image pas_normal
    with byso
    pas "Сейчас к сожалению и в правду не могу ничего предложить.{w} Те две кубышки на благотворительность это отдали..."
    pas "Как приедешь - предложу что-то стоящее твоего внимания."
    hide image oleg_shy
    show image oleg_happy at left
    with byso
    oleg "Правильно, новую модель плазмоинтегратора."
    hide image pas_normal
    show image pas_angry
    hide image liz_bukal
    show image liz_laugh at right
    with byso
    "Пошутил Олег.{w=1} Гордон нахмурился, а Лиза и Константин рассмеялись."
    pas "Вот же сучий потрох, а? {w}Прям как клоун из анекдота..."
    hide image liz_laugh
    show image liz_grin at right
    with byso
    liz "Что за анекдот?"
    hide image pas_angry
    show image pas_smile
    with byso
    pas "Да совсем короткий.{w} Ебёт один клоун другого, как вдруг один оборачивается и говорит:<<Вот что-то уже нихуя не смешно>>."
    hide image oleg_happy
    show image oleg_shy at left
    hide image liz_grin
    show image liz_laugh at right
    with byso
    "На этот раз рассмеялись все кроме Олега."
    hide image oleg_shy
    show image oleg_think at left
    hide image liz_laugh
    show image liz_grin at right
    with byso
    "Спустя некоторое время, весь отряд встал и собрал тарелки."
    pas "Ну лады, товарищи, в добрый путь."
    scene bg ext_dining_hall_near_day
    show image liz_grin at right
    show image oleg_think at left
    with byso
    play ambience ambience_camp_center_day fadein 1
    stop music fadeout 3
    "Отряд вышел из столовой под неприязненный взгляд Мику."
    kt "А какова вероятность того, что симуляция в которую мы едем уничтожена?"
    hide image liz_grin
    show image liz_bukal at right
    with byso
    liz "Нулевая."
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "Ага, мы всё уже узнали в логистике."
    hide image liz_bukal
    show image liz_angry at right
    with byso
    liz "Не без споров конечно-же."
    "Укоризненно проворчала Лиза и отвела взгляд."
    kt "Да я слышал.{w} А в чём разногласие-то возникло?"
    hide image oleg_smile
    show image oleg_shy at left
    with byso
    oleg "Ира как всегда."
    hide image liz_angry
    show image liz_bukal at right
    with byso
    liz "Она говорит, мол, это нормально просто так убивать людей."
    liz "Жизнь тех, кто был слишком сильно видоизменен инреальностью не имеет смысла."
    kt "Понимаю..."
    scene bg ext_camp_entrance_day
    show image oleg_think at left
    show image liz_normal at right
    show image andr_normal
    with fade
    play music regret fadein 3
    "У выхода из лагеря их встретил Андрей."
    andr "А вот и вы."
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Гордон нам обновил трансформатор?"
    hide image andr_normal
    show image andr_normal2
    with byso
    andr "Да.{w=1} Только полчаса назад ушёл."
    hide image oleg_think
    show image oleg_happy at left
    with byso
    oleg "Ура!"
    "Радостно выкрикнул Олег.{w=1} Андрей же не разделял его счастья."
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Как только вы прибудете на место, свяжитесь с нами через точку связи.{w=1} По мере возможности обыщите склады и на обратном пути заберите двух путников."
    kt "Понято-принято."
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    oleg "Так точно."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Хорошо."
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "Тогда выезжайте.{w=1} Удачи, бойцы."
    hide image andr_normal3 with byso
    "Пожелал Андрей и ушёл обратно в лагерь."
    scene bg int_avtobus
    show image oleg_happy at right
    show image liz_bukal at left
    with byso
    play ambience ambience_camp_center_day volume 0.7 fadein 1
    play sound sfx_open_window
    "Войдя в автобус, Константин почувствовал запах свежей сварки и открыл окно. Олег был вне себя от радости."
    oleg "Вот это да!{w=1} Автоматический круиз контроль!{w} Слава научным трудам Гордона!"
    hide image liz_bukal
    show image liz_smile at left
    with byso
    liz "Заводи."
    play sound sfx_blanket_off_stand
    "Приказала Лиза и расстелила на задней площадке плед."
    play sound korobka_peredach
    play ambience sfx_bus_idle volume 0.5 fadein 1
    hide image oleg_happy
    show image oleg_smile at right
    with byso
    "Олег проскрипел коробкой передач и автобус завёлся."
    oleg "22-25а. Поехали!"
    play sound sfx_ikarus_open_doors
    play ambience bus_inside volume 0.2 fadein 1
    stop music fadeout 3
    hide image oleg_smile
    show image oleg_happy at right
    with byso
    "Двери закрылись и автобус начал движение.{w=1} Олег быстро вернулся и сел на плед."
    liz "Кость, вот тебе литература на почитать."
    play sound sfx_paper_bag
    "Лиза дала ему белую папку с подписью <<#4>>."
    scene bg int_avtobus2 with byso
    hide image liz_smile
    show image liz_normal at left
    with byso
    liz "Мы с Олегом пока в карты поиграем."
    kt "И без меня?!"
    hide image liz_normal
    show image liz_grin at left
    with byso
    "С наигранной злобой воскликнул Константин.{w=1} Лиза улыбнулась."
    liz "Ничего, ты тоже поиграешь, только тебе с этим надо ознакомиться в обязательном порядке."
    hide image oleg_happy
    show image oleg_smile at right
    with byso
    oleg "Не бойся, карты не съедим."
    kt "Ладно-ладно, я понял."
    hide image oleg_smile
    hide image liz_grin
    with byso
    play sound sfx_paper_bag
    play music deadrazy2 fadein 7
    "Выдохнул Константин и открыл папку на первом листе."
    window hide
    $ set_mode_nvl()
    "{font=inrealnost/font/NoRules.ttf}Если кто-то это читает значит это не было бесполезной работой."
    th "Это уже не было бесполезной работой, раз это сочинение всё сопротивление читает."
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
    show image oleg_think at right
    show image liz_bukal at left
    with byso
    kt "Слушай, а на кой хрен этот Миша делит всё это счастье на кучу страниц?"
    oleg "Нашёл кого спросить!{w=1} Мы сами не знаем."
    liz "Может ему казалось что так удобнее, но получилось как всегда."
    hide image oleg_think
    hide image liz_bukal
    with byso
    play sound sfx_paper_bag
    "Константин усмехнулся и перевернул страницу."
    window hide
    $ set_mode_nvl()
    "{font=inrealnost/font/NoRules.ttf}Силы контроля."
    "{font=inrealnost/font/NoRules.ttf}Если говорить о базовых силах контроля симуляции, то их две: генмод и ЭМ-ограды."
    "{font=inrealnost/font/NoRules.ttf}Так же инреальность позволяет людям проявлять нечеловеческие силы. Происходит это самопроизвольно и/или при смерти. Определяется расположенностью."
    "{font=inrealnost/font/NoRules.ttf}Расположенность - константа, уникальная для каждого субъекта. Определяет возможности к той или иной силе."
    "{font=inrealnost/font/NoRules.ttf}Для принудительного развития силы следует изменить в меньшую сторону стабильность симуляции. Ошибка, развивающая силы в путнике называется дарующей."
    "{font=inrealnost/font/NoRules.ttf}Ошибка является редкой и иногда передаёт способности создателя, смотри Существа, страница 5."
    "{font=inrealnost/font/NoRules.ttf}На способности путников распыляться не имеет смысла. Их много и не все известны."
    nvl clear
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
    show image oleg_think at right
    show image liz_bukal at left
    with byso
    kt "Слушайте, а какого хрена тогда Валери проводит эксперименты с генмодом, если делать этого нельзя?"
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Сам знаешь, у неё беды с башкой!"
    liz "Она сказала что у неё есть вакцина от терминальной стадии."
    kt "И что же это?"
    hide image liz_bukal
    show image liz_angry at left
    with byso
    liz "Не знаю, но доказательства излечения она предоставила."
    oleg "Только потом всё-равно отравила парня, потому что тот ей напоминал отца."
    th "Да уж, тяжёлые у неё травмы..."
    kt "Понятно..."
    hide image oleg_shy
    hide image liz_angry
    with byso
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
    th "М-да, вот не в падлу же этому Михаилу было всё это исследовать..."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Лирика."
    "{font=inrealnost/font/NoRules.ttf}Немного лирики для самого себя.{w} Можете пропустить."
    "Константин выбрал один из написанных ниже элементов лирического отступления."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}ИСТЕКАЯ ДОБРОТОЙ"
    ""
    "{font=inrealnost/font/NoRules.ttf}Свет внутри меня -"
    "{font=inrealnost/font/NoRules.ttf}Больше, чем просто свет -"
    "{font=inrealnost/font/NoRules.ttf}Это новая заря,"
    "{font=inrealnost/font/NoRules.ttf}Золотого века человека..."
    "{font=inrealnost/font/NoRules.ttf}Но вокруг -"
    "{font=inrealnost/font/NoRules.ttf}Погасшие люди - изранены злобой."
    "{font=inrealnost/font/NoRules.ttf}Новый круг -"
    "{font=inrealnost/font/NoRules.ttf}Череда предательств, такой знакомый..."
    ""
    "{font=inrealnost/font/NoRules.ttf}Истекая добротой из открытых ран -"
    "{font=inrealnost/font/NoRules.ttf}Вспомни о том, что желал сам -"
    "{font=inrealnost/font/NoRules.ttf}Отдавать себя до последнего грамма души."
    "{font=inrealnost/font/NoRules.ttf}Истекая добротой от ножей в спине -"
    "{font=inrealnost/font/NoRules.ttf}Даруй последний свой огонь, как Прометей -"
    "{font=inrealnost/font/NoRules.ttf}И ни о чем, ни о чем не жалей..."
    "{font=inrealnost/font/NoRules.ttf}Ты сделал всё, что сумел."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Пометки о прочтении."
    "{font=inrealnost/font/NoRules.ttf}Если ты прочёл это писание, то оставь пометку. {w}Это позволит вести счёт оригинальных симуляций, которые с текстом ознакомились."
    "Подписей на странице было 6.{w} Михаил, Андрей, Максим, Ирина, Елизавета, Семён."
    window hide
    $ set_mode_adv()
    window show
    stop music fadeout 3
    show image oleg_think at right
    show image liz_bukal at left
    with byso
    kt "Вопрос, а на кой хер ты и Ира подписали имена?"
    hide image liz_bukal
    show image liz_angry at left
    with byso
    "Лиза сосредоточилась на картах."
    liz "Я не была в тот момент в сопротивлении, а Ира не знаю."
    kt "Понятно."
    play sound bus_sms
    pause 1
    play sound2 card_take
    hide image oleg_think
    show image oleg_angry
    with byso
    "Приборная панель запиликала, а Олег яростно кинул карты и направился к ней."
    hide image liz_angry
    show image liz_surp at left
    with byso 
    oleg "Фуллхаус твою налево!"
    hide image oleg_angry with byso
    liz "Мы в дурака играли..."
    kt "Чего там?"
    play music stresss fadein 3
    show image oleg_think at right with byso
    "Удивлённый Олег вернулся на место."
    oleg "Не знаю как...{w=1}  Но через две наша.{w=1} Время там - 10 вечера.{w=1} Идеально чтоб прогуляться."
    hide image liz_surp
    show image liz_dontlike at left
    with byso 
    liz "Быстро мы!"
    kt "Это да..."
    oleg "Знал бы сам почему...{w=1} Нам ехать даже с новым трансформатором не менее 4х часов."
    liz "Я наверное поняла почему...{w=1} Мы проехали через уничтоженные симуляции...{w} Ты же слышал странные звуки вдалеке?"
    kt "Какие это?"
    hide image liz_dontlike
    show image liz_bukal at left
    with byso 
    liz "Ну крики..."
    "Олег почесал подбородок."
    kt "Я был слишком увлечён чтением."
    oleg "Возможно...{w=1} Но я думал это колёса скрипят..."
    liz "Жаль. Походу, мы обратно так не проедем..."
    kt "Почему?"
    oleg "Трансформатор самостоятельно обрабатывает маршруты, я тут не при чём.{w=1} По кошмару он не поедет по настройкам Гордона."
    liz "Олег, попробуй установить обратный маршрут."
    hide image oleg_think
    hide image liz_bukal
    show image liz_bukal
    with byso
    "Олег пошёл обратно к приборной панели и начал там ковыряться."
    kt "Я так и не понял...{w=1} Как скорость связана со стабильностью симуляции?"
    hide image liz_bukal
    show image liz_grin
    with byso
    liz "Во, научным языком заговорил."
    "Подшутила Лиза."
    hide image liz_grin
    show image liz_bukal
    with byso
    liz "Короче.{w=1} Если ты едешь через симуляции с низкой стабильностью, то это трансформатор может в силу ошибки проскочить пару-тройку симуляций."
    liz "Ошибки симуляции позволяют буквально проезжать сквозь пространство по прямой, минуя углы и прочее счастье."
    show image oleg_think at right
    hide image liz_bukal
    show image liz_normal at left
    with byso
    oleg "Боюсь нам так не повезёт на обратном пути."
    kt "А чё так?"
    oleg "Мы поедем по схожему маршруту со вчерашним. 5 плюс-минус 1 час."
    "Константин пожал плечами."
    kt "Ну, я хоть посплю."
    hide image liz_normal
    show image liz_smile at left
    with byso
    liz "Да-а, было бы не плохо."
    hide image oleg_think
    show image oleg_smile at right
    with byso
    oleg "Ладно, держите перехватчики кода."
    "Олег выдал им по пульту."
    kt "Что это?"
    hide image oleg_smile
    show image oleg_happy at right
    with byso
    oleg "Красная кнопка!"
    "Достаточно исчерпывающе описал прибор Олег."
    hide image liz_smile
    show image liz_normal at left
    with byso
    liz "Эта хрень моментально телепортирует тебя в заданную по настройкам симуляцию."
    hide image oleg_happy 
    show image oleg_think at right
    with byso
    oleg "Гордон недавно выпустил что-б не помирало много новичков от Батори."
    kt "Любопытно..."
    "Автобус постепенно начал тормозить."
    hide image liz_normal
    show image liz_bukal at left
    with byso
    liz "Оружие заряжено?"
    kt "Да. На предохранителе в кобуре."
    liz "Отлично."
    stop music fadeout 3
    play sound2 sfx_bus_stop volume 0.7
    play sound sfx_ikarus_open_doors
    play ambience ambience_camp_entrance_night fadein 3
    "Автобус остановился и двери открылись."
    oleg "Теперь пошли."
    scene bg ext_bus_night
    show image oleg_think at left
    show image liz_normal at right
    with byso
    play music lim fadein 3
    "Отряд вышел из автобуса, вокруг всё было в достаточной мере тихо."
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Нам в старый корпус.{w=1} Направо."
    kt "Зачем?"
    liz "Там пункт связи, а также основной пункт прибытия по <<красной кнопке>>."
    kt "Идём."
    scene bg int_old_building_night
    show image oleg_think at left
    show image liz_normal at right
    with fade
    "Дойдя до старого корпуса, они вошли внутрь.{w=1} В нём царил запах плесени и сырости."
    kt "И где тут пункт связи?"
    hide image liz_normal
    show image liz_smile at right
    with byso
    "В ответ Лиза лишь усмехнулась."
    liz "Много вопросов задаёшь."
    play sound sfx_open_metal_hatch
    hide image oleg_think with byso
    "Олег начал открывать люк, расположенный на полу."
    kt "А-а, точно, бункер."
    scene bg int_catacombs_living
    show image liz_bukal at right
    show image oleg_shy at left
    with fade
    play ambience ambience_catacombs fadein 1
    "Войдя в бункер, Лиза начала настраивать радиотехнику."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Какая частота?"
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "124.1 вроде."
    play sound sfx_radio_tune
    "Лиза настроилась на частоту."
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "<<Дзета>> вызывает капитана.{w=1} Приём."
    th "М-м...{w=1} Позывные даже на радио..."
    play sound sfx_bed_squeak1
    "Олег облокотился на шкафчики, а Константин сел на кровать."
    "Радио молчало."
    liz "Повторяю, <<Дзета>> вызывает капитана.{w=1} Приём."
    andr "Капитан на связи.{w=1} Докладывайте.{w=1} Приём."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Мы на месте.{w=1} Какие будут указания?"
    stop music
    play sound pum
    andr "Итак.{w=1} Ваша задача из медпункта вынести всё, что возможно, привезти двух-трёх путников и в центре лагеря разбить ампулу генмода."
    play music paralysis fadein 1
    hide image liz_normal
    show image liz_rage at right
    hide image oleg_think
    show image oleg_shy at left
    with byso
    liz "Чего?!{w=1} Какой генмод?!{w=1} Тут путников вагон и телега!!!"
    th "Это что-ж получается..."
    andr "Нас уже не интересует.{w=1} Сил нам хватает."
    oleg "Нельзя убивать столько людей!!!"
    andr "Это приказ!{w=1} Не обсуждается!"
    th "Сопротивление переобулось..."
    "Подумал Константин и подошёл к станции."
    liz "Но это же люди!"
    andr "Тут логика простая.{w=1} Либо убиваете их, либо умираете с ними."
    kt "Ладно, мы поняли. Какие будут ещё указания?"
    liz "Костя, блять!"
    andr "Отлично. На этом всё, после этого вы покидаете симуляцию. Конец связи."
    play sound sfx_radio_squelch_2
    "Радио зашипело и выключилось."
    liz "Что значит <<мы поняли>>?!{w} Ты там после диалогов с Валери напрочь ебанулся?!"
    kt "Если этого не хочешь делать ты, то это сделаю я."
    liz "Но..."
    kt "Лиз, не начинай.{w=1} Это залог нашей победы."
    oleg "Костя прав...{w=1} Нам нужно внести свой вклад в победу."
    liz "И ты туда-же?!{w=1} Вы оба, блять головой уебались?!{w=1} Вы несёте хуйню!"
    liz "Я вас старше по званию и я вам предписываю не делать этого!{w=1} Мы забираем Лену и уезжаем!"
    oleg "Прости, но нет.{w=1} Мы должны это сделать."
    liz "Да когда же тебе, сука, <<Эрида>> мозги промыла, блять!"
    play sound sfx_pat_shoulder_hard
    play music proshloe fadein 2
    hide image oleg_shy
    show image oleg_think at fleft
    hide image liz_rage
    show image liz_shysurp
    with byso
    "Константин подошёл к Лизе и обнял её.{w} Она вмиг окрасилась красным и замолчала."
    kt "Хватит.{w} Успокойся, переведи дыхание.{w} Все хорошо."
    hide image oleg_think
    show image oleg_smile at fleft
    with byso
    "Погладив её по спине, Константин обратил внимание на Олега, который за спиной Лизы руками показывал большой палец, одобряя такой способ её успокоить."
    kt "Я думаю что куда больше людей страдает от Генды. Мы должны это исправить."
    kt "Счастье надо завоевать и мы все своё завоюем. Эта жертва будет во благо людей инреальности."
    hide image liz_shysurp
    show image liz_sad
    with byso
    liz "Ладно...{w=1} Может ты и прав..."
    play sound sfx_grate_hand_fall
    hide image liz_sad
    show image liz_sad at right
    hide image oleg_smile
    show image oleg_smile at left
    with byso
    "Олег сорвал дверь шкафчика с петель и достал небольшую белую коробочку с красным крестом."
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Тогда начали."
    hide image liz_sad
    show image liz_dontlike at right
    with byso
    liz "Хорошо, кого мы заберём для Валери?"
    play sound sfx_paper_bag
    stop music fadeout 3
    hide image oleg_happy
    show image oleg_think at left
    with byso
    "Константин вспомнил про конверт.{w=1} Достав его, он разорвал упаковку и обнаружил внутри пожелтевшую бумажку."
    "На ней было что-то написано красными чернилами, но Константин не мог понять что именно."
    hide image liz_dontlike
    show image liz_sad at right
    with byso
    liz "Давай прочту."
    play sound sfx_paper_bag
    "Лиза взяла у Константина бумагу и начала читать."
    liz "Я поняла кого ты мне напоминаешь.{w=1} Я слышала что ты попал в инреальность с братом."
    liz "Мне в целом подойдёт любой человек, но если ты найдёшь..."
    "Пытаясь расшифровать написанное, Лиза всмотрелась в бумажку."
    play sound pum
    hide image liz_sad
    show image liz_surp at right
    with byso
    liz "Грачёва Романа Михайловича?"
    liz "Это же твой брат!"
    liz "То тащи ко мне именно его.{w=1} Это тот самый мальчик из сказки.{w=1} Люблю.{w=1} Твоя Валери."
    play music "<from 0 to 96>inrealnost/Music/Music/greedy_charm.mp3" fadein 5
    "Константин встал в ступор."
    oleg "В каком смысле брат?"
    hide image liz_surp
    show image liz_dontlike at right
    with byso
    liz "Что это значит?"
    "Константин лишь отрыл рот и в шоке смотрел на радио."
    kt "Тащим этого уёбка в автобус."
    oleg "Стой-стой...{w} Ты же не хочешь отдать свою родню на растерзание Валери?!"
    kt "Уже хочу..."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "Ладно..."
    "Олег был шокирован пожеланием Константина и отряд направился прочь из бункера."
    scene bg ext_old_building_night_moonlight
    show image oleg_shy at right
    show image liz_sad at left
    with fade
    play ambience ambience_camp_center_night fadein 1
    "Выйдя на поверхность, Константин осмотрелся."
    kt "Что дальше?"
    hide image liz_sad
    show image liz_normal at left
    with byso
    liz "Значит...{w=1} Я за Леной, Олег за припасами, а ты за Ромой."
    kt "Принял. Встретимся в автобусе?"
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Да, поехали."
    scene bg ext_path2_night with byso
    "Отряд разошёлся.{w=1} Константин направился в клубы."
    th "Вот же...{w} Мразь!"
    th "У него же была девушка!"
    th "И мало того девушка!{w=1} Он ещё и издевался над другими!"
    th "Я то думал что он со мной так плохо обошёлся, а он..."
    th "Бросил любившую его девчонку, так ещё и издевался над другими."
    th "Ну ничего-ничего.{w}.. Отомстим за всех..."
    scene bg ext_clubs_night with byso
    "Он дошёл до клубов, откуда доносились периодичные шлепки. {w}Константин достаточно быстро сообразил что происходит."
    th "Блять, ты сука серьёзно?!"
    scene bg int_clubs_male_night with byso
    play ambience ambience_int_cabin_night fadein 1
    play sound sfx_door_squeak_light
    "Константин тихо открыл дверь и вошёл.{w} У окна стоял Рома и трахал Ольгу, лежащую на столе."
    play sound ammo volume 0.3
    "Достав пистолет, Константин начал подбираться к Роме."
    rm "Да-а, получай, пизда неёбаная."
    kt "Единственный кто тут получит, так это ты!!!"
    play sound sfx_lena_hits_alisa
    "Прокричал Константин и со всей силы огрел Рому по голове прикладом пистолета." with vpunch 
    "Рома упал без сознания. {w}Константин взглянул на бывшую вожатую."
    "Сахарова лежала на столе с пеной у рта и не подавала никаких признаков жизни. Константин взял её руку и пытался нащупать пульс."
    th "Пульса...{w} Нет?!"
    kt "Ёб твою мать блять!{w} Ты что, труп ебал?!" with vpunch 
    show image oleg_think with byso
    pause 0.1
    hide image oleg_think
    show image oleg_shy
    with bso
    play sound vomit
    pause 0.1
    hide image oleg_shy with byso
    "Константина стошнило. На крики в клуб прибежал Олег, но заметив картину быстро выбежал."
    kt "Блять{w=1}, больной,{w=1} нахуй,{w=1} ублюдок!" with vpunch 
    kt "Что с тобой не так, сука, объебос конченый!" with vpunch 
    play sound sfx_paper_bag
    "Отдышавшись, Константин накрыл лицо вожатой её панамкой, после чего взял со стола строительные хомуты и потащил Рому в автобус."
    scene bg int_avtobus2
    show image oleg_shy
    with fade
    play ambience ambience_camp_center_night volume 0.7 fadein 1
    play sound sfx_paper_bag
    "Дотащив Рому до автобуса, Константин обратился к Олегу и протянул пачку хомутов."
    kt "Свяжи этого уёбка, да покрепче!"
    oleg "Х-хорошо..."
    "Неуверенно пробормотал Олег и усадив Рому на сиденье, начал фиксировать его хомутами."
    scene bg ext_camp_entrance_night with byso
    play ambience ambience_camp_center_night fadein 1
    "Константин взял ампулу генмода и пошёл на площадь."
    scene bg ext_clubs_night
    show image liz_sad at left
    show un surprise pioneer at right
    with byso
    "По пути он встретил Лену и Лизу."
    liz "Ты уже тут. Доделывай, мы ждём в автобусе."
    un "П-привет?..."
    kt "Привет, понял..."
    scene bg ext_square_night with byso
    "Лиза и Лена побежали в автобус, а Константин, дойдя до площади, засмотрелся на ампулу с чёрной жидкостью."
    th "Блять...{w=1} Рома...{w} Невозможно просто!"
    th "Трахать трупы! Как до этого можно докатиться?!"
    play sound light_inh
    "Достав сигарету, Константин закурил."
    kt "Гори всё пламенем ада!"
    "Выкрикнул Константин и метнул ампулу в статую Генды."
    play sound glass_break
    pause 0.5
    play sound2 genmod
    "Ампула разбилась и раздалось шипение, словно при жарке на масле."
    scene bg ext_clubs_night with byso
    "Развернувшись, он со всех ног побежал в автобус."
    scene bg int_avtobus2
    show image liz_sad at right
    show un shocked pioneer at left
    show image oleg_shy
    with byso
    play ambience sfx_bus_idle volume 0.5 fadein 1
    "Забежав, Константин махнул рукой.{w} Автобус уже был заведён и все ждали Константина."
    play sound korobka_peredach
    play sound2 sfx_ikarus_open_doors
    play ambience bus_inside volume 0.2 fadein 1
    hide image oleg_shy
    show image oleg_think
    with byso
    "Олег скрипнул коробкой передач и автобус поехал."
    scene bg black with dissolve
    stop ambience fadeout 3
    stop music fadeout 2
    window hide dissolve
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
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt5b.png" with byso
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt_end3.png" with dissolve5
    pause 10
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt1.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt2.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt3a.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt4.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt5b.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt_end3.png"
    hide load
    scene bg black
    with dissolve
    stop music fadeout 2
    pause 1
    jump d5_withsopr_liz
label razvedfjdsvnifosdvhnisfnvisfdnvinifdn:
    hide image andr_normal2
    show image andr_normal3
    with byso
    andr "Отлично."
    play sound sfx_open_table
    hide image andr_normal3
    show image andr_normal
    with byso
    "Андрей что-то написал и убрал листик в ящик тумбочки."
    andr "Твои задачи тебе озвучит Ирина или же <<Эрида>>."
    andr "Теперь ты в её подчинении."
    kt "А в чём состоит задача разведки как таковой?"
    hide image andr_normal
    show image andr_normal3
    with byso
    "Андрей снял и протёр очки."
    andr "В основном наблюдение за состоянием инреальности.{w=1} В случае мобилизации вы переводитесь в логистику и координируете действия отрядов."
    kt "Хорошо.{w=1} Я понял.{w} А чем в штатное время занимается логистика?"
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "Координацией поставок, но я боюсь что эта информация тебе не пригодится."
    kt "Почему?"
    hide image andr_normal2
    show image andr_normal3
    with byso
    andr "Планируется мобилизация.{w=1} Я вчера тебе вкратце говорил."
    kt "Принято."
    stop music fadeout 3
    play sound sfx_dinner_horn_processed volume 0.4
    "На улице зазвучал горн."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "Замечательно. {w=1}Кстати да, у нас тут тоже трёхразовое питание.{w} За сигареты или деньги можно запросить абонемент на улучшенное питание."
    kt "Понял. На этом всё?"
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Да, можешь идти.{w} Работаешь в библиотеке, если не узнавал."
    kt "Понял, до встречи."
    scene bg int_admins with byso
    play sound sfx_close_door_1
    "Попрощался Константин и покинул кабинет капитана."
    th "Да уж...{w=1} Фантастика...{w} К сожалению, не в хорошем смысле слова."
    th "Может всё-таки стоило пойти в отряд ликвидации?"
    scene bg ext_admins_day with byso
    play ambience ambience_ext_road_day fadein 1
    play sound door_cl
    play music music_list["trapped_in_dreams"] fadein 3
    "Константин вышел из административного корпуса."
    th "Да нет, переживу."
    th "Не хочется ставить свою задницу на кону.{w=1} В разведке посижу, ничего страшного."
    th "Ну, приключение начинается."
    scene bg ext_dining_hall_away_day with fade
    "Со стороны столовая ничем не отличалась от лагерной.{w=1} Всё те же <<пионеры>> шли поесть, но только в меньшем количестве."
    th "Интересно, неужели у них такие проблемы с одеждой? {w=1}Все так и ходят в пионерских нарядах."
    th "Хотя чем я лучше... {w=1}Та же форма, только вместо шорт джинсы."
    th "Не, ну если подумать то реально, где тут найти другую одежду?"
    th "Кто с чем попал сюда, тот в том и ходит."
    th "Олег в тельняшке и джинсах, Ира в чёрной юбке и рубашке, Андрей в зелёной тройке."
    scene bg ext_dining_hall_near_day
    show image oleg_think at left
    show image liz_bukal at right
    with byso
    "У входа Константина встретила Женя и Олег."
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "О, ты вовремя.{w=1} Пошли с нами есть."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Ну чего, ты с нами остался?"
    stop music fadeout 2
    "Константин отрицательно помотал головой."
    kt "Нет, я перевёлся в разведку."
    play music cirk fadein 2
    hide image oleg_smile
    show image oleg_think at left
    hide image liz_normal
    show image liz_rage at right
    with byso
    "С лица Олега пропала улыбка, а Лиза сильно разозлилась."
    liz "А, значит так, да?!{w=1} Мы тебя тут привезли, а ты нам вот так ответил?!"
    kt "Вот это да, привезли, спасибо."
    hide image liz_rage
    show image liz_angry at right
    with byso
    "Константин поклонился Лизе в ноги."
    kt "Спасибо вам небесное, а теперь всё, дайте пожрать."
    hide image liz_angry
    show image liz_rage at right
    with byso
    liz "Ну и иди, хамло!"
    hide image oleg_think
    hide image liz_rage
    with byso
    "Константин прошёл мимо Олега, а Лиза ушла прочь."
    th "Не, ну я хотел разойтись без ссор...{w} Не вышло, бывает."
    scene bg int_dining_hall_day
    show mi normal pioneer
    with byso
    stop music fadeout 3
    play ambience ambience_dining_hall_empty fadein 1
    "Константин вошёл в столовую, где встретил Мику за стойкой."
    show mi grin pioneer with byso
    mip "О, новенький. Здорова."
    kt "Привет. Чего поесть можно?"
    play music deadrazy2 fadein 5
    "Константин пытается игнорировать имя <<Мику>> в своей голове, понимая что может произойти та же ситуация, как и на площади."
    show mi happy pioneer with byso
    mip "Ну смотри.{w=1} Базовая - кабачковая каша, продвинутая - яичница.{w} Напиток лимонный в любом случае."
    show mi smile pioneer with byso
    mip "Чего изволишь?"
    "Константин достал сигарету и положил на раздачу."
    kt "Давай продвинутую."
    "Девочка взяла сигарету и осмотрела."
    show mi laugh pioneer with byso
    mip "Сержант у нас богат, сигареты даже с кнопкой!{w} Отлично, уговор."
    "Девочка достала тарелку и положила на неё яичницу, после чего налила жёлтый напиток."
    show mi grin pioneer with byso
    mip "Приятного, товарищ."
    kt "Спасибо."
    hide mi with byso
    "Протянул Константин и взяв свою порцию пошёл за самый дальний столик."
    th "Чисто, пусто, почти никого нет...{w=1} Неужто никто не торопится на завтрак?"
    th "Ну тут вон, людей раз-два и обчёлся."
    th "Не то что бы это плохо, просто наблюдение."
    "Константин глянул на стоящего у раздачи Олега."
    th "Ну а они... Что они... Не знаю. Вроде серьёзная фракция, милитаризм, бла-бла-бла..."
    th "Но они всё равно как дети."
    "Константин начал неспеша есть свою порцию."
    play music mono fadein 3
    "Вдали он заметил стоящую у раздачи Иру."
    "Она же, взяв еду, направилась напрямую к Константину."
    show image irr_happy with byso
    irr "Я рада что ты сделал правильный выбор!{w=1} Приятного аппетита."
    kt "Спасибо, тебе тоже.{w} А как ты узнала?"
    hide image irr_happy
    show image irr_laugh
    with byso
    "В ответ Ира хихикнула."
    irr "Когда Лиза начала материться на всю симуляцию, я сначала подумала что это Олег опять хернёй страдает, но потом, услыхав среди отборного мата твоё имя, я всё поняла."
    "Константин чуть не подавился от смеха."
    kt "Сильно, ничего не сказать."
    kt "Кстати, чего мы сегодня делаем?"
    hide image irr_laugh
    show image irr_normal
    with byso
    irr "По мелочи. {w}Сидим с Энджи и читаем <<Цену грехов>>, сидим на горячей линии и между всем этим можем поигрывать в шахматы."
    "Не поняв ничего кроме шахмат, Константин повернул голову набок и вопросительно посмотрел на Иру."
    kt "А если попроще?"
    hide image irr_normal
    show image irr_grin
    with byso
    "Ира усмехнулась."
    irr "Точно, прости.{w} Въелся сленг в лексикон немного."
    irr "Ангелина - главная логистка, с которой мы чередуемся в задачах.{w} Обычно она на горячей линии, а мы на книгах, ну и наоборот."
    irr "У неё там ещё есть помощник...{w=1} Семён...{w=1} Полу-пустышка.{w} Но он просто в звании рядового бегает за пивом."
    hide image irr_grin
    show image irr_normal
    with byso
    irr "В целом как и должен."
    kt "Кстати, чего ты так на полу-пустышек обозлилась?"
    hide image irr_normal
    show image irr_sad
    with byso
    "Ира немного погрустнела."
    irr "Не могу сказать, прости."
    irr "Просто прими как данное."
    kt "Хорошо, расспрашивать не стану."
    hide image irr_sad
    show image irr_happy
    with byso
    "В ответ она улыбнулась."
    irr "Отлично.{w=1} Так вот.{w} Про книжку ты уже знаешь...{w} Горячая линия.{w=1} Это у нас такой способ коммуникации.{w} Ты же знаешь про радиотехнику?"
    kt "Ну кибернетики в клубе баловались помню."
    hide image irr_happy
    show image irr_laugh
    with byso
    "Услышав нелепицу Константина, Ира искренне рассмеялась."
    irr "Нет-нет.{w=1} Короче говоря, писание почитаешь поймёшь."
    hide image irr_laugh
    show image irr_normal
    with byso
    irr "Хоть про писание знаешь?"
    "С усмешкой спросила Ира.{w=1} Константин кивнул."
    kt "Да, про это мне Лиза говорила."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Ну хоть про что-то она тебе рассказала. Ну что, в разведпункт?"
    kt "Идём."
    scene bg ext_dining_hall_near_day
    show image oleg_shy at fright
    show image irr_normal
    with byso
    play ambience ambience_camp_center_day fadein 1
    "На выходе их встретил Олег, который взглядом провожал Иру и Константина."
    hide image oleg_shy
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Вот я на него смотрю и думаю..."
    kt "Ты про кого?"
    hide image irr_happy
    show image irr_angry
    with byso
    irr "Ну про Олега.{w} Он вроде не полу-пустышка, попал сюда на второй цикл, но божечки, какой же он тупой..."
    "Недовольно проговорила Ира.{w=1} Константин пожал плечами."
    kt "Ну в кой-то мере ты права. С другой стороны вопросов лишних не спрашивает."
    hide image irr_angry
    show image irr_laugh
    with byso
    irr "Хах, ты прав."
    "Ира почесала затылок."
    hide image irr_laugh
    show image irr_normal
    with byso
    irr "Я и забыла, тебе надо сходить к медсестре."
    kt "Точно.{w=1} Ну я тогда сейчас зайду, хорошо?"
    irr "Отлично, иди.{w} Как закончишь - иди к нам, мы будем ждать."
    kt "Договорились."
    hide image irr_normal
    show image irr_grin
    with byso
    irr "Только смотри как бы тебя Валери не съела, она достаточно странно относится к шатенам."
    "С усмешкой предупредила она."
    scene bg ext_square_day with byso
    stop music fadeout 3
    "На перепутье Константин и Ира разошлись."
    th "Валери?{w} Видимо местный медик."
    th "Нелестно конечно о ней отзывалась Лиза перед капитаном, но тут уже не могу знать точно."
    th "Ну типа Лиза даже Иру называла больной.{w} Просто за то что она не поддерживала её взгляды на ценность человеческой жизни."
    th "Главный закон СМИ из моего мира - приплети угнетённых, стариков, инвалидов и детей...{w=1} ну либо всё и сразу - так все начинают любой новости сочувствовать."
    th "В этом плане Ира умнее.{w=1} Да и вообще, как мне кажется, она носит маски.{w} Умная, обладает навыками холодного расчёта, местами аморальна, но при мне почти всегда весёлая и доброжелательная."
    th "Хотелось бы узнать, что у неё на уме."
    scene bg ext_aidpost_day with byso
    "Дойдя до медпункта, он собрался с силами."
    th "Ну, посмотрим..."
    play sound sfx_knock_door7_polite
    "Константин вежливо постучал."
    csp "О, гости...{w=1} Заходите!"
    scene bg int_aidpost_day_apple
    show image val_calm
    with byso
    play sound door_cl
    play ambience ambience_medstation_inside_day fadein 1
    play music lim fadein 3
    "Войдя, он встретил девушку лет 30ти с синими волосами, повязкой на глазе и оружием на спине."
    th "Йо-хо-хо и бутылка формалина."
    play sound sfx_bus_window_hit
    hide image val_calm
    show image val_smile2
    with byso
    "Откинув на кушетку книжку <<Половая психопатия>>, она глянула на Константина."
    csp "Новенький...{w=1} Привет...{w=1} Я Валери.{w} Чего же тебя ко мне занесло?"
    "Константин засмотрелся на повязку, которая была на глазу у Валери."
    kt "Здравствуй.{w=1} Кровь сдать хотел.{w} Точнее надо."
    hide image val_smile2
    show image val_smile
    with byso
    val "Надо-надо...{w=1} Нам не нужно вспышек генмода в симуляции."
    val "А тут подумаешь, уколоть пальчик..."
    hide image val_smile
    show image val_smile2
    with byso
    val "Кстати, у меня тут есть экспериментик, не хочешь поучаствовать?"
    "С едкой ухмылкой спросила Валери, в кой-то мере похотливо глядя на Константина."
    kt "Нет, откажусь, крови достаточно."
    hide image val_smile2
    show image val_sad
    with byso
    val "М-м-м..."
    play sound sfx_open_table
    "Недовольно промычала Валери и начала что-то искать в ящиках."
    val "Все оставляют даму одну в столь тяжёлый период...{w=1} А ведь мне просто хочется чу-уточку мужского внимания."
    "Протянула Валери, достав небольшое лезвие. В целом её речь была весьма неторопливой и со множеством пауз."
    hide image val_sad
    show image val_calm
    with byso
    val "Ну подумаешь человечка под катализаторами патогеном заразить...{w} Я ведь за всем прослежу... {w=1}Зато весело будет!"
    val "Давай лапку."
    "Константин сел на кушетку и протянул руку Валери."
    "Она сделала небольшой надрез и начала собирать кровь в пробирку."
    hide image val_calm
    show image val_normal
    with byso
    val "Чего это тебя к нам в сопротивление занесло?"
    kt "Познакомился с первым лейтенантом под прикрытием и теперь в разведку перевёлся."
    hide image val_normal
    show image val_smile2
    with byso
    val "А, Ира то...{w=1} Хорошая девочка.{w} Но, может ты останешься и со мной?{w=1} Поможешь мне чутка..."
    "Предложила Валери, глядя Константину прямо в душу."
    kt "Нет, я уже в разведке, меня всё устраивает."
    hide image val_smile2
    show image val_smile
    with byso
    val "Ну и ладно.{w=1} Отряд <<Дзеты>> просили привести мне человечка для экспериментов..."
    val "Буду ждать красивого и выносливого мальчика, шатена по мере возможности..."
    th "Насчёт красивого не уверен, но Рома подходит по описанию..."
    val "Ты бы неплохо подошёл...{w=1} Но нельзя..."
    hide image val_smile
    show image val_sad
    with byso
    val "Запретный плод сладок..."
    "Выдохнула Валери, закрыв подписанную пробирку с кровью и отставив на штатив."
    hide image val_sad
    show image val_smile2
    with byso
    play sound sfx_pat_shoulder_hard
    "Константин было хотел встать, но Валери схватила его за руку."
    val "Но ты же проследишь чтоб они доставили паренька именно мне?..."
    hide image val_smile2
    show image val_madsmile
    with byso
    "Проговорила она, слизнув кровь с пальца Константина."
    play sound sfx_punch_medium
    kt "Хорошо-хорошо, посмотрю по мере возможности."
    hide image val_madsmile
    show image val_smile
    with byso
    val "Хороший мальчик, жду."
    scene bg ext_aidpost_day with byso
    play ambience ambience_ext_road_day fadein 1
    play sound sfx_close_door_1
    stop music fadeout 3
    "Константин вышел из медпункта."
    th "Ну видимо бытующее мнение в кой-то мере оправдано..."
    th "Либидо поверх чего угодно...{w=1} Жуть..."
    "Достав сигарету, он закурил и направился к библиотеке."
    th "Чем-то напоминает мне торчалую, с которой я по объёбу лишился девственности."
    stop ambience
    play sound in_vosp
    play music sab
    scene bg semen_room
    show shum_white
    with flash
    "Вещества в теле Константина превышали практически любой допустимый ПДК. Он молча сидел и залипал в стену."
    chel "Ух, блять, хорошо пошла..."
    nap "Мне хоть оставь, нарколыга ебучий!"
    "Константин лёг на спину и засмотрелся на люстру."
    th "Красиво...{w=1} Новый год..."
    th "Новый год - новые места..."
    th "Что я тут делаю...{w=1} Зачем я тут делаю..."
    th "Сраная моя жизнь...{w=1} Хотя сейчас мне хорошо..."
    th "Хорошо...{w=1} Ведь в экзистенциальном смысле я победил?"
    th "Я же родился - значит победа."
    th "А может и поражение...{w=1} Сильно ли вообще победа отличается от поражения?"
    th "Поражение - плохо или поражение - хорошо...{w=1} Сложно сказать вне контекста..."
    th "Да и победа не так чиста...{w=1} Чиста как стекло на новеньком Nikon-е..."
    th "Я же занимался фотографией...{w=1} Куда это пропало..."
    th "Пропало вдохновение...{w=1} Вдохновение?{w=1} Кто же мне его давал?..."
    th "Настя...{w=1} Настя мертва..."
    th "Была ли это победа или поражение?..."
    chel "Всё, не наю как вы, н-н я прилягу..."
    "Парень распластался на полу и захрапел."
    nap "А ты чё такой грустный?"
    kt "Скучаю..."
    nap "По кому это?"
    kt "По Насте."
    "Девочка села на Константина и начала расстёгивать его ремень."
    nap "Так и быть, избавлю тебя от печали."
    play sound out_vosp
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 1
    hide shum_white
    scene bg ext_aidpost_day
    with flash
    "Константин передёрнуло от неприятности этого воспоминания."
    th "Нет, не она, но похожа...{w=1} Ту точно не Валери звали..."
    th "Мне кажется, лучше бы у меня никогда не было секса, чем так..."
    th "Может тогда бы я думал что это нечто чудесное...{w=1} То, ради чего Адам и Ева покинули чертоги райского острова."
    th "А на деле это просто первобытная мясная возня..."
    th "Говорили...{w=1} Пестики и тычинки нам даны не для того, чтобы утопать в своей похоти..."
    th "Дегенерация, да и только..."
    scene bg ext_square_day
    show image pas_normal2
    with byso
    play music sanari fadein 5
    "Выйдя на площадь он встретил Гордона."
    pas "Снова здорова, молодой. Чё как?"
    kt "Да нормально. В разведпункт иду, теперь там работаю."
    hide image pas_normal2
    show image pas_normal
    with byso
    "Гордон почесал затылок."
    pas "Эх, упустил ты свой шанс на приключения и оружие...{w=1} Кстати, я хоть и иду в агроцех, но могу тебе предложить личное оружие."
    kt "Агроцех? Оружие?"
    hide image pas_normal
    show image pas_smile
    with byso
    pas "А, ты не знаешь.{w=1} Короче выращиваем мы тут некоторые растительные продукты питания. Грядки, насаждения, прочая херня."
    pas "А что касается оружия...{w=1} Маузер С96 с модификацией.{w=1} По факту, это скорее похоже на люгер. {w=1} От оригинала отличается съёмностью магазина и улучшенным спуском."
    kt "И откуда таковой раздобыли?"
    hide image pas_smile
    show image pas_normal2
    with byso
    "Гордон выкинул бычок и снова закурил."
    pas "Запчасти валяются по старому корпусу, а магазин пришиваю от люгера."
    pas "К делу.{w=1} Да или нет?"
    kt "Возьму.{w=1} Сколько?"
    pas "Пошли в мастерскую, там разберёмся."
    hide image pas_normal2 with byso
    "Пробурчал Гордон, махнув рукой в сторону клубов."
    scene bg int_clubs_male_day
    show image pas_normal
    show dv sad pioneer at fleft
    show image oleg_think at left
    with byso
    play ambience ambience_clubs_inside_day fadein 1
    play sound sfx_open_door_clubs_2
    "Зайдя за Гордоном, Константин встретил Олега, который о чём-то переговаривался с Ритой."
    oleg "Да я тебе говорю, он как <<Эрида>>."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    "Заметив Константина, Олег замолчал и посмотрел на Риту, та пожала плечами."
    show dv guilty pioneer with byso
    rita "Ну, что сказать, может ты и прав."
    "Озвучила она, глядя на Гордона."
    hide image pas_normal
    show image pas_angry
    with byso
    pas "Чё пялишь?{w} Сколько раз говорил, хуйнёй не страдаем пока я отхожу!"
    pas "Или ты ещё хочешь поработать бесплатно?"
    show dv angry pioneer with byso
    hide dv with byso
    "Рита озлобилась и, взяв планшет с бумагами пошла к складу."
    pas "А ты чё уши развесил, молодой?"
    oleg "Иду-иду."
    hide image oleg_shy with byso
    "Обиженно пробубнил Олег и покинул помещение."
    hide image pas_angry
    show image pas_normal
    with byso
    pas "Как дети малые...{w=1} Так о чём мы...{w=1} Да, тебе в рублях или в сигаретах?"
    kt "В сигаретах, монет у меня нет."
    pas "Понял, одна пачка."
    play sound sfx_paper_bag
    "Константин достал пачку в которой оставалось 12 сигарет."
    kt "У меня больше нет с собой, если хочешь, то потом остальные занесу."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "С кнопкой?{w} Ладно, сделаю скидку. {w=1}Давай сюда."
    play sound sfx_pat_shoulder_hard
    "Гордон убрал пачку в карман и достал из под стола отполированный пистолет."
    pas "Вот ещё кобура."
    play sound sfx_punch_medium
    "Достав кожаный ремень с двумя магазинами, он протянул его Константину. {w=1}Константин убрал пистолет в кобуру и надел её на пояс."
    pas "Отлично.{w} Приятно иметь дело.{w=1} Пользуйся на здоровье."
    play sound ammo volume 0.4
    "Константин повесил кобуру на пояс и убрал туда пистолет."
    kt "Спасибо. Может у тебя есть ещё что-то полезное?"
    hide image pas_smile
    show image pas_normal
    with byso
    pas "Ну, поскольку ты в разведке, то предложить мне тебе нечего.{w=1} У меня в основном поставки на выезд."
    kt "Понял. Тогда давай, до встречи."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Покеда."
    scene bg ext_clubs_day with byso
    play ambience ambience_camp_center_day fadein 1
    play sound sfx_open_door_clubs
    stop music fadeout 3
    "Константин вышел из клуба и направился в свой домик за новой пачкой сигарет."
    th "Думаю в библиотеке меня уже заждались... {w=1}Ну, сейчас возьму курево и подойду."
    scene bg ext_library_day with fade
    "Спустя некоторое время, он дошёл до библиотеки."
    th "Ну, посмотрим с чем и с кем я буду работать..."
    scene bg int_library_day
    show image irr_normal at right
    show image ang_think at left
    with byso
    play ambience ambience_library_day fadein 1
    play sound sfx_open_door_2
    play music god fadein 3
    "Войдя без стука он встретил Иру и черноволосую девочку с синими глазами. Они сидели и играли в шахматы"
    hide image irr_normal
    show image irr_happy at right
    with byso
    irr "Ха, лёгок на помине.{w} Мы уже думали тебя из под ножа Валери вытаскивать."
    kt "Да, извиняюсь, я ещё к Гордону заскакивал.{w} Ты Ангелина?"
    hide image ang_think
    show image ang_normal at left
    with byso
    ang "Угу.{w=1} А ты, как я поняла, Константин.{w} Рада знакомству."
    hide image irr_happy
    show image irr_grin at right
    with byso
    "Бесчувственно сказала Ангелина, Ира ткнула её в бок локтем."
    irr "Она может показаться немного неживой, но это только кажется."
    hide image ang_normal
    show image ang_smile at left
    with byso
    ang "Да-да, очень смешно."
    kt "А почему на тебе такая одежда?"
    "Спросил Константин осматривая Ангелину."
    hide image ang_smile
    show image ang_normal at left
    with byso
    ang "А в чём суть вопроса?"
    kt "Да просто любопытно."
    "Почесав затылок спросил Константин, Ира усмехнулась."
    hide image irr_grin
    show image irr_normal at right
    with byso
    irr "Дресс код на работе дело такое."
    hide image ang_normal
    show image ang_smile at left
    with byso
    ang "Угу.{w} Так получилось.{w} Можешь не рассказывать как ты попал в инреальность, Ира уже все уши пробубнила."
    hide image irr_normal
    show image irr_shy at right
    with byso
    irr "Энджи!"
    hide image ang_smile
    show image ang_think at left
    with byso
    ang "Да-да.{w=1} Так, у нас партия не закончена."
    play sound sfx_open_table
    "Ангелина открыла ящик стола и протянула Константину белую папку с подписью <<#4>>. Ира по-тихому переставила одну из фигур на другое место"
    hide image ang_think
    show image ang_normal at left
    with byso
    ang "Вот, держи, ознакомься.{w} Потом мы скажем что тебе делать."
    kt "Понял.{w=1} Прочитаю."
    hide image irr_shy
    show image irr_normal at right
    with byso
    irr "Садись, место у нас есть."
    play sound dvizh
    "Ира поставила стул к одному из столов."
    hide image ang_normal
    show image ang_think at left
    with byso
    ang "Если по радио кто-то заговорит и мы не услышим - обозначь.{w=1} Мы пока доиграем."
    irr "А если возникнут вопросы по писанию, то спрашивай, ответим."
    kt "Ладно."
    hide image ang_think
    hide image irr_normal
    with byso
    stop music fadeout 3
    "Константин сел на стул, который ему предоставили.{w=1} Ангелина и Ира возобновили игру."
    ang "У тебя тут слон не стоял.{w} Ира, может хватит мухлевать, а?"
    irr "М-м, всё-таки заметила..."
    "Недовольно пробубнила Ира и поставила своего слона на должное место."
    play music deadrazy2 fadein 3
    window hide
    $ set_mode_nvl()
    "{font=inrealnost/font/NoRules.ttf}Если кто-то это читает значит это не было бесполезной работой."
    th "Это уже не было бесполезной работой, раз это сочинение всё сопротивление читает."
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
    kt "Слушай, а на кой хрен этот Миша делит всё это счастье на кучу страниц?"
    show image irr_laugh with byso
    irr "Ну вот нравится человеку бумагой сорить, чего докопался?"
    play sound sfx_paper_bag
    hide image irr_laugh with byso
    "Константин усмехнулся и перевернул страницу."
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
    window show
    kt "А у нас в сопротивлении есть товарищи со способностями?"
    show image ang_think at left
    show image irr_normal at right
    with byso
    ang "Нет."
    play sound chess
    "Ответила Ангелина и убрала со стола пешку Иры."
    irr "Почему, был один.{w=1} У него была вроде как способность к неограниченной выносливости."
    kt "И чего он?"
    hide image ang_think
    show image ang_normal at left
    with byso
    ang "Его отдали на эксперименты Валенайн."
    hide image irr_normal
    show image irr_happy at right
    with byso
    play sound chess
    "Ира усмехнулась и сделала ход."
    irr "Да уж, после её экспериментов никто не возвращается."
    kt "А почему Андрей тогда вообще назначил Валери медиком?"
    hide image irr_happy
    show image irr_normal at right
    with byso
    irr "У неё выдающиеся умения в медицине."
    kt "Как вы это узнали?"
    hide image ang_normal
    show image ang_think at left
    with byso
    ang "Она сшила по частям парня, которого разорвало в мастерской Гордона."
    play sound sfx_blow_out_candle
    "Ответила Ангелина и сделала рокировку."
    hide image irr_normal
    show image irr_sad at right
    with byso
    irr "Ну это один из случаев.{w=1} Валери на деле отличный врач, но в силу травматического опыта немного своеобразная."
    th "Своеобразная?{w=1} Некорректное наблюдение как по мне."
    hide image ang_think
    hide image irr_sad
    with byso
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
    kt "Слушайте, а почему тогда Валери проводит эксперименты с генмодом, если делать этого нельзя?"
    show image ang_normal at left
    show image irr_normal at right
    with byso
    ang "Она нашла хорошее средство, которое нейтрализует последствия терминальной стадии."
    hide image irr_normal
    show image irr_happy at right
    with byso
    irr "Как она мне говорила, это гопантеновая кислота."
    kt "Не буду спрашивать как она это проверила...{w=1} А ты с ней общаетесь?"
    play sound chess
    hide image irr_happy
    show image irr_shock at right
    with byso
    "Ангелина поставила Ире шах."
    hide image ang_normal
    show image ang_think at left
    with byso
    ang "Я ей не нравлюсь.{w=1} Ира периодически с ней за обедами сидела."
    kt "Понятно."
    hide image irr_shock
    hide image ang_think
    with byso
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
    window hide
    $ set_mode_adv()
    window show
    kt "У нас робокошка бушевать не будет?"
    show image ang_think at left
    show image irr_normal at right
    with byso
    ang "Сложный вопрос.{w=1} Гордон утверждает что нет."
    hide image irr_normal
    show image irr_laugh at right
    with byso
    irr "То же самое он говорил когда его установка взорвалась и взрывной волной порвала Семёна на части."
    play sound sfx_blow_out_candle
    "Ира разменяла ферзя Ангелины."
    hide image irr_laugh
    show image irr_happy at right
    with byso
    irr "По поводу техники лучше у него спрашивай."
    hide image irr_happy
    hide image ang_think
    with byso
    window hide
    $ set_mode_nvl()
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
    th "М-да, вот не в падлу же этому Михаилу было всё это исследовать..."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Лирика."
    "{font=inrealnost/font/NoRules.ttf}Немного лирики для самого себя.{w} Можете пропустить."
    "Константин выбрал один из написанных ниже элементов лирического отступления."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}ИСТЕКАЯ ДОБРОТОЙ"
    ""
    "{font=inrealnost/font/NoRules.ttf}Свет внутри меня -"
    "{font=inrealnost/font/NoRules.ttf}Больше, чем просто свет -"
    "{font=inrealnost/font/NoRules.ttf}Это новая заря,"
    "{font=inrealnost/font/NoRules.ttf}Золотого века человека..."
    "{font=inrealnost/font/NoRules.ttf}Но вокруг -"
    "{font=inrealnost/font/NoRules.ttf}Погасшие люди - изранены злобой."
    "{font=inrealnost/font/NoRules.ttf}Новый круг -"
    "{font=inrealnost/font/NoRules.ttf}Череда предательств, такой знакомый..."
    ""
    "{font=inrealnost/font/NoRules.ttf}Истекая добротой из открытых ран -"
    "{font=inrealnost/font/NoRules.ttf}Вспомни о том, что желал сам -"
    "{font=inrealnost/font/NoRules.ttf}Отдавать себя до последнего грамма души."
    "{font=inrealnost/font/NoRules.ttf}Истекая добротой от ножей в спине -"
    "{font=inrealnost/font/NoRules.ttf}Даруй последний свой огонь, как Прометей -"
    "{font=inrealnost/font/NoRules.ttf}И ни о чем, ни о чем не жалей..."
    "{font=inrealnost/font/NoRules.ttf}Ты сделал всё, что сумел."
    nvl clear
    "{font=inrealnost/font/NoRules.ttf}Пометки о прочтении."
    "{font=inrealnost/font/NoRules.ttf}Если ты прочёл это писание, то оставь пометку. {w}Это позволит вести счёт оригинальных симуляций, которые с текстом ознакомились."
    "Подписей на странице было 6.{w} Михаил, Андрей, Максим, Ирина, Елизавета, Семён."
    window hide
    $ set_mode_adv()
    window show
    stop music fadeout 3
    show image ang_think at left
    show image irr_sad at right
    with byso
    kt "Ир, а зачем ты поставила подпись?"
    hide image ang_think
    show image ang_smile at left
    with byso
    play sound chess volume 1.4
    "Ангелина усмехнулась и поставила Ире мат."
    irr "Да чего я?{w=1} Поржать."
    kt "Серьёзно?"
    ang "Да нет, ты ей дай ручку, она тебе и кредит на себя оформит."
    hide image irr_sad
    show image irr_angry at right
    with byso
    "Ире не понравились слова Ангелины."
    irr "Нашлась самая умная..."
    play music god fadein 2
    play sound sfx_radio_squelch_2
    vng "Приём, на связи отряд <<Козерог>>, вызываем центр."
    "Радио перебило их диалог."
    ang "Чего смотришь, ты проиграла, твоя очередь на линии сидеть."
    hide image ang_smile
    hide image irr_angry
    show image irr_normal
    with byso
    "Ира тяжело вздохнула и пересела к радиотехнике."
    play sound sfx_radio_squelch_1
    irr "Центр на связи.{w=1} Что у вас?{w=1} Приём."
    vng "У нас обнаружился схрон, который не был указан в сборочном листе, что делаем?{w=1} Приём."
    hide image irr_normal
    show image irr_angry
    with byso
    irr "Идиотский вопрос, не думаете?{w=1} Приём."
    "Едко подметила недовольная Ира."
    vng "Как раз проблема в схроне.{w=1} Это 32 ампулы генмода.{w=1} Приём."
    hide image irr_angry
    show image irr_shock
    with byso
    "Ира и Ангелина сильно удивились таким количествам мутагена."
    hide image irr_shock
    show image irr_angry
    with byso
    irr "Та-ак...{w=1} Назовите код симуляции. Приём."
    vng "19-34g."
    play sound sfx_paper_bag
    hide image irr_angry
    show image irr_normal
    with byso
    "Ира отлистала какой-то журнал и поставила карандашом пометку."
    irr "Отлично. 30 везите на базу, две разбейте на поверхности.{w=1} По возвращению заходите в разведку.{w=1} Как понял, приём?"
    vng "Команду принял.{w=1} Конец связи."
    play sound sfx_radio_squelch_2
    stop music fadeout 3
    hide image irr_normal
    show image irr_normal at right
    show image ang_surp at left
    with byso
    "Радио зашумело и замолкло, Ира вернулась за шахматный стол."
    kt "30 ампул?{w=1} Откуда и зачем нам столько?"
    hide image irr_normal
    show image irr_sad at right
    with byso
    irr "Да я вообще без понятия.{w=1} Потому мы на всякий случай и нейтрализуем ту симуляцию."
    hide image ang_surp
    show image ang_think at left
    with byso
    ang "Если тебе интересно зачем, то это к Валентайн.{w} На один её опыт уходит штук 15 как минимум."
    kt "Куда ей столько?"
    hide image ang_think
    show image ang_normal at left
    with byso
    ang "Ходит миф что она сама их пьёт, но это невозможно. {w}Кстати о ней, пойду её порадую."
    hide image ang_normal
    hide image irr_sad
    show image irr_normal
    with byso
    play sound sfx_close_door_1
    play music BlueJetta fadein 7
    "Ангелина направилась в медпункт.{w=1} Ира махнула рукой Константину."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Садись, сыграем."
    "Константин пожал плечами и сел к Ире."
    kt "Только сильно не души, я отвратительно играю."
    hide image irr_happy
    show image irr_grin
    with byso
    irr "Да ладно тебе, все мы тут любители."
    "С садистской улыбкой произнесла она и подмигнула."
    th "Сейчас меня раскатают."
    hide image irr_grin
    show image irr_normal
    with byso
    irr "Какой в твоём понимании должна быть идеальная любовь?"
    "Расставляя фигуры по доске спросила Ира."
    kt "Любовь? {w=1}Слишком малознакомое для меня понятие."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Неужели никогда никого не любил?"
    kt "Любил, почему...{w=1} Она покончила с собой."
    hide image irr_happy
    show image irr_sad
    with byso
    "Ира неловко почесала затылок."
    irr "Прости, не хотела говорить на наболевшие темы..."
    kt "Да нет, всё в порядке."
    hide image irr_sad
    show image irr_normal
    with byso
    irr "За белых или за чёрных?"
    kt "Давай за белых."
    "Ира развернула к Константину шахматную доску."
    play sound chess volume 0.6
    "Он сделал первый ход.{w=1} Пешка Е4."
    kt "Если пофантазировать, то могу сказать что она должна быть построена на взаимопонимании и доверии.{w=1} Без этого никуда."
    play sound chess volume 0.9
    "Ира походила конём на F6."
    hide image irr_normal
    show image irr_shy
    with byso
    irr "Как ты думаешь, любовь оправдывает убийство?{w=1} С моральной точки зрения разумеется."
    play sound chess volume 0.7
    "Константин защитил пешку конём С3."
    kt "Да, оправдывает, а к чему все эти вопросы?"
    play sound chess volume 1
    "В ответ она походила пешкой D5."
    hide image irr_shy
    show image irr_happy
    with byso
    irr "А насколько долго ты готов преследовать свои чувства?"
    play sound chess volume 0.7
    "Константин переместил второго коня на F3."
    kt "Сколько потребуется. Если это настоящая и беспрекословная любовь, то может даже вечность."
    play sound chess volume 0.9
    "Ира поставила пешку на Е6."
    hide image irr_happy
    show image irr_laugh
    with byso
    irr "Ну тогда я тебя поздравляю, твой стиль любви схож с Батори."
    play sound chess volume 0.5
    "Ненадолго задумавшись, он сделал ход пешка G3."
    kt "С чего бы то у тебя такие мысли?"
    play sound chess volume 0.8
    "Она разыграла слона на Е7."
    hide image irr_laugh
    show image irr_sad
    with byso
    irr "Она всё это время ищет какого-то парня и продолжает бушевать, поскольку никак его не нашла."
    play sound chess volume 0.6
    "Константин сыграл пешка B3."
    kt "Ну, значит её любовь самая настоящая, в кой-то мере я её не осуждаю...{w=1} Но средства у неё всё-таки немного дикие."
    play sound chess volume 0.9
    "Ира походила конём на С6."
    irr "Знаешь, я тоже в какой-то мере понимаю её действия.{w=1} Жизнь в одиночестве страшная штука."
    play sound chess volume 0.6
    play sound2 sfx_inhale
    "Тяжело вздохнув, Константин походил пешкой в А4."
    kt "Согласен.{w=1} Интересно, а по твоему, Генда одинок?"
    hide image irr_sad
    show image irr_normal
    with byso
    play sound sfx_blow_out_candle volume 0.5
    "Подумав несколько секунд, Ира хмыкнула и сделала рокировку."
    irr "Не знаю.{w=1} Возможно.{w=1} Нет фактов от слова совсем."
    irr "Ну, осмелюсь предположить что да. Есть же причина по которой он всех нас тут держит после смерти."
    play sound chess volume 0.9
    "Константин развил пешку на Н4."
    kt "Да, думаю что логично...{w=1} Я конечно понимаю, что такой вопрос странно задавать второму лейтенанту, но целиком ли ты поддерживаешь сопротивление?"
    play sound chess volume 0.9
    "Достаточно провокационно Ира походила пешкой в D5."
    irr "Вообще 50 на 50.{w=1} Сам знаешь моё отношение более чем к половине окружающих."
    play sound chess volume 1.1
    "Поставив пешку на D3, он приготовился к защите."
    kt "А вообще, какой была твоя симуляция?"
    hide image irr_normal
    show image irr_sad
    with byso
    play sound chess volume 0.6
    "Ира забрала пешку на Е4."
    irr "Своеобразной.{w=1} Я была не единственной в ней, всего нас было четверо.{w=1} Ангелина, я, Игорь и...{w=1} идолопоклонник Семён на третьем цикле..."
    play sound chess volume 0.8
    pause 1
    play sound sfx_blow_out_candle volume 0.5
    "Константин разменял пешку, после чего они сразу же разменялись ферзями."
    play sound chess volume 0.6
    "Ира походила пешкой на А6."
    irr "Игорь был весьма начитанным парнем, чем достаточно быстро привлёк внимание Ангелины.{w=1} Втроём мы планировали присоединиться к сопротивлению, но Семён имел свои планы."
    play sound chess volume 0.5
    "Константин походил пешкой на А5."
    irr "И в один вечер он просто отравил Игоря цианидом, после чего напал на меня с арматурой."
    play sound chess volume 0.9
    "Переместив ладью на D8, Ира поставила Константину шах."
    kt "Хм-м..."
    play sound chess volume 1.1
    "Отодвинув короля на Е1, Константин практически моментом получил коня на G4."
    irr "Он сломал мне плечевую кость, после чего его зарезала Ангелина.{w=1} Только в сопротивлении меня подлатала Валери."
    irr "В целом это всё, как-то так."
    play sound chess volume 0.6
    "Переместив слона на H3, Константин глянул в окно."
    kt "То-то я понимаю почему ты так ненавидишь полу-пустышек."
    play sound chess volume 0.9
    hide image irr_sad
    show image irr_normal
    with byso
    "Ира походила пешкой на H5."
    irr "Ага.{w=1} А в твоей симуляции чего?{w=1} Много путников?"
    play sound chess volume 0.4
    "Константин ответил конём на G5."
    kt "Да, Лиза говорила что даже слишком.{w=1} Меня смущало другое - один усопший, который хотел мне помочь."
    play sound chess volume 0.7
    "Почесав подбородок Ира сходила конём на D4."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Любопытно.{w=1} Как он выглядел?{w=1} Как помогал?"
    play sound chess volume 0.4
    "Пытаясь вспомнить, Константин походил ладьёй на А2."
    kt "Как Семён, только весь израненный, бледный как смерть и с чёрными волосами.{w} Помогал он мне рассказывая про инреальность по писанию, как я сегодня узнал."
    kt "Вроде как говорил что знает Мишу, автора."
    play sound chess volume 0.8
    "Ира походила конём на Е5."
    hide image irr_happy
    show image irr_normal
    with byso
    irr "Интересно...{w=1} Возможно этот призрак весьма могуч, раз он даже Мишу знает...{w=1} Странным кажется только то, что он сам не направил тебя на прочтение писания."
    play sound chess volume 0.6
    "Константин походил слоном на F4."
    kt "Олег и Лиза говорили что он опасен и распылили его из интегратора."
    play sound chess
    hide image irr_normal
    show image irr_grin
    with byso
    "Усмехнувшись, она ответила пешкой на F6, после чего Константин разменял слона на коня."
    play sound sfx_close_door_1
    hide image irr_grin
    show image ang_normal at right
    show image irr_normal at left
    with byso
    "В разведпункт вошла Ангелина."
    stop music fadeout 3
    ang "Играете?{w=1} Как успехи?"
    hide image irr_normal
    show image irr_happy at left
    with byso
    irr "Пока ровно, у меня ферзь, пешка и слон, у Кости ферзь, пешка и конь. Чего так долго?"
    hide image ang_normal
    show image ang_think at right
    with byso
    ang "Капитан вызывал.{w=1} Есть новости.{w} Нормальная и не очень."
    ang "Валентайн ждёт-не дождётся своего груза, это понятно, а отряд <<Дзетты>> должен был отправляться в 22-25a, откуда и приехали."
    kt "И чего?"
    hide image ang_think
    show image ang_angry at right
    with byso
    ang "А то, что Лизу и Олега замещают.{w=1} За неоднократное оспаривание приказов она перенаправлена в агроцех и разжалована до сержанта."
    play music god fadein 3
    ang "И я вам сочувствую, вам придётся ехать вместо них."
    hide image irr_happy
    show image irr_angry at left
    with byso
    irr "Чего?!"
    "Ире сильно не понравились эти известия."
    hide image ang_angry
    show image ang_normal at right
    with byso
    ang "Того.{w=1} Вы после обеда едете на вылазку.{w} По словам Андрея, однократно."
    irr "Какого хрена эти инвалиды не едут?"
    ang "Я уже сказала."
    "В ответ она устало прикрыла лицо рукой."
    kt "А кто вместо нас будет?"
    hide image ang_normal
    show image ang_think at right
    with byso
    ang "Гордон и я.{w=1} Звучит как старый анекдот."
    hide image irr_angry
    show image irr_sad at left
    with byso
    irr "Н-да...{w=1} Походу дела совсем плохо..."
    kt "Ты о чём?"
    play sound sfx_open_drapes
    play sound2 sfx_dinner_horn_processed
    "Ира встала со стула и осмотрев шахматную доску, она смела все фигуры в кучу. Заиграл горн."
    hide image irr_sad
    show image irr_happy at left
    with byso
    irr "Сейчас расскажу.{w} Энджи, пойдёшь есть?"
    hide image ang_think
    show image ang_normal at right
    with byso
    ang "Нет, я пас.{w=1} Зайдите потом к капитану, он вас ждёт."
    stop music fadeout 2
    kt "Ладно, Ир, идём."
    scene bg ext_library_day
    show image irr_normal
    with byso
    play ambience ambience_ext_road_day fadein 1
    play sound door_cl
    play music warm_evening fadein 3
    "Константин и Ира вышли из библиотеки."
    kt "Так и что?"
    hide image irr_normal
    show image irr_angry
    with byso
    irr "Да я про то что Лиза опять выделываться, мол не хочет руки марать и прочие отмазки."
    irr "И как капитан её терпит..."
    kt "Да уж, понимаю, каково содержать неэффективных подчинённых."
    hide image irr_angry
    show image irr_happy
    with byso
    irr "Ну и ладно...{w=1} Давно я не была на разъездах."
    kt "А ты была?"
    hide image irr_happy
    show image irr_normal
    with byso
    irr "Угу.{w=1} В отряде поставок.{w=1} Я умею водить автобус, потому, видимо, отправили именно меня с тобой."
    kt "Ангелину почему не взяли?"
    irr "Не знаю чем капитан руководствовался, когда такое указание давал. {w=1}Думаю хотел оставить кого-то с техникой и книгами."
    play sound sfx_paper_bag
    "Предположила Ира и достала пачку сигарет <<Космос>>."
    scene bg ext_houses_day
    show image irr_happy
    with byso
    irr "Будешь?"
    window hide
    menu:
        "Предложить свои.":
            $ renpy.block_rollback()
            $ irrscore += 1;
            kt "Может мои?"
            "Спросил Константин, достав новую пачку честерфилда."
            hide image irr_happy
            show image irr_grin
            with byso
            irr "Давай твои, почему нет."
            play sound light_inh
            "Он поделился с Ирой, после чего они оба закурили."
            irr "Давно не курила сигарет с кнопкой..."
            kt "А какие в нашем мире предпочитала?"
            hide image irr_grin
            show image irr_laugh
            with byso
            "В ответ Ира рассмеялась."
            irr "Я не курила."
        "Взять сигареты Иры.":
            $ renpy.block_rollback()
            hide image irr_happy
            show image irr_normal
            with byso
            kt "Спасибо."
            play sound light_inh
            "Константин достал зажигалку и закурил."
            irr "М-м, не курила с самого утра."
            kt "А какие в нашем мире предпочитала?"
            hide image irr_normal
            show image irr_laugh
            with byso
            "В ответ Ира рассмеялась."
            irr "Я не курила."
    scene bg ext_admins_day
    show image irr_normal at right
    show image rkis_normal
    with fade
    "Константин и Ира дошли до административного корпуса."
    rkis "Проходите, капитан ожидает вас в своём кабинете."
    stop music fadeout 3
    scene bg int_admins
    show image irr_normal
    with byso
    play ambience ambience_int_cabin_day volume 0.7 fadein 1
    play sound sfx_open_door_clubs
    "Пропустив Константина и Иру, робокошка закрыла дверь."
    play sound sfx_knock_door3_dull
    "Константин постучал."
    andr "Войдите."
    scene bg int_admins_room2
    show image irr_normal at left
    show image andr_normal at right
    with byso
    play sound sfx_close_door_1
    play music Gallow fadein 3
    "В кабинете их ожидал Андрей, который писал что-то на бумажке."
    hide image irr_normal
    show image irr_happy at left
    with byso
    irr "Вызывали?"
    hide image andr_normal
    show image andr_normal3 at right
    with byso
    andr "Да, секунду, присаживайтесь пока что."
    play sound sfx_bed_squeak1
    pause 0.5
    play sound sfx_open_table
    hide image andr_normal3
    show image andr_normal2 at right
    hide image irr_happy
    show image irr_normal at left
    with byso
    "Константин с Ирой сели на диван.{w=1} Поставив подпись, капитан выключил лампу, убрал бумаги в стол и встал."
    hide image andr_normal2
    show image andr_normal at right
    with byso
    andr "Итак. {w=1}Начнём издалека.{w} Ирина, ваш план оказался действенным и приводится в действие."
    kt "О чём речь?"
    hide image irr_normal
    show image irr_happy at left
    with byso
    irr "Мы начинаем боевые действия."
    hide image andr_normal
    show image andr_normal3 at right
    with byso
    andr "Так точно.{w=1} Отряды спасения переквалифицированы в карательные и они в данный момент активно нарушают стабильность симуляций."
    kt "Для чего?"
    hide image andr_normal3
    show image andr_normal at right
    with byso
    "Андрей поправил пиджак и посмотрел на часы."
    andr "Мы хотим открыть доступ в административные симуляции, где лишим Генду контроля."
    hide image andr_normal
    show image andr_normal2 at right
    with byso
    andr "Бывший первый лейтенант вам говорила о том что таковые есть.{w} Уж простите, но вам придётся ехать вместо неё."
    hide image andr_normal2
    show image andr_normal at right
    with byso
    andr "Кстати да, Константин, вы повышены до четвёртого лейтенанта.{w=1} Ирина, вы до первого."
    window hide
    menu:
        "Так быстро?":
            $ renpy.block_rollback()
            $ irrscore += 1;
            andr "Так сложились обстоятельства.{w=1} Считай так тебе повезло."
        "А что с Олегом?":
            $ renpy.block_rollback()
            andr "Как и <<Дзета>>, понижен."
    kt "Ладно."
    andr "Значит.{w=1} Ваша главная задача - привезти путника для эксперимента Валенайн, обыскать медпункт и уничтожить 22-25a."
    hide image irr_happy
    show image irr_shock at left
    with byso
    irr "А зачем нам уничтожать 22-25а?"
    hide image andr_normal
    show image andr_normal3 at right
    with byso
    andr "Судя по схемам, предоставленным Ангелиной вчера, она является важным узлом для симуляций 22й серии."
    irr "Не путаете ли в её с 22-25d случаем?"
    hide image andr_normal3
    show image andr_normal2 at right
    with byso
    andr "22-25d уже не существует.{w=1} Батори."
    andr "Значит, Ира, ты помнишь как управлять автобусом?"
    hide image irr_shock
    show image irr_happy at left
    with byso
    irr "Да, помню."
    hide image andr_normal2
    show image andr_normal at right
    with byso
    andr "Отлично.{w=1} Тогда отправляйтесь.{w=1} Гордон выдаст вам припасы и сухпаёк, а так-же одну ампулу генмода."
    kt "А для чего нам генмод?"
    hide image andr_normal
    show image andr_normal2 at right
    with byso
    "Андрей поправил очки и глянул в окно."
    andr "Вы разобьёте её в центре лагеря.{w=1} Самый быстрый и безучастный способ очистки."
    kt "Понятно.{w=1} У меня больше нет вопросов."
    hide image irr_happy
    show image irr_normal at left
    with byso
    irr "У меня тоже."
    hide image andr_normal2
    show image andr_normal at right
    with byso
    andr "Отлично. Удачи в поле."
    scene bg ext_admins_day
    show image irr_normal
    with byso
    play ambience ambience_camp_center_day fadein 1
    play sound door_cl
    "Константин и Ира вышли из административного корпуса."
    kt "Да уж, а я пошёл в разведку как раз чтоб не кататься лишний раз по симуляциям..."
    hide image irr_normal
    show image irr_laugh
    with byso
    irr "Вот блин, а я думала из-за моей очаровательной улыбки!"
    "С едкой усмешкой сказала Ира, Константин рассмеялся."
    hide image irr_laugh
    show image irr_grin
    with byso
    irr "Да ладно тебе, развлечёмся хоть немного."
    kt "Ну, развлечение ли это или нет сказать сложно."
    scene bg ext_clubs_day 
    show image irr_normal at right
    show image pas_smile at left
    with byso
    "Дойдя до клубов они встретили Гордона."
    pas "Оу, <<Эрида>>, молодая, моё почтение, давно не виделись."
    hide image irr_normal
    show image irr_happy at right
    with byso
    irr "Привет-привет. Ты починил мп-шку?"
    pas "Ещё давно, только мы с тобой не пересекались, пойдём."
    scene bg int_clubs_male_day
    show image pas_smile at left
    show image irr_happy at right
    with byso
    play ambience ambience_clubs_inside_day fadein 1
    play sound sfx_punch_medium
    "Войдя в клубы, Гордон начал доставать из под стола кучу разной техники и после этого достал немецкий пистолет-пулемёт MP-40."
    pas "Вот и он, красавец, на нём и мухи не ебались, а если и ебались, то только в тапочках."
    "Проговорил Гордон и отдал оружие Ире."
    hide image irr_happy
    show image irr_laugh at right
    with byso
    irr "Спасибо тебе огромное. Спуск отрегулировал?"
    pas "Обижаешь, молодая!{w} Патроны хавает как Наташа мои деньги."
    natasha "Эй, я вообще-то всё слышу!"
    "Прокричала недовольная Наташа со склада."
    hide image pas_smile
    show image pas_angry at left
    hide image irr_laugh
    show image irr_happy at right
    with byso
    pas "Хорошо что слышишь!{w} Ебало на ноль!{w=1} Хоть сейчас мозги не компостируй!"
    pas "Короче да, вот вам ещё по перехватчику."
    "Гордон дал Константину и Ире по пульту."
    pas "Так, вот ещё сумка с сухпайком и генмодом, оставьте потом в автобусе.{w=1} Только содержимое не перепутайте!{w=1} Мне ещё нужны покупатели!"
    kt "Обязательно перепутаем!"
    hide image pas_angry
    show image pas_smile at left
    with byso
    "Подшутил Константин, все усмехнулись."
    hide image irr_happy
    show image irr_laugh at right
    with byso
    pas "А, точно, Ир, тебе медсестричка письмо передавала. {w}Почитай как сядешь грит."
    play sound sfx_paper_bag
    hide image irr_laugh
    show image irr_normal at right
    with byso
    "Ира взяла у Гордона письмо и убрала в нагрудный карман."
    irr "Поняла.{w=1} Спасибо.{w} Слушай, патронов 9х19 у тебя лишних не завалялось?"
    hide image pas_smile
    show image pas_normal at left
    with byso
    "В ответ он лишь пожал плечами."
    pas "Сама знаешь, щас чертова куча автобусов уехала.{w} 25 у тебя в магазине, а в симуляции заберёшь ещё 40."
    hide image irr_normal
    show image irr_happy at right
    with byso
    irr "Поняла.{w=1} Ну что, <<Корсар>>, едем?"
    kt "Поехали."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Бон вояж."
    scene bg ext_camp_entrance_day
    show image irr_normal at right
    show image ang_smile at left
    with fade
    play ambience ambience_camp_center_day fadein 1
    "У выхода из лагеря их ждала Ангелина."
    ang "Удачи, она вам пригодится.{w=1} Там в 22-25а путников много, мало-ли какие неадекватные."
    hide image irr_normal
    show image irr_happy at right
    with byso
    irr "Спасибо."
    kt "Да, тебе тоже удачи."
    hide image ang_smile
    show image ang_normal at left
    with byso
    ang "Мне то зачем? {w=1}Я тут сижу-сижу...{w=1} А, вот вам в дорогу."
    "Монотонно проговорила Ангелина и протянула им багряную книжку."
    ang "Заодно посмотрите чего нового."
    kt "Спасибо."
    hide image irr_happy
    show image irr_grin at right
    with byso
    irr "Ладно, мы стартуем, не скучай!"
    hide image ang_normal
    show image ang_smile at left
    with byso
    ang "Надеюсь ещё увидеть вас живыми."
    scene bg int_avtobus
    show image irr_normal
    with byso
    "Зайдя в автобус, Константин отложил сумку, которую ему дал Гордон на заднее сиденье, а Ира села на водительское место и начала вбивать настройки в приборной панели."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Итак...{w=1} 22-25а...{w=1} 4 часа...{w=1} Едем."
    play sound2 bus_sms
    pause 0.5
    play sound sfx_ikarus_open_doors
    play ambience bus_inside volume 0.2 fadein 1
    "Приборная панель пропищала, а дверь закрылась и автобус начал своё движение."
    hide image irr_happy
    show image irr_grin
    with byso
    "Ира села на сиденье и махнула рукой Константину."
    irr "Садись."
    kt "Сажусь."
    "С улыбкой повторил Константин и сел на соседнее пассажирское место."
    stop music fadeout 3
    kt "Слушай, а откуда ты достала тут пистолет-пулемёт?"
    hide image irr_grin
    show image irr_normal
    with byso
    irr "А, этот то?{w=1} Достался от идолопоклонника.{w} Тут уже к нему вопрос, откуда он у него появился и почему он им так и не воспользовался."
    play sound sfx_home_phone_take
    "Отложив оружие на пол, она закинула ноги на торпеду."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "М-м, кайф...{w=1} Я радио включу, ты не против?"
    scene bg int_avtobus2
    show image irr_happy
    with byso
    kt "Радио?{w=1} В инреальности?"
    hide image irr_happy
    show image irr_normal
    with byso
    "Ира потянулась и хмыкнула."
    irr "Как не странно, но да, есть такое."
    play sound sfx_click_1
    "Она дотянулась до приёмника и нажала кнопку."
    play sound sfx_radio_tune
    play music summerdays fadein 5
    irr "Автопоиском не найдёшь, но передаётся на частоте 92.1 повсеместно."
    kt "И откуда играет?"
    hide image irr_normal
    show image irr_grin
    with byso
    irr "А чёрт его знает, но музыка круглосуточно."
    "Ответила она, прикрыв глаза."
    kt "Слушай, я так и не спросил у Гордона что это за перехватчик."
    "Проговорил Константин, вертя в руках странный пульт."
    hide image irr_grin
    show image irr_normal
    with byso
    irr "А, это-то?{w=1} Телепортатор.{w} Он тебя перекинет обратно в 15-27z, то есть к сопротивлению."
    kt "Всегда недолюбливал телепортацию."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Чего так?"
    "С усмешкой спросила Ира.{w=1} Константин потёр глаза."
    kt "Тебя же по сути расщепляет на молекулы и собирает снова, только уже в другом месте.{w} Это по сути своей означает неминуемую смерть, так ещё и просто ради поржать."
    hide image irr_happy
    show image irr_normal
    with byso
    irr "Он работает как и этот автобус, только 1-3 раза вместо 1000-5000."
    kt "Ну тогда ладно..."
    hide image irr_normal with byso
    "Ира встала с места и пошла на заднюю площадку."
    irr "Как насчёт обеда?"
    kt "Я не против, давай."
    show image irr_happy with byso
    "Она принесла две банки консервов, вилки и стеклянную бутылку лимонного напитка."
    irr "Держи."
    kt "Спасибо."
    "Ира и Константин открыли банки.{w} У обоих была картошка с мясом."
    hide image irr_happy
    show image irr_grin
    with byso
    irr "Приятного аппетита!"
    kt "Спасибо, тебе тоже."
    "С приятной улыбкой ответил Константин и начал есть."
    hide image irr_grin
    show image irr_normal
    with byso
    irr "Кстати, ты умеешь готовить?"
    "Константин усмехнулся."
    kt "Когда ты работаешь на работе где тебе недоплачивают чуть ли не половину зарплаты - хочешь не хочешь, а научишься."
    hide image irr_normal
    show image irr_sad
    with byso
    irr "М-да...{w=1} А я практически нет."
    kt "Ничего, если мы отсюда выберемся живыми, то может обучу паре рецептов."
    hide image irr_sad
    show image irr_shy
    with byso
    irr "Да ладно, правда?"
    "С счастливой улыбкой спросила его Ира.{w=1} Константин развёл руками."
    kt "Не, в этом ничего такого. Это просто."
    hide image irr_shy
    show image irr_sad
    with byso
    "Ира пожала плечами."
    irr "Не скажи.{w=1} Мне проще будет из повареной соли атомарный натрий добыть, чем суп сварить."
    kt "Хах, это как?"
    hide image irr_sad
    show image irr_happy
    with byso
    "В ответ она усмехнулась и отпила немного лимонного напитка."
    irr "Греешь до плавления и элекролизуешь."
    kt "Кхе, нет уж, я лучше борщ сварю."
    "Выдохнул Константин, вылавливая из банки кусочки мяса."
    hide image irr_happy
    show image irr_normal
    with byso
    irr "Как ты думаешь, все ли законы нашего мира работают в инреальности?"
    "Константин махнул вилкой."
    kt "Закон на запрет самосуда - нет.{w=1} Мораторий на смертельную казнь - нет.{w=1} Запрет на применение биологического оружия - тоже нет."
    hide image irr_normal
    show image irr_laugh
    with byso
    "Рассмеявшись, Ира чуть не упала с кресла."
    irr "Хах, я говорю тебе про законы физики."
    kt "Ух, нашла кого спросить.{w=1} Я бухгалтер а не физик-теоретик."
    hide image irr_laugh
    show image irr_happy
    with byso
    irr "А если чисто гипотетически?"
    kt "Думаю что да.{w=1} Мы же всё ещё не улетели от отсутствия гравитации?{w=1} Метаболизм работает?{w=1} Значит да."
    hide image irr_happy
    show image irr_normal
    with byso
    irr "А может они работают иначе?"
    kt "Ну а нам-то в таком случае какое дело?"
    play sound sfx_blow_out_candle
    hide image irr_normal
    show image irr_angry
    with byso
    "Отставив банку на пол, Ира киношно скрестила руки."
    irr "Душнила."
    kt "Ну-ну."
    "Проговорил Константин, выкинув банку в открытую форточку."
    hide image irr_angry
    show image irr_normal
    with byso
    "Ира глянула вдаль."
    irr "Знаешь, я периодически задумывалась..."
    kt "М-м-м?"
    "Промычал в ответ Константин, разминая шею."
    hide image irr_normal
    show image irr_sad
    with byso
    irr "Батори не настолько плоха насколько её представляет сопротивление."
    kt "Хах, посмотрел бы на тебя перед тем как она изуродует твоё милое личико."
    hide image irr_sad
    show image irr_shy
    with byso
    "С усмешкой проговорил Константин, Ира немного покраснела."
    irr "За комплимент спасибо, но я сейчас не про это."
    irr "Как ты и говорил.{w=1} Ей на самом деле движет любовь.{w=1} Не жажда крови, как это говорит кто-либо ещё."
    irr "Я это поняла совсем недавно, когда встретила в инреальности одного парня...{w} Он мне очень понравился."
    irr "Возможно это просто кратковременная влюблённость, но это мне уже не свойственно."
    irr "Я никогда в своей жизни не любила по настоящему...{w} Да-да, тётка 26 и девственница, жуть какая, правда?"
    irr "Но я понимаю Батори.{w=1} Мы об этом говорили ранее с Энджи и Валери, они мне говорили про то же, но я этого просто не понимала."
    irr "Теперь я это поняла и прочувствовала."
    "Романтично сказала Ира и поправила волосы."
    irr "Просто чтоб это понять надо это чувствовать."
    window hide
    menu:
        "Не люблю романтику, давай не об этом.":
            $ renpy.block_rollback()
            $ irrscore -= 1;
            hide image irr_shy
            show image irr_sad
            with byso
            irr "Ну ладно..."
            "Уныло проговорила Ира, закинув руки за голову."
            irr "Знаешь, вообще во всём сопротивлении хуже всего Валери."
        "И что это за парень?":
            $ renpy.block_rollback()
            "Ира усмехнулась."
            irr "А вот это секрет."
            "С усмешкой проговорила Ира, закинув руки за голову."
            hide image irr_shy
            show image irr_sad
            with byso
            irr "На самом деле меня больше всего печалит судьба Валери."
        "Сама знаешь, я всё это не совсем понимаю.":
            $ renpy.block_rollback()
            $ irrscore += 1;
            hide image irr_shy
            show image irr_happy
            with byso
            irr "Во всяком случае я думаю, что хоть когда-нибудь тебе получится пережить это вновь после твоего опыта."
            "Мечтательно сказала Ира, закинув руки за голову."
            kt "Не знаю, может и да... Сложно сказать."
            hide image irr_happy
            show image irr_sad
            with byso
            irr "Жаль что только Валери не сможет."
    kt "А что с ней?"
    "Ира повернула голову и посмотрела в глаза Константина."
    irr "Ты думаешь, почему она такая странная?{w} У неё самая жуткая история, которую я слышала за всё время."
    kt "Расскажешь?"
    irr "Могу."
    "Сразу было видно, что история ни о чём хорошем не повествует."
    irr "Раньше она была талантливой и послушной, училась на патологоанатома."
    irr "Её все унижали.{w=1} Родители, бабушка с дедом, вообще все."
    irr "Её били, высмеивали и откровенно издевались..."
    irr "Потом она полюбила парня, которого встретила на межвузовском конкурсе.{w} Этот парень напоил её бутиратами и воспользовался."
    irr "После этого её жизнь превратилась в сущий ад.{w} Она употребляла наркотики и спустя несколько лет убила и расчленила парня, которого она встретила на конкурсе."
    irr "Она попала в инреальность.{w} Одна проблема.{w=1} Как раз с тем парнем."
    irr "И теперь Валери в его поисках что-б полноценно отомстить."
    play sound light_inh
    "Константин достал сигареты и закурил."
    kt "Да уж...{w=1} Подожди, она же давала тебе письмо."
    hide image irr_sad
    show image irr_normal
    with byso
    "Ира оживилась."
    irr "Точно! Гордон же передавал."
    play sound sfx_paper_bag
    "Открыв конверт она достала жёлтую бумажку, на которой было что-то написано красными чернилами."
    hide image irr_normal
    show image irr_sad
    with byso
    irr "Привет, Ирочка, это Валери."
    irr "Помнишь сказку о девочке со шрамом?"
    kt "Какая сказка?"
    hide image irr_sad
    show image irr_normal
    with byso
    "Ира отвлеклась от письма и посмотрела на Константина."
    irr "Свою историю она преподносила как сказку."
    hide image irr_normal
    show image irr_sad
    with byso
    "Константин сделал глубокую затяжку, а Ира продолжила читать."
    irr "Так вот, тут такая история. Константин частично напомнил мне того самого мальчика..."
    irr "А так-же я узнала что у Константина есть братик..."
    irr "Так раз вы едете в его симуляцию...{w=1} Если это Грачёв Роман Михайлович, то везите ко мне именно его."
    irr "Передавай привет Константину.{w=1} Люблю.{w=1} Твоя Лера."
    "Константин впал в глубокий ступор."
    hide image irr_sad
    show image irr_happy
    with byso
    irr "У тебя есть брат?"
    kt "Ага..{w=1}. Двоюродный...{w=1} А знаешь в чём главный прикол?..."
    hide image irr_happy
    show image irr_shock
    with byso
    irr "Ты же не хочешь сказать что..."
    "Константин кивнул и выкинул сигарету в окно."
    kt "Именно он...{w=1} Грачёв Рома..."
    "Иру шокировали это новости."
    irr "Жесть какая..."
    kt "Не то слово!{w=1} Я всегда знал что он мразь...{w=1} Но такое!"
    play sound light_inh
    hide image irr_shock
    show image irr_sad
    with byso
    "В ответ она поникла, встала с места и закурила."
    irr "Выбор за тобой..."
    kt "Мы забираем этого уёбка..."
    hide image irr_sad
    show image irr_shy
    with byso
    "Ира улыбнулась и погладила Константина по голове."
    irr "Я знала что ты это скажешь."
    stop music fadeout 3
    play sound bus_sms
    "С романтичной ноткой прошептала Ира.{w=1} Панель начала сигналить, а радио выключилось."
    hide image irr_shy
    show image irr_sad
    with byso
    irr "Что такое?"
    hide image irr_sad
    show image irr_shock
    with byso
    "Подойдя к панели, Ира сильно удивилась."
    irr "В 22-25а по местному времени 22:03.{w=1} Мы через одну выходим."
    kt "Так быстро?"
    play music Gallow fadein 3
    "Константин встал с места."
    hide image irr_shock
    show image irr_normal
    with byso
    irr "Мы походу сильно срезали."
    kt "Как это?"
    play sound ammo volume 0.5
    "Ира взяла своё оружие и проверила боезапас."
    irr "Дыры, созданные ошибками симуляций позволяют миновать некоторые симуляции.{w=1} Нам так повезло, что мы несколько раз через них проскочили."
    "Надев на ремень свой пистолет-пулемёт, Ира перевесила его через плечо."
    irr "Вряд-ли нам второй раз так повезёт...{w=1} В первый раз я так быстро проехала на другой конец инреальности."
    "Подметила Ира и взялась за поручень.{w=1} Автобус начал трястись и снижать скорость."
    kt "Генмод беру?"
    irr "Нам ещё медпункт обчистить.{w=1} Возьми мешок в бардачке."
    play sound sfx_put_sugar_cart
    "Константин достал из бардачка мешок из под сахара."
    kt "Серьёзно?"
    hide image irr_normal
    show image irr_laugh
    with byso
    "Ира посмотрела на Константина и рассмеялась."
    irr "Ну простите, за багаж автобуса я не в ответе."
    play ambience ambience_camp_center_night fadein 1
    play sound sfx_ikarus_open_doors
    play sound2 sfx_bus_stop volume 0.7
    "Автобус остановился и двери открылись."
    kt "Погнали."
    scene bg ext_camp_entrance_night
    show image irr_normal
    with byso
    play sound sfx_wind_gust
    "На выходе их встретил прохладный вечерний ветерок."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Так, план такой.{w=1} Сейчас мы за схроном в старом корпусе, затем за медикаментами, а потом за Ромой."
    kt "Побежали."
    scene bg int_old_building_night
    show image irr_normal
    with fade
    play sound sfx_wood_floor_squeak
    "Добежав в старый корпус, Ира оторвала нижнюю ступеньку и достала зелёный ящик, про который упоминалось в писании."
    irr "Я в автобус. {w=1}Встретимся в медпункте."
    kt "Принял."
    scene bg ext_path2_night with byso
    "Константин и Ира разбежались."
    stop music fadeout 3
    th "Рома..."
    th "У него же была девушка!"
    th "И мало того девушка!{w=1} Он ещё и издевался над другими!"
    th "Я то думал что он со мной так плохо обошёлся, а он..."
    th "Бросил любившую его девчонку, так ещё и издевался над другими."
    th "Ну ничего-ничего...{w=1} Отомстим за всех..."
    scene bg int_aidpost_lamp with byso
    play ambience ambience_medstation_inside_night fadein 1
    play sound door_break
    "Константин добежал до медпункта и выбил дверь с ноги."
    "Вываливая всё содержимое маленьких ящичков в мешок, Константин буквально сметал всё на своём пути."
    "Полностью заполнив мешок, Константин взял его и побежал обратно в автобус."
    scene bg ext_clubs_night
    show image irr_shock
    with fade
    play ambience ambience_camp_center_night fadein 1
    play music "<from 0 to 96>inrealnost/Music/Music/greedy_charm.mp3" fadein 3
    "У клубов стояла удивлённая Ира с MP-40 в руках."
    hide image irr_shock
    show image irr_angry
    with byso
    irr "Твой братец время не терял."
    play sound sfx_put_sugar_cart
    "Злобно проговорила Ира.{w=1} Константин поставил мешок на землю и прислушался."
    "Из здания доносились периодичные шлепки.{w=1} Константин достаточно быстро сообразил что происходит."
    th "Блять, ты сука серьёзно?!"
    scene bg int_clubs_male_night with byso
    play ambience ambience_int_cabin_night fadein 1
    "Константин тихо открыл дверь и вошёл, пока Ира ждала на стрёме снаружи.{w=1} У окна стоял Рома и трахал Ольгу, лежащую на столе."
    "Достав пистолет, Константин начал подбираться к Роме."
    rm "Да-а, получай, пизда неёбаная."
    kt "Единственный кто тут получит, так это ты!!!"
    play sound sfx_lena_hits_alisa
    "Прокричал Константин и со всей силы огрел Рому по голове прикладом пистолета."
    "Рома упал без сознания.{w=1} Константин взглянул на бывшую вожатую."
    "Сахарова лежала на столе с пеной у рта и не подавала никаких признаков жизни. Константин взял её руку и пытался нащупать пульс."
    th "Пульса...{w=1} Нет?!"
    kt "Ёб твою мать блять!{w=1} Ты что, труп ебал?!" with vpunch
    show image irr_angry with byso
    play sound vomit
    "Константина стошнило. На крики в клуб прибежала Ира."
    hide image irr_angry
    show image irr_shock
    with byso
    irr "Что произо...{w=1} Блять!!!{w=1} Что тут происходит?!"
    kt "Блять,{w=1} больной,{w=1} нахуй,{w=1} ублюдок!" with vpunch
    kt "Что с тобой не так, сука,{w=1} объебос конченый!"
    irr "{image=inrealnost/Pic/Spec/german.png}Scheiße! \nБлять!" with vpunch
    hide image irr_shock with byso
    "Выкрикнула Ира, закрыв глаза и отвернувшись."
    "Отдышавшись, Константин накрыл лицо вожатой её панамкой, Ира взяла пачку строительных хомутов."
    "Константин потащил Рому в автобус."
    scene bg int_avtobus2
    show image irr_shock
    with fade
    play ambience ambience_camp_center_night fadein 1
    "Дотащив Рому до автобуса, Константин усадил его на двойное кресло, а Ира, занеся мешок с награбленным, достала хомуты."
    kt "Фиксируй этого больного ублюдка!"
    irr "Сейчас!"
    "Ира дала ему половину из хомутов, которые лежали в пачке."
    "Константин фиксировал руки Ромы к спинкам сидений, а Ира фиксировала его ноги к ножкам сидения."
    "Израсходовав буквально всю пачку хомутов, они отошли от Ромы."
    scene bg ext_bus_night
    show image irr_sad
    with byso
    "Достав ампулу генмода, Константин пошёл на выход, а Ира за ним."
    scene bg ext_square_night
    show image irr_angry
    with byso
    "Выйдя на площадь, они смотрели прямо на медного Генду."
    irr "И как, ты, идиот, такое допускаешь в своих мирах?!"
    kt "Не то слово..."
    kt "Блять...{w=1} Рома...{w=1} Невозможно просто!"
    kt "Трахать трупы!{w=1} Как до этого можно докатиться?!"
    hide image irr_angry
    show image irr_mad
    with byso
    "Ира выхватила у Константина ампулу."
    irr "Умрите!" with vpunch
    "Прокричала она и метнула ампулу в статую Генды."
    play sound glass_break
    pause 0.5
    play sound2 genmod
    "Ампула разбилась и раздалось шипение, словно при жарке на масле."
    scene bg ext_clubs_night
    show image irr_sad
    with byso
    "Развернувшись, они со всех ног побежали в автобус."
    scene bg int_avtobus2
    show image irr_sad
    with byso
    play sound korobka_peredach
    play sound2 sfx_ikarus_open_doors
    play ambience bus_inside volume 0.2 fadein 1
    "Забежав, Константин махнул рукой.{w=1} Ира быстро вбила настройки и дверь закрылась."
    "Автобус начал свой путь."
    scene bg black with dissolve
    stop music fadeout 3
    stop ambience fadeout 3
    window hide dissolve
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
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt5b.png" with byso
    show image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt_end7.png" with dissolve5
    pause 10
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt1.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt2.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt3a.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt4.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt5b.png"
    hide image "inrealnost/Pic/Bg/bgcg/d5/D5_BGCG_txt_end7.png"
    hide load
    scene bg black
    with dissolve
    stop music fadeout 2
    pause 1
    jump d5_withsopr_irr