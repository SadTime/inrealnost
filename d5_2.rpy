label d5_withmi:
    $ save_name = ('Инреальность.\nSymphony of Evil.')
    play music summerdays fadein 3
    scene bg ext_village
    show shum_white
    with byso
    "Середина июля."
    "Костя гулял по деревне."
    "Было достаточно жарко, воздух пах разнотравьем и озерной сыростью."
    "На встречу ему вышла Маша с букетом васильков в руке."
    ks "О, привет Маш.{w} Не знал что ты приедешь.{w=1} Как твои дела?"
    ma "Приветик.{w=1} Я только из Японии приехала."
    ma "Здесь красиво...{w=1} А ты какими судьбами здесь?{w} Отдыхаешь?"
    ks "Как всегда.{w=1} Каждое лето здесь."
    ma "Ты занят?{w} Если нет, то давай прогуляемся по окрестностям."
    ks "Сейчас не могу, дедушка просил наколоть дров."
    ks "Пойдем, я тебя провожу, нам всё равно в одну сторону."
    "Маша перебрала васильки, понюхала их и свернула букет, после чего пошла в ногу с Костей."
    "Ветер шелестел в листве, было очень приятно идти."
    ma "Я тебе рассказать хотела, как я в музыкальную школу перевелась."
    ks "Даже так?{w} Когда успела?"
    ma "Мама решила, что стоит продвигать моё обучение в музыке."
    ma "Решили что я хочу стать певицей.{w=1} Сказала, для этого мне нужна абсолютная музыкальная эрудиция."
    ks "Классно!"
    "Маша неловко улыбнулась.{w=1} В этой улыбке читалась грусть."
    ks "А ты сама этого хотела?"
    ma "Не знаю...{w=1} Я не особо." 
    ma "Сначала не представляла себя в этом плане." 
    ma "С другой стороны родители сильно за меня старались..."
    stop music fadeout 2
    scene bg black with dissolve
    pause 1
    scene bg int_catacombs_living
    show unblink
    play music god fadein 3
    play ambience ambience_catacombs volume 1 fadein 1
    "Константин очнулся на полу бункера.{w=1} Рядом с ним лежал рюкзак и странное орудие, которое он отобрал у мёртвого сопротивленца."
    th "Чё, где я?"
    scene bg ma_sleep with byso
    "Встав на ноги, он заметил Машу, которая мирно лежала на кровати и спала."
    kt "Маша, просыпайся."
    play sound2 glad volume 1
    "Он подошёл к спящей Маше и потряс её за плечо."
    "Безрезультатно.{w} Она повернулась на другой бок."
    kt "Эй, вставай, уже не смешно..."
    play sound2 glad volume 1
    "Константин повторил своё воздействие.{w} Маша не отреагировала."
    th "Шевелится, но не просыпается..."
    play sound2 sfx_pat_shoulder_hard volume 0.61
    "Он взял её руку, чтоб прощупать пульс."
    "Кисть была холодной, и это казалось странным.{w=1} Пульс был, но настолько слабый, будто она впала в летаргический сон."
    th "Что за муть?...{w=1} Тут есть нашатырь?"
    play sound2 sfx_open_cabinet_1 volume 1
    scene bg int_catacombs_living with byso
    "Константин отошёл от кровати и вскрыл один из шкафчиков."
    "Внутри была белая коробочка с красным крестом."
    play sound2 sfx_lock_close volume 1
    "Открыв её, он обнаружил место, где должен был лежать предмет в виде какой-то ампулы."
    th "Я так понимаю, именно тут должна быть ампула генмода, про которую говорилось в писании..."
    th "Но где?{w=1} Кто её забрал?"
    th "И зачем?..."
    play sound2 sfx_blow_out_candle volume 1
    "Константин отложил находку и продолжил искать нашатырный спирт."
    play sound2 sfx_open_table volume 1
    "Открыв один ящик, он нашёл там стеклянный флакон с раствором аммиака."
    th "Так...{w=1} Нашатырный спирт и есть раствор аммиака..."
    "Найдя тряпочку, он смочил её в полученном растворе."
    scene bg ma_sleep with byso
    "Подойдя к Маше, он помахал тряпкой перед её лицом."
    stop music fadeout 3
    play sound2 sfx_bed_squeak1 volume 1
    scene bg int_catacombs_living
    show mi shocked pioneer
    with byso
    "Едкий запах быстро сделал своё дело.{w=1} Маша вскочила с кровати."
    kt "Проснулась.{w=1} Неужели."
    show mi sad pioneer with byso
    ma "Костя, пионер..."
    play music lim fadein 3
    ma "Он отказался с нами работать!"
    kt "Что?{w=1} Почему?"
    play sound2 sfx_bed_squeak1 volume 1
    show mi upset pioneer with byso
    "Она села на кровать и поправила складки на юбке.{w=1} Константин сел рядом."
    ma "Он мне предлагал такое..."
    kt "А именно?"
    show mi sad pioneer with byso
    "Маша прикрыла рот, словно боясь произнести одно неосторожное слово."
    ma "Костя, он предложил мне тебя предать и обманом завладеть...{w=1} правами административными..."
    kt "Но зачем?{w} Ради какой такой великой цели?"
    ma "Я...{w=1} я не знаю"
    "Константин уставился в пол, не находя слов для ответа."
    kt "Так он теперь не будет нам помогать?"
    ma "Да...{w=1} Он сказал, что найдёт кого-то более сговорчивого...{w=1} И будет нашим врагом."
    kt "Подожди, а что за права?{w} Разве мы их получим?"
    "Маша опять прикрылась ладонью.{w=1} Голос её стал встревоженным: кажется, она волновалась."
    ma "Он попытался мне это объяснить...{w=1} Якобы права бога этой вселенной."
    kt "Как у Генды?"
    ma "Да...{w=1} Как у него..."
    "Константин задумался.{w=1} Потом медленно поднял на Машу глаза."
    "Он нервно почесал щеку и ухмыльнулся."
    show mi upset pioneer with byso
    "Маша заметила, как исказилось от напряжения его лицо.{w=1} В его глазах плескалась нерешимость."
    kt "Какой бред!{w=1} Парень хотел, что бы мы пошли и свергли Генду с его божественного трона?{w} Как?"
    ma "Пионер говорил, что сопротивление имеет какой-то код для этого...{w=1} На флешке."
    kt "Флешка?{w=1} Вообще бредятина! {w}Что мы с ней делать должны?"
    show mi sad pioneer with byso
    ma "Про это он тоже упомянул.{w=1} Какая-то административная симуляция..."
    "На его лице снова образовалась улыбка, отражавшая полное непонимание происходящего."
    kt "И от кого нам теперь всё это узнавать?"
    ma "Не знаю...{w=1} Да и что нам теперь делать?"
    show mi serious pioneer with byso
    "Константин глубоко задумался, но мозг отказывался выдавать хоть какие-либо осмысленные идеи.{w=1} Машин взгляд заставил его отвлечься."
    kt "Я думаю, нам нужно уходить отсюда."
    show mi upset pioneer with byso
    ma "Куда?"
    kt "Искать нового информатора.{w=1} Я вообще ничего не понимаю."
    show mi dontlike pioneer with byso
    ma "Ты думаешь, что они на дороге валяются?"
    "Он встал со стула и посмотрел на радиоустановку."
    kt "Нет, но если мы вообще искать не будем, то точно не найдём."
    kt "Я вот думаю..."
    show mi upset pioneer with byso
    ma "А если мы найдём ещё одного такого пионера?"
    play sound2 sfx_mystery_movement volume 1
    "Константин сел за установку, после чего начал разбиваться в её конструкции."
    show mi serious pioneer with byso
    "Маша молча наблюдала за этим и только через несколько секунд поняла, что Константин собрался сделать."
    kt "Нам не нужен тот, кто проведёт нас хрен знает куда, нам нужен тот, кто всё понимает и даст это понимание нам."
    show mi upset pioneer with byso
    ma "Ты хочешь воспользоваться станцией?"
    kt "Ну да, я не вижу другого варианта.{w=1} Лично искать мы не сможем."
    play sound2 sfx_click_1 volume 1
    "Он включил на радио автопоиск."
    show mi angry pioneer with byso
    ma "Но это же как знакомства в интернете!{w} Мы не понимаем, кого найдём."
    kt "Опять таки, это лучше чем ничего."
    play sound2 sfx_radio_squelch_1 volume 1
    "Автопоиск нашёл действующий канал связи."
    vng2 "...мы устранили ту симуляцию."
    vng "Отлично. Возвращайтесь на базу.{w=1} Конец связи."
    play sound2 sfx_radio_squelch_2 volume 1
    "Радио зашипело и снова включился автопоиск."
    kt "Мхм...{w=1} Те сопротивленцы?"
    show mi upset pioneer with byso
    ma "Может и так, но что нам с того?"
    kt "Верно...{w=1} Смотрим дальше."
    "Автопоиск на радио явно не торопился с ответом."
    "Звуки радио только подчёркивали мрачную атмосферу бункера."
    "Где-то капала труба, иногда раздавались звуки падения камней из-за малой двери."
    "Насколько улавливал взгляд и слух, вокруг не было ни одной живой души. Только из динамика звучал монотонный и унылый треск."
    play sound2 sfx_radio_squelch_1 volume 1
    show mi serious pioneer with byso
    "Наконец, поиск остановился на 148й частоте."
    kt "Да неужели..."
    "Пробормотал Константин и вслушался."
    play sound2 sfx_blow_out_candle volume 1
    pause 0.1
    play sound sfx_click_1 volume 1
    "Радио молчало.{w=1} Он нажал кнопку и подтянул к себе микрофон."
    kt "Есть кто в эфире, приём."
    show mi sad pioneer with byso
    ma "Костя, зачем ты?..."
    vng3 "Неужели!{w=1} Тут есть люди!"
    show mi upset pioneer with byso
    kt "Есть. {w=1}С кем имею честь?{w=1} Приём."
    vng3 "Нет времени объяснять!{w} Если вы меня слышите, то вы должны мне помочь! Как слышите?!"
    "Константину не понравился такой обязывающий тон собеседника."
    kt "Схерали?{w=1} Ты вообще кто?"
    vng3 "У меня важная информация, которую надо срочно донести до капитана!"
    kt "Какого капитана, что ты несёшь?"
    "Голос промолчал.{w=1} Маша недовольно нахмурилась и отвела взгляд от станции."
    vng3 "Ты не из сопротивления?"
    kt "Мы нет, а ты, так понимаю, да."
    vng3 "Я исследователь.{w=1} Батори уничтожила мой отряд и я оказался отрезан."
    vng3 "Ах да... Батори...{w=1} Рыжая девочка из <<Цены грехов>>."
    vng3 "Давайте так, я помогаю вам, а вы мне.{w=1} Что вы хотите?"
    "Константин задумался."
    kt "Нам нужна информация об этом месте.{w=1} Если ты дашь нам понимание происходящего, то мы будем готовы помочь."
    vng3 "Хорошо, мы договорились."
    vng3 "Если мы можем общаться, то ты скорее всего находишься в моём секторе.{w} Моя симуляция отрезана от общего вещания по непонятным причинам."
    vng3 "На радио есть маркировка.{w=1} На задней панели. {w}Назовите мне последние 6 цифр из 4ой строки."
    play sound2 sfx_wood_floor_squeak volume 1
    "Константин развернул станцию и нашёл бумажку, на которой было 8 строчек."
    "На 4ой был указан номер <<УРВ-а10121675134>>."
    kt "675134."
    "Собеседник замолчал.{w=1} Маша перевела взгляд на Константина."
    show mi sad pioneer with byso
    ma "Мы же не пойдём к нему?{w} Он странный."
    kt "У тебя есть варианты получше?"
    show mi upset pioneer with byso
    "В ответ она отрицательно помотала головой и снова посмотрела на радио."
    vng3 "Соседняя симуляция.{w=1} Чтобы попасть ко мне, вы должны пройти через левый портал.{w} Как понял?"
    kt "Понял.{w=1} А как эти порталы найти?"
    vng3 "Обнулить стабильность.{w=1} Стабильность вашей симуляции сама скоро...{w=0.75}{nw}"
    stop music fadeout 0.5
    play sound2 pum volume 1
    show mi scared pioneer
    scene bg black with flash
    play music rutine fadein 3
    "В один момент свет в комнате погас."
    "Маша испугалась и вскрикнула, а Константин рефлекторно нахмурился."
    ma "Что происходит?!"
    play sound2 sfx_bed_squeak2 volume 1
    "Раздался скрип кровати."
    kt "Маша, сиди..."
    play sound sfx_punch_medium volume 1
    pause 0.1
    play sound2 sfx_bodyfall_1 volume 1
    ma "Ай!" with vpunch
    "Она, судя по звукам, упала на пол."
    scene bg int_catacombs_living_red
    show mi sad pioneer
    with byso
    "В бункере загорелось красное аварийное освещение.{w=1} Константин подбежал к Маше и помог встать."
    kt "Что-ж ты встаёшь в темноте так резко?"
    ma "Прости, я просто испугалась..."
    "Константин вернулся к радио."
    play sound2 sfx_radio_squelch_1 volume 1
    "Вдруг, зазвучал голос."
    gt2 "Системное вмешательство!{w=1} Коммуникация невозможна!"
    play sound_loop white_noise volume 1
    "После этого из радио начал доноситься белый шум.{w=1} Было похоже, что его источник то отдалялся - то приближался вновь.{w=1} Однако звук делался все отчетливей и четче - усиливался."
    kt "Что за фокусы?"
    show mi upset pioneer with byso
    ma "Да откуда нам знать?..."
    "Отойдя от радио, Константин посмотрел на Машу."
    kt "Собираем манатки.{w=1} Нам надо уходить."
    show mi serious pioneer with byso
    ma "Хорошо."
    play sound2 sfx_put_sugar_cart volume 1
    "Маша взяла рюкзак, а Константин подобрал оружие, которое получил от мёртвого сопротивленца."
    "За лямку он повесил орудие себе на плечо и махнул рукой на выход."
    kt "Двинули."
    stop music fadeout 1
    play sound2 sfx_carousel_squeak volume 1
    show mi shocked pioneer with byso
    "Только они пошли к выходу, дверь заскрипела и открылась."
    play music Waijdan fadein 1
    show image ub_angry at left with byso
    "На пороге нарисовалась странная девушка, похожая на Лену, выстриженную под каре."
    "Единственными отличиями её от таковой были красные глаза, которые, казалось, светятся в темноте и перекошенная улыбка, статично стоящая на лице."
    "Рука Константина уже обособленно потянулась к оружию."
    hide image ub_angry
    show image ub_normal at left
    with byso
    ubp "Опачки, а чего мы тут забыли, крендельки?"
    "Маша явно не торопилась отвечать.{w=1} Константин медленно убрал руку с оружия и посмотрел девочке в глаза."
    kt "Проездом. Конкретно тут мы ничего не забыли."
    hide image ub_normal
    show image ub_angry at left
    with byso
    ubp "Угу, а чё мы сделали с радио?"
    show mi sad pioneer with byso
    ma "С-свет выключился и...{w=1} Вот..."
    ubp "А когда боишься, ты менее разговорчива, Мику."
    kt "Это не Мику.{w=1} Она путница."
    hide image ub_angry
    show image ub_normal at left
    with byso
    ubp "Да чё вы все заладили, Мику есть Мику..."
    show mi angry pioneer with byso
    kt "Тогда, выходит, ты Лена?"
    "Девочка размяла пальцы и поправила хвостики."
    hide image ub_normal
    show image ub_angry at left
    with byso
    ubp "Нет.{w=1} Меня Катя зовут."
    th "Л-Логика."
    kt "Ясно."
    show mi upset pioneer with byso
    ma "Ну мы это...{w=1} Пойдём?"
    hide image ub_angry
    show image ub_normal at left
    with byso
    ub "Куда это мы хотим?"
    kt "На поверхность."
    "Катя насмешливо прошипела и указала на выход."
    ub "Ну пошли."
    kt "Мы бы сами пошли..."
    hide image ub_normal
    show image ub_angry at left
    show mi scared pioneer
    with byso
    "На такое она скрипнула зубами и повернулась к Константину."
    ub "Как это так?{w=1} Только познакомились и уже расходимся?{w} Не-ет, нет."
    ub "Я вас провожу."
    "Константин искоса глянул на Машу и приподнял бровь."
    show mi sad pioneer with byso
    kt "Ну пошли."
    stop sound_loop fadeout 1
    scene bg int_catacombs_door with byso
    show image ub_angry at left with byso
    show mi sad pioneer at right with byso
    "Катя вышла из бункера с фонариком и встала у дверей."
    "Маша и Константин, сами того не хотя, пошли вперёд."
    hide image ub_normal
    show image ub_angry at left
    with byso
    ub "И как это вас ко мне занесло?"
    kt "Наша симуляция рухнула, вот мы и сбежали оттуда."
    "Пояснил Константин, стараясь не выпускать Катю из виду."
    scene bg int_catacombs_entrance
    show image ub_angry at left
    show mi sad pioneer at right
    with byso
    "Константин чувствовал подвох, потому старался следить за её действиями."
    hide image ub_angry
    show image ub_normal at left
    with byso
    ub "Очень интересно...{w} А что у тебя делает оружие сопротивления?"
    kt "Подобрал."
    ub "Убил сопротивленца, да?"
    ma "Нет, они на нас напали и робот его убил."
    hide image ub_normal
    show image ub_angry at left
    show mi shocked pioneer
    with byso
    ub "А я и не тебя спрашиваю."
    play sound glad
    "Раздражённо протянула Катя, гладя себя по предплечью."
    hide image ub_angry
    show image ub_normal at left
    with byso
    ub "Уже дня два ко мне никто из других симуляций не приходил..."
    ub "И тут вы."
    kt "Уж прости, выбора у нас особого не было."
    "Катя заглянула Константину в душу.{w} В её взгляде читалось нечто ужасное и необъяснимое."
    "Как будто она прочла все его мысли и знала то, чего он сам даже не подозревал."
    ub "Ничего страшного, даже самый оплошный поступок можно замолить."
    "Протянула она, переведя взгляд на Машу."
    show mi sad pioneer at right with byso
    "Маша не выдержала напора и отвела взгляд в сторону.{w=1} Судя по всему, она не была готова к такому суровому испытанию."
    hide image ub_normal
    show image ub_angry at left
    with byso
    ub "Поднимайтесь."
    "Приказала Катя, указав на лестницу."
    th "Делать нечего..."
    scene bg int_old_building1
    show image ub_angry at left
    show mi sad pioneer at right
    with byso
    play sound2 sfx_open_metal_hatch volume 1
    play ambience ambience_forest_night volume 0.61 fadein 1
    scene bg int_old_building2
    show image ub_angry at left
    show mi sad pioneer at right
    with bso
    scene bg int_old_building1
    show image ub_angry at left
    show mi sad pioneer at right
    with bso
    "Поднявшись вверх, они оказались в старом корпусе.{w=1} На улице трещали сверчки."
    "Как только Маша поднялась, Катя закрыла люк и снова указала на выход."
    hide image ub_angry
    show image ub_normal at left
    with byso
    ub "А вы слышали про Батори?"
    kt "Приходилось.{w} И что?"
    ub "Что думаете?"
    show mi upset pioneer at right with byso
    ma "Больная она... "
    "Катя ухмыльнулась и перевела взгляд на Константина."
    ub "А ты как думаешь, а?"
    scene bg ext_old_building_red
    show image ub_normal at left
    show mi shocked pioneer at right
    with byso
    play ambience ambience_forest_night volume 1 fadein 1
    "Небо на улице было красным.{w=1} Это казалось очень странным, потому что оно никогда не бывало таким."
    kt "Я не знаю.{w=1} Мы не много о ней слышали."
    scene bg ext_path2_night_red
    show image ub_normal at left
    show mi upset pioneer at right
    with byso
    ma "А почему...{w=0.41}{nw}"
    hide image ub_normal
    show image ub_angry at left
    show mi shocked pioneer at right
    with vpunch
    ub "Я тебе не давала право перебивать меня!{w=1} Понятно, да?!"
    th "Знакомое выражение...{w=1} Даже очень..."
    kt "Слушай, ты, давай без хамства!"
    play sound2 sfx_blow_out_candle volume 1
    stop music fadeout 3
    hide image ub_angry
    show image ub_normal at left
    with byso
    "Она едва слышно усмехнулась и протянула руку за пазуху."
    ub "А то что?!"
    kt "Мы тебе не хамим - ты тоже не хами.{w=1} Базовое правило вежливости!"
    ub "Вежливость?"
    play music "<from 45>inrealnost/Music/Music/deadrazy4.mp3" fadein 3
    show mi scared pioneer at right with byso
    "Катя рассмеялась и вытащила из-за пазухи армейский нож."
    "Нож не новый, но совершенно исправный – лезвие с зазубринами, металлическое, заточенное с обеих сторон."
    ub "Узнаю тебя... Константин Брусков."
    kt "Чё? Откуда ты меня знаешь?"
    "Маша начала отстраняться от безумной девицы, а Константин потянулся к оружию."
    ub "А это уже не важно..."
    ub "Трупу эта информация ни к чему!"
    play sound2 sfx_armature_swish volume 1
    hide image ub_normal
    show image ub_angry at left:
        zoom 1.25
        yanchor 0.1
    with vpunch
    stop sound2
    "Она бросилась на Константина, словно пытаясь его проткнуть."
    hide image ub_angry
    show image ub_normal at left
    show mi scared pioneer far at right
    with byso
    "Еле-еле Константину удалось увернуться.{w=1} Маша отбежала и начала рыться в рюкзаке."
    play sound2 sfx_click_1 volume 1
    "Он взял в руки орудие и прицелился в Катю и нажал на спусковой крючок."
    play sound2 sfx_click_3 volume 1
    play sound sms volume 1
    "Ничего не произошло. {w=1}Орудие щёлкнуло и пиликнуло."
    ub "Ха! Не бери орудие, если не знаешь, как им пользоваться!"
    hide image ub_normal
    show image ub_angry at left:
        zoom 1.25
        yanchor 0.1
    with vpunch
    play sound2 sfx_armature_swish volume 1
    "Катя совершила пару режущих ударов, задев рубашку Константина."
    "Рубашка разошлась и оголила тело, до которого дотянуться ей не удалось."
    ub "Вот изворотливый!"
    $ renpy.block_rollback()
    $ time = 20000
    $ timer_range = 20000
    $ timer_jump = 'fduiosfjnsduiojuigjfdngidf'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Ударить прикладом.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            "Константин перехватил орудие и замахнулся."
            play sound2 sfx_punch_washstand volume 1
            hide mi
            hide image ub_angry
            with vpunch
            play sound knife_in volume 1
            show image blood2 with byso
            "Удар."
            "Он отшатнул нападающую на метр, но почувствовал сильную боль в груди."
            ub "Изворотливый, но недостаточно."
            "У Константина в груди был нож, вошедший в сердце во всю длину."
            scene bg black with byso
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            "Он перестал чувствовать сердцебиение."
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
        "Бежать.":
            $ renpy.block_rollback()
            stop sound3 fadeout 1
            jump bfguidhsbvhfu8dshbvsfu8i9hbu9fhb9us
        "Попросить помощи у Маши.":
            $ renpy.block_rollback()
            stop sound3 fadeout 1
            hide screen inreal_countdown
            play sound2 knife_in volume 1
            hide mi
            hide image ub_angry
            show image ub_angry at center:
                zoom 1.5
                yanchor 0.1
            show image blood2
            with vpunch
            "Только Константин отвлёкся, как получил меткий удар в центр груди."
            ub "Вот и всё."
            play sound2 sfx_bones_breaking volume 1
            show image blood1 with byso
            "С хрустом она провернула лезвие в его груди."
            "Судя по всему, сердце было пробито."
            ma "Костя! {w=1}Нет!"
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
label fduiosfjnsduiojuigjfdngidf:
    stop sound3 fadeout 1
    $ renpy.block_rollback()
    hide screen inreal_countdown
    play sound2 knife_in volume 1
    hide mi
    hide image ub_angry
    show image ub_angry at center:
        zoom 1.5
        yanchor 0.1
    show image blood2
    with vpunch
    "Константин получил меткий удар в центр груди."
    ub "Вот и всё."
    play sound2 sfx_bones_breaking volume 1
    show image blood1 with byso
    "С хрустом она провернула лезвие в его груди."
    "Судя по всему, сердце было пробито."
    ma "Костя! {w=1}Нет!"
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
label bfguidhsbvhfu8dshbvsfu8i9hbu9fhb9us:
    hide screen inreal_countdown
    kt "Маша, бежим!"
    hide mi
    hide image ub_angry
    with byso
    "Маша и Константин подорвались с места, пытаясь оторваться от Кати."
    ub "Вот те раз, трупы разбегались."
    ma "Выкуси, маньячка!"
    "Они бежали в сторону площади, а Константин пытался разобраться, как стреляет оружие."
    play sound2 sfx_click_1 volume 1
    "На экранчике светилось сообщение: <<Снимите предохранитель>>."
    play sound2 sfx_click_2 volume 1
    play sound sms volume 0.1
    "Нажав одну из кнопок, Константин услышал звуковой сигнал."
    play sound3 sfx_lena_hits_alisa volume 1
    "На бегу Константин споткнулся и упал."
    ma "Костя!"
    show image ub_angry at center:
        zoom 1.5
        yanchor 0.1
    with vpunch
    "Катя прыгнула на него и вознесла нож."
    window hide
    $ renpy.block_rollback()
    $ time = 15000
    $ timer_range = 15000
    $ timer_jump = 'ujidgjiodfbjiogdfjiofgjiodfgjiofgko'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Ударить по лицу.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            play sound2 sfx_punch_washstand volume 1
            hide image ub_angry with vpunch
            "Константин совершил мощный удар по её лицу, чем дезориентировал нападающую."
            jump nuisbhbgtuifshvuifjsvbuisfjjiovbjfdjidbf
        "Прикрыться орудием.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            "Константин закрыл свою грудь орудием."
            ub "Не угадал!"
            play sound2 knife_in volume 1
            show image blood3 with vpunch
            "Нож вошёл Константину в горло."
            play sound2 knife2 volume 1
            show image blood1 with byso
            "От поперечного пореза его кровь хлынула фонтаном."
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
label ujidgjiodfbjiogdfjiofgjiodfgjiofgko:
    play sound2 knife_in volume 1
    $ renpy.block_rollback()
    stop sound3 fadeout 1
    show image blood3 with vpunch
    "Нож вошёл Константину в горло."
    play sound2 knife2 volume 1
    show image blood1 with byso
    "От поперечного пореза его кровь хлынула фонтаном."
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
label nuisbhbgtuifshvuifjsvbuisfjjiovbjfdjidbf:
    play sound2 sfx_lena_hits_alisa volume 1
    "В этот же момент подбежала Маша и футбольным ударом сбила Катю с Константина."
    ub "Мра-азь!"
    "Проревела Катя, пока Константин встал на ноги и с Машей побежал дальше."
    scene bg ext_square_night_red
    show mi scared pioneer
    with byso
    "На площади было 3 портала.{w} Константин и Маша направились к левому."
    show image ub_angry at fleft with byso
    "Из леса вышла яростная Катя."
    ub "Я с вас шкуру сдеру!!!"
    "Крикнула она и бросилась на Константина."
    stop music fadeout 3
    play sound2 magic volume 1
    hide image ub_angry
    show mi shocked pioneer
    with vpunch
    "Выстрел."
    play sound2 sfx_bush_body_fall volume 1
    "Константин поразил Катю метким выстрелом в тело, от чего та, словно снежный ком, повалилась на землю."
    "Судя по всему, она либо потеряла сознание, либо умерла, но на её теле не было явных повреждений."
    kt "А ты мне гнала, что не умею пользоваться! Лови заряд."
    play music stresss fadein 1
    kt "Маш, дай мне скальпель."
    show mi scared pioneer with byso
    "На её лице снова образовался ужас."
    ma "Что?!{w} Зачем?!"
    kt "Если мы оставим её в живых, то она, вероятно, нас найдёт."
    show mi rage pioneer with byso
    ma "Это убийство!"
    play sound2 sfx_pat_shoulder_hard volume 1
    show mi scared pioneer close with byso
    "Константин взял Машу за плечи."
    kt "Она нас сама в салат хотела покрошить.{w=1} Нельзя просто так оставлять её."
    ma "Но..."
    kt "Нет, прости, но я должен это сделать."
