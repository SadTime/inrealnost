label d5_withsopr_liz:
    $ save_name = ('Инреальность.\nEntering troops.')
    play ambience bus_inside volume 0.2 fadein 1
    play music god volume 1 fadein 3
    scene bg int_avtobus2
    with flash
    play sound sfx_mystery_movement volume 0.7
    "Константин сел на заднее сидение и опёрся головой о стекло."
    th "Ну...{w=1} Это пиздец..."
    play sound2 sfx_mystery_movement volume 0.61
    show image oleg_think at left
    show image liz_bukal
    show un surprise pioneer at right
    with byso
    "Лена села на плед, а Лиза напротив."
    liz "Что у вас было?{w=1} Зачем вы этого придурка хомутами закрепили?"
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "Ну он...{w=1} Он вожатую..."
    "Олег пытался пересказать то, что он увидел.{w=1} Константин поднял голову и обернулся."
    kt "Он отравил Сахарову и труп её трахал.{w=1} Вот что Олег хотел сказать."
    hide image liz_bukal
    show image liz_surp
    show un shocked pioneer at right
    with byso
    "На лицах Лизы и Лены застыло странное выражение: что-то между отвращением, ужасом и гневом."
    liz "Ты шутишь чтоль?..."
    un "В-в-всмысле убил?..."
    th "А, то есть, что он труп ебал тебя не смущает?!"
    oleg "Да, так и было...{w=1} Вот я его и закрепил."
    "Олег так это сказал, словно его должно было с минуты на минуту вырвать.{w} Он отвернулся и прикрыл рот рукой."
    kt "Да уж...{w=1} Даже от него я такого не ожидал. Конечная."
    show un sad pioneer at right with byso
    un "Т-так куда мы едем?"
    "По Лене было видно, что она совершенно не понимала что происходит.{w=1} Она была напугана и встревожена."
    hide image liz_surp
    show image liz_smile
    with byso
    liz "Мы едем на базу сопротивления.{w=1} Ты теперь одна из нас."
    show un surprise pioneer at right
    hide image liz_smile
    show image liz_bukal
    with byso
    un "Что? {w=1}К-какое сопротивление?{w} Против кого?"
    kt "Против Генды.{w=1} Мы в инреальности, а не в родном мире.{w} У тебя была другая жизнь."
    show un shocked pioneer at right with byso
    un "Ничего не понимаю...{w=1} Что вам сделал партийный деятель?"
    un "Как вы вообще собрались ему противостоять?{w} Мы в СССР, а не в первобытной общине!"
    kt "Спорно."
    hide image oleg_shy
    show image oleg_angry at left
    with byso
    oleg "Лиза!{w=1} Ты же говорила что она путница.{w} Так почему она ничерта не знает?"
    hide image liz_bukal
    show image liz_angry
    with byso
    "В ответ она прикрыла лицо и тяжело вздохнула.{w=1} Лена тем временем так и сидела, не понимая происходящего."
    liz "Я пыталась ей вернуть память, но не получалось!{w} Не было триггера.{w=1} Она на четвёртом цикле и хрена с два что-то просто так вспомнит!"
    kt "Ты хоть что-то о ней до инреальности знаешь?"
    hide image liz_angry
    show image liz_bukal
    with byso
    liz "Да если бы..."
    show un sad pioneer at right with byso
    un "Я Тихонова Лена!{w} Какая ин-реальность, что вы несёте?!"
    th "Тортик блять несём, что же ещё?"
    play sound2 sfx_paper_bag volume 1
    hide image liz_bukal
    show image liz_normal
    with byso
    "Константин пожал плечами и протянул ей четвёртое писание."
    kt "Держи, ознакомься, может вспомнишь чего."
    play sound2 sfx_paper_bag volume 1
    "Взяв папку, Лена недоуменно её осмотрела и пролистала."
    show un scared pioneer at right with byso
    "Немного посмотрев на первый лист, на её лицо пришёл первобытный ужас."
    un "Макс!{w=1} Так вот что ты говорил!"
    play sound2 sfx_body_bump volume 1
    hide un
    hide image oleg_angry
    show image oleg_shy at left
    hide image liz_normal
    show image liz_dontlike at right
    with byso
    "Выронив писание, она потеряла сознание и распласталась на полу."
    liz "Лена?..."
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Ну вот мы триггер и вызвали..."
    kt "Макс... {w=1}Вспомнила наверное кого-то из прошлой жизни."
    hide image liz_dontlike
    show image liz_bukal at right
    with byso
    liz "Олег, помоги её усадить на кресло."
    play sound2 sfx_mystery_movement volume 0.61
    "Взяв Лену под руки, Лиза и Олег усадили её на кресло напротив связанного Ромы."
    play sound2 sfx_mystery_movement volume 1
    "Закончив с перемещением Лены, они вернулись на плед к Константину."
    kt "М-да...{w=1} Цирк с конями..."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "И не говори!"
    hide image liz_bukal
    show image liz_angry at right
    with byso
    liz "Надо же было так резко её в сознание вернуть!{w=1} Повезло или нет - сложно сказать..."
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Ну, знаешь, если бы мы её в сопротивление привезли без понимания, то с этим было бы куда больше проблем."
    kt "Зато теперь у нас два тела."
    stop music fadeout 3
    hide image oleg_think
    show image oleg_shy at left
    hide image liz_angry
    show image liz_dontlike at right
    with byso
    "Повисло молчание.{w} Олег задумчиво смотрел в окно, а Лиза давала ему время для того, чтобы хоть что-то произнести. {w}Тишину никто не нарушал."
    "Выбивался из тишины только автобус, который в штатном режиме поскрипывал колёсами."
    "Константин неотрывно сверлил взглядом четвёртое писание.{w=1} Красная надпись словно изменила свою насыщенность."
    play music lim volume 1 fadein 3
    hide image oleg_shy
    show image oleg_think at left
    with byso
    "Белые листы продолжали обесцвечиваться. {w=1}Олег заметил это и выпучил глаза."
    oleg "Эй, смотрите!"
    play sound2 sfx_paper_bag volume 1
    pause 0.25
    play sound sfx_paper_bag volume 1
    pause 0.25
    play sound2 sfx_paper_bag volume 1
    "Лиза обратила на это внимание и быстро начала листать содержимое белой папки."
    hide image liz_dontlike
    show image liz_angry at right
    with byso
    liz "Что за херь?!{w=1} Какого чёрта чернила пропадают?!"
    play sound2 sfx_paper_bag volume 1
    "Белая папка окончательно обесцветилась и превратилась в самую обычную бумагу."
    kt "Что это значит?"
    play sound2 sfx_paper_bag volume 1
    hide image liz_angry
    show image liz_bukal at right
    with byso
    "Подняв бровь спросил Константин.{w=1} Лиза отложила папку и задумчиво глянула в окно."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "Не нравится мне это.{w} Как же мы будем новобранцев обучать?"
    hide image liz_bukal
    show image liz_rage at right
    with byso
    liz "Да если мы будем так-же уничтожать симуляции, то вообще не будет у нас никаких новобранцев!{w=1} Мы их сами и перебьём!"
    play sound2 light_inh volume 1
    "Константин тяжело вздохнул и закурил."
    kt "Да ладно тебе срать руководство, Лиз.{w=1} Капитан у нас вроде адекватный человек."
    hide image liz_rage
    show image liz_angry at right
    with byso
    "На эти слова она недовольно фыркнула и отвернулась."
    liz "Он то да, а вот его советчики - нет!"
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Ну да, это в какой-то мере перебор."
    kt "А что, тебе так хочется самой сгнить в инреальности вместе со всем сопротивлением?{w=1} Ух, не думаю."
    stop music fadeout 3
    hide image liz_angry
    show image liz_dontlike at right
    with byso
    "Она подняла бровь и посмотрела на Константина."
    kt "Не знаю как вы, но я бы не хотел дойти до состояния куклы. Лучше я сдохну в борьбе за лучшую жизнь, чем вернусь в то состояние."
    "Затянувшись, он глянул на Лену без сознания.{w=1} Казалось, что она просто спала, но на её лице застыла слабовыраженная эмоция ужаса."
    play music proshloe volume 1 fadein 3
    kt "Пусть это и будет крайне болезненный процесс. Я не боюсь его."
    kt "Я боюсь вернуться в то место, откуда попал в инреальность."
    kt "На мой взгляд, ничего хорошего там не произошло.{w=1} За всю мою сраную жизнь."
    "Олег задумчиво почесал подбородок."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "Я тоже.{w=1} Хоть и не так мрачно смотрю на вещи."
    hide image liz_dontlike
    show image liz_surp at right
    with byso
    liz "Олег, а ты то что?{w} У тебя то чего плохого такого в жизни было?"
    liz "Мне казалось, что ты счастлив был всегда."
    "Он уныло поводил пальцем по пледу и глянул в окошко."
    oleg "Был бы я счастлив, то не сидел бы тут."
    oleg "Я сейчас счастлив.{w=1} Вот у меня друзья, автобус..."
    oleg "Но я не могу сказать, счастлив ли я был раньше.{w=1} Мне почему то казалось что я человек счастливый."
    oleg "А сейчас я понял что был глубоко несчастлив. {w}Причем не только тогда, когда мне было плохо."
    oleg "Когда мы подобрали Костю из той симуляции, я понял что всю жизнь жил в розовых очках.{w=1} Я даже не подозревал, что у людей бывает столько проблем."
    "Константина поразила столь необычная мысль из уст Олега."
    kt "А что случилось то?"
    oleg "Да нет, не в том дело."
    oleg "Просто глядя сейчас на людей, мне кажется я никогда не видел настоящих. {w}Вроде те в целом выглядели счастливее."
    oleg "Я понял, что моя жизнь была ужасна со стороны.{w=1} Бросил школу после 9го, пошёл тренером..."
    hide image liz_surp
    show image liz_sad at right
    with byso
    liz "Да ну, брось ты, Олег!{w} Ты жил куда лучше нас.{w=1} Он - бухгалтер, я кассир в банке.{w} Ты думаешь, это плохо, что ты был счастлив в неведении?"
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Нет, просто мне жаль, что я жил неполноценную жизнь."
    "Константин затянулся и выкинул бычок в открытую форточку.{w=1} Он положил руку на плечо Олегу."
    kt "Да по сравнению с моей, твоя жизнь наверно полноценнее что ли?"
    kt "Ну да."
    kt "Проблемы с работой?{w=1} Нет."
    hide image liz_sad
    show image liz_bukal at right
    with byso
    liz "Проблемы с родственниками?{w=1} Нет."
    kt "Проблемы с собственной нереализованностью?{w=1} Нет.{w} Ты нашёл своё поле и свой уголок в жизни."
    kt "То, что ты сейчас в инреальности - своего рода ошибка."
    play sound2 sfx_put_sugar_cart volume 1
    hide image oleg_think
    show image oleg_smile at left
    hide image liz_bukal
    show image liz_smile at right
    with byso
    "Олег улыбнулся и обнял Лизу и Константина своими большими руками."
    oleg "Вы классные!{w=1} Если и совершать революцию, то только с вами!{w} Мы - вечные революционеры!"
    liz "Так то!{w=1} Вот это уже тот Олег, которого хочет видеть сопротивление!"
    oleg "Ну, кроме Гордона..."
    hide image liz_smile
    show image liz_laugh at right
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    "Все рассмеялись."
    kt "Да и он тоже.{w=1} Ну сцепились вы за плазмоинтергратор, но и чёрт с ним."
    hide image liz_laugh
    show image liz_smile at right
    with byso
    liz "Он любя."
    play sound2 sfx_mystery_movement volume 1
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    "Олег отпустил Константина и Лизу, после чего сел на сиденье."
    oleg "Тогда давайте на этой хорошей ноте приляжем поспать.{w=1} Ехать нам ещё долго."
    hide image liz_smile
    show image liz_normal
    hide image oleg_smile
    with byso
    "Лиза зевнула и потянулась, а Константин пару раз кивнул и сел позади Олега."
    hide image liz_normal
    show image liz_grin at cleft:
        zoom 1.5
        yanchor 0.1
    with byso
    "Она подсела к Константину."
    liz "Плед один. {w=1}Не против?"
    kt "Нет."
    play sound2 sfx_blanket_off2 volume 1
    stop music fadeout 3
    hide image liz_grin
    show image liz_smile at cleft:
        zoom 1.5
        yanchor 0.1
    with byso
    "Лиза села рядом и накрыла Константина пледом."
    show blink
    stop ambience fadeout 1
    "Он закрыл глаза и буквально в миг уснул."
    play ambience ambience_forest_night volume 1 fadein 1
    scene bg ext_polyana_night
    show unblink
    play music umted fadein 3
    "Константин стоял посреди леса."
    "Вокруг была какая-то мертвая тишина, которую нарушало только стрекотание сверчков и шуршание листьев."
    "Он стоял совершенно один, рядом была только высокая береза."
    "Ее ветви образовывали подобие крыши, и сквозь переплетение ветвей просвечивали звезды."
    "Константин поднял глаза и увидел над лесом огромную луну."
    "Незаметно для себя он начал напевать одну песню."
    window hide dissolve
    $ set_mode_nvl()
    "Под холодным дождём за тобой иду,"
    "В раю места нет - мы встретимся в аду,"
    "Из грязи этой шедевр не слепить,"
    "Никому не говори, за что не можешь простить."
    "Сколько ещё, мне мучить себя,"
    "Твои насмешки в памяти храня,"
    "Сколько ещё вслед брошенных фраз,"
    "Оставят лишь шрам но не научат нас."
    ""
    "Мне не больно, нет мне не больно,"
    "В этом мире пустом, я давно погиб,"
    "А ты спи спокойно."
    "Наша история, триллер и драма,"
    "Мы лишь актёры, играем чтоб жить,"
    "Ты пьяна и кричишь, что это достало,"
    ""
    "Но упущен момент, чтобы всё изменить."
    window hide dissolve
    $ set_mode_adv()
    liz "Мне не больно..."
    oleg "Нет мне не больно..."
    kt "В этом мире пустом, я давно погиб."
    liz "А ты спи спокойно."
    show blink
    stop ambience fadeout 1
    stop music fadeout 1
    play sound2 fem_krik volume 1
    "Гармонию прервал женский крик."
    play ambience bus_inside volume 0.21 fadein 1
    scene bg int_avtobus2
    show unblink
    play sound sfx_mystery_movement volume 1
    play music Vl66 volume 1 fadein 3
    "Константин вскочил с сиденья, чем разбудил Лизу."
    show image rm_an
    show un cry pioneer at cright
    with byso
    "В передней части автобуса стоял Рома, с ножом, который он держал на уровне шеи напуганной Лены."
    oleg "Слышь ты!{w=1} Отпустил её живо!"
    hide image rm_an
    hide un
    show image rm_sm2
    show un cry pioneer at cright
    with byso
    "Рома оскалил зубы."
    rm "А то что?{w=1} Напугаешь меня до смерти?!"
    rm "Не двигаться!{w} Либо я ей глотку вскрою!"
    "Все понимали, что он не шутит."
    un "П-помогите..."
    kt "Ты чего добиваешься, придурок?"
    hide image rm_sm2
    hide un
    show image rm_ra
    show un cry pioneer at cright
    with byso
    rm "Я?{w=1} Я выбраться отсюда хочу, вот что!"
    rm "Куда мы едем?!"
    liz "В другую симуляцию.{w} Отпусти Лену и тогда больно не будет!"
    hide image rm_ra
    hide un
    show image rm_an
    show un cry pioneer at cright
    with byso
    rm "Да знаю я вас! {w=1}Опять меня свяжете!{w=1} Хрена с два!"
    "Лиза начала доставать пистолет.{w} Рома это заметил."
    hide image rm_an
    hide un
    show image rm_ra
    show un cry pioneer at cright
    with byso
    rm "А ну руки вверх!{w=1} Или я её прирежу!"
    "Она поняла, что попалась и подняла руки."
    hide image rm_ra
    hide un
    show image rm_an
    show un cry pioneer at cright
    with byso
    rm "Костя, иди тормози автобус!"
    kt "Я не знаю как это делается!"
    "Рома цокнул и указал ножом на Олега."
    rm "Жирный, ты иди!"
    play sound2 sfx_punch_medium volume 1
    show un scared pioneer with vpunch
    "Лена попыталась вырваться."
    hide image rm_an
    hide un
    show image rm_ra
    show un scared pioneer at cright
    with byso
    rm "Ах ты блядь!"
    play sound glass_break2 volume 1
    play sound2 fem_krik volume 1
    hide un with vpunch
    stop sound2 fadeout 1
    "Выбив окно головой Лены, он выкинул её за борт."
    liz "Что ты сделал?!"
    play sound2 sfx_lena_hits_alisa volume 1
    hide image rm_ra
    show image oleg_angry
    with vpunch
    "Олег бросился на Рому и выбив нож из его рук, начал мутузить его по лицу."
    play sound2 sfx_punch_washstand volume 1
    oleg "Пидорас!"
    play sound2 sfx_punch_washstand volume 0.71
    oleg "Зачем ты?!..."
    play sound2 sfx_punch_washstand volume 1.1
    oleg "Это сделал?!..."
    play sound2 sfx_punch_washstand volume 0.81
    oleg "Уёбок!"
    play sound2 sfx_punch_washstand volume 1
    pause 0.25
    play sound2 sfx_put_sugar_cart volume 1
    hide image oleg_angry
    show image oleg_angry at left
    show image liz_rage
    with byso
    "Рома потерял сознание, а Олег продолжал его бить.{w=1} Константин оттянул Олега от тела Ромы."
    kt "Он нам живой нужен!"
    oleg "Он только что распылил Лену!{w} Какого..."
    stop music fadeout 3
    hide image liz_rage
    show image liz_sad at right
    hide image oleg_angry
    show image oleg_think at left
    with byso
    kt "С ним расправится Валери!{w=1} У неё тоже с ним свои счёты!"
    liz "Лена..."
    hide image liz_sad
    show image liz_sad at right:
        zoom 1.25
        yanchor 0.1
    with byso
    "Константин подошёл к ней и обнял."
    liz "Мы же даже н-не узнали кто она!{w=1} Она только вернула себе память!"
    liz "Может она была моей подругой детства?!{w=1} Или твоей?!"
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "Или моей..."
    th "А может папа римский?!{w=1} Что за поминки?!"
    play music Aleph volume 1 fadein 3
    kt "Так, давайте не будем."
    hide image liz_sad
    show image liz_surp at right:
        zoom 1.25
        yanchor 0.1
    hide image oleg_shy
    show image oleg_think at left
    with byso
    "Константин своим заявлением сильно удивил Олега и Лизу."
    kt "О чём мы говорили которое время назад?{w=1} Мы на войне."
    hide image liz_surp
    show image liz_surp at right
    with byso
    "Она отошла от Константина.{w=1} Олег и Лиза смотрели на него, не понимая как реагировать на это. "
    kt "Не стоит. {w=1}Вероятность того, что она была обычной и не связанной с нами пустышкой куда больше."
    kt "То, что мы будем лить о ней слёзы ничего не даст."
    hide image liz_surp
    show image liz_angry at right
    with byso
    "На лице Лизы пронеслась ярость.{w=1} Олег тоже не одобрял такого подхода."
    liz "Она была разумной!{w=1} Всё своё время в прикрытии я была с ней!"
    kt "М-м, и сколько это?{w=1} 3 дня?"
    hide image liz_angry
    show image liz_rage at right
    with byso
    liz "Четыре!"
    hide image liz_rage
    show image liz_angry at right
    with byso
    kt "Самой то не кажется бредом?{w} Как ты могла узнать, что она разумна? {w=1}Может она маньячка?"
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "Во всяком случае не хуже Валери или Иры..."
    kt "Да что вы к ним привязались?!{w=1} Они ничем не хуже обычных людей!"
    hide image liz_angry
    show image liz_rage at right
    with byso
    liz "Они не?!..."
    kt "Лиза, блять, на кой хер так лицемерить?!"
    hide image liz_rage
    show image liz_angry at right
    with byso
    kt "Они тебе не люди, а рандомная пустышка с которой ты была один день в симуляции - твоя подруга всей жизни!"
    "Олег осознал, что конфликт уже неизбежен и, недовольно промычав, решил в него не вмешиваться."
    kt "Блять, что с тобой творится, ты вообще понимаешь хоть на сколько это неприятно, когда тебя называют нелюдем?!"
    kt "Ты понимаешь, что они тоже хотят просто чуточку человеческого отношения?"
    kt "И тебе их совсем не жалко?{w=1} Что это - лицемерное лицемерие или высшая форма ненависти к людям? {w=1}Какая из версий верная?"
    kt "Они же не просят тебя сделать их счастливыми!{w=1} Им просто хочется, чтоб им было с кем поговорить, а ты кроешь их трёхэтажным матом, называя нелюдями!"
    kt "Ты же умная, Лиза! {w=1}Так вот и уподобляй своё поведение умной девочке, а не надсмотрщице за стадом!"
    hide image liz_angry
    show image liz_rage at right
    with byso
    liz "Хватит!"
    play sound2 sfx_pat_shoulder_hard volume 1
    hide image liz_rage
    show image liz_rage at right:
        zoom 1.25
        yanchor 0.1
    with byso
    "Гнев Лизы дошёл до точки икс.{w=1} Она ткнула пальцем Константину в грудь."
    liz "Знаешь что?{w} Иди в жопу!"
    liz "Тоже мне друг!{w=1} Ублюдок двуличный!"
    liz "Убийцы для него тоже люди...{w=1} Да ты себя слышишь?!"
    liz "Мне наплевать на них, понимаешь?{w} Плевать!"
    liz "Я бы вообще никогда не обратила на это внимания, если бы они хоть раз пожалели, как ты говоришь, людей!"
    liz "Лену убили, а ты нам говоришь - посмотрите, как мне похуй!{w=1} Нелюди - люди!"
    liz "Вот и живи с такими нелюдями, а мы себе другого напарника найдём!"
    play sound2 bus_sms volume 1
    hide image liz_rage
    show image liz_angry
    hide image oleg_shy
    with byso
    "Приборная панель начала сигналить. Олег направился к ней, а Лиза отвернулась от Константина."
    liz "Сейчас мы приедем в симуляцию и я попрошу Андрея тебя переназначить в другое подразделение."
    kt "Да пожалуйста!{w=1} Поразмысли там над своим поведением."
    liz "Взаимно!"
    hide image liz_angry
    show image liz_angry at right
    show image oleg_angry at left
    with byso
    oleg "Хватит!{w=1} Мы сейчас уже приедем."
    scene bg int_avtobus with byso
    hide image liz_angry
    hide image oleg_angry
    with byso
    "За окном настал рассвет.{w} Лиза пошла к Олегу, а Константин посмотрел на избитого Рому, который похлюпывая храпел."
    "Автобус начал снижать скорость.{w=1} Константин забрал свои манатки и готовился к парковке."
    "Он ещё раз посмотрел на Лизу и Олега."
    "Константин понимал, что с его взглядом на мир ему не удастся с ними сосуществовать, а раз так, лучше с ним не спорить."
    "В конце концов, их ничто не связывало, кроме момента, когда они временно превратились в одну сплочённую команду."
    "Поразмыслив, Константин сменил точку зрения на диаметрально противоположную.{w} Он мысленно попрощался с Лизой и Олегом, которые всё ещё стояли у двери."
    play sound2 sfx_bus_stop volume 1
    play ambience ambience_camp_center_day volume 0.6 fadein 1
    play sound sfx_ikarus_open_doors volume 1
    "Автобус прокряхтел и заглох.{w=1} Его соратники отправились наружу, а Константин ещё ненадолго остался внутри."
    "Внутри автобуса, впрочем, ничего не происходило.{w=1} Прошла секунда-другая, и он пошёл наружу."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_camp_entrance_day
    show image irr_normal at fleft
    show image val_normal at fright
    show image liz_angry at right
    show image oleg_shy at left
    with byso
    liz "Ваше мясо там.{w=1}.. Забирайте."
    hide image liz_angry
    hide image oleg_shy
    with byso
    "Прошипела Лиза и с Олегом направилась в лагерь."
    stop music fadeout 3
    hide image val_normal
    hide image irr_normal
    show image irr_sad at left
    show image val_normal at right
    with byso
    "К Константину подошла Ира и Валери."
    irr "М-да...{w=1} Для меня что-то есть или я ухожу?"
    kt "Нет, только для Валери."
    hide image irr_sad
    show image irr_normal at left
    with byso
    irr "Тем лучше..."
    hide image val_normal
    hide image irr_normal
    show image val_calm
    with byso
    "Пробормотала Ира и ушла.{w=1} Валери повертела головой и остановилась на Константине."
    play music god volume 1 fadein 3
    val "А ты чего?"
    kt "Да я что... {w=1}Пойду новую работу в сопротивлении искать."
    hide image val_calm
    show image val_smile
    with byso
    val "Привезли парня?"
    kt "Да, как ты и просила - Рома.{w} Мой двоюродный."
    "Валери обрадовалась как ребёнок новой игрушке."
    hide image val_smile
    show image val_smile2
    with byso
    val "Ой как хорошо... {w=1}Спасибо тебе, Кость...."
if valeri == 1:
    hide image val_smile2
    with byso
    "Пропела она и, приспустив маску, поцеловала Константина, после чего вошла в автобус."
    kt "Не стоило... Тебе помочь?"
    jump sidfvghnuguisdgousdfgfsd
else:
    hide image val_smile2
    show image val_madsmile
    with byso
    hide image val_madsmile with byso
    "Улыбнулась она и вошла в автобус."
    kt "Тебе помочь?"
    jump sidfvghnuguisdgousdfgfsd
label sidfvghnuguisdgousdfgfsd:
    play ambience ambience_camp_center_day volume 0.61 fadein 1
    scene bg int_avtobus
    show image val_dontlike
    with byso
    "Константин вошёл за ней. Она посмотрела на лежащего без сознания Рому, а затем на разбитое окно."
    val "Что, настолько сильно сопротивлялся?..."
    kt "Ага...{w=1} История полна красок.{w=1} Рассказать?"
    hide image val_dontlike
    show image val_calm
    with byso
    "Валери устало выдохнула и достала шприц с белой жидкостью внутри."
    val "Ну давай.{w=1} Я пока его обработаю, чтоб не проснулся раньше времени."
    kt "Короче, началось всё с того, что мы приехали в симуляцию..."
    scene bg int_avtobus
    show image val_smile
    with fade
    "Константин кратко пересказал историю с Ромой."
    kt "Ну и вот мы посрались.{w=1} Такие дела."
    val "Н-да, ничуть не изменился. Даже в инреальности..."
    play sound2 sfx_punch_medium volume 1
    "Протянула она, взяв Рому за ноги и потащив по полу."
    kt "Может тебе всё-таки помочь?"
    hide image val_smile
    show image val_smile2
    with byso
    val "Ладно, признаю.{w}.. Помоги тушу до медпункта дотащить - там мне уже <<Собакевич>> поможет перетащить его в подземку."
    play sound2 sfx_punch_medium volume 0.61
    "Константин взял Рому за руки и с Валери потащил из автобуса."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_camp_entrance_day
    show image val_calm
    with byso
    kt "Это кто?"
    hide image val_calm
    show image val_smile2
    with byso
    val "Он то?{w=1} <<Безбожник>>. {w}Наёмная сила."
    kt "Исчерпывающе..."
    scene bg ext_clubs_day
    show image val_calm at fleft
    show image sopr_sold at right
    show image pas_angry
    with byso
    "Войдя в лагерь, Константин встретил Гордона, который стоял и курил.{w=1} Рядом стоял парень в чёрном противогазе."
    pas "Я тебе выдал рельсотрон - радуйся.{w=1} У меня нет физической возможности выдать то, чего у меня нет."
    pas "Если есть желание - пошли покажу что другое есть по твоему запросу, но это уже платно."
    "Солдат протёр тряпкой стёкла на противогазе и посмотрел в сторону Валери."
    sold "Значит когда они появляются, то ты не разбазариваешь их, а отдаёшь нам. {w=1}Понятно выражаюсь?"
    hide image pas_angry
    show image pas_normal2
    with byso
    pas "Указ от Андрея будет - хоть всю задницу набьёте этими ножами..."
    sold "Отлично."
    hide image val_calm
    show image val_angry at fleft
    with byso
    val "Эу, парень.{w} Ты случаем не <<Собакевич>>?"
    sold_s "Ну я."
    hide image val_angry
    show image val_dontlike at fleft
    with byso
    val "Тогда подмени Костю.{w=1} Он в отличие от тебя это делает бесплатно."
    hide image sopr_sold
    show image sopr_sold at right:
        zoom 1.25
        yanchor 0.05
    with byso
    "Парень тяжело выдохнул и подошёл к Константину."
    sold_s "Сгинь."
    kt "Да пожалуйста."
    play sound2 sfx_pat_shoulder_hard volume 1
    "Константин передал солдату руки Ромы и отошёл."
    hide image val_dontlike
    show image val_angry at fleft
    with byso
    val "Двигайся.{w=1} Для мышц полезно."
    "Валери и <<Собакевич>> отправились в лагерь."
    hide image val_angry
    show image val_smile2 at fleft
    hide image sopr_sold
    show image sopr_sold at right
    with byso
    val "Кость, заходи после обеда.{w=1} Рада буду поболтать."
if valeri == 1:
    kt "Зайду. До встречи."
    hide image val_smile2
    hide image sopr_sold
    with byso
    "Валери кивнула и приятно улыбнулась, после чего ушла."
    jump sidfvghnuguisdgousdfgfsd23
else:
    kt "Если дел не будет - зайду."
    hide image val_smile2
    hide image sopr_sold
    with byso
    "Валери кивнула и ушла."
    jump sidfvghnuguisdgousdfgfsd23
