label d2_withre_otkus:
    scene bg black with dissolve
    window hide
    python:
        bgcg = random.randint(1,2)
    if bgcg == 2:
        scene bg bgcg1
        show load
        with byso
        pause 10
        $ bgcg -= 2
        stop music fadeout 2
        window show
        jump gfhu9sdnofsdpghnsfvpiupsvifnd
    else:
        scene bg bgcg4
        show load
        with byso
        pause 10
        $ bgcg -= 1
        window show
        jump gfhu9sdnofsdpghnsfvpiupsvifnd
label gfhu9sdnofsdpghnsfvpiupsvifnd:
    stop music fadeout 2
    $ save_name = ('Инреальность.\nДень второй.')
    $ persistent.sprite_time = 'day'
    $ day_time ()
    play music music_list["sunny_day"] fadein 1
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_mt_day
    show unblink
    "Константин проснулся из-за адской боли в области пояса."
    th "Ух-х, больно вообще-то!"
    th "Незабываемое чувство смерти.{w=1} Интересно, как создатель спроектировал таких монстров."
    show mt smile pioneer with byso
    "Вожатая, что сидела за столом заметила пробуждение Константина и улыбнулась."
    mt "Доброе утро.{w=1} Вовремя ты проснулся.{w=1} Только тебя хотела будить."
    kt "Доброе{w=1}. Сколько времени?"
    mt "7:30. Сходи к умывальникам, это налево от нашего домика, потом возвращайся, у нас сбор."
    kt "Хорошо.{w=1} Тогда я пойду."
    "Константин начал неторопясь одеваться."
    th "М-да, Рена была права. Спать тут неприятно..."
    jump joevcejvcspjigfvs
label d2_withre:
    scene bg black with dissolve
    window hide
    python:
        bgcg = random.randint(1,2)
    if bgcg == 2:
        scene bg bgcg1
        show load
        with byso
        pause 10
        $ bgcg -= 2
        stop music fadeout 2
        window show
        jump gfgiowhenujnofvidofvnsdiobnvsdf
    else:
        scene bg bgcg4
        show load
        with byso
        pause 10
        $ bgcg -= 1
        window show
        jump gfgiowhenujnofvidofvnsdiobnvsdf
label gfgiowhenujnofvidofvnsdiobnvsdf:
    stop music fadeout 2
    $ save_name = ('Инреальность.\nДень второй.')
    $ persistent.sprite_time = 'day'
    $ day_time ()
    play music music_list["sunny_day"] fadein 1
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_mt_day
    show unblink
    "Константин проснулся из-за адской головной боли."
    th "Ух-х, такое чувство, словно вчера бухал как проклятый..."
    th "Интересно, а безболезненно покинуть кошмар можно?{w=1} Я не готов каждое утро в таком состоянии вставать."
    show mt smile pioneer with byso
    "Вожатая, что сидела за столом заметила пробуждение Константина и улыбнулась."
    mt "Доброе утро.{w=1} Вовремя ты проснулся. {w=1}Только тебя хотела будить."
    kt "Доброе.{w=1} Сколько времени?"
    show mt grin pioneer with byso
    mt "7:30. {w=1}Сходи к умывальникам, это налево от нашего домика, потом возвращайся, у нас сбор."
    kt "Хорошо. Тогда я пойду."
    "Константин начал неторопясь одеваться."
    th "М-да, Рена была права.{w=1} Спать тут неприятно..."
    jump joevcejvcspjigfvs
label d2_withre_shot:
    scene bg black with dissolve
    window hide
    python:
        bgcg = random.randint(1,2)
    if bgcg == 2:
        scene bg bgcg1
        show load
        with byso
        pause 10
        $ bgcg -= 2
        window show
        jump gfdshgsdhbjmyhngbfvdctyikik
    else:
        scene bg bgcg4
        show load
        with byso
        pause 10
        $ bgcg -= 1
        window show
        jump gfdshgsdhbjmyhngbfvdctyikik
label gfdshgsdhbjmyhngbfvdctyikik:
    $ persistent.sprite_time = 'day'
    $ day_time ()
    $ save_name = ('Инреальность.\nДень второй.')
    play music music_list["sunny_day"] fadein 1
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_mt_day
    show unblink
    "Константин проснулся из-за адской головной боли."
    th "Ух-х, незабываемое чувство пули в голове..."
    th "Интересно, кто там себя таким снайпером почувствовал..."
    show mt smile pioneer with byso
    "Вожатая, что сидела за столом заметила пробуждение Константина и улыбнулась."
    mt "Доброе утро.{w=1} Вовремя ты проснулся.{w=1} Только тебя хотела будить."
    kt "Доброе. Сколько времени?"
    show mt grin pioneer with byso
    mt "7:30.{w=1} Сходи к умывальникам, это налево от нашего домика, потом возвращайся, у нас сбор."
    kt "Хорошо.{w=1} Тогда я пойду."
    "Константин начал неторопясь одеваться."
    th "М-да, Рена была права.{w=1} Спать тут неприятно..."
    jump joevcejvcspjigfvs
label d2_withre_topor:
    scene bg black with dissolve
    window hide
    python:
        bgcg = random.randint(1,2)
    if bgcg == 2:
        scene bg bgcg1
        show load
        with byso
        pause 10
        $ bgcg -= 2
        window show
        jump jhfgjoikjfgomnbncvorjge
    else:
        scene bg bgcg4
        show load
        with byso
        pause 10
        $ bgcg -= 1
        window show
        jump jhfgjoikjfgomnbncvorjge
label jhfgjoikjfgomnbncvorjge:
    $ save_name = ('Инреальность.\nДень второй.')
    $ persistent.sprite_time = 'day'
    $ day_time ()
    play music music_list["sunny_day"] fadein 1
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_mt_day
    show unblink
    "Константин проснулся из-за адской головной боли."
    th "Ух-х, больно вообще-то!"
    th "Шалава позорная!{w=1} Я б хотел с тобой то же самое сделать ещё на работе!"
    show mt smile pioneer with byso
    "Вожатая, что сидела за столом заметила пробуждение Константина и улыбнулась."
    mt "Доброе утро.{w=1} Вовремя ты проснулся.{w=1} Только тебя хотела будить."
    kt "Доброе...{w=1} Сколько времени?"
    show mt grin pioneer with byso
    mt "7:30.{w=1} Сходи к умывальникам, это налево от нашего домика, потом возвращайся, у нас сбор."
    kt "Хорошо. Тогда я пойду."
    "Константин начал неторопясь одеваться."
    th "М-да, Рена была права. Спать тут неприятно..."
    jump joevcejvcspjigfvs