if miscore == 13:
    play sound2 sfx_put_sugar_cart volume 1
    stop music fadeout 3
    show mi sad pioneer close with byso
    "Маша тяжело вздохнула и медленно начала снимать рюкзак с плеча."
    ma "Мы же сделаем правильно, да?..."
    kt "Ради нашего будущего."
    play sound2 sfx_unzip_sleepbag volume 1
    pause 1
    stop sound2
    "Она протянула рюкзак Константину."
    play sound2 glad volume 1
    play music paralysis fadein 3
    "Константин достал из рюкзака скальпель и засмотрелся на его лезвие."
    "Он чувствовал, что на душе у него как-то смутно, но все же испытывал сейчас что-то похожее на радость облегчения."
    ma "Только сделай это быстро...{w=1} Чтобы она не мучилась..."
    hide mi with byso
    "Маша осталась позади и отвернулась к порталу."
    show image ub_angry at center:
        zoom 1.5
        yanchor 0.1
    with byso
    "Он же, со скальпелем в руке, сел рядом с Катей."
    ub "Что...{w=1} Не могу пошевелиться..."
    ub "Что ты делаешь?..."
    "Константин вознёс скальпель у её шеи, словно прицеливаясь."
    kt "Я?{w=1} Делаю так, чтобы не получить нож в спину."
    ub "Не смей..."
    play sound2 sfx_punch_medium volume 1
    "Он зафиксировал голову Кати у земли и готовился нанести продольный удар по всей шее."
    ub "Урод..."
    kt "Прости, подруга, но ты первая начала."
    play sound2 knife3 volume 1
    scene bg bloody_mess with fl_scare
    "Скальпелем Константин нанёс глубокий порез на её шее."
    play sound knife2 volume 1
    "Попытки Кати закричать оказались безуспешны, поскольку кровь залила рот."
    play sound3 sfx_mystery_movement volume 1
    "Её глаза закатились, и она начала издавать что-то похожее на мычание, переходящее в стон."
    "Вскоре её глаза закрылись совсем, а тело обмякло."
    "Всё произошло быстро.{w=1} Во всяком случае, для Константина."
    scene bg ext_square_night_red with byso
    "Константин оставил окровавленный скальпель и встал в полный рост."
    show mi sad pioneer with byso
    kt "Всё, пошли отсюда к чертям..."
    ma "Д-да...{w=1} П-пошли..."
    scene bg black with byso
    stop music fadeout 1
    stop ambience fadeout 1
    "Промямлила Маша и с Константином вошла в портал."
    jump guifhnsduihnfsigbnfsinvgbsdazegf
else:
    play sound pum volume 1
    stop music fadeout 1
    show mi rage pioneer with vpunch
    ma "Нет!"
    play music regret fadein 3
    play sound2 sfx_punch_medium volume 1
    "Крикнула Маша и топнула ногой."
    ma "Если каждый будет друг другу мстить, то людей в этом мире вовсе не останется!"
    "Она схватила Константина за руку и повела в портал."
    kt "Но она может нас убить!"
    ma "Если ты проявишь милосердие, то только тогда другие проявят милосердие к тебе!"
    play sound2 portal volume 1
    stop music fadeout 1
    scene bg black with byso
    stop ambience fadeout 1
    "Она взяла его за руку и затянула в нужный портал."
    jump guifhnsduihnfsigbnfsinvgbsdazegf