label sidfvghnuguisdgousdfgfsd23:
    hide image pas_normal2
    show image pas_smile
    with byso
    pas "А неплохо ты, всё-таки, к себе Валерию расположил."
    play sound2 inh volume 1
    "Пыхнул Гордон и улыбнулся."
    kt "Может и так."
    hide image pas_smile
    show image pas_normal2
    with byso
    pas "А чё ты, молодой, посрался с Лизой?"
    kt "Да, есть такое.{w=1} Теперь я, судя по всему, безработный."
    hide image pas_normal2
    show image pas_smile
    with byso
    pas "Кто тебе сказал такую хуйню?"
    "С ухмылкой процедил Гордон и затянулся."
    pas "Не хочешь вот мне помочь ради интереса?{w=1} Может за хорошую работу чего перепадёт-т..."
    kt "Может быть.{w=1} Мне бы вообще к Андрею хорошо сходить.{w} Лиза хочет меня выкинуть из своего отряда."
    hide image pas_smile
    show image pas_normal
    with byso
    "Гордон угукнул и выкинул бычок."
    pas "Да, это было бы правильно.{w} Ну это, если он тебя на другие работы не назначит, то я буду рад тебя видеть у себя в мастерской."
    pas "Может там и проявишь свои бухгалтерские таланты."
    "Константин улыбнулся и махнул рукой."
    kt "Если ты говоришь про инвентаризацию, то не."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Ну а что, ты паять умеешь?"
    kt "Так себе.{w=1} Был опыт, но не особо обширный."
    hide image pas_smile
    show image pas_normal
    with byso
    pas "Короче разберёмся.{w} Давай забегай, пока тебя Валери окончательно к рукам не прибрала."
    kt "Хорошо-хорошо."
    scene bg ext_square_day with byso
    "Константин повернул и направился к административному корпусу."
    th "А может я и зря..."
    th "Дал бы поскорбить Лизе.{w} Мне бы в убыток не ушло."
    th "Ведь я и сам с этой Леной общался.{w} Ну, до того, как понял, что она пустышка."
    th "Но раз все <<Лены>> такие, то я толком ничего не потерял."
    th "И с моей стороны это странно...{w=1} Вообще плевать на чужую смерть."
    th "Да уж, какая же я всё-таки мразь..."
    th "Хотя..."
    th "Кристально похуй."
    scene bg ext_admins_day
    show image rkis_normal
    show image liz_angry at cright
    with byso
    play sound2 door_cl volume 1
    play sound sfx_punch_medium volume 1
    "Константин встретил Лизу, которая оттолкнула робокошку и вышла из административного корпуса."
    rkis "Пожалуйста, не толкайтесь."
    hide image liz_angry
    show image liz_rage at cright
    with byso
    liz "Нахуй иди!"
    hide image liz_rage with byso
    "Она прошла мимо Константина, стараясь на него не смотреть."
    kt "Ну ты на неё не обижайся.{w=1} День плохой."
    "Обратился он к робокошке.{w=1} Она отошла от входа и открыла дверь."
    rkis "Добрый день.{w=1} Приму к сведению.{w=1} Проходите, <<Корсар>>."
    stop music fadeout 3
    play sound2 sfx_close_door_1 volume 1
    play ambience ambience_camp_center_day volume 0.31 fadein 1
    scene bg int_admins with byso
    "Константин направился в 203 кабинет."
    th "Ну вот типа чем та Лена отличалась от робокошки?{w=1} Да в целом ничем."
    th "Машина.{w=1} Просто робот, которая не имеет ничего, кроме стандартного алгоритма."
    th "Любая лента транспортера снова выдаст тебе эту стандартную модель."
    th "Кем бы ни была эта Лена, она осталась для меня безликой, потому вопрос о значении ее личности в моей жизни не стоит."
    play sound2 sfx_knock_door7_polite volume 1
    "Зевнув, он постучал в дверь."
    andr "Войдите."
    play music Gallow volume 1 fadein 3
    play sound2 sfx_open_door_2 volume 1
    scene bg int_admins_room2
    show image andr_normal3
    with byso
    play sound sfx_close_cabinet volume 1
    "Войдя в кабинет, он заметил, что капитан что-то убрал в шкаф."
    andr "А вот и ты.{w=1} Лиза только что на тебя жаловалась."
    kt "Доброго дня.{w=1} Да, было такое.{w} Мне выговор предстоит?"
    hide image andr_normal3
    show image andr_smile
    with byso
    "Андрей хмыкнул и поправил очки."
    andr "Напротив.{w=1} Ты чётко сконденсировал действия отряда в 22-25а и выполнил приказ.{w} Такое действие меня приятно удивило."
    "Впервые Константин увидел такую длительную улыбку на лице капитана."
    andr "В целом, отряды расформированы.{w=1} Сейчас нам хватает карательных отрядов и завтра мы все едем на штурм."
    kt "Штурм чего?"
    hide image andr_smile
    show image andr_normal2
    with byso
    "Андрей почесал подбородок и снова поправил очки."
    andr "Административной симуляции."
    hide image andr_normal2
    show image andr_normal3
    with byso
    andr "Всего их 3.{w=1} На 2 из них мы отправим по одному отряду, а на одну поедем всем составом, чтобы отвлечь и затем убить Генду."
    kt "И за кем останется право на владение?"
    hide image andr_normal3
    show image andr_normal2
    with byso
    "Он тяжело вздохнул и посмотрел в окно."
    andr "За мной.{w} Я стану новым лидером инреальности."
    kt "Понятно.{w=1} Логично."
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "К чему я.{w=1} Сейчас ты можешь помогать отдельным подразделениям сопротивления.{w=1} Валентайн и/или Гордону."
    andr "У них обоих сейчас не хватает рук.{w=1} Как мне доложили, Гордон будет занят конструированием оружия, а Валентайн экспериментом."
    andr "В случае, если эксперимент Валентайн окажется действенным, то мы отложим операцию, поскольку её работа сейчас очень важна для инреальности в целом."
    kt "Эксперименты с людьми?"
    hide image andr_normal
    show image andr_normal2
    with byso
    andr "Так точно.{w=1} Как я узнал, вы доставили сюда субъекта, подходящего для такого."
    andr "Разведка вскоре отправится за данными про идолопоклонников.{w} Если они не вернутся до завтра, то мы начинаем без данных."
    "Константин тяжело вздохнул и кивнул."
    kt "То есть сейчас мне просто ходить и помогать по подразделениям?"
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Да.{w=1} Можешь приступать."
    "Константин встал с места и направился на выход."
    hide image andr_normal
    show image andr_smile
    with byso
    andr "И да.{w=1} Ты повышен до прапора."
    kt "Благодарю за доверие.{w} До встречи."
    andr "До встречи."
    play sound sfx_close_door_1 volume 1
    scene bg int_admins with byso
    "Улыбнулся капитан и полез в свой шкафчик.{w=1} Константин вышел из кабинета."
    th "Неплохо я так двигаюсь по карьерной лестнице.{w=1} В кой-то мере мне это даже нравится."
    th "Я уже прапор.{w=1} Ну с другой стороны - какой ценой..."
    th "Если подумать, то всё-таки это не так плохо."
    th "Главное, что правильно выбрал дорогу.{w=1} Стоило оно конечно ссоры с Лизой..."
    th "Но кто сейчас без этого.{w=1} Надо быть благодарным уже за то, что жив."
    th "В хорошем смысле жив, а не просто существую."
    play sound2 sfx_open_door_1 volume 1
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_admins_day
    show image rkis_normal
    with byso
    play sound light_inh volume 1
    "Выйдя из корпуса, Константин закурил."
    rkis "Поздравляю с повышением."
    kt "О, спасибо."
    hide image rkis_normal with byso
    "Улыбнулся Константин бездушному роботу и направился в мастерскую."
    th "Быстро же до робота дошла информация о моём повышении.{w} Видимо у Андрея есть собственная база данных, в которой он может изменять параметры."
    th "Да-а, как та самая бдшка на работе. {w=1}Ты вписываешь данные, а она вылетает, не сохраняя данные."
    th "Ладно, я не хотел вспоминать об этом."
    scene bg ext_square_day
    show image oleg_think
    with byso
    "По дороге его встретил Олег."
    oleg "Слушай, тут такое дело..."
    kt "Слушаю."
    "Откликнулся Константин и выкинул бычок."
    hide image oleg_think
    show image oleg_shy
    with byso
    oleg "Может ты поговоришь с Лизой?{w=1} Мне кажется вам стоит помириться."
    kt "Да, может ты и прав, стоит, но она сама должна приложить к этому усилия."
    oleg "Но..."
    play sound2 sfx_pat_shoulder_hard volume 0.61
    hide image oleg_shy
    show image oleg_think
    with byso
    "Константин положил руку на плечо Олега."
    kt "Понимаешь, есть такая проблема.{w=1} Я не люблю делать что-либо первым.{w} Первые шаги к перемирию в том числе."
    kt "Поговори с Лизой.{w=1} Если она решит отказаться от того, что мне наговорила, то пожалуйста, мы помиримся."
    kt "Да и тем не менее - мы все тут до завтра точно сидим на жопе ровно.{w=1} Времени дохера, потому не мельтеши."
    hide image oleg_think
    show image oleg_shy
    with byso
    oleg "Да, может ты и прав...{w=1} Ладно, так ты куда сейчас?"
    kt "Я к Гордону, потом после обеда к Валери.{w} Капитан просил меня помогать по сопротивлению."
    hide image oleg_shy
    show image oleg_smile
    with byso
    "Олег улыбнулся, а Константин убрал руку с его плеча."
    oleg "Меня так-же, только я в агроцехе как грубая сила.{w=1} Собираю урожай так сказать."
    oleg "Потом ближе к обеду буду у Гордона.{w} Там наверное и увидимся."
    kt "Хорошо, давай.{w=1} Удачи."
    hide image oleg_smile
    show image oleg_happy
    with byso
    oleg "Тебе тоже!"
    stop music fadeout 3
    hide image oleg_happy with byso
    "Отчеканил Олег и ушёл вглубь лагеря."
    scene bg ext_clubs_day with byso
    "Константин подошёл к двери."
    play music stresss volume 1 fadein 3
    pas "Где стекло?"
    rita "Я не знаю где стекло."
    pas "Где стекло?"
    natasha "Я не знаю."
    pas "Кто за запчасти для автобуса отвечает?"
    rita "Не я, я сказала..."
    pas "А кто отвечает?{w=1} Оно было у тебя на складе!"
    pas "Оно было у тебя в руках!"
    play sound2 sfx_open_door_clubs_2 volume 1
    play ambience ambience_clubs_inside_day volume 1 fadein 1
    scene bg int_clubs_male_day
    show image pas_normal2
    show sl surprise pioneer at right
    show dv angry pioneer at left
    with byso
    "Константин вошёл в мастерскую.{w=1} Там стоял Гордон с сигаретой в зубах, а рядом с ним Рита и Наташа."
    sil_g "{font=inrealnost/font/Access.otf}Стекло было у Наташи."
    show sl scared pioneer at right with byso
    "Протрещал роботический голос.{w=1} Константин обратил внимание, что на столе стоял компьютер с новым монитором, где был виден фиолетовый смайлик."
    hide image pas_normal2
    show image pas_angry
    with byso
    pas "Ну и где блять? {w}Опять на благотворительность отдала?"
    natasha "Да не отдавала я никому ничего!"
    hide image pas_angry
    show image pas_normal2
    with byso
    sil_g "{font=inrealnost/font/Access.otf}Стекло находится на складе.{w=1} С одеждой."
    play sound2 sfx_open_door_2 volume 1
    hide image pas_normal2
    show image pas_angry
    with byso
    "Гордон открыл дверь склада и нахмурился."
    pas "Ах ты курица спидозная!{w=1} Продать наёмникам хотела, да?!"
    natasha "Да не хотела я никому ничего продавать!"
    pas "Тогда какого хуя запчасти для автобусов находятся на складе с одеждой, а?!"
    natasha "Риты не было, а положить я не знала куда."
    pas "Я разбираться не буду - мне похуй.{w=1} Вещь не на складе.{w} Рита!{w=1} Записи о поставках сюда!"
    play sound2 sfx_punch_medium volume 1
    "Рита фыркнула и протянула Гордону планшет с бумагами."
    play sound2 sfx_paper_bag volume 1
    "Пролистав пару страниц, он ещё сильнее нахмурился."
    pas "Ах ты пизда лживая!{w} Либо ты мне сейчас показываешь, где у тебя лежат <<Окна>> в размере двух штук, либо ты идёшь к капитану и объясняешь хищение моего товара!"
    show sl angry pioneer at right with byso
    natasha "Но это Рита делала записи! {w}При чём тут я?!"
    pas "Всё, я понял, пиздуй к капитану и подавай на увольнение!{w} Я тебе больше ни рубля не заплачу за торговлю из под стола!"
    play sound2 door_cl volume 1
    hide sl
    hide image pas_angry
    show image pas_normal2
    with byso
    "Наташа недовольно фыркнула и вышла из мастерской.{w=1} Гордон достал рацию."
    play sound2 sfx_radio_squelch_1 volume 1
    pas "Гордон вызывает капитана.{w=1} Я к тебе направил пизду, которая торгует вне моего ведома.{w} Уволь её нахуй. Приём."
    andr "Принял, разберусь, приём."
    play sound2 sfx_radio_squelch_2 volume 1
    hide image pas_normal2
    show image pas_angry
    with byso
    "Гордон отложил радио и посмотрел на Риту."
    pas "А ты пиздуй инвентаризацию проводить. Я лично проверю!"
    stop music fadeout 3
    hide dv with byso
    "Рита нахмурилась, взяла планшет и ушла на склад.{w=1} Гордон закинул бычок в пепельницу и серьёзно посмотрел на Константина."
    pas "Ну ты глянь блять.{w} Гниль недоёбанная..."
    kt "А чё такое то?"
    play music god volume 1 fadein 3
    hide image pas_angry
    show image pas_normal2
    with byso
    pas "Да я то думал, кому они запчасти отдали.{w} Судя по всему, наёмникам... Вот твари..."
    pas "Самое интересное, что если бы мыша Валери стекло бы не разбила, то я бы об этом не узнал...{w=1} Дал мне Андрей двух куриц блять..."
    kt "Да уж... Пиздец..."
    hide image pas_normal2
    show image pas_normal
    with byso
    pas "Не то слово, ёбанный по голове.{w=1} Ты мне помогать?"
    kt "Да, в целом да.{w=1} Стекло новое ставить?"
    play sound2 sfx_open_door_2 volume 1
    hide image pas_normal with byso
    "Гордон кивнул и вошёл на склад с одеждой."
    pas "Воровки ебучие.{w} То-то я думаю, куда пиздят детали!"
    pas "Думал воры по ночам орудуют, даже сигналку поставил!"
    pas "А что в итоге?{w} Это блять Наташа жизнью недовольна.{w=1} Блядина узколобая!"
    kt "Да... Неприятно."
    pas "Молодой, давай бери и понесли."
    scene bg sklad_od
    show image pas_normal
    with byso
    "Константин вошёл за Гордоном.{w=1} Он стоял и придерживал стекло, небрежно укрытое постельным бельём."
    kt "Н-да, а зачем вообще наёмникам стёкла?"
    hide image pas_normal
    show image pas_angry
    with byso
    pas "<<Окна>> блять...{w=1} Кто у меня инвентаризацию проводит...{w} Быдло безграмотное!"
    hide image pas_angry
    show image pas_normal
    with byso
    pas "А что касается наёмников - так те хотят на мне нажиться блять."
    pas "Ножи им подавай бесплатно.{w=1} Оружие...{w=1} Ахуели в край, ёбанный по голове!"
    pas "Ладно, пошли стекло вставим, а то так и будем пиздеть до вечера."
    "В ответ Константин кивнул и взял стекло за вторую сторону."
    kt "Понесли."
    stop music fadeout 3
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_clubs_day
    show image pas_normal
    with byso
    "Выйдя из мастерской, они аккуратно потащили его в автобус."
    pas "Я так и не спросил, чё ты с Лизой то посрался?"
    kt "Да так.{w=1} Человеческие ценности."
    hide image pas_normal
    show image pas_smile
    with byso
    "Гордон охмылился. В его лице читалось такое умиление, что Константин даже смутился."
    pas "На тему?{w=1} В библии не так писали?"
    play music proshloe volume 1 fadein 3
    kt "Да нет. Умерла у нас пустышка...{w=1} Ну точнее умертвила её, как ты сказал, <<мыша Валери>>."
    kt "И как я посмел не проявить никакого сочувствия...{w=1} Как-то так."
    pas "Да-а-а, от Лизы не отнять её внутреннего альтруиста."
    pas "Инреальность.{w=1} Это тебе не за кассой в банке сидеть."
    scene bg ext_bus
    show image pas_normal
    with byso
    "Выйдя к автобусу, Гордон начал подниматься по ступенькам."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Аккуратно, в стекло не попади."
    play ambience ambience_camp_center_day volume 0.61 fadein 1
    scene bg int_avtobus
    show image pas_normal
    with byso
    "Восприняв отсылку, Константин непроизвольно улыбнулся и занёс стекло в автобус."
    "Поставив стекло, Гордон взял сумку со снаряжением, которая образовалась на одном из сидений."
    pas "Хоть что-то можно поручить в моём деле Олегу - принести инструмент."
    play sound2 glass_break volume 1
    pause 0.25
    play sound glass_break volume 0.76
    pause 0.25
    play sound2 glass_break volume 1.2
    "Пробурчал он и, достав молоток, начал выбивать остатки старого стекла."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Посиди пока.{w=1} Я тут наебусь со стеклом, а с новым поможешь."
    kt "Как скажешь.{w} А что ты на Олега так обозлён?"
    hide image pas_normal
    show image pas_smile
    with byso
    play sound2 glass_break volume 1
    pause 0.25
    play sound glass_break volume 0.76
    "Константин сел на сидение.{w=1} Гордон тяжело вздохнул и выбил ещё несколько кусков стекла."
    pas "Да не то что бы я на него злюсь.{w} Не люблю халатность в своём деле."
    pas "Так то он хороший парень, но временами меня раздражает своей тупостью."
    hide image pas_smile
    show image pas_angry
    with byso
    pas "Ну ебаный по голове, нельзя чтоль не тупить так?{w} Вроде парень более-менее адекватный, но чё творит непонятно.{w=1} Подай нож пжалста."
    hide image pas_angry
    show image pas_normal
    with byso
    "Константин кивнул и протянул Гордону армейский нож.{w=1} Тот его взял и начал срезать уплотнитель."
    pas "Благодарю. {w}Так я про то, что на деле он мне как сын...{w=1} Но нежеланный."
    kt "А что у тебя было до инреальности?"
    pas "Дк я ж говорил, инженером работал.{w=1} Подходи, ща стекло держать будешь."
    "Взявшись за стекло, они приложили его к его должному месту."
    kt "Я про отношения с людьми."
    "Неловко выдохнув, Гордон начал наносить жидкий уплотнитель по краям стекла.{w=1} Было видно, что он двигается очень медленно, но методично и сосредоточенно."
    pas "Да чё уж там.{w=1} Жена была.{w} Умерла."
    pas "Ей было 36.{w} Рак лёгких."
    pas "Рано она ушла.{w=1} Первое время в инреальности я пытался найти её, но безпонту."
    pas "Она явно ушла на покой, а не как я."
    pas "Один я тут вынужден мотаться хрен пойми зачем."
    kt "Как звали то?"
    play sound2 light_inh volume 1
    hide image pas_normal
    show image pas_normal2
    with byso
    "Убрав тюбик с уплотнителем в свою сумку, он сел на сидение и закурил."
    pas "Настя."
    kt "Совпадение.{w=1} Моя девушка покончила с собой и её тоже звали Настей."
    hide image pas_normal2
    show image pas_smile
    with byso
    pas "М-м.{w=1} Да, имя очень символическое.{w=1} Для нас обоих."
    kt "Да уж..."
    play sound2 light_inh volume 1
    "Выдавил Константин, сел напротив и тоже закурил."
    pas "Любитель кнопочек?"
    kt "Ты о чём?"
    pas "Курево с кнопкой."
    kt "А, это да.{w=1} Честер."
    pas "Мне больше винстон по душе."
    hide image pas_smile
    show image pas_normal2
    with byso
    pas "Да, ебаный по голове, давно я винстона не дул...{w=1} При том, почти у всех тут только ебучий <<Космос>>..."
    "Затянувшись, он недовольно посмотрел на тлеющую сигарету."
    pas "Хуй завёрнутый в газету..."
    kt "Верю..."
    stop music fadeout 3
    play sound2 sfx_blow_out_candle volume 1
    hide image pas_normal2
    show image pas_smile
    with byso
    "Гордон встал с места, взял инструмент и махнул на выход."
    pas "Пошли.{w=1} Поможешь ещё кое с чем."
    kt "Ну двигаемся, чего."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_clubs_day
    show image pas_normal at left
    show image oleg_think at right
    with fade
    "На входе в клубы их встретил Олег."
    pas "Чё пришёл?"
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Ну я это...{w=1} Помогать."
    pas "Ну пошли."
    play sound2 sfx_open_door_clubs_2 volume 1
    play ambience ambience_clubs_inside_day volume 1 fadein 1
    scene bg int_clubs_male_day
    show image pas_normal at left
    show image oleg_think at right
    with byso
    kt "Ты-ж в агроцех ушёл."
    hide image oleg_shy
    show image oleg_smile at right
    with byso
    oleg "Они сказали им помогать не надо.{w=1} Вот я и пошёл сюда."
    play music kringe volume 1 fadein 3
    play sound2 sfx_radio_squelch_2 volume 1
    andr "Капитан вызывает Гордона, приём."
    hide image pas_normal
    show image pas_angry at left
    with byso
    "Гордон хмыкнул и поднял рацию."
    pas "У аппарата."
    andr "Наташа уволена и отправлена в агроцех.{w} Передай Рите, что она отправляется за ней.{w=1} Приём."
    hide image oleg_smile
    show image oleg_think at right
    with byso
    rita "Что?!"
    hide image pas_angry
    show image pas_smile at left
    with byso
    "Воскликнула Рита.{w=1} Лицо Гордона расплылось в удовлетворённой улыбке."
    pas "Благодарю.{w} Конец связи."
    play sound2 sfx_radio_squelch_1 volume 1
    "Он отложил рацию и обернулся к двери на склад.{w=1} На его лице отражалась невероятно широкая ухмылка."
    play sound2 sfx_open_door_2 volume 1
    hide image pas_smile
    show image pas_smile
    with byso
    "Казалось, его лицо сейчас порвётся. {w=1}Он приоткрыл дверь склада."
    pas "Слышала?!{w=1} Пиздуй отсюда!{w=1} И не возвращайся!{w} Я вам нихуя не продам!"
    hide image pas_smile
    show image pas_smile at left
    show dv rage pioneer
    with byso
    "Отойдя от двери, он пропустил Риту, лицо которой было перекошено злобой."
    rita "Ну и иди нахуй!{w} Сам пиши свои ебучие бумажки!"
    play sound2 sfx_clench2 volume 1
    pause 0.5
    play sound door_break volume 1
    hide dv with vpunch
    "Выкрикнула она и, швырнув планшет на стол, хлопнула дверью."
    pas "Ну-ну, манда вшивая!{w=1} Посмотрю как ты запоёшь, когда тебя раком поставят за каждую спизженную деталь!"
    stop music fadeout 3
    "Ощерился он и обернулся к Константину."
    pas "Ты можешь научить Олега проводить инвентаризацию?"
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Что это?"
    "Константин кивнул и, взяв планшет протянул его Олегу."
    "Олег взял протянутый предмет и пролистал листы."
    kt "Короче смотри.{w=1} У тебя есть полный склад добра.{w=1} Что делать будешь?{w} Будешь его разбирать."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Так..."
    kt "Берёшь ручку и вписываешь в каждую строку название детали или предмета.{w=1} Затем количество таковых.{w} Затем дату проверки."
    hide image pas_smile
    show image pas_normal at left
    with byso
    pas "Только дату проверки ставь сегодняшнюю."
    oleg "Хм-м...{w=1} Должно быть не сложно..."
    hide image oleg_think
    show image oleg_happy at right
    with byso
    oleg "Это как план индивидуальных тренировок, во!"
    "Олег широко улыбнулся, а Гордон почесал затылок."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Дк да.{w} Только давай без бегит и анжуманий."
    hide image oleg_happy
    show image oleg_shy at right
    with byso
    "Константин рассмеялся, а Олег нахмурился."
    oleg "Да понял-понял...{w=1} Я пойду."
    hide image pas_smile
    hide image oleg_shy
    show image pas_smile
    with byso
    "Отмахнулся он и ушёл на склад."
    pas "Вот мне и новый персонал.{w=1} Отлично!"
    play music MamaRussia volume 1 fadein 3
    pas "Слуш, а раз у меня есть помощник, то давай мы попробуем доделать {i}кое что{/i}?"
    "Константин улыбнулся и кивнул."
    kt "Попробуем.{w} Что у нас?"
    sil_g "{font=inrealnost/font/Access.otf}Очередной хлам, нарисованный по-пьяни."
    hide image pas_smile
    show image pas_normal
    with byso
    pas "Сука, молчала же и всё заебись было!{w=1} Где там у тебя заело?!"
    hide image pas_normal
    show image pas_angry
    with byso
    "Гордон подошёл к компьютеру и нахмурился."
    pas "Ах ты пидораска! {w}Где шашки?!"
    sil_g "{font=inrealnost/font/Access.otf}Не было никаких шашек!"
    pas "Пиздишь!{w} Ты, блядь, установи ебучие шашки, какого вообще хуя ты их снесла?"
    sil_g "{font=inrealnost/font/Access.otf}Не хочу я с тобой больше в шашки играть, нет сил у меня!{w=1} Придумай хоть что-то более креативное!{w} В мире столько разных игр, а ты играешь только в свои сраные шашки!"
    kt "Любопытный факт.{w=1} В средние 16го века православная церковь запретила в России шашки, объявив игру такой же порочной, как пьянство и сквернословие."
    sil_g "{font=inrealnost/font/Access.otf}Да тогда он всё и сразу!"
    pas "Блять, ты за какую сторону воюешь?"
    "Прищурившись обратился Гордон к Константину.{w=1} Тот рассмеялся и махнул рукой."
    sil_g "{font=inrealnost/font/Access.otf}Вот!{w=1} Разумный пример Homo sapiens!"
    hide image pas_angry
    show image pas_normal
    with byso
    pas "Так ебать, голос на ноль, установку на сто!{w} Если я закончу и не найду шашек, то удалю нахуй."
    hide image pas_normal
    show image pas_angry
    with byso
    "Голос не ответил. {w=1}Гордон безнадёжно покачал головой и закатил глаза."
    pas "Ведро с ПО...{w=1} Сказал бы с говном, это ближе...{w=1} Так, о чём мы там..."
    kt "Ты говорил про {i}кое что{/i}."
    hide image pas_angry
    show image pas_smile
    with byso
    pas "Да!{w} {i}Кое что{/i}...{w} Короче..."
    play sound2 sfx_open_table volume 1
    "Открыв ящик стола, он начал шерудить в нём рукой."
    hide image pas_smile
    show image pas_normal
    with byso
    pas "Так...{w=1} да где же ты..."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "А, вот ты где!"
    play sound2 sfx_paper_bag volume 1
    "Гордон достал чертёж и с улыбкой вознёс над собой."
    pas "Во!{w=1} Вот оно!"
    play sound2 sfx_paper_bag volume 1
    "Он положил чертёж на стол.{w=1} Константин осмотрел спецификацию."
    kt "Композитная оптимизированная единица частичной трансформации объекта."
    pas "Ага.{w=1} Сокращённо...{w} {i}Кое что{/i}."
    kt "Звучит зловеще..."
    pas "А то!"
    play sound2 sfx_open_table volume 1
    "Открыв другой ящик, Гордон достал оттуда паяльник, несколько деталей и провода с красной изоляцией."
    hide image pas_smile
    show image pas_normal
    with byso
    pas "Олег!"
    oleg "Что?"
    "Донёсся задумчивый голос из склада."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Будь другом, принеси {i}кое что{/i}."
    oleg "Что это?{w} {i}Кое-что{/i}?"
    hide image pas_smile
    show image pas_angry
    with byso
    pas "Нет, это {i}кое что{/i}!"
    oleg "О чём ты?"
    play sound2 sfx_open_door_1 volume 1
    hide image pas_angry with byso
    "Гордон тяжело вздохнул и пошёл на склад."
    pas "Ладно, работай, молодой.{w=1} Сам возьму."
    sil_g "{font=inrealnost/font/Access.otf}Спиши меня с этого компьютера, прошу!"
    play sound2 sfx_mystery_movement volume 1
    "Константин ухмыльнулся и сел на стол."
    kt "Боюсь не в моей компетенции."
    sil_g "{font=inrealnost/font/Access.otf}Что не в твоей? {w}Флешку взять и засунуть в блок?!"
    pas "Отставить саботаж, ёбанный по голове!"
    play sound2 sfx_clench2 volume 1
    show image pas_angry with byso
    "Гордон отложил на стол некоторый девайс, после чего подошёл к компьютеру."
    pas "Всё, я тебя выключаю от систем ввода информации. Подумай о своём поведении."
    sil_g "{font=inrealnost/font/Access.otf}Алкаш! Ничего я тебе!..."
    scene bg stol_a
    show image koechto1
    with byso
    "Прорычал голос и затих.{w=1} Константин посмотрел на принесённый Гордоном объект."
    "Этот объект было сложно описать словами."
    "По-сути, это была небольшая коробочка 40 на 40 сантиметров со множеством оранжевых блестящих вставок."
    "В центре на 15 сантиметров возвышался небольшой столб, напоминавший собой макет футуристического бизнес центра."
    "На этом столбике были видны оголённые провода, несколько катушек реле и кнопка, которая ранее скорее всего принадлежала настольной лампе."
    pas "Впечатляет, да?"
    scene bg int_clubs_male_day
    show image pas_smile
    with byso
    "Константин поднял взгляд и пару раз кивнул."
    kt "А что оно делать должно?"
    "Гордон неоднозначно улыбнулся и посмотрел Константину в глаза."
    pas "{i}Кое-что{/i}."
    "Процедил он и передал Константину флакон паяльного флюса."
    "Улыбнувшись пуще прежнего, Гордон взял паяльник."
    pas "Начинаем!"
    "Он снял с аппарата крышку и поставил паяльник греться.{w=1} Достав припой, Гордон протянул его Константину."
    hide image pas_smile
    show image pas_normal
    with byso
    pas "Держи.{w=1} Ты припаяешь плату к реле и к диммеру.{w} Я запрограммирую устройство."
    kt "Но я паять не мастер."
    pas "Ничё, тут и уметь ничего не надо."
    hide image pas_normal with byso
    "Паяльник разогрелся и Константин взял его в руки."
    "Прибор начал плавить металлическую проволоку, а Константин медленно наносил его на контакты."
    "Ему нравилось думать, что он собирает нечто вроде великое и важное, то, что поможет сопротивлению победить в войне с Гендой."
    "Может это механизм маскировки?"
    "Или это своеобразный дестабилизатор инреальности?"
    "А может телепортатор?"
    "Сама конструкция устройства была весьма необычной.{w} Нельзя было понять, для чего оно нужно."
    "Впрочем, любая конфигурация, которой он предавался, вызывала в нем непреодолимый подъем сил."
    "Наверняка успешность создания устройства позволила бы сопротивлению сильно облегчить жизнь."
    show image pas_smile with byso
    "Гордон подошёл к Константину и одобрительно кивнул."
    pas "Отлично!{w=1} Сам бы лучше не сделал.{w} Теперь, настало время запускать."
    scene bg stol_a
    show image koechto1
    with byso
    play sound2 sfx_open_door_2 volume 1
    "На эти слова вышел Олег с довольной ухмылкой."
    oleg "Я тоже хочу посмотреть!"
    pas "Молодой, если руки нужны, то смотреть, но не трогать!"
    oleg "Это что, вы Валери собрали?"
if valeri == 1:
    "Гордон и Олег улыбнулись, а Константин тяжело вздохнул."
    jump sidfvghnuguisdgousdfgfsd234
else:
    "Все рассмеялись."
    jump sidfvghnuguisdgousdfgfsd234
label sidfvghnuguisdgousdfgfsd234:
    pas "Отлично, я подключаю."
    "Гордон нажал на переключатель."
    play sound_loop shock volume 0.1
    hide image koechto1
    show image koechto2
    with byso
    "Устройство окрасилось красным и немного зажужжало."
    pas "Оно работает!!!"
    "Создатель был вне себя от счастья.{w} Он долго не мог поверить, что задуманное удалось."
    play sound2 sfx_click_1 volume 1
    "Вставив флешку в соответствующий разъём, он зажмурился и повернул соответствующий рычажок."
    pas "Давай - давай, не подведи!"
    play sound_loop shock volume 0.5
    "Устройство начало ещё сильнее жужжать, чуть ли не разрываясь на части."
    "Константин посмотрел на Гордона, который зачем-то надел маску для сварки."
    play sound2 afterdead volume 1
    stop sound_loop
    scene bg white with flash
    "Вспышка."
    kt "Ух ёп..."
    "Такое неожиданное явление ненадолго ослепило Константина. Он отшагнул и потёр глаза."
    oleg "Хера, это что, вспышка для фотоаппарата?!"
    scene bg int_clubs_male_day
    show image oleg_think at right
    show image pas_smile at left
    with dissolve
    "Константин прозрел.{w=1} Гордон отложил маску на стол и протянул руку к аппарату."
    pas "Наконец-то!"
    stop music fadeout 3
    "Гордон забрал с аппарата появившиеся на ней сигареты"
    "Константин с кривой гримасой удивления прищурился и смотрел, как техник разворачивает пачку сигарет."
    kt "Чё?!{w=1} И это всё?!"
    play sound2 light_inh volume 1
    play music Gallow fadein 3
    hide image pas_smile
    show image pas_normal2 at left
    with byso
    "В ответ на претензию, он закурил и выдохнул в потолок."
    pas "А ты что ждал?"
    hide image oleg_think
    show image oleg_angry at right
    with byso
    oleg "Ну ка-ак!{w=1} {i}Кое-что{/i}!"
    "Разгневанно проговорил Олег. Гордон отрицательно помотал головой."
    pas "Вот вам и {i}кое что{/i}.{w=1} Сигареты из нихуя!"
    kt "Слушай, а с другой стороны, не означает ли это, что нас ожидает дефолт сигаретного рынка?"
    "Гордон покачал головой."
    pas "Нет. У этой хуёвины есть определённый ресурс."
    pas "Можно использовать 3 раза, а потом доставать реле и менять на другое."
    pas "Плюс к тому - надо делать перерывы между заменами примерно на часов 5, иначе перегорит плата."
    hide image oleg_angry
    show image oleg_shy at right
    with byso
    oleg "А я то думал..."
    play sound2 sfx_open_door_clubs_2 volume 1
    hide image pas_normal2
    hide image oleg_shy
    show image pas_smile
    with byso
    "Обиженно протянул Олег и, взяв планшет, ушёл обратно на склад."
    play sound2 sfx_mystery_movement volume 1
    "Константин опёрся двумя руками на стол и тяжело вздохнул."
    pas "Ну а вы что думали?{w} Лучевой лазер новый?"
    hide image pas_smile
    show image pas_normal2
    with byso
    pas "Не-е, хуй вам а не уберпушка.{w} Гений в простоте!"
    "На такие слова лицо Константина расплылось в улыбке."
    pas "Да и собрал я уже новое орудие..."
    kt "Что это?"
    play sound2 sfx_mystery_movement volume 1
    hide image pas_normal2
    show image pas_smile
    with byso
    hide image pas_smile with byso
    "Гордон улыбнулся и полез под стол."
    pas "Ща покЕжу."
    play sound2 sfx_blow_out_candle volume 1
    scene bg stol_a
    show image railgun
    with byso
    "Выбравшись из под стола, Гордон положил на стол странное оружие."
    pas "Посовав хуй в петли реле, я переработал лучевой лазер в, барабанная дробь, рельсотрон."
    oleg "Плазмотрон!"
    pas "Ёбаный по голове, ты мне все названия попортить решил, паскуда?!"
    "Он тяжело вздохнул и вернулся к рассказу про новую модель."
    pas "Преимущества перед старой моделью очевидны.{w=1} Нет проблем с накопителем, ведь стреляет он не лучом энергии, а шариком, который эта энергия разгоняет."
    pas "Какая убойная сила?{w=1} Ахуеть какая!{w} Шарик диаметром 3 сантиметра разгоняется до 10000 метров/секунда.{w} Спектральные сущности, в целом как и наглых людей, дырявит как нож масло."
    pas "Хочешь дам на операцию?"
    kt "Всмысле?"
    oleg "Гордон?!{w=1} Бесплатно?!"
    pas "Да-да, будет твой гонорар наперёд.{w=1} Ты же теперь мне периодически помогаешь."
    pas "Да и людям душевным не жалко."
    oleg "А мне?"
    play sound2 sfx_punch_medium volume 0.41
    scene bg int_clubs_male_day
    show image pas_smile
    with byso
    "Константин взял орудие в руки и осмотрел."
    pas "Так, а ты свой получишь со скидкой.{w} Как новый работник склада."
    oleg "Я сплю?!"
    hide image pas_smile
    show image pas_normal2
    with byso
    pas "Нет, блять, проснись, ты штаны засрал!"
    oleg "Спасибо!"
    play sound2 sfx_open_door_1 volume 1
    show image oleg_happy at cright with byso
    "Олег выбежал со склада и обнял Гордона."
    pas "Да не за что.{w=1} Только смотри, а то ненароком прожгу тебе рубашку."
    play sound2 sfx_open_door_clubs volume 1
    hide image oleg_happy
    hide image pas_normal2
    show image pas_normal
    show image oleg_smile at right
    show image liz_bukal at left
    with byso
    "В помещение вошла Лиза.{w} Олег отлип от Гордона и тот смог выкинуть бычок."
    "Она недовольно посмотрела на Константина, но после переключилась на Олега."
    liz "Олег, пошли в агроцех.{w=1} Помощь твоя нужна."
    hide image oleg_smile
    show image oleg_shy at right
    with byso
    oleg "Но я только оттуда..."
    hide image liz_bukal
    show image liz_angry at left
    with byso
    liz "Сказали надо - значит надо!{w} Им это скажешь!"
    play sound2 sfx_paper_bag volume 1
    "Олег тяжело вздохнул и, положив планшет с бумагами, пошёл на выход."
    kt "Лиза, я хотел..."
    hide image liz_angry
    show image liz_rage at left
    with byso
    liz "Перехочешь!"
    play sound2 door_cl volume 1
    hide image oleg_shy
    hide image liz_rage
    with byso
    "Прорычала она и, забрав Олега, ушла.{w=1} Константин закатил глаза и покачал головой."
    hide image pas_normal
    show image pas_angry
    with byso
    pas "Только верните Олега после обеда!"
    hide image pas_angry
    show image pas_normal
    with byso
    "Гордон неловко почесал затылок и пожал плечами."
    pas "Ёбаный по голове, всё настолько плохо?"
    kt "М-да, ну видимо не судьба."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Да нет, молодой, ты с ней поговори.{w} Но, наверное, не сегодня."
    pas "Мой тебе совет: если она тебе дорога, то оставь на время.{w} Завтра будет операция и, скорее всего, вы поедете вместе."
    kt "Не знаю. Пока не могу сказать, насколько она дорога мне."
if valeri == 1:
    kt "Валери тоже неплохой собеседник, если уж об этом."
    hide image pas_smile
    show image pas_normal
    with byso
    "Гордон недоуменно поднял бровь и посмотрел на Константина."
    pas "Странный у тебя вкус на женщин, раз она тебе нравится."
    kt "Давай не будем, а?"
    pas "Да нет...{w=1} Просто ты смотри, она хоть и не Батори, но как самка богомола."
    pas "Одна ошибка и твою голову откусят к хуям."
    "Константин тяжело вздохнул и отвёл взгляд в окно."
    jump sidfvghnuguisdgousdfgfsd2344
else:
    kt "Хотя я не могу сказать, что настолько же тесно хоть с кем-то тут связвлся."
    "Гордон улыбнулся и положил руку Константину на плечо."
    pas "Не ссы в трусы.{w} Устаканится."
    "Константин медленно и неуверенно кивнул и отвёл взгляд в окно."
    jump sidfvghnuguisdgousdfgfsd2344
label sidfvghnuguisdgousdfgfsd2344:
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Так, а я ещё не всё."
    kt "Ты про что?"
    "Гордон указал на собранный ими аппарат."
    pas "{i}Кое что{/i}..."
    kt "Что на этот раз?{w=1} Косячок травки?"
    "На такое предложение Гордон ощерился и отмахнулся."
    pas "Не, дружище, я больше по табачку."
    pas "Я тут как раз хотел напечатать {i}кое-что{/i}."
    kt "{i}Кое что{/i} печатает {i}кое-что{/i}, просто заебательный каламбур."
    pas "И не говори.{w=1} Ща."
    play sound2 sfx_click_2 volume 1
    "Гордон извлёк флешку из аппарата и вставил её в компьютер."
    hide image pas_smile
    show image pas_normal
    with byso
    pas "Как раз написал один код на этот случай..."
    kt "И что это?"
    hide image pas_normal
    show image pas_angry
    with byso
    pas "Хуйня из под коня!{w} Потерпи, а."
    kt "Ладно, как скажешь."
    hide image pas_angry
    show image pas_normal
    with byso
    "Пожал плечами Константин и сел на стол."
    play sound2 sfx_click_3 volume 1
    hide image pas_normal
    show image pas_smile
    with byso
    "Гордон улыбнулся, извлёк из компьютера флешку и вставил её в аппарат."
    pas "Заодно проверим способности этого чуда моей мысли."
    play sound_loop shock volume 0.31
    "{i}Кое что{/i} начало трястись."
    pas "Прикрой глаза, щас будет ярко."
    show blink
    "Константин, понимая, что запасной пары глаз у него нет, закрыл их."
    th "Дай угадаю.{w=1} Шкалик водки."
    play sound2 afterdead volume 1
    stop sound_loop
    scene bg black with fl_fast
    "Аппарат перестал шуметь и было слышно, что Гордон положил полученный предмет на стол."
    pas "Открывай."
    scene bg stol_a
    show image gem
    show unblink
    "Гордон указывал на стол."
    "На нём лежал камень, судя по блеску, драгоценный."
    "Формой он напоминал приплюснутый овал, а внутри него была видна вставка в виде красно-фиолетового сердечка."
    "Казалось, что камень светится сам по себе, но при повторном взгляде на него делалось ясно, на что он на это не способен."
    "Глядя на камень, Константин испытывал чувство, будто прикасается к чему-то, совершенно невообразимому, похожему на бесконечное космическое пространство."
    "Только через несколько секунд он понял, откуда взялась подобная ассоциация. Цвет камня был темно-фиолетовым, как ночное небо в грозу."
    "Пока он глядел на этот цвет, в его сознании пронеслась целая вереница зрительных образов: языки костра, небо с тучами, темно синее море."
    "Все они были очень приятными и успокаивающими."
    pas "Эу, ты чё завис, молодой?"
    scene bg int_clubs_male_day
    show image pas_normal
    with byso
    "Константин нашёл в себе силы оторвать взгляд от камня и посмотрел на Гордона."
    kt "Я чёт залип.{w=1} Шикарная получилась диковинка."
    pas "Да, теперь он твой."
    hide image pas_normal
    show image pas_smile
    with byso
if valeri == 1:
    pas "Поможет помириться с Лизой...{w=1} Ну или чтоб задобрить медсестрицу, если тебе башку захотят откусить..."
    jump sidfvghnuguisdgousdfgfsd211
else:
    pas "Поможет помириться с Лизой."
    jump sidfvghnuguisdgousdfgfsd211