label joevcejvcspjigfvs:
    hide mt
    scene bg ext_house_of_mt_day
    with byso
    stop music fadeout 3
    play sound door_cl
    play ambience ambience_forest_day fadein 1
    "Одевшись, Константин поспешил покинуть домик."
    "Выйдя на улицу, он вдохнул свежий утренний воздух."
    th "Приятно однако, та самая деревенская утренняя влага..."
    th "Да только сигаретный дым ничем не хуже."
    "Константин оглянулся."
    "Найдя укромное место, он направился в сторону леса."
    scene bg ext_polyana_day with byso
    play sound light_inh
    "Выйдя на поляну, Константин закурил."
    th "Сигаретка с утра самое оно. Именно благодаря ей я хоть немного чувствую себя человеком."
    "Присев на пенёк, он засмотрелся на ближайшее дерево."
    th "Помню, когда с дедушкой в лес ходил, любил присесть на пенёк и помечтать о лучшей взрослой жизни."
    th "Как это было прекрасно присесть после долгого похода и посмотреть на дикую природу."
    th "Да вот только повзрослев понимаешь, что несмотря на всю красоту и жестокость природы, самими жестокими будут люди."
    th "Единственный вид, что убивает друг друга, словно в массовом побоище. Дерутся за власть, которая им нужна ради социального статуса и мешают друг друга с говном."
    th "Как же мерзко понимать, что они заставляют хороших людей истекать добротой. Доброта истекает, словно кровь, что остановить нельзя."
    th "А когда крови больше нет, человек умирает. Так и с добротой, человек лишается этого качества и становится чёрствым и злобным как я."
    th "Хотя по какой причине я вообще думаю о прошлой жизни?"
    th "В своём мире я жестокий террорист, который с особым садизмом перебил бывших коллег, трёх сотрудников оперативных служб и умер на старой остановке."
    th "Я думаю меня даже не похоронили, не достоин, а родители снова ахнули, какой их сын вырос."
    play sound in_vosp
    stop ambience
    play music sab
    scene bg semen_room
    show shum_white
    with flash
    moth "Тебе надо хоть иногда меня слушать! Сколько раз я тебе говорила бросить курить?"
    "Отец лишь молчал, ожидая возможность где-то поддакнуть"
    kt "С какой целью?"
    moth "Как ты не поймёшь! Это вредно! Мы вот с отцом бросили - и ты брось."
    "Константин прекрасно понимал что идея бросить курить не устраивала его отца, но ему пришлось прогнуться из-за давления матери."
    moth "Да и вообще, ты всё ещё думаешь о своей этой Насте. Рома вон уже нашёл настоящую девушку, поступил и работает, получает повышенную стипендию, а ты лишь у нас на шее сидишь!"
    kt "Ну да, я зато на траве не сижу и мне не нужно много денег для существования."
    fath "Тебе уже 19, а у тебя даже нет девушки..."
    moth "Вот именно, вместо того чтобы свой LD курить, девушку бы привёл!"
    kt "А знаете что, а давайте! Я собираю вещи и уезжаю. Сегодня же."
    scene bg ext_polyana_day
    hide shum_white
    with flash
    stop music
    play sound out_vosp
    play ambience ambience_forest_day fadein 3
    th "Ладно, долой философию, пойду умоюсь."
    "Константин выкинул бычок и направился умыться."
    scene bg ext_washstand_day with byso
    play sound sfx_open_water_sink
    pause 1
    stop sound
    play sound_loop sfx_water_sink_stream
    "Выйдя к умывальникам, он открыл кран и потрогал воду."
    th "Холодная, словно лёд.{w=1} Прямо как я люблю."
    "Константин умылся холодной водой и протёр шею, чтобы быстрее зарядиться энергией."
    stop sound_loop
    play sound sfx_close_water_sink
    play music music_list["lightness"] fadein 3
    "Намывшсь вдоволь, Константин понял, что кто-то тоже направляется к умывальникам."
    show sl normal sport with byso
    play sound sfx_slavya_run
    "Это была Славя. Она была одета в спортивный костюм, что весь промок от пота."
    show sl smile sport with byso
    "Заметив Константина, она улыбнулась."
    sl "Доброе утречко!{w=1} Как спалось?"
    th "Спал как убитый."
    kt "Доброе.{w=1} Нормально."
    show sl smile2 sport with byso
    sl "Ты же сейчас к Ольге Дмитриевне?"
    kt "Да, а что?"
    sl "Понятно.{w=1} Скажи что могу задержаться."
    kt "Хорошо.{w=1} Скажу."
    show sl smile sport with byso
    sl "Спасибо большое!{w=1} Скоро буду."
    hide sl with byso
    th "Можешь и не быть."
    "Подумал Константин и направился обратно в домик."
    show mt normal pioneer panama
    scene bg ext_house_of_mt_day
    with byso
    "У домика он увидел вожатую, что лежала на гамаке и читала книгу."
    kt "Я вернулся."
    show mt surprise pioneer panama with byso
    "Вожатая лениво посмотрела на Константина, но потом, осознав своё положение резко вскочила."
    show mt smile pioneer panama with byso
    mt "Прекрасно.{w} А Славя где?"
    th "Нигде."
    kt "Просила передать, что немного задержится, так как она только закончила зарядку."
    "Предположил Константин."
    show mt surprise pioneer panama with byso
    mt "Странно, она обычно никогда не опаздывает."
    show mt smile pioneer panama with byso
    mt "Ну ладно.{w} Мне доложили, что у нас сегодня приедет новая пионерка."
    th "Рена..."
    mt "Раз Славя опаздывает, её встретишь ты."
    kt "Хорошо."
    th "Прекрасно."
    show mt grin pioneer panama with byso
    mt "Так-же тебя переселяют в другой домик.{w} Как раз с новой пионеркой."
    "Вожатая усмехнулась."
    mt "Скажи спасибо, я постаралась."
    th "Да кому ты чешешь, я то всё знаю!"
    kt "Спасибо. Какой сегодня план на день?"
    show mt smile pioneer panama with byso
    mt "Твоя задача провести новенькой экскурсию по клубам и может даже её позвать в наш клуб."
    mt "За это тебе будет награда в виде дополнительных обеденных блюд."
    th "Ништяк. А жизнь то налаживается."
    kt "Понял.{w=1} Во сколько она должна приехать?"
    mt "Она приедет примерно в 11-12 часов.{w=1} До этого твоя задача осмотреть клубы, вдруг кто бездельничает.{w} Их мы пристроим на вечернюю работу."
    show sl smile2 pioneer at right with byso
    "Пришла Славя."
    sl "Извините, Ольга Дмитриевна.{w} Задержалась на зарядке немного."
    show mt grin pioneer panama with byso
    mt "Ничего. Славя, ты сегодня помогаешь кибернетикам готовить площадь к вечеру.{w} После чего можешь отдыхать."
    show sl smile pioneer at right with byso
    sl "Хорошо, я тогда пойду?"
    mt "Иди. Я с Костей пока что поговорю."
    hide sl with byso
    "Славя улыбнулась и пошла прочь."
    mt "Итак, осилишь сегодняшнюю работу?"
    kt "Да, осилю."
    show mt smile pioneer panama with byso
    "Вожатая улыбнулась"
    mt "Ещё раз. Встретить пионерку, осмотреть клубы, потом свободен."
    mt "Зайди к кибернетикам и спроси ключи от лагеря."
    th "О, ключи.{w=1} Это уже лучше."
    kt "Понял-принял.{w} Пойду?"
    mt "Да, иди."
    hide mt with byso
    "Константин направился в лагерь, а вожатая пошла в домик."
    th "Неплохо я устроился. Теперь только плети и пряника не хватает."
    scene bg ext_square_day with fade
    play sound sfx_dinner_horn_processed
    "Константин вышел на площадь.{w} Заиграл горн, зазывающий в столовую."
    "Он достал телефон и посмотрел время."
    th "Ровно 8.{w=1} Надо запомнить."
    stop music fadeout 2
    play music music_list["heather"] fadein 2
    show mz bukal glasses pioneer with byso
    "По дороге он встретил Женю."
    mz "Ну привет.{w} Ты теперь ещё и в клубе надзирателей?"
    kt "Надзиратели?"
    show mz normal glasses pioneer with byso
    mz "Наставничество."
    kt "Да, а что?"
    show mz bukal glasses pioneer with byso
    mz "Да так, просто.{w} Нам бы помощь для подготовки к вечеру."
    kt "Что нужно?"
    show mz smile glasses pioneer with byso
    "Жене понравился деловой подход Константина."
    mz "Нужен человек для помощи.{w=1} Есть кто на примете?"
    show dv sad pioneer2 far at right with byso
    "Константин заметил недалеко Алису."
    kt "Есть.{w=1} Алиса!"
    show dv shocked pioneer2 far at right
    show mz normal glasses pioneer
    with byso
    "Крикнул Константин. Алиса вздрогнула."
    show dv sad pioneer2 at right with byso
    dv "Чего?..."
    kt "Ты теперь помогаешь литературному."
    show dv angry pioneer2 at right with byso
    dv "Ага, чёрта с два."
    show dv shocked pioneer2 close at right with byso
    "Константин подошёл у Алисе."
    kt "Дай шепну на ушко."
    "Константин перешёл на шёпот."
    kt "Ты же прекрасно понимаешь, что ты не на том месте, чтоб командовать."
    kt "Или ты хочешь стать посмешищем для всего лагеря благодаря вчерашней ситуации?"
    show dv sad pioneer2 at right with byso
    "Алиса напряглась."
    dv "Хорошо."
    kt "Ну вот. Алиса в твоём распоряжении."
    show mz laugh glasses pioneer with byso
    mz "Прекрасно. {w}Хоть кто-то полезный из вас есть."
    hide dv
    hide mz
    with byso
    "Своеобразно отблагодарила она Константин и пошла к Алисе. Он же поплёл дальше."
    scene bg ext_dining_hall_near_day
    show mi normal pioneer
    with byso
    "Дойдя до столовой он заметил его звала Мику."
    mi "Привет.{w}.. Можешь помочь?"
    kt "Что?"
    show mi smile pioneer with byso
    mi "Мне нужна помощь в музклубе.{w} Поможешь?"
    th "У меня теперь каждый будет помощь просить?"
    kt "Я нет.{w} Но человека подберу."
    show image tl_normal at right with byso
    "Константин заметил проходившего мимо Толика."
    kt "Эй ты!{w} Иди сюда."
    hide image tl_normal
    hide mi
    show mi normal pioneer at right
    show image tl_angry at left
    with byso
    "Толик нехотя послушался."
    kt "Помогаешь сегодня в музклубе."
    tl "Ещё чего!"
    show mi upset pioneer at right with byso
    kt "Могу в лоб прописать дабы тонизировать."
    tl "Ладно!"
    kt "Мило.{w} Вот Мику, разбирайтесь."
    mi "Спасибо."
    hide image tl_angry
    hide mi
    with byso
    stop music fadeout 2
    "Промямлила Мику с натянутой улыбкой и повела Толика в клуб."
    scene bg int_dining_hall_people_day with byso
    play ambience ambience_dining_hall_full
    "Константин зашёл в столовую и встал на раздачу."
    th "Только сегодня думал про борьбу за бесполезную власть, а теперь сам таким стал.{w} Какой я лицемер."
    "С усмешкой подумал он, гладя себя по затылку."
    "На завтрак давали рисовую кашу со стаканом какао."
    th "Ужас смертный!{w} Лучше поголодаю до обеда!"
    "Как Константин встал на раздачу, повариха стала в него вглядываться."
    kt "У меня что-то на лице?"
    pov "Нет.{w=1} Ты из клуба наставничества?"
    kt "Да, а что?"
    pov "Тебе другая еда."
    "Повариха открыла другую тарелку, в которой лежала аппетитная запеканка."
    th "Во-о, другой разговор."
    "Положив два кусочка, повариха обильно полила их вареньем и протянула Константину."
    kt "Спасибо большое!"
    pov "Не за что."
    show us dontlike pioneer with byso
    "Ульяна, что стояла позади роняла слюни."
    us "А можно мне так?"
    pov "Тебе можно рисовую кашу."
    show us angry pioneer with byso
    us "Фе!"
    hide us with byso
    "Константин усмехнулся и направился за свой столик."
    "Сев, Константин отпил какао."
    th "Интересно, неужто партия настолько стимулирует людей приобщаться к управлению?"
    th "Я не думал что быть так называемым надзирателем имеет столько полезных ништяков..."
    th "Моей прошлой работы походу это тоже касалось."
    play music music_list["everyday_theme"] fadein 3
    show mt smile pioneer with byso
    "Как только Константин преступил к запеканке, к нему подошла Ольга Дмитриевна."
    mt "Приятного аппетита."
    kt "Спасибо.{w=1} Вы что-то хотели?"
    show mt grin pioneer with byso
    mt "Хотела тебя похвалить.{w} За первые 15 минут ты помог двум клубам и даже пристроил Алису к труду и обороне.{w=1} Молодец!"
    "С улыбкой проговорила вожатая."
    kt "Спасибо, ничего такого."
    show mt smile pioneer with byso
    mt "Хорошо, так держать!"
    hide mt with byso
    th "Приятно иметь хоть какую-то власть.{w} Чувствую себя работорговцем, что хлыстом гоняет рабов."
    stop music fadeout 2
    "Константин продолжил свою трапезу."
    stop ambience
    play sound in_vosp
    play music the_date_of_death
    scene bg int_school
    show shum_white
    with flash
    mks "Эй ты, Брусков!"
    ks "Да?"
    di "Ты какого хрена нам фальшивое дз подсунул?"
    mks "Мы из-за тебя по паре получили!"
    ks "Я говорил, надо самим дз было делать, вы не послушали."
    di "Ах ты!"
    "Дима замахнулся на Константина, но тот парировал и ударил оппоненту в живот."
    "От боли Дима упал на пол и скрючился."
    mks "Ты чё творишь?"
    "В атаку пошёл Никита, но после неудачной вертушки был пойман за ногу."
    ks "Полежи!"
    "Костя резко потянул за ногу, в результате чего второй упал на спину и потерял сознание."
    abc "Ты чего делаешь?!"
    "Учитель, заметив двоих на полу, принялся возвращать своих учеников в чувства."
    abc "У тебя всё нормально с головой?!{w=1} Родителей в школу!"
    ks "Это была самооборона."
    di "Он врёт! {w=1}Он нас просто так избил!"
    "Учитель злобно посмотрел на Костю."
    abc "А ну к директору, живо!!!"
    ks "И вы за них."
    "Пробурчал Костя и направился к кабинету директора."
    stop music
    play sound out_vosp
    hide shum_white
    scene bg int_dining_hall_people_day
    play music music_list["she_is_kind"]
    show sl smile pioneer
    with flash
    "Константин доел и направился сдавать тарелки.{w=1} Его встретила Славя."
    sl "Кость, поможешь мне перетащить тяжести на площадь.{w=1} Всего две колонки."
    window hide
    menu:
        "Согласиться":
            $ renpy.block_rollback()
            kt "Идём."
            "Славя обрадовалась."
            sl "Пошли."
            play ambience ambience_forest_day
            scene bg ext_dining_hall_near_day
            show el normal pioneer at right
            show sh normal pioneer at left
            show sl normal pioneer
            with byso
            "Выйдя из столовой, они зашли за неё."
            "Около двери стояли Электроник и Шурик."
            el "Доброе утро..."
            kt "Взаимно."
            "Шурик молча заводил свои часы."
            play sound sfx_keys_rattle volume 0.3
            "Славя была озадачена подбором ключа."
            show sl smile2 pioneer with byso
            sl "А где Рома?"
            show sh serious pioneer at left with byso
            sh "Следит, чтоб Ульянка к клубу не подходила.{w} Сама её знаешь."
            show sl tender pioneer with byso
            sl "Она же ещё маленькая.{w=1} Не вините её."
            hide sl with byso
            play sound sfx_unlock_medpunkt_door
            "Оправдала Славя Ульяну и открыла склад."
            hide sh
            hide el
            scene bg sklad
            with byso
            "Склад выглядел довольно новым.{w} Кибернетики взяли нужные вещи и пошли на площадь."
            "Было две телеги с колонками."
            show sl normal pioneer with byso
            sl "Берём."
            "Славя повезла одну из двух телег. Константин последовал её примеру и пошёл за ней."
            scene bg ext_square_day
            show sl smile pioneer
            show el normal pioneer far at left
            show sh normal pioneer far at right
            with byso
            "На площади Шурик уже во всю развлекался с приборами, а Электроник был занят проводами."
            sl "Ставь сюда."
            "Константин снял с телеги колонку и поставил её на указанном месте."
            sl "Хорошо, спасибо за помощь, дальше мы сами."
            kt "Ладно."
            stop music fadeout 2
            "Отстрелялся Константин и пошёл за ключами к кибернетикам."
        "Отказаться":
            $ renpy.block_rollback()
            $ rerp += 1;
            kt "Нет, я не могу.{w}.. Мне надо пойти посмотреть, как в музклубе дела у Мику."
            th "Чё за бред?"
            sl "Ну тогда ладно, сами довозим."
            play ambience ambience_forest_day
            scene bg ext_dining_hall_near_day with byso
            "Константин со Славей вышли из столовой и разошлись.{w} Константин понял что колонки они берут прямо у его укромной курилки."
            th "Ладно, пойду тогда в лесу покурю."
            scene bg ext_polyana_day with byso
            "Константин направился на лесную полянку, что была не так далеко от столовой."
            play sound light_inh
            th "Снова поляна, снова сигарета, снова пенёк."
            "Без каких-либо мыслей Константин сидел и взглядом гипнотизировал дерево напротив."
            "То было стройное кривое дерево, стоящее на невысокой зеленой горке. Ствол его был покрыт желтыми шишками и походил на голову какого-то старика, чья седина поблекла от времени. Из-за этого дерево казалось безобразным, но теплым и мягким."
            "В какой-то момент со стороны могло показаться, что и дерево гипнотизирует Константина в ответ..."
            th "Да уж...{w=1} Надо было мне в том мире продать квартирку и купить участок на природе."
            "Константин затушил сигарету и направился обратно в лагерь."
            scene bg ext_square_day
            show el normal pioneer far at left
            show sh normal pioneer far at right
            with byso
            "Кибернетики уже во всю ковырялись в технике, а Славя уже ушла по своим делам."
            th "А, точно, ключи от лагеря надо забрать."
            stop music fadeout 2
            "Подумал Константин и пошёл к кибернетикам."
    hide sl
    hide sh
    hide el
    play music music_list["faceless"] fadein 3
    scene bg ext_clubs_day
    show image rm_sm
    with byso
    "Константин дошёл до клубов.{w} На входе сторожил Рома."
    rm "Утро доброе, Костян.{w} Как спалось?"
    kt "Не очень. Дай ключи забрать."
    rm "Да подожди ты с ключами.{w} Давай поговорим."
    th "О чём нам с тобой разговаривать?"
    rm "Как там в надзирателях? {w}Нравится?"
    kt "Вполне себе. За вступление не жалею."
    hide image rm_sm
    show image rm_th2
    with byso
    rm "А че не к нам?"
    kt "Предпочитаю управление подчинению."
    rm "Ну не знаю, по тебе не скажешь, держи ключи."
    play sound sfx_keys_rattle volume 0.6
    "Рома протянул ключи Константину."
    hide image rm_th2
    show image rm_sm
    with byso
    rm "Но при одном условии."
    "При попытке Константина забрать ключи, Рома убрал руку."
    rm "Слышал, у нас сегодня новенькая. {w}Это мне."
    play sound2 sfx_punch_medium
    play sound sfx_keys_rattle
    hide image rm_sm
    show image rm_th
    with byso
    "Константин усмехнулся и выхватил ключи у Ромы."
    kt "Ага, ты это потом ей скажи.{w=1} Попробуй там подкатить, мало ли получится."
    th "Пусть его четвертуют."
    hide image rm_th
    show image rm_an
    with byso
    rm "Ну смотри.{w=1} Вот увидишь, моей будет."
    hide image rm_an with byso
    stop music fadeout 2
    "Константин с улыбкой пошёл на площадь."
    scene bg ext_square_day with byso
    "Константин достал синий телефон и посмотрел на время."
    th "10:20.{w=1} Ещё минут 40 до приезда Рены."
    show mt normal pioneer panama with byso
    play music music_list["my_daily_life"]
    "Константин встретил вожатую с большой коробкой."
    mt "Вот ты где."
    play sound sfx_put_sugar_cart
    "Вожатая поставила коробку на землю."
    show mt smile pioneer panama with byso
    mt "Это бельё для нового домика.{w=1} Иди застелись, пока новенькой нет."
    kt "Ладно."
    th "Теперь моя очередь исполнять приказы..."
    kt "А где домик?"
    show mt grin pioneer panama with byso
    mt "В первом корпусе.{w=1} Это те, что у клубов.{w=1} Первый ряд самый левый.{w=1} Вот ключи."
    "Вожатая дала Константину два новеньких ключа.{w=1} Ключи были простые, без всякой маркировки, с неровными, одинакового размера зубчиками и приплюснутой верхней частью."
    kt "Понятно.{w} Пойду тогда."
    hide mt with byso
    "Константин направился в сторону своего нового домика."
    th "Интересно, как пионер добился нашего переселения.{w}.. Может он обладает особой силой не только в кошмаре."
    th "Но тогда почему он не сверг Генду сам?"
    th "Много вопросов."
    scene bg ext_house_of_sl_day with byso
    "Константин дошёл до домика."
    th "Этот домик куда более привлекателен.{w}.. По крайней мере, в нём не живёт Сахарова."
    scene bg int_house_of_kt_day with byso
    stop ambience
    play sound door_cl
    "Константин достал полученные ключи и открыл дверь."
    "Начав уборку и заправку кроватей, он задумался."
    th "Домик на окраине и рядом есть старый корпус. {w}Надо будет туда сходить."
    th "Только сейчас до меня дошло насколько этот домик находится в самом уютном месте."
    th "Когда я жил у вожатой, её домик находился почти в центре лагеря, а теперь вот."
    th "Хоть выходи и кури, одна херня никто тут не ходит... Скорее всего"
    "Заправив кровати, Константин посмотрел на время."
    th "Почти 11.{w} Пора идти встречать Рену."
    scene bg ext_house_of_sl_day with byso
    play ambience ambience_forest_day
    play sound door_cl
    stop music fadeout 2
    "Константин взял коробку, вышел из домика, закрыл дверь на ключ и пошёл к клубам."
    scene bg ext_clubs_day
    show sh normal pioneer at left
    show el normal pioneer at right
    with fade
    play music music_list["sunny_day"]
    "У клубов стоял Шурик и Электроник."
    kt "Вам презент.{w=1} Уберите на склад."
    play sound sfx_put_sugar_cart
    "Указал Константин и поставил пустую коробку на пороге."
    show sh serious pioneer at left
    show el serious pioneer at right
    with byso
    el "А самому поставить слабо?"
    th "М-да, начнём воспитательные работы."
    hide el
    show el surprise pioneer close
    show sh surprise pioneer close at left
    with byso
    "Константин подошёл в упор к Электронику.{w=1} Тот занервничал."
    kt "Дружище, тебя родители не учили держать язык за зубами?"
    show sh rage pioneer close at left with byso
    sh "Учили, но не с таким быдлом, как ты."
    "Встрял Шурик."
    play sound sfx_punch_washstand
    hide sh
    show el shocked pioneer close 
    with vpunch
    "Константин не долго думая дал Шурику в солнышко.{w} Шурик скрючился от боли."
    kt "Ещё раз ты хоть что-то выскажешь без моего спроса, ударю так, что потом в медпункте по кусочкам собирать будут."
    el "Ладно, мы уберём!"
    hide el with byso
    "Не вытерпев сказал Электроник и подошёл к плачущему от боли Шурику."
    kt "То-то."
    stop music fadeout 2
    "Усмехнулся Константин и пошёл на остановку."
    scene bg ext_no_bus with byso
    "На остановке не было никого."
    th "Я рано походу."
    play sound light_inh
    "Закурив, он сел на бордюр."
    scene bg ext_no_bus with fade
    "Просидев минут 10, Константин услышал звук приближающегося автобуса."
    th "Наконец-то!"
    "Радостно подумал Константин и встал с места."
    play sound sfx_bus_stop
    scene bg ext_bus with byso
    "Автобус приехал.{w} Константин хотел посмотреть кто за рулём."
    "Автобус остановился, но за рулём никого не было."
    th "Что за чёрт..."
    scene bg int_bus with byso
    stop ambience fadeout 2
    "Константин зашёл в салон и начал искать Рену.{w} Он снова обратил внимание на отсутствие у автобуса педалей и приборной панели."
    play music music_list["farewell_to_the_past_edit"] fadein 3
    "Рена сидела на том-же месте, где день назад был Константин.{w} Она сладко спала, облокотясь на маленький белый чемоданчик."
    "Константин нежно потряс Рену за плечо."
    kt "Доброе утро, соня."
    show image re_kind_casual with byso
    "Рена немного вздрогнула и приоткрыла глаза."
    ren "Костя!"
    play sound sfx_pat_shoulder_hard
    hide image re_kind_casual
    show image re_kind2_casual at center:
        zoom 1
        linear 0.5 zoom 1.5 yanchor 0.1
    "Вскрикнула она и обняла Константина."
    hide image re_kind2_casual
    show image re_smile3_casual at center:
        zoom 1.5
        yanchor 0.1
    with byso
    ren "Утречка!{w} Рада снова увидеться."
    "Протянула Рена и сонно потянулась."
    kt "Я тоже рад.{w} Как поездка?"
    hide image re_smile3_casual
    show image re_smile4_casual
    with byso
    ren "Да как-как. Меня отправил пионер и тут я просыпаюсь уже с тобой."
    kt "Понятно.{w} Пошли в наш домик?"
    hide image re_smile4_casual
    show image re_grin_casual
    with byso
    ren "Идём."
    "Константин взял чемоданчик и повёл Рену к выходу."
    hide image re_grin_casual
    show image re_shy2_casual
    with byso
    "Открыв бардачок у водительского сиденья, Константин достал оттуда карту, пачку сигарет и ещё один ключ."
    ren "Откуда это?{w} Водитель на нас не рассердится?"
    kt "Автобус приехал без водителя.{w=1} Да и как вообще этот автобус водить?"
    ren "Это как вообще?"
    kt "Да вот так.{w} Автопилот времён СССР."
    stop music fadeout 2
    play ambience ambience_ext_road_day
    hide image re_shy2_casual
    scene bg ext_camp_entrance_day
    show image re_grin_casual at right
    show sl smile pioneer at left
    with byso
    "Рена усмехнулась и вышла из автобуса.{w} Константин вышел за ней."
    play music music_list["everyday_theme"] fadein 3
    "У ворот уже стояла Славя."
    show sl smile pioneer at left with byso
    sl "Привет, ты наверное новенькая?"
    hide image re_grin_casual
    show image re_bored_casual at right
    with byso
    ren "Да.{w=1} Чем обязана?"
    show sl surprise pioneer at left with byso
    "Без интереса спросила Рена. Славе стало неловко."
    show sl smile pioneer at left with byso
    sl "Меня зовут Славя. Я первая помощница вожатой, а это Костя, второй помощник вожатой."
    hide image re_bored_casual
    show image re_angry2_casual at right
    with byso
    ren "Кости в супе варятся.{w=1} А для тебя это Константин."
    show sl smile pioneer at left with byso
    sl "Х-хорошо.{w} Я тогда пойду, а Константин тебя отведёт до вожатой."
    ren "До скорой встречи."
    sl "Пока."
    hide image re_angry2_casual
    hide sl
    show image re_smile_casual
    with byso
    "Славя неловко помахала рукой и ушла."
    kt "Здорово ты её. {w=1}Ты её уже знаешь?"
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    "Рена улыбнулась."
    ren "Да, та ещё заноза.{w=1} Одна из любимиц Семёнов."
    kt "Понятно.{w=1} Пошли тогда в домик."
    hide image re_smile_casual
    scene bg ext_clubs_day
    show us normal pioneer at right
    show image re_smile_casual
    with byso
    stop music fadeout 2
    "Отравившись дальше, они вышли к клубам."
    play music music_list["always_ready"]
    "У кубов была стандартная ситуация.{w} Ульянка украла у кибернетиков очередную безделушку."
    hide image re_smile_casual
    show image re_grin_casual
    with byso
    ren "Давай сюда, я спрячу."
    show us smile pioneer at right with byso
    play sound sfx_punch_medium
    show sh rage pioneer at left with byso
    "Ульянка с улыбкой дала Рене эту безделушку.{w=1} Из клубов вышел Шурик и смерил Ульяну грозным взглядом.{w=1} На Константина он старался не смотреть."
    sh "Ульяна!{w} Где барометр?!"
    show us grin pioneer at right with byso
    us "У меня ничего нет.{w=1} Видишь, руки пустые."
    show sh upset pioneer at left with byso
    "Шурик обратился к Рене."
    sh "Новенькая.{w} Не знаешь, куда она спрятала мой барометр?"
    hide image re_grin_casual
    show image re_smile2_casual
    with byso
    ren "Ты про это?"
    show us sad pioneer at right with byso
    "Словно не понимая ситуации спросила Рена, показав вещь, что ей дала Ульяна."
    show sh smile pioneer at left with byso
    sh "Да это он.{w} Отдай пожалуйста."
    "Попросил Шурик и подошёл к ней."
    hide image re_smile2_casual
    show image re_kind_casual
    with byso
    ren "Ну тогда забери."
    show us grin pioneer at right with byso
    play sound sfx_punch_medium volume 0.7
    "Хихикнула Рена и кинула барометр Ульяне."
    show us laugh pioneer at right with byso
    us "Хороший пас!{w=1} Ну что, Шура, догонишь?"
    show sh rage pioneer at left with byso
    sh "Ах ты!"
    hide sh
    hide us
    with byso
    "Выкрикнул Шурик и кинулся на Ульянку.{w=1} Она же в свою очередь подмигнула Константину и Рене."
    us "Догоняй, очкарик!"
    "Прокричала она и метнулась прочь.{w=1} Шурик ускорился, что было сил."
    kt "Цирк, не иначе."
    "С улыбкой сказал Константин."
    hide image re_kind_casual
    show image re_smile_casual
    with byso
    ren "А то.{w=1} А теперь все, кто видел бег Шурика за Ульяной, занести по сто рублей в кассу цирка."
    stop music fadeout 2
    "С усмешкой ответила Рена."
    kt "А, кстати, тебе же нужна одежда.{w=1} Она тут, на складе."
    kt "Я возьму."
    play sound door_cl
    play ambience ambience_clubs_inside_day
    hide image re_smile_casual
    scene bg int_clubs_male_day
    with byso
    "Сказал Константин и направился на склад."
    play sound door_cl
    scene bg sklad_od with byso
    "Отрыв склад, он начал рыться в коробках."
    th "Советова, Сахарова, Хатсуне.{w}.. Двачевская?"
    th "А, вот."
    "Константин достал коробку с подписью Рюгу и пошёл на выход."
    play sound door_cl
    play ambience ambience_ext_road_day
    play music music_list["heather"]
    scene bg ext_clubs_day
    show image rm_th2 at left
    show image re_holod2_casual at right
    with byso
    "На выходе Константин заметил, что недалеко был Рома, что направился к Рене."
    th "Ух что щас будет..."
    "Рома подошёл к Рене и помахал рукой."
    rm "Привет, новенькая. Как тебя звать?"
    "Рена задумалась."
    hide image re_holod2_casual
    show image re_smile_casual at right
    with byso
    ren "Меня зовут Яна, а фамилия Салях."
    hide image rm_th2
    show image rm_th at left
    with byso
    rm "Яна Салях?"
    hide image re_smile_casual
    show image re_grin_casual at right
    with byso
    ren "Да, это я заметила. {w=1}А так с каких пор меня это должно волновать?"
    "Константин улыбнулся."
    hide image rm_th
    show image rm_an at left
    with byso
    "До Ромы дошёл подкол Рены."
    stop music fadeout 2
    rm "Ой, да иди ты, стерва!"
    play music music_list["sunny_day"]
    play sound2 sfx_put_sugar_cart
    play sound sfx_pat_shoulder_hard
    hide image re_grin_casual
    show image re_holod2_casual
    hide image rm_an
    show image rm_no at left
    with byso
    "Рена схватила Рому за галстук и притянула с силой к себе.{w} Он нехотя поддался."
    ren "А вот ты поаккуратнее со словами, молодой человек."
    ren "У меня нервы немного шалят в последнее время.{w} Давай не будем лишний раз меня выводить на гнев."
    ren "Если тебе ещё нужна голова на плечах, то иди своей дорогой и ничего не говори.{w} Твой голос как наждак для моего мозга."
    ren "Так что продолжай месить глину в своём кружке и с глаз моих долой."
    ren "Я ничего не говорю тебе - ты ничего не ляпаешь в ответ. Ясно?"
    "На удивление Константина, Рома не нашёл что ответить."
    stop music fadeout 2
    hide image re_holod2_casual
    show image re_grin_casual at right
    with byso
    "Рена отпустила Рому и позвала Константина."
    ren "Пошли.{w} Он, надеюсь, всё уяснил."
    hide image re_grin_casual
    hide image rm_no
    scene bg ext_square_day
    show image re_grin_casual
    with byso
    "Они пошли дальше. Рома так и остался в ступоре."
    play music music_list["trapped_in_dreams"] fadein 3
    kt "А круто ты его. Завидую..."
    hide image re_grin_casual
    show image re_smile4_casual
    with byso
    ren "Да ладно тебе. Ты меня этому научил."
    kt "Как это я?"
    hide image re_smile4_casual
    show image re_grin_casual
    with byso
    ren "Пока ты сидел в интернете, я запомнила все твои обороты.{w} Как видишь, пригодилось."
    kt "М-да теперь мне стыдно."
    ren "За что?"
    kt "Ты же всё видела получается. {w=1}Как я падал на самое дно."
    kt "И вот сейчас я только про это подумал."
    hide image re_grin_casual
    show image re_sad_casual
    with byso
    play sound glad
    "Рена провела рукой по голове Константина."
    ren "Эх ты, дурашка. Это для меня никогда не было важно.{w} Ты молодец."
    ren "Не печалься. Жизнь – это жизнь. И одиночество – тоже жизнь, только другими способами."
    ren "Сейчас у нас обоих есть шанс начать новую игру. Без отсылок на прошлое."
    hide image re_sad_casual
    show image re_holod2_casual
    show un normal pioneer far at fleft
    with byso
    "Недалеко сидела Лена и читала книгу."
    ren "Слишком много наблюдателей.{w} Пошли дальше."
    kt "Идём."
    "Монотонно протянул Константин и повёл Рену к домику."
    hide un
    hide image re_holod2_casual
    scene bg ext_house_of_sl_day
    with byso
    kt "Мы на месте."
    play sound door_cl
    stop ambience
    stop music fadeout 2
    scene bg int_house_of_kt_day
    show image re_grin_casual
    with byso
    ren "А ты убрался тут перед моим приходом я так вижу."
    play sound sfx_put_sugar_cart
    play sound2 sfx_open_table volume 0.6
    "Константин поставил коробку с вещами Рены на пол и пригнал чемоданчик к шкафу."
    kt "Да.{w=1} Тут был бардак.{w=1} Кровати пришлось самому заправлять."
    play music music_list["meet_me_there"]
    play sound sfx_punch_medium
    hide image re_grin_casual
    scene bg re_close
    with byso
    "Рена посмотрела на Константина и повалила его на кровать."
    "Сев поверх Константина она заглянула ему в глаза."
    ren "Мне не важно что было до нашей встречи.{w} Я истинно тебя люблю и готова любого перемолоть в фарш ради нашего будущего."
    "Прогладив Константина по торсу, она наклонилась к нему."
    ren "А ты готов ради меня убить кого-либо?"
    window hide
    menu:
        "Да":
            $ renpy.block_rollback()
            $ rerp += 1;
            ren "Всегда знала, что ты останешься верен мне."
        "Нет":
            $ renpy.block_rollback()
            ren "Почему?"
            kt "Не мой стиль.{w} Я хоть и убил троих до попадания сюда, но меня это и без того напрягает."
            ren "Понятно.{w}.. Но мне хватит мыслей о том, что ты просто любишь меня."
    "Их губы вновь слились в поцелуе.{w=1} Константин давно не чувствовал себя настолько хорошо."
    "Отлипнув от Константина, Рена села на край кровати."
    ren "Хочешь узнать что я набрала?"
    scene bg int_house_of_kt_day
    show image re_grin_casual
    with byso
    stop music fadeout 2
    "Спросила Рена и потянулась за чемоданчиком."
    kt "И чего там?"
    "Константин пересел на кровать напротив."
    play music music_list["into_the_unknown"]
    ren "Сама не знаю, я не много выбирала.{w} Сейчас и глянем."
    hide image re_grin_casual
    show image re_smile_casual
    with byso
    "Рена ввела код от чемодана и открыла его."
    "В нём лежало множество всяких вещей. {w=1}Одежда, аксессуары.{w} Внимание Константина упало на бутылку ликёра. Своеобразный вид спиртного был для него неожиданностью."
    "Он с удивлением заметил, как его глаза начинают щуриться."
    kt "Молочный ликёр.{w=1} Тебе он нравится?"
    "Константин взял бутылку и принялся её осматривать."
    hide image re_smile_casual
    show image re_smile4_casual
    with byso
    ren "Я не знаю. {w=1}Ещё не пробовала алкоголь. Выбирала по твоим предпочтениям."
    kt "Понятно.{w} Ну, что сказать, неплохой выбор."
    hide image re_smile4_casual
    show image re_grin_casual
    with byso
    "Рена улыбнулась и продолжила выкладывать вещи."
    "Константин взял небольшую коробочку и открыл её."
    "Это был новенький мультитул с разными дополнительными насадками.{w} В коробке была инструкция."
    "Константин стал внимательно читать ее, изображая интерес.{w} Оказалось, что насадок два вида — с мелкими и средними инструментами и каждая из них делает свое дело."
    kt "Вот это уже дело. {w=1}Пригодится."
    "Константин убрал его в карман."
    hide image re_grin_casual
    show image re_bored2_casual
    with byso
    ren "Пара банок консервов.{w=1} Я их тоже не просила, но раз уж дали..."
    "Константин достал катану в кейсе."
    hide image re_bored2_casual
    show image re_smile4_casual
    with byso
    ren "А это мой тебе подарок.{w=1} Я думаю, это хорошее оружие для ближнего боя. {w=1}Ещё и в кошмар можно взять."
    kt "Спасибо большое.{w} Откуда ты знаешь о том что я могу его взять в кошмар?"
    hide image re_smile4_casual
    show image re_smile_casual
    with byso
    ren "Пионер сказал что как-то можно."
    ren "Вот ещё фонарик на всякий случай."
    "Выложив всю одежду из чемодана, на дне лежал небольшой кейс из чёрной кожи."
    kt "Что это?"
    ren "Не знаю, давай посмотрим."
    hide image re_smile_casual
    show image re_shy_sad_casual
    with byso
    play sound sfx_lock_close
    pause 0.3
    play sound sfx_lock_close
    "Рена достала кейс и, щелкнув обоими заклёпками, сильно удивилась."
    kt "Что там?"
    ren "Сам посмотри!"
    "Рена развернула кейс в сторону Константина."
    "В кейсе лежал новенький и красивый пистолет Люгера, из воронёной стали и чёрного жжёного дерева.{w} Рядом был один магазин и 30 подходящих патронов."
    "Оружие поразило Константина своей ухоженностью, словно прямо с завода за пистолетом тщательно ухаживали."
    "Он взял пистолет в руку. Люгер был тяжёлым и холодным."
    kt "Ничего себе, я такие только в музеях видел."
    "Рена убрала кейс в шкаф."
    hide image re_shy_sad_casual
    show image re_smile_casual
    with byso
    ren "М-да, ну ладно, надеюсь не пригодится."
    hide image re_smile_casual with byso
    stop music fadeout 2
    "Сложив всю одежду в шкаф, Рена начала переодеваться. Константин ради приличия отвернулся к окну."
    play music music_list["everyday_theme"]
    ren "Да ладно тебе, я не голая."
    "С насмешливо пропела она."
    kt "Не хочу портить сюрприз."
    ren "Хе, как знаешь."
    ren "Готово.{w=1} Можешь смотреть."
    show image re_smile3_pioneer with byso
    "Рена была одета в пионерский костюм, что был в коробке со склада."
    kt "А тебе идёт!"
    hide image re_smile3_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Мне не очень этот наряд нравится, но раз тебе нравится, я буду его носить."
    play sound2 sfx_close_cabinet volume 1
    "Проговорила Рена и закрыла шкаф."
    kt "Ладно, в какой клуб ты хочешь?"
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "А по твоему ответ не очевиден?"
    ren "Конечно же в тот, где числишься ты."
    kt "А оно и правильно. {w=1}Нас будут кормить другой едой, что точно будет лучше.{w} Можно спокойно упрекать кого угодно, а так же нас будут называть надзирателями."
    kt "Детские мечты, но довольно весело."
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    ren "А ты смотри в перспективу.{w} Мы можем просить кого угодно сделать что угодно.{w=1} Хоть и в разумных пределах, но всё-таки удобно."
    kt "Верно.{w=1} Ну, получается, ты со мной в наставничестве?"
    hide image re_smile3_pioneer
    show image re_happy_pioneer
    with byso
    ren "Ага!"
    kt "Прекрасно, пошли сообщим вожатой, она тебя устроит."
    hide image re_happy_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Идём."
    hide image re_smile2_pioneer
    scene bg ext_house_of_sl_day
    show image re_smile2_pioneer
    with byso
    play sound door_cl
    play ambience ambience_ext_road_day
    "Выйдя из домика, Константин закрыл дверь на ключ."
    hide image re_smile2_pioneer
    scene bg ext_square_day
    show image re_smile_pioneer at cright
    show dv sad pioneer2 far
    with fade
    "На площади, они встретили Алису, что шла от библиотеки. {w}Рена показала рукой Константину постоять на месте и послушать."
    hide dv
    hide image re_smile_pioneer
    show image re_smile3_pioneer at cright
    show dv smile pioneer2 at left
    with byso
    "Увидев Рену, она немного оживилась и улыбнулась."
    dv "Здорова, ты же новенькая, как тебя звать?"
    ren "Привет. Я Рена.{w} А как тебя звать?"
    "С наигранным интересом спросила Рена."
    show dv grin pioneer2 at left with byso
    dv "А я Алиса. Будем знакомы..."
    stop music fadeout 2
    "Рена перебила Алису."
    play music music_list["faceless"]
    show dv surprise pioneer2 at left
    hide image re_smile3_pioneer
    show image re_madsmile_pioneer at cright
    with byso
    ren "А, та самая девочка о которой слухи ходят?"
    show dv guilty pioneer2 at left with byso
    "Алиса встревожилась."
    hide image re_madsmile_pioneer
    show image re_madsmile2_pioneer at cright
    with byso
    ren "Да-а, точно... Та которая надзирателю угрожала, а потом хныкала и в литературном отрабатывала?"
    "Рена начала смеяться."
    show dv cry pioneer2 at left with bso
    hide dv with byso
    "Алиса, увидев за спиной Рены Константина, заплакала и убежала в направлении второго корпуса."
    hide image re_madsmile2_pioneer
    show image re_smile2_pioneer
    with byso
    stop music fadeout 2
    "Рена прекратила смеяться. Тот смех явно был наигран ради большего давления."
    kt "Её не было смысла унижать.{w} Она и так бы сделала всё что мы захотим, стоило лишь пригрозить её секретом."
    ren "А так она вообще не сможет поставить ничего против.{w=1} Ни своё мнение, ни свои действия. {w=1}Отныне, она просто пустышка."
    ren "Тут логика простая, чем больше сломлен разум, тем проще человеком управлять. Это политика в чистом виде."
    play music music_list["everyday_theme"] fadein 3
    kt "Ладно, тебе виднее."
    "Задумчиво хмыкнул Константин.{w=1} Они направились дальше."
    hide image re_smile2_pioneer
    scene bg ext_house_of_mt_day
    show image re_smile_pioneer at left
    show mt normal pioneer panama at right
    with fade
    "Вожатая была у домиков и сидя на скамейке что-то писала."
    kt "Здравствуйте.{w=1} Вот прибыла новая пионерка.{w} Её зовут Рена."
    th "Напомню на всякий случай, Сахарова и без того туповата."
    "Ольга подняла глаза, убрала ручку и посмотрела на Рену."
    show mt smile pioneer panama at right with byso
    mt "Здравствуй, Рена.{w} Добро пожаловать в наш отряд."
    hide image re_smile_pioneer
    show image re_smile3_pioneer at left
    with byso
    ren "Здравствуйте.{w=1} Спасибо."
    show mt grin pioneer panama at right with byso
    mt "Меня зовут Ольга Дмитриевна.{w} Это Константин.{w=1} Член клуба наставничества и мой помощник."
    mt "Сегодня у нас будет годовщина лагеря и дискотека в честь этого до ужина тебе надо определиться с клубом."
    show mt smile pioneer panama at right with byso
    mt "Есть клуб кибернетики, спорта, музыки, литературы и наставничества.{w} Ты можешь посмотреть и решить, в каком клубе тебе место."
    ren "Выбираю клуб наставничества."
    show mt surprise pioneer panama at right with byso
    "Без каких либо колебаний отчеканила Рена. Вожатая сильно удивилась такой решительности."
    mt "Так ты даже не видела другие клубы."
    hide image re_smile3_pioneer
    show image re_smile2_pioneer at left
    with byso
    ren "В будущем я хотела бы стать руководителем, а не подчинённым, потому и хочу попасть в этот клуб и получить необходимые качества."
    show mt smile pioneer panama at right with byso
    "Вожатая улыбнулась."
    mt "Тогда прекрасно.{w=1} Я тебя запишу.{w} Сейчас тебе с Константином задание: вы должны пройтись по лагерю и посмотреть за исправной работой клубов."
    mt "Всех отлынивающих и занимающихся бесполезными делами можете заставить работать под предлогом лишения ужина, а так же пристроить их в любой клуб по вашему усмотрению."
    hide image re_smile2_pioneer
    show image re_happy_pioneer at left
    with byso
    ren "Хорошо, я поняла.{w=1} Всё будет на высшем уровне."
    th "Неплохо она так с Сахаровой заладила."
    show mt grin pioneer panama at right with byso
    mt "Прекрасно, если так. Через минут 15 я созову ребят, чтобы ты с ними познакомилась.{w} Пусть Константин пока покажет тебе территорию лагеря."
    kt "Сделаем."
    mt "А теперь идите.{w} Я пока созову ребят и запишу Рену в клуб."
    hide mt with byso
    "Проговорила вожатая и направилась на площадь."
    kt "Сколько попыток в твоём <<путешествии>> тебе вообще потребовалось, чтоб так других читать?"
    hide image re_happy_pioneer
    show image re_smile_pioneer
    with byso
    ren "Циклов где я общалась с обитателями было не много. {w}Как нибудь расскажу подробнее, но в целом, это первый раз как я попадаю в этот клуб."
    kt "Понятно. {w=1}Ну что, пошли погуляем?"
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Почему нет?"
    hide image re_smile3_pioneer with byso
    "Улыбчиво произнесла Рена и пошла вперёд, поманив за собой Константина."
    scene bg musclub
    show image re_smile4_pioneer at cright
    show mi normal pioneer far at left
    with fade
    "Они вышли к музклубу.{w=1} Им навстречу шла Мику."
    hide mi
    show mi smile pioneer at left
    with byso
    mi "О, привет, новенькая.{w=1} Как тебя зовут?"
    hide image re_smile4_pioneer
    show image re_angry_pioneer
    with byso
    ren "Салют. Рена.{w} Почему не в клубе?"
    show mi upset pioneer at left with byso
    "Мику неловко почесала затылок."
    mi "Да нужно Толику кое-что взять со склада.{w=1} Ты музыку любишь?"
    ren "Нет, я уже в надзирателях, а что?"
    mi "А, ну тогда ничего, извини."
    hide mi with byso
    "Отговорилась Мику и пошла дальше."
    hide image re_angry_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Странная манера вечно извиняться...{w} Она, кстати, среди обитателей наименее популярна."
    kt "Оно и понятно.{w=1} Постоянные неловкие ситуации и неумение общаться на лицо."
    hide image re_smile4_pioneer
    scene bg ext_square_day
    show mt smile pioneer panama far
    show image re_smile4_pioneer at left
    with byso
    "Константин с Реной вернулись на площадь, где их уже ожидал отряд."
    stop music fadeout 2
    mt "О, вы как раз во время.{w=1} Отряд собрался чуть быстрее чем я думала."
    mt "Константин, становись в ряд.{w=1} А ты, Рена, вставай сюда."
    "Константин встал в ряд."
    show mt grin pioneer panama far with byso
    mt "Итак, отряд, у нас сегодня очередное пополнение.{w} Это Рена. Новенькая, а так же участница клуба наставничества."
    "Рена глянула на Константина, после чего улыбнулась и помахала рукой."
    hide image re_smile4_pioneer
    show image re_smile2_pioneer at left
    with byso
    ren "Всем привет, кого не видела."
    hide image re_smile2_pioneer
    show image re_smile_pioneer at left
    show mt smile pioneer panama far
    with byso
    "Вожатая начала свою представительную речь."
    play music music_list["forest_maiden"]
    mt "Это Славя.{w=1} Моя помощница и образцовая пионерка."
    show sl smile2 pioneer at right with byso
    "Славя вышла и помахала рукой."
    sl "Привет ещё раз..."
    hide image re_smile_pioneer
    show image re_madsmile2_pioneer at left
    with byso
    ren "Здравствуй."
    stop music fadeout 2
    hide sl with byso
    "Славя неловко попятилась."
    play music music_list["she_is_kind"]
    mt "Это Мику.{w=1} Глава нашего музклуба."
    show mi upset pioneer at right
    hide image re_madsmile2_pioneer
    show image re_bored_pioneer at left
    with byso
    mi "Привет..."
    "Уныло выдавила Мику."
    ren "Угу."
    stop music fadeout 2
    hide mi with byso
    "Мику вернулась в строй."
    play music music_list["faceless"]
    show mt surprise pioneer panama far with byso
    mt "Это Алиса..."
    hide image re_bored_pioneer
    show image re_madsmile_pioneer at left
    show dv sad pioneer2 at right
    with byso
    "Алиса молча вышла из строя, боясь даже заглянуть в глаза Рене."
    ren "Чего такая неразговорчивая?{w} Скажи что-то, это не вежливо."
    dv "Привет..."
    hide dv
    hide image re_madsmile_pioneer
    show image re_smile_pioneer at left
    with byso
    stop music fadeout 2
    "Через силу буркнула Алиса и вернулась."
    show mt smile pioneer panama far with byso
    play music music_list["two_glasses_of_melancholy"]
    mt "Это Женя. Наш библиотекарь."
    show mz shy pioneer glasses at right with byso
    mz "Приветствую."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at left
    with byso
    ren "Здравствуй."
    hide mz with byso
    stop music fadeout 2
    th "А со мной она вообще не здоровалась..."
    play music music_list["timid_girl"]
    mt "Это Ульяна.{w=1} Самая младшая из отряда."
    show us shy2 pioneer at right with byso
    us "Привет!"
    "Радостно выкрикнула Ульянка."
    ren "Приветик!"
    stop music fadeout 2
    "Весьма приветливо ответила Рена."
    hide us with byso
    play music music_list["faceless"]
    mt "Наши кибернетики."
    hide image re_smile2_pioneer
    show image re_madsmile2_pioneer at left
    show image rm_an at right
    with byso
    "Вышел Рома."
    mt "Рома."
    rm "Бонжур."
    ren "Салам алейкум."
    hide image rm_an with byso
    mt "Шурик."
    "Он не удосужился даже выйти из строя и Рена его проигнорировала."
    mt "И Электроник."
    hide image re_madsmile2_pioneer
    show image re_madsmile_pioneer at left
    show el surprise pioneer at right
    with byso
    "Электроник вышел из строя, завороженно смотря на Рену."
    ren "У меня что-то в волосах?"
    el "Да нет.{w}.. Привет."
    ren "Приветствую."
    hide image re_madsmile_pioneer
    show image re_smile4_pioneer at left
    hide el
    with byso
    mt "А это Константин.{w} Умелый и серьёзный товарищ из твоего клуба."
    kt "Ну меня ты знаешь."
    "С улыбкой проговорил Константин и кивнул."
    "Рена помахала Константину рукой."
    "После слов Константина у Ромы явно изменилось выражение лица."
    show mt grin pioneer panama with byso
    mt "Так что сегодня продолжаем приготовление к дискотеке.{w=1} Все по своим клубам, через час на обед."
    hide image re_smile4_pioneer
    hide mt
    with byso
    "Заявила вожатая и ушла по своим делам.{w=1} Отряд распустился."
    show image rm_an with byso
    "Рома подошёл к Константину."
    rm "Ах, так эта стерва твоя подруга?"
    kt "Мать у тебя стерва, а это Рена."
    show image re_bored_pioneer at left with byso
    "Прорычал Константин, после чего посмотрел ему в Глаза.{w=1} К ним подошла Рена."
    rm "Значит ты своего брата променяешь на какую-то бабу?"
    kt "Я тебе скажу больше.{w=1} Твоё жалкое естество я могу без задней мысли променять на воздух в бутылке, сверху доплатив."
    play sound sfx_punch_medium
    "Рома со злости схватил Константина за воротник."
    hide image re_bored_pioneer
    show image re_madsmile2_pioneer at left
    with byso
    stop music fadeout 2
    ren "А может со мной подерёшься?"
    hide image rm_an
    show image rm_th
    with byso
    "Рома насмешливо хмыкнул."
    rm "Пф. Я девочек не бью.{w} Катись отсюда!"
    ren "Да? Я тоже мальчиков не бью."
    play music kittycity fadein 1
    hide image re_madsmile2_pioneer
    show image re_madsmile_pioneer at cleft
    with byso
    "Рена подошла к Роме на четверть метра."
    ren "Мне кажется что избиение зачастую не является достаточной мерой наказания..."
    ren "Потому я беру нож и отрезаю с мышц по маленькому кусочку, пока от тела не останется оголённый скелет."
    ren "Человек, караемый таким способом будет мучится весьма долго, по крайней мере пока не истечёт кровью...{w=1} Не думаю что тебе это хочется испытать на себе."
    ren "Или ты предпочитаешь ослепнуть?{w=1} А может по классике лоботомия?{w=1} Можешь выбрать на следующий раз."
    ren "А сейчас мы мирно разойдёмся...{w=1} Ну, если тебе жизнь ещё нужна."
    hide image rm_th
    show image rm_an
    with byso
    "После слов Рены Рома отпустил воротник Константина."
    rm "Ну и шагайте, твари."
    hide image rm_an
    hide image re_madsmile_pioneer
    show image re_smile_pioneer at cleft
    with byso
    stop music fadeout 2
    "Фыркнул он и ушёл."
    play music music_list["lightness"]
    kt "Слушай, а я такому тебя не учил..."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at cleft
    with byso
    ren "Да, это я сама умею.{w} Хоть и немного жестоко... Но меня устраивает."
    th "М-да, Рена слишком кровожадна временами.{w=1} Надо её контролировать."
    kt "Ну что, чем хочешь заняться до обеда?"
    hide image re_smile2_pioneer
    show image re_bored_pioneer at cleft
    show mi normal pioneer at right
    with byso
    "Рена задумалась.{w=1} К ним подошла Мику."
    mi "П-привет, ребята.{w=1} Я хотела бы кого-то другого в клуб."
    kt "А в чём проблема?"
    mi "Толя слишком далек от музыки.{w=1} Он не может и аккорда сыграть. {w}Сегодня вечером музыкальный номер, а я не могу его научить играть."
    hide image re_bored_pioneer
    show image re_angry_pioneer at cleft
    with byso
    ren "Почему это наша проблема?{w=1} Ты просила помощь, вот тебе помощь.{w} Как-бы подобрать больше некого."
    stop music fadeout 2
    mi "Может тогда Костя мне поможет?"
    play music music_list["sunny_day"]
    hide image re_angry_pioneer
    show image re_mad_pioneer at cleft
    with byso
    th "Упс."
    show mi shocked pioneer at right with byso
    "Рена глядела прямо в глубины души Мику.{w=1} Её взгляд был переполнен ненавистью и жестокостью.{w=1} Мику моргнула, стараясь отцепить её пронзающий взгляд от себя, но сразу же стало понятно, что это невозможно. "
    ren "Нет уж, кого дали - того дали.{w=1} Работай с ним."
    mi "Но..."
    ren "Без но.{w=1} Иди работай!"
    "Злобно прорычала Рена."
    show mi sad pioneer at right with byso
    mi "Хорошо..."
    hide mi with byso
    "Грустно промямлила Мику и ушла."
    kt "Зачем ты с ней так?"
    hide image re_mad_pioneer
    show image re_angry2_pioneer
    with byso
    "Рена подозрительно посмотрела на Константина."
    ren "Ты мне хочешь сказать что хочешь пойти с ней?"
    kt "Нет, не хочу.{w=1} Но за что с ней так?"
    stop music fadeout 2
    ren "Потому что..."
    hide image re_angry2_pioneer
    show image re_shocked2_pioneer
    with byso
    play sound sfx_pat_shoulder_hard
    play music music_list["farewell_to_the_past_edit"]
    "Константин взял Рену за руку и отвёл подальше от общественного обозрения."
    "Взяв Рену за обе руки, он заглянул ей в глаза."
    window hide
    menu:
        "Не надо так ненавидеть всех вокруг.":
            $ renpy.block_rollback()
            hide image re_shocked2_pioneer
            show image re_sad_pioneer
            with byso
            "Рена немного успокоилась."
            ren "Тоже верно.{w=1} Извини, была не права."
        "Не надо ревновать всех ко мне.":
            $ renpy.block_rollback()
            $ rerp += 1;
            kt "Я слишком много раз провинился перед тобой.{w=1} Я больше не допущу такой ошибки."
            "Константин погладил Рену по голове."
            hide image re_shocked2_pioneer
            show image re_sad2_pioneer
            with byso
            "Рена обняла Константина."
            ren "Тебе это неприятно?...{w} Не грусти, я постараюсь так больше не поступать."
            "Отлипнув от Константина, она окинула взором ближайшие 10 метров."
    hide image re_sad2_pioneer
    hide image re_sad_pioneer
    show image re_smile2_pioneer
    with byso
    kt "Ладно, идём прогуляемся что-ли?"
    ren "Идём."
    "Со слабой улыбкой ответила Рена."
    hide image re_smile2_pioneer
    scene bg ext_path2_day
    show image re_smile2_pioneer
    with byso
    "Они пошли по небольшой лесной тропе. Запах хвои и свежей листвы наполнял их легкие, делая воздух почти сладким. "
    kt "Как же это всё это странно."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Что именно?"
    kt "Мы с тобой в каком-то лагере.{w=1} Почему Генда не отправил нас в настоящий ад?"
    hide image re_smile_pioneer
    show image re_bored_pioneer
    with byso
    "Рена сорвала листок с куста."
    ren "Не знаю.{w=1} Хороший вопрос.{w} В этом сто процентов подвох."
    "Задумчиво проговорила Рена и начала делить листочек на жилки."
    kt "Хотя он и говорил, что хочет перевоспитать меня.{w=1} Сделать слугой."
    hide image re_bored_pioneer
    show image re_smile3_pioneer
    with byso
    ren "А тебе ли не смешно от таких слов?{w} Как часть твоей души, могу сказать что ты как минимум не такой."
    "Константин остановился.{w=1} Рена посмотрела ему в глаза."
    ren "Что такое?"
    hide image re_smile3_pioneer
    show image re_shy_pioneer
    with byso
    play sound sfx_punch_medium volume 0.6
    play sound2 glad
    "Константин глянул на листок, что рвала Рена и взял её за плечи."
    kt "Не называй себя так. {w=1}Отныне ты такой же человек как и я."
    ren "Но..."
    kt "Никаких но!{w=1} Ты теперь равна, а то и выше меня. {w=1}Мне неприятно слышать когда ты так себя называешь."
    kt "Ты лучше меня во всём. {w=1}Я хоть и горд, что создал такую прекрасную девушку..."
    kt "Я не хочу быть как Генда и называть тебя своим рабом.{w} Ты теперь вольна делать что тебе угодно."
    kt "Даже убить меня..."
    hide image re_shy_pioneer
    show image re_smile4_pioneer
    with byso
    "Рена поцеловала Константина."
    "Константин почувствовал в глубине души что-то тёплое и приятное."
    ren "Спасибо тебе.{w}.. Я всегда знала, что ты добрый человек.{w=1} Я люблю тебя."
    hide image re_smile4_pioneer
    show image re_smile2_pioneer
    with byso
    "Романтично произнесла Рена и немного покраснела."
    ren "Ты - мой смысл жизни и я не перенесу, если ты умрёшь или отвернёшься от меня."
    ren "Для меня это будет значить лишь смерть.{w=1} Во всех смыслах."
    "Константин сел на пенёк и достал сигарету."
    kt "Будешь?"
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Давай, почему бы не попробовать."
    play sound light_inh
    "Рена взяла у Константина сигарету с кнопкой и после Константина прикурила."
    kt "Хм, уверенно куришь, словно знаешь как это делать."
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    "Она выдохнула и с улыбкой глянула на Константина."
    hide image re_smile3_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Так ты меня и научил."
    kt "Не заставляй меня сожалеть."
    "С улыбкой ответил Константин."
    ren "В этом и в правду что-то есть.{w} Теперь я понимаю почему ты так много курил в городе. {w=1}Хорошо маскирует окружающие запахи."
    kt "Рад что ты меня понимаешь."
    "Произнёс Константин и, затушив сигарету, встал с пенька."
    "Рена докурила до фильтра и сделала так же."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Хорошо, перекурили, теперь пошли дальше?"
    stop music fadeout 2
    kt "Пошли." 
    hide image re_smile_pioneer
    scene bg ext_old_building_sunset
    with byso
    "Пройдя 100 метров, Рена и Константин наткнулись на заброшенное здание и решились подойти к нему поближе.."
    play music music_list["sunny_day"] fadein 1
    pp "Не советую сюда ходить."
    show image re_mad_pioneer with byso
    ren "Кто тут?"
    play sound par
    show image poter_n_p at right with byso 
    "Материализовался призрак пионера."
    pp "Это я. Тут вам делать нечего."
    kt "С чего бы то?"
    pp "В кошмаре именно это место является единым укрытием, но в обычной симуляции, я думаю, тут топтаться не стоит."
    kt "Хорошо.{w=1} Как скажешь..."
    "Пожав плечами хмыкнул Константин и развернулся в сторону лагеря."
    kt "Пошли.{w=1} Скоро обед."
    hide image re_mad_pioneer
    show image re_smile_pioneer
    with byso
    ren "Идём!"
    hide image poter_n_p with byso
    stop music fadeout 2
    "Кивнула Рена и пошла за ним.{w=1} Призрак растворился."
    play sound sfx_dinner_horn_processed
    "В отдалении заиграл горн."
    hide image re_smile_pioneer
    scene bg ext_dining_hall_near_day
    show image re_sad_pioneer at right
    show us smile pioneer at left
    with byso
    play music music_list["everyday_theme"]
    "Когда Константин и Рена вышли к столовой, их встретила Ульянка."
    us "Привет, новенькая.{w=1} Как проводишь свой день?"
    hide image re_sad_pioneer
    show image re_smile4_pioneer at right
    with byso
    "Рена приятно улыбнулась."
    ren "Приветик.{w=1} Я хорошо. А ты как?"
    show us grin pioneer at left with byso
    us "Хочешь, пойдём в футбол поиграем?{w=1} Заодно своего друга затащишь."
    th "Только не футбол."
    hide image re_smile4_pioneer
    show image re_smile_pioneer at right
    with byso
    ren "Я бы с радостью, но Ольга Дмитриевна дала приказ клубы караулить.{w=1} Может завтра?"
    show us laugh pioneer at left with byso
    us "Хорошо, посмотрим."
    hide us with byso
    "Радостно проговорила Ульянка и убежала в столовую."
    kt "Почему ты так хорошо к ней относишься?"
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Ну как сказать, она приятная маленькая девочка, единственная среди остальных кто будет к тебе добр."
    kt "Ну как сказать... Грубовата она, да и при том немного гиперактивна."
    play ambience ambience_dining_hall_full
    hide image re_smile_pioneer
    scene bg int_dining_hall_people_day
    show image re_sad_pioneer
    with byso
    "Они зашли в столовую."
    ren "Это всё из-за оторвы Дваче, что её не тому учит.{w=1} Она могла бы стать и опрятной девочкой, но не в компании той оторвы."
    kt "Теперь понятно, почему ты Алису так ненавидишь."
    "На обед простым смертным давали щи, пюре с котлетой и стакан компота.{w=1} Как пришла очередь Константина, он обратился к поварихе."
    kt "Добрый день. Это Рена, она тоже из наставничества."
    hide image re_sad_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Здравствуйте."
    pov "Привет.{w=1} Хорошо."
    "Повариха положила по тарелкам салата с курицей и залила их квасом.{w} В другую тарелку положили котлету с пюре, добавив к подносу стакан киселя."
    pov "Сегодня наставникам окрошка. {w=1}Приятного аппетита."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Спасибо большое."
    pov "Не за что."
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    "С улыбкой ответила повариха.{w=1} Константин пошёл за привычный ему столик."
    show image tl_normal at right with byso
    stop music fadeout 2
    "Как не удивительно, после вчерашнего за тем столиком сидел Толик."
    th "Он мазохист что-ли..."
    play music music_list["heather"]
    kt "Убить его мало."
    hide image re_smile_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Дай-ка я попробую разобраться."
    "Рена подошла к Толику и обратилась к нему."
    ren "Привет.{w=1} Можешь освободить столик, пожалуйста, это наш."
    hide image tl_normal
    show image tl_angry at right
    with byso
    "Толик без интереса поднял глаза и помотал головой в знак отрицания."
    hide image re_smile3_pioneer
    show image re_smile_pioneer
    with byso
    ren "Ну освободи местечко."
    tl "Ещё я какой-то девке место освобождать буду."
    hide image re_smile_pioneer
    show image re_mad_pioneer
    with byso
    play sound sfx_table_hit volume 0.6
    "Рена скрипнула зубами и поставила свой поднос на столик."
    ren "Так, ты, свинота жирная, либо ты прямо сейчас освободишь место, либо освобождать его будет некому."
    play sound sfx_punch_medium
    "Толик проигнорировал слова Рены.{w=1} Подошёл Константин и взял Толика за шкирку."
    hide image re_mad_pioneer
    show image re_smile_pioneer
    with byso
    kt "Я тебе говорил, что такое безумие?"
    kt "Безумие - это повторение одного и того-же действия. {w}Раз за разом,{w=0.25} раз за разом.{w=1} В надежде на изменения."
    kt "Так что, ты хочешь тарелку щей на голове поносить?{w=1} Я организую, у тебя 15 секунд."
    hide image tl_angry with byso
    "Толик молча встал, взял поднос и ушёл."
    kt "Ещё хоть раз сюда сядешь..."
    stop music fadeout 2
    "Константин подошёл к соседнему столику со свободным стулом, где сидели пионеры из другого отряда."
    kt "Вам стул нужен?"
    pions "Нет, бери."
    play sound dvizh
    "Почти хором ответили пионеры.{w=1} Константин взял стул и поставил его Рене."
    kt "Вот, садись. Приятного аппетита!"
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Спасибо, тебе тоже."
    "Мило произнесла Рена и начала есть окрошку."
    th "Давно я не ел окрошки, да ещё и с таким квасом."
    th "Теперь понятно, что именно было лучше по мнению старух и стариков в моём падике."
    th "Квас без всяких примесей и добавок. {w=1}Такой я пил только в раннем детстве."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Как же это вкусно!{w=1} Для знойного летнего дня лучше ничего не придумаешь."
    kt "Это точно.{w=1} Квас ещё такой вкусный, не то что я пробовал дома."
    ren "Мне сравнивать не с чем, но всё-же это прекрасно."
    "Рена переключилась на гречку. Константин уже доедал котлету."
    show mt grin pioneer at left with byso
    play music music_list["lightness"] fadein 3
    "К ним подошла вожатая со своей стандартной глупой лыбой."
    th "Что опять то?"
    show mt smile pioneer at left with byso
    mt "Приятного аппетита, пионеры."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Спасибо."
    "С улыбкой ответила Рена.{w=1} Константин кивнул вожатой."
    show mt grin pioneer at left with byso
    mt "Я и забыла, что вам надо ещё пройти медосмотр.{w} Вот вам нужные бумаги.{w=1} Между делом зайдите в медпункт."
    kt "Ладно, будет сделано."
    mt "Вот и хорошо.{w=1} Если будут ещё поручения, я вас найду."
    kt "Хорошо."
    hide mt with byso
    "Вожатая ушла от столика Константина и направилась к раздаче."
    "Константин закинул ногу на ногу и начал допивать кисель."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Что дальше делаем?"
    "Уточнила Рена, сложив столовые приборы в тарелку.{w=1} Константин начал вчитываться в бумажки."
    kt "Ну что поделаешь, пошли в медпункт."
    ren "Пошли."
    play ambience ambience_ext_road_day
    hide image re_smile3_pioneer
    scene bg ext_dining_hall_near_day
    with byso
    scene bg map_camp with byso
    "Выйдя из столовой, Константин открыл карту."
    kt "Тут буквально за поворотом."
    "Рена заглянула в карту."
    ren "Давай сразу продумаем маршрут. {w}Смотри. Тут мы будем в медпункте."
    "Указав на медпункт, она начала водить пальцем по карте."
    ren "Потом мы навестим спортивный клуб, оттуда в литературный, потом в музыкальный, а там уже и в гей-клуб."
    "Константин рассмеялся, Рена улыбнулась и посмотрела на идущего им на встречу Электроника и Шурика."
    ren "Вспомнишь звёздочку - она и загорится.{w=1} Вот и они."
    scene bg ext_dining_hall_near_day
    show image re_smile4_pioneer at cleft
    show el surprise pioneer at right
    show sh serious pioneer at fright
    with byso
    "Заметив Рену, Электроник смущённо отвёл взгляд, а Шурик стал злобно смотреть на Константина."
    show el grin pioneer at right with byso
    el "О, привет Рена.{w=1} Не хочешь с нами за столик кибернетиков?{w} Вместе есть вкуснее."
    hide image re_smile4_pioneer
    show image re_smile3_pioneer at cleft
    show el upset pioneer at right
    with byso
    "Рена искренне рассмеялась, чем ещё пуще смутила Электроника."
    ren "Я только из столовой вышла, а меня уже тут достаёт кибернетик с предложениями на свидание."
    ren "Приятного тебе аппетита, спасибо за предложение, мы вам перезвоним."
    "С усмехнулась Рена и пошла вперёд, поманив Константина за собой."
    hide el
    hide sh
    hide image re_smile3_pioneer
    scene bg ext_square_day
    show image re_smile_pioneer
    with byso
    kt "Вот это клоун конечно.{w=1} Даже после выходок своих коллег по клубу он вообще не боится с тобой говорить..."
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Твердолобость не порок, что могу сказать.{w=1} Хотя...{w=1} может просто отсутствие инстинкта самосохранения."
    hide image re_smile2_pioneer
    scene bg ext_aidpost_day
    show image re_smile_pioneer
    with byso
    "Они вышли к зданию медпункта. Над ним развивался белый флаг с красным крестом."
    kt "Меня напрягает, что там будет ворчливая старуха за 60 лет.{w=1} Не знаю к чему бы то."
    hide image re_smile_pioneer
    show image re_shy_pioneer
    with byso
    "Рена немного покраснела."
    ren "Не буду спойлерить, сам всё увидишь."
    th "Только не это..."
    stop music fadeout 2
    play sound sfx_knock_door2
    "Константин постучал в дверь."
    csp "Войдите!"
    th "Ну голос вроде не старческий."
    play sound door_cl
    stop ambience
    play music music_list["gentle_predator"]
    hide image re_shy_pioneer
    scene bg int_aidpost_day
    show cs normal glasses at right
    show image re_smile2_pioneer at left
    with byso
    "Войдя в кабинет, Константин увидел медсестру лет 30-ти, что читала журнал мод."
    show cs smile at right with byso
    csp "Ну здравствуйте...{w=1} Пионеры..."
    "Медсестра быстро окинула взглядом Рену, потом перевела взгляд на Константина."
    kt "Мы на медосмотр.{w=1} Вот бумаги."
    show cs smile glasses at right with byso
    "Константин протянул ей бумаги. Медсестра достала очки и посмотрела на бумажки."
    csp "Что-ж, раз вы новенькие, введу вас в курс дела. {w}Я Виола, ваш врач на эту смену."
    cs "Что-то болит?{w=1} Смело ко мне, помогу чем смогу."
    cs "Теперь медосмотр.{w=1} Кто первый?"
    kt "Как-то не важно, давайте я."
    hide cs
    hide image re_smile2_pioneer
    show cs shy glasses
    with byso
    cs "Какой смелый молодой человек. Не парень, а мечта, правда?"
    "С профессиональной ухмылкой обратилась она к Рене."
    ren "Может быть..."
    show cs smile with byso
    cs "Итак, жалобы на здоровье, что-то болит?"
    kt "Жалоб нет, ничего не болит."
    show cs normal stethoscope with byso
    cs "Поднимай рубашку, будем слушать."
    "Константин поднял рубашку. Медсестра достала стетоскоп и приложила его к груди Константина."
    cs "Хорошо, дыши."
    "Он начал дышать, пытаясь сдержать кашель курильщика, из-за чего начал похрипывать."
    cs "Хорошо, теперь спиной."
    hide cs
    show image re_smile4_pioneer
    with byso
    "Константин развернулся спиной и поймал на себе взгляд Рены, что мгновенно перевела взгляд в окно."
    hide image re_smile4_pioneer
    show cs smile
    with byso
    cs "Вроде всё хорошо, но с сигаретами балуйся поменьше.{w=1} Садись на стул, будем голову на вшей проверять."
    th "Что, настолько всё плохо, что я хриплю как старый дед?"
    "Константин сел на стул.{w=1} Виола начала копаться в волосах Константина."
    cs "Вроде чист, но что у тебя за странный шрам на голове...{w=1} Не важно.{w} Теперь весы."
    hide cs
    show cs normal glasses at right
    show image re_smile_pioneer at left
    with byso
    "Константин молча встал на весы."
    th "Механические весы, такие-же у бабушки были."
    cs "Хорошо, записала.{w} Рост."
    "Он прислонился к ростомеру."
    cs "1,85.{w=1} Всё, можешь заправлять рубаху и забирать бумагу."
    "Константин заправился и забрал у Виолы бумажку."
    cs "Всё, свободен.{w=1} До скорой."
    kt "До свидания.{w=1} Я жду у выхода."
    "Обратился он к Рене."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    "Она утвердительно кивнула."
    hide image re_smile4_pioneer
    scene bg ext_aidpost_day
    with byso
    play sound door_cl
    play ambience ambience_ext_road_day
    stop music fadeout 1
    "Выйдя из кабинета, он облокотился на столб."
    th "Ах, да.{w=1} Шрам на голове."
    stop ambience
    play sound in_vosp
    play music sab
    scene bg black
    show shum_white
    with flash
    vr "Везите в отдел черепно-мозговых травм, он истекает кровью!"
    csp "Хорошо, дорогу носилкам!"
    "Константин упал в обморок.{w=1} Последнее, что он заметил - это лицо медсестры, что казалось ему невероятно знакомым."
    scene bg black
    show shum_white
    with flash
    na "Извини, я не думала, что так выйдет."
    ks "Да иди ты нахуй!{w=1} Я уже понял, какая ты падаль.{w} Натравить на своего же парня какого-то дружка-быдлана."
    na "Я не хотела, чтоб так вышло..."
    ks "Да?{w=1} А я не хотел чтобы мне по голове били стеклянной бутылкой!"
    csp "Время посещения вышло, покиньте помещение."
    na "Хорошо, пока..."
    scene bg black
    hide shum_white
    show bg kt_room
    show shum_white
    with flash
    vr "Вы скоро поправитесь. У вас лишь лёгкое потрясение мозга с одной глубокой раной."
    ks "А что это было?"
    "Доктор поправил очки."
    vr "Вас ударили бутылкой по голове.{w=1} Бутылка раскололась и нанесла вашей голове внешние повреждения. В итоге вы потеряли сознание от болевого шока."
    ks "Понятно.{w=1} Это заживёт?"
    vr "Волосы отрастут, но останется шрам."
    th "Ну прекрасно. Этого мне не хватало."
    stop music
    hide shum_white
    scene bg ext_aidpost_day
    show image re_serious3_pioneer
    with flash
    play ambience ambience_ext_road_day
    play sound door_cl
    "Из медпункта вышла Рена с заполненной бумажкой.{w=1} Встав рядом с Константином, она посмотрела в даль."
    ren "О чём задумался?"
    kt "Да так.{w=1} Вспомнил откуда у меня шрам на голове."
    hide image re_serious3_pioneer
    show image re_smile2_pioneer
    with byso
    "Рена погладила шею Константина."
    ren "Ничего, шрамы украшают мужчину.{w=1} Это не повод грустить."
    kt "Да я и не грущу.{w=1} Просто воспоминания противные."
    play music music_list["get_to_know_me_better"] fadein 3
    kt "Ладно, пошли по клубам?"
    "Спросил Константин, убрав бумажку из медпункта в карман."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Идём.{w=1} Всё веселье ещё впереди."
    kt "А то!"
    "По своему плану они пошли к спортивному клубу."
    ren "Чем сегодня вечером заниматься будем?"
    kt "Не знаю.{w=1} Идей нет, честно говоря."
    hide image re_smile_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Сегодня будет дискотека вроде как.{w=1} Можно и станцевать..."
    kt "Да об твои намёки порезаться можно.{w=1} Конечно станцуем."
    hide image re_smile4_pioneer
    show image re_smile3_pioneer
    with byso
    ren "Вот и хорошо."
    stop music fadeout 1
    hide image re_smile3_pioneer
    scene bg ext_playground_day
    show image re_smile_pioneer at cright
    show us normal sport at left
    with fade
    play music music_list["timid_girl"]
    "Выйдя на площадку, первое что они заметили это одинокую Ульянку, что тренировала финты с футбольным мячом."
    show us smile sport at left with byso
    us "О, привет новенькие!{w=1} Не хотите мячик попинать?"
    hide image re_smile_pioneer
    show image re_smile3_pioneer at cright
    with byso
    ren "Я ж говорила, мы с радостью, да вот только дела."
    show us calml sport at left with byso
    us "Ну мало-ли что-то изменилось..."
    "Словно с обидой пробурчала Ульянка."
    show us smile sport at left with byso
    us "Костя, а хочешь устроить небольшой забег?"
    kt "Зачем?"
    hide image re_smile3_pioneer
    show image re_smile_pioneer at cright
    with byso
    us "Не знаю, я хочу загладить наш вчерашний конфликт."
    show us grin sport at left with byso
    us "Но ты не подумай.{w=1} Это всё благодаря твоей подруге."
    window hide
    menu:
        "Согласиться.":
            $ renpy.block_rollback()
            $ rerp += 1;
            $ event1 += 1;
            us "Хорошо.{w=1} Бежим вокруг поля один круг.{w=1} Ставка чисто символическая - стакан киселя на ужине."
            kt "Ладно, почему нет."
            hide image re_smile_pioneer
            hide us
            show us laugh sport
            with byso
            "Константин встал на черту. Ульянка встала рядом."
            ren "На старт.{w=1} Внимание. Марш!"
            "Константин резко стартанул, немного обогнав Ульянку."
            th "Неужто она отстаёт?"
            "Как бы не так.{w=1} Ульяна мигом догнала Константина и вышла вперёд на повороте."
            "Константин прибавил ходу и выровнялся с ней."
            "Но это не помогло.{w=1} Ульяна всё-равно его опередила и добежала быстрее."
            "Константин пересёк финиш и начал восстанавливать дыхание."
            show us grin sport with byso
            us "А ты не так плох как кажешься, но всё-равно проиграл."
            kt "Ну уж спасибо, бегунья..."
            "Съязвил Константин, переводя дыхание."
            us "Теперь за тобой должок.{w=1} Не забудь, а сейчас у меня матч с ребятами из другого отряда."
            show image re_smile2_pioneer at cright
            with byso
            kt "Хорошо, удачи тебе."
            "Он отдышался и размял ноги."
            ren "Болеем за тебя."
            us "Спасибо, ладно, идите."
            "Проговорила Ульяна и помахала им рукой.{w=1} Константин с Реной направились к библиотеке."
        "Отказать.":
            $ renpy.block_rollback()
            kt "Не, я в беге не силён, а так благодаря нашей обшей подруге, я готов забыть все наши конфликты."
            show us sad sport at left with byso
            us "Эх ты.{w=1} Всё такой же зануда...{w=1} Скоро у меня матч с ребятами из другого отряда."
            ren "Хорошо, удачи тебе."
            kt "Удачи."
            us "Спасибо, ладно, идите."
            "Проговорила Ульяна и помахала им рукой. Константин с Реной направились к библиотеке."
    hide image re_smile_pioneer
    hide us
    show image re_smile2_pioneer
    with byso
    ren "Вот видишь, она не такая плохая девочка.{w=1} Главное иметь к ней правильный подход."
    kt "Может ты и права..."
    "Заключил Константин, потянувшись на ходу."
    stop music fadeout 2
    hide image re_smile2_pioneer
    scene bg ext_square_day
    show sl normal pioneer at left
    show image re_bored_pioneer at cright
    with fade
    "Выйдя на площадь, они заметили Славю, что мела площадь."
    show sl smile2 pioneer at left with byso
    sl "Привет, ребят.{w=1} Как успехи?"
    kt "Нормально.{w=1} А зачем ты метёшь площадь, когда на ней нет мусора?"
    show sl smile pioneer at left with byso
    sl "Это я уже заканчиваю.{w=1} Люблю чистоту."
    ren "Ясно.{w=1} Мы пойдём, нам ещё 3 клуба осмотреть."
    sl "Хорошо.{w=1} Кстати, как закончите, можете сходить искупаться.{w} Всё-равно у нашего клуба больше дел быть не должно."
    th "Уж спасибо за разрешение."
    kt "Будем знать."
    hide sl
    hide image re_bored_pioneer
    show image re_sad_pioneer
    with byso
    "Кивнул Константин и поплёл дальше.{w=1} Рена пошла с ним."
    ren "Её разрешения только и ожидали."
    kt "Читаешь мои мысли."
    "С усмешкой подметил он."
    hide image re_sad_pioneer
    scene bg ext_library_day
    with fade
    "Наконец, они вышли к библиотеке."
    ren "Самое унылое место лагеря..."
    kt "М-да, и не поспоришь."
    scene bg int_library_day
    show image re_bored_pioneer at cright
    with byso
    play ambience ambience_library_day
    play sound door_cl
    play music music_list["smooth_machine"]
    "Произнёс Константин и открыл дверь."
    "В библиотеке стояла полная тишина, среди которой было слышно лишь лёгкое сопение."
    ren "А вот и первый бездельник."
    kt "Или бездельница."
    "Константин указал на Женю, что спала за своим местом."
    play sound sfx_knock_door2
    "Не долго церемонясь, он отстучал по столу."
    ren "Доброе утро.{w=1} А чем мы занимаемся?"
    "Упрёк Рены не очень понравился Жене."
    show mz bukal pioneer at left with byso
    mz "Да так, уровень пыли на столе измеряю."
    "Сонно проворчала Женя, надевая очки."
    show mz normal pioneer glasses at left with byso
    mz "Не подумайте.{w=1} Я весь план на сегодня выполнила.{w} Алиса хоть и того не хотя, помогла мне с уборкой.{w=1} Всё чисто, можете проверить.{w} Лена занята стенгазетой, а я жду результата."
    kt "Так помоги ей что-ль?"
    mz "Да зачем, она предпочитает работать одна.{w=1} У неё так лучше получается."
    show un smile pioneer at fleft
    hide image re_bored_pioneer
    show image re_mad_pioneer at cright
    with byso
    "Из-за угла вышла Лена.{w=1} Рена смерила её презрительным взглядом."
    un "Стенгазета готова.{w=1} Можешь проверить..."
    show un shy pioneer at fleft with byso
    "Заметив Константина, Лена покраснела."
    show mz laugh pioneer glasses at left with byso
    mz "Вот, видите, безделья ни в одном глазу."
    kt "Ладно, сегодня мы добрые, так что отдыхайте пока."
    "Приказал Константин, направляясь к выходу."
    kt "Идём, Рена."
    play ambience ambience_ext_road_day
    play sound door_cl
    stop music fadeout 2
    hide image re_mad_pioneer
    hide mz
    hide un
    scene bg ext_library_day
    show image re_serious_pioneer
    with byso
    "Рена, подозрительно глянув Лене в глаза, направилась к выходу."
    kt "Половину дел сделали.{w=1} Дальше по плану Мику?"
    ren "Да, идём..."
    "Задумчиво прошептала Рена."
    kt "О чём думаешь?"
    ren "Да нет, ерунда, не бери в голову."
    kt "Как знаешь."
    hide image re_serious_pioneer
    scene bg musclub
    show image re_smile_pioneer
    with fade
    play sound sfx_miku_song_learn2 volume 0.6
    "У веранды клуба были слышны кривые аккорды гитары."
    mi "Нет, Толя, смотри как надо."
    play sound sfx_miku_song_learn1 volume 0.6
    "Судя по всему, Мику отобрала гитару у Толика и сыграла аккорд правильно."
    mi "Уследил как надо? Могу ещё раз показать."
    tl "Да я понял уже."
    play sound sfx_miku_song_learn2
    "Толик снова сыграл аккорд неправильно."
    kt "Ну, я думаю тут всё и так ясно."
    hide image re_smile_pioneer
    show image re_bored_pioneer
    with byso
    ren "М-да.{w=1} Идём дальше?"
    kt "Пошли."
    hide image re_bored_pioneer
    scene bg ext_clubs_day
    show image re_bored_pioneer
    with fade
    play sound sfx_knock_door2
    "Дойдя до клубов, Константин вежливо постучал, несмотря на отсутствие желания вообще с кем-то из кибернетиков общаться."
    el "Заходите!"
    "Константин открыл дверь и с ухмылкой пропустил Рену."
    kt "Дамы вперед."
    hide image re_bored_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Да-да, очень смешно."
    "С улыбкой подметила она."
    play music music_list["sunny_day"]
    play sound door_cl
    play ambience ambience_clubs_inside_day
    hide image re_smile2_pioneer
    scene bg int_clubs_male_day
    show image re_smile_pioneer at cright
    show image rm_th at left
    show el surprise pioneer at fleft
    show sh upset pioneer at cleft
    with byso
    "В клубе была типичная атмосфера.{w=1} Шурик и Рома стояли над каким-то чертежом, а Электроник завороженно смотрел на Рену."
    hide image re_smile_pioneer
    show image re_angry_pioneer at cright
    with byso
    ren "Я тебе что, картина? Чего ты на меня пялишься уже пол-дня?{w=1} Хватит, мне неприятно!"
    el "Извини."
    "Отмазался он и опустил взгляд в пол."
    hide image re_angry_pioneer
    show image re_angry2_pioneer at cright
    with byso
    ren "Не извиню, если повторится."
    hide image rm_th
    show image rm_an at left
    with byso
    rm "И чё вам тут надо?"
    kt "Водки и шоколада!{w} Проверить чем вы тут заняты."
    show sh rage pioneer at cleft with byso
    sh "Мы, в отличие от некоторых, заняты делом."
    th "Как ты меня бесишь!"
    kt "Слышь, водолаз, тебе там опять зубы жмут?"
    show sh serious pioneer at cleft with byso
    rm "А тебе там ничего не жмёт, хамить так кому попало."
    kt "Мне ничего, я делаю свою работу, а эта чепуха очкастая мне ещё что-то высказывает."
    rm "Сам ты чепуха, а он нормальный мужик!"
    hide image re_angry2_pioneer
    show image re_madsmile_pioneer at cright
    with byso
    ren "Ну да, с точки зрения биологии он мужского пола, но в душе явно хрупкая девочка, что в случае чего прячется за чужую спину."
    "Рена хихикнула."
    ren "Да и вообще очень странно, что в отличие от тебя, Рома, Костя вырос адекватным человеком."
    rm "Он то?! {w=1}Да ты его первый день видишь!"
    ren "А с чего ты взял?"
    ren "Костю я знаю больше нескольких лет.{w=1} Тебя тоже, кстати. {w=1} Память подводит?{w=1} Могу напомнить."
    stop music fadeout 2
    rm "А меня ты вообще не знаешь, прошмандовка."
    ren "Да?"
    hide image re_madsmile_pioneer
    show image re_madsmile2_pioneer at cright
    with byso
    play music "<from 11>inrealnost/Music/Music/kittycity.mp3" fadein 3
    "Рена ухмыльнулась."
    ren "А как твой клуб отнесётся к тому, что ты любишь поиздеваться над людьми?"
    hide image rm_an
    show image rm_th at left
    show el upset pioneer at fleft
    with byso
    ren "Ну ладно над людьми, это можно понять, но что тебе сделал тот дворовый серый котёнок?"
    ren "Неужто он настолько оскорбил тебя своим существованием, что ты решил раздавить его?"
    hide image rm_th
    show image rm_th2 at left
    show el scared pioneer at fleft
    show sh scared pioneer at cleft
    with byso
    ren "Он протяжно кричал, пока ты своим ботинком давил его голову."
    ren "А ты словно на зло его давил медленно, чтоб он ещё дольше мучился."
    ren "Костя пытался помочь пушистому, но ты просто превратил голову ничем не повинного зверька в кровавую лужу."
    "Рома замолчал от удивления.{w=1} Шурик и Электроник стояли в ужасе и смотрели на Рому."
    ren "Ну да ладно, дальше вам расскажет вам сам Рома. {w=1}Я сюда пришла чтоб узнать, чем занят клуб глиномесов.{w=1} Сделаем вид, что ничем."
    rm "Ты врёшь, не было такого!"
    ren "От правды не убежишь...{w=1} Она настигнет тебя везде, даже здесь.{w} А у нас ещё есть дела."
    ren "Пошли, Кость.{w=1} Пусть дальше сами разбираются."
    kt "Соглашусь."
    stop music fadeout 3
    "Константин и Рена направились к выходу."
    play sound door_cl
    play ambience ambience_ext_road_day
    play music music_list["i_want_to_play"]
    hide sh
    hide el
    hide rm_th
    hide image re_madsmile2
    scene bg ext_clubs_day
    show us smile pioneer at right
    show image re_smile_pioneer at left
    with byso
    "Выйдя из клуба, они встретили вечно жизнерадостную Ульянку.{w=1} Судя по её настроению, историю из жизни Ромы она не услышала."
    us "Ну как вам поход к этим.{w}.. Как вы там говорили... Глиномесам?"
    "С усмешкой уточнила Ульяна.{w=1} Константин поддержал усмешку."
    kt "Да как всегда, чертят черти чертёж."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at cright
    show us grin pioneer at right
    with byso
    "Срифмовал Константин.{w=1} Рена подошла к Ульянке и шепнула что-то на ухо."
    hide image re_smile2_pioneer
    show image re_smile_pioneer at left
    show us laugh pioneer at right
    with byso
    us "Хорошо, я поняла.{w=1} Вот потеха то будет."
    us "Тогда я их караулить.{w=1} Потом обязательно покажу!"
    play sound sfx_bush_leaves
    "Игриво проронила Ульянка и спряталась в кустах."
    hide us
    hide image re_smile_pioneer
    scene bg ext_square_day
    show image re_smile_pioneer
    with byso
    "Рена с Константином вышли на площадь.{w} Любопытство Константина взяло своё."
    kt "А что ты ей сказала?"
    hide image re_smile_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Я попросила выкрасть тот самый чертёж.{w=1} Интересно, что они там планируют."
    kt "Это правильно.{w=1} Либо у них Электроник тугодум, либо он специально нас этим заинтересовал."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Скорее первое.{w=1} Он и так особо умом отличен не был, хотя клеится ко мне впервые.{w} Куда теперь, кстати?"
    stop music fadeout 3
    "Константин, почесав подбородок, посмотрел на статую Генды."
    kt "В теории, мы всё сделали и можем отдохнуть.{w=1} Я думаю, стоит доложить вожатой об этом, а там увидим."
    ren "Хорошо идём.{w=1}.. А вот и она, вспомни звёздочку как говорится..."
    play music music_list["lightness"] fadein 2
    kt "Да-да.{w=1} Ольга Дмитриевна!"
    hide image re_smile_pioneer
    show mt smile pioneer panama at left
    show image re_smile_pioneer at right
    with byso
    "Вожатая откликнулась и подошла к Константину."
    mt "Что такое? Уже закончили?"
    kt "Да, мы всё.{w=1} Вот бумажки из медпункта."
    play sound sfx_paper_bag
    hide image re_smile_pioneer
    show image re_smile4_pioneer at right
    with byso
    "Константин и Рена достали бумажки из карманов и отдали вожатой."
    kt "Будет какая ещё работа?"
    "Ольга сложила документы в карман и задумалась."
    mt "Работа то всегда есть, но для вас ничего.{w} Хотите на кого-то доложить?{w=1} Как раз нужны работники для настройки музыкального оборудования."
    mt "Кибернетики утром что-то сделали, но как видите, ничего ещё не готово."
    hide image re_smile4_pioneer
    show image re_smile3_pioneer at right
    with byso
    ren "Очень удобно, что они как раз ничем не заняты.{w=1} Смело их зовите."
    "Вожатой понравились слова Рены."
    mt "Хорошо.{w=1} Прекрасная работа!{w} Пока до ужина можете быть свободны."
    kt "Понятно, спасибо.{w=1} Мы можем пойти на пляж?"
    mt "Пожалуйста.{w=1} Идите.{w} Я вас найду на ужине в случае чего."
    kt "Тогда мы пошли?"
    show mt grin pioneer panama at left with byso
    mt "До ужина.{w=1} Не забудьте."
    hide image re_smile3_pioneer
    show image re_smile4_pioneer
    hide mt
    with byso
    "Напомнила вожатая и ушла."
    ren "А быть надзирателем вовсе не так нудно, как казалось.{w=1} Плавки при тебе?"
    kt "Не-а.{w=1} Пошли в домик зайдём."
    ren "Хорошо."
    hide image re_smile4_pioneer
    scene bg int_house_of_kt_day
    show image re_sad_pioneer
    with fade
    stop ambience
    play sound door_cl
    stop music fadeout 5
    "Дойдя до домика, Константин нашёл свои плавательные шорты."
    "За ним вошла Рена и взяла мешочек, куда положила свои принадлежности."
    kt "Я к тебе положу?"
    hide image re_sad_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Хорошо, вот."
    "Константин взял мешок и положил туда свои шорты."
    kt "Теперь можно идти."
    play ambience ambience_ext_road_day
    play music music_list["everyday_theme"]
    hide image re_smile2_pioneer
    scene bg ext_square_day
    show image re_smile_pioneer
    show sh serious pioneer far at fleft
    show el normal pioneer far at left
    with fade
    "Они вернулись на площадь.{w=1} Там уже Шурик копался в технике."
    ren "Хе-хе, так то."
    stop music fadeout 3
    hide image re_smile_pioneer
    scene bg ext_playground_day
    show mt angry pioneer panama
    show us sad pioneer at left
    show image re_sad2_pioneer at right
    with byso
    play music music_list["awakening_power"] fadein 2
    "Они вышли к футбольному полю, где встретили вожатую, что отчитывала Ульяну."
    kt "Что случилось?"
    mt "Шурик сказал, что она регулярно у него ворует и грубит ему, вот и ведём разъяснительные работы."
    show us dontlike pioneer at left with byso
    us "Да не грубила я ему!{w=1} Он выдумывает!"
    show mt rage pioneer panama with byso
    mt "Как ты разговариваешь со старшими?!"
    "Гнев Ольги дошёл до точки кипения."
    hide image re_sad2_pioneer
    show image re_angry_pioneer at right
    with byso
    ren "Да на самом деле, тут не столько Ульяна виновата, сколько Шурик и остальные."
    mt "Что?"
    show mt surprise pioneer panama
    show us calml pioneer at left
    with byso
    "Все вокруг Рены изрядно удивились, а особенно Ульянка."
    ren "Кибернетикам самим надо следить за языком. {w}Они грубят в ответ на замечания и показывают ей плохой пример."
    "Поучительно высказала Рена.{w=1} Константин добавил."
    kt "Видимо, думают что я брат одного из них и в случае чего отмажу от ответственности.{w=1} Ошибаются."
    show mt normal pioneer panama with byso
    stop music fadeout 3
    "Вожатая в момент сменила гнев на милость."
    mt "Ну тогда хорошо, я с ними поговорю."
    show mt angry pioneer panama with byso
    "Она перевела взгляд на Ульяну."
    mt "А ты, Ульяна, сделай так, чтоб на тебя больше не было жалоб."
    us "Ну ладно..."
    hide mt with byso
    "Вожатая ушла."
    play music music_list["timid_girl"]
    hide image re_angry_pioneer
    show image re_smile_pioneer at right
    show us grin pioneer at left
    with byso
    us "А круто вы ей лапши на уши навешали!{w} Спасибо вам."
    ren "Да ничего.{w} Старайся больше не попадаться.{w=1} От этого зависит наша репутация."
    us "Постараюсь."
    "На удивление серьёзно ответила Ульянка."
    kt "Кстати, ты достала, что тебя просила Рена?"
    show us laugh2 pioneer at left with byso
    us "Не, вожатая зашла в ненужный момент, вот мне и выговаривали.{w=1} Но до ужина обязательно украду!"
    "Игриво протараторила Ульянка.{w=1} Константин кивнул."
    kt "Прекрасно.{w=1} Удачи тогда."
    hide image re_smile_pioneer
    show image re_smile3_pioneer at right
    with byso
    ren "Хочешь с нами на пляж?"
    show us grin pioneer at left with byso
    us "Да нет, матч, дела.{w}.. Воровские!"
    "Добавила Ульяна и широко улыбнулась."
    ren "Тогда беги.{w=1} Как кстати прошлый матч?"
    show us upset pioneer at left with byso
    us "Да как-как, вратарь-дырка, обороняющий-бревно и только я в нападении.{w=1} Проиграли короче, ничего хорошего."
    hide image re_smile3_pioneer
    show image re_smile4_pioneer at right
    with byso
    ren "Ну что поделать, одной хорошо играть в командные игры сложновато."
    th "Мои слова..."
    show us laugh pioneer at left with byso
    us "Ух, это точно."
    us "Ладно, пойду займусь твоей просьбой, за мной должок."