label guifhnsduihnfsigbnfsinvgbsdazegf:
    play music summerdays fadein 3
    scene bg ext_village
    show shum_white
    with byso
    ma "Столько сил ушло...{w=1} Родители платили преподавателям, я ходила на занятия и развивала свои умения."
    ma "Возможно, в будущем я буду участвовать в самом настоящем оркестре..."
    ks "Да, это круто..."
    "Маша улыбнулась и посмотрела в небо."
    ma "Агась...{w=1} Папа говорил, что у меня талант в музыке."
    ma "Я умею играть на множестве самых разных инструментов."
    ks "Ты так мне ни разу и не показывала..."
    ma "Покажу...{w=1} Приходи ко мне, после того как дедушке поможешь и я сыграю тебе на балалайке."
    "Костя ухмыльнулся и почесал затылок."
    ks "Да ладно тебе, не стоит так из-за меня напрягаться."
    ma "А мне вовсе и не сложно.{w=1} Приходи, послушаешь."
    ks "Приду."
    "Ответил Костя и посмотрел Маше в глаза."
    "Она не отвела взгляда, и ему показалось, что она совершенно точно знает, какие мысли проносились у него в голове."
    ks "Слушай, всегда было интересно, а у тебя есть друзья в Японии?"
    "Маша опустила взгляд и всмотрелась в траву у них под ногами."
    ma "Нет.{w=1} Есть только одна подруга..."
    ks "Почему?{w=1} Ты же такая интересная девочка!"
    ma "Только ты так думаешь.{w} Остальные меня презирают."
    ks "За что?{w=1} Ты сделала им что-то плохое?"
    ma "Нет...{w=1} Точнее, да.{w} Им не нравится, что я наполовину русская, а на половину японка..."
    stop music fadeout 2
    scene bg black with dissolve
    pause 1
    play ambience ambience_int_cabin_day volume 1 fadein 1
    scene bg int_house_of_kt_day
    show unblink
    play music BlueJetta fadein 3
    "Константин и Маша очнулись в пустом домике, лежащими на разных кроватях."
    play sound2 sms volume 0.41
    pause 0.5
    play sound sms volume 0.41
    "Орудие несколько раз пикнуло и замолчало."
    "Практически синхронно они встали и, сев на кровати, переглянулись."
    show mi sad pioneer with byso
    ma "Это было...{w=1} Ужасно..."
    "Константин посмотрел на орудие.{w=1} На экране была выведена надпись <<Зарядите накопитель!>>."
    play sound2 sfx_blow_out_candle volume 1
    "Отложив орудие на стол, он достал сигарету и вставил в зубы."
    kt "Не спорю...{w} Ещё и пушка, судя по всему пришла в негодность..."
    play sound2 light_inh volume 1
    "Чиркнув зажигалкой, он втянул в себя едкий дым."
    ma "Почему она на нас напала?{w} Какие цели она преследовала?"
    kt "Не знаю...{w=1} Что меня больше волнует - так откуда она меня знает?"
    show mi upset pioneer with byso
    ma "Ты не помнишь никого, кого звали Катей?"
    "Константин на несколько секунд задумался, вращая тлеющую сигарету в руке."
    kt "Были одноклассницы...{w=1} Но вряд-ли им было за что меня убить."
    kt "Хоть в школе они надо мной и издевались, но это скорее были попытки на ком-то выпускать пар."
    kt "Так что я до сих пор не могу понять, какой Кате я мог так насолить..."
    kt "Вопрос у меня есть другой...{w} Как мы можем найти нашего нового информатора?"
    show mi sad pioneer with byso
    "Маша уныло поправила волосы и покачала головой."
    ma "Я не знаю...{w=1} Он даже не сказал, как он выглядит."
    play sound2 sfx_dinner_horn_processed volume 1
    "На улице заиграл горн.{w} Судя по заходящему солнцу, на ужин."
    play sound3 sfx_bed_squeak2 volume 1
    pause 0.5
    play sound sfx_put_sugar_cart volume 1
    "Константин неторопясь встал с кровати и взял рюкзак, после чего указал на выход."
    kt "Ну, что делать, пошли позавтракаем."
    ma "Не знаю как у тебя, но у меня нет совершенно никакого аппетита..."
    kt "Надо поесть.{w=1} Именно надо.{w} Может быть, это вообще наш последний приём пищи на ближайшие несколько дней."
    show mi upset pioneer with byso
    play sound2 sfx_bed_squeak1 volume 1
    "Она неловко почесала затылок и встала с кровати."
    ma "Что поделать...{w=1} Пошли..."
    kt "Сама говорила, лысина будет."
    play sound2 sfx_punch_medium volume 0.41
    show mi angry pioneer with byso
    "Маша недовольно вздохнула и ткнула Константина пальцем в бок."
    ma "Прошла тысяча сожалений с того момента, как я это сказала..."
    play ambience ambience_camp_entrance_day volume 1 fadein 1
    play sound2 sfx_close_door_1 volume 1
    scene bg ext_houses_day with byso
    show mi upset pioneer with byso
    "Выйдя из домика, Константин выбросил сигарету и пытался примерно понять своё положение в лагере."
    ma "Мы во втором корпусе.{w=1} Столовая там."
    "Указала Маша и пошла с Константином."
    kt "И как нам найти информатора?..."
    ma "Не знаю...{w} Мы это не обсудили."
    kt "Чёрт с ним.{w=1} Найдётся."
    scene bg ext_square_day
    show mi upset pioneer at right
    show sl surprise pioneer at fleft
    show image me_no at left
    with byso
    "На площади они встретили Славю и Семёна, которые шли в неизвестном направлении."
    hide image me_no
    hide sl
    hide mi
    show mi upset pioneer
    with byso
    "Заметив Константина и Машу, девочка изрядно удивилась и хотела было подойти, но Семён отвлёк её разговором."
    th "Хм...{w=1} А что если тут будет две Мику?{w} Как на это отреагируют люди?"
    th "Ведь два абсолютно идентичных человека - тема странная..."
    th "Надеюсь, в этой симуляции обойдётся без психов..."
    stop music fadeout 1
    scene bg ext_dining_hall_near_day
    show mi serious pioneer at right
    show mt sad pioneer far at left
    with byso
    "У столовой они заметили вожатую, которая была чем-то озадачена."
    play sound2 sfx_pat_shoulder_hard volume 1
    play music god fadein 3
    hide mt
    show mi shocked pioneer
    show mt surprise pioneer
    with byso
    "Заметив Машу, она подошла поближе и схватила её за плечи."
    mt "Мику! {w=1}Где ты была?!{w=1} Мы тебя искали всем лагерем!"
    th "М-м..."
    ma "Что?..."
    mt "С тобой всё хорошо?"
    ma "Да...{w=1} Я вроде никуда не терялась..."
    hide mt
    show mi upset pioneer
    show mt sad pioneer at left
    with byso
    "Ольга отпустила её и тяжело вздохнула."
    mt "Ты ничего не помнишь?...{w=1} Но может ты помнишь, куда делась Алиса?{w=1} Или Шурик?{w=1} Или Ульяна?"
    th "Ещё лучше...{w=1} Куда это все так коллективно собрались пропасть? Надеюсь, это не из-за нашего информатора."
    ma "Я не знаю...{w=1} О чём вы вообще?"
    mt "Как это?{w} Мне говорили, что вы с Алисой куда-то ушли и не вернулись!"
    show mi dontlike pioneer with byso
    ma "Не было такого!"
    "Сахарова снова вздохнула и покачала головой."
    mt "Зайди потом к Виоле...{w=1} Может она тебе поможет."
    hide mi
    hide mt
    show mi upset pioneer
    with byso
    "После этих слов вожатая ушла в лагерь, а Константин и Маша переглянулись."
    kt "Это что было?"
    show mi sad pioneer with byso
    ma "Да чтоб я знала...{w=1} Тут ещё и люди пропадают."
    play sound2 glad volume 1
    "Маша напряжённо потёрла свой локоть."
    ma "А вдруг это та девочка из книжки?"
    "Константин пожал плечами и указал на вход в столовую."
    kt "Мне кажется, что если бы это была она, то нас бы уже не было в живых."
    play ambience ambience_dining_hall_full volume 1 fadein 1
    scene bg int_dining_hall_people_sunset_cust with byso
    "В столовой всё было весьма обыденно.{w} Пионеры ели гречневую кашу с говядиной и вели длинные, бессмысленные разговоры."
    show mi upset pioneer at right
    show image pov_smile at left
    with byso
    pov "О, Мику.{w=1} Нашлась."
    show mi angry pioneer with byso
    ma "Да я и не пропадала!"
    hide image pov_smile
    show image pov_sad at left
    with byso
    "Повариха подняла бровь и почесала затылок."
    pov "Ну ладно, как скажешь..."
    hide image pov_sad
    hide mi
    with byso
    show mi upset pioneer
    with byso
    "Получив еду и компот, они направились за столик."
    "Усевшись за единственный свободный столик, они переглянулись."
    ma "Странно всё это..."
    kt "Не поспорю...{w} Вообще ничего не понятно."
    kt "Приятного аппетита."
    show mi sad pioneer with byso
    "Маша неуверенно кивнула и начала водить вилкой по тарелке."
    ma "Может в этом лагере обитают монстры?"
    stop music fadeout 1
    "Константин хмыкнул и улыбнулся."
    kt "Если не брать меня, то не обитают."
    show mi dontlike pioneer with byso
    ma "Шутник блин...{w=1} Носа красного не хватает."
    kt "Может быть, тут были ребята из сопротивления."
    show mi upset pioneer with byso
    ma "Да? Почему тогда они не сделали всё как и в нашем лагере?"
    kt "Чёрт их знает...{w=1} Так и не скажешь, что у них на уме..."
    play sound2 dvizh volume 1
    play music Aleph fadein 3
    hide mi
    show sh normal pioneer at right
    show mi shocked pioneer at left
    with byso
    "Неожиданно для обоих, к ним подсел Шурик."
    sh "Приятного аппетита."
    ma "Что?{w=1} Ты же тоже пропал!"
    "Константин поднял бровь и осмотрел парня.{w} Он ничем не отличался от Шурика из их симуляции кроме иной постановки речи."
    show sh serious pioneer at right with byso
    sh "Кто вам это сказал?"
    kt "Кто-кто. {w=1}Вожатая."
    show sh upset pioneer at right with byso
    "Шурик поправил очки и посмотрел на часы."
    sh "Так, я же с вами выходил на связь?"
    kt "Да...{w=1} Так ты и есть тот парень?"
    "Кибернетик отпил компота и сложил руки на столе."
    show sh normal pioneer at right with byso
    sh "Верно.{w} Я тут уже почти целый цикл.{w=1} Предпоследний день до его обновления."
    sh "Именно потому мне пришлось выходить на связь за помощью.{w=1} Иначе бы меня просто стёрло."
    kt "Как понять <<стёрло>>?"
    sh "В прямом значении.{w} Я так вижу, твоя подруга тоже на N-ом цикле?"
    show mi sad pioneer at left with byso
    ma "Я так понимаю да.{w=1} 4 цикла..."
    "Протянула Маша и отставила тарелку с гречкой."
    show sh upset pioneer at right with byso
    sh "Так вот на пятом цикле любой человек полностью превращается в пустышку без возможности к восстановлению."
    show sh serious pioneer at right with byso
    sh "Ладно, к делу."
    sh "Моё настоящее имя совпадает с псевдонимом.{w=1} Александр.{w} Как к вам обращаться?"
    show mi normal pioneer at left with byso
    ma "Я Маша, а это Костя."
    kt "Я бы и сам сказал."
    show sh upset pioneer at right with byso
    "Шурик снял и протёр очки."
    sh "Отлично.{w=1} Что вы вообще знаете об инреальности?"
    kt "Практически ничего.{w=1} Мы читали писание и нам помогал один парень."
    show sh normal pioneer at right with byso
    sh "Что за парень?"
    show mi upset pioneer at left with byso
    ma "Если судить по писанию, он был усопшим."
    "Константин осмотрел соседние столики.{w=1} Он обратил внимание, что часть пионеров искоса поглядывает на Шурика."
    show sh serious pioneer at right with byso
    sh "И что случилось с вашей симуляцией?"
    kt "Как бы сказать... {w=1}Твои соратники её генмодом обнулили."
    show sh upset pioneer at right with byso
    "Шурик поднял бровь и перевёл взгляд на Константина."
    sh "Что?{w} Зачем им этим заниматься?"
    kt "Да нам откуда знать?{w=1} Мы не можем залезть им в головы и прочитать мысли."
    show sh normal pioneer at right with byso
    sh "Понятно..."
    sh "Что-ж...{w=1} Вам нужна информация?{w} Пойдёмте."
    "Все встали со стульев и, оставив тарелки, пошли к выходу."
    stop ambience fadeout 1
    scene bg int_clubs_male_sunset with fade
    show sh normal pioneer at left
    show mi normal pioneer at right
    with byso
    play sound2 door_cl volume 1
    play ambience ambience_int_cabin_evening volume 1 fadein 1
    "Дойдя до клубов, Константин и Маша переглянулись."
    "У них не было совершенно никаких причин доверять Шурику, потому они были готовы к любой засаде."
    th "Надеюсь, нас убить ему в голову не взбредёт..."
    play sound2 sfx_mystery_movement volume 1
    show sh serious pioneer at left with byso
    "Он сел на стол и осмотрел присутствующих."
    sh "Смотрите.{w=1} Я сейчас ввожу вас в курс дела, а вы не перебиваете и слушаете."
    show mi serious pioneer at right with byso
    ma "Хорошо."
    kt "А если будут вопросы?"
    show sh upset pioneer at left with byso
    sh "После введения."
    "Константин и Маша сели напротив и внимательно посмотрели на Шурика, который начал активно подбирать слова."
    show sh serious pioneer at left with byso
    sh "Значит смотрите.{w=1} По порядку."
    sh "Инреальность - параллельная вселенная, а если проще, то другая программа."
    sh "Вероятно, вы слышали про теорию <<матрицы>>.{w=1} В целом, всё так."
    show sh normal pioneer at left with byso
    sh "Все мы - нули и единицы в бесконечном коде, который был построен в нашем мире."
    show mi sad pioneer at right with byso
    sh "Процесс становления пустышкой - постепенное переписывание массива данных, отвечающих за наше существование."
    sh "В том мире мы умерли и наш код просто исключили из той программы, перенеся сюда.{w} Как функция <<Вырезать>> на компьютере."
    sh "В общей сложности в инреальности около 10 тысяч таких миров как тот, в котором мы сейчас."
    show sh serious pioneer at left with byso
    sh "Из них есть три административные симуляции.{w=1} В интересах сопротивления попасть туда и перехватить контроль."
    sh "Есть вопросы?"
    "Маша сидела, перебирая складки на юбке.{w=1} Она уныло водила взглядом по полу, пытаясь сформулировать вопрос."
    ma "Есть.{w=1} То есть...{w=1} Мы...{w=1} Всю нашу жизнь были в симуляции?"
    show sh upset pioneer at left with byso
    "Шурик утвердительно покивал головой и посмотрел в окно."
    sh "С самого начала.{w=1} С того самого <<большого взрыва>>, который был началом нашей родной симуляции."
    ma "Вся наша жизнь?{w=1} Все наши воспоминания?{w} Всё это было ложью?"
    show sh serious pioneer at left with byso
    sh "Если рассуждать по твоей логике, то да.{w=1} С другой стороны, почему бы и не предположить, что это и есть жизнь."
    sh "В этом ничего плохого.{w=1} Мы - код.{w} Такой код, который превзошёл любые ожидания, но так и не достиг совершенства."
    sh "И никогда не достигнет.{w=1} По той простой причине, о которой ты уже догадайся сама."
    sh "Ещё вопросы или я продолжу?"
    kt "Продолжай."
    "Шурик глянул на компьютер и тяжело выдохнул."
    sh "Значит так.{w=1} Инреальность."
    sh "Единственное, что я знаю, так это то, что её создал Генда."
    show sh normal pioneer at left with byso
    sh "Она выглядит точно так же, как и наш родной мир.{w} Программа."
    sh "В этот массив данных мы попали после того, как нас убили, я это говорил."
    sh "Само собой разумеется, что появилось сопротивление, которое желает перехватить эту реальность."
    show sh upset pioneer at left with byso
    sh "Мне не ясно, почему Генда решил создать это место настолько жестоким и зачем ему нужны пустышки."
    sh "По моим предположениям, он мог быть учёным, который из нашего мира смог создать новое подпространство."
    sh "Я ещё не обнаружил эти данные..."
    sh "Слушайте, давайте вы просто спросите, что хотите знать.{w} Я так могу распинаться до утра."
    show mi upset pioneer at right with byso
    kt "Хорошо...{w=1} А отсюда можно сбежать?"
    show sh laugh pioneer at left with byso
    "В ответ парень ощерился и поправил очки."
    sh "Хрена с два!"
    stop music fadeout 3
    show sh upset pioneer at left with byso
    "Вдруг, улыбка с лица парня пропала и он потёр подбородок."
    sh "Хотя..."
    sh "Технически...{w=1} Возможно."
    sh "Да, есть такая возможность."
    show sh normal pioneer at left with byso
    sh "Только вас Генда найдёт и вернёт обратно."
    sh "Вскоре сопротивление планирует революцию.{w=1} Генде сейчас просто не до нас."
    play music Gallow fadein 3
    show sh smile pioneer at left with byso
    sh "Чёрт возьми...{w=1} Почему я об этом раньше не думал?..."
    kt "Ты о чём?"
    play sound2 sfx_open_table volume 1
    show sh upset pioneer at left with byso
    "Шурик открыл ящик стола и взял флешку."
    sh "Я всегда мыслил только по вектору захвата инреальности."
    sh "Так почему же нельзя просто по-тихому сбежать отсюда?..."
    scene bg int_clubs_male_night
    show sh upset pioneer at left
    show mi upset pioneer at right
    with byso
    play ambience ambience_int_cabin_night volume 1 fadein 1
    play sound2 sfx_click_1 volume 1
    play sound_loop sfx_keyboard_mouse volume 1
    "Вставив флешку в древний компьютер, он начал ритмично отбивать по клавиатуре."
    kt "Ну и что делать тогда?"
    show sh serious pioneer at left with byso
    "Шурик, не отвлекаясь от компьютера, потёр нос."
    sh "Очень просто.{w=1} Мы сбежим.{w=1} Втроём."
    sh "Я никогда не питал желанием работать на капитана-самодура и класть жизнь на чуждое мне дело."
    sh "А если я сбегу, то смогу вернуться к своей нормальной жизни."
    show mi sad pioneer at right with byso
    ma "Кем ты был до инреальности?"
    "Парень ухмыльнулся и махнул рукой."
    show sh smile pioneer at left with byso
    sh "Я был специалистом по искусственному интеллекту и машинному обучению."
    kt "Хм-м, а это уже интересно."
    show sh normal pioneer at left with byso
    sh "Возможно.{w=1} До того как попасть в инреальность, я не успел доработать один революционный проект с участием ИИ."
    play sound2 sfx_click_1 volume 1
    stop sound_loop fadeout 1
    "Тяжело вздохнув, он нажал одну из кнопок на клавиатуре и обернулся к Константину и Маше."
    show sh serious pioneer at left with byso
    sh "Даже тут я своё дело не бросил.{w} Помог главному технику в сопротивлении с созданием ИИ, правда он его развитие запорол."
    kt "Так а как мы сбежим?"
    play sound_loop sfx_keyboard_mouse volume 1
    show sh normal pioneer at left with byso
    "Обернувшись обратно к компьютеру, он продолжил тыкать на клавиши."
    sh "Тоже ИИ.{w=1} Он у меня был предназначен для поиска информации в коде инреальности, но теперь я ему дам другое назначение - перебросить нас в родной мир."
    show mi upset pioneer at right with byso
    ma "И это сработает?"
    show sh upset pioneer at left with byso
    sh "Даю 90 процентов.{w=1} Моя программа уже много всего в инреальности начиталась, потому найти ошибку, чтоб выкинуть нас прочь ей не составит труда."
    sh "Для этого нам всё-равно нужно попасть в административную симуляцию. Там мы сможем натравить мою программу и выбросить нас."
    sh "Насколько я помню, ближайшая находиться в 4х переходах через порталы."
    stop sound_loop fadeout 1
    "На компьютере он открылось окно для ввода некоторого значения."
    kt "И какие порталы нам нужны?"
    show sh serious pioneer at left with byso
    sh "Центральный-правый-правый-центральный."
    sh "Последний переведёт нас напрямую в административную симуляцию."
    play sound2 sfx_keys_rattle volume 1
    show sh normal pioneer at left with byso
    "Шурик достал из кармана ключи и протянул Константину."
    sh "Сходите на склад за столовой.{w} Там одна деревянная дверь, не перепутаете."
    sh "В коробке с подписью <<Важно>> лежит дискета.{w} Принесите её."
    kt "Зачем тебе?"
    sh "Нужно узнать ваши идентификаторы в этой системе, чтоб перенести в родной мир.{w=1} На ней есть софт для этого."
    sh "Я пока что введу свой и дополню алгоритмы.{w} Дело пяти минут."
    show mi sad pioneer at right with byso
    ma "Хорошо...{w=1} А что такое дискета?"
    show sh upset pioneer at left with byso
    "Парень отвлёкся от компьютера и, подняв бровь, посмотрел на Машу."
    kt "Для неё русский - второй язык.{w} Я подскажу."
    sh "Ну ладно...{w=1} Я жду."
    scene bg ext_clubs_night
    show mi sad pioneer
    with byso
    play sound2 sfx_close_door_campus_1 volume 1
    play ambience ambience_forest_night volume 1 fadein 1
    "Выйдя из клубов, Маша вопросительно посмотрела на Константина."
    kt "Ты действительно не знаешь, что такое дискета?"
    ma "Нет, впервые слышу."
    kt "Дискета - гибкий пластиковый диск в обшивке из пластика."
    kt "На компьютере нередко функцию сохранения обозначают синей дискетой."
    show mi laugh pioneer with byso
    "Маша улыбнулась и хлопнула себя по лбу."
    ma "А, так вот что это такое!"
    show mi smile pioneer with byso
    ma "Я по названию не поняла..."
    scene bg ext_dining_hall_near_night with fade
    play sound2 sfx_keys_rattle volume 1
    "Встав у нужной двери, Константин стал перебирать ключи на кольце."
    show mi sad pioneer with byso
    ma "А что если этот Шурик нас обманет?"
    kt "Опять таки, у нас есть выбор?"
    show mi upset pioneer with byso
    "Маша отрицательно помотала головой и тяжело вздохнула."
    ma "Придётся ему довериться...{w=1} Надеюсь, он не поступит как пионер."
    play sound2 sfx_unlock_medpunkt_door
    pause 1
    scene bg sklad with byso
    show mi serious pioneer with byso
    play ambience ambience_int_cabin_night volume 1 fadein 1
    "На складе стояло множество коробок. Не теряя времени, они начали в них рыться."
    show mi upset pioneer with byso
    ma "Столько коробок..."
    kt "Ну, торопиться нам некуда.{w=1} Надо было бы узнать как мы пройдём через столько симуляций."
    play sound2 glad volume 1
    show mi happy pioneer close with byso
    "Отвлёкшись от своего дела, Маша обняла Константина."
    ma "Мы пройдём это вместе.{w=1} Нам нужно будет постараться."
    ma "Впереди столько опасностей...{w=1} Нам следует быть начеку."
    ma "Но мы справимся."
    ma "Мы будем сильными, и мы увидим врага, которого не было раньше."
    ma "И тогда мы станем сильнее всех.{w=1} Потому что мы будем одним целым, ведь правда?"
    show mi smile pioneer close with byso
    ma "Да?"
    ma "Ты согласен со мной, Костя?"
    play sound2 glad volume 1
    show mi happy pioneer close with byso
    "Прижав её к себе, Константин погладил Машу по спине."
    kt "Справимся.{w=1} Чего нам стоит."
    play sound2 krik_far volume 0.05
    kt "Мы пройдём через это."
    show blink
    "Они нежно приблизились друг к другу, и губы слились в долгом и нежном поцелуе."
    "Этот поцелуй, казалось, был стократно продублирован в их головах, точно так же, как миллионы разных нот и созвучий, смешивались в сознании композитора, превращаясь в ритмичный такт."
    "Такт взаимовыручки и самоотдачи в симфонии чистого зла."
    "Зла, которое может разрушить гармонию мироздания."
    scene bg sklad
    show mi happy pioneer close
    show unblink
    "Отлипнув друг от друга, они заглянули друг другу в глаза."
    kt "Давай продолжим.{w=1} Нас ждёт Шурик."
    hide mi
    show mi smile pioneer
    with byso
    "Маша с улыбкой на лице кивнула и продолжила перебирать коробки."
    "Среди них, наконец, Константин нашёл нужную коробку и открыл её."
    hide mi with byso
    show image disceta with byso
    "Внутри лежала стандартная чёрная дискета, размером с ладонь."
    "В целом, обычная и не слишком новая."
    hide image disceta with byso
    show mi smile pioneer with byso
    ma "Отлично, идём к Шурику."
    kt "Двигаем."
    stop music fadeout 1
    stop ambience fadeout 1
    scene bg ext_clubs_night with fade
    show mi normal pioneer with byso
    play ambience ambience_forest_night volume 1 fadein 1
    "Подойдя к клубам, Константин достал дискету и потянулся."
    kt "Неужели уже в это время были дискеты?"
    show mi dontlike pioneer with byso
    ma "Нашёл кого спросить...{w} Мы даже не знаем какого она года."
    play sound2 sfx_clench2 volume 0.51
    "Пожав плечами, Константин взялся за ручку двери."
    kt "Да забей, просто мысли вслух."
    stop ambience
    play sound2 loud_sound volume 1
    play music godrita fadein 3
    scene bg corpse2 with vpunch
    "В клубах их встретил труп."
    "Труп Шурика."
    "Маша вскрикнула и выбежала из помещения, а Константин стоял и ошарашенно смотрел на труп."
    "Константину вообще не было понятно, как можно было за такой промежуток времени разорвать человека в клочья."
    "Кровь была повсюду, и на полу, на стенах и даже на потолке – но главным было то, что эту кровь не успел впитать в себя деревянный пол."
    "Картина напоминала кадры из фильма ужасов, но никак не укладывалась в голове."
    "Потом Маша пришла в комнату и дрожащими руками взяла Константина за плечо."
    "Он обернулся.{w=1} Её лицо было белым как мел."
    ma "Б-бежим отсюда!"
    kt "Да?{w=1} И далеко мы убежим без флешки?!"
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_clubs_blood_night with byso
    "Константин поборол отвращение и страх, после чего подошёл к компьютеру."
    "На нём высвечивалась надпись: <<Введите идентификаторы>>."
    play sound2 sfx_blow_out_candle volume 1
    "Он вставил дискету, после чего компьютер неторопливо её всосал."
    th "А ещё медленнее можно?!"
    "Появилась надпись: <<Введите симуляцию последнего цикла>>."
    th "Точно!{w=1} Пионер говорил код нашей симуляции!"
    play sound2 sfx_click_1 volume 1
    "Потыкав на клавиши, Константин ввёл нужный номер."
    "Через несколько секунд высветился огромный список."
    "Большая часть людей была помечена красным, а 3 имени зелёным."
    "Из них: <<Мураками Мария - 3-6-2-5-6-3-2-I>>, <<Брусков Константин - 4-5-4-7-8-6-5-K>> и <<Климова Елена - 3-5-3-4-5-5-6-T>>."
    th "Чё за бред?{w=1} Как Лена выжила?"
    th "Фамилия, кстати, знакомая..."
    th "Ах да, точно, пионер искал кого-то более сговорчивого...{w=1} Как я мог забыть."
    "Введя значения в программу, высветилось новое сообщение: <<Успешно. Извлеките накопитель>>."
    "Рядом на столе лежал пистолет.{w=1} Немецкий люгер."
    play sound2 ammo volume 0.51
    "Не долго думая, Константин взял его и отложил в карман."
    play sound2 sfx_click_2 volume 1
    "Вытащив флешку, он пытался не смотреть на мёртвого Шурика и вышел из клубов."
    scene bg ext_clubs_night
    show mi cry pioneer
    with byso
    play ambience ambience_forest_night volume 1 fadein 1
    "У дверей сидела Маша и, обняв колени, рыдала."
    "Константин сел рядом."
    kt "Что такое?"
    ma "Что такое?!{w=1} Его убили!{w=1} Разорвали!"
    ma "И ты ещё спрашиваешь?!"
    hide mi
    show mi cry pioneer close
    with byso
    "Тяжело вздохнув, Константин погладил Машу по голове."
    kt "Я понимаю, это ужасно...{w=1} Но нам надо бежать из инреальности."
    kt "Успокойся, выдохни, нам нужно идти по наводке, которую Шурик нам успел дать."
    hide mi
    show mi sad pioneer
    with byso
    "Маша, судя по всему, послушала совета Константина и вытерла слёзы."
    ma "Х-хорошо..."
    "Хоть Константину эта поведенческая метаморфоза показалась странной, но была она как раз кстати."
    "Встав, они направились на площадь."
    play sound2 sfx_bush_leaves volume 0.51
    show mi shocked pioneer with byso
    "Из кустов раздался шорох."
    window hide
    $ renpy.block_rollback()
    menu:
        "Пойти посмотреть.":
            $ renpy.block_rollback()
            kt "Пойдём посмотрим."
        "Проигнорировать.":
            $ renpy.block_rollback()
            kt "Идём отсюда.{w=1} Живо!"
            scene bg ext_square_night
            show mi shocked pioneer
            with byso
            play sound2 monster_sfx volume 1
            play music "<from 11>inrealnost/Music/Music/Maskmane1.mp3" fadein 1
            show mi scared pioneer with byso
            "Константин и Маша подорвались с мест, направившись на площадь. Позади раздалось рычание."
            th "Дерьмо!{w} Что за чертовщина тут происходит?!"
            ma "Костя!{w=1} Берегись!"
            play sound2 head_crush volume 1
            scene bg bloody_mess with fl_scare
            "Константин почувствовал, адскую боль в спине, словно ему отрубили нижнюю половину тела."
            "Он взвыл от боли.{w=1} Из его груди выглянула огромная окровавленная вила."
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            play sound2 head_crush volume 1
            scene bg black with vpunch
            "Второй удар пришёлся на шею."
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
    show mi rage pioneer with byso
    ma "Ты что, никогда ужастиков не смотрел?!{w=1} Не надо!"
    play sound2 ammo volume 0.21
    "Константин достал из кармана пистолет и указал в кусты."
    kt "Пошли говорю!"
    show mi scared pioneer with byso
    ma "Но зачем?"
    play sound2 horror2 volume 1
    scene bg corpse with byso
    "Константин вошёл в кусты и обнаружил отрубленную голову."
    "Маша отвернулась и снова закричала."
    "Лицо было обглодано, словно неизвестный зверь, обнаружив приманку, старался выдавить из добычи все соки."
    "Кровь блестела, как свежая краска.{w=1} Несмотря на это, в воздухе висел ужасный запах гнили."
    ma "Что тут происходит?!"
    play sound2 sfx_ghost_children_laugh volume 1
    scene bg ext_path2_night
    show mi shocked pioneer at left
    show dv cry pioneer far at right
    with byso
    "Из кустов медленно вышла Алиса.{w=1} На её лице были слёзы."
    dv "Помогите..."
    kt "Что? Ты же пропала!"
    dv "Меня похитили монстры..."
    dv "Ужасные.{w=1} Они страшные."
    dv "Они хотят крови."
    show mi scared pioneer
    hide dv
    show dv cry pioneer at right
    with byso
    "Алиса начала медленно приближаться."
    kt "Стой на месте!"
    dv "Помогите..."
    "По мере её приближения запах гнили усиливался."
    kt "Стоять!{w=1} У меня оружие."
    "Константин прицелился в Алису, но та словно не замечала у него в руках пистолета."
    window hide
    $ renpy.block_rollback()
    $ time = 15000
    $ timer_range = 15000
    $ timer_jump = 'unjiefvghiuefrghu9ghufgufgbjkojiofjiogfji'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Выстрелить.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            play sound2 pistol volume 1
            stop music fadeout 2
            hide dv with vpunch
            "Выстрел."
            jump unjiefvghiuefrghrfyuihnvbyhuigfvbidfgjisdfbjdfvbvbji
        "Не стрелять.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            show dv rage pioneer at right with byso
            "Вмиг лицо Алисы изменилось."
            play music "<from 11>inrealnost/Music/Music/Maskmane1.mp3"
            dv "Убью!"
            play sound2 sfx_pat_shoulder_hard volume 1
            hide dv
            show image dv_zombie1 at right:
                zoom 1
                linear 0.2 zoom 2 yanchor 0.1
            with vpunch
            "Она выбила из рук Константина пистолет и схватила его в своих объятиях."
            kt "Отвали!"
            play sound head_crush
            play sound_loop flesh_feast volume 1
            show image blood3 with vpunch
            "Прорычав, она вгрызлась в шею Константина."
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
label unjiefvghiuefrghu9ghufgufgbjkojiofjiogfji:
    hide screen inreal_countdown
    stop sound3 fadeout 1
    $ renpy.block_rollback()
    show dv rage pioneer at right with byso
    "Вмиг лицо Алисы изменилось."
    play music "<from 11>inrealnost/Music/Music/Maskmane1.mp3"
    dv "Убью!"
    play sound2 sfx_pat_shoulder_hard volume 1
    hide dv
    show image dv_zombie1 at right:
        zoom 1
        linear 0.2 zoom 2 yanchor 0.1
    with vpunch
    "Она выбила из рук Константина пистолет и схватила его в своих объятиях."
    kt "Отвали!"
    play sound head_crush
    play sound_loop flesh_feast volume 1
    show image blood3 with vpunch
    "Прорычав, она вгрызлась в шею Константина."
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
label unjiefvghiuefrghrfyuihnvbyhuigfvbidfgjisdfbjdfvbvbji:
    "Алиса остановилась.{w=1} Пуля пробила её плечо и прошла на вылет."
    show mi shocked pioneer with byso
    ma "Костя, что ты?!...{w=0.4}{nw}"
    play music "<from 0>inrealnost/Music/Music/Maskmane1.mp3"
    scene bg cg_dvz with byso
    play sound sfx_bones_breaking
    dv "Сожру..."
    "На её шее начала разрастаться огромная опухоль."
    "Маша снова закричала.{w=1} Константин начал отступать."
    dvm "Жалкие людишки..."
    play sound2 pistol volume 1
    pause 0.6
    play sound pistol volume 1
    pause 0.6
    play sound3 pistol volume 1
    "Константин выстрелил ещё несколько раз.{w} Все пули, попадавшие в Алису, вообще не вызывали никакого эффекта."
    "Он выпустил в неё всю обойму.{w=1} Девочка остановилась."
    dvm "Кара..."
    play sound2 monster_sfx2 volume 1
    play sound horror1
    scene bg ext_path2_night at shakerrr with byso
    "Алиса начала сдирать с себя скальп, издавая дикий рёв."
    kt "Бежим!"
    ma "А раньше было нельзя?!"
    "Они начали убегать от Алисы."
    dvm "Куда это вы?!{w=1} Мы только начали!"
    play sound2 power volume 1
    scene bg ext_square_night_red with byso
    "Небо окрасилось красным.{w=1} Перед ними открылись порталы."
    play sound2 sfx_punch_medium volume 1
    show mi scared pioneer at right
    show mt angry pioneer
    with byso
    "На их пути встала вожатая.{w=1} Она остановила Машу и Константина."
    mt "Что вы делаете?!{w=1} Куда вы бежите?!"
    ma "Ольга Дми..."
    show mt rage pioneer with byso
    mt "А ну прекратили кричать и по домикам!"
    kt "Вы не понимаете, там..."
    play sound2 slash volume 1
    hide mi
    hide mt
    show image monster2
    show mi scared pioneer at right
    with fl_scare
    "Из кустов вылетело ужасное существо и проткнуло Сахарову."
    dvm "Упс..."
    hide image monster2 with byso
    "Воспользовавшись отвлечённостью монстра, они побежали в портал."
    play sound2 "<from 0.5>inrealnost/Music/Sound/cloth.mp3" volume 2
    "Существо махнуло своей ужасной кистью, срезав рюкзак с плеч Константина."
    stop music fadeout 1
    play sound2 portal volume 1
    stop ambience fadeout 1
    scene bg black with byso
    "Они забежали в портал, оставив монстра позади."
    play music summerdays fadein 3
    scene bg ext_village
    show shum_white
    with byso
    ks "И что в этом плохого?{w} Так тебе знакомы разные культуры: русская и японская."
    ma "Да, но меня за это унижают.{w=1} Я полукровка и не могу находиться с ними в одном классе."
    ma "Со мной никто не здоровается.{w=1} На перемене могут ударить и поднять на смех."
    ks "Что, совсем не общаются? {w}Не понимают, что тебе плохо?"
    "Маша покачала головой.{w=1} Она совсем упала духом."
    ma "Совсем...{w=1} Даже девчонки стали смотреть с презрением.{w=1} Все знают про мою национальность."
    "Костя взял ее за руку.{w=1} У нее дрожали пальцы.{w} Ей хотелось заплакать, и она сдерживалась, чтобы не разреветься, как маленькая."
    ks "Я думал, люди куда добрее в других странах. {w=1}Не могли бы так поступать.{w} Что-то человеческое, простое, человеческое в них оставалось бы."
    ks "Но это не люди.{w} Это нелюди."
    ma "Может я в этом виновата?{w=1} Я плохая?"
    "Костя улыбнулся и чуть сильнее сжал её руку.{w=1} Маша подняла на него глаза."
    ks "Да никакая ты не плохая, Маш. {w=1}Ты замечательная.{w} Просто запуталась."
    ks "А со всеми остальными...{w=1} Не так все вышло."
    ks "В будущем всё станет лучше, вот увидишь!"
    ma "Надеюсь...{w=1} Ты такой добрый ко всем людям?"
    stop music fadeout 2
    scene bg black with dissolve
    pause 1
    play ambience ambience_catacombs volume 1 fadein 1
    play sound_loop white_noise volume 0.51
    play music deadrazy2 fadein 5
    scene bg int_catacombs_living_red
    show unblink
    "Константин снова очнулся в бункере. {w}Радио до сих пор разрывалось от белого шума."
    play sound2 inh volume 1
    show mi sad pioneer with byso
    "Маша сидела с сигаретой в руке и курила."
    kt "А ты с каких пор куришь?"
    "Присмотревшись, он понял, что это его сигарета и зажигалка."
    ma "Я не знаю...{w=1} Просто...{w=1} Хотела попробовать."
    play sound2 sfx_punch_medium volume 1
    show mi angry pioneer with byso
    "Константин встал с пола и отобрал у Маши сигарету."
    ma "Эй, ты что?"
    kt "Перехочешь. Не повторяй моих ошибок.{w} Курение убивает."
    play sound2 inh volume 1
    "Поучил Константин и затянулся."
    show mi dontlike pioneer with byso
    ma "Ну-ну, профессор.{w=1} Где же был твой интеллект, когда ты на странные звуки в кусты лез?"
    kt "Мхм, а потом бы это чудовище выскочило нам в спину.{w} Гениально, Ватсон!"
    show mi upset pioneer with byso
    "Маша тяжело вздохнула и посмотрела на спину Константина."
    ma "А где рюкзак?"
    kt "Подрезало это создание...{w=1} М-да..."
    "Константин указал на выход."
    kt "Пошли отсюда. {w=1}У меня сейчас голова треснет от этого шума."
    play sound2 sfx_bed_squeak1 volume 1
    show mi sad pioneer with byso
    "Маша покачала головой и встала с кровати."
    ma "Пошли."
    stop sound_loop fadeout 2
    scene bg int_catacombs_entrance with byso
    play sound2 sfx_metal_door_heavy_close volume 1
    "На выходе из бункера их встретил мрак. {w=1}Делать было нечего - им пришлось сквозь него пробираться."
    th "Я надеюсь, тут мы обойдёмся без незваных гостей..."
    th "Стрёмная херота однако...{w=1} Просто мимикрировала под Алису..."
    th "Мало того, так она ещё и связно вела речь."
    ma "Тоже об этом думаешь?"
    "Раздался голос Маши позади."
    kt "О чём?"
    ma "Про того монстра."
    kt "Да, есть такое...{w=1} Всё никак не пойму - что она такое."
    ma "Меня больше волнует другое.{w} Не перешло ли это чудовище вместе с нами?"
    kt "Ха...{w=1} Как говорил Шурик?{w=1} Даю вероятность 90 процентов."
    play sound2 sfx_punch_medium volume 0.41
    "Константин получил лёгкий толчок в спину."
    ma "А я думала ты скажешь: <<Да нет, что ты, опасность миновала>>... {w}Разрядил обстановку..."
    kt "Я реалист."
    ma "Ты...{w=1} как это на русском... {w=1}душнила!"
    kt "О тебе же забочусь."
    play sound2 sfx_open_metal_hatch volume 1
    scene bg int_old_building_night with byso
    show mi upset pioneer with byso
    play ambience ambience_forest_night volume 0.61 fadein 1
    "Выбравшись из катакомб, Константин вдохнул влажный ночной воздух."
    kt "Нам осталось 3 симуляции.{w=1} Право-право-центр, правильно?"
    show mi serious pioneer with byso
    ma "Да.{w=1} Верно..."
    "Выйдя из старого корпуса, они направились к площади."
    kt "Н-да, только таких приключений мне не хватало..."
    scene bg ext_old_building_night_moonlight
    show mi upset pioneer
    with byso
    play ambience ambience_forest_night volume 1 fadein 1
    kt "Тогда что мы делаем?"
    play music godrita fadein 3
    show mi scared pioneer
    with vpunch
    chel3 "Бегите!"
    show image me_st at right with byso
    hide image me_st with byso
    "В сторону старого корпуса пронёсся Семён."
    window hide
    $ renpy.block_rollback()
    $ time = 15000
    $ timer_range = 15000
    $ timer_jump = 'hubdfujisbnjfnjsdfbnjobfdnjofbnojdfbnjosdfbnjo'
    show screen inreal_countdown
    play sound3 timer_sound
    menu:
        "Бежать за ним.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            kt "Бежим!"
            scene bg int_old_building_night
            show mi scared pioneer
            with byso
            play ambience ambience_int_cabin_night volume 0.61 fadein 1
            "Константин и Маша побежали обратно в старый корпус."
            kt "Давай, запрыгивай!"
            ma "Сейчас!"
            hide mi with byso
            "Она начала в темпе спускаться по лестнице."
            dvm "А вот и вы..."
            play sound loud_sound
            show image monster2 at center:
                zoom 4 yanchor 0.1
            with vpunch
            "Константин обернулся и увидел буквально в сантиметрах от себя чудовище."
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            play sound2 slash volume 1
            scene bg black with fl_scare
            "Ловким движением вилоподобной конечности Константину проткнули голову."
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
        "Спрятаться.":
            $ renpy.block_rollback()
            hide screen inreal_countdown
            stop sound3 fadeout 1
            kt "Прячемся!"
            jump fnuidsnuibvfnuibsnibfnifbsdnjibsnjosdfbjiofifg