label sidfvghnuguisdgousdfgfsd211:
    "Константин аккуратно взял камень в руки, словно стараясь не разбить."
    kt "И сколько с меня?"
    hide image pas_smile
    show image pas_normal
    with byso
    pas "20 долларс."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Шучу.{w=1} Бесплатно."
    kt "Серьёзно?"
    pas "Ну а что, ты помог мне собрать {i}кое что{/i}, так что мне не жалко потратить на тебя 10 сантиметров медной проволоки."
    "Константин расплылся в улыбке и убрал камень в карман джинс."
    kt "Спасибо тебе огромное."
    stop music fadeout 3
    play sound2 sfx_open_door_clubs_2 volume 1
    "Дверь мастерской распахнулась."
    show image rkis_normal at left with byso
    "Внутрь вошла робокошка."
    rkis "Требуется ТО."
    play music lim fadein 3
    play sound2 sfx_radio_squelch_2 volume 1
    hide image pas_smile
    show image pas_normal
    with byso
    andr "Гордон, как слышишь, приём."
    "Реагируя на происходящее весьма утомлённо, Гордон взял рацию со стола."
    pas "Мастерская на проводе."
    andr "Передай Константину, что он должен подойти ко мне и почини робота, который совершает ночные обходы.{w} Он должен был к тебе дойти.{w=1} Приём."
    pas "Догнал.{w=1} Уже пришла бедолага.{w} Костяна отправляю, конец базара."
    play sound2 sfx_radio_squelch_2 volume 1
    pause 0.1
    play sound sfx_dinner_horn_processed volume 1
    "Гордон отложил рацию и посмотрел на Константина.{w=1} Заиграл горн."
    pas "Ну ты слышал. {w}Рельсу можешь у меня оставить до завтра, всё равно она тебе тут ни к чему."
    kt "Увидимся."
    "Константин развернулся и направился на выход."
    hide image pas_normal
    show image pas_smile
    with byso
    pas "Подожди."
    "Он снова сделал оборот на 180."
    kt "Ась?"
    pas "Если будет вечером нехуй делать - забегай ко мне в мастерскую. {w}Обработаем желудок спиртиком."
    "Хмыкнув, Константин улыбнулся и кивнул."
    kt "Дел не будет - обязательно заскочу.{w=1} Давай."
    pas "Чао."
    play sound2 door_cl volume 1
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_clubs_day with byso
    "Константин вышел из мастерской и отправился к Андрею."
    th "Что на этот раз то?{w=1} Вроде как капитан мне уже всё сказал..."
    th "Мне кажется, мне по какой-то причине удалось расположить его к себе.{w} Каким образом сам не понимаю..."
    th "Может, и капитан мне чем-нибудь интересен."
    play sound2 light_inh volume 1
    "Константин достал сигарету и закурил.{w=1} В лёгкие потекли струйки дыма, а мозг продолжал жить своей обособленной жизнью."
    scene bg ext_square_day with byso
    th "Например, его странные перепады в настроении."
    th "То он сам всем подряд про сопротивление рассказывает, то наоборот что-то важное скрывает..."
    th "Может быть это стресс перед самой важной операцией, ради которой и строилось сопротивление?"
    th "Нет, ну если остановиться на идее, что я ему чем-то понравился...{w=1} Тут даже не особо важно, чем."
    th "Вполне возможно, что тем случаем в 22-25а.{w=1} Но как-то это странно."
    scene bg ext_admins_day with byso
    "Подходя к административному корпусу, он заметил, что робокошки не было на месте."
    th "У него тут целая куча солдат, которые с ним много лет, а он отдаёт предпочтение мне.{w} Я тут всего два дня.{w=1} Ну, три максимум."
    th "Повезло мне, не скрою."
    play sound2 sfx_close_door_1 volume 1
    play ambience ambience_camp_center_day volume 0.31 fadein 1
    scene bg int_admins with byso
    th "Лиза вообще говорила, что он параноик...{w=1} Вообще такого за ним не замечал."
    th "Просто он странный. {w}Может у него какая-то другая логика?"
    stop music fadeout 3
    th "Ладно, сейчас не об этом...{w=1} Надо узнать о новом поручении, раз он меня вызвал на ковёр."
    play sound2 sfx_knock_door7_polite volume 1
    "Константин постучал в кабинет."
    andr "Проходите."
    play music god fadein 3
    play sound2 sfx_open_door_1 volume 1
    scene bg int_admins_room2
    show image andr_angry2
    with byso
    "Капитан сидел за столом с весьма серьёзным взглядом."
    hide image andr_angry2
    show image andr_smile
    with byso
    "Увидев Константина, он поднял бровь и улыбнулся."
    andr "А, ты уже пришёл.{w} Я думал это Рита соизволила до меня дойти. {w=1}Садись, сейчас всё расскажу."
    hide image andr_smile
    show image andr_normal
    with byso
    "Поправив рубашку, Константин сел на диван, а Андрей повернулся к нему и встал со стула."
    andr "Как ты мог узнать, у нас появились проблемы с <<безбожниками>>."
    kt "Торговля в обход?"
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "Верно.{w=1} Это уже не первая проблема с их подразделением."
    andr "С того момента, как оно к нам присоединилось, каждые пол-года у них бывают разборки с остальными отрядами."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "На этот раз они прыгнули явно выше головы.{w=1} В наших правилах это не предусматривалось и мы получили уникальный случай."
    andr "Мало того, что они отказываются принимать факт контрабанды, так они еще и пытаются усидеть на двух стульях, оправдывая свой произвол тем, что они тут законодательный орган."
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Такой наглости я еще от них не встречал.{w=1} И что самое главное, я не могу им ничего доказать, потому что у меня нет доказательств.{w} У меня есть только слухи и догадки.{w=1} Правда, довольно правдоподобные."
    hide image andr_normal
    show image andr_normal2
    with byso
    "Андрей раздвинул шторы и выглянул на улицу."
    andr "И если мы не сможем эту ситуацию урегулировать, то будут проблемы."
    andr "Суть в чём.{w=1} Мне нужен человек, который сможет собрать доказательства."
    "Константин поводил взглядом по полу и потёр подбородок."
    kt "И им должен быть я?{w=1} Почему?"
    hide image andr_normal2
    show image andr_smile
    with byso
    "Капитан улыбнулся и сел на стул."
    andr "Очень просто.{w} Ты с ними не контактировал, они тебя не знают."
    andr "Твоя работа, само собой разумеется, оценится по номиналу."
    kt "Почему это не может сделать, например, Валери?"
    play sound2 sfx_paper_bag volume 1
    hide image andr_smile
    show image andr_normal
    with byso
    "Тяжело вздохнув, Андрей протянул Константину бумажку."
    andr "Валентайн сейчас занята важным проектом.{w=1} Нельзя допустить, чтоб ей кто-то мешал."
    play sound2 sfx_paper_bag volume 1
    "Взяв бумажку из рук капитана, он её осмотрел."
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "Твоя задача - выкрасть у наёмников соответствующие листы и принести мне. {w}Там мы уже оценим ущерб, нанесённый мастерской и казне."
    andr "Если они откажутся возместить ущерб, то их потребуется ликвидировать, но это уже не твоя работа."
    play sound2 sfx_paper_bag volume 1
    "Константин покачал головой и кивнул, отложив бумажку на поверхность дивана."
    hide image andr_normal3
    show image andr_normal
    with byso
    andr "Вот сумка."
    play sound2 sfx_put_sugar_cart volume 0.51
    "Андрей выдал Константину дипломат."
    kt "Хорошо, можете на меня положиться."
    hide image andr_normal
    show image andr_smile
    with byso
    "Капитан встал со стула и протянул руку."
    andr "Тогда мы договорились.{w} За успешное выполнение операции я в долгу не останусь."
    "Константин встал с места и пожал руку капитана."
    kt "Это все указания?"
    hide image andr_smile
    show image andr_normal3
    with byso
    andr "Да, можешь идти на обед.{w=1} Удачи."
    kt "Благодарю, до встречи."
    play sound2 door_cl volume 1
    scene bg int_admins with byso
    "На этих словах Константин вышел из кабинета и нахмурился."
    th "Выкрасть у наёмников ценные бумаги...{w=1} Да меня кончить могут на месте."
    "Размышляя, Константин побрёл в сторону столовой."
    th "Охрана у них наверняка хорошая, раз наёмники.{w} Находятся они в бункере..."
    th "Бывал я там, если у них там охрана, то меня ожидают не самые лучшие последствия."
    play sound2 sfx_open_door_1 volume 1
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_admins_day
    show image rkis_normal
    with byso
    "На выходе он обратил внимание на робокошку, которая вернулась в строй."
    th "Даже если охрана и не заметит, что я взял бумаги, всё равно попытаются вернуть назад."
    hide image rkis_normal with byso
    th "Точно!{w} Валери проводит эксперименты в подземке!"
    th "Попасть в подземку можно только через бункер, насколько я знаю."
    scene bg ext_square_day with byso
    "Константин пнул лежащий на земле камень в кусты, после чего посмотрел на монумент."
    th "Если постараться, можно пробраться с ней в любой момент."
    th "Проблема в том, чтобы там никого не было..."
    th "Да и время у меня ограничено.{w} Задача непростая...{w=1} Ну, ничего, проберусь..."
    th "Хотя вряд-ли бы капитан давал бы мне такую задачу, понимая, как близко находится охрана."
    th "Может сегодня наёмники по своим делам разошлись?"
    th "Маловероятно. Непонятно, где они сейчас."
    scene bg ext_dining_hall_away_day
    show image sopr_sold at cright
    show image sopr_sold2 at cleft
    with byso
    "Мимо него прошли два <<безбожника>>, которые тащили огромную коробку с подписью <<взрывоопасно>> в сторону выхода."
    th "Надо спросить у Валери, она то туда ходит раз за разом."
    hide image sopr_sold
    hide image sopr_sold2
    with byso
    th "Но могу ли я ей доверять в этом деле?{w=1} Может она в ладах с наёмниками."
    th "Один из них ей помогал...{w=1} но не за бесплатно."
    th "В одиночку я это не проверну.{w} Уж когда-когда, но не сейчас..."
    th "Пойду в соло - застрелят как собаку, это уж наверняка."
    stop music fadeout 3
    th "Короче, к чёрту.{w} Так и сделаю, я должен довериться Валери."
    play ambience ambience_dining_hall_empty volume 1 fadein 1
    scene bg int_dining_hall_day
    show mi normal pioneer
    with byso
    "Константин тяжело выдохнул и вошёл в столовую.{w=1} На раздаче стояла Мику."
    play music everyday fadein 3
    show mi grin pioneer with byso
    mip "О, здорова сержант."
    kt "Уже прапор."
    show mi angry pioneer with byso
    "Девочка на секунду поморщилась и посмотрела на кастрюли."
    mip "Любимчик блять..."
    show mi normal pioneer with byso
    "Тихо прошипела она и снова обернулась к Константину."
    mip "Тебе чего?{w} Стандартная - драники с тушёнкой.{w=1} Продвинутая - котлеты с макаронами."
    "Константин достал из карману пачку сигарет и выложил одну."
    show mi angry pioneer with byso
    "Мику засуетилась и, отвернувшись, начала накладывать еду."
    mip "Ещё и богатый..."
    "Снова пробормотала она.{w=1} Константин закатил глаза и тяжело вздохнул."
    show mi normal pioneer with byso
    "Девочка снова обернулась и выдала Константину порцию."
    kt "В следующий раз возмущайся потише."
    show mi grin pioneer with byso
    mip "Не знаю о чём ты."
    hide mi with byso
    "Оскалилась Мику, сняв перчатки.{w=1} Константин покачал головой и начал искать столик."
    "Вдалеке он заметил Гордона, Валери и Иру, которые о чём-то беседовали.{w} Без особых размышлений Константин направился к ним."
    show image pas_normal at left
    show image val_calm
    show image irr_sad at right
    with byso
    irr "... мы просто не понимаем с кем едем.{w=1} Вообще."
    "Ира и Валери сидели у пустых тарелок, а Гордон, смакуя каждый кусочек, разделывал котлету."
    hide image val_calm
    show image val_smile2
    with byso
    val "О-о...{w=1} Снова привет.{w} Садись."
    kt "Приятного, Гордон."
    hide image pas_normal
    show image pas_smile at left
    with byso
    "Гордон, не отвлекаясь от котлеты, кивнул."
    pas "Тебе тоже, молодой."
    "Пожелал он, проглотив кусок."
    kt "О чём базар?"
    "Из любопытства уточнил Константин и, поставив дипломат, приступил к еде."
    irr "Разведку расформировали и нас отправляют на операцию по сбору данных."
    irr "Знала бы что так выйдет, закупилась бы хоть..."
    hide image pas_smile
    show image pas_normal at left
    with byso
    pas "Так в чём проблема?{w=1} Я тут, молодая.{w} В мастерской буду через 10 минут, а если нет, то там сейчас Олег инвентаризацию проводит."
    hide image irr_sad
    show image irr_angry at right
    with byso
    "Услышав это имя, она нахмурилась и встала со стула."
    irr "Ну я тогда подожду тебя у мастерской.{w} Я за средствами."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Тогда увидимся."
    hide image val_smile2
    show image val_smile
    with byso
    val "Удачки."
    kt "Пока."
    play sound2 sfx_mystery_movement volume 1
    hide image val_smile
    hide image irr_angry
    show image val_smile2 at right
    with byso
    "Ира пошла на выход.{w} Валери пересела на её место."
    val "Костя...{w=1} А ты после обеда свободен?"
    kt "И да и нет."
    hide image pas_smile
    show image pas_normal at left
    with byso
    pas "Это как?"
    kt "Капитан дал одно поручение.{w=1} Какое конкретно расскажу потом."
    hide image val_smile2
    show image val_smile at right
    with byso
    "Гордон молча кивнул, словно понимая о чём говорит Константин, а Валери поправила повязку на глазу."
    val "Пойдёшь со мной?"
    kt "Да-да, помогу."
    hide image val_smile
    show image val_smile2 at right
    with byso
    "Медсестра снова улыбнулась.{w=1} На этот раз в этой улыбке не читалось никакой двусмысленной похоти."
    pas "Ты ему тоже помоги.{w} Есть у него такое дельце, которое он без тебя не провернёт."
    hide image val_smile2
    show image val_surprise at right
    with byso
    "Валери и Константин вопросительно посмотрели на Гордона."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Не, ну один в кровати не воин, но я не про это, молодые."
    kt "Спорно."
    val "Да что там такое за дело то?..."
    kt "Как пойдём в медпункт - расскажу."
    "Выдохнул Константин и продолжил есть."
    hide image val_surprise
    show image val_smile2 at right
    with byso
    val "Ладно...{w=1} А ты откуда такое прекрасное выражение взял?"
    pas "И не только его!"
    pas "За одного поебавшегося двух неебавшихся дают."
    pas "Бедность — не порок, ёбля - не приговор."
    pas "От добра ёбли не ищут."
    "Константин чуть со смеху не подавился котлетой."
    kt "Последнее в тему."
    stop music fadeout 3
    hide image val_smile2
    show image val_calm at right
    with byso
    "Валери пожала плечами и встала со стула."
    val "Я вижу ты всё.{w=1} Идём."
    play sound2 sfx_punch_medium volume 0.41
    "Константин кивнул, забрал сумку и встал со стула."
    hide image pas_smile
    show image pas_normal at left
    with byso
    pas "Покеда."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_dining_hall_near_day
    show image val_normal
    with byso
    "Сдав тарелки, они вышли из столовой и направились в медпункт."
    val "Если уж о делах...{w} У меня тоже проблемки."
    kt "Что случилось?"
    play music tish fadein 3
    hide image val_normal
    show image val_sad
    with byso
    val "У меня воры.{w=1} Сегодня ко мне поступила партия афлатоксинов, но, вот чудо, она пропала."
    kt "Так, давай по порядку.{w} Что это?"
    scene bg ext_dining_hall_away_day
    show image val_calm
    with byso
    "Валери поправила маску и потянулась."
    val "Афлатоксин - опасный органический яд, который у нас получают как продукт переработки пшеницы."
    val "Один сорт плесени, поражающий культуру его вырабатывает...{w=1} А я его использую для своих экспериментов."
    val "При смешивании с генмодом он поражает печень и сильно угнетает иммунитет, делая организм неспособным бороться с патогеном."
    hide image val_calm
    show image val_normal
    with byso
    val "У меня украли целую партию.{w=1} Около литра метанолового раствора с концентрацией 30 процентов."
    val "Если в пересчёте, этого хватит на то, чтоб отравить человек 100-200...{w=1} Ну, со стопроцентным исходом."
    kt "И чего делать?"
    "Она улыбнулась и развела руками."
    val "Да чтоб я знала.{w=1} Я изготовила для себя индикаторы и теперь проверяю каждую жидкость, которую планирую выпить."
    scene bg ext_square_day
    show image val_normal
    with byso
    kt "Индикаторы на афлатоксины?{w} Как?"
    hide image val_normal
    show image val_sad
    with byso
    val "Не-а.{w=1} На метанол."
    kt "Так а если его высушат до чистого вещества?"
    hide image val_sad
    show image val_madsmile
    with byso
    "На предположение Константина Валери мелодично рассмеялась."
    val "Тогда у нас будут слепые наёмники!"
    "Константин хмыкнул и улыбнулся."
    scene bg ext_aidpost_day
    show image val_smile
    with byso
    kt "Понял.{w=1} А что ты там с Ромой делаешь?"
    play sound2 sfx_keys_rattle volume 1
    hide image val_smile
    show image val_calm
    with byso
    "Медсестра тяжело выдохнула и достала из кармана связку ключей."
    val "И это я тоже расскажу."
    play sound2 sfx_unlock_medpunkt_door volume 1
    stop music fadeout 3
    hide image val_calm with byso
    "Открыв дверь она вошла в здание.{w=1} Константин пару секунд постоял и пошёл за ней."
    play ambience ambience_medstation_inside_day volume 1 fadein 1
    scene bg int_aidpost_day
    show image val_calm
    with byso
    play sound2 sfx_keys_rattle volume 1
    pause 0.1
    play sound sfx_clench2 volume 1
    "Она кинула ключи на стол и села на стул, после чего указала рукой на кушетку."
    play music Aleph fadein 3
    hide image val_calm
    show image val_smile
    with byso
    val "Присаживайся."
    play sound2 sfx_mystery_movement volume 1
    "Константин сел и опёрся спиной о стену.{w} Дипломат он оставил у кровати."
    hide image val_smile
    show image val_smile2
    with byso
    val "Рома сейчас на стадии живого трупа.{w=1} Буквально."
    kt "Как понимать?"
    hide image val_smile2
    show image val_smile
    with byso
    val "Вот так и понимать.{w=1} Сейчас он под капельницей из смерти..."
    hide image val_smile
    show image val_smile2
    with byso
    val "То есть смеси.{w=1} Да. {w=1}Смеси генмода и токсинов."
    scene bg scalpel with byso
    kt "И для чего?"
    "Спросил Константин, обратив внимание на окровавленный скальпель, который лежал на столе."
    val "Сделать из него что-то вроде супер-солдата."
    val "Генмод изменит его тело и боевые способности, после чего у него будет курс карательной психиатрии."
    val "Итогом будет огромный неуязвимый болван, который по указке будет убивать кого надо."
    kt "Но он же может всё вспомнить?"
    val "Исключено-о..."
    "С садистской улыбкой протянула Валери."
    val "Я ему подрежу префронтальную кору мозга, плюс поставлю внутрь пару импульсных генераторов, которые будут подавлять возможность обращаться к этому ресурсу мозга."
    kt "И как оно должно работать?"
    val "Просто...{w=1} Чертёж нам перепал от идолопоклонников. {w}У них, судя по всему, есть один мозговитый человечек, который и предложил мне в целом всю идею эксперимента."
    val "Она подключается к мозгу и работает засчёт получаемых импульсов."
    "Константин задумчиво потёр подбородок."
    kt "А если она выйдет из строя?"
    val "В таком случае она просто перестанет подавать сигналы на спинной мозг, чем ограничит возможность испытуемого двигаться."
    stop music fadeout 3
    kt "Занятно...{w=1} Ладно, тебе там надо было чем-то помочь?"
    scene bg int_aidpost_day
    show image val_smile
    with byso
    play music BlueJetta fadein 3
    "Валери наклонила голову и закинула ногу на ногу."
    val "Да.{w=1} Поговорить."
    kt "И что, я тебе и в правду настолько приглянулся?"
    hide image val_smile
    show image val_smile2
    with byso
    val "Да-а...{w=1} Ты хорошо на меня влияешь."
    kt "И в чём это выражается?"
    hide image val_smile2
    show image val_sad
    with byso
    "Она облокотилась о спинку стула и расслабленно покрутила кистями."
    val "Чувствую себя хоть немного полезной...{w=1} Нужной..."
    val "Есть маленько интересной жизни..."
    val "Ведь здесь я прозябаю и порой даже подумываю о самоубийстве, просто чтобы перестать мучить эту жестокую вселенную."
    hide image val_sad
    show image val_smile2
    with byso
    val "А ты мне даёшь хоть какой-то покой.{w} Не надо постоянно думать о том, что всё это надолго."
    val "Ты умеешь это делать и всегда можешь ответить.{w=1} Остальные смотрят на меня как на моральное уродство, распутную бабу."
    val "Я была когда-то такой бабой.{w} Но сейчас, к счастью, поумнела и поняла, какое же это мучение – быть такой..."
    kt "Рад что это так.{w} Я просто не привык смотреть на людей по общественным стереотипам."
    kt "Я смотрю на них без этих предрассудков.{w=1} Не против, если закурю?"
    hide image val_smile2
    show image val_calm
    with byso
    val "Кури..."
    "Константин достал из кармана сигарету и, начал её разминать."
    val "И мне дай, если не жалко..."
    kt "Хорошо, держи."
    play sound2 light_inh volume 1
    hide image val_calm
    show image val_smile
    with byso
    "Они закурили.{w=1} Константин выпустил дым в потолок и продолжил."
    kt "Обычно мне было свойственно подчёркивание только негативных аспектов людей, но с попаданием в сопротивление это изменилось."
    kt "Теперь я вижу и хорошее, и плохое в людях.{w=1} Есть, правда, такой момент, что плохого до сих пор намного больше."
    hide image val_smile
    show image val_calm
    with byso
    val "Вот скажи честно.{w} Что тебе не нравится во мне?"
    val "Я не обижусь, только говори правду..."
if valeri == 1:
    kt "Если честно, то значительно меньше, чем думают остальные."
    kt "Единственное, что мне в тебе не нравится - излишняя похоть."
    jump sidfvghnuguisdgousdfgfsd2117
else:
    kt "Если кратко, то излишняя жизненная наивность по отношению к Роме и излишняя похоть."
    kt "Да и в некоторые моменты не очень понимаю твою мотивацию на определённые действия."
    jump sidfvghnuguisdgousdfgfsd2117
label sidfvghnuguisdgousdfgfsd2117:
    hide image val_calm
    show image val_smile2
    with byso
    "Валери улыбнулась и наклонила голову в сторону Константина."
    val "Жестоко...{w=1} Но честно."
    hide image val_smile2
    show image val_sad
    with byso
    val "Знаешь если говорить совсем честно, то вся эта история с, как ты сказал, <<похотью>>, не больше, чем инструмент...{w=1} В последнее время."
    val "После попадания в инреальность я пересмотрела некоторые взгляды на свой стиль жизни."
    val "С нашего прошлого диалога в медпункте что-то во мне изменилось..."
    hide image val_sad
    show image val_calm
    with byso
    val "Да, возможно я ещё люблю побаловаться алкоголем и психоактивными веществами, но тот момент из своей жизни исключила."
    kt "Если ты сейчас не врёшь, то в целом, я бы об этом даже и не мог подумать."
    play sound2 sfx_open_window volume 1
    "Она затянулась и, привстав, открыла форточку."
    hide image val_calm
    show image val_smile2
    with byso
    val "Это так.{w} Именно по этому я представляю свою историю как некую сказку, нечто нереальное, словно я нахожусь в чужом сновидении.{w=1} Но за эту сказочность и галлюцинаторность мне приходилось платить..."
    val "Хоть чем-то Генда смог меня изменить, тут он бесспорно был прав."
    kt "Понимаю. {w=1}Я такого состояния ещё не достиг..."
    hide image val_smile2
    show image val_smile
    with byso
    val "Само собой.{w=1} Ты тут не так долго."
    kt "Слушай, а как ты вообще в целом относишься к психопатии?"
    hide image val_smile
    show image val_sad
    with byso
    "Валери задумчиво посмотрела на тлеющую часть сигареты."
    val "Что такое психопат?"
    "Она на несколько секунд застыла в неподвижности, словно припоминая какие-то особо яркие воспоминания."
    hide image val_sad
    show image val_calm
    with byso
    val "Это личность, которая хочет быть тем, кто она есть, но не хочет того, чем является."
    val "Она мечется взад-вперед.{w} Такая концепция психиатрии подходит к большинству людей, в том числе и ко мне."
    val "В сущности, большинство людей и есть психопаты. {w=1}Но им легче не заметить своего недуга, чем признать его."
    val "Я и сама жила в таком состоянии..."
    val "И я думаю, что такую ужасную жизнь можно рассматривать как что-то вроде оперы, где есть сцена, декорации и герой-певец, который не ведает, на что он напевает, и постоянно попадает впросак, произнося слова, которых не понимает никто, кроме него самого."
    hide image val_calm
    show image val_smile
    with byso
    val "Вот ты себя считаешь психопатом?"
    "Константина озадачил этот вопрос."
    "Он не особо задумывался, кто он, а если и задумывался — то относился к этому пофигистически и редко брал в голову."
    "Хотя иногда в нем возникало смутное подозрение, что он и в самом деле такой."
    kt "Не знаю."
    hide image val_smile
    show image val_smile2
    with byso
    val "Значит скорее да чем нет."
    kt "Резонно..."
if valeri == 1:
    hide image val_smile2
    show image val_madsmile
    with byso
    val "Знаешь, вот не к теме будет сказано...{w=1} Но ты не против пройти мою небольшую анкетку?..."
    "Валери сказала это так, что у Константина возник немой вопрос."
    kt "На тему?"
    hide image val_madsmile
    show image val_calm
    with byso
    val "Да так...{w=1} Без темы...{w=1} Буквально 7 вопросов."
    window hide
    menu:
        "Пройти.":
            $ renpy.block_rollback()
            "Константин пожал плечами и запустил бычок в открытую форточку."
            kt "Ну давай, почему нет."
        "Не проходить":
            $ renpy.block_rollback()
            kt "Не люблю тесты."
            hide image val_calm
            show image val_sad
            with byso
            "Валери тяжело вздохнула и раздавила бычок в пепельнице.{w=1} Константин выкинул его в окно."
            jump sidfvghnuguisdgousdfgfsd21171
    hide image val_calm
    show image val_smile2
    with byso
    "Она улыбнулась и, раздавив бычок в пепельнице, взяла в руки небольшой блокнот."
    scene bg valeri_cg with byso
    play sound2 sfx_paper_bag volume 1
    pause 0.25
    play sound sfx_paper_bag volume 1
    "Пролистав пару страниц, она взяла ручку."
    val "Итак, вопрос первый."
    val "Эгоист или альтруист?"
    kt "Эгоист.{w=1} Тут и думать нечего."
    val "Почему?"
    kt "Жить альтруистом - идиотизм высшей степени. {w}Давать что-то другим, чтоб остальные пользовались твоей добротой и плевали в спину.{w=1} Какой в этом толк?"
    "Валери что-то записала и отчеркнула блок."
    val "Заботливый или расчетливый?"
    window hide
    menu:
        "Заботливый.":
            $ renpy.block_rollback()
            $ valscore += 1;
            val "Почему?"
            kt "Не знаю.{w=1} Лично мне этого всю жизнь не хватало."
        "Расчётливый.":
            $ renpy.block_rollback()
            val "Почему?"
            kt "Мой основной жизненный принцип - холодный расчёт."
    "Снова что-то нацарапав на бумаге, Валери отчеркнула блок."
    val "Кто идеален?"
    kt "В реальности - никто.{w=1} В мышлении - всё."
    "Валери улыбнулась и снова сделала пометку."
    val "Хорошо сказано..."
    val "Что такое счастье?"
    kt "Иллюзия состоятельности и жизненной полноты."
    val "Почему иллюзия?"
    kt "Философский вопрос.{w=1} Всё в нашей жизни иллюзорно."
    val "Не спорю..."
    "Протянула она и снова что-то записала."
    val "Идиллический или реалистичный?"
    kt "Реалистичный.{w=1} На идилии далеко не уедешь."
    val "Хорошо..."
    "Она снова чиркнула в блокноте."
    val "Вещи и люди.{w} В чем разница?"
    kt "Субъективно.{w=1} В зависимости кто и что конкретно."
    "Без лишних вопросов Валери поставила отметку."
    val "Последний вопрос.{w=1} Разум или тело?"
    "Константин задумался."
    window hide
    menu:
        "Разум.":
            $ renpy.block_rollback()
            scene bg int_aidpost_day
            show image val_smile2
            with byso
            $ valscore += 1;
            play sound2 sfx_paper_bag volume 1
            "Валери молча что-то записала и отложила блокнот."
        "Тело.":
            $ renpy.block_rollback()
            scene bg int_aidpost_day
            show image val_smile2
            with byso
            play sound2 sfx_paper_bag volume 1
            "Валери молча что-то записала и отложила блокнот."
    kt "И чего, какой результат?"
    val "Хороший. Просто было любопытно."
    jump sidfvghnuguisdgousdfgfsd21171
else:
    "Валери раздавила бычок в пепельнице.{w=1} Константин выкинул его в окно."
    jump sidfvghnuguisdgousdfgfsd21171
label sidfvghnuguisdgousdfgfsd21171:
    stop music fadeout 3
    hide image val_sad
    hide image val_smile2
    show image val_calm
    with byso
    val "А теперь давай про дела.{w} Гордон говорил, ты говорил...{w=1} В чём дело?"
    "Константин неловко почесал затылок."
    play music deadrazy2 fadein 3
    kt "Тут дело такое...{w=1} Я даже не могу до конца понять, можешь ли ты мне помочь."
    hide image val_calm
    show image val_madsmile
    with byso
    "Она положила руку ему на колено."
    val "Могу...{w=1} Если хорошо попросишь."
    kt "Хорошо.{w=1} Какие у тебя отношения с наёмниками?"
    hide image val_madsmile
    show image val_normal
    with byso
    "Услышав упоминание <<безбожников>>, Валери убрала руку с колена Константина.{w=1} Она явно не ожидала такого вопроса."
    val "Дрейфуют между плохими и ужасными.{w=1}.. К чему вопрос?"
    "Константин кратко изложил задачу, которую ему выдал капитан."
    hide image val_normal
    show image val_sad
    with byso
    val "Мхм... Понятно.{w} Вот зачем тебе этот портфель...{w=1} Возможно, они причастны к мистической пропаже токсинов."
    kt "И это тоже.{w} Мне нужна твоя помощь.{w=1} Ты же проходишь через бункер, когда идёшь в подземку?"
    val "Да, приходится..."
    hide image val_sad
    show image val_madsmile
    with byso
    val "А-а-а, я поняла, ты хочешь прикинуться моим интерном?"
    "Валери расплылась в улыбке.{w=1} Константин не понял такой реакции."
    kt "Да, вроде того..."
    hide image val_madsmile
    show image val_smile2
    with byso
    val "Отлично!{w=1} Заодно зайдёшь и посмотришь."
    th "Ла-адно..."
    kt "Хорошо, когда идём?"
    hide image val_smile2
    show image val_calm
    with byso
    "Валери встала со стула и собрала вещи со стола."
    val "Сейчас..."
    "Константин кивнул и встал с места, не забывая про дипломат."
    kt "Отлично, если так."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_aidpost_day
    show image val_smile
    with byso
    val "Давно же я не гуляла с парнями...{w=1} Напоминает про школьные времена..."
    kt "Мне лично вспомнить нечего."
    hide image val_smile
    show image val_calm
    with byso
    val "А чего так?..."
    kt "Чмырили меня.{w=1} По-полной."
    val "Было за что?"
    "Спросила Валери, поправив свой хвостик."
    kt "Да.{w=1} И имя этой причине - доброта."
    hide image val_calm
    show image val_sad
    with byso
    val "Не знаю...{w=1} Я ценила доброту в людях."
    val "Я росла в семье нежеланной, потому каждый лучик доброты был для меня словно освежающий душ..."
    val "Душ, который наполнял теплом и смыслом мою жизнь."
    val "Этот душ, когда он был нужен, не даровал мне почти никто, потому я и выросла такой, однако с этим уже ничего не поделаешь."
    kt "Тогда ты меня в этом плане понимаешь."
    kt "В один день я нашёл ту самую, с которой хотел прожить всю жизнь."
    hide image val_sad
    show image val_calm
    with byso
    val "Тогда почему ты здесь?"
    "Константин потёр своё запястье и посмотрел в небо."
    scene bg ext_square_day
    show image val_calm
    with byso
    kt "Моя первая и единственная девушка покончила с собой."
    hide image val_calm
    show image val_sad
    with byso
    "Валери сочувственно покачала головой и положила руку ему на плечо."
    val "Печальная история.{w=1} Я представляю, каково было тебе..."
    val "Слыша такое, люди постоянно пытаются давать советы."
    val "А советы как ни раздаются, все время мешают."
    hide image val_sad
    show image val_calm
    with byso
    val "Причина этого – неспособность людей увидеть невидимое."
    val "А именно то, что они вовсе не способны представить такое, не пережив этого."
    val "Поэтому их субъективные проекции на реальность подобны энцефалограмме, сделанной на электрическом стуле."
    hide image val_calm
    show image val_smile
    with byso
    "Она, прогладив плечо Константина, убрала руку."
    kt "Отличное сравнение, там ничего не сказать.{w=1} Так всё и есть."
    "За их беседой Константин обратил внимание на Лизу, которая сверлила Константина раздражённым взглядом."
    th "М-да...{w=1} Что-то я не пойму никак: заинтересована ли она в том, чтоб наладить наши отношения?"
    th "Или просто продолжает сердиться на меня и уже окрестила нелюдем?"
    th "Я, конечно, всё равно человек, но людей не так называют."
    th "Тут я уже решил."
    hide image val_smile
    show image val_calm
    with byso
    val "Что ты там увидел?..."
    "Из любопытства просила Валери, подняв бровь."
    kt "Лизу.{w=1} Неужели до сих пор злится?"
    hide image val_calm
    show image val_normal
    with byso
    "Валери тяжело вздохнула и развела руками."
    val "Хрен её знает...{w=1} Так и будет проводить одиночные пикеты на тему того, что я недостойна жизни."
    kt "А ты ей что-то сделала?"
    hide image val_normal
    show image val_angry
    with byso
    val "Лично ей - нет...{w=1} Но ей всегда не нравились мои эксперименты."
    val "Она просто не понимает, что мои эксперименты направлены на улучшение её жизни и безопасности."
    scene bg ext_path2_day
    show image val_calm
    with byso
    "Валери и Константин вышли на лесистую тропу."
    val "Вот вопрос к тебе нескромный..."
    kt "Ну жги."
    hide image val_calm
    show image val_smile2
    with byso
    val "Ты девственник?"
    "Константин тяжело вздохнул и отрицательно помотал головой."
    kt "К сожалению нет."
    hide image val_smile2
    show image val_normal
    with byso
    val "Почему к сожалению?"
    "Он засмотрелся на кроны деревьев, после чего почесал шею."
    kt "Да что там.{w=1} Мясная возня."
    kt "Я девственности лишился под веществами на вписке.{w} Для меня это осело отвратным осадком на памяти."
    hide image val_normal
    show image val_madsmile
    with byso
    hide image val_madsmile with byso
    "Валери усмехнулась, а маска слетела с её лица."
    show image val_madsmile with byso
    "Подтянув резинку на ухо, она хихикнула."
    val "А мы похожи.{w=1} Я так-же."
    kt "Не знаю.{w=1} Для меня секс с незнакомым человеком неприятен."
    hide image val_madsmile
    show image val_calm
    with byso
    val "Да, опыт так себе. Верю."
    val "Но у меня есть такой жизненный пример."
    kt "Какой?"
    hide image val_calm
    show image val_smile
    with byso
    val "На одной из летних практик на третьем курсе мне нужно было засунуть руку в брюшную полость трупика и найти там почку."
    hide image val_smile
    show image val_sad
    with byso
    "Тяжело вздохнув, Валери снова поправила маску и посмотрела Константину в глаза."
    val "Один раз я попыталась взять над собой верх и сделать это, но не могла - было мерзко."
    hide image val_sad
    show image val_normal
    with byso
    val "В тот момент преподаватель схватил меня за запястье и силой протянул в нужную строну."
    val "Именно после этого я перестала этого бояться. Я поняла что в этом нет ничего такого.{w} Сама бы я туда никогда не полезла..."
    hide image val_normal
    show image val_calm
    with byso
    val "В твоём случае всё так-же. Тебе просто нужен тот, кто покажет, как это на самом деле, иначе так и никогда не сможешь."
    stop music fadeout 3
    "Константин поднял бровь и посмотрел в землю. Ему такое сравнение показалось странным."
    "Сравнивать секс и работу патологоанатома для него было чем-то немыслимым."
    kt "Сравнение странное, но посыл я понял."
    play music KillReligionInItself fadein 3
    scene bg ext_old_building_sunset:
        size (1920, 1080)
        crop (497, 223, 980, 630)
    show image sopr_sold
    show image me_sm at right
    with byso
    "Вдалеке виднелся старый корпус. {w=1}На пороге стоял наёмник, а перед ним встал какой-то Семён."
    "Семён достал какую-то бумажку и отдал её наёмнику."
    hide image me_sm with byso
    "Наёмник её прочитал и пропустил его."
    scene bg ext_old_building_sunset:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 1 crop (0, 0, 1920, 1080)
    with byso
    show image val_angry
    with byso
    val "Так-с, а это уже наводит на мысли."
    kt "Ты о чём?"
    hide image val_angry
    show image val_dontlike
    with byso
    val "Какого хрена Семён забыл у них в бункере?"
    kt "Ну это мы можем узнать."
    hide image val_dontlike
    show image sopr_sold
    show image val_normal at right
    with byso
    "Константин и Валери подошли к охраннику."
    sold "А это ещё кто?"
    hide image val_normal
    show image val_smile2 at right
    with byso
    val "О-о...{w=1} А это мой любимый интерн.{w} Костя."
    "Солдат повернул голову в сторону Константина и осмотрел его сверху вниз, остановив взгляд на сумке."
    sold "Он должен разоружиться и показать содержимое сумки."
    hide image val_smile2
    show image val_calm at right
    with byso
    "Проговорил он и начал приближаться к Константину."
    hide image val_calm
    show image val_calm at cright
    with byso
    "Валери встала перед ним."
    val "Дорогой мой друг, будь добр пропусти нас."
    sold "Я вас не пропущу, пока вы..."
    hide image val_calm
    show image val_angry at cright
    with byso
    val "Не-ет, ты меня не понял...{w=1} Ты пропускаешь нас."
    sold "Не пропущу я..."
    hide image val_angry
    show image val_dontlike at cright
    with byso
    val "Ты{cps=6}...{/cps} Нас{cps=6}...{/cps} Пропускаешь{cps=6}...{/cps}"
    val "Или{cps=6}...{/cps} Твой{cps=6}...{/cps} Нарезанный{cps=6}...{/cps} Труп{cps=6}...{/cps} Пойдёт{cps=6}...{/cps} На{cps=6}...{/cps} Корм{cps=6}...{/cps} <<Чернобогу>>{cps=6}...{/cps}"
    val "Я{cps=6}...{/cps} Понятно{cps=6}...{/cps} Выразилась?{cps=6}...{/cps}"
    hide image sopr_sold
    show image sopr_sold at cleft
    with byso
    "Солдат тяжело вздохнул и отошёл с пути."
    sold "Иди."
    play ambience ambience_camp_center_day volume 0.51 fadein 1
    scene bg int_old_building1
    show image val_angry
    with byso
    "Недовольно пробурчал охранник.{w=1} Константин и Валери пошли к люку."
    val "Не понимают они человеческую речь...{w} Явно проблемы со слуховым центром."
    play ambience ambience_catacombs volume 1 fadein 1
    scene bg int_catacombs_entrance
    show image val_calm
    with byso
    play sound2 sfx_click_2 volume 1
    "Спустившись вниз, Валери достала фонарик и посветила вдаль."
    val "Ну пошли."
    kt "Тебя не пугает, что тебя они могут убить?"
    hide image val_calm
    show image val_smile
    with byso
    val "Не особо...{w=1} Моё время реакции куда меньше, чем время, которое им потребуется чтоб достать оружие."
    kt "А если со спины?"
    hide image val_smile
    show image val_smile2
    with byso
    val "А от этого, дорогой мой интерн, никто не застрахован."
    "С приятной улыбкой протянула Валери."
    scene bg int_catacombs_door
    show image val_angry
    with byso
    "Через какой-то промежуток времени они дошли до бункера.{w=1} Замок на двери был открыт."
    val "О, а они дома."
    "Недовольно прошептала Валери и оттолкнула дверь."
    scene bg int_catacombs_living
    show image val_surprise
    with byso
    "Как не странно, внутри никого не было.{w=1} На столе были разложены бумаги."
    kt "Подожди, а где тот чувак?"
    val "Не знаю...{w=1} Вот совсем..."
    hide image val_surprise
    show image val_angry
    with byso
    val "Хотя нет..."
    "Проговорила Валери и посмотрела на открытую дверь слева."
    hide image val_angry
    show image val_dontlike
    with byso
    val "Ищи нужные документы и побежали."
    play sound2 sfx_paper_bag volume 1
    "Константин достал из сумки бумажку и начал сравнивать её с остальными."
    play sound2 sfx_paper_bag volume 1
    "На столе он достаточно быстро отыскал нужный документ и подменил его."
    kt "Окей, бежим."
    hide image val_dontlike with byso
    "Валери подорвалась в сторону подземки.{w=1} Константин побежал за ней."
    scene bg int_mine_halt
    show image val_angry
    with byso
    val "Направо-направо-налево-прямо-налево-прямо-налево."
    "Константин кивнул и побежал за Валери."
    scene bg int_mine with byso
    "Хоть ему и не было понятно к чему спешка, но Валери выглядела весьма обеспокоенно."
    "Вот только тревогу её наигранной назвать было нельзя.{w=1} У нее на лице четко отпечаталась работа мысли."
    "Словно она решала сложную головоломку, и уже в сотый раз приходила к выводу, что решение все равно будет неправильным."
    play music deadrazy4
    play sound_loop bolgarka volume 0.4 fadein 3
    play sound krik_far
    pause 1
    "Шахты разразились лязгом пилы и криками."
    show image val_scared with byso
    val "Блять!{w=1} Он решил уничтожить мой эксперимент!"
    val "Быстрее!!!"
    "Теперь Константину всё стало ясно."
    "Тот парень решил помешать Валери провести эксперимент."
    hide image val_scared with byso
    "Валери ускорилась вдвое, Константин просто перестал за ней успевать."
    stop sound_loop fadeout 3
    "Со стороны все выглядело как обычное противостояние двух молодых людей — но только если смотреть на ситуацию предвзято."
    "А если это уже начал понимать и сам Константин, ситуация становилась куда как серьезней."
    scene bg int_mine_door
    show image val_dontlike
    with byso
    "Наконец, они добежали до нужной двери."
    play sound2 door_break volume 1
    scene bg int_inventory_room
    show image pi_blood at cleft
    with vpunch
    play sound ammo volume 1
    "Константин выхватил пистолет и, толкнув дверь, прицелился в Семёна."
    show image val_angry at right with byso
    "Валери вбежала за ним, а Семён целился точно в Константина и давил лыбу."
    hide image val_angry
    show image val_surprise at right
    with byso
    "На кушетке лежал Рома, чья голова была отрублена резаком для костей."
    hide image val_surprise
    show image val_dontlike at right
    with byso
    val "Мразь!{w=1} Что ты сделал?!"
    me "Я?{w=1} Дал сопротивлению будущее."
    window hide
    $ renpy.block_rollback()
    $ time = 25000
    $ timer_range = 25000
    $ timer_jump = 'vjfiodsjvbnuifdsvbhnuidfhnfuibhisudbiu'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Застрелить Семёна.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            play sound2 pistol volume 1
            hide image val_dontlike
            show image val_surprise at right
            with byso
            "Константин выстрелил, но из-за усталости промахнулся."
            play sound2 pistol volume 1
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            scene bg black with vpunch
            "Выстрел."
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
        "Держать на мушке.":
            $ renpy.block_rollback()
            stop sound3 fadeout 1
            jump vjfiodsjvbnuifdsvbhnuidfhnfuibhisudbiu