if event1 == 1:
    us "За тобой тоже, кстати, не забывай!"
    "Напомнила Ульянка."
    kt "Помню-помню."
    jump vjidnsavnpdasnjvs
else:
    jump vjidnsavnpdasnjvs
label vjidnsavnpdasnjvs:
    hide us with byso
    stop music fadeout 3
    "Ульянка убежала по своим делам."
    hide image re_smile4_pioneer
    scene bg ext_beach_day
    with byso
    play ambience ambience_boat_station_day
    "Выйдя на пляж, Константин начал искать кабинки для переодевания."
    th "Не вызывают эти кабинки у меня доверия.{w}.. Но куда-ж деться."
    scene bg black with byso
    "Рена и Константин разошлись по раздевалкам. Константин, вспомнив вчерашний сюрприз в кабинке, пытался переодеться как можно быстрее."
    scene bg ext_beach_day
    show image re_smile_swim
    with byso
    play music music_list["goodbye_home_shores"] fadein 1
    "Выйдя на пляж, заметил Рену в жёлтом купальнике."
    kt "Купаться?"
    hide image re_smile_swim
    show image re_laugh_swim
    with byso
    ren "Купаться!"
    play sound sfx_water_emerge
    "Они разбежались и прыгнули в тёплую воду."
    "На момент время словно остановилось.{w=1} Рена и Константин отплыли от берега и, наслаждаясь тёплыми волнами легли на спину."
    "Небо было чистым.{w=1} Виднелись лишь небольшие облака, что шли в прекрасное далёко."
    "Грузовой поезд, что шёл вдалеке, легонько постукивая лишь добавлял расслабляющей атмосферы."
    "Подул прохладный ветерок, что лишь больше заставлял оставаться в тёплой воде. "
    "В какой-то момент Константин повернул голову и увидел Рену, которая глядела на него. Они долго глядели друг на друга, и Рене показалось, будто на её глазах заискрились радужные капли."
    hide image re_laugh_swim
    show image re_smile_swim
    with byso
    "Рена занырнула в глубь и достала красный камешек, что блестел на дне."
    play sound sfx_water_emerge
    "Рассмотрев его, она показала камень Константину.{w=1} В ответ он лишь улыбнулся и брызнул в Рену водой."
    hide image re_smile_swim
    show image re_laugh_swim
    with byso
    ren "Ах ты брызгаться!"
    scene bg ext_beach_day
    show image re_laugh_swim
    with fade
    "После обмена брызгами, они вышли на берег и сели на полотенце, что Рена принесла из домика."
    kt "Давно мне не было так весело купаться.{w=1} Словно в раннее детство вернулся."
    hide image re_laugh_swim
    show image re_smile_swim
    with byso
    ren "Это уж точно.{w=1} Так бы каждый день..."
    "Рена положила ладонь на руку Константина."
    kt "Романтично.{w} Только были бы мы в этом лагере одни.{w=1} Никаких тебе пионерских мудрёностей, Генд и кибернетиков."
    "Поводив рукой по песку, она c улыбкой вздохнула."
    ren "Ну что поделать.{w=1} Благо сейчас нам ничего из этого не мешает хорошо провести день у пляжа."
    kt "Действительно..."
    "Купаясь и отдыхая вместе, они даже и не заметили, как подкрался вечер."
    kt "Как бы то не хотелось, но уже вечер.{w=1} Пора переодеваться."
    ren "Ладно.{w}.. А так не хочется уходить отсюда..."
    kt "Завтра ещё вернёмся."
    hide image re_smile_swim
    show image re_laugh_swim
    with byso
    stop music fadeout 3
    "Рена утвердительно кивнула и они направились переодеваться."
    hide image re_laugh_swim
    scene bg black
    with byso
    "Войдя в кабинки, они быстро переоделись."
    scene bg ext_beach_day
    show image re_smile_pioneer
    with byso
    kt "Мы же забыли проверить стабильность, точно."
    hide image re_smile_pioneer
    show image re_sad_pioneer
    with byso
    "Рена достала из мешка синий телефон и передала Константину."
    play sound sfx_radio_squelch_1
    "Константин включил телефон и набрал номер. Ему ответил уже знакомый мужской голос."
    gt "Происходит замер.{w=1} Пожалуйста ожидайте."
    kt "Ну пожалуйста, будь больше 75..."
    gt "Стабильность составляет 87,5 процентов"
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Вот это замечательно!"
    kt "Да, порядок, пионер наколдовал.{w=1} Идем!"
    "Константин положил телефон в карман и махнул Рене."
    play ambience ambience_ext_road_evening
    hide image re_smile4_pioneer
    scene bg ext_playground_day
    show image re_smile_pioneer at right
    show us grin pioneer far at left
    with byso
    play music music_list["silhouette_in_sunset"]
    "У поля они вновь встретили Ульянку, что махала им рукой."
    hide us
    show us smile pioneer at left
    with byso
    us "Я достала. {w}Вот этот чертёж.{w=1} Давайте посмотрим, мне уже не терпится!"
    play sound sfx_paper_bag
    "Константин взял бумагу у Ульяны и развернул этот лист."
    kt "Какой ужас!"
    hide image re_smile_pioneer
    show image re_smile3_pioneer at cright
    show us surp1 pioneer at cleft
    with byso
    play sound sfx_paper_bag
    "Проговорил Константин и начал хохотать. {w}Рена взяла у него чертёж и вместе с Ульянкой начала его разглядывать."
    ren "Робот-кошкодевочка?{w=1} Даже и не догадывалась, что их тянет на девочек."
    us "О, да это же из той самой легенды про загадочную девочку!"
    hide image re_smile3_pioneer
    show image re_smile_pioneer at cright
    with byso
    "Константин отсмеялся, а Рену заинтересовали слова Ульяны."
    ren "Что за легенда?"
    show us laugh2 pioneer at cleft with byso
    us "Да это ещё пару смен назад был мальчик по имени...{w=1} Матвей вроде.{w}.. Так вот он всем всерьёз утверждал, что она существует и потом просто пропал среди ночи."
    us "Его искали дней 10, но так и не нашли. {w=1}Говорят, что его эта девочка и украла."
    th "Пропал среди ночи...{w=1} Хотя скорее всего просто лагерная легенда."
    us "А эти видимо решили народ попугать этим роботом."
    kt "Понятно.{w=1} Ну во всяком случае, спасибо что рассказала."
    us "Да ничего.{w=1} Скоро ужин, не опаздывайте."
    hide image re_smile_pioneer
    show image re_smile2_pioneer at cright
    with byso
    ren "А ты что?"
    show us laugh pioneer at cleft with byso
    us "А мне надо бесследно вернуть это кибернетикам, чтоб обо мне никто не подумал.{w=1} Не хочу вас подставить."
    ren "Тогда хорошо, спасибо тебе."
    us "Ерунда!"
    hide us with byso
    "Ульяна хихикнула и убежала."
    stop music fadeout 3
    kt "Пионер пропал среди ночи.{w=1} Напоминает нашего призрачного знакомого."
    hide image re_smile2_pioneer
    show image re_serious2_pioneer at cright
    with byso
    ren "Я тоже об этом подумала.{w=1} Надо сегодня у него спросить."
    "Пожав плечами, они направились дальше к домику."
    hide image re_serious2_pioneer
    scene bg int_house_of_kt_day
    show image re_smile2_pioneer
    with fade
    play sound sfx_dinner_horn_processed
    stop ambience
    "Развесив вещи, они услышали горн, который зазывал на ужин."
    kt "Вот и ужин, как раз аппетит появился."
    hide image re_smile2_pioneer
    show image re_smile3_pioneer at cright
    with byso
    stop music fadeout 3
    ren "Тогда идём, нас еще вожатая хотела видеть."
    hide image re_smile3_pioneer
    scene bg ext_square_sunset
    show cs normal at right
    show image re_smile2_pioneer at left
    with fade
    play ambience ambience_ext_road_evening
    play music music_list["smooth_machine"] fadein 1
    "Выйдя на площадь, они встретили Виолу."
    show cs shy at right with byso
    cs "Добрый вечер, пионеры.{w}.. Как там ваши водные процедуры?"
    kt "Добрый.{w=1} А откуда вы знаете?"
    hide image re_smile2_pioneer
    show image re_smile4_pioneer at left
    with byso
    cs "Да там один мальчик поранился, я по дороге и на пляж зашла, а там вы воркуете."
    "Покраснев протянула медсестра."
    ren "А это запрещено?"
    "Шутливо ответила Рена.{w=1} Виола с улыбкой посмотрела на Рену."
    show cs smile at right with byso
    cs "Нет, почему.{w=1} Просто не забывайте предохраняться."
    "Загадочно прошептала Виола и ушла."
    hide cs with byso
    kt "Очень смешно.{w=1} Да только мне острое нельзя."
    "Уныло пробурчал Константин и пошёл с Реной дальше."
    play ambience ambience_dining_hall_full
    hide image re_smile4_pioneer
    scene bg int_dining_hall_people_sunset_cust
    with byso
    "В столовой уже было людно.{w=1} Большая часть столов была занята.{w} На удивление Константина Толик сидел с Мику и более не претендовал на его место."
    "Обычным смертным подавали рис с куриной грудкой, а так же компот из сухофруктов."
    "А вот наставникам была жареная картошка с той же грудкой, обжаренной в масле.{w=1} Напитком был клубничный кисель."