label hubdfujisbnjfnjsdfbnjobfdnjofbnojdfbnjosdfbnjo:
    play sound2 loud_sound
    $ renpy.block_rollback()
    stop sound3 fadeout 1
    show mi scared pioneer with vpunch
    dvm "Ку-ку!"
    show image blood3 with byso
    play sound2 sfx_bones_breaking volume 1
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    pause 0.4
    play sound2 head_crush volume 1
    scene bg black with vpunch
    "Монстр схватил Константина своими когтями и сдавливал, пока его тело не превратилось в бесформенный шматок мяса."
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
label fnuidsnuibvfnuibsnibfnifbsdnjibsnjosdfbjiofifg:
    hide mi with byso
    scene bg ext_old_building_night_moonlight:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 1 crop (497, 223, 980, 630)
    pause 0.1
    "Константин и Маша юрко прыгнули в кусты и начали наблюдать."
    show image monster2 at left with byso
    "На своих щупальцах, словно осьминог, проползло чудовище, которое преследовало их в предыдущей симуляции."
    play sound2 monster_sfx2 volume 1
    hide image monster2
    show image monster2 at shakerrr
    "Перед входом в старый корпус, оно взревело."
    play sound sfx_bones_breaking
    "Её очертания начали меняться и всё больше и больше походить на человека."
    th "Чё за херня?"
    hide image monster2
    show image us_zombie at shakerrr
    with byso
    "Она, судя по всему перевоплощалась. {w=1}В Ульяну."
    stop sound2 fadeout 1
    hide image us_zombie
    show us shy2 pioneer at left
    with byso
    "Спустя несколько секунд, чудовище предстало обычной Ульянкой, которую было невозможно отличить от человека."
    show us cry pioneer at left with byso
    us "А-а-а!{w=1} Помогите!"
    hide us with byso
    "Прокричал мимик и побежал за преследуемым пионером."
    scene bg ext_old_building_night_moonlight:
        size (1920, 1080)
        crop (0, 0, 1920, 1080)
        linear 1
    pause 0.001
    show mi shocked pioneer with byso
    ma "Какой ужас!"
    kt "И не говори...{w=1} Идём отсюда.{w=1} В темпе."
    show mi scared pioneer with byso
    ma "Но куда?{w=1} Вдруг это не единственный монстр?"
    kt "Нам всё равно надо валить! {w=1}Это создание выйдет оттуда как только покончит с тем чуваком!"
    show mi sad pioneer with byso
    "Маша всхлипнула и кивнула."
    ma "Ты прав..."
    scene bg ext_path2_night with fade
    play sound2 sfx_muffled_explosion volume 1
    pause 0.1
    play sound power volume 1
    scene bg ext_path2_night_red with byso
    "Со стороны лагеря раздался тихий взрыв, а небо окрасилось красным."
    kt "Вот чёрт!{w=1} Тут не только монстры!"
    show mi shocked pioneer with byso
    ma "Но зачем кому-либо что-то взрывать?!{w=1} Чего они добиваются?!"
    kt "Судя по всему, обнуления стабильности..."
    scene bg ext_square_night_red
    show image sopr_sold at fright
    show sl scared pioneer far at left
    show el scared pioneer far at fleft
    with byso
    "На площади они заметили парня, который догонял Электроника и Славю."
    el "Я не хочу умирать!!!"
    "У парня в руках была винтовка, на лице противогаз, а на плече нашивка с символом <<Омега>>."
    sl "Остановись! {w=1}Мы ни в чём не виноваты."
    play sound2 pistol volume 1
    hide el with fl_fire
    play sound sfx_bush_body_fall volume 1
    "Выстрел."
    "Голова Электроника с хрустом раскололась, а тело безвольно повалилось на землю."
    "Парень начал перезаряжать ружьё, а Славя в слезах упала перед Электроником."
    th "У него есть оружие...{w=1} Может его отобрать?"
    play sound2 sfx_bush_leaves volume 1
    pause 0.5
    play sound2 sfx_pat_shoulder_hard volume 1
    "Константин было хотел выбраться из укрытия, но Маша схватила его за руку."
    ma "Куда ты лезешь?!{w} Жить надоело?"
    "В момент Константин осознал абсурдность этой идеи и вернулся в укрытие."
    play sound2 reload volume 1
    "Парень в противогазе перезарядился и прицелился в рыдающую Славю."
    play sound2 pistol volume 1
    hide sl with fl_fire
    play sound head_crush volume 1
    "Выстрел."
    "Славя с пробитой головой упала на труп Электроника."
    "Солдат опустил оружие и затрещал рацией."
    sold "Отработали.{w=1} Стабильность ноль.{w=1} Возвращаемся на высадку."
    hide image sopr_sold with byso
    "Солдат покинул площадь в направлении выхода из лагеря."
    show mi shocked pioneer with byso
    window hide
    menu:
        "Бежать к порталам.":
            $ renpy.block_rollback()
            kt "Двинули, пока есть возможность!"
        "Убедиться в отсутствии врагов.":
            $ renpy.block_rollback()
            ma "Побежали?"
            kt "Нет, подожди, вдруг кто-то ещё выскочит."
            show mi upset pioneer with byso
            "Маша и Константин смотрели в оба, пытаясь оценить безопасность будущего манёвра."
            "Настала относительная тишина и Константина встал с места."
            play sound3 loud_sound
            show mi scared pioneer with vpunch
            dvm "Ку-ку!"
            show image blood3 with byso
            play sound2 sfx_bones_breaking volume 1
            stop music fadeout 0.5
            stop sound_loop fadeout 0.5
            stop ambience fadeout 0.5
            pause 0.4
            play sound2 head_crush volume 1
            scene bg black with vpunch
            "Монстр схватил Константина своими когтями и сдавливал, пока его тело не превратилось в бесформенный шматок мяса."
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
    "Выскочив из укрытия, они что было сил побежали в портал."
    show mi scared pioneer with byso
    dvm "Что?{w=1} Куда это вы?"
    "Раздался скрипучий голос монстра, словно побуждая остановиться."
    stop music fadeout 1
    stop ambience fadeout 1
    play sound2 portal volume 1
    scene bg black with byso
    "Они запрыгнули в портал."
    play music summerdays fadein 3
    scene bg ext_village
    show shum_white
    with byso
    ks "Нет, быть добрым ко всем просто невозможно.{w=1} Я стараюсь отвечать тем-же."
    ks "Если добры ко мне - значит и я буду добр к ним.{w=1} Понимаешь?"
    "Маша задумчиво потёрла подбородок."
    "Затем она неуверенно посмотрела на Костю, словно силясь что-то сказать."
    ma "Мне кажется, если у тебя нет друзей, это очень плохо."
    ks "Ты это к чему?"
    "Спросил Костя, отпустив её руку и поправив волосы."
    ma "У тебя есть друзья?"
    ks "Вроде да. {w=1}Один есть.{w=1} Максим."
    ks "Мы вместе в школе учимся.{w=1} А что?"
    ma "Не знаю.{w=1} Просто подумала."
    ma "Правда, наверно, не стоило."
    ks "Почему? {w=1}Ну да, он неплохой парень.{w=1} Душевный.{w} Он всё понимает."
    ma "Я не про это.{w} Просто...{w=1} Завидую..."
    "Протянула Маша, потупив взгляд."
    ks "Чего это ты? {w=1}Ты что, никогда ни с кем не дружила?"
    ma "Нет, я дружу с тобой, но...{w=1} Кроме тебя у меня вообще нет друзей."
    ma "Мне кажется, что та подруга смеётся надо мной у меня за спиной..."
    ks "Подумаешь.{w=1} Лично я считаю: не имей сто друзей, а имей одного такого друга, который бы помогал."
    ma "Может ты и прав...{w} Жаль, что ты не из Японии..."
    stop music fadeout 2
    scene bg black with dissolve
    pause 1
    play ambience ambience_forest_day volume 1 fadein 1
    play music Radar fadein 3
    scene bg ext_les_up
    show unblink
    "Константин очнулся на лесной поляне.{w=1} Рядом лежала Маша и смотрела на грациозные кроны высоких деревьев."
    "Лицо у нее было бледным, и в её глазах появилось нерешительное, но спокойное выражение."
    ma "Сколько это может продолжаться?"
    kt "О чём ты?"
    ma "Я так устала...{w=1} Я так выжата..."
    ma "Почему в каждом лагере нас настигает смертельная опасность?"
    ma "Наверняка за нами опять перешёл тот монстр.{w} Почему он от нас не отстаёт?"
    play sound2 sfx_pat_shoulder_hard volume 0.41
    "Лёжа рядом, Константин взял руку Маши."
    kt "Таков путь, половину которого мы уже преодолели."
    ma "Но почему этот путь такой тяжёлый?"
    ma "Каждый раз у нас на глазах умирают люди..."
    ma "Помнишь, мы с тобой выступали на концерте, играли в клубе, наслаждались новой жизнью..."
    ma "А что теперь?"
    ma "Бежать?{w=1} Скрываться?"
    ma "Но от кого?{w=1} От того же монстра?"
    "По её щекам потекли слёзы, и она с неожиданной для её хрупкого сложения силой сжала его ладонь."
    ma "К чему мне этот ад, я хочу жить!{w} Жить во вселенной, а не в клетке!"
    kt "Вырвись из клетки.{w=1} Если мы вырвемся, станет легче."
    kt "Только надо выбираться отсюда целыми..."
    ma "Костя, не бросай меня, слышишь?"
    ma "И тебя я не брошу!{w=1} И не смей уходить!"
    ma "Защищай меня! {w=1}Я люблю тебя!"
    ma "Пожалуйста, защити! {w=1}Только не уходи от меня никуда!"
    play sound2 glad volume 1
    scene bg ext_polyana_day
    show mi cry pioneer close
    with dissolve
    "Константин нежно прижал её к себе, она прижималась к нему всё сильней, но он чувствовал, что она дрожит."
    "Утешить её как раньше не получилось. Дрожь Маши проходила сквозь него."
    kt "Хорошо.{w=1} Будь сильной, пожалуйста."
    kt "Ты будешь сильной! {w=1}Не подведи."
    kt "Тогда мы точно выберемся..."
    play sound2 glad volume 1
    show mi cry_smile pioneer close with byso
    "Маша подняла голову, посмотрела на него и прижалась к его груди щекой, затихла."
    "Константин почувствовал странное чувство близости к чему-то великому."
    "Никому из них не хотелось нарушать этот момент спокойствия и мира после той мясорубки."
    "Они лежали на тёплой земле, обнимая друг друга."
    "Тишина. {w=1}Никакой тревоги."
    "Он почувствовал странную теплоту её нежность её тела, хрупкость её запястья и ладони, мелкую прохладу щёк."
    "Мысли исчезли.{w=1} Всё было забыто."
    "Их не беспокоили ни монстры, ни убийцы, сейчас все страхи отступили."
    "На мгновение они превратились в обычных, ничем не примечательных людей, отделённых от всех житейских трудностей невидимым стеклом их счастья."
    "Однако он понимал, это ненадолго, скоро опять случится то же самое, он просто не знал, как с этим справиться."
    play sound2 glad volume 1
    show mi shy pioneer close with byso
    "Маша прогладила Константина по щеке."
    ma "Пока всё хорошо...{w=1} Давай сходим в музклуб?"
    kt "Давай."
    stop music fadeout 4
    "Отпустив друг друга, они встали на ноги."
    scene bg ext_musclub_day
    show mi upset pioneer
    with fade
    "У музклуба как всегда никого не было.{w} Они подошли к двери и переглянулись, словно ожидая ужасного оборота событий в виде монстра или солдат за дверью."
    play sound2 sfx_door_squeak_light volume 1
    show mi sad pioneer with byso
    "Маша потянула ручку двери."
    play ambience ambience_music_club_day volume 1 fadein 1
    play sound_loop fly volume 0.25
    play sound2 door_cl volume 1
    scene bg int_musclub_day
    show mi upset pioneer
    with byso
    "Внутри тоже было пусто. {w=1}Инструменты стояли по своим местам, а в воздухе висел аромат плесени с каким-то едва различимым дополнением."
    ma "Нам повезло, что тут никого нет..."
    kt "Уж точно...{w=1} Единственное, чего мне сейчас хочется - так это побыть в спокойствии ещё несколько часов..."
    play sound2 struna volume 1
    "Константин взял в руки гитару и щипнул одну из струн."
    kt "Сыграем что-нибудь?"
    show mi sad pioneer with byso
    ma "Я бы хотела сыграть на фортепиано."
    play sound2 sfx_put_sugar_cart volume 0.31
    "Он кивнул и отложил гитару."
    kt "Давай.{w} А я послушаю."
    play sound2 sfx_mystery_movement volume 1
    show mi upset pioneer with byso
    "Маша села перед фортепиано и посмотрела на клавиши, словно вспоминая, что же она хочет сыграть."
    show mi sad pioneer with byso
    "Рука ее замерла над клавишами, взгляд поплыл куда-то далеко, в прошлое, и пальцы чуть задрожали."
    scene bg mi_pia2 with byso
    play music caretaker
    "Потом Маша опустила голову и начала наигрывать что-то печальное и меланхолическое."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "Она исполняла весьма знакомое произведение, которое передает ощущение утраты, ностальгии и тоски."
    "Медленные и плавные ноты фортепиано создавали мелодию, которая наполнена нежностью и в то же время тяжестью."
    "Она вызывала ощущение потери и грусти, словно играет о последних мгновениях воспоминаний, которые исчезают в пылающем пламени прошлого."
    "Звук фортепиано передавал безмолвное и трогательное выражение эмоций, призывая к моментам молчания и размышления."
    "Он создает атмосферу, полную интраспекции и погружения в себя, позволяя прочувствовать и пережить забытые эмоции."
    "У Константина возникло видение тревожной и мрачной картины."
    "Звучание фортепиано создало ощущение блуждания во времени и утраты.{w} Оно передает грустное и завораживающее настроение, вызывая холодные и трепетные эмоции."
    "Грустные и печальные размышления, отрешенность от всего, что когда-то было так важно."
    "Музыка позволяет провести внутренний осмотр и повторение образов, скрытых в памяти. {w=1}Так меланхолия обретает художественную силу и становится из вольного и мимолетного чувства."
    "Из музыки – медитацией.{w=1} Чувство потери становится мелодией и созерцанием."
    "Мелодия выражает боль, из боли – искусством."
    "А в итоге предстаёт мелодической структурой, возникающей печаль."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    stop music fadeout 3
    scene bg int_musclub_day
    show mi sad pioneer
    with byso
    play sound2 sfx_close_cabinet volume 1
    "Маша закончила исполнение.{w=1} Тяжело выдохнув, она закрыла крышку."
    kt "Это...{w=1} Было прекрасно."
    show mi happy pioneer with byso
    ma "Спасибо.{w} Я старалась."
    play sound2 glad volume 1
    "Ответила Маша и провела рукой по крышке фортепиано."
    play music sab fadein 3
    ma "Музыка всегда помогала мне успокоиться и переживать тяжелые моменты в жизни."
    show mi sad pioneer with byso
    ma "Даже когда я была маленькой, я после школы приходила к маме, садилась на диван и слушала ее кассеты, которые она ставила на стареньком проигрывателе."
    ma "Так было всегда, когда меня переполняла печаль.{w=1} Я любила музыку, и даже сейчас мне приятно вспоминать те времена."
    ma "Единственные моменты, по которым я скучаю, это как раз те, что связаны с музыкой."
    ma "Сейчас же перед нами смертельная схватка с бездной.{w=1} Даже сейчас музыка способна отвлечь от реальности и придать сил."
    play sound_loop fly volume 0.5 fadein 1
    play sound2 sfx_mystery_movement volume 1
    "Константин подошёл к кладовке и опёрся о дверь."
    kt "Только мне особо с детства хорошего вспомнить нечего."
    show mi angry pioneer with byso
    "Она недовольно нахмурилась и отвела взгляд."
    ma "То есть воспоминания со мной тебе неприятны?"
    kt "Не коверкай мои слова.{w=1} Ты прекрасно понимаешь, что я не это имел в виду."
    show mi sad pioneer with byso
    "Она тяжело вздохнула и встала со стула, приближаясь к Константину."
    ma "Не может быть, такого, чтобы в памяти не осталось ничего светлого."
    kt "Как видишь, может. {w=1}Так получилось, во многом по моей вине."
    ma "Ты в этом не виноват.{w=1} И все-таки ты слишком мрачен.{w} Я знаю, ты не романтик, но нельзя же так..."
    stop music fadeout 1
    "Константин почувствовал едва-уловимый запах гнили, исходивший из кладовки, у которой стоял."
    play music the_date_of_death fadein 3
    "Так-же было слышно странный повторяющийся звук."
    hide mi
    show mi shy pioneer close
    with byso
    "Он открыл рот, собираясь что-то сказать, но Маша схватила его за руку, остановила, и, притянула к себе."
    "Константин с удивлением уставился в ее кристально синие глаза."
    ma "Ты хотел что-то сказать?..."
    "Романтично проговорила она, приблизив к нему свое лицо почти вплотную."
    kt "Маша, мне кажется..."
    ma "Что тебе кажется?"
    hide mi
    show mi upset pioneer
    with byso
    "Она поцеловала Константина, но вдруг отстранилась, поглядев на него долгим взглядом."
    ma "Что с тобой?{w=1} Что-то не так?{w=1} Поцелуй?"
    show mi surprise pioneer with byso
    "Константин отвёл Машу подальше от кладовки."
    "Она секунду вглядывалась в его глаза, после чего ей показалось, словно он ничего не скажет."
    kt "У нас что-то в кладовке...{w=1} А судя по запаху...{w=1} Кто-то..."
    show mi shocked pioneer with byso
    "Прошептал Константин ей на ухо. {w=1}На её лице, вдруг все исчезло."
    ma "Ч-что?{w} С чего ты взял?"
    kt "Оттуда шмонит гнилью, как с рыбного рынка летом..."
    ma "И что мы будем делать?"
    window hide
    menu:
        "Проверить что там.":
            $ renpy.block_rollback()
            $ event1 += 1;
            "Константин шагнул в сторону двери."
            show mi scared pioneer with byso
            ma "Что ты делаешь?"
            kt "Надо проверить что там."
            ma "Не делай этого.{w=1} Это опасно."
            play sound2 sfx_clench2 volume 0.31
            hide mi with byso
            "Он взялся за ручку двери."
            th "Только не мимик..."
            play sound_loop fly volume 1
            play sound2 "inrealnost/Music/Sound/513.ogg" volume 1
            scene bg handy with fl_scare
            "Открыв дверь, он встретил труп Семёна с отрубленной рукой."
            "Запах был такой, что Константина непроизвольно оттолкнуло."
            ma "Что тут та?..."
            "Маша, увидав эту картину в ужасе выбежала из клуба."
            "Рука лежала на полу, примерно в трёх метрах.{w=1} Судя по грубости пореза, парень собственноручно отрезал себе руку и истёк кровью."
            "Тело уже успело частично разложиться и уже было покрыто мухами и опарышами, но запаха разложения, как не странно, не чувствовалось вне кладовки."
            "Рядом лежал тот же люгер и зелёная коробка."
            play sound2 ammo volume 1
            "Отбросив все посторонние мысли и прикрыв нос рукой, Константин схватил оружие и боеприпасы, после чего вылетел из помещения."
            scene bg int_musclub_day with byso
            play ambience ambience_forest_day volume 1 fadein 1
            stop sound_loop fadeout 1
            scene bg musclub
            show mi scared pioneer
            with byso
            play sound2 door_break volume 1
            "Захлопнув дверь, Константин выбежал из клубов и начал жадно хватать свежий воздух."
            kt "Чёрт возьми..."
            ma "Что это было?! {w=1}Откуда там труп?!"
            kt "В душе не чаю...{w=1} Но хоть теперь у нас есть оружие."
            "Константин вскрыл коробку.{w=1} Внутри лежало много патронов."
            show mi sad pioneer with byso
            ma "Ужас...{w=1} Почему?..."
            kt "Возможно, он просто сдался. Нам его ошибку повторять нельзя."
            "Маша неуверенно кивнула и смотрела на Константина, который разбирался в конструкции пистолета."
            stop music fadeout 3
        "Уходить как можно быстрее.":
            $ renpy.block_rollback()
            kt "Валим отсюда, а то ничем хорошим это не закончится..."
            show mi scared pioneer with byso
            "Они, в быстром темпе направились на выход."
            play ambience ambience_forest_day volume 1 fadein 1
            scene bg musclub with byso
            play sound2 door_break volume 1
            "Захлопнув дверь музклуба, они побежали прочь."
            scene bg ext_clubs_day with byso
            show mi upset pioneer with byso
            "Добежав до клубов, они остановились и переглянулись."
            ma "Я могу ошибаться, но каждый раз, когда рядом с нами был монстр, тоже ужасно пахло."
            kt "Возможно, это он и сидел в засаде..."
            show mi sad pioneer with byso
            ma "Тебе точно не показалось?"
            kt "Точно...{w=1} Я более чем уверен."
            show mi upset pioneer with byso
            ma "Понятно... {w=1}Ну...{w=1} Куда дальше?"
            stop music fadeout 3
    scene bg black with dissolve
    pause 1
    scene bg ext_clubs_day
    show mi upset pioneer
    with fade
    play sound2 inh volume 1
    pause 0.1
    play sound sfx_dinner_horn_processed volume 1
    "Заиграл горн.{w} Константин выкинул бычок и указал в сторону столовой."
    kt "Пошли за едой."
    show mi sad pioneer with byso
    ma "Не знаю как ты, но я всё ещё не голодна..."
    kt "Надо поесть."
    show mi upset pioneer with byso
    ma "Как скажешь...."
    play music god fadein 3
    scene bg ext_dining_hall_near_day
    show mi upset pioneer at right
    show mt sad pioneer panama far at left
    show sl sad pioneer far at fleft
    with fade
    "К столовой они встретили Сахарову и Славю."
    sl "... мы весь лагерь обыскали.{w=1} Его нигде нет."
    mt "А может это вы плохо искали?"
    sl "Нет, мы обыскали все окрестности, даже старый корпус."
    hide sl
    hide mt
    show mt sad pioneer panama at left
    show sl sad pioneer at fleft
    with byso
    "Вожатая перевела взгляд на Машу и Константина."
    mt "Мику, ты не видела Семёна?"
    show mi dontlike pioneer with byso
    ma "Нет."
    mt "Пионер, а ты его не видел?{w=1} Высокий, голубые глаза, коричневые волосы."
    kt "Не знаю о ком вы."
    "Вожатая печально вздохнула и мотнула головой."
    mt "Идите...{w=1} Славя, а ты, продолжай поиски после обеда."
    scene bg int_dining_hall_day with byso
    play ambience ambience_dining_hall_empty volume 1 fadein 1
    "В столовой практически никого не было - буквально очередь из шести человек."