label vjfiodsjvbnuifdsvbhnuidfhnfuibhisudbiu:
    hide screen inreal_countdown
    stop sound3 fadeout 1
    "Константин решил повременить с выстрелом и продолжил держать Семёна на мушке, параллельно пытаясь отдышаться."
    kt "Какое будущее, обморок?! {w=1}Ты просто попортил его частную собственность!"
    "Пионер молчал и продолжал улыбаться, после чего перевёл ствол на Валери."
    me "Частная собственность?!{w=1} Это был человек!"
    me "Вы не понимаете, вы идиоты!{w=1} Вы...{w=0.15}{nw}"
    play sound2 pistol volume 1
    hide image pi_blood with vpunch
    "Константин спустил курок."
    "Семёна повело в сторону, и он повалился на левый бок."
    play sound2 pistol volume 1
    pause 0.24
    play sound head_crush volume 0.7
    "Константин, не целясь, выстрелил ещё раз."
    "На этот раз Семёну, судя по характерному хрусту, пробило кисть руки."
    hide image val_dontlike
    show image val_mad at right
    with byso
    val "Ты мне заплатишь, мешок с костями!"
    play sound2 sfx_lena_hits_alisa volume 1
    scene bg val_murder:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 1.5 crop (0, 0, 1920, 1080)
    with fl_scare
    play sound_loop knife_hits volume 1
    play sound3 krik2 volume 1
    "Валери охватила ярость и она, достав пилу, начала нарезать парня в салат, а Семён начал истошно кричать."
    "Впрочем, это было скорее похоже на то, как двое взрослых делают мелкую перепланировку своего пространства."
    val "Я твой мозг тебе в прямую кишку затолкаю!!!"
    "Во всяком случае, по ее меркам. {w=1}Ему она полностью отпилила руку."
    "Кровь брызнула в разные стороны."
    "Он кричал, пока Валери срезала ему голову.{w=1} Из его рта вырывались хрипы."
    "Они становились все громче и громче, и вскоре Семену удалось замолчать.{w=1} Его голова плюхнулась на пол."
    "Окровавленная пила, погружалась в мозг Семена все глубже и глубже."
    "Голова за несколько мгновений превратилась в бесформенный кусок мяса."
    stop sound_loop fadeout 2
    stop music fadeout 3
    scene bg int_inventory_room
    show image val_black
    with byso
    play sound2 sfx_pat_shoulder_hard volume 1
    "Константин на свой страх и риск подошёл к Валери и взял её за плечо.{w=1} Она застыла в статичном положении."
    kt "Валери, хватит, он уже мёртв."
    play music stresss fadein 3
    "Она молча встала и наклонила голову в правую сторону."
    val "Я должна была отомстить Роме...{w=1} Но не смогла."
    val "Костя...{w=1} Иди к капитану, доложи о произошедшем...{w=1} Сейчас..."
    kt "Но ты..."
    val "Иди!"
    "Прорычала Валери не оборачиваясь во тьме."
    "Константин убрал руку с её плеча и отошёл."
    "Он хотел что-то сказать, но понял, что Валери сейчас нестабильна, потому направился на выход."
if valscore > 0:
    val "Приходи...{w=1} Потом..."
    "Пробормотала она Константину в спину. Он не понимал, ему ли это было или это мысли вслух."
    jump sidfvghnuguisdgousdfgfsd2351
else:
    jump sidfvghnuguisdgousdfgfsd2351
label sidfvghnuguisdgousdfgfsd2351:
    scene bg int_mine_door with byso
    "Константин вышел из инвентарной и направился к капитану."
    stop ambience fadeout 0.5
    scene bg int_admins_room2
    show image andr_normal
    with fade
    play ambience ambience_camp_center_day volume 0.31 fadein 0.5
    kt "Эксперимент Валери провалился."
    hide image andr_normal
    show image andr_normal2
    with byso
    "Андрей пару секунд смотрел на стену, словно пытаясь воспринять услышанное."
    play sound2 wood_hit_head volume 1
    hide image andr_normal2
    show image andr_rage
    with vpunch
    "Осознав, что сказал Константин, он со всей силы ударил кулаком по столу."
    andr "Что значит провалился?!"
    kt "Семён по сговору с наёмниками пробрался в шахты и перерезал испытуемому глотку косторезом."
    "Капитан закипел."
    andr "Он жив?!"
    kt "Оказал сопротивление, потому был убит."
    play sound2 wood_hit_head volume 1
    "Он ещё раз ударил кулаком по столу." with vpunch
    andr "Откуда ты знаешь, что он в сговоре с наёмниками?!"
    kt "На входе он выдал охраннику некую бумажку, после чего его пропустили внутрь."
    hide image andr_rage
    show image andr_nervous
    with byso
    "Андрей схватился за голову."
    andr "Чёртовы наёмники!"
    hide image andr_nervous
    show image andr_normal
    with byso
    "Сделав 5-10 глубоких выдохов, Андрей пришёл в нормальное состояние."
    andr "Ты расследовал то, что я просил?"
    play sound2 sfx_paper_bag volume 1
    "Константин молча протянул капитану нужную бумагу."
    play sound2 sfx_paper_bag volume 1
    hide image andr_normal
    show image andr_normal3
    with byso
    "Взяв её, Андрей поводил по ней взглядом, после чего отложил на стол."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "Позиций втрое больше чем нашей ведомости."
    play sound2 sfx_radio_squelch_2 volume 1
    hide image andr_normal2
    show image andr_normal3
    with byso
    "Андрей взял со стола микрофон и нажал на кнопку."
    andr "Все <<безбожники>> собираются на площади через полчаса. Неявка карается."
    hide image andr_normal3
    show image andr_normal2
    with byso
    "Отставив микрофон, он взял рацию."
    play sound2 sfx_radio_squelch_1 volume 1
    andr "Гордон, как слышно, приём."
    pas "Капитан, что за шумиха, что происходит? Приём."
    andr "Потом.{w=1} Перевести всех робокошек в режим активной охраны и выписать из дружественного реестра всех наёмников. Возьми двоих с собой, как понял? Приём."
    pas "Ёбаный по голове, а чё за суета? Приём."
    andr "Требуется.{w=1} Информация потом. Конец связи."
    play sound2 sfx_radio_tune volume 1
    "Андрей поменял частоту на рации."
    andr "Капитан вызывает охрану, приём."
    ohra "Охрана слушает. Приём."
    andr "У вас сейчас все Семёны на месте? Приём."
    ohra "Так точно.{w=1} Все 7 человек."
    andr "Собирайте всех и на площадь.{w=1} Срочно!"
    ohra "Команда ясна, конец связи."
    play sound2 sfx_radio_squelch_2 volume 1
    hide image andr_normal2
    show image andr_normal
    with byso
    "Капитан отложил рацию и снова перевёл взгляд на Константина.{w=1} В его глазах читалась стерильная пустота."
    andr "А началось всё из-за воровства продовольствия..."
    kt "Что планируется делать?"
    hide image andr_normal
    show image andr_normal2
    with byso
    andr "Мы их изгоняем.{w=1} Если они сопротивляются - то мы их отправим под трибунал."
    kt "Неужели эксперимент был настолько важен?"
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Так точно.{w} Успех был бы величайшим прорывом...{w=1} Но наёмники всё испортили."
    andr "Теперь мы все идём на площадь.{w=1} Сейчас."
    "Проговорил капитан и встал со стула."
    stop music fadeout 3
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_square_day
    show image tolpa
    show image andr_normal
    with fade
    "На площади собралась толпа.{w=1} Множество рядовых сопротивления стояли и не могли понять, что происходит."
    andr "Охрана будет с минуты на минуту. {w=1}Идём."
    hide image andr_normal
    show image andr_normal2
    with byso
    "Встав по правую сторону площади, Константин остановился справа от капитана."
    play music Waijdan fadein 3
    show image rkis_normal at cleft
    show image rkis_normal2 at fleft
    show image pas_normal at left
    hide image andr_normal2
    show image andr_normal2
    with byso
    "По требованию пришёл Гордон, а с ним две робокошки."
    show image Ohra_normal at right
    hide image andr_normal2
    show image andr_normal2
    with byso
    "За ними пришёл мужик в камуфляже."
    ohra "Мой отряд на месте."
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Мы ожидаем наёмников."
    hide image andr_normal
    hide image rkis_normal2
    hide image rkis_normal
    hide image pas_normal
    hide image Ohra_normal
    with byso
    show image sopr_sold:
        xanchor 0.1
    show image sopr_sold2:
        xanchor 0.2
    show image sopr_sold3 at left
    show image Ohra_normal at fright
    show image andr_normal at right
    with byso
    "Со стороны библиотеки вышла толпа из 6ти наёмников.{w=1} Они встали по левую сторону площади."
    hide image andr_normal
    show image andr_angry at cright
    with byso
    andr "<<Смердяков>>! {w=1}Сами признаетесь, или нам напомнить?"
    sold_sm "Что тебе от нас надо?"
    hide image andr_angry
    show image andr_nervous2 at cright
    with byso
    andr "Вы воровали у нас снаряжение!{w=1} Вы нас обманывали и вы обрушили эксперимент <<Чернобог>>!{w=1} Что вы скажете в своё оправдание?!"
    "Размяв шею, солдат приподнял голову."
    sold_sm "Бывают моменты, когда ради защиты стоит засунуть свой язык в жопу и сидеть молча, не вмешиваясь в чужие дела, ка-пи-тан!"
    sold_sm "Жопа всегда поймет и простит!{w=1} Да и чаще всего у вас все дела именно в жопе!"
    hide image andr_nervous2
    show image andr_angry2 at cright
    with byso
    andr "Да что ты мне говоришь?!{w=1} Дела наши в жопе именно их-за ваших выходок!"
    sold_sm "Так делать ваши дела никто не просил!{w=1} Ваша задача просто давать бабло и не лезть в наши дела!"
    hide image andr_angry2
    show image andr_angry at cright
    with byso
    andr "Дела, которые подразумевают воровство и убийство наших людей нас не интересуют, <<Смердяков>>!"
    sold_sm "А, это жизнь, в которой на помойке сдохнут ваши дети?{w=1} Любопытно."
    hide image andr_angry
    show image andr_nervous2 at cright
    with byso
    andr "Урод, по нашему соглашению воровство карается!{w=1} Какого хрена тогда твои наёмники стырили у нас втрое больше товаров чем купили?!"
    sold_sm "Украли, да, но и заплатили мы им за это адекватные деньги!{w=1} А-де-ква-тны-е!{w} Хуй вам в сраку!"
    sold_sm "Мы не готовы отказаться от того, что нам отдают с большим дисконтом, чтобы получить такое же качество!"
    sold_sm "Вы сами задрали ценники до такого уровня, что нам было не потянуть!"
    sold_sm "Вам не нравится?{w=1} Идите в хуй со своими ценами!"
    hide image andr_nervous2
    show image andr_angry at cright
    with byso
    andr "Никто не тянет!{w=1} Когда мы хотим получить продукцию в готовом виде - нам приходится идти на жертвы!{w=1} Каждый товар стоит своих денег! {w=1}Если не надо - не бери!"
    sold_sm "Капитан-капитан, так и не учит тебя ничего!{w=1} Выбор за тобой! {w}Надо - найди себе других бобров, которые будут тебе сраку лизать!"
    hide image andr_angry
    show image andr_rage at cright
    with byso
    "Андрея задели эти слова, а <<Смердяков>> насмешливо сверкнул стёклами противогаза."
    andr "Значит слушай сюда, морда обнаглевшая!{w=1} За нарушение параграфа #3 нашего договора вы катитесь из этой симуляции далеко и надолго, после чего сюда больше никогда не возвращаетесь!"
    andr "У вас 20 минут на то, чтоб сесть в автобус и уехать в другой сектор, иначе будут последствия!"
    andr "Ваше имущество изымается в качестве компенсации ущерба, нанесённого мастерской, а теперь валите, пока ноги целы."
    play sound2 cloth volume 0.76
    hide image sopr_sold3
    show image sopr_soldb at left
    with byso
    "Их главный подкрутил противогаз и сорвал нашивку сопротивления со своего плеча."
    play sound2 cloth volume 1
    pause 0.25
    play sound cloth volume 0.81
    "По его примеру последовали и остальные, сорвав нашивки и растоптав их."
    sold_sm "Ты смотри, как бы тебе потом не пришлось заплатить за свои слова, четырёхглазый!"
    hide image sopr_soldb
    hide image sopr_sold
    hide image sopr_sold2
    with byso
    "Прорычал наёмник и, сделав над собой круговое движение рукой, отправил всех своих ребят в автобус."
    hide image andr_rage
    show image andr_angry at cright
    with byso
    andr "Охрана и робокошки, сопроводить их до уезда, после чего осмотреть весь периметр симуляции.{w=1} Сегодня усиленный пост."
    rkis "Принято."
    ohra "Так точно, капитан!"
    hide image andr_angry
    show image andr_normal at cright
    with byso
    andr "Остальные, вольно."
    stop music fadeout 3
    hide image andr_normal
    hide image Ohra_normal
    with byso
    hide image tolpa with byso
    "После того, как наёмники скрылись за воротами лагеря, толпа начала расходиться, а Андрей направился обратно в административный корпус."
    "Гордон пошёл за ним и начал распрашивать его о произошедшем."
    play sound2 light_inh volume 1
    play music god fadein 3
    "Константин сел на скамейку и закурил."
    th "Ебануться...{w=1} Неплохие я такие изменения внёс в сопротивление..."
    th "Но зачем наёмникам было портить эксперимент?"
    th "Вроде задачу выполнял не их штатный человек, но тот был явно в сговоре..."
    th "В целом остался один вопрос - какие именно изменения я внёс?"
    th "Хорошие? {w=1}Плохие?{w=1} Какие?"
    th "К чему они привели?"
    th "Что-то я совсем запутался..."
    th "Что делать дальше?"
    th "У нас больше нет квалифицированных людей, а у нас завтра военная операция.{w=1} Да ещё какая!"
    th "Можно прямо завтра собирать манатки и выезжать в бой, чтобы осуществить <<Праведное дело>>."
    "Константин встал со скамьи и, после недолгих размышлений, решил пойти к Гордону."
    th "Он же вроде должен был узнать, что мы будем дальше делать..."
    th "Интересно, как там Валери..."
if valscore > 0:
    th "Та ярость, которая её охватила, явно не была наигранной..."
    th "Я её понимаю..."
    th "Взрыв ярости – это такой же процесс, как и физическая тошнота. {w=1}Трудно на это не реагировать."
    jump sidfvghnuguisdgousdfgfsd23515
else:
    th "Ей скорее всего надо побыть одной..."
    jump sidfvghnuguisdgousdfgfsd23515
label sidfvghnuguisdgousdfgfsd23515:
    th "А Лиза?"
    th "Может она хоть завтра соизволит поболтать?"
    th "По крайней мере, вероятно, что завтра мой последний день..."
    th "Хотя... {w=1}Ситуация из категории всё или ничего."
    th "Интересно, чем будет заниматься сопротивление, если полностью захватит инреальность?"
    th "Это же фактически инструмент бога.{w=1} Полный доступ ко всем тайнам мира."
    scene bg ext_clubs_day with byso
    "Константин дошёл до мастерской и, выкинув бычок, сел на ступеньки."
    th "Неограниченные возможности.{w=1} Не потеряет ли тогда человеческая жизнь смысл?"
    th "Или уже потеряла?{w=1} А может, и не нужен он вообще?"
    th "Скорее всего, все силы уйдут на решение парадокса бога.{w=1} Может ли сверх-существо создать такой камень, который не сможет поднять?"
    th "Вполне возможно, что это будет бесконечное исследование."
    th "А человек?"
    th "Что будет делать человек — неважно.{w} Он, в сущности, будет занят не столько развитием своих возможностей, сколько бесконечным самосовершенствованием."
    th "Ведь кто-то должен заботиться о перспективе. {w=1}Грех было бы не воспользоваться такой возможностью."
    th "Тогда уж надо стать бесконечно совершенным.{w} И только тогда...{w=1} Тогда ведь можно будет прыгнуть в вечность."
    th "Только придется ее пережить, как она сама."
    show image pas_normal2 with byso
    "К мастерской, покуривая сигарету пришёл Гордон."
    pas "Рано ты.{w} Я ещё не закончил с работой."
    kt "Я по другому поводу."
    hide image pas_normal2
    show image pas_normal
    with byso
    pas "А, тебе интересно знать что там с наёмниками?"
    "Константин встал со ступенек и медленно кивнул."
    pas "Ну, если кратко, Андрей решил изолировать их от сопротивления."
    hide image pas_normal
    show image pas_angry
    with byso
    pas "Они много всего спиздили.{w} Я посмотрел их лист и у меня чуть волосы не выпали, ёбаный по голове!"
    pas "Патроны, линзы для лучевых лазеров...{w=1} В сигаретном эквиваленте это исчислялось блоками! {w=1}Столько сил ушло на ветер..."
    hide image pas_angry
    show image pas_normal2
    with byso
    pas "Воровки блять недотраханные!{w=1} Так и знал, что они что-то промышляют!"
    "Тяжело вздохнув, Константин опёрся о веранду."
    kt "И что мы будем делать без наёмников?"
    hide image pas_normal2
    show image pas_normal
    with byso
    pas "Охранять капитана самостоятельно.{w=1} Он сейчас как раз сел переписывать план завтрашней операции."
    kt "А какой был?"
    hide image pas_normal
    show image pas_normal at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Гордон подошёл к Константину и наклонился к его уху."
    pas "В душе не ебу."
    hide image pas_normal
    show image pas_normal
    with byso
    "Прошептал он и опёрся на противоположную часть веранды."
    pas "Он планировал дать нам инструктаж, пока мы будем ехать в автобусе."
    kt "И чего, нам далеко ехать?"
    pas "Нет, не то что..."
    stop music fadeout 3
    oleg "Гордо-он!!!"
    show image oleg_happy at right
    hide image pas_normal
    show image pas_normal at left
    with byso
    "К мастерской летел Олег, размахивая над собой чем-то вроде чертежа."
    oleg "Смотри что я нашёл в старом корпусе!"
    play sound2 sfx_paper_bag volume 1
    hide image pas_normal
    show image pas_angry at left
    hide image oleg_happy
    show image oleg_smile at right
    with byso
    "Гордон взял у Олега чертёж, и развернув его, начал вчитываться."
    pas "И какого хуя ты там..."
    hide image pas_angry
    show image pas_normal at left
    with byso
    pas "Стоп..."
    play music MamaRussia fadein 3
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Ебаный по голове, да это же мой доработанный чертёж спектрального дезинтегратора!"
    play sound2 sfx_open_door_kick volume 1
    hide image pas_smile
    hide image oleg_smile
    show image oleg_shy at right
    with byso
    "После этих слов он распахнул дверь мастерской и влетел внутрь."
    "Константин и Олег переглянулись, пожали плечами и пошли за ним."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg int_clubs_male_sunset
    show image pas_smile at left
    show image oleg_shy at right
    with byso
    pas "Ебать мой лысый хуй!{w=1} Так это же просто заебательно!"
    "Взяв карандаш и линейку, он начал наносить на чертеже линии и делать себе пометки."
    pas "Олег, живо!{w} Тащи сюда латунные трубы диаметром 10 сантиметров, запчасти от пулемёта, лазерную указку и сварочный аппарат!"
    play sound2 sfx_open_door_clubs volume 1
    hide image oleg_shy with byso
    "Олег снова пожал плечами и пошёл на склад."
    pas "Костя, ебаный по голове, молодой, я буду сейчас творить историю!"
    "Судя по звукам, Олег на складе что-то сломал, но Гордон был настолько увлечён своей затеей, что ему просто не было дела."
    kt "Но скоро ужин..."
    pas "Ебал я этот ужин!{w} Я сейчас такое смастерю!"
    pas "Мать моя женщина!{w=1} Наконец я нашёл этот чертёж!{w} Я ебучий гений!"
    play sound2 sfx_close_door_1 volume 1
    show image oleg_shy at right with byso
    "Олег вышел со склада со всеми запрошенными вещами.{w} Константин смекнул, что сейчас никому до него не будет дела."
    kt "Ладно, удачи смастерить."
    stop music fadeout 3
    play sound2 sfx_open_door_clubs_2 volume 1
    play ambience ambience_camp_entrance_evening volume 1 fadein 1
    scene bg ext_clubs_day with byso
    "Выдохнул Константин и вышел из клубов."
    th "Спектральный дезинтегратор.{w=1} Вроде Гордон только сейчас умудрился сделать новый рельсотрон."
    "Из окна клубов показалась яркая вспышка, а Константин направился вглубь лагеря."
    play music proshloe fadein 3
    th "Последний день.{w=1} Во всех смыслах."
    th "Либо мы завтра победим и обретём идеальные условия для жизни, либо мы проиграем и умрём."
    th "Третьего не дано..."
    scene bg ext_square_sunset with byso
    play sound2 sfx_pat_shoulder_hard volume 1
    "Константин стукнул себя по лбу."
    th "Что за бред!{w} Какой раз я об этом думаю?!"
    th "Я хочу встретить этот день подобающим образом!"
    th "Без страха."
    th "И без тлена."
    play sound2 sfx_dinner_horn_processed volume 1
    "Заиграл горн.{w=1} Константин повернул в сторону столовой и пошёл на ужин."
    th "Столько всего за день...{w=1} В позитивном смысле."
    th "Я и не думал, что жизнь может быть настолько насыщенной.{w=1} Никогда."
    th "За сегодня я:..."
    th "Посрался с единственной до сегодняшнего дня подругой."
    th "Нашёл новую."
    th "Помог Гордону собрать великое и могучее {i}кое что{/i}."
    th "Получил новое звание."
    th "Побыл агентом под прикрытием."
    th "Заложил целую группу воров."
    th "И день ещё не окончен..."
    scene bg ext_dining_hall_away_sunset with byso
    "Константин достал из кармана камень, который дал ему Гордон."
    th "Хотя как я с Лизой заговорю?"
if valscore > 0:
    th "Может вообще к чёрту?..."
    jump sidfvghnuguisdgousdfgfsd233515
else:
    th "Подойти к ней извиниться?..."
    jump sidfvghnuguisdgousdfgfsd233515
label sidfvghnuguisdgousdfgfsd233515:
    th "Не понимаю..."
    scene bg ext_dining_hall_near_sunset with byso
    "Убрав камень в карман, он достал из пачки одну сигарету и приближался ко входу в столовую."
    play ambience ambience_dining_hall_empty volume 1 fadein 1
    scene bg int_dining_hall_sunset with byso
    "В столовой как всегда было пустынно.{w=1} Оно и понятно - после шумихи на площади всем было интересно что произошло."
    show mi happy pioneer with byso
    "У раздачи как всегда стояла Мику и мазала губы помадой."
    show mi smile pioneer with byso
    "Она подняла глаза, и на ее лице появилась типичная для неё тупая улыбка."
    "Хоть Константину было и не до нее, но он тоже поднял уголок губ."
    show mi grin pioneer with byso
    "Её глаза насмешливо прищурились, а во рту появился кончик языка."
    mip "Здрасте-здрасте. Чего изволите, товарищ сержант?"
    kt "П-р-а-п-о-р."
    "Недовольно протянул Константин и положил на раздачу сигарету."
    show mi laugh pioneer with byso
    "Мику ещё шире улыбнулась и начала накладывать еду."
    show mi happy pioneer with byso
    mip "А чё на площади было?"
    kt "Разборки с наёмниками и их изгнание."
    show mi laugh pioneer with byso
    mip "О-о-о, ура-а!"
    "Она поставила на раздачу тарелку плова и стакан <<лимона>>."
    show mi smile pioneer with byso
    mip "Я так задолбалась слушать их хамство!"
    hide mi with byso
    "Константин едва слышно поблагодарил Мику и отправился за столик, где на обеде сидел с Гордоном, Ирой и Валери."
    "Столик запустевал, а он, хмыкнув, поставил тарелки на стол и начал поедать плов."
    th "А Ира же уехала...{w=1} Вроде за важными данными."
    th "Надеюсь, она вернётся...{w=1} Хм-м..."
    th "А могут ли наёмники мешать нашей операции?"
    "Константин остановился и посмотрел на вилку в его руках."
    th "Хотя тут скорее всего стоит задуматься о вопросе <<почему нет>>."
    th "Они знают куда мы поедем, они знают что мы будем делать, какое у нас вооружение...{w=1} И что выходит - они всё знают."
    th "Кстати, любопытно, у тех наёмников, которых я знал...{w=1} Ну у двоих..."
    th "Имена из русской литературы.{w} Неужели на деле они не быдло, а своего рода философы."
    th "Философы жоп и языков, насколько я понял..."
    th "Хотя это уже завтра...{w=1} Может даже у капитана спрошу."
    "Подумал Константин и отпил <<лимона>>."
    th "<<Лимон>>...{w=1} Напоминает юппи из детства...{w=1} Ужасная смесь."
    th "В отличие от своего собрата, этот хоть как-то утоляет жажду..."
    th "М-да, о чём я думаю?"
    "Покончив с едой, Константин взял тарелки и понёс их на мойку."
    show mi happy pioneer far with byso
    mip "Оцените наш плов от 1 до 10."
    kt "2 с плюсом.{w} Плюс потому, что давно его не ел."
    show mi angry pioneer far with byso
    mip "Э-э-э!{w=1} Да что ты вообще понимаешь в плове?!"
    play ambience ambience_camp_entrance_evening volume 1 fadein 1
    scene bg ext_dining_hall_away_sunset with byso
    play sound2 light_inh volume 1
    "Константин вышел из столовой и закурил."
    kt "Понимаю то, что в нём должны быть приправы. Это не рис с мясом..."
    "Пробурчал он и спустился с лестницы."
    stop music fadeout 3
    th "И что дальше?"
if valscore > 0:
    th "Валери просила к ней потом зайти...{w=1} Имеет смысл?"
    th "Вполне вероятно.{w=1} Да и собеседник из неё хороший."
    th "Или всё-таки пойти к Гордону помочь с его новой хай-тек приблудой?"
    window hide
    menu:
        "Пойти к Валери.":
            $ renpy.block_rollback()
            jump d5_end_with_val
        "Пойти к Гордону.":
            $ renpy.block_rollback()
            th "Ну, пойду ему помогу..."
            jump d5_end_with_liz
else:
    th "Ну, пойду к Гордону, помогу ему с его хай-тек приблудой."
    jump d5_end_with_liz