if event1 == 1:
    $ event1 -= 1;
    kt "Можно мне ещё один стаканчик киселя. Я тут немного проиграл спор, потому должен."
    "Повариха улыбнулась и налила еще один стаканчик."
    kt "Спасибо большое."
    pov "Пожалуйста."
    "Ответила повариха и стала накладывать еду следующему по очереди."
    "Константин заметил Ульянку и подошёл к её столику. Рена пошла за ним."
    show us normal pioneer at right
    show dv sad pioneer2 at left
    with byso
    kt "Вот, как и обещал."
    show dv surprise pioneer2 at left with byso
    "Константин поставил Ульяне на поднос стакан киселя."
    show us laugh pioneer with byso
    us "Спасибо, настоящий друг!"
    "Алиса лишь открыла рот, не особо понимая ситуацию."
    hide dv
    hide us
    show image re_smile2_pioneer
    with byso
    "Константин сел за свой столик вместе с Реной."
    ren "Молодец, долгов не забываешь."
    "С приятной улыбкой подметила Рена."
    kt "Никогда не забывал.{w=1} Что должен, то возвращаю."
    ren "Я знаю."
    jump vnjpfpvnfdsvjfdspvfods
else:
    "Константин поблагодарил повариху за еду и вместе с Реной направился за свой столик."
    show image re_smile2_pioneer
    with byso
    jump vnjpfpvnfdsvjfdspvfods