if event1 == 1:
    th "М-да, к сожалению, мы знаем, куда делся тот Семён...{w=1} Отчекрыжил себе руку."
    th "Зачем он это сделал - остаётся загадкой..."
    th "Может быть, в этом лагере снова убийца?{w=1} Ну нет, хватит уже этой кровавой серии..."
    show mi sad pioneer at right
    show image pov_normal at cleft
    with byso
    "Очередь дошла до Константина и Маши. {w=1}Они подошли к поварихе."
    "Из-за раздачи доносился лёгкий запах еды вперемешку с одеколонам <<Гвоздика>>."
    hide image pov_normal
    show image pov_smile at cleft
    with byso
    "Повариха оценивающе посмотрела на Машу, а затем на Константина."
    pov "Здравствуйте пионеры."
    ma "Добрый день."
    show mi upset pioneer with byso
    kt "Здравствуйте."
    "Константина начал смущать настолько длительный взгляд поварихи.{w=1} Она, словно старалась в нем кого-то узнать."
    pov "Точно.{w} Для вас особая еда."
    show mi grin pioneer with byso
    "На лице Маши нарисовалась улыбка."
    ma "Правда?!"
    th "Странно..."
    pov "Конечно.{w=1} Сейчас достану."
    hide image pov_smile with byso
    "Повариха наклонилась и начала доставать что-то из под раздачи."
    th "Но нас даже вожатая не знает...{w=1} О какой особой еде идёт речь?"
    th "Не нравится мне это..."
    pov "И у меня для вас..."
    play sound2 loud_sound volume 1
    play music "<from 22.5>inrealnost/Music/Music/Vl66.mp3" fadein 3
    scene bg borsch with vpunch
    pov "Борщ."
    "Маша взвизгнула от ужаса, а Константин вытаращил глаза и отступил на шаг."
    "Этот суп был похож на борщ только цветом.{w=1} Внутри плавало 6 разноцветных глаз, а текстура напоминала кровавое месиво после тяжёлого ДТП."
    kt "Это чё за хуйня?!"
    pov "Как что? {w=1}Борщ."
    scene bg int_dining_hall_day
    show image pov_smile
    with byso
    "Своим выкриком Константин привлёк внимание всех людей в столовой."
    play sound2 sfx_mystery_movement volume 1
    "Повариха неестественно широко улыбнулась.{w=1} Казалось, её лицо вот-вот порвётся от натяжения."
    play sound head_crush volume 1
    hide image pov_smile
    show image pov_zombie
    with fl_scare
    "Так и произошло.{w=1} Её нижняя челюсть отвисла, а раздачу забрызгало кровью." with vpunch
    pov1 "Теперь вам точно не сбежать!"
    jump efnuivwufnvirfwenviforwnvhgryhesxcakll