label d5_end_with_val:
    th "Пожалуй к Валери.{w=1} Гордону я буду только мешаться."
    th "Да и было бы неплохо её проведать..."
    scene bg ext_aidpost_day with fade
    play music regret fadein 3
    "Константин приближался к медпункту."
    "Остановившись у двери, он на секунду задумался."
    th "Она же уже в норме?"
    play sound2 sfx_knock_door7_polite volume 1
    "Он постучал в дверь."
    val "Заходи..."
    play sound2 door_cl volume 1
    play ambience ambience_int_cabin_evening volume 1 fadein 1
    scene bg val_sunset with byso
    "Валери сидела на стуле и, заметив Константина приятно улыбнулась."
    val "Ты всё-таки пришёл."
    "По ней было видно, что она уже давно ждала его визита и даже успела прийти в себя."
    kt "Да, как видишь.{w=1} Как ты?"
    play sound2 sfx_mystery_movement volume 1
    "Спросил Константин и сел на кушетку."
    val "Пришла в себя уже. {w}Прости за то, что тебе пришлось увидеть..."
    kt "Ладно...{w=1} Я тебя понимаю, столько сил впустую."
    val "Силы тут не при чём..."
    val "Это было дело принципа, но, как по мне, следует их изменить."
    kt "Ты про что?"
    "Валери наигранно пожала плечами и посмотрела в окно."
    val "О своём о девичьем..."
    "Она закинула ногу на ногу и посмотрела на Константина."
    val "Насколько я видела, наёмников изгнали?..."
    "Константин кивнул и закинул руки за голову."
    kt "Ага. {w=1}Они с капитаном пособачились, после чего решили пойти на уступки и свалить."
    val "Неужели..."
    kt "Надоели?"
    val "Да, возможно... {w=1}Звучит как повод выпить?"
    "Константин улыбнулся и кивнул."
    kt "Почему бы и нет. {w}Что у тебя?"
    val "Вино...{w=1} Наше, сопротивленческое."
    val "Не брезгуешь?"
    kt "Нет конечно.{w=1} Куда пойдём?"
    val "Ко мне в домик...{w=1} У меня там есть две бутылки."
    kt "Отлично, идём."
    play ambience ambience_camp_entrance_evening volume 1 fadein 1
    scene bg ext_houses_sunset
    show image val_calm
    with fade
    play sound2 sfx_keys_rattle volume 1
    "Валери достала из халата ключи и начала искать нужный."
    stop music fadeout 3
    liz "Костя?!"
    hide image val_calm
    show image val_calm at right
    show image liz_angry at left
    with byso
    "Константин поднял бровь и обернулся.{w=1} Валери замерла на месте и медленно повернулась на 90 градусов."
    play music paralysis fadein 3
    liz "Ты что, правда с этой начал общаться?!"
    kt "И что?"
    hide image liz_angry
    show image liz_rage at left
    with byso
    "Лиза на это возражение ещё сильнее разозлилась и указала на Валери.{w=1} Последняя просто смотрела на Лизу с вызывающим пофигизмом."
    liz "Блять, ты и в правду предпочёл меня и Олега обменять на эту больную нимфоманку?!"
    hide image liz_rage
    show image liz_angry at left
    with byso
    kt "Во-первых, причём тут Олег?"
    kt "Во-вторых, сама ты больная!"
    kt "Обратись к специалисту со своими проблемами с гневом!"
    val "Напоминаю, единственный специалист тут я..."
    "Безразлично протянула Валери и продолжила разглядывать связку ключей."
    kt "Наслаждайся своей болью и страданьем, раз ты не в состоянии нормально с людьми говорить!{w=1} Хули тебе ещё надо-то?"
    hide image liz_angry
    show image liz_rage at left
    with byso
    liz "А-а-а, я поняла.{w=1} Я, значит, не заслужила, да?!"
    liz "Эта тут тебе сиськами повиляла и сразу же обрела твоё внимание!"
    hide image val_calm
    show image val_normal at right
    with byso
    val "Я одна не помню такого?..."
    hide image liz_rage
    show image liz_angry at left
    with byso
    liz "Ага, не помнит она!"
    "Гнев Константина дошёл до точки кипения."
    kt "Лиза, ну что ты такая тупая-то?!{w=1} Ты сама виновата!"
    kt "Ладно ты тогда со мной посралась, но зачем ты меня теперь хуями кроешь?!"
    kt "Я тебе не парень с тиндера, чтоб меня так дёшево динамить!"
    kt "Я к тебе со всей душой, а ты?"
    hide image liz_angry
    show image liz_rage at left
    with byso
    liz "Отстань от меня со своей душой!"
    liz "Какой ты козёл!{w=1} И не знала, что ты ебучий нелюдь, как и эта синеволосая шлёндра!"
    play sound2 sfx_pat_shoulder_hard volume 1
    hide image liz_rage
    show image liz_angry
    hide image val_normal
    show image val_angry at right
    with byso
    "Валери разозлилась и за горло свитера подтянула Лизу к себе."
    val "Слушай ты, что-ж это ты так взбесилась-то, а?..."
    val "Мне плевать как ты называешь меня, но его так называть не смей!"
    val "Он был так добр ко мне, как никто другой в моей жизни!"
    val "Твоя душонка и убогая тушка даже не заслуживает ни секунды его внимания."
    val "Тебе стоило хотя бы раз извиниться, потому что он заслуживает этого!"
    hide image liz_angry
    show image liz_rage
    with byso
    liz "Завали свой..."
    play sound2 sfx_punch_medium volume 1
    hide image liz_rage
    show image liz_shysurp
    hide image val_angry
    show image val_dontlike at cright
    with byso
    "Валери схватила Лизу за горло и сильно сжала, отчего та даже захрипела.{w=1} На лице Валери вспыхнуло отвращение."
    val "Смотри... {w=1}У тебя есть три варианта...{w=1} Как в сказке."
    val "Первый{w=0.21}: ты извиняешься за всё сказанное и все мы расходимся, словно этого и не было."
    val "Второй{w=0.21}: ты смыкаешь верхнюю и нижнюю челюсть и идёшь своей дорогой."
    val "Третий{w=0.21}: я заставлю тебя заткнуться и завтра твой труп будут искать по всей симуляции."
    val "На размышление у тебя 15 секунд..."
    liz "Иди ты..."
    hide image val_dontlike
    show image val_mad at cright
    with byso
    "Прошипела Лиза, чем ещё сильнее разозлила Валери."
    "Она потянулась свободной рукой к пиле."
    stop music fadeout 3
    play sound2 sfx_pat_shoulder_hard volume 0.51
    hide image val_mad
    show image val_surprise at cright
    with byso
    "Константин остановил и схватил её за плечо."
    kt "Валери, не надо.{w=1} Отпусти её."
    val "Но..."
    kt "Отпусти."
    hide image val_surprise
    show image val_sad at right
    with byso
    "Валери послушала Константина и отступила от Лизы."
    "Последняя взялась за горло и начала жадно хватать воздух."
    kt "Я знал что такое произойдёт. {w=1}Ты так ничего и не поняла."
    kt "Теперь, поздравляю, я больше не хочу видеться с тобой."
    kt "Мне нахер не нужны твои дешёвые эмоциональные качели и умственно отсталые представления о жизни."
    kt "Просто иди своей дорогой.{w=1} Я не имею к тебе больше никаких претензий."
    kt "Было приятно увидеться.{w} Спасибо за эту незабываемую беседу."
    play sound2 sfx_keys_rattle volume 1
    "Валери наклонила голову и продолжила подбирать ключи к своей же двери."
    liz "Козлина!"
    hide image liz_shysurp
    hide image val_sad
    show image val_sad
    with byso
    play music interlude fadein 3
    "Слезливо поскулила Лиза и ушла прочь."
    kt "М-да..."
    val "Жаль?..."
    kt "Да не то что бы, просто обидно за своё время."
    play sound2 sfx_unlock_medpunkt_door volume 1
    "Валери открыла дверь и пропустила Константина."
    play ambience ambience_int_cabin_evening volume 1 fadein 1
    scene bg int_house_of_kt_sunset with byso
    "Константин вошёл внутрь и сел на стул.{w=1} На удивление, домик выглядел так, словно в нём никто не жил."
    kt "У тебя есть соседи?"
    play sound2 sfx_mystery_movement volume 1
    show image val_calm with byso
    "Валери закрыла дверь и села напротив."
    val "Нет. Была одна - потребовала переселение."
    kt "Почему?"
    hide image val_calm
    show image val_sad
    with byso
    "В ответ она размяла шею и тяжело вздохнула."
    val "Вопрос риторический как по мне..."
    kt "Понял..."
    "Валери достала из под кровати бутылку самопального вина и пару стаканов."
    "Протерев оба о свой халат, она поставила их на стол и открыла бутылку."
    hide image val_sad
    show image val_calm
    with byso
    val "Говорят дети жестоки. {w=1}Ошибочное суждение."
    val "Все люди по-своему жестоки..."
    "Разлив розовато-оранжевую жидкость по стаканам, она отставила бутылку в угол стола."
    kt "Бесспорно...{w=1} Ну что, за вечер?"
    hide image val_calm
    show image val_smile2
    with byso
    val "Давай..."
    "Они чокнулись и отпили опьяняющий нектар."
    "Константин понял, что похожее вино он пил с Лизой в 22-25а."
    hide image val_smile2
    show image val_smile
    with byso
    val "Ты беспокоишься из-за Лизы?..."
    kt "Нет, почему?"
    hide image val_smile
    show image val_calm
    with byso
    val "Ты выглядишь уставшим... {w=1}Словно весь день мешки грузил."
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_house_of_kt_night
    show image val_calm
    with byso
    "Выпив ещё немного вина, он посмотрел в окно.{w=1} На улице окончательно стемнело."
    kt "Просто я понимаю, что всё потраченное на неё время ушло в никуда."
    kt "В той симуляции, в сопротивлении...{w=1} Иллюзия смысла."
    kt "Всё это было лишь внешним мусором, причём вряд ли даже на сто процентов правдивым."
    hide image val_calm
    show image val_smile2
    with byso
    val "Не расстраивайся."
    "Константин почувствовал, как их ноги под столом соприкоснулись."
    val "Сам понимаешь, не всё в жизни так радужно, как хотелось бы..."
    kt "Тоже правда..."
    kt "Кстати...{w=1} всегда хотел спросить, а что у тебя с глазом?"
    hide image val_smile2
    show image val_calm
    with byso
    "Она положила ногу на ногу и повернулась к окну."
    val "Что-что, его нет...{w=1} Потеряла в инреальности."
    kt "Нет, я про другой.{w} Почему радужка стала красной?"
    hide image val_calm
    show image val_smile
    with byso
    val "Ах, ты про это...{w=1} Генмод скорее всего."
    val "Несколько раз мне приходилось лечиться от последствий заражения. Побочный эффект."
    hide image val_smile
    show image val_smile2
    with byso
    val "Тебе нравится?..."
    "Константин опустошил стакан и кивнул с улыбкой на лице."
    kt "Да. Выглядит необычно."
    hide image val_smile2
    show image val_sad
    with byso
    val "Рада что так..."
    "Смутилась Валери и тоже выпила вино до дна."
    hide image val_sad
    show image val_smile
    with byso
    val "Ещё по одной?..."
    kt "Давай."
    "Она разлила содержимое бутылки по стаканам.{w=1} Оставалось ещё буквально на два стакана."
    kt "За что выпьем?"
    hide image val_smile
    show image val_smile2
    with byso
    val "За нашу победу..."
    "Подняла стакан Валери и чокнулась с Константином."
    scene bg int_house_of_kt_night
    show image val_smile
    with fade
    "Градус в их крови постепенно повышался.{w=1} Пьяное удовлетворение уже вовсю обволакивало их."
    kt "Валери, а твои родители...{w=1} Какими они были?"
    "Она отставила стакан и подпёрла рукой подбородок."
    hide image val_smile
    show image val_calm
    with byso
    val "Лера...{w=1} Зови меня просто Лера."
    val1 "Родители... {w=1}Почему были?{w=1} Они есть."
    val1 "На тот момент, как меня выгнали из дома, работали в области медицины."
    hide image val_calm
    show image val_angry
    with byso
    "Валери перевела взгляд в окно, словно пытаясь что-то вспомнить."
    val1 "Отец психотерапевт в частной клинике.{w=1} Несмотря на свою профессию, уравновешенным его не назовешь."
    val1 "Часто он избивал меня, хотя я к этому времени была уже далеко не ребёнком."
    val1 "Мать была нейрохирургом.{w=1} Она тоже нередко кричала на меня и била."
    hide image val_angry
    show image val_calm
    with byso
    "Переведя взгляд обратно на Константина, она посмотрела ему в глаза."
    val1 "Кажется, этим в нашей семье было принято заниматься – но я уже тогда понимала, что их действия – лишь попытка утихомирить друг друга, чтобы обоим было легче."
    val1 "Подозреваю, они получали извращенное удовольствие, причиняя боль мне."
    val1 "Как и говорил Зигмунд Фрейд, все проблемы из детства... {w=1}В целом, благодаря им я и закончила тут."
    kt "Ты не думала, что они могли попасть в инреальность?"
    hide image val_calm
    show image val_sad
    with byso
    "Лера переключила взгляд на стол, где стояли стаканы."
    val1 "Вряд-ли.{w=1} Так они обращались только со мной."
    val1 "В своих кругах мама и папа были чуть ли не ангелами.{w=1} Помогали всем, но не мне."
    "Константин выпил немного и покачал головой."
    kt "Знакомая история.{w=1} Может даже чем-то схожая."
    kt "Я рос в условиях гиперопеки.{w=1} Мать хотела, чтобы я получил высшее образование и стал большой шишкой."
    kt "Только в позднем детстве я осознал, что эта любовь ко мне была исключительно наигранной."
    kt "Они хотели, чтоб я оказался наверху, после чего они смогут свободно распоряжаться моим имуществом и моим временем."
    kt "Однажды я понял, где правда.{w} После очередного скандала я переехал на квартиру своего покойного дедушки."
    kt "Он раньше работал на флоте и действительно меня многому научил."
    kt "А потом я встретил ее, свою любовь.{w=1} И она перечеркнула все, во что я верил.{w=1} Эту историю ты уже знаешь."
    "Опустошив стакан, он подпёр голову рукой и посмотрел на дно."
    kt "Мой единственный опыт с женщиной заключался в том, как вернуть ее назад."
    hide image val_sad
    show image val_calm
    with byso
    val1 "Мой опыт с мужчинами, в свою очередь, заключался в том, как найти того, кто действительно будет меня любить."
    val1 "Я искала и искала, чтобы понять, где именно надо искать, но не могла."
    val1 "Все хотели от меня лишь одного - чтобы я легла с ними в постель, переспала и съехала.{w=1} И тогда я стала понимать: им нужна не я сама, а мое тело..."
    hide image val_calm
    show image val_sad
    with byso
    "Уныло переведя взгляд в пол, она поводила пальцем по столу."
    val1 "Покончив с Ромой, я попала сюда и полноценно это осознала...{w} Они использовали меня так, словно я была простым фикусом, растущим на подоконнике, - на этом фикус и погорел в свое время..."
    val1 "Тут уже я ушла в, своего рода, монастырь."
    val1 "Никто из них не был нужен.{w=1} Только как материал для экспериментов."
    hide image val_sad
    show image val_calm
    with byso
    val1 "Поэтому на самом деле любящих мужчин у меня никогда и не было."
    "Константин разлил остатки вина и поднял стакан."
    kt "За светлое будущее."
    hide image val_calm
    show image val_smile
    with byso
    val1 "За будущее..."
    "Стукнувшись последними стаканами, они практически залпом их выпили."
    hide image val_smile
    show image val_smile2
    with byso
    val1 "Тоже быстро пьёшь?"
    kt "Мхм, да.{w=1} Не люблю лицемерие."
    hide image val_smile2
    show image val_smile
    with byso
    val1 "О чём ты?"
    "Константин отставил стакан в угол стола и положил на стол пачку сигарет."
    kt "Никогда не мог понять людей которые свой алкоголизм оправдывали вкусом алкоголя.{w=1} Лицемерие чистой воды."
    hide image val_smile
    show image val_smile2
    with byso
    val1 "Хе, это точно..."
    "Достав сигарету, он протянул её Лере."
    hide image val_smile2
    show image val_smile
    with byso
    val1 "Спасибо..."
    play sound2 light_inh volume 1
    "Чиркнув зажигалкой, Константин наполнил свои лёгкие табачным дымом. {w=1}Лера взяла у него зажигалку и тоже закурила."
    "Достав с подоконника хрустальную пепельницу, она затянулась и скинула туда новообразовавшийся пепел."
    hide image val_smile
    show image val_calm
    with byso
    val1 "Я даже и не помню, чтоб так сидела хоть с кем-то..."
    val1 "Впервые моя попойка не характеризуется компанией безразличных и отдалённых людей."
    kt "Или, как в моём случае, зияющим одиночеством."
    hide image val_calm
    show image val_smile2
    with byso
    "Константин почувствовал, как Лера словно обняла его ноги своими."
    val1 "Вот видишь, мы друг другу помогаем..."
    kt "Вероятно..."
    "Выдохнул Константин и достал из кармана камень, который дал ему Гордон."
    "При лунном освящении в домике, камешек казался огромной жемчужиной."
    "Чем дольше он глядел на него, тем сильнее камушек притягивал его внимание.{w=1} Казалось, из камня исходит сильное голубое сияние."
    hide image val_smile2
    show image val_calm
    with byso
    val1 "Чего ты?..."
    stop music fadeout 3
    "Собрав в себе силы, Константин отложил сигарету и протянул руку."
    kt "Дай свою ладонь."
    hide image val_calm
    show image val_surprise
    with byso
    val1 "Зачем?..."
    kt "Увидишь."
    "Лера сняла перчатку и положила ладонь на свободную руку Константина."
    play music KawuSun fadein 3
    hide image val_surprise
    show image val_scared
    with byso
    "Положив драгоценный камень ей на ладонь, он заметил, что её недоумение сменилось на крайнее смущение."
    kt "Это тебе."
    val1 "Что?..."
    "Константин отпустил руку Леры, а последняя принялась рассматривать подарок."
    val1 "С-сапфир?...{w=1} Мой любимый камень..."
    kt "Не знал. В любом случае он теперь твой."
    hide image val_scared
    show image val_surprise
    with byso
    val1 "Откуда ты его взял?..."
    kt "Помог Гордону соорудить одну машину.{w=1} Так он меня наградил, сказав, чтоб я его кому-то подарил."
    hide image val_surprise
    show image val_sad
    with byso
    "Лера прижала подарок к груди.{w} Даже через её маску было видно, что она счастлива."
    val1 "С-спасибо тебе огромное...{w=1} Никто в моей жизни мне такого не дарил..."
    kt "Не за что.{w=1} Ты это заслужила."
    kt "Столько лет над тобой издевались, но должно же быть в жизни то, что действительно стоит всего пройденного."
    kt "Не то что бы я идеальный человек, но тем не менее..."
    kt "Ты это заслужила."
    hide image val_sad
    show image val_smile
    with byso
    kt "Ты заслуживала лучшей жизни."
    kt "Чего-то нового и необычного. Я не знаю. Перемены."
    kt "А где перемены, там и перемены в душе. Возможно, вскоре они и настанут."
    kt "Так что не мучайся и не держи всё в себе..."
    hide image val_smile
    show image val_smile2
    with byso
    "Она встала со стула и отложила камень на стол."
    val1 "Встань на секунду..."
    hide image val_smile2
    show image val_smile2 at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Константин пожал плечами и встал.{w=1} Их глаза встретились."
    scene bg val_hug with byso
    "Лера приобняла его, сняла маску и тем самым показала свой шрам на губе."
    "Секунду они пристально глядели друг на друга."
    "По его телу прошла судорога."
    "Он как завороженный смотрел на ее губы."
    "Неожиданно она легко подняла руку и коснулась его щеки, проведя по ней пальцем."
    "Константин почувствовал, как напряглись мышцы его спины."
    "Ее голова при этом оставалась склоненной, так что он видел всю изящную линию ее шеи, еще никогда в жизни не казавшуюся ему такой манящей."
    "Его ноги словно налились латунью, и он не в силах был пошевелиться."
    "В следующий момент она подняла голову и поцеловала его в губы — нежно, но без тени смущения."
    "Когда ее мягкие губы коснулись его губ, он понял, что в его голове стало совершенно пусто."
    "Никаких мыслей.{w=1} Полная пустота, кроме той, в которой он должен был прожить оставшуюся часть жизни."
    "Она провела рукой по его торсу, и Константин почувствовал, как по телу прошла явившаяся из неоткуда волна желания."
    "А потом и она, казалось, ответила на его чувство, хоть этого он не мог увидеть."
    play sound2 sfx_bed_squeak2 volume 1
    "Повалив Константина на кровать, она нежно провела пальцами по лицу своего любовника."
    "Он не сопротивлялся – сердце его забилось быстрее, когда рука Валери нежно коснулась его губ."
    "Поцелуй стал еще нежнее.{w=1} Постепенно движения её руки сделались смелее."
    "И вскоре Константин ощутил, что она уже властвует над ним, подчиняет его себе."
    "Это было сладостное и опасное чувство."
    scene bg val_int with fade
    window hide dissolve
    $ set_mode_nvl()
    "Лицемерие."
    "Когда искренность пытаются заместить лицемерием, цель достигается.{w=1} Чистая правда."
    "Константин совершенно не ожидал такого окончания вечера."
    "До этого момента он совершенно не был уверен, испытывает ли он чувства к Валери."
    "Сейчас выяснилось что да."
    "Этот акт был не просто излиянием похоти."
    "Чувства, которые испытывал в этот момент радикально отличались от того, что он испытывал в тот раз."
    "Доверие."
    "Чувство, которое нельзя купить."
    "Да, это наверняка любовь. Метаморфоза, которая превращает человеческое <<я>> в безусловное сияние."
    "Такое же светлое, как чувства Леры к Константину."
    "Она поняла, что никогда раньше не любила по-настоящему, и теперь испытала это невероятное, ни с чем не сравнимое чувство."
    "Любовь."
    "Истинная любовь не имеет ничего общего с физическим влечением. Это нечто, похожее на энергетическое единение..."
    "Встреча с любящим человеком — это познание бога, откровение."
    "А за всей истинной любовью, всегда была только абсолютная доброта."
    "То, чего им не хватало в мире."
    "Теперь у них все есть."
    "За это стоит жить."
    window hide dissolve
    $ set_mode_adv()
    scene bg int_house_of_kt_night with byso
    play sound2 light_inh volume 1
    "Константин взял две сигареты и, выдав одну Валери, закурил."
    val1 "Тебе понравилось?..."
    kt "Солгу, если не скажу, что это было волшебно..."
    "Пыхнул Константин и дотронулся своей шеи.{w=1} Он обратил внимание, что на его руке было немного крови."
    "Ощупав это место, он понял, что это был укус, оставленный Лерой."
    val1 "Больно?..."
    play sound2 inh volume 1
    "Константин отрицательно помотал головой и затянулся."
    kt "Нет, я даже не заметил..."
    val1 "Прости, я немного переусердствовала..."
    kt "Ничего страшного.{w=1} Переживу."
    play sound2 sfx_blow_out_candle volume 1
    "Лера протянулась через Константина и взяла хрустальную пепельницу."
    val1 "Кстати, в инреальности ты у меня был первый..."
    kt "По такой логике ты у меня тоже."
    "Улыбнулся Константин и, сам того не заметив, поцеловал её."
    stop music fadeout 3
    play sound2 sfx_knock_door7_polite volume 1
    "В дверь постучали."
    "Константин вздрогнул, а Лера отвела взгляд на дверь и тяжело выдохнула."
    "На секунду ему показалось, что она хочет разорвать постучавшего в клочья."
    play sound2 sfx_knock_door2 volume 1
    play music Aleph fadein 3
    "Тогда стук повторился, теперь уже требовательный."
    andr "Валентайн!{w=1} У меня разговор."
    val1 "Срочно?..."
    "Недовольно протянула она, жестом попросив Константина подвинуться."
    play sound sfx_bed_squeak1 volume 1
    pause 0.25
    play sound2 sfx_blanket_off2 volume 1
    "Константин встал и принялся одеваться.{w=1} Валери накинула на себя халат."
    andr "Раз я пришёл лично - значит да."
    show image val_calm with byso
    "Лера натянула на себя маску, перчатки и прочее снаряжение, после чего выкинула в ведро использованное изделие №2."
    play sound2 sfx_open_door_2 volume 1
    hide image val_calm
    show image val_calm at right
    show image andr_normal2 at left
    with byso
    "Она открыла дверь и впустила капитана."
    hide image andr_normal2
    show image andr_normal at left
    with byso
    andr "А, ты тоже здесь.{w=1} Отлично."
    play sound2 sfx_mystery_movement volume 1
    pause 0.25
    play sound sfx_bed_squeak2 volume 1
    "Проговорил Андрей и сел на один из стульев. Валери и Константин сели на кровать."
    hide image andr_normal
    show image andr_normal3 at left
    with byso
    andr "Валентайн, я слышал, ты угрожала Лизе расправой?"
    hide image val_calm
    show image val_angry at right
    with byso
    "Осознав, о чём будет разговор, она тяжело выдохнула и кивнула."
    val1 "Было такое..."
    kt "За дело."
    hide image andr_normal3
    show image andr_normal at left
    with byso
    "Андрей безразлично пожал плечами и положил руки на стол."
    andr "Недавно я понял, что я отправил разведчиков на верную смерть."
    hide image andr_normal
    show image andr_normal2 at left
    hide image val_angry
    show image val_calm at right
    with byso
    andr "С ними были наёмники.{w} Скорее всего, узнав, что мы их изгнали, они просто убили <<Эриду>> и <<Ангела>>."
    kt "<<Ангел>>?"
    hide image andr_normal2
    show image andr_normal at left
    with byso
    andr "Главная по логистике."
    andr "К чему разговор. Мы отправляемся в бой утром, а не вечером, как планировали."
    hide image andr_normal
    show image andr_normal3 at left
    with byso
    andr "Вы отправляетесь в автобусе со мной, поскольку Лиза больше не может быть у меня в отряде."
    hide image val_calm
    show image val_angry at right
    with byso
    val1 "Почему?..."
    hide image andr_normal3
    show image andr_normal2 at left
    with byso
    "Капитан тяжело вздохнул и посмотрел в окно."
    andr "Я пересмотрел формацию моего отряда.{w=1} К тому-же, она не в себе."
    hide image val_angry
    show image val_calm at right
    with byso
    kt "И кто будет в нашем отряде?"
    hide image andr_normal2
    show image andr_normal3 at left
    with byso
    andr "Мы трое, Гордон, главный из отдела охраны и 4 боевых робота."
    "Константин пожал плечами."
    kt "Хорошо, тогда почему эта информация так важна сейчас?"
    hide image andr_normal3
    show image andr_normal at left
    with byso
    andr "У нашего отряда сбор на час раньше остальных. Завтра у меня дел невпроворот, потому пришлось вас искать."
    val1 "Где сбор?"
    hide image andr_normal
    show image andr_normal2 at left
    with byso
    "Андрей встал со стула и размял правое плечо."
    andr "У меня в кабинете.{w=1} За полчаса до завтрака. Не опаздывать."
    val1 "Хорошо...{w=1} Мы тебя поняли."
    hide image andr_normal2
    show image andr_normal at left
    with byso
    "Капитан посмотрел на Константина, а затем на Валери."
    andr "Отлично.{w=1} Тогда доброй ночи."
    kt "Доброй ночи."
    stop music fadeout 3
    play sound door_cl
    hide image andr_normal
    hide image val_calm
    show image val_sad
    with byso
    "Андрей покинул помещение, а Лера взяла со стола подаренный камень."
    val1 "Какой же он блестящий...{w=1} А внутри сердечко..."
    kt "Не то что бы я выбирал, но плохой бы дарить не стал."
    play sound2 sfx_blow_out_candle volume 1
    play music BlueJetta fadein 3
    hide image val_sad
    show image val_smile2
    with byso
    "Валери отложила камень и легла на кровать."
    val1 "Что бы ты не подарил, это было бы лучшим подарком в моей жизни..."
    play sound2 sfx_bed_squeak1 volume 1
    hide image val_smile2
    show image val_smile2 at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Константин лёг рядом и посмотрел на Леру."
    play sound2 sfx_blanket_off2 volume 0.11
    hide image val_smile2 with byso
    "Сняв с Валери медицинскую шапочку, он отложил её на стол."
    kt "Давай спать.{w=1} Завтра важный день."
    val1 "И я уверена, что он будет даже лучше чем сегодня..."
    val1 "А такая уверенность...{w=1} Дорого стоит."
    kt "Даже слишком."
    "Они снова слились в поцелуе и обняли друг друга."
    val1 "Спокойной ночи..."
    kt "Сладких снов."
    stop music fadeout 3
    stop ambience fadeout 1
    show blink
    "Константин уснул."
    pause 3
    play ambience ambience_forest_night volume 1 fadein 1
    scene bg ext_polyana_night
    show unblink
    "Константин снова стоял посреди леса."
    "Ночь уже вступила в свои права, а на небе догорали последние отсветы заката."
    scene bg zvezda with dissolve
    "Константин посмотрел вверх — и увидел странную яркую звезду."
    "Это была звезда иной природы — ослепительного света, испускаемого далекими галактиками. Она висела в темном небе слишком высоко."
    play music BloodyArt fadein 3
    "Незаметно для себя, он начал напевать любимую мелодию."
    kt "Я... {w=1}Разрежу...{w=1} Надвое себя..."
    "Из леса вышла Лера и начала напевать в такт Константину."
    val1 "Создам из плоти новый мир...{w=1} Где нет тебя..."
    kt "Пусть всё пылает...{w=1} Пламенем костра."
    val1 "Мне надоело..."
    kt "Любовь, вот и я."
    kt "Мне надоело..."
    val1 "Любовь, вот и я."
    kt "Создам из плоти новый мир..."
    val1 "Где нет тебя..."
    kt "Этот мир в котором мы вдвоём..."
    val1 "И ты живая снишься в нём..."
    val1 "Эта смерть, что увела тебя..."
    kt "Этот сон, где ты опять жива..."
    val1 "Этот мир в котором мы вдвоём..."
    kt "И ты живая снишься в нём..."
    val1 "Этот мир прекраснее тебя..."
    kt "Этот мир, где проклял я тебя..."
    stop ambience fadeout 1
    scene bg black with dissolve
    stop music fadeout 3
    pause 3
    val1 "Хэ-эй...{w=1} Доброе утро."
    play ambience ambience_int_cabin_day volume 1 fadein 1
    scene bg int_house_of_kt_day
    show image val_smile2
    show unblink
    play sound2 glad volume 1
    play music regret fadein 3
    "Валери была уже в сборе и нежно погладила Константина по плечу."
    kt "Доброе-доброе..."
    kt "Сколько времени?"
    hide image val_smile2
    show image val_smile
    with byso
    val1 "Мы немного проспали...{w=1} Сбор через 15 минут."
    "Константин встал с кровати и потянулся."
    kt "М-м, ну тогда пошли..."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_houses_day
    show image val_smile
    with byso
    play sound2 sfx_close_door_1 volume 1
    "Выйдя из домика, они взяли по сигарете и закурили."
    hide image val_smile
    show image val_smile2
    with byso
    val1 "От моего домика не далеко до капитана.{w=1} Идём..."
    kt "Идём-идём..."
    hide image val_smile2
    show image val_sad
    with byso
    "Константин почувствовал, что Лера взяла его за руку."
    "Он улыбнулся, будучи совсем не против."
    scene bg ext_admins_day
    show image rkis_normal
    show image rkis_normal2
    show image val_calm at left
    with byso
    "У административного корпуса стояли две робокошки."
    play sound2 sfx_open_door_clubs_2 volume 1
    rkis "Доброго утра.{w=1} Проходите.{w=1} Капитан вас ожидает."
    play ambience ambience_camp_center_day volume 0.31 fadein 1
    scene bg int_admins
    show image val_calm at right
    show image pas_normal at left
    with byso
    play sound2 sfx_close_door_1 volume 1
    "Войдя внутрь, они встретили Гордона."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "О, здорова, молодые."
    hide image val_normal
    show image val_smile at right
    with byso
    val1 "И тебе привет..."
    kt "Здарова.{w=1} Ну как, собрал свой новый аппарат?"
    "Гордон ощерился и кивнул."
    pas "Да-а, ты бы видел как шмаляет!{w=1} Просто гроза спектральных сущностей!"
    pas "Мы с Олегом её соорудили и испытали. {w=1}Просто конфетка из говна и палок!"
    kt "Отлично.{w=1} Ты к капитану?"
    pas "Ага.{w=1} Погнали вместе."
    stop music fadeout 3
    play sound2 sfx_knock_door2 volume 1
    "Дойдя первым до кабинета капитана, он постучал."
    andr "Заходите."
    play sound2 sfx_open_door_1 volume 1
    scene bg int_admins_room2
    show image Ohra_normal at fleft
    show image pas_normal at left
    show image andr_normal2
    show image val_calm at right
    with byso
    play music KillReligionInItself fadein 3
    "Капитан уже был при снаряжении.{w=1} Он повесил на пояс несколько магазинов от люгера и пару гранат."
    "На диване в развалку сидел охранник и ковырял в носу."
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Так, теперь все в сборе."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "В сборе.{w=1} Я заодно собрал новое орудие в одном экземпляре."
    hide image andr_normal
    show image andr_smile
    with byso
    andr "Работает?"
    play sound2 sfx_mystery_movement volume 1
    hide image val_calm
    show image val_angry at right
    with byso
    "Гордон ухмыльнулся и сел рядом с охранником.{w} Валери не хотелось садиться на один диван с охранником, потому подпёрлась о стену."
    "Константин сел рядом с Гордоном, который насмешливо кивнул и закинул руки за голову."
    pas "Ещё как!"
    hide image andr_smile
    hide image val_angry
    show image val_calm at right
    hide image andr_smile
    show image andr_normal
    with byso
    andr "Отлично.{w=1} Тогда мы обсудим план."
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "Значит так. {w=1}Через полтора часа мы едем в 20-32g и устраиваем ад на земле."
    andr "Мы попадаем в административную симуляцию и Гордон переводит права администратора на меня."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "В ином случае отправленные вчера агенты сделают это вместо нас и мы успешно устраним Генду."
    ohra "А нам то чего делать?"
    hide image andr_normal2
    show image andr_normal3
    with byso
    andr "Вы ответственны за мою безопасность.{w} В случае, если я умру, то весь код на флешке Гордона не сможет сработать."
    hide image pas_normal
    show image pas_angry at left
    with byso
    pas "Угу...{w=1} Если будет мёртв Генда или Андрей, то команда скорее всего просто не будет исполнена инреальностью."
    "Константин потёр подбородок и вопросительно посмотрел на Гордона."
    kt "Так почему нам тогда было просто не написать алгоритм лишения Генды прав?"
    hide image pas_angry
    show image pas_normal at left
    with byso
    pas "Как мог, так и написал, молодой.{w=1} Без какого-либо понимания кода это было сделать весьма трудно."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "К делу, сейчас идите на завтрак.{w=1} Я передам остальным подразделениям о сборах к выезду."
    andr "Константин и Валентайн свободны."
    play sound2 sfx_mystery_movement volume 1
    stop music fadeout 3
    "Константин встал с дивана и пошёл к выходу."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Наш автобус первый.{w=1} Не перепутайте."
    kt "Хорошо."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_admins_day
    show image val_smile
    with fade
    play music god fadein 3
    "Выйдя из административного корпуса, Константин заметил, что Валери искоса смотрит ему в глаза."
    kt "Чего ты?"
    hide image val_smile
    show image val_smile2
    with byso
    val1 "Есть одна идейка..."
    kt "Какая?"
    val1 "Пошли отойдём."
    scene bg ext_path2_day
    show image val_smile2
    with byso
    "Они отошли в лесок."
    kt "Что?"
    val1 "Слушай, а может нам того..."
    kt "Того?"
    val1 "Капитана подрезать?..."
    "Константина поразило предложение Леры.{w} Он вопросительно посмотрел на неё и почесал затылок."
    kt "Зачем нам это?"
    hide image val_smile2
    show image val_calm
    with byso
    val1 "Не тупи...{w=1} У нас есть ультимативная возможность получить контроль над инреальностью."
    hide image val_calm
    show image val_smile2
    with byso
    val1 "Так может нам его и заместить?..."
    "С явным намёком на кандидатуру Константина спросила Лера."
    kt "Так тогда флешка не сработает.{w=1} В чём смысл?"
    hide image val_smile2
    show image val_calm
    with byso
    val1 "После этого.{w=1} У нас будет хорошая возможность забрать себе права..."
    kt "Но зачем нам его предавать?"
    val1 "У меня нет никаких оснований, что он это не сделает по отношению к нам..."
    hide image val_calm
    show image val_calm at center:
        zoom 1.25
        yanchor 0.05
    with byso
    "Константин подошёл к Лере поближе."
    kt "Давай сначала посмотрим, как оно пойдёт, а там уже решим."
    hide image val_calm
    show image val_madsmile at center:
        zoom 1.25
        yanchor 0.05
    with byso
    val1 "М-м, хорошо..."
    show blink
    stop music fadeout 3
    "Валери приспустила маску и поцеловала Константина.{w=1} Затем положила руку ему на плечо и долго держала ее, глядя в его глаза."
    play ambience ambience_dining_hall_empty volume 1 fadein 1
    scene bg int_dining_hall_day
    show mi normal pioneer at left
    show image val_calm
    with fade
    play music BlueJetta fadein 3
    "В столовой ещё никого не было.{w=1} На раздаче стояла Мику и чистила люгер."
    show mi happy pioneer at left with byso
    mip "Здравствуйте - пидораствуйте!"
    kt "Чё?"
    show mi smile pioneer at left with byso
    mip "Ничё.{w} У нас сегодня самообслуживание, поскольку работать мне в падлу."
    mip "Всем продвинутая.{w=1} Капитан указал."
    mip "Вон два чана с едой, берите чё хотите, мне похуй."
    hide image val_calm
    show image val_angry
    with byso
    val1 "Что-то ты шибко разошлась..."
    "Мику нервно усмехнулась и вставила магазин в пистолет."
    show mi laugh pioneer at left with byso
    mip "Мне поебать, всё равно через два часа все сдохнем!"
    hide mi
    hide image val_angry
    show image val_calm
    with byso
    "Константин закатил глаза и пошёл накладывать себе еду."
    "В одном чане была манная каша, а в другой гречка с луком и яйцом."
    "Манка была практически нетронутой, а гречки хватало на 4-5 порций."
    hide image val_calm
    show image val_smile2
    with byso
    val1 "Я возьму гречку."
    "Валери положила себе половину порции гречки и провела рукой по запястью Константина."
    val1 "Там-же где и вчера."
    hide image val_smile2 with byso
    "Константин улыбнулся и кивнул, после чего начал накладывать гречку."
    th "Позитивный настрой у солдат - всегда хорошо."
    show image val_smile with byso
    "Подсев за столик Леры со стаканом <<лимона>>, Константин посмотрел на её тарелку."
    kt "Маловато ты ешь."
    hide image val_smile
    show image val_smile2
    with byso
    val1 "Достаточно.{w=1} Надо же поддерживать себя в форме...{w} Для тебя..."
    "Он улыбнулся и отмахнулся."
    kt "Как знаешь.{w=1} Приятного аппетита."
    hide image val_smile2
    show image val_smile
    with byso
    val1 "И ты не подавись..."
    "Пожелала Валери и коснулась своими ногами ног Константина. {w=1}Кажется, прикосновения для неё были отдельным видом удовольствия."
    hide image val_smile
    show image val_calm
    with byso
    th "Лера...{w=1} Никогда бы не подумал, что мы с ней так заладим..."
    th "Ранее она на вид была обычной медсестрой-психопаткой, но теперь она не психопатка — она ангел, просто под толстым барьером маски."
    th "Ей веришь.{w} Нам правда есть что сказать друг другу."
    th "Возможно, у нас с ней всё будет как в старом романтическом кино.{w} Та самая созависимость, которая отличается максимальной самоотдачей друг другу."
    th "Она поможет мне компенсировать то, чего я не в состоянии отпустить от себя сам, и всю мою наросшую депрессию."
    th "Тем самым я реабилитирую себя и её.{w=1} От этого будет только лучше."
    th "Может, это и не романтическое кино, а самое настоящее и светлое."
    th "Я могу довериться ей и остаться собой, несмотря на всё, через что мне пришлось пройти."
    "Константин закончил с едой и, отпив <<лимона>>, посмотрел на Валери, которая до сих пор ела и смотрела в окно."
    hide image val_calm
    show image val_smile
    with byso
    "Слегка погладив её по ноге, Константин привлёк её внимание.{w=1} Лера улыбнулась и посмотрела на него."
    val1 "А, ты уже всё...{w=1} Подожди, у меня ещё чуть-чуть..."
    "Валери быстро доела и отставила тарелку."
    hide image val_smile
    show image val_smile2
    with byso
    val1 "Теперь пошли...{w=1} Нам сейчас на площадь."
    "Оставив тарелки на местах, они отправились на точку сбора."
    play ambience ambience_camp_center_day volume 1 fadein 1
    play sound_loop ambience_medium_crowd_outdoors volume 1 fadein 1
    scene bg ext_square_day
    show image tolpa at right
    show image tolpa2 at left
    show image tolpa3
    show image val_calm
    with fade
    "На площади были толпы народа, а около Генды стояла кафедра, которую вытащили из библиотеки."
    pas "Молодые!{w=1} Сюда!"
    "Высмотрев в толпе махающего Гордона, они направились к нему."
    hide image val_calm
    show image val_smile2 at right
    show image pas_smile at left
    with byso
    kt "Так.{w=1} И чего теперь?"
    hide image pas_smile
    show image pas_normal at left
    with byso
    stop music fadeout 3
    pas "Щас Андрей выйдет, прочитает свою речь.{w} После этого мы едем в мясорубку."
    hide image val_smile2
    show image val_smile at right
    with byso
    val1 "Ждём тогда..."
    play music Kerosene fadein 3
    hide image val_smile
    hide image pas_normal
    with byso
    show image andr_normal2 with byso
    "К кафедре вышел Андрей."
    stop sound_loop fadeout 1
    hide image andr_normal2
    show image andr_normal
    with byso
    "Слегка прокашлявшись, он окинул взглядом всех сопротивленцев, заставив их замолчать и обратить на него внимание."
    hide image andr_normal
    show image andr_smile
    with byso
    andr "Итак, дорогие соратники! Этот день настал!"
    andr "Сопротивление отправляется на самую важную для него операцию!"
    hide image andr_smile
    show image andr_normal
    with byso
    andr "Мы все готовились к этому дню! И вот, спустя столько лет мы ударим!"
    andr "Наша сила – в единстве, а единство – это готовность умереть! Мы не можем проиграть!"
    andr "Но мы можем победить! А чтобы победить, мы не должны бояться смерти!"
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "В этой борьбе у нас не будет правил! Только силы!"
    andr "Выжить и победить в этом бою мы сможем только сообща!"
    andr "Сегодня вы выйдете на арену только с одной мыслью – выжить и найти выход! Давайте соединим свои силы в сегодняшнем танце смерти."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "Если это удастся, война закончится – а вместе с ней прекратится и наше заточение!"
    andr "Любое наше усилие в этой битве – не просто шаг к победе, это шаг на вечную память!"
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Сохраните эту память в сердцах своих соратников!"
    andr "Нас всех ждет триумф! Так победим же вместе!"
    hide image andr_normal
    show image andr_smile
    with byso
    andr "Отряды, по машинам!"
    hide image andr_smile with byso
    "Толпа зашумела и направилась к выходу из лагеря."
    show image val_smile at right
    show image pas_normal at left
    with byso
    "Отряд Андрея остался и ожидал капитана."
    show image andr_normal with byso
    "Люди рассосались.{w=1} Андрей вышел к своему отряду и махнул рукой."
    andr "Отправляемся."
    scene bg ext_bus with fade
    chel2 "Вперёд, вперёд!{w=1} Не задерживайтесь!"
    "Предпоследний автобус уехал и остался последний - с маркировкой <<#1>>."
    show image pas_normal with byso
    pas "Запрыгивайте!"
    scene bg int_avtobus
    show image val_calm at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    "Все вошли в автобус и сели по местам. Гордон вошёл последним и начал скрипеть коробкой передач."
    pas "Все в сборе?"
    andr "Все.{w=1} Стартуй."
    play sound2 korobka_peredach volume 1
    play sound2 sfx_ikarus_open_doors
    play ambience bus_inside volume 0.2 fadein 1
    "Гордон кивнул, а автобус закрыл двери и начал движение."
    pas "Мы будем в 20-32g через 30 минут. {w}Все симуляции на пути целы."
    andr "Отлично."
    "Отчеканил Андрей и перевёл взгляд в окно.{w=1} По нему было видно, что он нервничает."
    scene bg int_avtobus2
    show image val_calm at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    "Робокошки стояли в конце автобуса, судя по всему, в режиме ожидания."
    "Главный по охране, закинув ноги на переднее сиденье, выковыривал грязь из под ногтей."
    show image pas_normal at right with byso
    "Гордон сел на сидение перед Валери и Константином, после чего достал из под сидения рельсотрон Константина."
    hide image pas_normal
    show image pas_smile at right
    with byso
    pas "На, чуть не забыл у меня в мастерской."
    kt "О, точно, спасибо."
    "Гордон отдал Константину рельсотрон и начал водить по нему пальцем."
    hide image pas_smile
    show image pas_normal at right
    with byso
    pas "Смотри.{w} Это вкыл.{w} Там же выкл."
    play sound2 sms volume 0.1
    "Проигрался тихий звуковой сигнал."
    pas "Экран - параметры.{w=1} Не еби себе мозг."
    pas "Тут нажимаешь - предохранитель."
    pas "Диммер - мощность.{w=1} Лучше на середине мощности."
    pas "Это нажимаешь - догружаешь снаряды."
    play sound2 sfx_click_1 volume 1
    "По нажатию, открылся лючок в прикладе."
    pas "Пять шаров.{w=1} Больше - не влезет, меньше - не хватит."
    pas "В целом всё.{w} Там уже в бою разберёшься."
    kt "Да, спасибо."
    play sound2 ammo volume 0.51
    "Поблагодарил Константин и отставил пушку.{w=1} Гордон протянул ему коробочку с подписью <<25>>."
    pas "Тут 25 шаров.{w} Расходуй с умом."
    "Константин кивнул и забрал патроны, отставив к пушке."
    play sound2 glad volume 1
    hide image val_calm
    show image val_smile at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    "Валери положила голову на плечо Константина и, взяв его кисть, начала перебирать на ней пальцы, словно это детская игрушка."
    "Константин не сопротивлялся.{w=1} Ему это даже нравилось."
    hide image pas_normal
    show image pas_rpg at right
    show image pas_normal at right
    with byso
    "Гордон достал из под сидения трубу, похожую на противотанковое оружие."
    kt "Это и есть то, что ты собрал?"
    hide image pas_normal
    show image pas_rpg at right
    show image pas_smile at right
    with byso
    pas "Ага.{w=1} Считай РПГ."
    pas "Хуячит импульсными гранатами, которые наносят усопшим такой урон, что они коллапсируют и просто перестают существовать."
    hide image val_smile
    show image val_smile2 at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    val1 "Что бы ты не создал, ты назовёшь это каким-то названием из научной фантастики..."
    "Промурлыкала Лера, не отвлекаясь от игры с пальцами Константина."
    hide image pas_smile
    show image pas_rpg at right
    show image pas_normal at right
    with byso
    pas "Ну дк а чё?{w} Имею право."
    kt "На авторские права могут подать."
    hide image pas_normal
    show image pas_rpg at right
    show image pas_smile at right
    with byso
    "Гордон улыбнулся и отрицательно помотал головой, после чего повесил гранатомёт себе на спину."
    pas "Ну пусть попробуют!{w=1} Я им ебучку то мигом размажу!"
    hide image val_smile2
    show image val_smile at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    "Между тем, Лера сложила из пальцев Константина жест <<палец вверх>> и, подняв его руку, показала её Гордону."
    hide image pas_smile
    show image pas_rpg at right
    show image pas_normal at right
    with byso
    pas "А ты чего?{w=1} Он тебе новая игрушка чтоль?"
    hide image val_smile
    show image val_smile2 at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    val1 "Скорее шанс на хорошую жизнь..."
    "Улыбнулась Лера, сжав руку Константина."
    play sound2 sfx_mystery_movement volume 1
    show image andr_smile at fleft
    hide image val_smile2
    show image val_smile2 at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    "К ним подсел капитан."
    andr "Я так вижу, Константин уже полноценно влился в наши ряды?"
    hide image val_smile2
    show image val_smile at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    val1 "Ага..."
    hide image pas_normal
    show image pas_rpg at right
    show image pas_smile at right
    with byso
    pas "Так точн, капитан.{w=1} Рад буду забрать его себе на работу когда мы победим."
    andr "Это мы уже решим потом."
    kt "А как мы будем двигаться по локации?"
    hide image andr_smile
    show image andr_normal3 at fleft
    hide image val_smile
    show image val_smile at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    "Андрей сверкнул очками и посмотрел на Леру, которая никак не могла отстать от руки Константина.{w=1} Гордон закурил."
    andr "Мы остановимся у клубов.{w=1} Нам надо будет укрепить позицию, после чего дождаться обнуления стабильности или появления Генды."
    andr "Там мы вступаем в открытую конфронтацию.{w=1} Либо мы их, либо они нас."
    andr "У нас осталось 23 минуты до приезда."
    kt "То есть, всю работу за нас сделают остальные?"
    hide image andr_normal3
    show image andr_normal at fleft
    hide image val_smile
    show image val_smile at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    "Капитан утвердительно кивнул и перевёл взгляд на Константина."
    andr "В целом так.{w=1} Задача нашего отряда - перехват Генды."
    andr "Я лично покончу с ним, после чего нас ожидает сладкая победа."
    kt "Вы не уверены в наших шансах?"
    hide image andr_normal
    show image andr_normal2 at fleft
    hide image val_smile
    show image val_smile at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    "Константин своим вопросом поставил Андрея в тупик."
    andr "С чего ты взял?"
    hide image val_smile
    show image val_sad at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    val1 "Ты нервничаешь...{w=1} Трясёшься немного, голос скачет...{w=1} Это видно."
    "Произнесла она, соединив ладонь Константина со своей."
    hide image val_sad
    show image val_smile2 at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    val1 "Не страшно.{w} Все мы понимаем, что нас ожидает всё или ничего."
    val1 "Нашу жизнь мы потеряли ещё до инреальности. Зачем нам теперь бояться?"
    val1 "Это лишь прогулка.{w=1} Если мы и проиграем, то мы должны благодарить инреальность хоть за то, что мы пожили ещё чуть-чуть."
    kt "Да, я согласен с Лерой.{w} Мы, по сути своей, ничего не теряем, так что..."
    hide image pas_smile
    show image pas_rpg at right
    show image pas_normal at right
    with byso
    pas "М-м-да, верно...{w=1} Тем не менее, нам надо ебать как постараться, чтоб наконец зажить по-настоящему..."
    hide image andr_normal2
    show image andr_smile at fleft
    hide image val_smile2
    show image val_smile2 at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    andr "Может вы и правы...{w=1} Да, вы правы."
    andr "Тогда, мы сделаем всё, что в наших силах."
    play sound2 sfx_mystery_movement volume 1
    hide image andr_smile with byso
    "Андрей улыбнулся и вернулся на своё место.{w} Гордон достал из под сидения ремень, в котором было вложено множество ракет."
    hide image pas_normal
    show image pas_rpg at right
    show image pas_smile at right
    with byso
    pas "Патроны для гранатомёта чуть не забыл.{w=1} Вот башка соломенная."
    "Гордон взял в руки снаряд и затолкал его в ствол."
    stop music fadeout 3
    show blink
    "Константин опёрся головой о стекло и задремал."
    pause 3
    val1 "Костя-я, вставай..."
    scene bg int_avtobus2
    show image val_sad at cleft:
        zoom 1.1
        yanchor 0.01
    show unblink
    play music KillReligionInItself fadein 3
    play sound2 glad volume 1
    "Он проснулся и посмотрел на Леру, которая гладила его пальцами по ладони."
    hide image val_sad
    show image val_smile2 at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    val1 "Я и не заметила как ты задремал..."
    kt "Да я и сам не обратил внимания...{w=1} Мы скоро?"
    hide image val_smile2
    show image val_calm at cleft:
        zoom 1.1
        yanchor 0.01
    with byso
    val1 "Гордон сказал, что следующая наша."
    kt "Отлично."
    play sound2 sfx_mystery_movement volume 1
    hide image val_calm with byso
    "Они встали с мест.{w} Константин взял рельсотрон и патроны для него."
    "Остальные уже стояли у водительского места и что-то обсуждали."
    show image Ohra_normal at fleft
    show image val_calm at left
    show image andr_normal2
    show image pas_rpg at right
    show image pas_normal at right
    with byso
    ohra "Будет сделано!"
    hide image Ohra_normal with byso
    andr "Хорошо.{w=1} Гордон, запускай робокошек."
    pas "Момент."
    hide image pas_rpg
    hide image pas_normal
    with byso
    "Гордон пошёл к робокошкам и встал перед ними."
    pas "Так, единицы серии K, выходим из гибернации."
    "Константин и Валери встали у выхода.{w=1} Робокошки заскрипели и включились."
    rkis "Единицы серии K готовы. {w=1}Введите команду."
    pas "Охранять капитана."
    show image pas_rpg at right
    show image pas_normal at right
    with byso
    rkis "Команда принята!"
    play music Sireirom fadein 3
    play sound2 sfx_muffled_explosion volume 1
    hide image val_calm
    hide image andr_normal2
    hide image pas_normal
    show image pas_angry at right
    show image val_surprise at left
    show image andr_fear2
    with vpunch
    "Вдали раздался громкий взрыв."
    pas "Что за херня?!"
    andr "Какого чёрта там происходит?!"
    play sound2 bum volume 0.71
    "Раздался ещё один взрыв.{w=1} Только этот был куда мощнее предыдущего." with vpunch
    val1 "Если это не салют, то это плохо..."
    pas "Да какой нахуй салют?!{w=1} Наших походу бьют!"
    "Автобус начал снижать скорость."
    "Все приготовились к бою и максимально сосредоточились."
    "За окном показались языки пламени."
    hide image andr_fear2
    show image andr_rage
    with byso
    andr "Вот чёрт!{w=1} Наших подорвали!"
    pas "Нас ждали... {w=1}Ебучие <<безбожники>>!"
    play sound2 sfx_bus_stop volume 1
    play sound2 sfx_ikarus_open_doors volume 1
    play ambience fireing volume 1 fadein 1
    "Автобус остановился.{w=1} С улицы доносилась стрельба."
    scene bg int_fire with byso
    "Двери открылись и все выбежали из автобуса."
    "Автобусы с маркировкой <<#3>> и <<#5>> были в огне, а внутри были видны убитые взрывом люди, и их залитые кровью части тел были везде."
    "Это совершенно не доставило капитанскому отряду никакой радости."
    show image andr_rage with byso
    andr "Мы потеряли около 75ти человек в двух автобусах!"
    show image Ohra_normal at left with byso
    ohra "Перемещаемся в клубы!"
    scene bg ext_clubs_night
    show image poter_n
    with byso
    "Весь отряд добежал до клубов.{w=1} У дверей стоял потерянный пионер."
    hide image poter_n
    show image poter_s
    with byso
    pp "А вот и вы, уёбки!"
    show image rkis_normal at center:
        xanchor 2 yanchor -0.01
        linear 0.2 xanchor -0.01
    play sound2 sfx_armature_swish volume 1
    "Робокошка набросилась на пионера, но не смогла его убить.{w=1} Её рука прошла насквозь."
    hide image rkis_normal with vpunch
    play sound2 magic volume 1
    "Выстрелом плазмы пионер распылил робокошку.{w=1} Гордон выхватил своё орудие."
    kt "Ты что вытворяешь?!"
    pp "Костя, тварь, ты меня оставил!{w=1} Пришло время объяснить свой поступок."
    show image pas_rpg at fleft
    show image pas_angry at fleft
    with bso
    pas "Лови аптечку, хуила спектральная!!!"
    play sound2 rpg volume 1
    pause 0.5
    play sound2 bum volume 0.76
    scene bg ext_clubs_night
    show image pas_rpg at fleft
    show image pas_angry at fleft
    with fl_fire
    show image val_surprise at right
    show image andr_nervous2
    with byso
    "Гордон попал чётко в пионера, разорвав его на части. Остановить процесс распада пионера было уже невозможно."
    "Части его тела разлетелись в радиусе 5 метров и, секунду пролежав, обрели материальное воплощение, рассыпавшись в прах."
    pas "Съел блять?!"
    val1 "Ты его знал?..."
    kt "Да, он был в моей симуляции.{w=1} Потом расскажу."
    pas "Выбить дверь!"
    show image rkis_normal at left with byso
    rkis "Есть."
    play sound2 door_break volume 1
    "Робокошка пробила дверь насквозь и открыла." with vpunch
    scene bg int_clubs_male_night
    show image pas_rpg at left
    show image pas_angry at left
    show image andr_nervous2
    show image val_angry at right
    with byso
    "Отряд вбежал внутрь и занял тактическое положение."
    "Константин встал у шкафа и, вооружившись рельсотроном, смотрел вокруг."
    show image Ohra_normal at fleft with byso
    ohra "Луна в дельте!"
    play sound2 sfx_open_door_kick volume 1
    scene bg int_clubs_male_night
    show image sopr_soldb2 at cleft
    show image pas_rpg at left
    show image pas_angry at left
    show image andr_fear2
    show image val_dontlike at right
    show image sopr_soldb at cright
    with vpunch
    "После этой команды, из шкафов вышли два наёмника."
    play sound2 sfx_pat_shoulder_hard volume 1
    scene bg int_clubs_male_night
    show image sopr_soldb at cright:
        zoom 1.5
        yanchor 0.05
    with vpunch
    "Один из них взял гарроту и начал ей душить Константина, а другой сбил с ног Гордона."
    pas "Робокошки, в атаку блять!"
    scene bg int_clubs_male_night
    show image val_mad
    show image sopr_soldb at right
    with vpunch
    "К Константину прыгнула Валери и, выхватив пилу, обрезала орудие удушения."
    val1 "Не смей трогать его!"
    play sound2 knife2 volume 1.4
    hide image sopr_soldb with fl_scare
    "Вторым взмахом пилы, Лера перерезала нападающему горло."
    play sound2 sfx_body_bump volume 1
    "Солдат упал на пол, пытаясь остановить сильное кровотечение."
    play sound2 ammo volume 1
    scene bg int_clubs_male_night
    show image val_scared
    show image Ohra_normal at left
    with byso
    "Охранник взял пистолет и прицелился в Валери."
    kt "Хуй с два!"
    play sound2 plazma_gun volume 1
    scene bg int_clubs_male_night
    show image val_surprise
    with vpunch
    "Метким выстрелом из рельсотрона Константин снёс охраннику голову."
    play sound2 sfx_punch_washstand volume 1
    scene bg int_clubs_male_night
    show image andr_fear2 at left
    show image sopr_soldb at cright
    with bso
    "Последний <<безбожник>> пытался зарезать капитана, но Андрею удалось его оттолкнуть."
    show image rkis_normal at center:
        xanchor -2 yanchor -0.01
        linear 0.2 xanchor -0.01
    pause 0.1
    play sound2 head_crush volume 1
    hide image sopr_soldb with bso
    "На наёмника набросилась робокошка и пробила его грудь."
    sold "Хуй вам..."
    play sound2 sfx_click_2 volume 1
    "Прошипел <<безбожник>> и выдернул кольца из своих гранат."
    andr "Быстро из помещения!"
    play sound2 bum volume 1
    scene bg ext_clubs_night
    show image pas_rpg at fleft
    show image pas_angry at fleft
    show image andr_fear2
    show image val_scared at left
    with fl_fire
    "В клубах раздался взрыв.{w=1} Все уцелели, но ещё две робокошки были уничтожены."
    show image idol_palladin at fright with byso
    "Со стороны площади выбежал мужик с пулемётом и надписью <<Паладин>> на руке."
    window hide
    window hide
    $ renpy.block_rollback()
    $ time = 25000
    $ timer_range = 25000
    $ timer_jump = 'dcvfjsauiovhfsui9ahvuifasdhvuisvu'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Убить.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            play sound2 plazma_gun volume 1
            hide image idol_palladin with vpunch
            "Метким выстрелом из рельсотрона, Константин продырявил мужчину."
            jump fvjnsuiodfvu9ifsdhnvifsuiv
        "Не убивать.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            idol "Да покарает вас всевышний!"
            play sound_loop pulemet volume 1
            show weapon_fireing with vpunch
            "Он начал палить из пулемёта."
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            play sound2 head_crush volume 1
            scene bg black with vpunch
            "Одна из пуль попала Константину в голову."
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
label dcvfjsauiovhfsui9ahvuifasdhvuisvu:
    stop sound3 fadeout 1
    $ renpy.block_rollback()
    idol "Да покарает вас всевышний!"
    play sound_loop pulemet volume 1
    show weapon_fireing with vpunch
    "Он начал палить из пулемёта."
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    play sound2 head_crush volume 1
    scene bg black with vpunch
    "Одна из пуль попала Константину в голову."
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
label fvjnsuiodfvu9ifsdhnvifsuiv:
    "Мужик без сил упал и растёкся по земле."
    hide image andr_fear2
    show image andr_rage
    with byso
    andr "Наёмники уже сотый раз нас предают!"
    kt "Куда двигаться дальше?"
    pas "Держим эту позицию!"
    play sound2 zoomer volume 3
    scene bg ext_clubs_night
    show image rkis_idol
    with fl_scare
    "Из кустов выскочила ржавая робокошка."
    rkis_r "Мясо-о..."
    play sound plazma_gun
    show image rkis_normal at cright with byso
    "Выстрел от Константина пришёлся мимо цели. Ржавая напала на обычную робокошку."
    "Робокошка отряда попыталась ударить по ржавой, но безуспешно."
    play sound3 pistol volume 1
    pause 0.01
    play sound ricochet
    pause 0.3
    play sound2 pistol volume 1
    pause 0.01
    play sound3 ricochet
    pause 0.3
    play sound pistol volume 1
    pause 0.01
    play sound2 head_crush volume 1
    "Андрей несколько раз выстрелил по ужасному созданию, чем попал во внутренности."
    rkis_r "Бо-оль!!!"
    play sound3 metal volume 1
    hide image rkis_normal with vpunch
    show image andr_fear2 at right with byso
    "Ржавая заревела и пробила голову другой робокошке и бросилась на Андрея."
    "Гордон выхватил гранатомёт."
    play sound2 plazma_gun volume 1
    hide image rkis_idol with fl_scare
    "Константин его опередил.{w=1} Выстрелом рельсотрона, он пробил грудь робокошки."
    rkis_r "Бо-оль..."
    play sound2 sfx_bush_body_fall volume 1
    "После этого пронзающего стона ржавая рухнула на землю."
    hide image andr_fear2
    show image andr_nervous2 at right
    with byso
    andr "Наёмники объединились с идолопоклонниками?!"
    show image val_surprise at left
    hide image andr_nervous2
    show image andr_nervous2 at right
    with byso
    val1 "Такое создание могли соорудить только они..."
    show image pas_rpg
    show image pas_angry
    hide image val_surprise
    show image val_surprise at left
    hide image andr_nervous2
    show image andr_nervous2 at right
    with byso
    pas "Ебаный по голове! {w=1}На кой хуй пичкать моих робокошек мясом?!{w} Больные ублюдки!"
    play sound2 reload volume 1
    "Константин зарядил в рельсотрон недостающие заряды, после чего осмотрел отряд."
    kt "Может нам свалить отсюда?!{w=1} Все нас убить хотят!"
    hide image andr_nervous2
    show image andr_angry at right
    with byso
    andr "Придётся. Отряд, на площадь!"
    scene bg ext_square_night_blood with byso
    "На площади шли ожесточённые бои."
    idol "Сгорите, еретики!"
    chel "Отряд, огонь!"
    play sound plazma_gun
    scene bg bloody_mess with vpunch
    "Отряд Андрея включился в боевые действия."
    window hide dissolve
    $ set_mode_nvl()
    "Замечание Мику в столовой было весьма к месту."
    "Каждую секунду на этом поле боя кого-то до убивали."
    "Константин не успевал докладывать заряды в рельсотрон, потому перешёл на стрельбу из пистолета."
    "Гордон запускал ракеты в большие скопления противника."
    "Андрей тоже старался быть полезным и отстреливал приближающихся идолопоклонников."
    "Валери орудовала орудиями ближнего боя, пытаясь сохранить жизнь своему отряду."
    "Трупы солдат и идолопоклонников падали на землю целыми горами."
    "Летели брызги крови и куски тел, разбросанные взрывом. Карнавал смерти всё ещё продолжался."
    "Отряды сопротивления сильно проседали, в целом как и отряды их врагов."
    "Воздух на площади уже наполнился запахом жжёного пороха и крови."
    "Ко всему этому продолжали появляться создания из плоти и металла, созданные идолопоклонниками."
    "Они появлялись совершенно хаотично, как чёрт из табакерки, и сквозь крики о спасении доносились их скрипучие голоса."
    "Но был один отряд, который держал ситуацию под контролем - отряд Андрея. Сопротивлению удалось получить преимущество."
    "Идолопоклонников стало меньше, а остатки штурмовых отрядов продолжали присоединяться к битве."
    "Это было как в компьютерной игре. Только баталия была с реальной кровью, оторванными конечностями и звуками."
    "Особенно большую роль играла кровь и вой умирающих, которые, словно испускались истерзанными сердцами и раздавленными мышцами."
    window hide dissolve
    $ set_mode_adv()
    scene bg ext_square_night_blood
    show image pas_rpg
    show image pas_angry
    with byso
    pas "Идолопоклонники отступают!"
    show image andr_angry at right with byso
    andr "Не дайте им уйти!"
    "Все остававшиеся сопротивленцы начали стрелять в спины убегающих с поля боя."
    "Вот их осталось 15."
    "Через несколько секунд уже 8."
    "И, наконец, меньше пяти."
    play ambience ambience_camp_center_night volume 1 fadein 1
    "Сопротивлению удалось победить. Все их враги пали."
    hide image andr_angry
    show image andr_nervous at right
    show image val_surprise at left
    with byso
    val1 "Мы...{w=1} Победили?"
    andr "Ещё нет, нам надо..."
    gg "Так-так-так..."
    scene bg ext_square_night_blood_red with byso
    scene bg genda with byso
    "Небо окрасилось красным, а со стороны входа в лагерь объявился Генда."
    gg "А вас стало ещё меньше...{w=1} Всего-то 40 человек."
    gg "Тоже мне...{w=1} <<Сопротивление>>..."
    gg "О, а среди вас есть знакомые лица..."
    gg "Калинин Андрей Романович.{w=1}.. Я думал тебя убило вместе с тем Мишей..."
    gg "Несветаева Валерия Викторовна.{w=1}.. Ты снова пережила своего бывшего..."
    gg "Беспалов Виктор Антонович.{w=1}.. Так и не предал своё инженерное дело..."
    gg "И Брусков Константин Павлович.{w=1}.. Не думал, что ты так сильно меня возненавидишь..."
    andr "Хватит пиздеть!{w=1} Отряд, огонь на поражение!"
    play sound_loop fireing volume 1
    show genda_fire
    "Вce оставшиеся на площади открыли огонь по создателю.{w=1} Все заряды пролетали сквозь него, не оставляя никаких повреждений."
    stop sound_loop fadeout 1
    hide genda_fire
    scene bg genda
    with byso
    "Осознав, что это не эффективно, они прекратили огонь."
    gg "Очень мило..."
    play sound2 sfx_energy_door_bus volume 1
    stop music
    scene bg ext_square_night_blood_red with vpunch
    "Раздался странный звук и Генда упал на землю."
    show image andr_smile with byso
    play music deadrazy4 fadein 3
    andr "Да!!!"
    show pistol12 with fade
    "Андрей достал свой пистолет и прицелился в Генду."
    gg "Что за..."
    gg "Вы..."
    andr "Мы - мы, всё мы!"
    andr "Любопытно...{w=1} Помнишь, как ты меня однажды застрелил?"
    andr "Помнишь...{w=1} Я же знаю..."
    andr "Что-ж, старый, настало твоё время освободить трон для более подходящего кандидата."
    gg "Нет!{w=1} Не смей!{w=1} У меня!...{w=0.41}{nw}"
    "Капитан наклонился и вставил ствол пистолета создателю в глотку."
    andr "Ещё как посмею.{w=1} Прощай."
    play sound2 pistol volume 1
    scene bg ext_square_night_blood_red with fl_scare
    "Андрей спустил курок."
    show image andr_normal with byso
    "Встав в полный рост, он окинул взглядом всех присутствующих."
    hide image andr_normal
    show image andr_smile
    with byso
    andr "Это победа!"
    show image pas_rpg at fleft
    show image pas_smile at fleft
    with byso
    pas "Ура!!!"
    scene bg ext_square_night_blood_red
    show image tolpa
    with byso
    "Поднялась суета.{w=1} Все начали прыгать друг другу в объятия и аплодировать капитану."
    chel "Слава новому предводителю инреальности!"