label vnjpfpvnfdsvjfdspvfods:
    kt "Приятного аппетита."
    ren "Тебе тоже."
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    "Ответила Рена и преступила к трапезе."
    show mt smile pioneer at left with byso
    "Спустя 5 минут к ним подошла вожатая."
    mt "Вновь приятного аппетита.{w=1} Как провели день?"
    kt "Водные процедуры на пляже освежают как никогда.{w=1} Вы хотели нам что-то поручить?"
    show mt grin pioneer at left with byso
    mt "Да.{w=1} Вам нужно попросить у Мику один музыкальный инструмент для Виолы.{w} Она сегодня хочет немного разбавить сегодняшнюю дискотеку живой музыкой."
    hide image re_smile4_pioneer
    show image re_sad_pioneer
    with byso
    ren "Какой инструмент нам нужен?"
    mt "Мику уже в курсе.{w=1} Просто скажите что это для Виолы."
    kt "Хорошо, будет сделано."
    show mt smile pioneer at left with byso
    mt "Прекрасно.{w} Так-же не забудьте нарядится для дискотеки.{w=1} Сегодня будут танцы."
    kt "Принято."
    mt "Тогда ужинайте и ждите Мику у клуба.{w=1} Её музыкальный номер провалился, потому она в наказание будет сегодня намывать клуб.{w} Ещё раз приятного аппетита."
    hide mt
    hide image re_sad_pioneer
    show image re_smile4_pioneer
    with byso
    stop music fadeout 3
    "Закончив трапезу, они сдали тарелки и пошли к музклубу."
    hide image re_smile4_pioneer
    scene bg ext_square_sunset
    show image re_smile3_pioneer
    with byso
    play ambience ambience_ext_road_evening
    ren "Вот занятный вопрос."
    kt "Какой?"
    hide image re_smile3_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Вожатая пойдёт, скажет Мику, отправит нас, а мы и принесём."
    ren "Почему не сказать Виоле, чтоб сама пошла и взяла?"
    kt "Чудеса людской лени, что сказать."
    hide image re_smile2_pioneer
    show image re_smile_pioneer
    with byso
    ren "Да тут вовсе не о лени, а просто о феноменальной тупости, как по мне."
    ren "Ей же меньше делать."
    kt "Да слушай, она и в офисе сообразительностью не отличалась.{w=1} Что уж тут..."
    kt "Регулярно путала бумаги, а начальнику хоть бы хны.{w=1} Всё Брусков."
    ren "М-да, что уж делать, в семье не без урода."
    kt "Да они там все были уроды..."
    play ambience ambience_ext_road_evening
    play music music_list["silhouette_in_sunset"]
    hide image re_smile_pioneer
    scene bg musclub
    show image re_happy_pioneer
    with byso
    "Мику ещё не вернулась, так что они решили сесть на ступеньки у музклуба."
    "Рена положила голову на плечо Константина."
    ren "Никогда до этого не видела такой природы.{w} Тепло, приятно, рядом пляж, птицы поют, цикады сверчат."
    ren "Если бы не все прошлые обстоятельства, то не это ли рай?"
    kt "Как говорил мне Генда, он отправит меня в рай становиться лучше. Может это и работает."
    kt "А не видела потому что Рома у меня дедушкину дачу отсудил."
    hide image re_happy_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Это в прошлом.{w=1} Теперь у нас есть настоящее и возможно будущее."
    play sound glad
    "Рена погладила Константина по плечу."
    ren "Я...{w} Разрежу...{w} Надвое себя..."
    ren "Создам из плоти новый мир...{w} Где нет тебя..."
    ren "Пусть всё пылает...{w} Пламенем костра..."
    ren "Мне надоело...{w} Любовь...{w} Вот и я."
    show mi normal pioneer at right
    show image tl_normal at left
    hide image re_smile2_pioneer
    show image re_bored_pioneer
    with byso
    "На горизонте явилась Мику с Толиком, что уныло о чём то говорили."
    hide image tl_normal
    show image tl_angry at left
    with byso
    "Завидев Константина, Толик скорчил недовольную мину."
    show mi smile pioneer at right with byso
    mi "Вы за инструментом Виолы?"
    kt "Верно.{w=1} Он же у тебя?"
    mi "Да, сейчас вынесу."
    "Пробормотала Мику и начала открывать дверь музклуба."
    hide image tl_angry with byso
    hide mi with byso
    play sound door_cl
    "Открыв, она пропустила Толика, а потом зашла сама."
    hide image re_bored_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Дамы вперёд."
    "С усмешкой шепнула Константину Рена.{w=1} Константин прыснул со смеху."
    hide image re_smile4_pioneer
    show image re_bored_pioneer
    show mi normal pioneer at right
    with byso
    "Мику вышла, вытащив что-то вроде гитары."
    mi "Вот, держите, всё настроено как надо."
    "Рена взяла инструмент и осмотрела его."
    ren "Ну смотри.{w=1} В случае чего, проблемы будут у тебя."
    "Презрительно подметила Рена."
    mi "Всё хорошо, не беспокойся.{w=1} Я всё проверила."
    kt "Прекрасно, если так."
    hide mi
    hide image re_bored_pioneer
    scene bg ext_square_sunset
    show image re_smile_pioneer
    with byso
    "Заключил Константин и встал со ступенек. {w=1}Рена встала вместе с ним и они пошли в медпункт."
    kt "Не знаю почему, но мне кажется, что они могли чем-то насолить."
    hide image re_smile_pioneer
    show image re_bored_pioneer
    with byso
    ren "Мне тоже так кажется.{w} Ну, мы просто курьеры, так что проблема будет не наша."
    "Ответила Рена, пожав плечами."
    show cs normal far at left with byso
    "У Генды стояла Виола, что явно ожидала своей гитары."
    show cs smile at left with byso
    cs "А вот и вы. Спасибо, пионеры."
    hide image re_bored_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Рады помочь."
    cs "Идите, скоро дискотека.{w} Не пропустите моё соло."
    hide cs with byso
    "С улыбкой напомнила Виола и пошла в медпункт."
    stop music fadeout 3
    kt "Ну что, финальное приготовление?"
    hide image re_smile2_pioneer
    show image re_smile4_pioneer
    with byso
    ren "Ага..."
    "Шурик сидел и ковырялся в конструкции стола."
    kt "Он там что, стол повторно паяет?{w} Весь день что-то ковыряет."
    hide image re_smile4_pioneer
    show image re_smile_pioneer
    with byso
    ren "Кибернытики, что с них взять."
    hide image re_smile_pioneer
    scene bg int_house_of_kt_day
    show image re_serious_pioneer
    with fade
    play music music_list["meet_me_there"] fadein 3
    play sound door_cl 
    stop ambience
    "Дойдя до домика, она открыла шкаф."
    "Рена достала из шкафа своё платье и беретик, а так же протянула Константину коричневую рубашку."
    hide image re_serious_pioneer
    show image re_smile2_pioneer
    with byso
    ren "Вот тебе подарочек.{w=1} Надеюсь тебе понравится."
    play sound sfx_blanket_off2
    "Константин принял подарок и расправил эту рубаху."
    kt "Неплохо, сейчас примерим."
    "Рубашка идеально подходила Константину и немного даже красила."
    hide image re_smile2_pioneer
    scene bg d2_kt
    with byso
    "Встав пред зеркалом он начал осматриваться."
    th "Неплохо.{w=1} Давно не носил ничего такого удобного."
    kt "Спасибо, мне нравится!"
    "Рена подошла к нему и посмотрела с ним в зеркало."
    ren "Красавчик!"
    "Прошептала она и обняла его сзади."
    kt "Ну что, пора?"
    ren "Идём!"
    "Указала Рена и вышла из домика."
    th "Давно я не ходил на такие свидания."
    "Подумал он про себя и вышел за Реной."
    scene bg ext_houses_night with byso
    play sound door_cl
    play ambience ambience_ext_road_night
    "На улице стемнело. Константин закрыл дверь на ключ."
    scene bg ext_square_night_party
    show image re_kind_casual
    with fade
    stop music fadeout 3
    "На площади мерцали огоньки, всё выглядело атмосферно и приятно.{w} Даже статуя Генды не была похожа на чудище."
    ren "Красиво. Не зря очкарик ковырялся в этих приборах."
    kt "Сложно это говорить, но хоть на что-то он способен."
    hide image re_kind_casual
    show image re_grin_casual
    with byso
    "Из динамиков раздался голос вожатой."
    mt "Доброго вечера, пионеры и пионерки из разных отрядов."
    mt "Сегодня у нашего лагеря годовщина. Дискотека объявляется открытой."
    play music sanari
    play sound sfx_concert_applause
    "Раздались аплодисменты толпы и заиграла музыка."
    hide image re_grin_casual
    show image re_kind_casual
    with byso
    "Рена пустилась в пляс.{w=1} Константин тоже не смог долго стоять на месте и присоединился."
    "Обычно, музыка раздражала Константина.{w} Для него множество людей, танцующих под неё были лишь стадом, но в этот день и он сам был в танце."
    "Причиной тому была она - Рена.{w} Единственная родственная душа среди этих людей."
    "Рена.{w} Добрая и отзывчивая, но при том холодная и временами жестокая.{w=1} Несмотря на то, что она личность противоречивая и непостоянная, Константину это нравилось."
    "Его аморальные и неприятные множеству выборы послужили формированию её личности."
    "Все неудачи и плевки в спину Константина со стороны судьбы тоже оставили след в личности Рены."
    "Для неё Константин является всем.{w} Именно благодаря ему она не потерялась в множестве миров Генды и вообще начала своё существование."
    "Хоть Рена формально не человек, но для Константина это и есть самая настоящая человеческая душа."
    "Искренняя и тонкая. Со всеми человеческими склонностями и недостатками.{w=1} Душу нельзя пощупать, измерить, взвесить или запротоколировать.{w=1} Её можно только почувствовать."
    "Рена чувствовала душу Константин и способна поменять в нём многое."
    "Но это зависит лишь от него."
    stop music fadeout 3
    "Спустя некоторое время музыка прекратилась и вновь раздался голос Ольги."
    play music music_list["farewell_to_the_past_full"]
    mt "А сейчас объявляется белый танец.{w=1} Девушки приглашают кавалеров."
    "После этих слов, Рена без каких-либо раздумий подошла к Константину."
    ren "Станцуем?"
    kt "Давай..."
    hide image re_kind_casual
    scene bg re_dance
    with byso
    "Они принялись танцевать под ритм вальса."
    "Несмотря на большую людность на площади, помимо них было лишь 4-5 пар, что танцевали с ними рядом."
    "Эти минуты что для Рены, что для Константина были незабываемы.{w=1} Они кружились в танце, совершенно не обращая внимания на окружающих."
    "Несмотря на то, что их движения были не идеальны, они работали максимально синхронно, словно они как зеркальное отражение одного человека."
    "Как чёрное и белое."
    "Как инь и янь."
    "Образец истинной гармонии и завершённости."
    "Многие смотрели с завистью на танцующих, но последним вовсе не было дела."
    "Танец словно сливал души в один сосуд, где они чувствовали друг друга как нельзя хорошо."
    scene bg ext_square_night_party
    show image re_kind2_casual
    with byso
    "Музыка затихла.{w} Константин и Рена нехотя отлипли друг от друга и поцеловались."
    "Это вызвало ажиотаж у всех наблюдателей, но ни Рене ни Константину не было до этого дела."
    hide image re_kind2_casual
    show image re_smile_casual
    with byso
    mt "А теперь выступит наша любимая Виола в своём соло на гитаре."
    "Вышла Виола, одетая в тесное платье и приличным количеством макияжа."
    "Она начала играть.{w=1} Все дружно принялись танцевать, в том числе и Константин с Реной."
    "Соло не длилось долго.{w} Как оно закончилось, Рена взяла за руку Константина и потянула за собой."
    hide image re_smile_casual
    show image re_kind2_casual
    with byso
    ren "Идём прогуляемся?"
    kt "Хорошо."
    stop music fadeout 3
    "Без малейших возражений ответил Константин."
    hide image re_kind2_casual
    scene bg ext_boathouse_night
    show image re_kind2_casual
    with byso
    play ambience ambience_boat_station_night
    play music umted
    "Они вышли на пирс, где сели на край."
    hide image re_kind2_casual
    show image re_smile2_casual
    with byso
    ren "Я даже и не знаю что сказать..."
    kt "Что такое?"
    ren "Я никогда не ощущала себя так прекрасно.{w=1} Этот день был первым, что пролил свет на смысл моего существования.{w} Я поняла, что не смотря на всю жестокость жизни и её развратность, есть и такие моменты, ради которых стоит продолжать существовать."
    ren "Такие моменты как этот день.{w} Я проснусь и увижу тебя.{w=1} Могу тебя почувствовать, обнять.{w=1} Ты меня устроил в этот клуб, провёл со мной весь день в разных интересных и весёлых, несмотря на некоторые моменты, ситуациях."
    ren "И вот сейчас я сижу и понимаю.{w=1} День подходит к концу и не понятно, что будет завтра."
    "Константин взглянул в небо."
    kt "А это наверное и к лучшему, что мы не знаем что нас ждёт."
    kt "Завтра всё может быть куда лучше.{w=1} Это место... Оно странное."
    kt "С одной стороны это моя тюрьма надолго, но я тут прекрасно провожу время."
    kt "Провожу время с человеком, что действительно меня любит.{w=1} С тобой, Рена."
    kt "И я готов пожертвовать всю свою жалкую прошлую жизнь ради таких моментов."
    hide image re_smile2_casual 
    show image re_kind2_casual
    with byso
    "Рена поцеловала Константина."
    hide image re_kind2_casual
    show image re_kind_casual
    with byso
    ren "Я тебя люблю. Ты и есть смысл моего существования.{w} Я готова на всё ради тебя, лишь бы тебе было хорошо..."
    window hide
    menu:
        "Ответить взаимностью.":
            $ renpy.block_rollback()
            kt "Это взаимно.{w=1} Хоть я в своё время и отвернулся от тебя, но теперь осознал свою неправоту."
            kt "Я думал что брехня всё это и мне придётся пробыть всю свою жизнь в одиночестве."
            kt "И теперь у меня есть надежда на то, что я буду всегда с тобой."
            "Рена обняла Константина изо всех сил."
            ren "Люблю тебя.{w}.. Ты только мой и я тебя никому не отдам!"
            ren "Ни при каких условиях."
        "Промолчать.":
            $ renpy.block_rollback()
            ren "Надеюсь ты такого-же мнения."
            "Рена обняла Константина."
            ren "Ты только мой и я никому тебя не отдам."
    hide image re_kind_casual
    show image re_angry2_casual
    with byso
    stop music fadeout 3
    mt "А что вы тут делаете?"
    show mt angry dress at right with byso
    "Позади раздался недовольный голос вожатой."
    th "Опять ты всё портишь!"
    kt "Сидим и смотрим на звёзды.{w=1} Решили отойти от шума дискотеки."
    mt "Надо было предупреждать, что вы отошли. {w}Срочно на площадь, сейчас будет небольшой наградительный огонёк."
    hide mt
    hide image re_angry2_casual
    show image re_bored2_casual
    with byso
    "Поучительно проговорила вожатая и пошла обратно к площади."
    play music music_list["reflection_on_water"]
    ren "Ладно, что поделаешь, надо идти."
    kt "Как бы не хотелось тут остаться, но всегда найдётся тот, кто испортит такой момент."
    hide image re_bored2_casual
    play ambience ambience_ext_road_night
    scene bg ext_square_night_party
    show image tolpa at cright
    show image tolpa2 at cleft
    show image re_bored_casual at cright
    with fade
    "На площади все встали вокруг Ольги с микрофоном.{w=1} Рена и Константин были в задних рядах."
    mt "Итак, сейчас у нас небольшая церемония награждения. {w}Награждаются самые активные и опрятные пионеры совёнка."
    mt "Первая, кого я хотела бы поблагодарить от имени всего наставнического состава."
    kt "Не всего."
    hide image re_bored_casual
    show image re_kind2_casual at cright
    with byso
    "Под нос пробубнил Константин.{w=1} Рена ухмыльнулась."
    mt "Славяна.{w=1} Самая главная помощница всего лагеря.{w=1} Уже на протяжении нескольких смен она помогает всем отрядам и всему персоналу лагеря."
    "Вышла Славя, которой вручили грамотку и немного конфет.{w=1} Все вокруг стали аплодировать."
    sl "Спасибо большое."
    mt "Следующей, кого я бы хотела наградить за усердную работу в клубе."
    mt "Елена.{w=1} Она помогала в библиотеке и писала самые занимательные стенгазеты."
    "Из строя вышла Лена, что была готова упасть в обморок от неловкости.{w=1} Снова зашумели аплодисменты."
    "Ей вручили то же, что и Славе."
    "Лена молча вернулась в толпу."
    th "М-да, как же интересно всё это слушать."
    hide image re_kind2_casual
    show image re_bored_casual at cright
    with byso
    kt "Со скуки подохнуть можно..."
    ren "А то..."
    "Подтвердила Рена и устало зевнула."
    "Вожатая продолжала оглашать список наград, из рядов выходили пионеры из разных отрядов и получали грамоту с горстью конфет."
    "Константин уже был готов уснуть на месте, как вожатая закончила раздавать награды."
    mt "Вот и все награждённые.{w} Если вы хотите иметь такую-же почётную грамоту, то работайте, учитесь и меняйтесь, как говорит наш вождь Генда."
    th "Так эта морда себя ещё и на место Сталина и Ленина поставила.{w=1}.. Высокомерию нет предела."
    mt "А сейчас все расходитесь по домикам.{w=1} Скоро отбой."
    kt "Наконец-то..."
    hide image re_bored_casual
    show image re_kind2_casual
    with byso
    mt "Напомню, что кибернетики и члены музклуба остаются убирать площадь."
    "Рена хихикнула."
    ren "Будут знать, как пререкаться.{w=1} Пойдём в домик?"
    kt "Это точно.{w=1} Пошли."
    stop music fadeout 3
    "Рена взяла Константина под руку и они пошли к домику."
    hide image re_kind2_casual
    scene bg int_house_of_kt_night
    with byso
    play sound door_cl
    play music proshloe
    stop ambience
    "Открыв дверь домика, они зашли внутрь."
    "Константин снял нарядную рубаху и повесил её в шкаф.{w} Рена сняла платье и берет, повесив их рядом."
    "Константин лёг в постель.{w} Рена выключила свет и легла к нему. Он чувствовал тепло её тела и её дыхание."
    ren "Эх ты, куряга.{w=1} Весь куревом провонял."
    play sound glad
    "Съязвила Рена, разворошив волосы у Константина на голове."
    kt "Кто-б говорил."
    "С едко ответил Константин."
    ren "Спасибо тебе за этот день.{w=1} Ты сделал лучшим за время моего существования."
    kt "Завтра всё может быть лучше, поверь.{w=1} У нас еще несколько дней впереди!"
    ren "Это хорошо.{w=1} Поставь на телефоне будильник."
    kt "Зачем?"
    "Рена усмехнулась."
    ren "Если вожатая увидит нас в одной постели, сам понимаешь что будет."
    kt "Ну да, это верно.{w=1} На 7 ставить?"
    ren "Да, ставь."
    play sound2 sfx_lock_close
    play sound sfx_blanket_off2
    "Константин поставил будильник, положил телефон на стол и поделился с Реной одеялом."
    kt "Укутайся, а то холодно будет."
    ren "Спасибо.{w=1} Ты заботливый..."
    "Рена поместилась под одно одеяло с Константином.{w=1} Они были лишь в паре сантиметров друг от друга."
    ren "Ладно, пора спатеньки.{w=1} Удачного кошмара, любимый."
    kt "Спасибо тебе тоже."
    play sound glad
    "Рена провела рукой по щеке Константина и устроилась поудобнее."
    show blink
    stop sound fadeout 1
    stop music fadeout 3
    "Константин закрыл глаза и заснул."
    show image so_sm
    show unblink
    play music music_list["sunny_day"]
    "Отрыв глаза, он вновь встретил Генду."
    gg "Вставай-вставай."
    th "М-да.{w=1} А как я мог забыть..."
    "Константин сидел на кресле перед столиком и креслом побогаче."
    gg "В честь годовщины сегодня я тебя шибко мучить не буду, праздник как-никак.{w} Просто хочу с тобой поговорить."
    kt "Не о чем мне с тобой говорить!"
    hide image so_sm
    show image so_gd
    with byso
    gg "Уж нет. Я сказал есть, значит есть!"
    "Таким же тоном ответил Генда."
    scene bg cafe
    hide image so_gd
    show image so_sm
    with byso
    "Они очутились в кафе, где у Константина был выпускной."
    gg "Знакомое местечко, да?"
    kt "И чё тебе от меня надо?"
    hide image so_sm
    show image so_gd
    with byso
    play sound sfx_face_slap
    "Генда влепил Константину леща."
    gg "Не говори, когда не просят, какой раз повторяю!"
    kt "Ага, а может тебе ещё кофе сварить?"
    hide image so_gd
    show image so_sm
    with byso
    gg "Было бы неплохо, но нет."
    "С усмешкой ответил Генда, наливая себе стакан воды."
    gg "Давай поговорим как человек с человеком.{w=1} Хоть на вы, как ты и хотел пару дней назад."
    kt "Упустим этот момент."
    "Генда сел напротив и налил стакан воды Константину."
    gg "Вот видишь, совсем не сложно быть вежливым.{w=1} Как тебе лагерь?"
    "Рука Константина освободилась и он хлебнул воды."
    kt "А ты будто не знаешь..."
    hide image so_sm
    show image so_gd
    with byso
    gg "Не поверишь, но нет. Так бы не спрашивал.{w} Мир хоть и принадлежит мне, но у меня и без того дел достаточно."
    th "Дела-дела...{w=1} Ну-ну, какие дела у <<Божественной самости>>."
    kt "И какие же дела?"
    "Генда поправил очки."
    gg "Не твоего ума дело.{w=1} Есть значит есть."
    kt "Вежливость, ну-ну."
    "Генда пропустил колкость мимо ушей."
    gg "Поменялось ли что-то в твоей жизни?"
    "Константин почесал затылок и глянул на потолок."
    "Потолок сильно отличался от того что был в их зале на выпускном.{w} Там были рисунки в готическом цвете, выполненные из чёрного и белого мрамора."
    kt "Да, поменялось."
    gg "И как оно чувствуется?"
    th "Не нравится мне тематика этих вопросов."
    kt "Неплохо."
    "Сухо ответил Константин."
    kt "Можно теперь я спрошу?"
    hide image so_gd
    show image so_sm
    with byso
    gg "Ну попробуй."
    "Проговорил Генда, ухмыльнувшись и положив руки на стол."
    kt "Почему я?{w=1} И почему так?"
    gg "А, ты говоришь про то почему именно ты попал сюда?"
    gg "Всё очень просто, у меня есть некоторый списочек.{w=1} Список скота на убой если угодно."
    "Генда размахнул руками."
    gg "Людей в нем порядка 50-100 тысяч.{w=1} Раз в некоторое время я выбираю одного по критерию забытости окружающими раз в некоторое время."
    gg "Ты мне приглянулся.{w} Друзей нет, родственникам на тебя плевать, куда уж там брак, дети и тому подобное."
    gg "Забрать тебя тогда я мог и в лифте.{w}.. Но мне захотелось немного протестировать твою психику."
    kt "То есть..."
    hide image so_sm
    show image so_gd
    with byso
    play sound wood_hit_head
    gg "Не перебивай!"
    "Приказал Генда и стукнул по столу кулаком."
    gg "Компания в которой ты работал была в достаточной степени бесполезной для общества.{w} Мне давно хотелось от неё избавиться.{w=1} Сколько людей из списка она отправила в никуда."
    "Генда снял очки и начал протирать о свой халат."
    gg "<<Полимер>> не переживёт дурной славы и потери целого штата сотрудников в честь чего и будет закрыт по долгам."
    gg "Сейчас считай у тебя курс психотерапии по моей личной методике.{w=1} В целом я ответил на твой вопрос.{w=1} Теперь я продолжу."
    "Генда вернул очки себе на нос."
    gg "Чувствуешь ли ты потерю своей предыдущей жизни?"
    kt "Нет, не то что бы."
    hide image so_gd
    show image so_sm
    with byso
    "Мужчина удивился и вдвое сильнее заинтересовался диалогом."
    gg "Хорошо.{w=1}.. Почему?"
    "Константин потёр подбородок и облокотился на стол."
    kt "В прошлой жизни я так и искал смерти.{w=1} У меня не было перспектив и воли.{w=1} Теперь у меня есть луч надежды."
    gg "Прекрасно! Твой отзыв учтён.{w} Правда... Тебе всё равно в кошмар."
    show blink
    pause 0.5
    hide image so_sm
    scene bg black
    stop music fadeout 2
    "Кресло из под Константина пропало и он упал на пол."
    scene bg int_house_of_kt_night
    show unblink
    play music nightmare
    "Константин моргнул и очутился в домике.{w} Рены рядом не было."
    th "Это было...{w=1} Странно..."
    "На столе лежала катана и записочка."
    play sound sfx_paper_bag
    th "Я и пионер ждём тебя там же, где заброшка.{w=1} Постарайся быстрее, гончие не дремлют. Второй этаж налево."
    th "Понятно..."
    "Константин вынул катану из ножен, она была изрисована тёмной завивающейся полосой. Лезвие оказалось серебристым, чистым и необыкновенно лёгким."
    "Кроме этого, Константин сразу увидел, что заточка была весьма качественная. В металлической поверхности клинка можно было увидеть своё отражение."
    play sound door_cl
    scene bg ext_houses_night with byso
    "Уложив катану обратно, он вышел из домика."
    scene bg ext_path2_night with byso
    play sound monster_sfx volume 0.5
    play sound2 sfx_bones_breaking volume 0.5
    play sound3 krik volume 0.5
    "С площади доносились ужасные звуки.{w} Хруст костей, крики и рыки монстров."
    "Константин побежал что было сил в старый корпус."
    scene bg ext_old_building_night_moonlight with byso
    "Дорога обошлась без встреч со всякими нежелательными существами, потому он добрался туда быстро."
    scene bg int_old_building_night with byso
    stop music fadeout 2
    "Войдя туда его встретила поломанная лестница на второй этаж.{w} Константин поднялся на второй этаж и зашёл налево."
    play music the_date_of_death
    show image poter_n at left
    show image re_dontlike_casual at right
    with byso
    "В комнате почти в полной темноте сидела Рена, напевая любимую песню Константина и напротив её пионер стоял и курил в окно."
    hide image re_dontlike_casual
    show image re_kind_casual at right
    with byso
    ren "Молодец!{w=1} Я верила в тебя."
    pp "И снова здравствуй."
    "Устало проговорил призрак и выкинул бычок в окно."
    kt "Привет.{w=1} Есть новые вести?"
    pp "Как не странно, но да. При том достаточно много."
    hide image re_kind_casual
    show image re_kind2_casual at right
    with byso
    ren "Рассказывай."
    pp "Ваш цикл уникален.{w=1} В нём всё совершенно другое, относительно циклов с Семёнами."
    pp "Схемы с Семёнами являются проверенными временем и редко случаются ошибки."
    "Пионер достал пачку сигарет и достал 3 сигареты."
    kt "Спасибо."
    hide image re_kind2_casual
    show image re_smile_casual at right
    with byso
    ren "Благодарю."
    play sound inh
    play sound2 schelk
    "Поджёг он все три щелчком пальцев."
    pp "Ошибки в сценарии заставляют программу работать неправильно и непредсказуемо."
    pp "Генда создал кошмар и зря. Он так и желает проникнуть в реальный мир."
    pp "Первый был Миша.{w} Я тут в следствии второй ошибки.{w=1} Рена тут в результате третьей."
    pp "Между тем, Рома тоже игрок как выяснилось, но его память аккуратно подтёрта."
    pp "То есть он может как и вспомнить прошлое, так и стать пустышкой как и остальные члены симуляции.{w=1} Что-то между тем и тем."
    kt "А что есть парадокс?"
    pp "Просто говоря, огромная ошибка симуляции.{w} Грань между лагерем и кошмаром сотрётся.{w=1} Будет катастрофа, что в редких случаях выходит и на другие симуляции.{w} Мясорубка."
    pp "И если так выйдет, то с приличной вероятностью наши души как и души всех обитателей будут удалены, словно вирус."
    pp "Все мы просто умрём и потеряемся в бесконечной тьме."
    pp "Так и вышло с Мишей.{w=1} Его больше не существует."
    hide image re_bored_casual
    show image re_sad_casual at right
    with byso
    ren "Неприятно..."
    pp "Что касается стабильности."
    "Пионер выкинул бычок. Рена и Константин сделали так же."
    pp "Мне получилось залатать пару дыр.{w=1} Стабильность выросла."
    pp "Так что аккуратно.{w=1} Не дайте симуляции обрушиться, пока я что-нибудь не придумаю."
    pp "Помочь мне вам пока нечем и незачем, так что пока что можете отдохнуть в меру возможности."
    kt "Хорошо, мы поняли."
    kt "Если о странностях.{w=1} Генда сегодня отказался от пыток."
    "У пионера глаза вылезли на лоб.{w=1} Рена ничего не понимая почесала затылок."
    pp "Чего?"
    ren "Какие пытки?"
    pp "Генда терзает каждую ночь некоторых игроков.{w=1} Таких как я и Константин.{w=1} Про тебя он скорее всего просто не знает."
    "Рена погрустнела."
    ren "Ну и мразь..."
    kt "Короче он хотел со мной поговорить."
    "Константин кратко пересказал сегодняшний диалог."
    pp "Странно.{w}.. Видимо для него ты особенный.{w=1} Я поразмышляю над этим."
    hide image re_sad_casual
    show image re_bored_casual at right
    with byso
    ren "Чего-то сам Генда ментальной стабильностью не отличается..."
    kt "Хрен поспорю..."
    pp "Ладно, думаю на сегодня всё.{w=1} Мне вас вернуть из кошмара?"
    ren "Я не откажусь.{w=1} Не хочу тут находиться."
    kt "Согласен."
    pp "Прекрасно. {w}Про все даже малейшие странности рассказывайте мне. Может это знак.{w=1} К завтрашнему дню я что-то да придумаю."
    ren "Понятно."
    kt "Хорошо."
    "Пионер коснулся Рены и Константина."
    pp "Удачи!"
    show blink
    "Глаза Константина сомкнулись."
    jump d3_withre