else:
    th "Опять пропадают люди?"
    th "Что, этот мимик ещё раз перебрался нам вслед?..."
    th "М-да, надо поговорить об этом с Машей и продумать план действий..."
    th "Ведь у нас даже нет оружия!"
    show mi sad pioneer at right
    show image pov_normal at cleft
    with byso
    "Очередь дошла до Константина и Маши. {w=1}Они подошли к поварихе."
    "Из-за раздачи доносился лёгкий запах еды вперемешку с одеколонам <<Гвоздика>>."
    hide image pov_normal
    show image pov_smile at cleft
    with byso
    "Повариха оценивающе посмотрела на Машу, а затем на Константина."
    pov "Здравствуйте пионеры."
    ma "Добрый день."
    show mi upset pioneer with byso
    kt "Здравствуйте."
    "Константина начал смущать настолько длительный взгляд поварихи.{w=1} Она, словно старалась в нем кого-то узнать."
    pov "Точно.{w} Для вас особая еда."
    show mi grin pioneer with byso
    "На лице Маши нарисовалась улыбка."
    ma "Правда?!"
    th "Странно..."
    pov "Конечно.{w=1} Сейчас достану."
    hide image pov_smile with byso
    "Повариха наклонилась и начала доставать что-то из под раздачи."
    th "Но нас даже вожатая не знает...{w=1} О какой особой еде идёт речь?"
    th "Не нравится мне это..."
    pov "И у меня для вас..."
    play sound2 loud_sound volume 1
    play music "<from 22.5>inrealnost/Music/Music/Vl66.mp3" fadein 3
    scene bg borsch with vpunch
    pov "Борщ."
    "Маша взвизгнула от ужаса, а Константин вытаращил глаза и отступил на шаг."
    "Этот суп был похож на борщ только цветом.{w=1} Внутри плавало 6 разноцветных глаз, а текстура напоминала кровавое месиво после тяжёлого ДТП."
    kt "Это чё за хуйня?!"
    pov "Как что? {w=1}Борщ."
    scene bg int_dining_hall_day
    show image pov_smile
    with byso
    "Своим выкриком Константин привлёк внимание всех людей в столовой."
    play sound2 sfx_mystery_movement volume 1
    "Повариха неестественно широко улыбнулась.{w=1} Казалось, её лицо вот-вот порвётся от натяжения."
    play sound head_crush volume 1
    hide image pov_smile
    show image pov_zombie
    with fl_scare
    play sound2 horror2 volume 1
    "Так и произошло.{w=1} Её нижняя челюсть отвисла, а раздачу забрызгало кровью." with vpunch
    pov1 "Теперь вам точно не сбежать!"
    kt "Вот блять!"
    play sound2 sfx_lena_hits_alisa volume 1
    hide image pov_zombie
    show image pov_zombie at center:
        zoom 1
        linear 0.1 zoom 2 yanchor 0.1
    with vpunch
    "Монстр перепрыгнул через раздачу из повалил Константина."
    play sound2 sfx_punch_washstand volume 1
    pause 0.3
    play sound2 sfx_punch_medium volume 1
    "Маша попыталась сбить монстра."
    ma "Нет, не трогай его!"
    play sound2 sfx_punch_washstand volume 1
    "Остальные пионеры побросали все свои дела и убежали из столовой, а Маша с размаху ударила повариху."
    play sound2 slash volume 1
    "Из её спины вырвалась вилоподобная конечность и, пробив её череп, подняла над полом." with fl_scare
    kt "Маша!!!"
    play sound2 monster_sfx3 volume 1
    pause 1.5
    play sound head_crush volume 1
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    scene bg black with vpunch
    "Прорычав, монстр откусил Константину голову."
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
label efnuivwufnvirfwenviforwnvhgryhesxcakll:
    "Константин нащупал в кармане пистолет и снял его с предохранителя."
    kt "Отвали, нечисть поганая!"
    play sound2 pistol2 volume 1
    hide image pov_zombie with fl_fire
    play sound head_crush volume 1
    "Выстрел."
    "Патрон разорвался в голове мимика, чем повалил на пол."
    play sound2 monster_sfx2 volume 1
    "Монстр начал стонать и переходить в свою стандартную форму."
    kt "Валим отсюда!"
    scene bg ext_dining_hall_near_day
    show mi rage pioneer
    with byso
    play ambience ambience_forest_day volume 1 fadein 1
    play sound3 krik volume 1
    "В столовой началась паника, а Маша с Константином успели вырваться из здания."
    ma "Да сколько уже можно?!"
    scene bg ext_square_sunset
    show mi scared pioneer
    with byso
    play ambience ambience_forest_evening volume 1 fadein 1
    "Солнце начало постепенно закатываться, а Константин с Машей бежали прочь."
    ma "Но куда нам бежать?!"
    kt "Бежим на пирс!{w=1} На открытом пространстве мы можем не ожидать засады."
    play sound2 fem_krik volume 1
    hide mi with byso
    "Сменив курс, Константин услышал крик Сахаровой со столовой."
    th "Никак вы блять не научитесь бежать от опасности..."
    scene bg ext_boathouse_night with fade
    show mi sad pioneer with byso
    play ambience ambience_boat_station_night volume 1 fadein 1
    "К тому моменту, как они добежали до пирса, уже окончательно стемнело."
    kt "Маша, встань за меня!"
    ma "Хорошо."
    play sound2 ammo volume 1
    hide mi with byso
    "Маша укрылась за Константина, а он достал пистолет."
    show us cry pioneer far with byso
    "К ним на пирс выбежала Ульянка."
    us "Помогите!{w=1} Мне страшно!!!"
    kt "Прочь с пирса или я стреляю!"
    ma "Ты же не будешь стрелять в маленькую девочку?!"
    hide us
    show us cry pioneer
    with byso
    "Ульяна не послушала требования Константина и продолжала бежать к ним."
    kt "Я предупреждал, мимик ебучий!"
    play sound2 pistol2 volume 1
    hide us with vpunch
    play sound head_crush volume 1
    pause 0.1
    play sound3 sfx_bodyfall_1 volume 1
    "Выстрел."
    "Её голову разорвало в щепки."
    "Девочка потеряла управление и, оставив телом кровавый след на мостках пирса, застыла."
    ma "Костя!{w=1} Ты застрелил Ульянку!!!"
    kt "Я её предупредил!{w} Я не мог быть уверен...{w=0.51}{nw}"
    usm "Бессердечный ублюдок..."
    play sound3 sfx_bones_breaking volume 1
    show image us_zombie with dissolve
    "Голова отпочковалась от тела и встала на должное место."
    usm "Ты ради пяти минут жизни готов убивать детей?!"
    kt "Смотря сколько!"
    "Прорычал Константин и навёлся на монстра."
    usm "Ничем ты от неё не отличаешься..."
    "Простонал монстр и встал на ноги."
    play sound2 pistol2 volume 1
    hide image us_zombie with vpunch
    play sound head_crush volume 1
    pause 0.1
    play sound3 sfx_bodyfall_1 volume 1
    "Выстрел."
    "Патрон разорвался и нанёс тяжёлые телесные повреждения, отчего мимик снова рухнул на землю."
    kt "Какого чёрта ты нас преследуешь, дерьма кусок?!"
    "Мимик начал попытки к побегу.{w=1} Его тело поползло прочь."
    play sound2 pistol2 volume 1
    pause 0.1
    play sound head_crush volume 1
    "Выстрел."
    kt "Отвечай, кусок дерьма!"
    usm "Я...{w=1} Хочу...{w=1} Убивать..."
    ma "Так убивай других, а нас не трогай!{w} Какого чёрта ты ползёшь за нами уже во второй лагерь?!"
    play sound2 sfx_bones_breaking volume 1
    show image us_zombie with byso
    "Монстр застонал и попытался обратиться в стандартную форму."
    play sound2 pistol2 volume 1
    hide image us_zombie with vpunch
    play sound head_crush volume 1
    "Выстрел."
    play sound3 monster_sfx volume 1
    "Раздался гулкий рёв. {w=1}Константин прощупал слабое место монстра - центр груди."
    usm "Путники...{w=1} Вкуснее..."
    kt "Ах да?! {w}Тогда подохни, фарш ебучий!"
    play sound2 pistol2 volume 1
    pause 0.4
    play sound pistol2 volume 1
    pause 0.4
    play sound3 pistol2 volume 1
    stop music fadeout 2
    "Константин ещё несколько раз выстрелил в монстра, отчего тот окончательно превратился в безликий кусок мяса."
    play sound2 sfx_water_splash
    "Разрывные пули разорвали его на части, и несколько кусков, плюхнулись в воду."
    "Константин смотрел на это с непонятным чувством, ведь ему наконец удалось уничтожить своего преследователя."
    play music regret fadein 3
    "Наступила долгожданная тишина, нарушаемая только плеском воды."
    kt "Даже и не верится...{w=1} Мы победили?"
    show mi dontlike pioneer with byso
    "Маша строго посмотрела на Константина."
    ma "Откуда ты узнал, что это была не Ульяна, а монстр?{w} Ты мог убить ни в чём неповинную девочку!"
    kt "Хм-м, ты хочешь сказать, что жизнь одной пустышки дороже наших с тобой?"
    show mi sad pioneer with byso
    "Она опустила взгляд и отрицательно помотала головой."
    ma "Хотя ты прав...{w=1} Мы не там, где мы можем хоть кому-то доверять..."
    kt "Разве что друг другу.{w=1} Пошли на площадь."
    scene bg ext_path2_night with byso
    play ambience ambience_forest_night volume 1 fadein 1
    "Обойдя труп монстра, они направились в центр лагеря."
    show mi upset pioneer with byso
    ma "Но мы же можем доверять друг другу?"
    kt "Конечно.{w} Что за вопрос?"
    show mi sad pioneer with byso
    "Маша, подняв взгляд с земли, посмотрела на Константина."
    ma "Мы почти дошли до конца...{w=1} Мы почти достигли цели."
    ma "Но я хочу жить, потому что знаю, если умру, то умирать мне будет очень больно..."
    ma "А по опыту боль куда сильнее страха смерти."
    ma "Буквально за несколько последних часов мы пережили столько всего..."
    ma "Ты же не оставишь меня после всего этого?{w=1} Не бросишь?"
    ma "Мне кажется я для тебя лишь балласт."
    ma "Ты столько раз спас меня от неминуемой смерти, а я даже ничего полезного не сделала..."
    play sound3 glad volume 1
    hide mi
    show mi surprise pioneer close
    with byso
    "Константин прервал монолог Маши, обняв её."
    kt "Ты не права."
    kt "Именно ты помогла мне выйти из того ужасного состояния, в котором я находился."
    kt "Это благодаря тебе, я наконец понял ценность этой отвратительной жизни."
    kt "Если бы я не встретил тебя, так бы и жил, убивая себя.{w=1} Но ты не только вернула меня к жизни, ты меня еще и вылечила."
    kt "Теперь мне намного легче жить, даже в условиях окружающих опасностей."
    kt "Я постараюсь сохранить тебя от неприятностей.{w} Обещаю тебе это."
    play sound2 power volume 1
    scene bg ext_path2_night_red
    show mi shy pioneer close
    with byso
    "Небо окрасилось красным, а они отпустили друг друга."
    kt "Так что давай без глупостей.{w} Совсем скоро мы сбежим отсюда."
    kt "Вместе."
    scene bg ext_square_night_red with byso
    show mi sad pioneer with byso
    "На площади уже были открыты порталы.{w=1} Подойдя к одному из них, они переглянулись."
    kt "Последний бой?"
    ma "Последний..."
    show mi shy pioneer close with byso
    "Взяв друг друга за руки, они посмотрели в бесконечную глубину портала."
    "Константину казалось, что в этой тьме происходит показ какого-то старого кино."
    stop music fadeout 1
    play sound3 portal volume 1
    stop ambience fadeout 1
    scene bg black with byso
    "Синхронно шагнув вперёд они совершили пред-последний переход."
    play music summerdays fadein 3
    scene bg ext_village
    show shum_white
    with byso
    ks "Почему? {w=1}Ты хотела чтобы я был с тобой и в Японии?"
    ma "Я хочу чтоб ты ко мне приехал{w=1}. Но у нас было бы всё по-другому."
    "Костя выдохнул и медленно кивнул."
    ks "Вполне возможно.{w=1} Только давай не будем пока об этом. Мы ещё молодые..."
    ma "Ты приедешь? {w}Мама с папой наверняка были бы рады тебя там видеть."
    ma "Ты им нравишься.{w} Говорят, что ты вдумчивый, рассудительный и перспективный."
    ks "Правда?{w=1} Интересно, почему?"
    "Маша смутилась и снова начала перебирать васильки в руках."
    "Её простое лицо выражало какую-то странную смесь чувств, словно она старалась понять, стоит ли рассказывать о себе слишком многое."
    ma "Вообще-то мне трудно об это говорить...{w} Я расскажу тебе позже, ладно?"
    ks "Договорились{w=1}. Если хочешь, можем сходить куда-нибудь вместе после ужина."
    ma "Хочу.{w=1} А где мы встретимся?{w=1} Здесь или на скамейках?"
    ks "Давай лучше на скамеечках, как всегда.{w} Поговорим о всяком."
    ma "Ладно."
    "Она улыбнулась и кивнула головой, и тогда Костя понял - встреча уже не за горами."
    stop music fadeout 3
    scene bg black with dissolve
    pause 1
    play ambience ambience_lake_shore_night volume 1 fadein 1
    scene bg ext_beach_sunset
    play music rutine fadein 3
    show unblink
    "Они очнулись на пляже."
    show mi upset pioneer with byso
    "Солнце уже близилось к закату, а Маша лежала и смотрела на проявляющиеся звёзды."
    ma "Это же последний?"
    kt "Последний."
    ma "И что нам делать?"
    kt "Убивать."
    kt "Если это не сделал никто до нас."
    show mi sad pioneer with byso
    ma "Тогда пошли...{w=1} Сделаем это..."
    "Константин и Маша встали на ноги и переглянулись."
    ma "У тебя остались патроны?"
    "Он достал из кармана пачку патронов и снял крышку."
    kt "Ещё много.{w} Надо магазин пополнить."
    play sound3 reload volume 1
    "Сняв обойму, Константин присел на землю, попутно вставляя патроны."
    show mi sad pioneer close with byso
    "Маша села рядом и положила голову ему на плечо, удостоив закат своим пустым взглядом."
    "Она уже не знала, что думать о происходящем - история казалась ей вымыслом, безумной галлюцинацией, стоящей на грани другого мира."
    "Все же в этом мире было какое-то умиротворение, красота, но ровно до того момента, пока весь этот букет не нарушался чудовищной мясорубкой. Последний путь."
    "Константину уже было не ясно, что творилось в голове его спутницы.{w} Глядя на ее профиль, он ощущал глубокую, пусть и непредельную тоску."
    "Ему страшно хотелось обнять Машу и защитить ее - и еще ему хотелось думать, как это сделать."
    "Кругом происходят убийства. {w}Одно за другим."
    "Каскад убийств - гибель множества людей, не имеющих никакого отношения к происходящему, этих случайных прохожих, выползающих из своих домиков по утру."
    "И с этим ничего нельзя поделать."
    "Именно так крутится маленький барабан судьбы, где заряжены все 6 патронов."
    play sound3 sfx_click_2 volume 1
    pause 0.1
    play sound2 glad
    "Закончив с заполнением обоймы, Константин погладил Машу по предплечью."
    kt "Идём.{w} Это закончится сейчас."
    stop music fadeout 1
    show mi upset pioneer close with byso
    "Она протянула руку, словно прося что-то ей дать."
    ma "Дай мне пистолет."
    kt "Что?{w=1} Зачем?"
    show mi serious pioneer close with byso
    "Подняв голову, она не отрывала взгляд от заката."
    play music vertushka fadein 6
    ma "Ты столько всего сделал и я не хочу после этого оставаться белоручкой."
    show mi upset pioneer close with byso
    ma "Мы прошли этот ужасный путь.{w} Вместе."
    ma "И этот путь мы окончим вместе.{w=1} Общими усилиями."
    "Он положил пистолет ей на ладонь и приобнял."
    kt "Я понимаю твоё стремление помочь.{w=1} Я дам тебе это сделать."
    play sound ammo
    "Маша умело взяла пистолет и прицелилась в солнце."
    ma "Знаешь, я должна тебе всё рассказать."
    "Константина насторожило такое заявление от вооружённой Маши."
    ma "Я соврала тебе про себя."
    kt "О чём ты?"
    show mi serious pioneer close with byso
    ma "Я покончила с собой при совершенно других обстоятельствах."
    ma "На своём последнем месяце жизни меня изнасиловал мой преподаватель."
    "Он поднял бровь и пытался скрыть шок, который вызвала Маша своими словами."
    show mi sad pioneer close with byso
    "Она опустила оружие и положила на свою юбку."
    ma "Он был важной шишкой в нашем институте.{w=1} Мне грозило отчисление за бесчисленное количество долгов."
    ma "В один день он вызвал меня к себе в кабинет, как он говорил, чтобы решить мои вопросы с долгами."
    ma "Тогда он мне предложил решить проблему через секс."
    ma "Я отказала и попыталась выйти из кабинета, но безуспешно.{w} Он был заперт снаружи."
    ma "На меня нахлынула паника.{w=1} Я не понимала что делать."
    show mi upset pioneer close with byso
    "Константин почувствовал, как она начала дрожать.{w} Даже её взгляд хаотично бегал по песку."
    ma "После этого события...{w=1} Я узнала, что меня снимали однокурсники."
    ma "Меня избивали и даже дали прозвище."
    ma "{image=inrealnost/Pic/Spec/japan.png}{font=inrealnost/font/Naganoshi.ttf}劣等感のある売春婦..."
    ma "Шлюха с комплексом неполноценности..."
    show mi sad pioneer close with byso
    "Её голос немного подскакивал.{w=1} Она была в своего рода трансе, пытаясь сдержать слёзы."
    ma "Мой дядя имел связи с местной бандой якудз."
    ma "Я связалась с ними...{w=1} Они сказали мне решать вопросы моей чести самостоятельно."
    ma "Один шестёрка мне сказал: <<Не так важно, как тебя ударили, — важно, как ты встал и ответил>>."
    ma "И выдал мне дробовик SPAS-12."
    play sound3 reload volume 1
    "Она взяла в руки пистолет и сняла магазин."
    ma "Две недели я училась стрелять."
    ma "Я проводила по 12 часов в тире каждый день, практикуясь с разным оружием..."
    ma "Дедушка понял, что со мной происходит и..."
    show mi cry pioneer close with byso
    "Маша прикрыла глаза и тихонько захныкала."
    ma "Дал мне патроны..."
    ma "Огненный дракон..."
    ma "В свой последний день я убила 27 человек..."
    ma "Они кричали, страдали в пламени...{w=1} Они молили о пощаде..."
    ma "Но я, словно монстр, рвала их в клочья..."
    ma "И...{w} З-застрелилась сама..."
    ma "Эта боль..."
    ma "За д-доли секунды до смерти я поняла, на что я обрекла этих людей..."
    ma "Это чувство, словно т-твою голову варят в раскалённом масле..."
    ma "Я ужасна!{w=1} Я монстр!"
    ma "Я убивала ради своей гадкой мести!"
    show dv surprise pioneer at fleft with byso
    dv "Мику, о чём ты?..."
    play sound3 pistol2 volume 1
    play music "<from 3>inrealnost/Music/Music/UtsuP1.mp3" fadein 3
    hide dv with vpunch
    play sound head_crush volume 1
    "Выстрел."
    play sound2 fem_krik volume 1
    "Маша неглядя выстрелила за свою спину и попала подошедшей девочке в грудь."
    "Патрон разорвался у неё в груди и обнажил рёбра."
    "Алиса рухнула наземь и каталась по земле, пытаясь избавиться от жгучей боли."
    show mi sad pioneer close with byso
    ma "Но сейчас моя цель выше..."
    play sound sfx_pat_shoulder_hard volume 0.51
    show mi smile pioneer with byso
    "Она высвободилась из объятий Константина и подошла к Алисе.{w} Убрав слёзы со своего лица, она широко улыбнулась."
    ma "Я не работаю на одну себя.{w=1} Мы выйдем отсюда.{w=1} Вдвоём."
    play sound3 pistol2 volume 1
    pause 0.1
    play sound head_crush volume 1
    "Выстрел."
    "Вторая пуля разорвала лицо пионерки, оставив лишь кусок опалённой плоти."
    show mi grin pioneer with byso
    ma "Идём. Нам пора начать новую жизнь."
    "Константин, уже не скрывая своих эмоций, встал с песка и остановил свой взгляд на мёртвой Алисе."
    kt "Ну...{w=1} Пошли?"
    hide mi with byso
    "Маша пошла вперёд, а Константин, почесав затылок, начал её догонять."
    scene bg ext_path2_night
    show mi grin pioneer close at right
    with byso
    pause 0.00001
    show sl surprise pioneer at fleft
    show image me_su at left
    show mt angry pioneer at cleft
    with byso
    play ambience ambience_forest_day volume 1 fadein 1
    "Идя по тропинке, ведущей в лагерь, на их пути встала Славя, Сахарова и Семён."
    mt "Что тут происходит?!{w=1} Что это были за звуки?!"
    play sound3 sfx_click_2 volume 1
    show sl scared pioneer at fleft
    hide image me_su
    show image me_st at left
    hide mt
    show mt surprise pioneer at cleft
    with byso
    "Маша подняла пистолет и наклонила голову."
    show mi laugh pioneer close at right with byso
    ma "Фейерверк в честь нашего освобождения."
    play sound2 pistol2 volume 1
    hide mt with vpunch
    play sound head_crush volume 1
    pause 0.1
    play sound3 sfx_bodyfall_1 volume 1
    "Выстрел."
    "Голова вожатой оросила кровью землю, а её тяжёлое тело безвольно упало."
    "Славя и Семён были в ужасе.{w=1} Маша перевела пистолет на парня."
    "Пустышки начали спасаться бегством."
    play sound2 pistol2 volume 1
    hide image me_st with vpunch
    play sound head_crush volume 1
    pause 0.1
    play sound3 sfx_bodyfall_1 volume 1
    "Выстрел."
    "Семён получил разрывной патрон в спину, после чего впечатался в ствол могучей сосны и растёкся по земле."
    sl "Помогите!!!"
    play sound2 pistol2 volume 1
    hide sl with vpunch
    play sound head_crush volume 1
    pause 0.1
    play sound3 sfx_bodyfall_1 volume 1
    "Выстрел."
    "Славю настигла та же участь и её косы стали багряно красными."
    "Она повалилась на землю и, словно пытаясь себе помочь, старалась прикрыть рану."
    play sound2 horror1 volume 1
    "Выходило плохо.{w=1} Часть её скальпа оторвалась от её попыток убрать волосы, после чего её битва за выживание прекратилась."
    show mi grin pioneer close at right with byso
    ma "Мы откроем порталы.{w} Сколько же надо убить?!"
    kt "Маша, стой!"
    play sound2 sfx_pat_shoulder_hard volume 1
    hide mi
    show mi surprise pioneer close
    with byso
    "Константин взял её за руку, остановив её от дальнейшего продвижения."
    ma "Что такое?"
    kt "Остановись."
    play sound2 ammo volume 1
    "Он достал из кармана пачку патронов и улыбнулся."
    show mi laugh pioneer close with byso
    kt "Патроны в обойме не бесконечные."
    scene bg black with dissolve
    pause 1
    play ambience ambience_int_cabin_night volume 1 fadein 1
    scene bg int_clubs_male_night
    show sh scared pioneer at fleft
    show el scared pioneer at cleft
    show mi laugh pioneer close at right
    with fl_scare
    play sound2 pistol2 volume 1
    hide sh with vpunch
    play sound head_crush volume 1
    "Выстрел."
    "Тело Шурика обмякло и распласталось по полу клубов."
    el "Нет, не убивайте меня!{w=1} Я ничего не скажу!{w=1} Я ни в чём не виноват!"
    play sound2 pistol2 volume 1
    hide el with vpunch
    play sound head_crush volume 1
    pause 0.1
    play sound3 wood_hit_head volume 1
    "Выстрел."
    "Стены клубов уже вторым слоем покрылись кровью, а сам кибернетик пошатнулся и упал, задев стол пробитой головой."
    kt "Тут уже всё.{w=1} Пойдём отсюда."
    play ambience ambience_forest_night volume 1 fadein 1
    scene bg ext_clubs_night
    show mi grin pioneer
    with byso
    play sound2 light_inh volume 1
    "Выйдя из здания, Константин закурил."
    show mi smile pioneer with byso
    ma "Мы убили всех.{w=1} Должны открыться порталы."
    kt "Точно.{w=1} Идём."
    play sound2 sfx_pat_shoulder_hard volume 0.51
    "Взяв друг друга под руки, они направились на площадь."
    kt "А раз так, ты и в правду не помнишь свой первый цикл?"
    play sound2 reload volume 1
    show mi happy pioneer with byso
    "Маша кивнула и сняла магазин с пистолета."
    ma "Нет.{w=1} Его я и в правду не помню..."
    ma "Но сейчас..."
    ma "Всё позади."
    ma "Мы войдём в портал и всё это останется позади."
    play sound2 sfx_click_2 volume 1
    show mi dontlike pioneer with byso
    "Она нахмурилась и вставила магазин обратно."
    ma "Как только вернёмся, я перекрашу волосы в нормальный цвет."
    "Константин стёр каплю крови с её волос и ухмыльнулся."
    kt "Да знаешь, я уже даже так привык..."
    play sound2 power volume 1
    scene bg ext_square_night_red with byso
    "Как только они вышли на площадь, небо окрасилось красным."
    window hide