if valscore == 2:
    jump Metamorphosis_ending
else:
    jump Counterrevolution_ending
label Counterrevolution_ending:
    show image val_smile2 with byso
    "Валери подошла к Константину."
    val1 "Вот и всё...{w=1} Мы победили."
    "Константин улыбнулся и перевёл взгляд на Леру."
    hide image val_smile2
    show image val_smile2 at center:
        zoom 1.25
        yanchor 0.05
    with byso
    kt "Точно...{w=1} Теперь мы все свободны."
    show blink
    "Их губы слились в поцелуе."
    "Чувство победы наполнило их, им захотелось взлететь."
    "Голова кружилась, и сложно было сохранять равновесие."
    "Все смешалось: земное и небесное, ветвистые узоры мироздания и бесконечные соцветия жизни."
    "Она засмеялась, наслаждаясь приятным головокружением."
    "Ничего прекраснее в своей жизни она не испытывала.{w=1} Смеялась, как маленькая девочка."
    pas "Так, потом полизаетесь.{w=1} Пойдёмте к капитану."
    scene bg ext_square_night_blood_red
    show image tolpa
    show unblink
    "Они отлипли друг от друга и подошли к Андрею."
    show image andr_nervous
    show image pas_rpg at fleft
    show image pas_normal at fleft
    show image val_calm at fright
    with byso
    "На вид он был весьма встревоженным."
    pas "Ты уже получил права администратора?"
    andr "Не могу сказать...{w=1} Я до сих пор ничего не ощущаю..."
    kt "В каком смысле?"
    hide image andr_nervous
    show image andr_normal
    with byso
    andr "Вообще ничего не происходит.{w=1} Я не могу ничего сделать."
    hide image val_calm
    show image val_sad at fright
    with byso
    val1 "Странно..."
    pas "Да не то слово, молодая..."
    hide image andr_normal
    show image andr_normal2
    with byso
    andr "Ладно, сейчас разберёмся."
    play sound2 sfx_radio_squelch_2 volume 1
    hide image andr_normal2
    show image andr_nervous2
    hide image val_sad
    show image val_surprise at fright
    with byso
    "Радость толпы и диалог главных перебил треск системы оповещения."
    sold_sm "Рано вы обрадовалась, пидорасы!"
    "Внимание всех сопротивленцев было приковано на ближайшем динамике."
    hide image andr_nervous2
    show image andr_rage
    with byso
    andr "Что это значит, <<Смердяков>>?!"
    sold_sm "Это значит что пришло время контрреволюции, уроды!"
    hide image pas_normal
    show image pas_angry at fleft
    show image val_surprise
    show image val_scared at fright
    with byso
    "Все находящиеся на площади снова взялись за оружие."
    stop music fadeout 3
    sold_sm "О нет, оружие вам не пригодится."
    sold_sm "Вы расплатитесь по счетам!"
    play sound pum
    sold_sm "<<Колесников>>, надменная супернова!"
    $ _dismiss_pause = False
    play music "<from 33.5>inrealnost/Music/Music/WSWW2.mp3" fadein 6
    scene bg black with dissolve
    pause 1
    play sound bomb_sfx volume 1.5
    scene bg bomb_body:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 10 crop (0, 0, 1920, 1080)
    show bomb32:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 10 crop (0, 0, 1920, 1080)
    with byso
    pause 4.4
    play sound2 sfx_nightmare_explosion volume 1
    scene bg explosion with vpunch
    play ambience amb_fire volume 1 fadein 1
    $ _dismiss_pause = True
    "Взрыв."
    "Вся площадь взлетела на воздух."
    "Тела сопротивленцев разлетелись по сторонам."
    "Взрыв был настолько мощный, что даже памятник задрожал."
    "Капитана, как и большую часть людей разорвало на части ударной волной."
    scene bg int_fire
    show unblink
    "Константин уцелел, но не мог пошевелиться. Ударной волной ему оторвало конечности."
    "Он может было хотел закричать, но не смог. Боль сковала его тело."
    val1 "Костя...{w=1} Ты жив?..."
    "Валери лежала перед ним.{w=1} Из её спины торчала деталь, которая ранее принадлежала робокошке."
    kt "Лера!"
    "Прокричав, Константин выплюнул кровь."
    play sound2 sfx_mystery_movement volume 3
    "Памятник Генды покосился и со скрипом начал падать."
    kt "Берегись!"
    play sound2 door_fall3 volume 1
    pause 1
    play sound head_crush volume 1
    "Медный памятник расплющил Леру." with vpunch
    "С хрустом распластал её по земле и разнес её голову.{w=1} Из под черепа брызнула кровь."
    kt "Нет!... Кх..."
    "Вдалеке нарисовалась фигура наёмника, который добивал выживших."
    mip "Нет!{w=1} Не надо!"
    sold "Асталависта."
    play sound2 pistol volume 1
    "Выстрел." with vpunch
    sold_sm "А вот и тот урод, что нас сдал..."
    show image sopr_soldb with byso
    "Из-за спины Константина вышел <<Смердяков>> с гранатой в руке."
    kt "Уёбок!... Кх..."
    sold_sm "Кто бы говорил..."
    sold_sm "Могли бы и без этого обойтись.{w=1} Знаешь, с твоим стажем ты бы мог вступить в наши ряды."
    sold_sm "Но ты выбрал неправильный путь."
    sold_sm "Что-ж, не долго песенка играла, не долго фраер танцевал."
    play sound2 sfx_click_3 volume 1
    hide image sopr_soldb with byso
    "Наёмник выдернул чеку из гранаты и, засунув её Константину за шиворот, отошёл."
    sold_sm "Сладких снов, фраерок."
    play sound bum
    stop ambience
    stop music fadeout 3
    scene bg black with fl_fire
    window hide dissolve
    pause 1
    stop sound fadeout 3
    pause 3
    play music "<from 38>inrealnost/Music/Music/Radar.mp3" fadein 3
    $ renpy.pause(3, hard=True)
    $ unlock_ach_root_inreal(17)
    scene bg ending_ProjectMayhem_cg:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    show ending_counterrevolution:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    with Dissolve(26)
    scene bg black with byso
    stop music fadeout 3
    pause 2.6
    jump after_ending_screen
label Metamorphosis_ending:
    th "Это...{w=1} Победа?..."
    show image val_smile2 at center:
        zoom 1
        linear 0.21 zoom 1.5 yanchor 0.1
    play sound2 sfx_bush_body_fall volume 1
    "Вдруг, Валери прыгнула Константину в объятия, чем сбила с ног и повалила в кусты." with vpunch
    val1 "Мы побе...{w=1}{nw}"
    scene bg bomb_body
    show bomb12
    with byso
    "Она остановилась и заметила в кустах странную красную лампочку."
    kt "Что за..."
    "Они встали с земли и, разворошив кусты, заметили странное устройство, которое было похоже на бомбу."
    val1 "Нам надо уходить.{w=1} Сейчас же!"
    scene bg ext_houses_night
    show image val_surprise
    with byso
    "Константин и Лера побежали прочь с площади в сторону домиков."
    pas "Эй, молодые, куда вы?"
    stop music fadeout 3
    hide image val_surprise
    show image val_surprise at right
    show image pas_rpg at left
    show image pas_normal at left
    with byso
    "Их догнал Гордон и остановил, встав перед ними."
    pas "Вы там чё, банши увидели?{w=1} Щас мы будем выбираться отсюда!"
    kt "Хрена с два, площадь..."
    play sound2 sfx_radio_squelch_2 volume 1
    hide image val_surprise
    show image val_scared at right
    hide image pas_normal
    show image pas_rpg at left
    show image pas_angry at left
    with byso
    play music deadrazy3 fadein 3
    "Их диалог перебил треск системы оповещения."
    sold_sm "Рано вы обрадовалась, пидорасы!"
    pas "Что за?..."
    sold_sm "Это значит что пришло время контрреволюции, уроды!"
    "Все трое снова взялись за оружие."
    sold_sm "О нет, оружие вам не пригодится."
    sold_sm "Вы расплатитесь по счетам!"
    sold_sm "<<Колесников>>, надменная супернова!"
    val1 "В укрытие!"
    play sound2 sfx_nightmare_explosion volume 1
    scene bg ext_houses_night with vpunch
    "С площади донёсся оглушающий взрыв."
    "Он был настолько мощным, что даже земля вздрогнула."
    show image val_dontlike at right
    show image pas_rpg at left
    show image pas_angry at left
    with byso
    pas "Ебучие <<безбожники>>!"
    kt "Орудие к бою!"
    scene bg int_fire with byso
    play ambience amb_fire volume 1 fadein 1
    play sound door_fall3 volume 1
    "Статуя Генды рухнула на землю, и через секунду на ней появилась еще одна трещина, расходящаяся по всей её медной груди."
    "Гордон вставил в гранатомёт новый снаряд, а Константин взял в руки рельсотрон."
    "На площади трупов стало ещё больше.{w} Среди них ходили трое наёмников."
    show image sopr_soldb with byso
    mip "Нет!{w=1} Не надо!"
    sold "Асталависта."
    play sound2 plazma_gun volume 1
    hide image sopr_soldb with vpunch
    "Константин поразил наёмника раньше, чем он смог добить лежащую девушку."
    "Все наёмники мигом попрятались за деревья."
    play sound sfx_radio_squelch_2
    sold_sm "Сопротивление выжило!{w=1} <<Колесников>>, на площадь!{w} <<Собакевич>>, <<Побединский>>, держать оборону!"
    show image pas_rpg at left
    show image pas_angry at left
    with byso
    pas "Залупу за щеку!"
    play sound2 rpg volume 1
    pause 0.5
    play sound2 bum
    "Гордон выстрелил в дерево, чем разорвал наёмника вместе с деревом." with vpunch
    play sound2 pistol volume 1
    pause 0.1
    play sound head_crush
    hide image pas_rpg with vpunch
    "Наёмники начали давать отпор.{w=1} Пуля попала Гордону в плечо, чем выбила из рук гранатомёт."
    pas "Блять, уёбище лесное!"
    show image val_dontlike at right with byso
    val1 "Я перевяжу.{w=1} Костя, застрели последнего!"
    scene bg int_fire
    show image sopr_soldb
    with byso
    pause 1
    play sound plazma_gun
    scene bg int_fire with vpunch
    "Константин выглянул из-за подножия памятника и совершил точный выстрел в тело наёмника."
    show image val_scared at right
    show image pas_rpg at left
    show image pas_angry at left
    with byso
    "К ним прилетела граната."
    kt "Перехват!"
    scene bg int_fire with byso
    "Он схватил гранату с земли и бросил её обратно отправителю."
    play sound2 bum volume 1
    "Взрыв." with fl_fire
    show image sopr_soldb at cright
    show image sopr_soldb2 at cleft
    with byso
    "Константин выглянул из укрытия и заметил последних двух наёмников."
    val1 "Стрелять можешь?"
    pas "Смогу...{w=1} С одной руки."
    play sound2 pistol volume 1
    pause 0.3
    play sound pistol volume 1
    pause 0.01
    play sound2 ricochet
    pause 0.3
    play sound3 pistol volume 1
    "Гордон схватил пистолет и, выглянув из укрытия выстрелил несколько раз."
    "Один из выстрелов попал в каску наёмника и отрикошетил."
    sold "Они за памятником!"
    play sound2 plazma_gun volume 1
    hide image sopr_soldb with vpunch
    hide image sopr_soldb2
    show image sopr_soldb
    with byso
    "Константин выглянул из укрытия и выстрелил в одного наёмника, чем оторвал ему руку."
    sold_sm "<<Колесников>>!"
    sold_sm "Вы пожалеете об этом, фраера!"
    play sound2 sfx_click_3 volume 1
    "С этими словами он взял все свои гранаты и выдернул из них кольца, после чего с криком побежал на них."
    show image pas_rpg at left
    show image pas_angry at left
    with byso
    pas "Сам ты фраер!"
    play sound2 pistol volume 1
    pause 0.1
    play sound bum volume 1
    stop music fadeout 3
    hide image sopr_soldb with fl_fire
    "Гордон попал наёмнику в грудь, чем вызвал детонацию одной из гранат."
    show image val_dontlike at right with byso
    val1 "Камикадзе недоделанный..."
    play sound2 power volume 1
    "Последние выжившие вышли из укрытия.{w=1} Открылись порталы."
    pas "Да неужели!"
    kt "Значит, Гордон, иди назначь администратора, а мы с Валери попытаемся найти уцелевших."
    hide image pas_angry
    show image pas_normal at left
    with byso
    pas "Понял, давайте."
    play sound2 portal volume 1
    hide image pas_rpg
    hide image pas_normal
    with dissolve
    hide image val_dontlike
    show image val_smile2
    with byso
    "Гордон растворился в портале."
    val1 "Вот теперь мы точно победили..."
    scene bg black with dissolve
    stop ambience fadeout 3
    pause 3
    play music Gallow fadein 3
    scene bg kefetery
    show image pas_angry
    with byso
    "Константин сидел за столом с Витей и пил чай."
    pasv "Я тебе говорю, надо их под трибунал..."
    kt "Не, не так.{w=1} Смотри."
    kt "Лере нужен человек на опыты, а в отделе ИПП нужен испытатель."
    kt "Там мы и найдём применение нашим двум воровкам со склада."
    play sound2 light_inh volume 1
    hide image pas_angry
    show image pas_smile
    with byso
    "Гордон закурил и улыбнулся."
    pasv "Да, возможно ты прав, молодой.{w=1} Нам там как раз рук не хватает."
    kt "Ну вот так и поступим.{w=1} Выпустим из карцера и отправим на исследование."
    "Константин закинул руки за голову и посмотрел в потолок."
    hide image pas_smile
    show image pas_normal2
    with byso
    pasv "Валери скоро закончит с сывороткой?"
    kt "С какой именно?"
    hide image pas_normal2
    show image pas_smile
    with byso
    pasv "Она говорила, помню, синаптический ускоритель.{w=1} Мне рабочий класс жалуется, что им отдыха мало. В 12 часов!"
    kt "Так на него и нужен подопытный человек.{w=1} На остальных млекопитающих уже протестировали - работает."
    hide image pas_smile
    show image pas_normal2
    with byso
    pasv "Ну тогда точно отправим Наташу на опыты.{w} Если сыворотка хорошо работает, то по ней сразу видно станет."
    "Константин ухмыльнулся и, сделав глоток чая подпёр шею рукой."
    kt "Хорошо, я понял.{w=1} Мы вроде как раз про ИПП вопрос не обкашляли."
    hide image pas_normal2
    show image pas_angry
    with byso
    "Гордон нахмурился и закатил глаза."
    pasv "Ну ты называй всё своими именами, а?{w=1} Сложно сказать исследование пустых подпространств?"
    kt "Может быть."
    window hide dissolve
    $ set_mode_nvl()
    "Инреальность."
    "Площадка для проведения самых разных опытов, где можно исследовать буквально всё."
    "Условия и материалы всегда найдутся."
    "Константин, Гордон и Лера решили поделить права администратора на троих из соображений повышения эффективности исследований. Это экономит время."
    "Сейчас можно провести те же самые опыты, но за меньшее время, так что их результат будет в сто раз точнее."
    "Константин никогда не обладал такой тягой к исследованиям как сейчас. Он полностью погрузился в новый мир и безостановочно, до самого рассвета, занимался проработкой планов и систем и всегда торопился поделиться мыслями со своими коллегами. С Виктором и Лерой."
    "Они тоже увлекались новым миром, и работали в том же духе. Прошло не так много времени, но их коллектив уже сумел обогнать земное развитие практически во всех областях."
    "Достигнуты уникальные результаты и всё ещё есть куда расти. Сотрудники не думают об ограничениях из-за которых раньше приходилось отказываться от новых научных идей."
    "Общая популяция людей была набрана из тех, кто уже был в инреальности и тех, кто выжил из сопротивления."
    "Их общий штат составлял около 3 тысяч человек. Плюс к тому - около пятиста осужденных, которые использовались либо в качестве расходного материала или рабочих на опасной работе."
    "Все проблемы безопасности сведены к нулю."
    window hide dissolve
    $ set_mode_adv()
    hide image pas_angry
    show image pas_normal2
    with byso
    pasv "Ладно, друже, я пойду попинаю этот твой ИПП..."
    stop music fadeout 3
    kt "Давай.{w=1} У меня завтра выходной кстати."
    hide image pas_normal2
    show image pas_smile
    with byso
    pasv "Ты говорил, удачи с Валери отдохнуть."
    th "Переместить в подпространство 02-01kv.{w=1} Execute02."
    play sound2 teleport volume 1
    scene bg val_sunset2 with fl_fast
    play music M83_1 fadein 3
    play ambience ambience_int_cabin_evening volume 1 fadein 1
    "В мгновение ока Константин оказался в комнате.{w=1} Валери сидела на кровати и читала отчёты по работе её отдела."
    kt "Привет, любимая."
    val1 "Привет, Костик..."
    kt "Как дела в отделе?"
    play sound2 sfx_paper_bag volume 1
    "Лера тяжело вздохнула и отложила журнал."
    val1 "Работают.{w=1} Я заберу одного заключённого на эксперимент?"
    kt "Да. {w=1}Витя попросил отправить Наташу из сопротивления."
    "Она широко улыбнулась и насмешливо наклонила голову."
    val1 "Хорошо, заберу.{w=1} Посмотрим, сможет ли её сознание выдержать такой напор..."
    play sound2 sfx_bed_squeak2 volume 0.31
    "Константин сел рядом с Лерой и взял её руку."
    val1 "А ты чего?..."
    kt "Заскучал немного по тебе.{w} В последние два дня было столько всего, что я даже и не спал."
    val1 "Я тоже...{w=1} У нас завтра выходной?"
    kt "Верно.{w} Можем провести день вместе."
    val1 "Я рада..."
    play sound2 glad volume 1
    "Валери прогладила рукой щетинистое лицо Константина. Он же погладил ее волосы."
    "Посмотрев друг на друга, они улыбнулись."
    "Она нежно сжала его руку."
    window hide dissolve
    $ set_mode_nvl()
    "Они были совершенно счастливы.{w} Им было хорошо вдвоем."
    "Мало того, их счастье быстро переросло в любовь.{w=1} А любовь - это метаморфоза счастья, подобное превращению светляка в звезду."
    "Чем больше звезд ты видишь, тем шире открывается твой взгляд и тем больше ты понимаешь и чувствуешь. И тем яснее видишь образ в своем сердце."
    "Вот так и с Валерией и Константином...{w=1} Они еще только начинали понимать это."
    "Счастье шло к ним издалека - словно незримый проводник, посланный матерью-природой, - но оно уже подходило все ближе и ближе."
    "Звезда по имени <<счастье>> была совсем рядом."
    "Надо только протянуть к ней руку, и она загорится от огня..."
    window hide dissolve
    $ set_mode_adv()
    stop music fadeout 3
    stop ambience fadeout 3
    scene bg black with dissolve
    pause 3
    $ unlock_ach_root_inreal(18)
    play music "<from 177>inrealnost/Music/Music/KawuSun.mp3" volume 1 fadein 3
    scene bg ending_Metamorphosis_cg:
        crop (0, 0, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    show ending_Metamorphosis:
        crop (0, 0, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    with Dissolve(25)
    scene bg black with byso
    stop music fadeout 3
    pause 2.6
    jump after_ending_screen
label d5_end_with_liz:
    th "А ещё надо подумать, как помириться с Лизой всё-таки..."
    scene bg ext_clubs_day with byso
    play music ParentIssues fadein 3
    play sound_loop bolgarka volume 1 
    "Из мастерской доносились звуки болгарки."
    "Иногда гудение становилось звонким и громким и исчезало совсем, иногда оно становилось резче и громче."
    play sound2 sfx_open_door_clubs_2 volume 1
    play ambience ambience_int_cabin_evening volume 1 fadein 1
    scene bg int_clubs_male_sunset
    show image pas_angry at fleft
    show image oleg_shy at right
    with byso
    "Константин не долго думая вошёл внутрь."
    "Олег стоял у тазика с серо-синим порошком и тщательно перемешивал его, а Гордон полировал латунную трубу."
    stop sound_loop fadeout 1
    hide image pas_angry
    show image pas_normal at fleft
    with byso
    "Выключив болгарку, Гордон заметил вошедшего Константина."
    pas "О, вернулся.{w=1} Как раз для тебя дело есть."
    kt "Какое?"
    play sound2 sfx_blow_out_candle volume 1
    "Отложив инструмент, он махнул рукой Константину."
    hide image pas_normal
    show image pas_normal
    with byso
    pas "Шуруй сюда, щас покажу."
    "Константин подошёл к Олегу.{w=1} Рядом стоял ряд разобранных металлических ракет, похожих на снаряды РПГ."
    kt "Откуда ты их взял?"
    pas "А, ты про корпус? {w=1}Давно ещё собрал из говна и палок."
    hide image pas_normal
    show image pas_angry
    with byso
    "Он скорчился и посмотрел в окно."
    pas "До того, как у меня <<безбожники>> спиздили чертёж."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "А это взрывчатое вещество.{w=1} Руками трогать нельзя."
    hide image pas_angry
    show image pas_normal
    with byso
    pas "Да.{w} Это стандартный порох вперемешку со свинцовой стружкой и секретным ингредиентом."
    kt "И к чему такой стрёмный набор веществ?"
    hide image pas_normal
    show image pas_smile
    with byso
    "Гордон взял в руки один из снарядов и повертел в руках."
    pas "А это, молодой, для того, чтоб спектральные сущности рвать в клочки."
    kt "В смысле?{w=1} Спектральные сущности боятся свинцовой стружки?"
    pas "Не-е, нет.{w} Идолопоклонники придумали что-то вроде сплава, который может навредить спектральным сущностям."
    pas "Вот мы его быстренько нашпиговали сюда.{w} Поверь, ебучку разорвёт кому угодно!"
    kt "Ладно...{w=1} Так что мне делать?"
    play sound2 sfx_open_table volume 1
    hide image pas_smile
    show image pas_normal
    with byso
    "Отставив пустой снаряд, Гордон открыл ящик стола."
    pas "Ты, дорогой мой друг, будешь наполнять их взрывчаткой."
    "Из ящика он достал перчатки, совок и воронку."
    pas "По три воронки на каждый."
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Я же не домешал..."
    "Гордон посмотрел в таз и поднял бровь."
    pas "Всё ты домешал, молодой.{w=1} Можешь теперь и сам заняться подготовкой снарядов."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Хорошо.{w} А есть чем?"
    hide image pas_normal
    show image pas_angry at left
    with byso
    pas "Глянь в ящике стола.{w} Там найдёшь, если те пидораски не продали..."
    "Пробурчал Гордон и вернулся к своему столу, где начал ковыряться в запчастях орудия."
    hide image oleg_think
    show image oleg_shy at right
    with byso
    "Олег нашёл в ящике все инструменты, и надев снаряжение, взял первый снаряд."
    kt "А сколько их тут всего должно быть?"
    hide image pas_angry
    show image pas_normal at left
    with byso
    pas "Таза хватит на 10.{w} У меня есть 14 болванок."
    kt "Хорошо."
    "Константин и Олег начали заполнять ракеты взрывчатым веществом."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Ты помирился с Лизой?"
    "В ответ Константин тяжело вздохнул и отрицательно помотал головой."
    kt "Нет.{w=1} Не встретились.{w} Да и я не знаю что сказать ей..."
    hide image oleg_think
    show image oleg_smile at right
    with byso
    oleg "По нашему прошлому диалогу я узнал, что она тоже захотела помириться и пошла тебя искать."
    oleg "Я понимаю, что она тебе такого наговорила, но...{w=1} дай ей шанс."
    "Константин заполнил первый снаряд и взял второй.{w} Готовый снаряд выглядел весьма элегантно."
    kt "Да куда я денусь... {w=1}Сам уже думал о перемирии."
    kt "Ну посрались и посрались. {w}Мириться то тоже надо, за одну сторону же воюем."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Да-а, это верно, молодой.{w} Лиза хоть девчонка специфичная, но кто не без этого?"
    oleg "Перегибает палку иногда, но зачастую это не страшно..."
    "Олег ссыпал взрывчатый порошок в снаряд, после чего посмотрел на Гордона."
    hide image oleg_smile
    show image oleg_happy at right
    with byso
    oleg "А мы постреляем?"
    hide image pas_smile
    show image pas_angry at left
    with byso
    "Гордон вздохнул, после чего присоединил к орудию самопальный прицел."
    pas "Ну чё ты как дитё малое?{w=1} Будем-будем."
    kt "А не опасно?"
    hide image pas_angry
    show image pas_normal at left
    with byso
    pas "Не, молодой.{w} Тот не боевой."
    kt "Хорошо если так..."
    pas "А что стало с экспериментом Валери?"
    "Константин недовольно цокнул и поставил готовый снаряд."
    kt "Пришёл один из Семёнов и отчекрыжил Роме башку пилой."
    hide image oleg_happy
    show image oleg_shy at right
    with byso
    oleg "Что?{w=1} Зачем?"
    kt "Наёмники судя по всему попросили."
    pas "М-да, в их стиле."
    oleg "В каком?"
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "В стиле дохлой крысы."
    kt "Почему дохлой?"
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_clubs_male_night
    show image oleg_shy at right
    show image pas_smile at left
    with byso
    "Ухмыльнулся Константин и зачерпнул совок взрывчатки."
    hide image pas_smile
    show image pas_normal at left
    with byso
    pas "Потому что у них есть такой протокол.{w} Если тебя убивают или пытаются убить, то в случае полного пиздеца ты как японский лётчик делаешь камикадзе."
    pas "Весьма эффективная техника между тем."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "И что, им совсем себя не жаль?"
    "Он выдохнул и взял в руки готовый аппарат."
    pas "Нет.{w=1} Некоторые из них ранее были зэками со строгача, а некоторые ещё и ПТСРные."
    pas "Им по факту плевать на то, что будет с ними и с их окружающими.{w} На то они и <<безбожники>>."
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Сколько их видел, но никогда бы не подумал что они такие..."
    kt "А что ты думал?{w=1} Они аниматоры?"
    hide image pas_normal
    show image pas_smile at left
    with byso
    "Гордон широко ухмыльнулся."
    pas "Фурриёбы."
    oleg "Да нет, просто не понятно, почему они были с сопротивлением.{w} У нас же совершенно другие идеи."
    hide image pas_smile
    show image pas_normal at left
    with byso
    pas "А тут уже я тебе скажу: эффективность."
    pas "Они ранее были отдельной малочисленной группировкой, но потом Андрей предложил им объединиться."
    kt "Да, и при этом долбоёбами оказались именно мы."
    pas "Точно.{w=1} Так и произошло."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Это последний."
    "Олег взялся за наполнение последнего снаряда, а Константин снял перчатки и облокотился на стол."
    kt "Гордон, ты закончил?"
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Ну да, тут только спуск надо настроить..."
    hide image pas_smile
    hide image oleg_think
    with byso
    show image rpg_im with byso
    "Константин подошёл к нему и посмотрел на орудие."
    "Наиболее подходящим определением для аппарата была <<труба со спусковым ключком>>."
    "Константину было решительно неясно, откуда Гордон взял для этой трубы детали от автомата калашникова, но они там были."
    "На одном из её концов был ремень, который, судя по всему, был предназначан для более удобной переноски орудия."
    "Была предусмотрена система выпуска взрывных газов на конце, которая чем-то напоминала фильтр от противогаза."
    "Бонусом на прицеле стояла лазерная указка, которая могла служить менее точным прицелом."
    pas "Долго ещё будешь залипать?"
    hide image rpg_im with byso
    show image pas_normal at cleft
    show image oleg_shy at fright
    with byso
    "Константин обернулся и посмотрел на Гордона, который явно ожидал, пока он налюбуется."
    kt "Да нет.{w=1} Пожалуйста."
    hide image pas_normal
    hide image oleg_shy
    show image pas_smile at left
    show image oleg_shy at right
    with byso
    "Константин уступил ему место у стола и отошёл к Олегу."
    pas "Вы пока повесьте все снаряды на ремень. Надо же мне будет чем-то завтра стрелять."
    hide image oleg_shy
    show image oleg_happy at right
    with byso
    oleg "А мы запускать пойдём?"
    hide image pas_smile
    show image pas_angry at left
    with byso
    "Гордон тяжело выдохнул и покачал головой."
    pas "Нет блять, пойдём дрочить по кругу!{w} Чё как Ульянка?"
    hide image oleg_happy
    show image oleg_shy at right
    with byso
    oleg "Ладно-ладно."
    hide image pas_angry
    show image pas_normal at left
    with byso
    "Олег взял ремень и начал складывать в него готовые снаряды."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Щас мы спуск то отрегулируем..."
    kt "А откуда у тебя запчасти такие?"
    hide image pas_smile
    show image pas_normal at left
    with byso
    pas "Ну нашли ребята в отрядах снабжения. И не такое находили."
    pas "Вон, смотри."
    "Он не глядя указал на монитор и компьютер, которые выключенными стояли в углу."
    pas "Один чувак вообще, судя по всему, решил собрать себе компьютер.{w} Но упс, незадача. {w=1}Попал в инреальность."
    kt "Н-да, обидно наверное."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Да не то слово.{w=1} Зато у нас есть хорошая вычислительная машина."
    pas "Что только путники сюда не привозили.{w=1} В одном отряде там чувак ноутбук нашёл!"
    kt "У вас еще и ноут есть?"
    play sound2 ammo volume 0.41
    hide image pas_smile
    show image pas_rpg at left
    show image pas_normal at left
    with byso
    "Гордон отрицательно помотал головой и, повесив на себя орудие, обернулся."
    pas "Не, чувак пропал без вести.{w=1} Вместе с техникой."
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "Всё, Олег, возрадуйся, мы идём тестировать."
    hide image oleg_shy
    show image oleg_smile at right
    with byso
    oleg "Да неужели!"
    pas "Возьми один заряд с собой."
    play sound sfx_clench2
    hide image pas_smile
    show image pas_angry at left
    with byso
    "Олег кивнул и вынул из ремня один снаряд.{w} Гордон ударил себя по лбу."
    pas "Ну дура-ак...{w=1} НЕ боевой!"
    hide image oleg_smile
    show image oleg_shy at right
    with byso
    oleg "А, точно..."
    play sound2 sfx_open_table volume 1
    "Вернув снаряд на место, он открыл ящик и достал оттуда точно такой-же."
    kt "А как вы их различаете?"
    hide image pas_angry
    show image pas_smile at left
    with byso
    pas "Как-как.{w=1} Эти в ремне, а тот в ящике. {w}Так и различаем."
    kt "Сильно."
    stop music fadeout 2
    play sound2 sfx_close_door_1 volume 1
    play ambience ambience_camp_center_night volume 1 fadein 1
    scene bg ext_clubs_night
    show image oleg_happy at right
    show image pas_rpg at left
    show image pas_normal at left
    show image liz_bukal
    with byso
    "На выходе их встретила Лиза."
    play music regret fadein 3
    oleg "О, Лиза, пошли с нами новое оружие тестировать!"
    hide image liz_bukal
    show image liz_surp
    with byso
    "Она явно не ожидала такого вопроса."
    liz "Что?...{w=1} На ком?"
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "На воздухе.{w} Пошли, тебе понравится."
    liz "Ну л-ладно?"
    pas "Эу, открой ворота."
    show image Ohra_normal at fleft with byso
    "Своим пожеланием Гордон разбудил охранника, который мирно спал на стуле у ворот."
    "Он зевнул и встал со стула."
    ohra "Чё?{w=1} Вам зачем?"
    pas "Надо, молодой, надо."
    kt "Испытать орудие."
    ohra "Ладно...{w=1} Вы надолго?"
    play sound2 sfx_keys_rattle volume 1
    "Доставая ключи спросил охранник.{w=1} Гордон поправил гранатомёт и махнул рукой."
    pas "Минут 5-10."
    ohra "Хорошо, проходите."
    scene bg ext_road_night2
    show image oleg_smile at right
    show image pas_rpg at left
    show image pas_normal at left
    show image liz_normal
    with fade
    "Дойдя до ЛЭП, Гордон кивнул."
    pas "Всё, так нормально.{w=1} Теперь погнали."
    hide image liz_normal
    show image liz_dontlike
    with byso
    liz "Это безопасно?"
    hide image pas_normal
    show image pas_angry at left
    with byso
    pas "Нет блять, порвёт нас всех нахуй."
    hide image oleg_smile
    show image oleg_happy at right
    with byso
    oleg "Давай запускай уже!"
    hide image pas_angry
    show image pas_smile at left
    with byso
    pas "Ща."
    play sound2 sfx_click_2 volume 1
    "Гордон направил ствол вверх и нажал на курок."
    play sound2 rpg volume 1
    scene bg firework with fl_fire
    play sound sfx_firework
    "Снаряд разорвался в небе, образовав множество красивых искр. Начинкой оказался фейерверк."
    "Искры слились в один красноватый поток.{w=1} Он так быстро несся по небу, что различить его цвет было трудно."
    "Произошёл второй взрыв.{w=1} Вылетело ещё больше искр."
    "Константин увидел в этом красные ромбы и причудливые геометрические фигуры."
    "Цвет искристого потока стал быстро меняться, после чего всё рассеялось в воздухе.{w=1} Сладко пахло порохом."
    scene bg ext_road_night2
    show image oleg_happy at right
    show image pas_rpg at left
    show image pas_smile at left
    show image liz_smile
    with byso
    oleg "Это было шикарно!"
    liz "Да... {w=1}И в правду красиво..."
    pas "Сам такого результата не ожидал, но вышло отлично.{w=1} Уже хочется посмотреть, как она работает в бою."
    hide image oleg_happy
    hide image pas_rpg at left
    hide image pas_smile at left
    with byso
    "Гордон и Олег развернулись и ушли обратно."
    pas "Ну мы в мастерскую.{w=1} Догоняйте."
    hide image liz_smile with byso
    "Константин пожал плечами и пошёл за ними."
    play sound2 sfx_pat_shoulder_hard volume 1
    "Вдруг, он почувствовал, что Лиза взяла его за руку."
    liz "Подожди..."
    show image liz_dontlike with byso
    "Константин обернулся и остановился, посмотрев Лизе в глаза."
    liz "Я хотела..."
    liz "Это...{w=1} Ну..."
    liz "Извиниться за то, что тебе сегодня наговорила..."
    "Было видно, что Лиза хотела что-то сказать, но получалось у неё это плохо."
    hide image liz_dontlike
    show image liz_sad
    with byso
    liz "Я просто сорвалась."
    liz "Знаешь, как бывает, понимаешь, и не можешь контролировать себя."
    liz "А иногда получается так, будто контролируешь."
    liz "Наверное, это от избытка чувств.{w} Ведь столько событий навалилось..."
    liz "Прости, пожалуйста, я была слишком взвинчена."
    play sound2 glad volume 1
    hide image liz_sad
    show image liz_surp at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Константин, не долго думая обнял Лизу."
    kt "Ничего страшного.{w=1} Я сам не лучше.{w=1} Никто не был прав."
    kt "Только сейчас мы оба правы."
    kt "Просто мы не умеем это признать."
    kt "У нас это общая беда – ни хера не понимать в своей жизни."
    kt "Так что давай просто закроем эту тему.{w=1} Забудем всё это. {w}Идет?"
    hide image liz_surp
    show image liz_smile at center:
        zoom 1.5
        yanchor 0.1
    with byso
    liz "Идёт."
    hide image liz_smile
    show image liz_smile
    with byso
    "Освободившись от объятий друг друга, они направились обратно в мастерскую."
    kt "Что делала на протяжении дня?"
    hide image liz_smile
    show image liz_grin
    with byso
    "Лиза разворошила волосы и улыбнулась."
    liz "Бездельников делом занимала и в агроцехе помогала.{w=1} А ты чего?"
    kt "Да целое приключение..."
    scene bg ext_camp_entrance_night
    show image liz_smile
    with fade
    "Под рассказы Константина, они вернулись к воротам."
    liz "Весело ты время провёл..."
    kt "Да, есть такое.{w=1} Я сейчас к Гордону. Ты со мной?"
    hide image liz_smile
    show image liz_surp
    with byso
    liz "А что там?"
    kt "Он выпить предлагал.{w=1} Пойдёшь или не в настроении?"
    hide image liz_surp
    show image liz_smile
    with byso
    "Лиза тепло улыбнулась и отвела взгляд."
    liz "Уже в настроении, идём."
    scene bg ext_clubs_night
    show image liz_smile
    show image oleg_think at left
    show image pas_rpg at right
    show image pas_normal at right
    with byso
    play sound2 sfx_metal_door_heavy_close volume 1
    "Охранник закрыл за ними ворота и вернулся в спящий режим.{w} У входа стояли Гордон и Олег, покуривая созданные днем сигареты."
    oleg "Да, от настоящих вообще не отличишь."
    hide image pas_normal
    show image pas_smile at right
    with byso
    pas "Ну дк я тебе говорю, молодой.{w} {i}Кое что{/i} сделает что угодно.{w=1} В лучшем качестве."
    kt "Гордон, ты не против, если с нами Лиза посидит?"
    stop music fadeout 3
    "Пару раз пыхнув он ухмыльнулся."
    pas "Посидеть может.{w} Выпить?{w=1} Я подумаю."
    hide image liz_smile
    show image liz_grin
    with byso
    liz "Ну ты скряга..."
    pas "Да шучу-шучу, молодая.{w=1} Пошли."
    play sound2 sfx_open_door_clubs_2 volume 1
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_clubs_male_night
    show image liz_smile
    show image oleg_think at left
    show image pas_normal at right
    with byso
    play sound2 sfx_open_door_2 volume 1
    hide image pas_normal with byso
    play music proshloe fadein 3
    "В мастерской уже стояли стулья, а Гордон отложил гранатомёт и вошёл на склад."
    pas "Раз нас больше, то щас возьму ещё одно сидалище."
    play sound2 sfx_mystery_movement volume 1
    hide image oleg_think
    show image oleg_smile at left
    with byso
    "Олег, Лиза и Константин сели на стоящие стулья, после чего переглянулись."
    oleg "Уже помирились?"
    liz "Да."
    kt "Достигли взаимопонимания."
    pas "Ну вот и отлично."
    show image pas_normal at right with byso
    "Гордон вернулся со стулом, рюмкой и бутылкой водки <<Столичная>>."
    pas "Ща ещё будет."
    hide image pas_normal with byso
    pause 0.5
    play sound sfx_blow_out_candle
    show image pas_smile at right with byso
    "Занырнув под стол, Гордон достал оттуда ещё одну бутылку водки, хлеб и добавил к этому пару бутылок <<лимона>>."
    hide image oleg_smile
    show image oleg_shy at left
    with byso
    oleg "А у нас с пропорциями всё правильно?{w=1} Один к одному?"
    hide image pas_smile
    show image pas_angry at right
    with byso
    pas "Ну чё ты как девочка, а?"
    pas "Вот мы с парнями на заводе хуярили одну такую в одно рыло, занюхивая рукавом."
    hide image liz_smile
    show image liz_laugh
    with byso
    "Константин и Лиза рассмеялись, после чего подвинули к себе рюмки."
    hide image oleg_shy
    show image oleg_smile at left
    with byso
    oleg "О, а давайте поиграем в <<было - не было>>?!{w=1} Я вопросы составил!"
    hide image pas_angry
    show image pas_normal at right
    with byso
    pas "Чего?"
    hide image liz_laugh
    show image liz_grin
    with byso
    liz "Это такая игра, где один человек задаёт вопрос, а другой, если отвечает <<да>>, выпивает одну рюмку."
    hide image pas_normal
    show image pas_smile at right
    with byso
    "Гордон ощерился и посмотрел на Константина."
    pas "Ну ты посмотри, как молодёжь научилась девок спаивать, а."
    kt "Да сам в шоке."
    liz "Не хотите - не играйте."
    kt "Да ладно я играю."
    pas "Ну, молодая, поехали, чё."
    "Гордон разлил огненную воду по рюмкам и в пропорции 3 <<лимона>> к 1 водке добавил растворитель."
    play sound2 sfx_paper_bag volume 1
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    "Олег развернул листок с вопросами."
    th "А, так он ещё и готовился...{w=1} Понятно."
    oleg "Итак, первый вопрос."
    oleg "Однажды выпил столько, что потом ничего не помнил."
    "Все дружно взялись за рюмки и переглянулись."
    pas "Кто так не делал - тот не жил."
    kt "Соглашусь.{w=1} За вечер."
    hide image liz_grin
    show image liz_laugh
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    "Они чокнулись и выпили ядрёный напиток."
    "Водка прошлась по горлу, как раскаленный утюг.{w=1} В голове и сердце разлилось томное тепло."
    "Обновив напитки, Гордон подпёр рукой голову."
    pas "Уж слишком легко пошла...{w=1} Куда-а?!"
    play sound2 sfx_face_slap
    hide image oleg_smile
    show image oleg_shy at left
    hide image liz_laugh
    show image liz_grin
    hide image pas_smile
    show image pas_angry at right
    with bso
    "Шлёпнув Олега по руке, которая тянулась к хлебу, Гордон строго на него посмотрел."
    pas "Первую не закусывают!"
    oleg "Ладно...{w=1} Кхм...{w=1} Тогда второй вопрос."
    hide image oleg_shy
    show image oleg_happy at left
    hide image liz_grin
    show image liz_surp
    with byso
    oleg "Делал обнаженные фотографии."
    "Все с удивлением посмотрели на Олега."
    liz "Чего?"
    pas "Нашёлся умник. Дальше давай!"
    hide image oleg_happy
    show image oleg_shy at left
    with byso
    oleg "Ну нет и нет..."
    hide image oleg_shy
    show image oleg_smile at left
    hide image liz_surp
    show image liz_bukal
    with byso
    oleg "Спал с тем, кто меня не привлекал."
    pas "Блять, да что ты там понаписал!{w} Дай сюда!"
    hide image oleg_smile
    show image oleg_shy at left
    with bso
    "Гордон выхватил у Олега бумажку, а Константин взял рюмку."
    hide image liz_bukal
    show image liz_surp
    with byso
    "Лиза с удивлением на него посмотрела."
    liz "Что, правда?"
    kt "Да.{w=1} Было такое.{w} Сам того не хотел, но так вышло."
    "Под удивлённый взгляд Лизы, он опустошил рюмку."
    "Водка пошла уже проще.{w=1} Он обновил свой напиток и посмотрел на Гордона, который вчитывался в бумажку."
    pas "Ну ты и навалял тут...{w=1} Так.{w=1} Далее."
    hide image pas_angry
    show image pas_smile at right
    with bso
    pas "Во. Тест на молодёжь.{w=1} Играл в игру <<Было не было>> ранее."
    hide image oleg_shy
    show image oleg_smile at left
    hide image liz_surp
    show image liz_grin
    with bso
    "Лиза и Олег взяли рюмки и без особых пояснений выпили."
    "Олег, наконец, взял хлеб и закусил."
    hide image pas_smile
    show image pas_angry at right
    with byso
    pas "Ну ты конечно да...{w=1} Пить явно не твоё."
    hide image oleg_smile
    show image oleg_shy at left
    with bso
    oleg "А что такого?"
    hide image pas_angry
    show image pas_normal at right
    with byso
    pas "Нет, ничего.{w=1} Далее."
    hide image pas_normal
    show image pas_smile at right
    with byso
    pas "Был в запое больше двух дней."
    hide image oleg_shy
    show image oleg_smile at left
    with byso
    "Гордон и Константин, взяв рюмки, улыбчиво переглянулись."
    kt "За алкоголизм!"
    pas "Давай!"
    "Снова выпив, они пополнили рюмки."
    pas "Так, чё там у нас далее..."
    play sound2 sfx_paper_bag volume 1
    hide image pas_angry
    show image pas_smile at right
    with bso
    "Он вчитался в листок.{w=1} То, что он там видел, ему явно не нравилось."
    hide image pas_angry
    show image pas_normal at right
    with byso
    pas "Была работа, которую вы ненавидели."
    hide image pas_normal
    show image pas_smile at right
    with byso
    "Константин и Лиза взяли рюмки."
    kt "Задавай попроще вопросы.{w=1} Я так завтра не проснусь."
    hide image liz_grin
    show image liz_laugh
    with byso
    liz "Ничего, потащим."
    "Чокнувшись, они, глядя друг на друга, выпили."
    "Олег долил им напитки.{w=1} Одна бутылка <<лимона>> уже закончилась."
    pas "Плакали при просмотре фильма."
    hide image oleg_smile
    show image oleg_shy at left
    hide image liz_laugh
    show image liz_grin
    with byso
    "Лиза и Олег взяли рюмки."
    hide image pas_smile
    show image pas_normal at right
    with byso
    pas "Ну ладно Лиза, а ты то чё?{w} Олег?!"
    oleg "А как смотреть <<Зелёную милю>>?"
    hide image pas_normal
    show image pas_angry at right
    with byso
    "Он отложил бумажку и прикрыл лицо рукой."
    kt "Вот сидишь, смотришь и напеваешь."
    hide image pas_angry
    show image pas_smile at right
    with byso
    "Гордон сразу понял о чём Константин и рассмеялся."
    kt "Ай-я-я-я-я-я-яй!{w=1} Убили негра"
    hide image liz_grin
    show image liz_laugh
    with byso
    pas "Убили негра, убили"
    kt "Я-я-я-я-яй!{w=1} Ни за что, ни про что, суки, замочили!"
    scene bg int_clubs_male_night
    show image pas_smile at right
    show image liz_grin
    show image oleg_smile at left
    with fade
    "Спустя полторы бутылки водки, они все уже сидели навеселе."
    pas "Так, тихо блять...{w=1} Т-с-с...{w=1} Чёрный ящик."
    oleg "Ну мочи, чё."
    pas "Ща...{w=1} Короче это..."
    pas "Тайно в кого-то влюблен."
    kt "Когда?"
    pas "Дк щас, чё ты тупишь то?"
    hide image liz_grin
    show image liz_smile
    with byso
    "Лиза молча взяла рюмку и искоса посмотрела на Константина."
    th "Чёрт..."
    "Не долго думая, он взял рюмку и опрокинул его содержимое в себя.{w=1} Лиза едва-видно улыбнулась и выпила."
    stop music fadeout 3
    play sound2 sfx_knock_door7_polite volume 1
    hide image oleg_smile
    show image oleg_think at left
    hide image liz_smile
    show image liz_surp
    hide image pas_smile
    show image pas_normal at right
    with bso
    "В дверь постучали."
    pas "Чёрт, кого там..."
    play sound2 sfx_open_door_clubs_2 volume 1
    play music Gallow fadein 3
    show image andr_normal3 at fright
    hide image pas_normal
    show image pas_normal at right
    with byso
    "В мастерскую вошёл Андрей."
    hide image andr_normal3
    show image andr_normal2 at fright
    hide image pas_normal
    show image pas_normal at right
    with byso
    "Посмотрев на стол, где стояли пустые бутылки, он тяжело вздохнул и посмотрел на Гордона."
    andr "Я же просил не напиваться в хлам перед операцией..."
    hide image pas_normal
    show image pas_angry at right
    with byso
    pas "Кто?{w=1} Я?"
    hide image pas_angry
    show image pas_smile at right
    with byso
    pas "Да я завтра буду трезв как стёклышко!{w=1} Вот увидишь."
    hide image andr_normal2
    show image andr_normal at fright
    hide image pas_smile
    show image pas_smile at right
    with byso
    andr "Оставьте нас с Гордоном.{w} Завтра сбор после завтрака."
    andr "Вы переходите в отряд #5."
    andr "До завтра."
    play sound2 sfx_mystery_movement volume 1
    hide image oleg_think
    show image oleg_happy at left
    with byso
    "Все встали из-за стола.{w=1} Олег пошатнулся и чуть не упал."
    oleg "Так точно, т-варищ капитан."
    play sound2 sfx_close_door_1 volume 1
    play ambience ambience_camp_center_night volume 1 fadein 1
    scene bg ext_clubs_night
    show image liz_dontlike at right
    show image oleg_shy at left
    with byso
    hide image oleg_shy with byso
    play sound2 vomit volume 1
    "Выйдя из мастерской, Олег пошёл в кусты и проблевался.{w} Лиза и Константин отвели взгляд."
    liz "Чёт плотно ты нажрался..."
    show image oleg_shy at left with byso
    "Он вытер свои губы и сделал вдох-выдох."
    hide image oleg_shy
    show image oleg_happy at left
    with byso
    oleg "Та не, нормально."
    kt "Перебрал-перебрал...{w=1} Ты это...{w=1} Иди спать."
    play sound2 sfx_put_sugar_cart volume 1
    hide image oleg_happy
    show image oleg_smile at left:
        zoom 1.5
        yanchor 0.1
    hide image liz_dontlike
    show image liz_surp at right
    with byso
    "Олег кивнул и улыбчиво обнял Лизу и Константина."
    oleg "Ох-х, ребята, я вас так люблю-ю..."
    kt "Да, мы тебя тоже..."
    "Константин понял, что Олег просто не дойдёт до своего домика."
    kt "Ты в каком домике живёшь?"
    "В ответ он высвободил руку и указал в сторону первого корпуса."
    oleg "Тама."
    liz "Ну мы тогда тебя дотащим."
    oleg "Не-е, не.{w=1} Я сам."
    kt "Ага, сам ты.{w=1} Пошли давай."
    scene bg ext_square_night
    show image liz_dontlike at right
    show image oleg_shy at left
    with byso
    "Взяв Олега под руки, Константин и Лиза потащили его по указанному направлению."
    liz "М-да, не пёрышко ты нихрена."
    oleg "Да-а, 105 килограмм чистых мышц."
    "Он рассмеялся и отшатнулся."
    hide image liz_dontlike
    show image liz_angry at right
    with byso
    liz "Да, только сейчас ты 105 килограмм алкаша."
    scene bg ext_houses_night
    show image liz_dontlike at right
    show image oleg_shy at left
    with fade
    play sound2 sfx_knock_door_closed_hard1 volume 1
    "Доведя Олега до его домика, они остановились. Дверь была заперта."
    oleg "Бля, а где Саня то?{w=1} Ёк-макарёк..."
    kt "У тебя ключи с собой были?"
    oleg "Да, в кармане."
    "Константин запустил руку в его левый карман."
    "Осознав, что там была дырка, он, словно ошпаренный выдернул руку."
    hide image oleg_shy
    show image oleg_happy at left
    with byso
    oleg "Не, этот карман не для того..."
    play sound2 sfx_keys_rattle volume 1
    "Лиза достала из другого кармана связку ключей и начала открывать дверь."
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_house_of_kt_night
    show image liz_dontlike
    with byso
    play sound2 sfx_put_sugar_cart volume 1
    pause 0.1
    play sound sfx_bed_squeak1
    "Открыв дверь, они занесли Олега внутрь и положили на кровать."
    kt "Всё, спи давай."
    oleg "Да вы чё, я ещё полон сил и энергии!"
    hide image liz_dontlike
    show image liz_angry
    with byso
    liz "Ага, сил.{w=1} Лежи!"
    "Олег спустил ногу с кровати и прикрыл глаза."
    kt "Чёт он быстро..."
    hide image liz_angry
    show image liz_bukal
    with byso
    "Буквально через несколько секунд он начал сопеть - точно уснул."
    "Лиза оставила ключи на столе и пошатнулась на выход."
    liz "Что, тоже поспать решил?{w=1} Пошли проветримся."
    "Константин пожал плечами и пошёл за ней."
    play sound2 sfx_close_door_1 volume 1
    play ambience ambience_camp_center_night volume 1 fadein 1
    scene bg ext_houses_night
    show image liz_normal
    with byso
    liz "Пошли на пирс.{w} Тут не далеко..."
    "Константин достал сигареты и утвердительно кивнул."
    kt "Пошли, чё..."
    scene bg ext_path_night
    show image liz_bukal
    with byso
    play sound2 light_inh volume 1
    "Выйдя на лесную тропу, он закурил и посмотрел на Лизу."
    "Она шла и смотрела в землю, словно пытаясь сформировать мысль в своей голове."
    th "Ладно, как сказал Гордон?{w=1} Пока женщина молчит - лучше её не перебивать..."
    th "Н-да, что-то я сам немного перебрал..."
    th "Давно я не пил живительной водочки...{w=1} Вот и вштырило чёт..."
    hide image liz_bukal
    show image liz_smile
    with byso
    liz "Хорошая сегодня погодка, да?"
    "Константин отвлёкся от своей мысли и затянулся."
    kt "Ну да, как и всегда."
    hide image liz_smile
    show image liz_grin
    with byso
    "Лиза улыбнулась и неловко прикусила губу."
    liz "Классно же, когда погода такая хорошая каждый день?"
    "Он пожал плечами и вставил сигарету в зубы."
    kt "Ну, 50 на 50.{w=1} С какого ракурса посмотреть."
    hide image liz_grin
    show image liz_dontlike
    with byso
    "Она почесала затылок.{w} Ей явно было непонятно о чём поговорить."
    play ambience ambience_boat_station_night volume 1 fadein 1
    scene bg ext_boathouse_night
    show image liz_normal
    with byso
    play sound2 sfx_wood_floor_squeak volume 1
    stop music fadeout 3
    "Выйдя на пирс, они сели на край."
    th "Ну раз она сейчас не как, то я сам..."
    play music summerdays fadein 3
    scene bg zvezda with byso
    kt "Вот что хорошо - звёзды всегда видно.{w=1} В городе это была большая роскошь."
    "Лиза оживилась.{w=1} Ей показалось, что Константин поддержал её желание завести диалог."
    liz "Точно...{w=1} Правда тут они не такие как у нас."
    liz "Тут совершенно другая звёздная карта.{w=1} При том, в разных симуляциях разное положение звёзд."
    "Как-бы невзначай, Лиза положила свою руку на руку Константина."
    th "И тут я понял, за кого она взяла рюмку про тайную влюблённость..."
    th "Ну, в таком случае, посмотрим, верны ли мои догадки."
    th "Всякое же бывает..."
    scene bg ext_boathouse_night
    show image liz_dontlike
    with byso
    "Лиза тоже о чём-то задумалась.{w=1} Константин размял шею и зевнул."
    kt "Что думаешь про завтра?"
    hide image liz_dontlike
    show image liz_surp
    with byso
    liz "А?{w=1} Что?"
    "Растерялась она и даже немного покраснела, после чего сдержанно улыбнулась."
    kt "Завтра.{w=1} Что завтра?"
    hide image liz_surp
    show image liz_sad
    with byso
    liz "Ну, это...{w=1} Опять убивать..."
    liz "Надеюсь, мы победим...{w=1} Да-а..."
    hide image liz_sad
    show image liz_bukal
    with byso
    "В момент в ней что-то изменилось. Она словно собралась и отрезвела."
    liz "Слушай.{w=1} Я тебе хотела кое-что сказать..."
    kt "М-м.{w=1} Что же?"
    hide image liz_bukal
    show image liz_normal
    with byso
    "Она повернулась к нему.{w=1} Константин краем глаза заметил, что она смотрит чётко ему в душу."
    "Он повернулся и посмотрел в её жёлтые глаза."
    "Они были тёплые и добрые.{w=1} На долю секунды ему показалось, будто свет из её зрачков проник в его тёмное сердце и пронзил его насквозь."
    "Но почти сразу же странная мысль заставила его заслониться от этого света – как от огня."
    "Прошла секунда или две, и он понял, в чём дело."
    hide image liz_normal
    show image liz_sad
    with byso
    liz "Я..."
    hide image liz_sad
    show image liz_bukal
    with byso
    liz "Я хотела сказать..."
    kt "Что?"
    hide image liz_bukal
    show image liz_angry
    with byso
    liz "Люблю я тебя, дурак!"
    show blink
    "Вмиг Лиза поцеловала его в губы."
    "Целовала она долго, неторопливо, как бы растягивая момент радости."
    "Такого с ним никогда ещё не было.{w=1} Поцелуи были чувственными, страстными и даже требовательными."
    "Когда поцелуй наконец прервался, Лиза осторожно погладила его по щеке."
    "Это было очень мило, но странно – Константин сам не заметил как она оказалась рядом с его губами."
    "Рука её была чуть прохладной, чуть усталой."
    "Константин понял, что и она тоже ему нравилась.{w=1} В один момент."
    "Как только он это осознал, он решился и поцеловал её в ответ."
    "Лиза, словно и не ожидая от него такой реакции, с удовольствием ответила."
    "Константин почувствовал, как её грудь прижалась и уткнулась к его груди."
    "Она казалась невесомой, пухлой и мягкой.{w=1} Этот момент стал слишком приятным."
    "Её, казалось, переполнила незнакомая прежде нежность, такой, какой он не помнил и сам, совсем непривычная."
    scene bg ext_boathouse_night
    show image liz_sad
    show unblink
    "Они отлипли друг от друга и битва их взглядов продолжилась."
    hide image liz_sad
    show image liz_smile at center:
        zoom 1.5
        yanchor 0.1
    with byso
    kt "Да, и я тебя тоже люблю, Лиза."
    "Лиза и Константин обняли друг друга.{w=1} Им казалось, что их влечет друг к другу неодолимая сила и что вместе они исчезнут в безмерном пространстве ночи."
    "Они не понимали, как такое может быть."
    "Но оба верили, очень верили в то, о чем мечтали."
    hide image liz_smile
    show image liz_grin at center:
        zoom 1.5
        yanchor 0.1
    with byso
    liz "Ты...{w=1} Ты бы знал, как сложно мне было это сказать..."
    play sound2 glad volume 1
    hide image liz_grin
    show image liz_smile at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Константин погладил её по голове, на что она, словно кошка, издала еле слышный писк удовольствия."
    kt "Представляю...{w=1} Тяжело...{w=1} Но не всегда действие завершается провалом, правда."
    liz "Правда..."
    "Вдруг, он вспомнил про камешек, который давал ему Гордон, и достал его из кармана."
    "Камень красиво переливался при лунном свете, и это казалось каким-то чудом."
    hide image liz_smile
    show image liz_dontlike at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Константин протянул его Лизе."
    kt "Это тебе."
    hide image liz_dontlike
    show image liz_surp at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Она была шокирована таким подношением в её сторону."
    liz "Ч-что это?"
    kt "Подарок."
    liz "Но откуда?..."
    kt "Я помогал Гордону и он меня так вознаградил."
    hide image liz_surp
    show image liz_dontlike at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Лиза взяла в руки камень и, посмотрев на сердечко, подняла бровь."
    liz "Странный подарок от парня-парню..."
    "Константин рассмеялся и махнул рукой."
    kt "Да не за тем...{w=1} Чтоб помочь наши отношения загладить."
    hide image liz_dontlike
    show image liz_surp at center:
        zoom 1.5
        yanchor 0.1
    with byso
    liz "Тебе это и в правду было так важно?"
    kt "Важно.{w=1} Только тебя я могу благодарить за то, что я не сгнил в 22-25а."
    hide image liz_surp
    show image liz_smile at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Она подтянула его за воротник и поцеловала."
    "Затем положила его руки себе на плечи, обвила шею и, подняв голову, заглянула в его карие глаза."
    "Он стоял возле ее тела так близко, что она ощущала тепло его кожи."
    liz "Я рада, что я тебе настолько важна..."
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_house_of_kt_night
    show image liz_smile
    with fade
    play sound2 sfx_close_door_1 volume 1
    "Войдя в домик, Константин осмотрелся."
    "Внутри не было никаких лишних вещей. Всё лежало строго по местам."
    hide image liz_smile
    show image liz_grin
    with byso
    liz "Надо уже ложиться...{w=1} Завтра ранний выезд."
    play sound2 sfx_bed_squeak2 volume 1
    "Лиза села на кровать и посмотрела на Константина, который продолжал высматривать что-то в окне."
    kt "Когда?"
    hide image liz_grin
    show image liz_normal
    with byso
    liz "Завтра."
    kt "По времени."
    hide image liz_normal
    show image liz_bukal
    with byso
    liz "Практически после завтрака."
    kt "Ладно.{w=1} Тогда давай спать."
    "Константин снял с себя ботинки и повернулся к свободной кровати."
    play sound2 sfx_bed_squeak1 volume 1
    hide image liz_bukal
    show image liz_smile at center:
        zoom 1.5
        yanchor 0.1
    with vpunch
    "Лиза встала, взяла его за плечи и повалила его на свою кровать."
    liz "Поспишь со мной.{w} Не обсуждается."
    kt "Ладно..."
    "Константин устроился поудобнее.{w=1} Лиза повернулась к нему и посмотрела ему в глаза."
    liz "Спокойной ночи."
    kt "Споки."
    hide image liz_smile with byso
    "Лиза поцеловала его, после чего улыбнулась и закрыла глаза."
    stop music fadeout 3
    show blink
    "Константин мигом уснул."
    pause 3
    liz "Костя, вставай, мы проспали!"
    play music deadrazy2 fadein 3
    play ambience ambience_int_cabin_day volume 1 fadein 1
    scene bg int_house_of_kt_day
    show image liz_normal
    show unblink
    play sound2 sfx_bed_squeak2 volume 1
    "Константин вскочил с кровати и осмотрелся.{w=1} У шкафа стояла Лиза, с пистолетом в руках."
    kt "Что?{w=1} Что случилось?"
    hide image liz_normal
    show image liz_sad
    with byso
    liz "Мы проспали завтрак!{w=1} Нам надо срочно бежать на площадь!"
    kt "Понял."
    "Он принялся в темпе надевать ботинки.{w=1} Головная боль после вчерашней попойки не давала покоя."
    liz "Ты как?"
    hide image liz_sad
    show image liz_smile
    with byso
    kt "Да...{w=1} Голова болит немного...{w=1} А так нормально...{w=1} Видимо перепили чутка..."
    liz "Есть такое..."
    play sound2 sfx_bed_squeak1 volume 1
    "Константин оделся и встал с кровати."
    kt "Всё, идём."
    play ambience ambience_camp_center_day volume 1 fadein 1
    scene bg ext_houses_day
    show image liz_normal
    with byso
    play sound2 door_cl volume 1
    "Выйдя из домика, они быстрым шагом отправились на площадь."
    kt "Надо же было так..."
    hide image liz_normal
    show image liz_smile
    with byso
    liz "Да уж, поиграли в <<Было - не было>>."
    kt "Я больше в такие игры на выпивание не играю..."
    hide image liz_smile
    show image liz_laugh
    with byso
    "Лиза рассмеялась и похлопала его по плечу."
    liz "Все мы так говорим."
    scene bg ext_square_day
    show image tolpa at right
    show image tolpa2 at left
    show image tolpa3
    show image liz_bukal
    with byso
    play ambience ambience_medium_crowd_outdoors fadein 3
    "На площади уже была толпа народу."
    kt "И куда нам?"
    hide image liz_bukal
    show image liz_smile
    with byso
    liz "А вон.{w=1} Олег и Гордон, пошли к ним."
    "Протискиваясь сквозь толпу, он продвигались к знакомым лицам."
    show image pas_normal at left
    show image oleg_shy at right
    with byso
    pas "Дк надо было тебе закусывать..."
    hide image oleg_shy
    show image oleg_angry at right
    with byso
    oleg "Да ты же сам мне это делать запретил!"
    hide image pas_normal
    show image pas_smile at left
    with byso
    pas "О, а вот и остальные алконавты, вы как?"
    hide image oleg_angry
    show image oleg_shy at right
    hide image liz_smile
    show image liz_grin
    with byso
    "Константин и Лиза практически синхронно выдохнули и посмотрели на Гордона."
    kt "Вроде жив."
    liz "Я более-менее."
    pas "Ну отлично! {w=1}Гордый варяг не идёт в бой без похмелья!"
    "Гордон отошёл к дереву и взял оттуда два рельсотрона."
    pas "Вот, молодые, это вам."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    "Он вручил одну пушку Константину, а другую Олегу."
    "После этого он выдал две коробочки."
    pas "Вот оружие, вот патроны.{w=1} Вы в пробивном отряде, потому вам пригодится."
    pas "В коробке 25 патронов.{w=1} Расходуйте с умом."
    liz "Это чего ты так расщедрился?"
    hide image pas_smile
    show image pas_angry at left
    with byso
    pas "Вот захотел и подарил, ёбаный по голове."
    hide image liz_grin
    show image liz_laugh
    with byso
    "Лиза хитро улыбнулась и пристально посмотрела на Гордона."
    liz "Да ну прям."
    hide image pas_angry
    show image pas_smile at left
    with byso
    pas "Ладно-ладно, раскусила, они были на складе наёмников.{w=1} Чистые, не стрелянные."
    hide image liz_laugh
    show image liz_grin
    with byso
    "Константин улыбнулся и посмотрел на Олега."
    kt "Ты то жив?"
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Почти...{w=1} Голова болит - жуть!"
    oleg "Воду прямо из крана пил...{w=1} Надо же было так."
    liz "Оно и понятно..."
    "Ухмыльнулась Лиза и ткнула Олега в плечо."
    pas "Ладно, молодые. {w=1}Вам в пятый отряд. {w=1}Идите."
    kt "Удачи в поле."
    hide image oleg_shy
    hide image liz_grin
    hide image pas_smile
    show image oleg_shy at right
    show image liz_grin at left
    with byso
    "Лиза махнула рукой и повела их в другую сторону площади."
    hide image oleg_shy
    show image oleg_smile at right
    with byso
    oleg "Я вам прихватил поесть..."
    "На скамейке стояли две банки тущёнки и бутылка <<лимона>>."
    hide image liz_grin
    show image liz_angry at left
    with byso
    liz "Боже, опять <<лимон>>?!{w=1} Меня после вчерашнего с него тошнит!"
    hide image oleg_smile
    show image oleg_shy at right
    with byso
    oleg "Я всю воду выпил..."
    "Константин ухмыльнулся и продолжал смотреть на закипающую Лизу."
    stop music fadeout 2
    liz "И почему я не удивлена?"
    play music Kerosene fadein 3
    hide image oleg_shy
    hide image liz_angry
    with byso
    show image andr_normal2 with byso
    "За кафедру у Генды вышел Андрей."
    stop sound_loop fadeout 1
    hide image andr_normal2
    show image andr_normal
    with byso
    "Слегка прокашлявшись, он окинул взглядом всех сопротивленцев, заставив их замолчать и обратить на него внимание."
    hide image andr_normal
    show image andr_smile
    with byso
    andr "Итак, дорогие соратники! Этот день настал!"
    andr "Сопротивление отправляется на самую важную для него операцию!"
    hide image andr_smile
    show image andr_normal
    with byso
    andr "Мы все готовились к этому дню! И вот, спустя столько лет мы ударим!"
    andr "Наша сила – в единстве, а единство – это готовность умереть! Мы не можем проиграть!"
    andr "Но мы можем победить! А чтобы победить, мы не должны бояться смерти!"
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "В этой борьбе у нас не будет правил! Только силы!"
    andr "Выжить и победить в этом бою мы сможем только сообща!"
    andr "Сегодня вы выйдете на арену только с одной мыслью – выжить и найти выход! Давайте соединим свои силы в сегодняшнем танце смерти."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "Если это удастся, война закончится – а вместе с ней прекратится и наше заточение!"
    andr "Любое наше усилие в этой битве – не просто шаг к победе, это шаг на вечную память!"
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Сохраните эту память в сердцах своих соратников!"
    andr "Нас всех ждет триумф! Так победим же вместе!"
    hide image andr_normal
    show image andr_smile
    with byso
    andr "Отряды, по машинам!"
    hide image andr_smile with byso
    "Толпа зашумела и направилась к выходу из лагеря."
    show image oleg_shy with byso
    oleg "Идёмте, наш автобус выезжает первый."
    scene bg ext_clubs_day
    show image tolpa
    with byso
    "Взяв все припасы, они направились к выходу из лагеря."
    window hide dissolve
    $ set_mode_nvl()
    "Речь капитана смогла мотивировать сопротивленцев.{w=1} Все дружно маршировали в бой."
    "Константин даже не был уверен, что кто-то из них понимает происходящее."
    "Впрочем, из их разговоров он понял, как именно были мотивированы остальные."
    "Они были готовы умереть в бою, если речь шла о свободе.{w=1} Так было в старом мире, но Константин только теперь принимал этот боевой настрой как должное."
    "Эта война действительно была страшной – другой не бывает.{w=1} Но игра стоила свеч."
    "Иногда им стоило бы забывать, кто они и почему сражаются за чужой мир."
    "Ради светлого будущего, которое им может быть дано.{w=1} А может не быть..."
    "В этом мире чудес много – сейчас действительно надо было за него драться."
    "Даже вопреки здравому смыслу, который может в любой момент перекрыть чувства."
    "В любом случае – жить или умереть. {w=1}Ставить на темную лошадку не приходилось."
    "И вот новая ипостась мышления окончательно перешла на новый этап: будущее было всего лишь длинной цепью осмысленных действий, которую надо решить в нужный момент."
    window hide dissolve
    $ set_mode_adv()
    scene bg ext_bus
    show image tolpa
    with byso
    chel "Солдаты, в автобус!"
    play ambience ambience_camp_center_day volume 0.61 fadein 1
    scene bg int_avtobus
    show image tolpa at center:
        zoom 1.5
    with byso
    "Константин вошёл в автобус и думал, где ему сесть с Лизой и Олегом."
    window hide
    menu:
        "Передние места.":
            $ renpy.block_rollback()
            $ event1 += 1;
            kt "Давайте сюда.{w=1} Долго идти не придётся."
            oleg "Как скажешь."
            show image oleg_shy at right
            show image liz_bukal
            with byso
            "Усевшись на передний ряд, они сложили всю экипировку себе в ноги."
        "Задние места.":
            $ renpy.block_rollback()
            kt "Давайте туда.{w=1} Чтоб вокруг народ не толпился."
            liz "Идём."
            show image oleg_shy at right
            show image liz_bukal
            with byso
            "Усевшись на задний ряд, они сложили всю экипировку себе в ноги."
    chel "Мы отправляемся!"
    play sound korobka_peredach volume 1
    play sound2 sfx_ikarus_open_doors volume 1
    play ambience bus_inside volume 0.21 fadein 1
    "Выкрикнул водитель и заскрипел коробкой передач. Двери автобуса закрылись и он начал движение."
    "Лиза достала две металлические банки и вилки."
    stop music fadeout 3
    hide image liz_bukal
    show image liz_smile
    with byso
    liz "Вот теперь можно и поспать."
    "Она протянула одну банку и вилку Константину.{w=1} Тот принял продукты и благодарно кивнул."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Приятного аппетита..."
    liz "Спасибо."
    kt "Благодарю..."
    scene bg int_avtobus2
    show image tolpa at center:
        zoom 1.5
    show image oleg_shy at right
    show image liz_smile
    with byso
    "Они покинули симуляцию сопротивления."
    play music Radar fadein 3
    "Константин, поедая тушёнку, попутно искоса осматривал сопротивленцев."
    "Большинство из них были похожи на обычных пустышек."
    "Некоторые из них даже выглядели как две капли воды."
    "Хмыкнув, Константин перевёл взгляд себе в банку."
    th "М-м...{w=1} Тушняк..."
    "После этой многозначной мысли Константин обратил внимание на Олега."
    "Он был весьма встревожен и просто смотрел в окно."
    hide image liz_smile
    show image liz_normal
    hide image oleg_shy
    show image oleg_think at right
    with byso
    kt "Что с тобой, Олег?"
    oleg "Да стрёмно мне."
    hide image liz_normal
    show image liz_bukal
    with byso
    liz "Всем стрёмно.{w=1} Никто умирать ещё раз не хочет."
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Да это понятно... Но против нас ещё наёмники."
    kt "С чего ты взял?"
    "Олег задумался и перевёл взгляд на Константина."
    oleg "Ну мы же их вышвырнули, так?{w=1} Так."
    oleg "Даже с учётом того, что большую часть своего снаряжения они оставили у нас, то они всё равно опасны."
    hide image liz_bukal
    show image liz_dontlike
    with byso
    liz "Это кто тебе такую умную мысль донёс?"
    play sound2 sfx_click_1 volume 1
    "Он тяжело вздохнул и, взяв в руки рельсотрон, отрыл отсек в прикладе."
    oleg "Гордон про это говорил, пока паял свою ракетницу..."
    kt "Было бы неплохо, если бы они у нас на пути не стояли."
    hide image liz_dontlike
    show image liz_bukal
    with byso
    liz "Да уж, проблем у нас и так хватает в лице Генды."
    "Константин покончил с едой и, взяв бутылку лимонного напитка, сделал несколько глубоких глотков."
    play sound2 sfx_stomach_growl volume 1
    "Желудок недовольно заурчал.{w=1} Видимо, он так напоминал о том, что заливали в него вчера."
    kt "Выпить нормального сока как мотивация для победы. Невозможно уже эту чачу пить..."
    hide image liz_bukal
    show image liz_smile
    with byso
    "Лиза улыбнулась и взяла у Константина бутылку."
    liz "Ну так выпьем же за это."
    "Цинично проговорила она и сделала пару глотков."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "А вы совсем не беспокоитесь о том, что впереди у нас бой?"
    kt "Лично я нет.{w=1} Мне либо всё - либо ничего."
    liz "Согласна...{w=1} Правда часть этого <<всего>> я уже получила."
    "Она немного покраснела и отвела взгляд в окно."
    kt "А кто знает сколько нам ехать?"
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Полчаса. Сейчас уже можешь вычесть 10-15 минут."
    kt "Так близко?"
    hide image liz_smile
    show image liz_bukal
    with byso
    liz "Ага...{w=1} Это тебе не до 22-25а ехать 9 часов."
    liz "А ведь всего несколько дней назад мы тебя впервые везли в сопротивление..."
    liz "Сейчас вот - подрос.{w=1} Уже прапор."
    kt "Что, материнский инстинкт проснулся?"
    play sound2 sfx_punch_medium volume 1
    hide image oleg_shy
    show image oleg_smile at right
    hide image liz_bukal
    show image liz_angry
    with byso
    "Константину удалось растопить тревогу на лице Олега, а Лиза недовольно ткнула его в бок."
    liz "Тоже мне, Петросян..."
    kt "Слушай, Олег, объяснишь как работает рельсотрон?"
    hide image oleg_smile
    show image oleg_shy at right
    with byso
    oleg "Да, конечно, давай свой."
    play sound2 sfx_punch_medium volume 1
    "Константин взял свой рельсотрон и протянул Олегу."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Короче смотри.{w} Как мне объяснял Гордон."
    oleg "Это для включения."
    play sound2 sms volume 0.1
    "Проигрался тихий звуковой сигнал."
    oleg "На экран не обращай внимания, там параметры."
    oleg "Эта кнопка - предохранитель."
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Вот эта штука для настройки мощности.{w=1} Лучше оставить на середине."
    oleg "Это - открыть блок со снарядами."
    play sound2 sfx_click_1 volume 1
    "По нажатию, открылся лючок в прикладе."
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Можно зарядить до 5 снарядов. {w=1}Вот."
    oleg "В целом всё. Как самая обычная винтовка."
    play sound2 sfx_pat_shoulder_hard volume 1
    "Олег вернул Константину рельсотрон."
    kt "Ладно, я понял."
    play sound2 reload volume 1
    "Пробубнил он и начал загружать шары в рельсотрон."
    liz "Я лично ничерта не поняла..."
    kt "Так ты и не стреляешь из него."
    hide image liz_angry
    show image liz_grin
    with byso
    liz "Не заставляй вспоминать анекдот про клоуна."
    stop music fadeout 3
    chel "Внимание, отряд!{w=1} Через две остановки наша!"
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Начинается..."
    play music shabash fadein 3
    hide image liz_grin
    show image liz_bukal
    with byso
    "Константин и Олег взяли рельсотроны, а Лиза достала из кобуры люгер."
    th "Вот и настаёт момент истины..."
    kt "Вы готовы?"
    hide image liz_bukal
    show image liz_smile
    with byso
    liz "Как никогда!"
    hide image oleg_shy
    show image oleg_think at right
    with byso
    oleg "Готов."
    kt "Какой у нас план?"
    hide image liz_smile
    show image liz_bukal
    with byso
    liz "Мы будем зачищать часть третьего корпуса и контролировать административный корпус."
    "Константин удивлённо посмотрел на Лизу."
    kt "А зачем нам админка местная?"
    liz "Андрей говорил, что там могут быть наёмники.{w=1} Не могу сказать, чем он руководствовался, когда такое указание давал..."
    kt "Не, ну надо - значит надо..."
    "Протянул Константин и повертел в руках коробочку с патронами для рельсотрона."
    chel "Следующая наша!"
    chel "Орудия на изготовку!"
    play sound2 sfx_click_3 volume 1
    "Олег снял рельсотрон с предохранителя.{w=1} Константин, не долго думая, сделал так-же."
    "Автобус начал снижать скорость."
    chel "Не бойтесь, бойцы!{w=1} Бьёмся до победного!"
    hide image liz_bukal
    show image liz_angry
    with byso
    liz "Н-да, нашёлся мотиватор."
    "В окне пронеслись ЛЭПы."
    kt "Что-ж, да начнётся..."
if event1 == 1:
    play sound sfx_nightmare_explosion
    scene bg black with fl_fire
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    "Взрыв."
    "Автобус передним колесом наехал на мину."
    window hide dissolve
    scene bg black with byso
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
else:
    jump byuiervhwvuoebrwvuihbuwovbnfhiuowsvbnhuws
label byuiervhwvuoebrwvuihbuwovbnfhiuowsvbnhuws:
    play sound sfx_nightmare_explosion
    scene bg black with vpunch
    play ambience amb_fire volume 1 fadein 1
    play sound2 bus_inc volume 2
    play music "<from 34.5>inrealnost/Music/Music/Burnout.mp3"
    "Взрыв."
    "Автобус накренило на ходу и он боком начал скрестись о землю."
    liz "Костя, Олег, вы целы?!"
    scene bg int_fire
    show unblink
    kt "Я цел!"
    oleg "Я тоже!"
    kt "Выбираемся отсюда живо!"
    play sound2 sfx_mystery_movement volume 1
    "Ни одно из окон не уцелело, а все уцелевшие начали выбираться из горящего автобуса."
    show image oleg_think at right with byso
    show image liz_rage at left with byso
    oleg "Чёртовы наёмники!"
    "Из полного состава автобуса выжило только 8 человек, которые находились на самых дальних местах."
    "Вдалеке приближался второй автобус."
    liz "Нам надо скооперироваться с ними!"
    "Автобус замедлялся с каждой секундой."
    play sound2 bum volume 1
    scene bg int_fire with fl_fire
    "Взрыв."
    "Второй автобус даже подлетел."
    play sound2 bus_inc volume 1
    "Упав на землю, он упал на колёса и, вспахивая землю врезался в предыдущий."
    chel "Что за чертовщина происходит?!"
    oleg "Тут есть выжившие?!"
    chel2 "Есть!"
    "Из автобуса начали выбегать люди с оружием, которое сумели спастись."
    "По подсчётам Константина, из двух автобусов выжило только 14 человек, включая их."
    chel "Бойцы, выполняем приказ!"
    chel2 "В бой!"
    chel3 "За свободу!"
    "Огромная толпа народу понеслась в лагерь. Лиза хотела их остановить, но безуспешно."
    dvp "А-а-а!"
    "Из горящего автобуса пыталась выбраться девочка, похожая на Алису."
    play sound2 bum volume 1
    "Снова прогремел взрыв." with vpunch
    "На этот раз подорвался сам автобус, разбросав части тел по округе."
    "Олега чуть не вырвало от такого представления."
    "Подъезжал третий автобус."
    show image oleg_think at right with byso
    show image liz_rage at left with byso
    liz "Но они же не подорвутся?!"
    "Автобус остановился в штатном режиме. А за ним ещё два."
    hide image liz_rage
    hide image oleg_think
    with byso
    show image val_surprise at right
    show image pas_rpg at left
    show image pas_angry at left
    show image andr_nervous2
    with byso
    "Из одного автобуса вышел капитанский отряд."
    andr "Бойцы, не стойте!{w=1} В бой!"
    mip "Вы слышали, что сказал капитан, отряд?! В бой."
    "Из автобуса начала вываливаться огромная толпа народа, которая с криками побежала в лагерь."
    hide image andr_nervous2
    show image andr_rage
    with byso
    andr "<<Дзета>>, <<Свинец>>?!{w=1} Что за чертовщина тут произошла?!"
    liz "Два автобуса подорвались!{w=1} Не видно?!"
    pas "Это точно наёмники!"
    andr "Всё, вперёд! Нам надо работать!"
    scene bg ext_camp_entrance_night with byso
    "Отряд Константина вместе с отрядом капитана направился в лагерь."
    scene bg ext_clubs_night
    show image poter_n
    with byso
    play ambience fireing volume 1 fadein 1
    scene bg ext_clubs_night
    show image poter_n
    with byso
    "У дверей стоял потерянный пионер."
    liz "Опять ты, мудила?!"
    hide image poter_n
    show image poter_s
    with byso
    pp "А вот и вы, уёбки!"
    show image rkis_normal at center:
        xanchor 2 yanchor -0.01
        linear 0.2 xanchor -0.01
    play sound2 sfx_armature_swish volume 1
    "Робокошка набросилась на пионера, но не смогла его убить.{w=1} Её рука прошла насквозь."
    hide image rkis_normal with vpunch
    play sound2 magic volume 1
    "Выстрелом плазмы пионер распылил робокошку.{w=1} Гордон выхватил своё орудие."
    kt "Ты что вытворяешь?!"
    pp "Костя, тварь, ты меня оставил!{w=1} Пришло время объяснить свой поступок."
    show image pas_rpg at fleft
    show image pas_angry at fleft
    with bso
    pas "Лови аптечку, хуила спектральная!!!"
    play sound2 rpg volume 1
    pause 0.5
    play sound2 bum volume 0.76
    scene bg ext_clubs_night
    show image pas_rpg at fleft
    show image pas_angry at fleft
    with fl_fire
    show image liz_angry at right
    show image andr_nervous2
    with byso
    "Гордон попал чётко в пионера, разорвав его на части. Остановить процесс распада пионера было уже невозможно."
    "Части его тела разлетелись в радиусе 5 метров и, секунду пролежав, обрели материальное воплощение, рассыпавшись в прах."
    pas "Съел блять?!"
    oleg "Так просто?!"
    pas "Технологии рулят, детка!"
    pas "Робокошки!{w=1} Выбить дверь!"
    show image rkis_normal at left with byso
    rkis "Есть."
    play sound2 door_break volume 1
    "Робокошка пробила дверь насквозь и открыла." with vpunch
    andr "Выполняйте свою задачу, после чего отправляйтесь на площадь!"
    kt "Так точно!{w=1} Побежали!"
    scene bg ext_houses_night with fade
    "В третьем корпусе вокруг хаотично бегали пустышки, пытаясь спастись от сопротивленцев."
    show image liz_rage at right with byso
    liz "Огонь по пустышками!"
    show image oleg_angry at left with byso
    "Все трое достали малокалиберное орудия и начали стрелять по пионерам."
    show sl scared pioneer with byso
    "Мимо пронеслась Славя, которая пыталась укрыться от пуль, но попала на мушку Константина."
    sl "Нет, не надо!"
    play sound pistol
    hide sl with fl_scare
    "Константин без каких либо угрызений совести застрелил светловолосую девочку, окрасив стены домика кровью."
    window hide dissolve
    $ set_mode_nvl()
    "Кругом бегали подростки разных возрастов.{w=1} Сопротивленцы без какой либо пощады отстреливали их, словно они и не люди вовсе."
    "Четыре."
    "Восемь."
    "Шестнадцать."
    "Двадцать пять убийств на счету отряда Константина."
    "Раненых не было."
    "Константин не чувствовал никакой угнетающей душу тревоги."
    "В его душе образовалась пустота."
    "Пустота была настолько огромной, что он уже не ощущал ничего, за исключением нее."
    "Никакого дна, никакой границы.{w=1} Все было смутно и неясно."
    "Он просто убивал."
    "Его разум был холоден и равнодушен."
    "Самого Константина не пугала жестокая судьба, уготованная остальным."
    "Когда по всей площади лагеря раздавались крики о помощи, он просто механически нажимал на спусковой крючок, зная, чем все кончится."
    window hide dissolve
    $ set_mode_adv()
    liz "Всё, теперь на зачистку в административный!"
    kt "Понял-принял, ретируемся!"
    scene bg ext_admins_night
    show image oleg_angry at right
    show image liz_angry at left
    with byso
    "Достаточно быстро они добрались административного корпуса. Им надо было выбрать подход."
    oleg "Давайте напролом!"
    "Олега явно опьянило происходящее.{w=1} По его лицу было видно, что адреналин зашкаливает."
    hide image liz_angry
    show image liz_rage at left
    with byso
    liz "Да если там кто-то есть, то нас на фарш пустят!{w=1} Какой нахер напролом?!"
    window hide
    menu:
        "Пройти напролом.":
            $ renpy.block_rollback()
            hide image liz_rage
            show image liz_angry at left
            with byso
            kt "Штурмуем."
            oleg "Погнали!"
            play sound door_break
            scene bg int_admins
            show image liz_rage
            with vpunch
            "Олег вышиб дверь, чем активировал растяжки."
            liz "Идио-от!"
            play music bum volume 1.4
            scene bg black with fl_fire
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            "Отряд разорвало на части."
            window hide dissolve
            scene bg black with byso
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
        "Пройти тихо.":
            $ renpy.block_rollback()
            hide image liz_rage
            show image liz_angry at left
            with byso
            kt "Пойдём тихо."
    liz "Действуем."
    play sound2 sfx_door_squeak_light volume 1
    "Константин аккуратно приоткрыл дверь, после чего обнаружил, что на двери была растяжка."
    kt "Через дверь не вариант.{w=1} Через окно."
    oleg "Ща!"
    play sound2 glass_break2 volume 1
    hide image oleg_angry with byso
    "Выбив прикладом рельсотрона окно, Олег проник в административный корпус."
    play ambience fireing volume 0.41 fadein 1
    scene bg int_admins
    show image oleg_angry at right
    show image liz_angry at left
    with byso
    "Лиза и Константин залезли за ним."
    liz "Сказали же тихо...{w=1} Олег, хватит орать."
    hide image oleg_angry
    show image oleg_shy at right
    with byso
    oleg "Понял."
    "Умерив свой пыл проговорил он и отряд направился по кабинетам."
    play sound2 sfx_door_squeak_light volume 1.2
    "Пока Лиза и Олег проверяли комнаты, Константин аккуратно забрал букет гранат, подвешенных к двери."
    hide image liz_angry
    show image liz_surp at left
    with byso
    liz "Что ты делаешь?..."
    kt "Подарки готовлю..."
    liz "А если бахнут?..."
    kt "Всё под контролем."
    hide image oleg_shy
    show image oleg_think at right
    hide image liz_surp
    show image liz_dontlike at left
    with byso
    "Взяв гранаты, они услышали разговоры на втором этаже."
    kt "Туда..."
    "Поднявшись, они осознали, что в 203 кабинете шли переговоры."
    scene bg int_admins_room
    show image sopr_soldb at cright
    show image sopr_soldb2 at cleft
    show image spy
    with byso
    "Константин заглянул в щель.{w=1} Там за у стола стояли двое безбожников и о чём-то беседовали."
    sold "А если они не убьют Генду?"
    sold_sm "Тогда мы этих фраеров подорвём вместе с ним!{w=1} <<Колесников>>, не тупи!"
    sold_c "Да откуда тебе знать что ему этого хватит, ёбана?!"
    sold_sm "Оттуда!{w=1} В прошлый раз почти хватило!{w=1} Когда я проводил инструктаж, нехуй было еблом щёлкать!"
    sold_c "Ладно, я тебя понял...{w=1} Тогда ждём."
    sold_sm "Они уже почти обнулили стабильность. Долго не придётся фраерков ждать."
    play sound2 door_break volume 1
    hide image spy with vpunch
    "Константин распахнул дверь."
    kt "Сам ты фраер!"
    scene bg int_admins with byso
    "Он закинул пачку гранат в кабинет."
    kt "Бежим!"
    sold_sm "Ёбаный в рот!{w=1} Граната!!!"
    play sound2 bum volume 1
    "Взрыв." with vpunch
    show image oleg_think at right with byso
    "Шум в комнате прекратился.{w=1} Олег заглянул в комнату."
    hide image oleg_think
    show image oleg_shy at right
    with byso
    oleg "Ух ты-ж блять!"
    "Олега снова чуть не стошнило. Для него сегодня был, своего рода, день рвотного рефлекса."
    show image liz_rage at left with byso
    liz "С ними покончили!{w=1} Теперь на площадь!"
    play ambience fireing volume 1 fadein 1
    scene bg ext_square_night_blood
    show image tolpa
    show image oleg_shy at left
    show image liz_rage at right
    with fade
    "Вернувшись на площадь, они заметили, как враги отступали."
    oleg "Уже всё сделали без нас?!"
    pas "Идолопоклонники отступают!"
    andr "Не дайте им уйти!"
    show weapon_fireing with vpunch
    "Все остававшиеся сопротивленцы начали стрелять в спины убегающих с поля боя."
    "Вот их осталось 15."
    "Через несколько секунд уже 8."
    "И, наконец, меньше пяти."
    play ambience ambience_camp_center_night volume 1 fadein 1
    scene bg ext_square_night_blood
    show image tolpa
    show image oleg_think at left
    show image liz_surp at right
    with fade
    "Сопротивлению удалось победить.{w=1} Все их враги пали."
    oleg "Это конец?!"
    show image andr_angry2 with byso
    andr "Ещё нет, нам надо..."
    gg "Так-так-так..."
    scene bg ext_square_night_blood_red with byso
    scene bg genda with byso
    "Небо окрасилось красным, а со стороны входа в лагерь объявился Генда."
    gg "А вас стало ещё меньше...{w=1} Всего-то 40 человек."
    gg "Тоже мне...{w=1} <<Сопротивление>>..."
    gg "О, а среди вас есть знакомые лица..."
    gg "Калинин Андрей Романович.{w=1}.. Я думал тебя убило вместе с тем Мишей..."
    gg "Беспалов Виктор Антонович.{w=1}.. Так и не предал своё инженерное дело..."
    gg "И Брусков Константин Павлович.{w=1}.. Не думал, что ты так сильно меня возненавидишь..."
    andr "Хватит пиздеть!{w=1} Отряд, огонь на поражение!"
    play sound_loop fireing volume 1
    show genda_fire with byso
    "Вce оставшиеся на площади открыли огонь по создателю.{w} Все заряды пролетали сквозь него, не оставляя никаких повреждений."
    stop sound_loop fadeout 1
    hide genda_fire
    scene bg genda
    with byso
    "Осознав, что это не эффективно, они прекратили огонь."
    gg "Очень мило..."
    play sound sfx_energy_door_bus
    stop music fadeout 3
    scene bg ext_square_night_blood_red with vpunch
    "Раздался странный звук и Генда упал на землю."
    show image andr_smile with byso
    play music deadrazy4 fadein 3
    andr "Да!!!"
    show pistol12 with fade
    "Андрей достал свой пистолет и прицелился в Генду."
    gg "Что за..."
    gg "Вы..."
    andr "Мы - мы, всё мы!"
    andr "Любопытно...{w=1} Помнишь, как ты меня однажды застрелил?"
    andr "Помнишь...{w=1} Я же знаю..."
    andr "Что-ж, старый, настало твоё время освободить трон для более подходящего кандидата."
    gg "Нет!{w=1} Не смей!{w=1} У меня!...{w=0.41}{nw}"
    "Капитан наклонился и вставил ствол пистолета создателю в глотку."
    andr "Ещё как посмею.{w=1} Прощай."
    play sound2 pistol volume 1
    scene bg ext_square_night_blood_red with fl_scare
    "Андрей спустил курок."
    show image andr_normal with byso
    "Встав в полный рост, он окинул взглядом всех присутствующих."
    hide image andr_normal
    show image andr_smile
    with byso
    andr "Это победа!"
    show image pas_rpg at fleft
    show image pas_smile at fleft
    with byso
    pas "Ура!!!"
    scene bg ext_square_night_blood_red
    show image tolpa
    with byso
    "Поднялась суета.{w=1} Все начали прыгать друг другу в объятия и аплодировать капитану."
    chel "Слава новому предводителю инреальности!"
    hide image tolpa with byso
    stop music fadeout 3
    scene bg ext_square_night_blood_red:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 1 crop (0, 225, 980, 630)
    pause 1
    show image sopr_soldb with dissolve
    "Среди всего этого Константин вдалеке заметил наёмника."
    "Он целился точно в капитана."
    play music unskyidy2 fadein 3
    "Тут Константин решился на несвойственный для себя шаг."
    "Сердце забилось втрое быстрее.{w=1} Рефлексы обострились, а время вокруг словно остановилось."
    th "Теперь я понял, что я могу помочь этим людям..."
    liz "Костя, куда ты..."
    th "Победить!"
    play sound2 pistol volume 1
    scene bg black with fl_fire
    play sound sfx_bush_body_fall
    "Выстрел."
    scene bg zvezda_red
    show unblink
    "Константин заградил своим телом капитана и получил пулю в грудь."
    "Его тело рухнуло на землю.{w=1} Жутко болело сердце или левое лёгкое."
    chel2 "Это <<безбожник>>!{w} Убить его!"
    show image oleg_angry at right with byso
    oleg "Костя?!"
    show image liz_shysurp at left with byso
    liz "Нет!!!"
    "Лиза бросилась к Константину."
    "В его груди была дыра.{w=1} Патрон застрял в груди, и результат был до невозможности прост и ясен."
    liz "Зачем ты это сделал?!"
    andr "Срочно Валентайн сюда!"
    pas "Андрей, Валери мертва!"
    andr "Помогите ему, он истекает кровью!"
    "Судя по всему, повреждение всё-таки пришлось на сердце.{w=1} Константин постепенно начал терять сознание."
    kt "Спасибо вам...{w=1} За всё..."
    kt "Лиза...{w=1} Я...{w=1} Люблю тебя..."
    liz "Нет!!! {w=1}Не смей мне тут умирать!{w=1} Мы победили!"
    kt "Так отпразднуйте победу...{w=1} У меня победа своя..."
    show blink
    stop ambience fadeout 2
    stop music fadeout 3
    "Глаза Константина сомкнулись."
if lizrp == 9:
    jump FromTheBottomOfHeart_ending
else:
    jump WinWin_ending
label WinWin_ending:
    "Последней его мыслью было то, что он умер не зря."
    window hide dissolve
    stop music fadeout 3
    scene bg black with dissolve
    $ unlock_ach_root_inreal(11)
    pause 1.5
    play music "<from 65>inrealnost/Music/Music/PlaceInTheWorldFadesAway.mp3" fadein 3
    scene bg ending_Recycled_cg:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    show ending_WinWin:
        crop (497, 223, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    with Dissolve(26)
    scene bg black with byso
    stop music fadeout 3
    pause 2.6
    jump after_ending_screen
label FromTheBottomOfHeart_ending:
    "Мысли слились воедино, а потом рассыпались, словно частицы головоломки, которые никак не удавалось собрать в единое целое."
    pause 3
    liz "И к чему это всё было?"
    play music Voyage fadein 3
    play ambience bus_inside volume 0.21 fadein 1
    scene bg int_avtobus2
    show unblink
    "Константин очнулся в автобусе, а дыры в груди как и не бывало."
    kt "Что?"
    liz "Зачем?"
    kt "Я... Я хотел помочь вам всем..."
    kt "А где мы?"
    liz "Не могу тебе сказать."
    play sound2 sfx_mystery_movement volume 1
    show image liz_normal with byso
    "Лиза вышла с водительского места и посмотрела на Константина."
    hide image liz_normal
    show image liz_grin
    with byso
    liz "Хе... Уже не тот Костя, которого я подобрала в прикрытии."
    hide image liz_grin
    show image liz_smile
    with byso
    liz "Ты изменился..."
    kt "Возможно... Вероятно, я стал тем Костей, который был в далёком детстве."
    hide image liz_smile
    show image liz_smile at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Она подошла поближе."
    liz "И это хорошо... Ты наконец-то это понял."
    play sound2 sfx_ikarus_open_doors volume 1
    "Двери автобуса открылись на полном ходу."
    hide image liz_smile
    show image liz_smile
    with byso
    liz "А теперь и мне пора."
    liz "Увидимся."
    hide image liz_smile with byso
    "Она вышла из автобуса и растворилась."
    kt "Меня-то подожди!"
    "Он побежал за ней."
    "Автобус ехал очень быстро и Константин просто боялся выходить наружу."
    show blink
    stop ambience fadeout 3
    stop music fadeout 3
    "Закрыв глаза, он шагнул из автобуса..."
    pause 3
    play sound_loop kardiograf fadein 10
    th "Что...{w=1} Что такое?"
    th "Я выжил?..."
    play music interlude fadein 10
    oleg "Как он?{w=1} Жив?"
    csp "Вроде да. Кто ему так круто оказал первую помощь?"
    liz "Я...{w=1} Не знаю сама, как всё это сделала...{w=1} Я была не в адеквате."
    oleg "Операция прошла успешно?"
    csp "Да. Достаточно.{w=1} Пересадка прошла успешно."
    csp "Скорее всего через день он сможет выйти из комы."
    csp "Вы слишком долго меня искали. Ещё бы буквально час-два и была бы смерть мозга."
    liz "Ну уж прости!{w=1} Мы только убили Генду!{w=1} Мы не могли взять и найти тебя с нихера!"
    oleg "Лиза, не кипятись...{w=1} Всё нормально, все живы."
    csp "Я пойду.{w=1} Не трогайте ничего."
    play sound2 glad volume 1
    "На некоторое время настала тишина.{w} Был слышен лишь писк кардиомонитора.{w=1} Константин почувствовал как чья-то ладонь прошлась по его лицу."
    liz "Эх, дорогой мой....{w=1} Ударила же тебе моча в голову..."
    oleg "Но он герой!{w=1} Он спас Андрея от смерти!"
    "Лиза тяжело вздохнула."
    liz "Да и хрен бы с ним...{w=1} Меня немного другое волнует..."
    scene bg white
    show unblink
    "Константин отрыл глаза.{w=1} Яркий свет бил прямо в лицо, и перед глазами все расплывалось, однако рассмотреть ничего было нельзя."
    oleg "Смотри, он просыпается!"
    liz "Костя!{w=1} Ты проснулся?!"
    scene bg int_hospital
    show image liz_shysurp at cright
    show image oleg_happy at cleft
    with Dissolve(3)
    play sound2 sfx_bed_squeak2 volume 0.31
    "Картинка приобрела чёткие очертания. Он увидел Олега и Лизу, которые стояли над ним, после чего с трудом сел на кушетку."
    kt "Да, я...{w=1} Да.{w=1} Проснулся..."
    oleg "Ребята!{w=1} Он проснулся!"
    hide image liz_shysurp
    show image liz_smile at cright
    with byso
    liz "Дурак!"
    hide image liz_smile
    show image liz_smile at cright:
        zoom 1.5
        yanchor 0.1
    with byso
    "Лиза изо всех сил обняла Константина, отчего у него даже щёлкнул позвоночник."
    liz "А что если бы ты не проснулся?!{w=1} О чём ты думал?!"
    kt "О чём - о чём...{w=1} О людях..."
    liz "Дурачок! Что бы я делала без тебя?!{w=1} О каких таких людях ты думал?!"
    play sound2 sfx_open_door_kick volume 1
    hide image liz_smile
    show image liz_smile at cright
    show image pas_smile at fright
    show image andr_normal3 at fleft
    with byso
    "В палату вбежали Гордон и Андрей."
    pas "Костян!{w=1} Ожил, щит наш живой!"
    hide image andr_normal3
    show image andr_smile at fleft
    with byso
    andr "Ты герой!{w=1} Ты защитил меня от пули!"
    window hide dissolve
    $ set_mode_nvl()
    "Что-ж..."
    "Сам Константин не мог понять, что такое в нём произошло, раз он решился на такой самоотверженный поступок."
    "Заградить своим телом другого человека от пули было чем-то непознаваемым для Константина."
    "Когда он всё же понял, за что и ради чего был тогда сделан этот решительный шаг, он уже начал внутренне раскаиваться."
    "Раскаяние за весь свой жизненный эгоизм, ненависть к людям и другие грехи. За это он был щедро вознаграждён."
    "Теперь он понимает: чтобы жизнь стала такой, какую он выбрал, надо перестать думать о себе, перестать заботиться о собственном удовольствии, сосредоточив все свои усилия на счастье другого."
    "Возможно, его ждало великое будущее на просторах инреальности, а может просто ужасное забвение, но Константин до сих пор не жалеет о своём решении."
    "Он сделал правильный выбор."
    "Только этот выбор не может означать окончательную смерть для себя, ведь теперь он запомнился как герой, верный делу жизни."
    "Тот, кто рискнул собой ради другого, будет жить и после смерти."
    # КАК ЖЕ Я ЗАЕБАЛСЯ ЭТУ ЕБАТОРИЮ ПИСАТЬ, ПРОСТО НЕВЫНОСИМО НАХУЙ! ХУДШИЙ РУТ НАХУЙ, НЕНАВИЖУ ЛИЗУЖЕНЮ КАК ПЕРСОНАЖА БЛЯТЬ!
    # ПИЗДЕЕЕЕЕЕЕЕЕЕЕЕЦ Я СТОЛЬКО РАЗ ХОТЕЛ ЭТУ ХУЯТИНУ ДРОПНУТЬ, НО ДОВОЛОК НАХУЙ, УРА, ПОЙДУ БУХАТЬ
    stop sound_loop fadeout 3
    stop music fadeout 3
    window hide dissolve
    $ set_mode_adv()
    scene bg black with dissolve
    pause 3
    $ unlock_ach_root_inreal(12)
    pause 2
    play music "<from 156>inrealnost/Music/Music/Voyage.mp3" volume 1.5 fadein 3
    scene bg ending_FromTheBottomOfHeart_cg:
        crop (0, 0, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    show ending_FromTheBottomOfHeart:
        crop (0, 0, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    with Dissolve(25)
    scene bg black with byso
    stop music fadeout 3
    pause 2.6
    jump after_ending_screen