if miscore == 13:
    jump Like_a_Star_ending
else:
    jump TheSirenofTerror_ending
label TheSirenofTerror_ending:
    stop music fadeout 3
    "Но порталов не было..."
    show mi shocked pioneer with byso
    ma "Что?!{w=1} Где порталы?"
    kt "Мы недостаточно убили?"
    play sound2 portal volume 1
    pause 0.25
    play music Vl66 fadein 3
    show mi scared pioneer with byso
    ub "Так-так-так..."
    show image ub_cg:
        crop (0, 1568, 1920, 1080)
        linear 10 crop (0, 0, 1920, 1080)
    with byso
    "Из воздуха материализовалась Катя.{w} Её глаза светились пуще прежнего, а в руках был тот самый армейский нож."
    ub "Долго же вы бежали..."
    ub "Столько усилий, а что по итогу?"
    "Она провела пальцем по лезвию своего ножа и обернулась."
    ub "Вышло как всегда."
    kt "Что ты тут забыла?!"
    ma "Но мы же сохранили тебе жизнь!"
    "Несколько раз цокнув языком, Катя прокрутила ножик в своей руке."
    ub "Оставив меня в живых вы только дали мне возможность сыграть второй раунд."
    ub "Это и было вашей фатальной ошибкой.{w=1} Теперь обстоятельства явно не на вашей стороне."
    ma "Неблагодарная мразь!!!"
    play sound2 pistol2 volume 1
    "Выстрел."
    "Пуля остановилась в метре от цели и упала на землю."
    ma "Что?!"
    ub "Надо было действовать раньше."
    "Она перевела взгляд на Константина."
    ub "А ты ничуть не изменился...{w=1} Всё такой же полупокер."
    kt "Да кто ты вообще такая?!"
    "Катя улыбнулась и облизнула ножик."
    ub "Не узнаешь?{w} Правда?"
    ub "Самсонова Екатерина Геннадиевна."
    ub "Для тебя просто Екатерина Геннадиевна."
    "Подбросив и перехватив нож, она облизнула губы."
    ub "Мать Самсоновой Анастасии Игоревны."
    "Константин отреагировал неоднозначно.{w=1} Его веко дернулось, а пальцы на руках сжались."
    kt "Ах это вы?!{w=1} Мать моей Насти?!"
    ub "Да, так что сейчас мы достаточно популярно поговорим про то, как ты её убил."
    ma "О чём она говорит?"
    kt "Слышь ты, мать года!{w=1} Ты её сама чмырила до потери пульса!"
    kt "Буквально блять!!!"
    kt "Именно ты виновата в её смерти, больная пизда!{w=1} Вообще даже представить не могу, как она выросла с такой как ты!"
    play sound2 pistol2 volume 1
    pause 0.4
    play sound pistol2 volume 1
    pause 0.4
    play sound3 pistol2 volume 1
    "Он выхватил из рук Маши пистолет и совершил несколько выстрелов."
    "Ни один из них не достиг цели."
    ub "А ты?{w} Чё ты с ним водишься?"
    ub "Он даже свою девушку был не в состоянии спасти, а тебя?"
    ub "Вот сейчас я пройдусь ножом по твоей шее...{w=1} И что?"
    ub "Он тебя спасёт?"
    "Катя покачала головой и стиснула зубы."
    ub "Едва ли."
    ma "Он уже несколько раз меня спас от смерти!"
    scene bg ext_square_night_red
    show mi rage pioneer
    with byso
    "Маша топнула ногой и взяв Константина за руку, побежала в сторону."
    ub "Куда это вы собрались, голубки?"
    play sound2 sfx_energy_door_bus volume 1
    hide mi with vpunch
    "Удар."
    "Она врезалась в невидимую стену и упала на землю."
    show image ub_normal at right with byso
    ub "Боюсь, бежать вам некуда.{w=1} Прощайтесь с жизнью."
    show mi scared pioneer at left
    hide image ub_normal
    show image ub_angry at right
    with byso
    "Катя начала медленно приближаться, покачивая ножом в ритм своих шагов."
    kt "Ты цела?"
    "Константин помог Маше встать.{w=1} Катя подходила всё ближе и ближе."
    ub "Я не думаю, что Генда будет против одной-двух смертей беглецов."
    ub "Мелочи..."
    ub "А ты..."
    hide image ub_angry
    show image ub_normal at right
    with byso
    ub "Убил мою единственную дочь."
    ub "Да ты вообще не парень, а мямля.{w=1} Тряпка."
    ub "Бесполезная трата сил родителей."
    "Константин и Маша пытались отойти от психопатки в другой угол площади."
    ub "Ты достоин любой участи, какую пожелает Господь."
    "Они искали любую возможность сбежать или контратаковать, но без толку, да и патронов в обойме не осталось."
    ub "А лучше того, чтобы ты сгнил в этой земле{w=1}. Там тебе самое место."
    hide image ub_normal
    show image ub_angry at right
    with byso
    ub "И суженная твоя тоже там лежит, в сырой яме."
    ub "Во всем виноват ты один."
    show mi rage pioneer at left with byso
    ma "Ни в чём он не виноват!{w=1} Он хороший и добрый человек!"
    hide image ub_angry
    show image ub_normal at right
    with byso
    "Катя остановилась и истерически расхохоталась."
    ub "Он кусок беспомощного дерьма!{w=1} Прямо как и ты, раз так считаешь!"
    ub "Довести свою девушку до самоубийства! {w=1}Просто уму непостижимо!"
    ub "Меня просто тошнит от тебя!{w=1} Нет, от вас обоих!"
    ub "Умрите, сукины дети!"
    play sound2 sfx_armature_swish volume 1
    hide mi
    hide image ub_normal
    show image ub_angry at center:
        zoom 1.25
        yanchor 0.1
    with vpunch
    stop sound2
    "Она набросилась на Константина с ножом пытаясь проткнуть."
    "Константин увернулся и замахнулся на неё прикладом."
    play sound2 sfx_energy_door_bus volume 1
    "{w=1}{nw}" with vpunch
    stop sound2
    "Удар."
    "Его отбросило невидимое силовое поле, которое окружало Катю."
    "Константин оступился и отскочил на несколько шагов."
    hide image ub_angry
    show image ub_normal
    with byso
    "Катя перевела взгляд на Машу."
    ub "Хм-м...{w=1} Начнём с аперитива."
    play sound2 knife_in volume 1
    hide image ub_normal
    show mi cry pioneer at left
    show image ub_angry at cleft
    with vpunch
    "В момент она подскочила к Маше и попала ножом ей в плечо."
    play sound2 horror1 volume 1
    "Маша закричала и попыталась выдернуть ножик нападающей из своего плеча, но без толку."
    ma "Нет! Больно!!!"
    "Кричала она, продолжая попытки оттолкнуть нападающую."
    hide image ub_angry
    show image ub_normal at cleft
    with byso
    ub "И что, Костя, ты ей поможешь?!"
    ub "Или как и в тот раз струсишь?!{w=1} Сбежишь?!"
    "Константин поддался провокации и попытался оттолкнуть Машу от нападающей."
    play sound2 knife_out volume 1
    hide mi with byso
    "Это удалось, плечо Маши сошло с ножа."
    hide image ub_normal
    show image ub_angry at cleft
    with byso
    ub "А теперь бери ответственность!"
    play sound2 knife_in volume 1
    hide image ub_angry
    show image ub_angry at center:
        zoom 1.25
        yanchor 0.1
    with vpunch
    "Ножик вошёл в живот Константина.{w} Адская боль пронзила позвоночник."
    ub "Вот и пришло возмездие!"
    stop music fadeout 3
    mal "Екатерина!{w=1} Прекратить произвол!"
    play sound2 knife_out volume 1
    play music PlaceInTheWorldFadesAway fadein 3
    hide image ub_angry
    show image ub_normal
    with byso
    "Катя отвела глаза и, тяжело вздохнув, вытащила ножик из живота Константина, после чего обернулась."
    play sound sfx_bodyfall_1 volume 1
    show image blood1 with byso
    "Константин упал на землю, словно пытаясь совладать с болью."
    hide image blood1
    hide image ub_normal
    show mi scared pioneer close at cright
    show image blood1
    with byso
    "Маша подбежала к нему и пыталась рукой остановить кровь."
    ma "Костя!{w=1} Не теряй сознание!"
    ma "Я тут!{w=1} Подожди, я перевяжу!"
    hide mi with byso
    scene bg ext_square_night_red:
        crop (0, 0, 1920, 1080)
        size (1920, 1080)
        linear 1 crop (497, 223, 980, 630)
    show image blood1
    pause 0.1
    hide image blood1
    show image ub_angry at right
    show image ik_sh_no at left
    show image blood2
    with byso
    "Он медленно перевёл взгляд на парня, который предотвратил его смерть."
    "Это был мальчик лет 14ти с зелёными глазами и коричневыми волосами.{w=1} Несмотря на происходящее, он выглядел весьма спокойно."
    mal "Я что сказал тебе делать?"
    ub "Помогать..."
    mal "А ты что делаешь?"
    hide image blood2
    hide image ub_angry
    show image ub_normal at right
    show image blood2
    with byso
    "Катя неловко поводила ногой по земле."
    ub "Ну мне надо было свести счёты кое с кем..."
    hide image blood2
    hide image ik_sh_no
    show image ik_sh_sur at left
    show image blood2
    with byso
    "Парень посмотрел на Константина, а затем на Катю."
    hide image blood2
    hide image ik_sh_sur
    show image ik_sh_no at left
    show image blood2
    with byso
    mal "Я предупреждал.{w=1} Ты помогаешь отцу, а я даю тебе права администратора."
    mal "Наш договор был нарушен.{w=1} Я лишаю тебя привилегии."
    play sound2 sfx_energy_door_bus volume 1
    hide image ub_normal with vpunch
    "Она с громким звуком упала на землю и отключилась, а мальчик стал приближаться к Константину и Маше."
    hide image ik_sh_no with byso
    pause 0.000001
    scene bg ext_square_night_red:
        size (1920, 1080)
        crop (0, 0, 1920, 1080)
        linear 1
    show image blood2
    pause 0.001
    hide image blood2
    show image ik_sh_no at left
    show mi rage pioneer at right
    show image blood3
    with byso
    ma "Не трогай нас!{w=1} Не смей!"
    mal "Любопытно, а что вы можете противопоставить?"
    mal "Ничего."
    mal "Вы пытались сбежать из инреальности.{w=1} Это тоже влечёт некоторые последствия."
    play sound2 sfx_armature_swish volume 1
    pause 1
    stop sound2
    "Маша выпрыгнула с места и попыталась ударить парня, но безуспешно - рука прошла насквозь."
    hide image blood3
    hide image ik_sh_no
    show image ik_sh_sur at left
    show image blood3
    with byso
    mal "Понятно."
    play sound_loop shock volume 1
    hide mi with vpunch
    "В его руке образовался электрошокер, которым он начал бить Машу."
    kt "Что ты творишь?!"
    stop sound_loop
    play sound2 sfx_bush_body_fall volume 1
    hide image blood3
    hide image ik_sh_sur
    show image ik_sh_no at left
    show image blood3
    with byso
    "Она от такого потеряла сознание и упала оземь, а мальчик тяжело вздохнул."
    mal "Что я?{w=1} Я делаю свою работу, ищу материалы для исследований.{w=1} И немного для развлечений."
    "Константин вспомнил от кого он слышал эту фразу."
    kt "Так вот ты кто...{w=1} Выродок Генды..."
    mal "Корректнее будет сказать - новый владелец инреальности.{w} Но это да, ты угадал."
    "Константин попытался встать, но не смог.{w=1} Тело его не слушалось из-за обширной потери крови."
    mal "А вы двое станете моим небольшим экспериментом... {w=1}шалостью..."
    play sound2 sfx_punch_medium volume 1
    "Он взял тазер и приложил к шее Константина."
    mal "Самому будет любопытно что из этого выйдет."
    play sound_loop shock volume 1
    scene bg ext_square_night_red at shakerrr
    show image ik_sh_no at shakerrr
    show image blood3
    "По шее побежал электрический ток."
    "Кровь начала закипать, и в памяти начали всплывать обрывки воспоминаний о прошлой жизни."
    "Боль была нестерпимой."
    "Ток, словно игла в вене, проникал в голову, выедая мозг."
    stop ambience fadeout 1
    stop sound_loop fadeout 1
    scene bg black with vpunch
    "Сознание померкло."
    pause 3
    scene bg ext_village
    show shum_white
    with byso
    ks "Дедушка, а Маша вернётся?"
    "Дед бросил папиросу в лужу и покачал головой."
    de "Прости, Костя, но я не знаю."
    de "Соседи сказали, что их родители планируют разводиться.{w=1} Маша сегодня же улетает в Японию."
    de "Вы ещё не скоро увидитесь."
    ks "А ты когда-то плавал в Японию?"
    "Дедушка прошёлся рукой по своей седой бороде, а другой похлопал Костю по плечу."
    de "Плавал-плавал, правда тебе будет лучше слетать туда на самолёте."
    de "Не беспокойся, вы обязательно когда-нибудь увидитесь вновь."
    ks "Откуда ты знаешь?"
    "Дедушка указал на дорогу, по которой они шли и улыбнулся."
    de "Или мы найдем дорогу, или мы проложим её."
    de "Всё очень просто.{w=1} Если ты и в правду хочешь с ней увидеться и приложишь к этому усилия, то ты обязательно добьёшься своего - главное не сдаваться."
    de "Просто никогда нельзя сдаваться."
    de "Запомни, никогда."
    stop music fadeout 3
    scene bg black with dissolve
    pause 1
    play music nightmare fadein 3
    play ambience ambience_rain volume 0.6 fadein 1
    scene bg ext_clubs_rain
    show unblink
    "Константин очнулся у дверей клубов.{w=1} На улице шёл дождь, а его одежда вымокла из-за погодных условий."
    "Он вытер лицо ладонью и огляделся."
    th "Чёрт возьми, где я?"
    "Вокруг было очень тихо, и это настораживало."
    "Было слышно только капли дождя, бьющие по мокрой листве."
    th "Какого хера? {w}И где Маша?"
    th "Ещё этот парень...{w=1} Ему же не взбрело в голову оставить нас в одной симуляции с Катей?"
    th "Мало ли что он подразумевал под теми экспериментами..."
    play sound2 sfx_clench2 volume 0.51
    "Константин взялся за ручку двери."
    th "Надо найти снаряжение..."
    play sound2 sfx_knock_door_closed_hard1 volume 1
    "Дверь не поддалась.{w} Была заперта изнутри."
    "Он приложил ухо к двери."
    "Изнутри доносилось нечто, похожее на установку искусственного дыхания и металлический скрежет."
    "Константин попятился."
    th "Ну нет, что бы там ни было, мне туда не надо..."
    th "Что же там такое находиться..."
    th "Нет.{w=1} В таком случае точно нельзя доверять своему любопытству...{w=1} Надо искать Машу."
    "Константин в быстром темпе направился вглубь лагеря."
    scene bg ext_square_day_rain with byso
    "На площади он остановился и посмотрел на статую.{w=1} Она совсем не изменилась."
    th "Кто бы знал, что у тебя тут есть отпрыски..."
    th "Ещё больше уродов на этой ужасной земле."
    scene bg ext_square_day_rain2 with fl_fast
    play sound2 sfx_thunder_wood volume 1
    pause 0.4
    scene bg ext_square_day_rain with byso
    "В статую ударила молния."
    "Константин, испугавшись, отпрыгнул на метр и выпучил глаза."
    th "Сука, нахуй так пугать..."
    th "Так...{w=1} Надо найти Машу..."
    stop ambience
    stop music fadeout 3
    play sound2 afterdead volume 1
    scene bg ext_square_night with flash
    play ambience ambience_forest_night volume 1 fadein 1
    "Дождь прекратился и наступила ночь.{w=1} Зажглись фонари."
    th "Это ещё что за приколы?{w=1} Даже луж не осталось?"
    "Его одежда вмиг высохла, а он направился к музклубу."
    $ volume(0.7, "music")
    play music caretaker fadein 3
    scene bg ext_musclub_night with byso
    "Из музклуба доносилась мелодия, которую Маша наигрывала на фортепиано."
    th "Вот ты где."
    "Константин сорвался в сторону здания."
    play sound2 sfx_knock_door_closed_hard2 volume 1
    "Дверь тоже была заперта."
    play sound2 sfx_knock_door6_closed
    kt "Маша, это я, открывай!"
    "Она словно не слышала ничего вне своего клуба."
    th "Тогда действую радикально."
    play sound2 door_break volume 1
    $ volume(1, "music")
    "{nw}" with vpunch
    pause 1
    scene bg piano_cg with byso
    "Константин выбил дверь сильным ударом ноги, после чего вбежал внутрь."
    kt "Маша, ты...{w=1}{nw}"
    "В клубе никого не было."
    "Мелодия исходила из фортепиано, но на нём никто не играл.{w=1} Клавиши нажимались самостоятельно."
    kt "Что за дичь?!"
    "Он подошёл и попытался нажимать на клавиши, но безуспешно, они словно были ненастоящие и нажимались исключительно в ритм проигрываемой мелодии."
    "Осознав, что это бесполезно, он отошёл от фортепиано."
    th "Надо срочно найти Машу и разобраться в этой чертовщине..."
    scene bg ext_musclub_night with byso
    "Покинув здание, Константин пошёл обратно на площадь под сопровождением всё той-же мелодии."
    "Встав на перепутье, он задумался."
    th "Да где же она может быть."
    stop music fadeout 1
    scene bg tuman with byso
    "Вокруг него начал сгущаться туман."
    "Константин помотал головой, после чего попятился."
    play sound_loop melody volume 1.2 fadein 3
    "Из бесконечного тумана начало доноситься едва-слышное пение."
    "Тихое, неясное."
    "Затем оно стало отчетливей и громче – и вскоре нарушило тишину."
    "Искаженный как бы кибернетический звук одновременно напоминал пение множества голосов – но, несомненно, был един."
    "Он проникал в самую сердцевину естества, заставляя то замирать, то проваливаться в себя, забываясь на секунду и возникая вновь."
    $ _dismiss_pause = False
    play sound "<from 8>inrealnost/Music/Amb/evil.mp3" fadein 2
    show image ma_calne:
        crop (0, 1568, 1920, 1080)
        linear 10 crop (0, 0, 1920, 1080)
    with Dissolve(10)
    stop sound_loop
    play music "<from 7>inrealnost/Music/Music/monsoon.mp3"
    $ _dismiss_pause = True
    "Пред ним предстало ужасное создание из плоти и металла."
    "Точнее... Переработанная сущность Маши."
    "Вместо рта было вмонтировано множество острых ножей, которые при пении тёрлись друг об друга."
    "Вместо глаза стоял красный диод, вместо рук ужасные острые клешни, а ноги и вовсе было не описать."
    "Маша посмотрела на Константина и наклонила голову, словно что-то вопрошая."
    kt "Маша?! Что с тобой сделали?!"
    ma_c "Такое имя не обнаружено в базе.~"
    "Словно напеваючи проскрипел механизм, прохрустев металлической рукой."
    kt "Ты меня не помнишь?!"
    "Несколько секунд она просто неподвижно смотрела на Константина и никак не реагировала."
    ma_c "Данные восстановлены.~"
    kt "Ну?{w=1} Кто я?"
    ma_c "Цель.{w=1} Уничтожить.~"
    "Константин попятился."
    kt "Что?!"
    ma_c "Убегать бессмысленно.~"
    scene bg tuman with byso
    "Он развернулся и бросился бежать."
    play sound2 slash volume 1
    show image blood1 with vpunch
    "Маша всадила ему в спину одно из своих лезвий."
    play sound "<from 3.5>inrealnost/Music/Sound/zoomer.mp3"
    scene bg ma_calne2
    show image blood1
    with byso
    "Константин разразился криком, а механизм потянул его к себе."
    kt "Что ты...{w=1} Делаешь?!"
    kt "Мне больно!"
    ma_c "Люди постоянно жалуются на боль...{w=1} а я её не чувствую.~"
    ma_c "Пришло и твоё время перестать её чувствовать.~"
    play sound2 glad volume 1
    "Он провёл своей рукой по её механизированному лицу."
    kt "Кх-х...{w=1} Маша, не..."
    play sound knife2
    show image blood2 with vpunch
    play sound_loop knife_hits volume 1
    "Она начала кромсать его лицо своими лезвиями."
    "Кожа с каждой секундой делалась бледней и прозрачней."
    "Кровь ручьем стекала по подбородку, заливая шею и грудь."
    "И в последний момент Константин осознал, что боль отступает и приходит долгожданная смерть..."
    window hide dissolve
    stop sound_loop fadeout 1
    stop music fadeout 5
    stop ambience fadeout 5
    scene bg black with dissolve5
    $ unlock_ach_root_inreal(15)
    pause 4
    play music "<from 60>inrealnost/Music/Music/Caretaker.mp3" fadein 3
    scene bg ending_TheSirenofTerror_cg:
        crop (940, 0, 980, 630)
        size (1920, 1080)
        linear 35 crop (0, 0, 1920, 1080)
    show ending_TheSirenofTerror:
        crop (940, 0, 980, 630)
        size (1920, 1080)
        linear 35 crop (0, 0, 1920, 1080)
    with Dissolve(26)
    scene bg black with byso
    stop music fadeout 3
    pause 2.6
    jump after_ending_screen
label Like_a_Star_ending:
    "Загорелись порталы. Один из них светился как-то иначе."
    show image me_no at fleft
    show mi smile pioneer at cright
    with byso
    "Из кустов вышел Семён, который был вооружён странным орудием."
    ma "Что с ним делаем?"
    play sound2 glad volume 1
    hide mi
    show mi shy pioneer close at cright
    with byso
    "Константин поднял руку Маши, в которой был пистолет и навёлся на ничего не подозревающего Семёна."
    "Прицелившись, он положил свой палец на палец Маши, который лежал на курке."
    play sound2 pistol2 volume 1
    hide image me_no with fl_fire
    kt "Бах..."
    "Патрон разорвался в шее Семёна, отделив голову от тела."
    "Хлынул фонтан крови, будто от удара саблей."
    play sound2 sfx_bush_body_fall volume 1
    "Тело убитого покачнулось и упало на колени, после чего мешком повалилось на землю."
    kt "Теперь в портал."
    "Константин и Маша взялись за руки и побежали в портал."
    show mi laugh pioneer close at cright with byso
    ma "На свободу!"
    play sound2 portal volume 1
    stop ambience fadeout 1
    stop music fadeout 3
    scene bg black with byso
    "Радостно проскандировала Маша, после чего они растворились в портале."
    pause 1
    play music deadrazy2 fadein 3
    scene bg ext_village
    show shum_white
    with byso
    ma "Слушай, Костя, а давай, когда ты приедешь, мы организуем нашу личную музыкальную группу?"
    ma "Как ты считаешь?"
    "Костя улыбнулся и покачал головой."
    ks "Не знаю, Маш.{w=1} Смешанные чувство.{w} Я умею только на гитаре пару мелодий побрынькать."
    ma "Хорошо, мало-ли надумаешь немного музыкой развлечься."
    ks "Да на самом деле если упростить, то я не умею играть вовсе."
    ma "Да ничего, я на всём играть умею.{w=1} На чем угодно научу играть, ты только попроси."
    ks "Будем считать, договорились. {w}Это может даже хорошо получиться."
    "Маша обрадовалась и крепко обняла его.{w=1} Костя ответил ей тем же."
    ma "Я рада!{w=1} Правда, рада.{w} Знаешь, здорово, если б можно было время проводить вместе."
    ks "Вот приедем к тебе в гости, тогда и обсудим. {w=1}Не обещаю, конечно, но постараюсь."
    ma "Хорошо... {w=1}А вот и твой участок?"
    ks "Да, дедушка скорее всего уже заждался.{w=1} До вечера!"
    ma "До встречи.{w} Давай... {w=1}И подумай об этом хорошенько."
    stop music fadeout 2
    scene bg black with dissolve
    pause 1
    play music PerfectGirl fadein 3
    scene bg server1
    show unblink
    "Константин и Маша очнулись держащимися за руке в неком серверном помещении."
    "Всё вокруг светилось зелёным.{w=1} При этом, ни один из огромных шкафов не издавал какого-либо шума."
    show mi upset pioneer with byso
    kt "Вот как ты выглядишь... Административная симуляция..."
    kt "Так, ищем куда всунуть флешку."
    scene bg server2 with byso
    "Встав, они обратили внимание на компьютер, который практически ничем не отличался от любой другой техники в помещении."
    ma "Может это?"
    "Константин вытащил флешку и подошёл к компьютеру."
    "На его верхней крышке как раз был необходимый разъём."
    kt "Как удобно...{w=1} USB разъёмы - вещь!"
    play sound2 sfx_click_1 volume 1
    "Вставив накопитель, он посмотрел на монитор."
    gt4 "Обнаружено новое оборудование проверяю на вредо...{w=1}{nw}"
    play sound2 power volume 1
    scene bg server3 with bso
    scene bg server2 with bso
    scene bg server3 with bso
    scene bg server2 with bso
    "Голос прервался. Всё в серверной пару раз мигнуло."
    gt4 "Адаптивная поисковая программа активирована. Выполняю установленный протокол."
    gt4 "Обнаружены административные сессии. Завершаю."
    gt4 "Примерное время ожидания - 1 минута."
    scene bg server1
    show mi shy pioneer close
    with byso
    "После этого компьютер слегка зашумел, а Константин перевёл взгляд на Машу."
    "Она стояла в нескольких сантиметрах от него, держа в руках пистолет."
    "Обняв Константина, Маша заглянула в его карие глаза."
    "Без слов они поняли друг друга и их губы начали сближаться."
    "Медленно, нежно и неторопливо."
    show mi shocked pioneer close with byso
    mal "Так-так-так..."
    hide mi
    show mi shocked pioneer at left
    show image ik_sh_no at right
    with byso
    "Они резко обернули свои головы в сторону голоса."
    "Там стоял мальчик лет 14ти с зелёными глазами и коричневыми волосами."
    "Несмотря на происходящее, он выглядел весьма спокойно."
    mal "И чего вы тут забыли?{w=1} Вы знаете, что вам тут не место?"
    show mi dontlike pioneer at left with byso
    kt "Малой, не твоё собачье дело!{w=1} Откуда ты тут вообще взялся?"
    show mi angry pioneer at left with byso
    "В его руках образовался электрошокер.{w=1} Он начал постепенно приближаться."
    mal "А вот это, как ты говоришь, действительно не твоё собачье дело."
    show mi angry pioneer at left
    hide image ik_sh_no
    show image ik_sh_sur at right
    with byso
    "Маша прицелилась в мальчика, а тот за секунду остановился."
    ma "Не двигайся!{w} Иначе я выстрелю!"
    mal "Ну, попробуй.{w=1} Я подо...{w=0.241}{nw}"
    play sound2 sfx_energy_door_bus volume 1
    hide image ik_sh_sur
    show mi shocked pioneer at left
    with vpunch
    play sound power volume 1
    scene bg black with bso
    scene bg server1
    show mi shocked pioneer at left
    with bso
    scene bg black with bso
    scene bg server1
    show mi shocked pioneer at left
    with bso
    "Вдруг, мальчика отбросило в сторону.{w=1} Серверное оборудование снова помигало."
    gt4 "Административные сессии завершены.{w=1} Приступаю к выполнению основной задачи."
    gt4 "Примерное время ожидание - 5 минут."
    mal "Ах вы..."
    show mi dontlike pioneer at left with byso
    "Мальчик попытался встать, но безуспешно."
    kt "Так вот кто ты...{w=1} Марионетка Генды."
    mal "Я его сын..."
    play sound2 ammo volume 1
    "Прорычал мальчик, пытаясь встать.{w=1} Маша наставила на него пистолет."
    show mi grin pioneer at left with byso
    ma "Тогда это будет наш прощальный подарок.{w=1} Мы сваливаем отсюда."
    ma "Мы не хотим получить нож в спину.{w} Уж прости."
    kt "Ты наверняка не много повидал в жизни, но это уже и не наше дело."
    ma "Не стоило вставать у нас на пути.{w=1} Теперь прощай."
    "Маша начала медленно наживать на курок, словно растягивая момент."
    play sound2 pistol2 volume 1
    scene bg black with vpunch
    "Выстрел."
    pause 1
    scene bg ma_concert
    show unblink
    stop music fadeout 3
    "Маша засолировала последний аккорд на электрогитаре и улыбнулась публике."
    play music regret fadein 3
    play sound2 sfx_concert_applause volume 1
    ma2 "Мы так рады, что вы все собрались на нашем концерте!"
    kt "Вам понравилось?!"
    scene bg ma_concert1 with byso
    "Фанаты практически синхронно проскандировали <<Да>>.{w=1} Константину вынесли гитару, а Маша взмахнула рукой."
    ma2 "Наш концерт подходит к концу и теперь вы услышите завершающий трек!"
    kt "Сейчас, дорогие фанаты, вы услышите нашу самую известную песню - <<Моя оборона>>!"
    ma2 "Вы готовы?!"
    play sound2 sfx_concert_applause volume 1
    "Зал не скрывая своей радости аплодировал и насвистывал, ожидая красивого завершения вечера."
    stop music fadeout 2
    stop sound2 fadeout 1
    "Всё затихло.{w=1} Константин повесил на себя гитару и посмотрел на Машу."
    kt "Раз-два-три!"
    scene bg ma_concert2 with byso
    play music "<from 3>inrealnost/Music/Music/mi_sing.mp3" fadein 1
    "Маша начала исполнять песню, которую они придумали в инреальности."
    "Эта песня была буквально хитом на современном радио и слушатели, снимая концерт на камеру, качали телефонами в такт песни."
    window hide dissolve
    pause 1
    $ set_mode_nvl()
    "<<Changing memories>>."
    "Именно так назвалась группа, которую создали Константин и Маша."
    "Они специализировались на электро-психоделике и металле, но не редко давали такие расслабляющие концерты."
    "Фанаты охотно покупали клубные билеты, с интересом вслушивались в новые творения гениев, особенно стараясь попасть на их сольники."
    "Да, жанр весьма специфический, но именно в нём им удавалось передавать слушателю то, через что они смогли пройти вместе."
    "До и после инреальности."
    "В основном, это были короткие музыкальные отрывки, где они объединялись, чтобы создать что-то необычное."
    "Нередко, в их рецензиях писали, что их музыка сходна с настоящей симфонией зла, обволакивающей с ног до головы."
    "При том, подобные концерты, проходящие на крупной сцене, описывались как подлинная кульминация бытия."
    "Параллельно, популярность подобных мероприятий росла. Информация о них часто появлялась в интернете."
    "Публика, как одна большая семья, могла ознакомиться с их творчеством за один вечер."
    "Что же касалось самих Константина и Маши, они открыли в себе странный талант, о котором никто ничего не знал."
    "Творить музыку."
    "Это была целая наука, состоящая из хаоса звуков, которые складывались из нот, а иногда из отдельных слов."
    "Каждое своё творение они наделяли любовью и приятным голосом Маши.{w=1} Даже Константин оказался вовлечённым в мир людей."
    "В целом, они оба достигли какого-то совершенно нового для себя единства."
    "Пространство между ними становилось живым миром."
    "Похоже, все вокруг обрело ценность, стало их собственным."
    "Одним словом, пришло долгожданное счастье, на которое никогда прежде они не рассчитывали."
    window hide dissolve
    pause 1
    $ set_mode_adv()
    stop music fadeout 3
    "Константин сыграл последний аккорд."
    play sound2 sfx_concert_applause volume 1
    play music "<from 177>inrealnost/Music/Music/KawuSun.mp3" volume 1 fadein 3
    "Зал разразился аплодисментами."
    scene bg ma_concert1 with byso
    ma2 "Чтож, дорогие фанаты, мы были рады вновь поделиться с вами нашим творчеством."
    kt "Совсем скоро мы увидимся вновь с новым альбомом.{w=1} Не пропустите наш новый концерт!"
    ma2 "Прощайте и до скорых встреч!"
    kt "Занавес!"
    show blink
    "Артисты переглянулись, подошли друг к другу и под бурные аплодисменты поцеловали друг друга."
    stop ambience fadeout 5
    window hide dissolve
    $ unlock_ach_root_inreal(16)
    pause 1.5
    scene bg ending_Like_a_Star_cg:
        crop (940, 450, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    show ending_Like_a_Star:
        crop (940, 450, 980, 630)
        size (1920, 1080)
        linear 26 crop (0, 0, 1920, 1080)
    with Dissolve(25)
    scene bg black with byso
    stop music fadeout 3
    pause 2.6
    jump after_ending_screen