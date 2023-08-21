label d3_withmz:
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
        jump fdafdafdsfasgfgdffdafdsgdrfgfdgs4regfdsvgc
    else:
        scene bg bgcg6
        show load
        with byso
        pause 10
        $ bgcg -= 1
        window show
        jump fdafdafdsfasgfgdffdafdsgdrfgfdgs4regfdsvgc
label fdafdafdsfasgfgdffdafdsgdrfgfdgs4regfdsvgc:
    $ save_name = ('Инреальность.\nДень третий.')
    scene bg int_house_of_mt_sunset
    show unblink
    play music music_list["torture"] fadein 3
    th "Угх.{w}.. Привыкать надо к такому утру.{w} Ещё и кулаки болят..."
    show mt angry pioneer with byso
    play sound sfx_bed_squeak2
    "Константин глянув на окровавленные бинты опёрся локтями на кровать.{w} За столом сидела вожатая и сверлила Константина взглядом."
    kt "Э-эм, доброе утро?"
    mt "Доброе-доброе.{w} Вставай и собирайся."
    "Злобно озвучила вожатая и перевела взгляд на бумаги."
    th "А чё в смысле?"
    kt "Не понял?"
    mt "Тебя сегодня ждёт автобус и увозит в город за нарушение правил лагеря.{w} Толик мне доложил что ты и Женя пили алкоголь."
    th "А.{w}.. Ага.{w}.. Какой вообще город?{w} Это же не мой мир..."
    mt "Так что ты, как и Женя, отправляетесь сегодня после завтрака.{w} До него можешь зайти в медпункт."
    play sound sfx_bed_squeak1
    "Константин встал с кровати и оделся."
    show mt sad pioneer with byso
    mt "Пионерский наряд, так и быть, можешь оставить себе."
    th "Ладно, плевать. Вроде как не один еду, так что не умру.{w}.. Наверное..."
    th "Да даже если и так, то без разницы."
    "Константин взял рюкзак и направился на выход из домика."
    show mt rage pioneer with byso
    mt "Стоять!"
    "Константин тяжело вздохнул и остановился."
    kt "Что ещё?"
    show mt angry pioneer with byso
    "Константин медленно развернулся и посмотрел на вожатую. Сахарова очень сильно злилась."
    mt "То есть ты даже не извинишься за своё поведение?"
    "В ответ он лишь рассмеялся."
    kt "Эх, Сахарова-Сахарова.{w}.. Ничем ты не изменилась.{w} Всё та же тупая и ленивая скотина, которая даже не желает понимать свою ответственность."
    show mt rage pioneer with byso
    mt "Да как ты смеешь!.."
    kt "Что, правда в глаз попала?{w} Я даже и не начал оглашать полный список твоих грехов."
    kt "Сама то как думаешь?{w} Тебе 24 года, а у тебя всё ещё нет даже намёка на отношения.{w} Почему?"
    show mt shocked pioneer with byso
    "Константин попал в самое больное место.{w} Вожатая была ошеломлена словами Константина, а он подошёл поближе."
    kt "Так это потому что ты что в <<Полимере>>, что тут лишь дегенеративная сука, которая всё что и может так это лениться и распиливать бюджет."
    kt "Если бы у тебя не было более-менее сносной внешности и груди шестого размера, то на тебя бы вообще никто не посмотрел."
    "Константин сделал ещё шаг в сторону Ольги."
    kt "Так бы и осталась."
    "Он шагнул ближе."
    kt "{cps=10}Жалкой.{/cps}"
    "Он продолжил приближаться."
    kt "{cps=7}Старой.{/cps}"
    "Встав почти вплотную к Сахаровой он растянул последнее слово."
    kt "{cps=3}Девой.{/cps}"
    play sound sfx_pat_shoulder_hard
    show mt scared pioneer with byso
    "Очнувшись, Сахарова хотела дать Константину пощёчину, но тот поймал её руку."
    kt "А вот драться не стоит. То что я внешне был более порядочный не означает то что я не бью девушек."
    "Константин отпустил руку бывшей вожатой."
    kt "В новой жизни увиделись, но на этот раз больше не увидимся никогда."
    stop music fadeout 2
    play sound door_cl
    play ambience ambience_camp_entrance_day
    scene bg ext_house_of_mt_sunset with byso
    "Сквозь зубы проскрипел он и покинул домик."
    play sound light_inh
    play music music_list["that_s_our_madhouse"] fadein 2
    "Достав из кармана сигареты, он закурил."
    th "Хотя... То что я уезжаю имеет свои плюсы."
    th "Всегда хотел высказать Сахаровой всё что про неё думал."
    scene bg ext_houses_sunset with byso
    "Константин шёл по лагерю, покуривая сигарету с фруктовой кнопкой.{w} Пионеры разных отрядов то и дело озирались на него."
    th "Хе-хе, уже все завидуют."
    scene bg ext_aidpost_day
    show mz bukal pioneer glasses far at right
    show un normal pioneer far at left
    with byso
    "Дойдя до медпункта, он встретил сидящих на ступеньках медпункта Лену и Женю."
    hide mz
    hide un
    show mz laugh pioneer glasses at right
    show un surprise pioneer at left
    with byso
    "Заметив Константина с сигаретой в зубах, у Лены отвисла челюсть, а Женя рассмеялась."
    mz "Ха-ха-ха-ха, знай наших!"
    un "Ты чего в лагере куришь?"
    stop music fadeout 3
    "Константин сделал последнюю затяжку и затоптал сигарету."
    kt "Ну я.{w}.. Что я? Уезжаю, как и Женя."
    "Лена ещё сильнее удивилась."
    un "Как это?!"
    show mz bukal pioneer glasses at right with byso
    mz "Да, нас выгнали за распитие алкоголя, потому мы после завтрака уедем."
    show un sad pioneer at left with byso
    un "А как же библиотека?"
    show mz bukal pioneer at right with byso
    "Женя достала из своей сумки тряпочку и протёрла очки."
    mz "Не знаю. Выходи из литературного, одна не вывезешь."
    un "Придётся.{w}.. Буду Виоле помогать."
    show un smile pioneer at left
    show mz bukal pioneer glasses at right
    with byso
    un "Кстати, Костя, тебе перевязать бинты?"
    kt "Да, было бы неплохо."
    scene bg int_aidpost_day
    show un smile pioneer at right
    show mz normal pioneer glasses at left
    with byso
    stop ambience
    play sound door_cl
    play music music_list["farewell_to_the_past_full"] fadein 3
    "Они вошли в медпункт. Константин сел на кушетку, Женя встала у окна, а Лена села на стул Виолы."
    show mz smile pioneer glasses at left with byso
    mz "Ну, зато будешь на шаг ближе к мечте. Чтоб стать хорошим психологом, тебе надо знать и биологию."
    play sound sfx_open_table
    "Лена тяжело вздохнула и достала из ящика бинты."
    show un sad pioneer at right with byso
    un "Как сказать. Словно я биологию не знаю.{w} Давай руку."
    "Константин протянул Лене руку и она начала аккуратно снимать старый бинт."
    kt "Может тебе понравится врачебное дело?"
    show un smile pioneer at right with byso
    "Лена легко улыбнулась."
    un "Может и так, почему нет."
    show un normal pioneer at right with byso
    "Сняв бинты, Лена полила руку Константина перекисью."
    show mz normal pioneer glasses at left with byso
    mz "Жжётся наверное."
    kt "Да нет, кожа уже более-менее восстановилась."
    show un sad pioneer at right with byso
    un "Это хорошо.{w} Главное чтоб не было сломанных костей."
    kt "Меня сложно сломать!"
    show un grin pioneer at right
    show mz smile pioneer glasses at left
    with byso
    "Непринуждённо пошутил Константин, Лена и Женя усмехнулись."
    show un smile pioneer at right with byso
    un "Да-а, тяжело мне будет без вас..."
    show mz bukal pioneer glasses at left with byso
    mz "Вот я и говорю, бросай библиотеку к чертям. Оно тебе не надо."
    show un sad pioneer at right with byso
    un "Я не в этом смысле. С тобой я знакома несколько смен, мне в принципе больно с тобой разъезжаться, а с Костей я только начала общение..."
    window hide
    menu:
        "Успокоить Лену.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            show un shy pioneer at right
            show mz smile pioneer glasses at left
            with byso
            play sound sfx_punch_medium
            "Константин взял Лену за руку.{w} Лена вмиг окрасилась красным."
            kt "Ничего страшного, ещё увидимся.{w} Обязательно увидимся в будущем."
            mz "Да, не грусти. Когда нибудь ещё пересечёмся."
            show un laugh pioneer at right with byso
            "Лена искренне улыбнулась."
            un "Ловлю на слове."
            "Проговорила Лена и продолжила накладывать бинт."
        "Промолчать.":
            $ renpy.block_rollback()
            show mz smile pioneer glasses at left with byso
            mz "Не грусти. Когда нибудь ещё пересечёмся."
            show un grin pioneer at right with byso
            "Лена слабо улыбнулась."
            un "Ловлю на слове..."
            "Выдохнула Лена и продолжила накладывать бинт."
    play sound sfx_open_table
    "Закончив с бинтами, Лена обрезала ненужную часть и убрала на место."
    show un smile pioneer at right with byso
    un "Вот и всё."
    show mz bukal pioneer glasses at left with byso
    play sound sfx_dinner_horn_processed
    stop music fadeout 7
    "На улице прозвучал горн."
    mz "А вот и еда.{w} Есть конечно не особо охота, но перед дорогой стоило бы."
    mz "Потом ещё сходим в библиотеку, мне надо кое-что забрать."
    "Женя глянула на Лену."
    mz "И тебе прощальный подарочек оставить."
    show un grin pioneer at right with byso
    un "Хах, мило."
    play sound door_cl
    play ambience ambience_camp_entrance_day
    play music music_list["gentle_predator"]
    scene bg ext_aidpost_day
    show mz bukal pioneer glasses at right
    show un smile pioneer at left
    show cs smile
    with byso
    "На выходе из медпункта их встретила Виола."
    cs "Пионер!{w} Ты чего своей вожатой наговорил?"
    kt "Ну-у, что думал то и сказал."
    show cs normal with byso
    "Виола немного разозлилась."
    cs "То есть ты хочешь сказать, говорить женщине что она помрёт старой девой это нормально?!"
    show mz laugh pioneer glasses at right with byso
    "Женя взорвалась от смеха, Лена же пыталась оставаться серьёзной, но получалось это плохо."
    kt "Н-да, знали бы вы что она за человек, то сказали бы точно так-же."
    show un laugh pioneer at left with byso
    "На этом моменте засмеялась и Лена, а у Жени была истерика такой силы, что она чуть не забыла как дышать."
    cs "Это низко..."
    hide cs with byso
    stop music fadeout 3
    "Поучила медсестра и ушла в медпункт."
    "Женя еле-еле заставила себя перестать смеяться."
    show un smile pioneer at left with byso
    un "Ну ты даёшь.{w}.. Ты что ей правда так сказал?"
    "Константин ухмыльнулся и пожал плечами."
    kt "Как видишь."
    show mz smile pioneer glasses at right with byso
    mz "Фу-у-ух, ну ты псих конечно.{w}.. Исключительно в хорошем смысле слова."
    play music music_list["heather"]
    scene bg ext_dining_hall_near_day
    show mz bukal pioneer glasses at right
    show un normal pioneer at left
    show mt angry panama pioneer
    with fade
    "У столовой их встретила вожатая, что пыталась игнорировать присутствие Константина."
    mt "Женя, ты собралась?"
    show mz angry pioneer glasses at right with byso
    "В ответ она недовольно сверкнула очками и глянула на Сахарову."
    mz "А по мне не видно?"
    show un surprise pioneer at left
    show mt rage panama pioneer
    with byso
    "Вожатая сильно вспылила. Лена прикрыла лицо рукой."
    mt "Как ты со старшими общаешься?!"
    show mz rage pioneer glasses at right
    show mt shocked pioneer panama
    with byso
    mz "Как хочу, так и общаюсь!{w} Не сильно то вы меня старше!"
    mz "Так что будьте добры, идите и хавайте свою баланду, а ещё ищите нового библиотекаря!"
    show mz bukal pioneer glasses at right
    show un normal pioneer at left
    with byso
    stop music fadeout 3
    un "Всё, Женя, идём."
    play ambience ambience_dining_hall_full
    scene bg int_dining_hall_people_day
    show mz bukal pioneer glasses at right
    show un normal pioneer at left
    with byso
    "Вожатая осталась в ступоре, а члены литературного встали на раздачу."
    show mz angry pioneer glasses at right with byso
    mz "Кругом одни идиоты, чесслово."
    "На завтрак им выдали чай каркаде и тарелку гречки на молоке."
    show un sad pioneer at left with byso
    un "М-да, у вожатой сегодня явно плохой день."
    kt "Да-да. Ей ещё разбираться с библиотекой."
    show mz smile pioneer glasses at right with byso
    mz "Мгм, куда она без нас."
    play music music_list["glimmering_coals"]
    el "Женя!"
    show mz bukal pioneer glasses at right
    show un angry2 pioneer at left
    show el fingal pioneer
    with byso
    "Улыбка Жени сошла на нет, Лена тяжело вздохнула, а Константин подпёр подбородок рукой."
    "Подошёл Электроник. Виола его конечно подлатала, но он так и не восстановился полностью."
    el "Мне сказали что ты сегодня уезжаешь. Мне жаль что так вышло. Я хотел тебе сказать что я тебя..."
    show mz angry pioneer glasses at cright
    show un surprise pioneer at left
    with byso
    play sound sfx_face_slap
    "Женя встала со стула и влепила Электронику леща." with vpunch
    mz "Заткнись уже хоть на минуту!{w} Как Славя ходит-ходит, бубнит на ухо!{w} Да я уеду и наконец с тобой больше не увижусь!{w} Ой, а знал бы ты насколько я рада!"
    mz "Уйди с глаз моих долой, баран!"
    kt "Тебе вчерашнего было мало?"
    hide el
    show mz bukal pioneer glasses at right
    with byso
    "Электроник не нашёл что сказать и ушёл. Женя села на место."
    show un sad pioneer at left with byso
    un "М-да..."
    show mz normal pioneer glasses at right with byso
    mz "Ну, в том что я сваливаю есть и плюсы.{w} Могу высказать всё что накопилось."
    kt "Да, это полезно временами бывает, рекомендую. Вожатая до сих пор не может оклематься."
    stop music fadeout 3
    "Закончив с гречкой Константин начал допивать чай."
    th "А всё-таки интересно, куда мы попадём..."
    show un smile pioneer at left with byso
    un "Ну что, идём в библиотеку?"
    show mz bukal pioneer glasses at right with byso
    mz "Да, идём... Всё равно мне испортили аппетит."
    play ambience ambience_camp_entrance_day
    play music music_list["a_promise_from_distant_days_v2"]
    scene bg ext_dining_hall_near_day
    show mz normal pioneer glasses at left
    show un normal pioneer at right
    with byso
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
    mz "Классный стих, Лен. Ты не рассказывала его до этого."
    show un sad pioneer at right with byso
    un "Искала подходящий момент. Не такой конечно, но как вышло так вышло."
    show mz bukal pioneer glasses at left with byso
    mz "М-да-а."
    play sound sfx_unlock_medpunkt_door
    hide mz with byso
    "Женя открыла библиотеку и вошла."
    play sound3 door_cl
    stop ambience
    scene bg int_library_day
    show mz bukal pioneer glasses at left
    show un sad pioneer at right
    with byso
    play sound sfx_open_table
    play sound2 sfx_paper_bag
    "В библиотеке она открыла ящик своего стола и собрала свои бумаги."
    show mz normal pioneer glasses at left with byso
    mz "Будет хоть о смене память.{w} Слушай, Лен, а ты не против мне на карточке подпись поставить?"
    show un laugh pioneer at right with byso
    un "Давай, где писать?"
    show mz smile pioneer glasses at left with byso
    "Женя достала из сумки фотографию ворот лагеря."
    mz "Вот, рисуй."
    "Лена взяла ручку и поставила свою подпись."
    mz "Спасибо.{w} Вот ключи."
    show mz laugh pioneer glasses at left with byso
    play sound sfx_keys_rattle
    "Женя достала из кармана ключи и передав Лене усмехнулась."
    mz "Загляни потом в подвал, там пара подарочков от меня."
    show un smile pioneer at right with byso
    un "Посмотрю."
    show mz bukal pioneer glasses at left with byso
    mz "Ну а теперь в последний путь?"
    show un sad pioneer at right with byso
    "В глазах Константина это утверждение звучало скорее в прямом, чем в метафорическом смысле."
    kt "Ага."
    un "Идём..."
    play sound door_cl
    play ambience ambience_camp_entrance_day
    stop music fadeout 2
    scene bg ext_library_day
    show mz bukal pioneer glasses at left
    show un sad pioneer at right
    with byso
    "Женя вышла из библиотеки и глубоко вдохнула."
    play music music_list["tried_to_bring_it_back"] fadein 1
    mz "А всё из-за этой Сахаровой.{w} Не в планах у меня было так рано уезжать."
    show un normal pioneer at right with byso
    un "Да ладно тебе Жень.{w}.. Ситуация конечно так себе, но всё-же. Она просто свой долг исполняла."
    show mz angry pioneer glasses at left with byso
    mz "Да мне без разницы. Долг-долг, мне то какое дело?"
    mz "Вот как отцу в глаза смотреть я не знаю..."
    kt "Ничего, выкрутишься. Скажи что тебя сдали."
    show mz bukal pioneer glasses at left with byso
    "Женя глянула на Константина."
    mz "Так и было, меня походу Толик заложил, он единственный видел как я от бутылки избавлялась."
    kt "А, вот оно что.{w} Да, так и есть, мне Сахарова сказала что нас Толик спалил."
    show un angry2 pioneer at right with byso
    "Лена немного нахмурилась.{w} Константин понял что Толику уже несдобровать."
    un "Ну ничего, я ему припомню."
    scene bg ext_camp_entrance_day
    show mz normal pioneer glasses at left
    show un smile pioneer at right
    with fade
    "Выйдя на остановку, они встали у ворот. Константин достал сигареты и раздал по одной."
    mz "Спасибо."
    un "Благодарю."
    show mz bukal pioneer glasses at left with byso
    mz "Ты что, куришь?"
    show un normal pioneer at right with byso
    un "Иногда.{w} Сейчас я не против."
    play sound light_inh
    "Они зажглись и стояли курили возле памятника пионеру."
    show mz normal pioneer glasses at left with byso
    mz "Автобус должен быть с минуты на минуту..."
    show un sad pioneer at right with byso
    "Лена достала из кармана закладку с подписью <<Санкт-Петербург>>."
    un "Я забыла тебе отдать, держи."
    show mz smile pioneer glasses at left with byso
    "Женя отмахнулась и улыбнулась."
    mz "Оставь себе.{w} Вспоминать будешь про меня."
    show un cry_smile pioneer at cleft with byso
    "Лена улыбнулась и обняла Женю."
    un "Спасибо. Буду хранить."
    mz "Да-да, только рубаху мне не сожги."
    "С усмешкой подметила Женя и выкинула окурок."
    play sound sfx_bus_stop
    play ambience sfx_bus_idle
    show un cry_smile pioneer at right with byso
    "Подъехал автобус, но на этот раз в нём сидел водитель и с приветливым лицом глянул на пионеров.{w} Константин и Лена выкинули бычки."
    un "Ладно, прощайте."
    "Лена ещё раз обняла Женю."
    hide un
    show un cry_smile pioneer
    with byso
    "Отойдя от Жени, Лена подошла к Константину."
    un "Ты не против?"
    kt "Не против."
    hide un
    show un cry_smile pioneer close
    with byso
    "Константин обнял Лену."
    kt "Ещё увидимся."
    show image oleg_smile at right
    hide un
    show un cry_smile pioneer close
    with byso
    "Из автобуса вышел водитель."
    olegp "Это очень мило, но Евгению и Константина прошу на борт."
    hide un
    show un cry_smile pioneer
    with byso
    stop music fadeout 3
    "Константин отпустил Лену."
    kt "Аревуар."
    un "Бон вояж."
    show un smile pioneer with byso
    "Пожелала Лена и помахала рукой."
    mz "Прощай."
    play music music_list["afterword"]
    scene bg int_avtobus
    show mz normal pioneer glasses
    with byso
    "Женя и Константин вошли в автобус и сели на места."
    th "А это не Икарус.{w}.. Хотя внешне похож..."
    play ambience bus_inside fadein 1
    play sound sfx_ikarus_open_doors
    $ volume(0.2, "ambience")
    "Автобус начал движение. Лена пустила слезу и махала рукой, а с территории лагеря выбежал Электроник."
    mz "Фух, вот и всё. Наконец эти шарады закончились...{w} Олег! Нам далеко ехать?"
    show mz bukal pioneer with byso
    "Крикнула Женя и сняла очки. Понимание Константином ситуации постепенно пропадало."
    oleg "Ща, маршрут проложу."
    play sound korobka_peredach
    "Ответил некий Олег и заскрипел коробкой передач."
    kt "Вы про что?"
    "Женя потёрла переносицу и достала из сумки бежевый свитер."
    mz "Ах, да. Ты не в курсе.{w} Сейчас всё расскажем."
    hide mz with byso
    show image liz_bukal with byso
    play sound sfx_blanket_off2
    "Женя надела на себя свитер и расстелила на свободной от кресел задней площадке небольшой плед."
    mz "Садись.{w} Сейчас Олег закончит развлекаться с трансформатором и мы всё тебе расскажем."
    hide image liz_bukal
    show image poter_n_p at left
    show image liz_bukal
    with byso
    play sound par
    pp "Эй, а вы куда его везёте?{w} Он не должен покидать эту симуляцию!"
    hide image liz_bukal
    show image liz_dontlike
    with byso
    "В автобусе материализовался потерянный пионер.{w} Женя косо глянула на него."
    mz "Оле-ег! У нас неприятности, тащи плазмоинтегратор."
    oleg "Чего?!"
    show image oleg_angry at right with byso
    "С рулевого места выскочил водитель с чем-то наподобие винтовки наперевес и навёлся на пионера."
    pp "Воу-воу, спокойно, опусти пу..."
    play sound magic
    hide image poter_n_p
    hide image oleg_angry
    hide image liz_dontlike
    show image oleg_think at right
    show image liz_bukal at left
    with fl_scare
    stop music fadeout 3
    play sound2 sms
    "Не долго думая Олег пальнул красным лучом из винтовки по пионеру, отчего он растворился, а странный аппарат пиликнул."
    kt "Ты чего делаешь?!"
    play music god fadein 3
    oleg "Вы откуда этого товарища подобрали?{w} Он своей энергией интегратор напрочь разрядил."
    hide image liz_bukal
    show image liz_rage at left
    with byso
    "Женя прикрыла лицо рукой."
    mz "Придурок, сколько раз я тебе говорила не экономить на интеграторах энергию!"
    mz "Ничего тебя после случая с банши не учит, да?!"
    "Константин лишь ошеломлённо следил за происходящим."
    hide image oleg_think
    show image oleg_angry at right
    with byso
    oleg "Да не гони на меня! Интегратор был заряжен на сотку!"
    mz "Ага, так я тебе и поверила!"
    oleg "Клянусь! Как приедем по протоколам посмотришь!"
    hide image liz_rage
    show image liz_angry at left
    hide image oleg_angry
    show image oleg_think at right
    with byso
    mz "Всё, забыли."
    hide image liz_angry
    show image liz_bukal at left
    with byso
    "Женя глянула на Константина."
    mz "А, точно.{w} Ты маршрут настроил?"
    hide image oleg_think with byso
    oleg "Не успел. {w}Момент."
    hide image liz_bukal
    show image liz_smile
    with byso
    mz "Не обращай внимания на этот нонсенс.{w} Бывает так сказать."
    kt "Вы что сделали с потерянным?"
    hide image liz_smile
    show image liz_surp
    with byso
    "Женя глянула в угол автобуса, где образовался пионер."
    mz "А, этого то.{w}.. В кошмар отправили на время.{w} Ты его знаешь?"
    kt "Да, он говорил что может мне помочь."
    hide image liz_surp
    show image liz_surp at right
    show image oleg_smile at left
    with byso
    oleg "Да-да, все они так говорят, а потом твой пепел уже в урну собирают."
    "Встрял в диалог Олег и вышел с водительского места."
    oleg "Всё.{w} Ехать нам дохера времени, мы на другом конце инреалки, так что есть время всё обсудить."
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    "Заявил он, по-турецки сел на плед и протянул Константину руку."
    oleg "Так, ты должно быть Константин.{w} Я Олег. Четвёртый лейтенант сопротивления, приятно познакомиться."
    play sound sfx_face_slap volume 0.7
    hide image liz_surp
    hide image oleg_happy
    show image liz_angry at right
    show image oleg_shy at left
    with vpunch
    "Женя дала Олегу подзатыльник."
    oleg "Ау, за что?!"
    mz "Да он даже не знает что такое симуляция, а ты ему про какие-то сопротивления рассказываешь."
    "Константин пожал руку Олегу."
    kt "Рад знакомству."
    hide image oleg_shy
    show image oleg_smile at left
    with byso
    oleg "Замечательно."
    hide image liz_angry
    show image liz_bukal at right
    with byso
    mz "Короче.{w} Меня не Женя зовут на деле. Я Лиза. {w}То было прикрытие для симуляции."
    liz "Давай по порядку. Олег, расскажи ему про сопротивление."
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Значит смотри.{w} Есть Генда. Знаешь такого?"
    kt "Да, видел его, а что?"
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    "Олег улыбнулся и глянул на Лизу."
    oleg "Молодец, толкового парня нашла!"
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    "Переведя взгляд на Константина, он продолжил."
    oleg "Короче, это всё вокруг тебя - инреальность.{w} Сейчас мы находимся в одной из симуляций. Всеми ими в разной мере управляет тот мужик в очках."
    oleg "Как ты наверное уже знаешь, Генда тот ещё подонок.{w} Он делает из людей слуг, а позже их использует в своих целях, что собственно называет исправлением."
    oleg "Но я думаю тебе не нужно объяснять что на деле это не исправление, а порабощение."
    oleg "И есть мы - сопротивление.{w} Мы стараемся отбить у Генды инреальность и отстроить в ней новый мир, свою цивилизацию."
    oleg "Предводительствует нами капитан Андрей.{w} Он был одним из первых кто сюда попал и благодаря неустойчивости систем Генды образовал сопротивление."
    oleg "Мы с Лизой состоим в отряде спасения и периодически проходим в симуляции чтоб найти одиночек, которые могли бы присоединиться."
    oleg "Сейчас мы на пути в симуляцию сопротивления. {w}Ты теперь один из нас."
    kt "Чего?"
    play sound out_vosp
    scene bg int_avtobus2
    hide image oleg_happy
    hide image liz_bukal
    show image liz_normal at right
    show image oleg_smile at left
    with dissolve
    "Лиза глянула в окно, на улице стемнело. Константин удивлённо поморщился и покрутил головой."
    oleg "О, выехали из твоей симуляции."
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Советую тебе к нам присоединиться, либо Андрей тебя выбросит в другую симуляцию."
    kt "А, то есть меня никто не хотел оповестить о подобном входе во фракцию?"
    hide image oleg_happy
    show image oleg_think at left
    with byso
    "Олег почесал затылок и пожал плечами."
    oleg "Ну, по крайней мере ты первый кто начал этому возмущаться."
    th "Н-да..."
    kt "Ладно, хренли делать..."
    hide image liz_bukal
    show image liz_smile at right
    with byso
    liz "Правильный выбор.{w} Как первый лейтенант назначаю тебя сержантом и бла-бла-бла."
    kt "А какая иерархия и что она означает?"
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "Значит смотри.{w} Порядок у нас такой: рядовой-ефрейтор-сержант-прапор-лейтенант-капитан."
    hide image liz_smile
    show image liz_normal at right
    with byso
    liz "Поскольку я тебя знаю и у тебя есть навыки, то я тебя сразу назначаю сержантом.{w} Подчинённых у тебя пока что не будет, но тем не менее это лучше чем рядовой."
    stop music fadeout 3
    kt "М-да..."
    liz "Означает она что у тебя будет оптимальный доступ к вооружению и пище, так что со всеми удобствами так сказать."
    liz "Рядовые вообще не имеют ничего кроме холодного оружия."
    "Олег радостно кивнул."
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Ага, тебе даже возможно плазмач выдадут!"
    kt "Могу посмотреть что это вообще?"
    oleg "Да, секу."
    hide image oleg_happy with byso
    play music sanari fadein 3
    "Держась за поручень, он дошёл до руля и достал свою винтовку."
    scene bg plazmach
    hide image oleg_happy
    hide image liz_normal
    with byso
    oleg "Держи, любуйся.{w} Он на предохранителе и плюс к тому разряжен."
    "Константин взял в руки винтовку.{w} Винтовка была весьма причудливой формы. Сквозь стеклянные поверхности было видно плавающую красную плазму, а на ручке было нацарапано имя владельца."
    "На панелях отображалась надпись <<Зарядите накопитель!>>. Всё орудие было достаточно лёгким, на ощущение 2-3 килограмма."
    kt "И кто вам такое конструировал?"
    oleg "А что, нравится, да?{w} Это Гордон нам штампует... Хотя собирают девочки обычно."
    scene bg int_avtobus2
    show image liz_normal at right
    show image oleg_smile at left
    with byso
    liz "Гордон - наш местный техник.{w} Кстати не удивляйся, у нас многие похожи на обычных обитателей лагеря."
    kt "А почему так?"
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Ну смотри. Ты наверное тоже заметил что твоя внешность с попаданием сюда изменилась?"
    liz "Так с каждым циклом твоя внешность будет всё больше и больше походить на обычных обитателей пустой симуляции, пока полностью таковой не станет."
    liz "Моя по образцу Жени, твоя по образцу Семёна, а его вообще по образу физрука."
    kt "В нашей симуляции был физрук?"
    hide image liz_bukal
    show image liz_normal at right
    with byso
    "Лиза отрицательно помотала головой."
    liz "В каждой симуляции случайная комплектация."
    kt "Понимаю.{w}.. До попадания сюда, кстати, мне было 25."
    liz "Хе, а мы с тобой почти ровесники. Я младше на год была."
    hide image oleg_smile
    show image oleg_shy at left
    with byso
    oleg "А мне было всего 22..."
    "Обиженно ответил Олег и стал смотреть в окно."
    hide image liz_normal
    show image liz_laugh at right
    with byso
    liz "Ну да, по нему заметно, что ему явно не 30."
    oleg "Эй, обидно вообще-то!"
    "Ещё больше надулся Олег.{w} Константин усмехнулся."
    kt "Слушайте, раз вы пионера застрелили, то расскажите как в инреальности всё устроено."
    hide image liz_laugh
    show image liz_smile at right
    with byso
    "Олег глянул на Лизу, а она сложив руки за затылок потянулась."
    liz "Инреальность что-то вроде огромной ММО игры.{w} Есть комплекс из 3-4 симуляций, от которых зависит вообще существование симуляции.{w} Условно сервер."
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Прости что прерываю, но нет ли у кого-то закурить?{w} Сигарет два дня не видел."
    play sound sfx_unzip_sleepbag
    "Константин достал блок с сигаретами из своего мира, в нём было 7 пачек сигарет, одна из которых начатая.{w} У Олега челюсть упала на пол."
    hide image oleg_think
    show image oleg_happy at left
    with byso
    oleg "Нихера себе у тебя запасы!{w} Да ты за одну сигу сможешь себе улучшенное пропитание на день оформить!"
    hide image liz_smile
    show image liz_laugh at right
    with byso
    liz "Да, забыла сказать.{w} У нас в сопротивлении ходовой валютой являются советские рубли, но бартерный обмен тоже приветствуется, так что да, ты самый богатый сержант."
    kt "М-м, даже так... Ну неплохо."
    play sound light_inh
    "Константин проставился по одной сигарете каждому и зажёгся."
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    oleg "Во-о, это по нашему, спасибо, дружище."
    hide image liz_laugh
    show image liz_smile at right
    with byso
    liz "Спасибо."
    hide image liz_smile with byso
    play sound sfx_open_drapes volume 0.7
    "Все закурили, а Лиза подошла к водительскому месту, открыла форточку и взяла пепельницу. Поставив её посередине пледа, она села на место."
    show image liz_bukal at right with byso
    liz "Так, чё я там говорила..."
    kt "Сервер, комплекс симуляций..."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Точно.{w} Короче. Система по четвёртому писанию представляет собой отдельные циклы, не имеющий плотной связи между собой.{w} Плотная связь может образоваться только в результате нарушения стабильности."
    liz "Нарушение стабильности - парадокс."
    hide image oleg_smile
    show image oleg_think at left
    with byso
    oleg "Ага, жуткая тема."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Парадокс - явление, происходящее в результате обнуления стабильности.{w} Миры и кошмар начинают сближаться, провоцируя множество ошибок, благодаря которым симуляция может дойти до -100, где мир просто остановится и исчезнет."
    liz "Стабильность - это цифра от 100 до -100, где 100 это абсолютное равновесие, а -100 разрушение мира.{w} Стабильная сотка только у систем <<Семёнов>> и меняется только в случае смерти обитателей."
    "Закинув бычок в пепельницу, Лиза продолжила. {w}Константин внимательно слушал, а Олег выковыривал грязь из ногтей."
    liz "Система <<Семёна>> это симуляция инреальности, где есть Семён. Если проще, система где нет путников, понимающих что они в инреальности."
    liz "Вопросы?"
    kt "Что за четвёртое писание?"
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Итак. Смотри.{w} В инреальности есть <<фракции>>, как ты и сказал."
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "Сопротивление, одиночки, усопшие, идолопоклонники, террористы и силы Генды."
    "Дополнил Олег не отвлекаясь своего дела."
    hide image liz_bukal
    show image liz_normal at right
    hide image oleg_smile
    show image oleg_think at left
    with byso
    liz "Да.{w} Так, ну сопротивление это все мы. Наша цель ясна - отобрать у Генды симуляцию и создать свой мир."
    liz "Одиночки - путники, которые даже не знают о существовании фракций или уже идут на <<исправление>> от Генды.{w} Примером того ты, Лена, Рома и так далее."
    kt "Так, а Лена тут при чём?"
    "Лиза печально посмотрела в окно."
    hide image liz_normal
    show image liz_sad at right
    with byso
    liz "Она путница.{w} У неё уже четвёртый цикл.{w} Твоя симуляция невероятно богата на путников, но это потом."
    kt "М-м-м.{w}.. Ладно..."
    hide image liz_sad
    show image liz_normal at right
    with byso
    liz "Далее, усопшие.{w} Те кто пал от рук Генды и не нашёл покоя. Примером тому твой <<пионер>> или более популярные банши."
    "Олег оживился."
    oleg "Да, банши это вообще жесть.{w} Они появляются редко, но метко, и если у тебя нет под рукой интегратора то это конечная..."
    hide image liz_normal
    show image liz_angry at right
    with byso
    liz "Мы с ней однажды встретились. А у этого дебила интегратор был разряжен.{w} Рядового сожрали живьём."
    hide image oleg_think
    show image oleg_angry at left
    with byso
    oleg "Ой, только не начинай, а?{w} Я тогда вообще не знал что его заряжать надо!"
    hide image liz_angry
    show image liz_dontlike at right
    with byso
    "Лиза усмехнулась и безнадёжно покачала головой."
    liz "Ну ты понял.{w}.. Так, дальше у нас идолопоклонники."
    hide image liz_dontlike
    show image liz_bukal at right
    hide image oleg_angry
    show image oleg_think at left
    with byso
    liz "Те же одиночки, но они верят в Генду как в бога и пытаются нам навредить и/или скорее вступить в ряды Генды в качестве очередной пустышки."
    liz "Неприятные молодые люди. {w}Обычно такими становятся если выживают после парадокса, или такие с самого попадания в честь низких показателей ума."
    play sound_loop bus_sms
    hide image oleg_think
    show image oleg_angry at left
    with byso
    "Приборная панель начала пиликать. Олег вздохнул и пошёл к ней."
    hide image oleg_angry with byso
    play sound metal
    stop sound_loop
    oleg "Когда же Гордон нам поставит новый?!{w} Я уже задолбался повторно вводить настройки!"
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "И самая интересная фракция - террористы.{w} Безумцы, которые решили в одиночку противостоять Генде."
    liz "Самым первым был Михаил - составитель всех четырёх писаний.{w} Наш капитоша Андрей был с ним в одной симуляции, но пошли они по разным путям. Если тебе интересно, то у него и спросишь."
    kt "Почему четыре писания?"
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Версии.{w} Создатель несколько раз менял инреальность чтоб подклеить дыры и усложнить нам жизнь.{w} Четвёртая - самая последняя и правильная."
    show image oleg_angry at left with byso
    "К ним вернулся Олег."
    stop music fadeout 3
    oleg "Я вас поздравлю, но нам теперь ехать ещё дольше.{w} Трансформатор навернулся и повёл нас в другую сторону."
    liz "Ладно, на этот раз готова признать. Надо заплатить Гордону.{w} Сколько он дерёт?"
    hide image oleg_angry
    show image oleg_think at left
    with byso
    oleg "Он говорил что возьмёт либо 5 сигарет либо 7 рублей."
    hide image liz_bukal
    show image liz_angry at right
    with byso
    liz "Вот скряга!{w} У тебя два рубля будет?"
    oleg "У меня только один."
    window hide
    menu:
        "Дать сигареты на оплату.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            hide image liz_angry
            show image liz_surp at right
            with byso
            play sound sfx_paper_bag
            "Константин отдал начатую пачку честерфилда с кнопкой Лизе, там оставалось 6 сигарет."
            kt "Только на дело, а не скурить."
            hide image oleg_think
            show image oleg_happy at left
            with byso
            oleg "Чё правда?!{w} Спасибо! Настоящий друг!"
            "Радостно проскандировал Олег и потряс Константина за плечо."
            hide image liz_surp
            show image liz_smile at right
            with byso
            liz "Выручил, вовек не забудем.{w} Спасибо тебе!"
            "Лиза мило улыбнулась и положила сигареты на стул."
        "Промолчать.":
            $ renpy.block_rollback()
            th "Нет уж, мне самому ещё чего-то курить."
    play music the_date_of_death fadein 10
    hide image liz_angry
    hide image liz_smile
    show image liz_normal at right
    with byso
    liz "Ладно, на чём мы остановились?{w}.. Террористы."
    hide image oleg_think
    hide image oleg_happy
    show image oleg_think at left
    with byso
    oleg "Могу сказать за тебя.{w} У всех фракций наступила одна огромная проблема."
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Ты уже знаешь о ком Олег говорит.{w} Рыжая девочка."
    oleg "Мы её называем по-разному.{w} Рыжая бестия.{w}.. Красная вдова.{w}.. Сестра крови.{w}.. Смертоносная белизна.{w}.. Или просто богиня мора."
    "Он говорил это так, словно восхищался её поступками."
    hide image liz_bukal
    show image liz_smile at right
    with byso
    "Лиза усмехнулась и посмотрела в потолок."
    liz "Не путай <<я>> и <<мы>>."
    hide image liz_smile
    show image liz_normal at right
    with byso
    liz "Её кодовое обозначение в наших кругах - Батори, в честь кровавой графини 15-16х веков.{w} Она попала сюда примерно в тот же временной сегмент что и ты."
    liz "Её существование плохо для всех.{w} В первую очередь для Генды. Он терпит огромные убытки в симуляциях."
    liz "По бытующим рассказам новоприбывших-свидетелей она даже убивала усопших."
    liz "Даже мы попадаем под удар."
    liz "Я пыталась не говорить о <<Цене грехов>> в лагере, это бы попортило стабильность, но это и есть наиболее практичный способ следить за ней."
    oleg "Однажды мы отправили ей на перехват отряд <<Прорыв>> из третьего лейтенанта и шестерых подчинённых, вооружённых лучшей на тот момент техникой."
    kt "И чего?"
    hide image liz_normal
    show image liz_bukal at right
    with byso
    "Лиза медленно провела большим пальцем по своей шее, Константин понял что она хочет сказать. Олег двумя пальцами отдал честь и посмотрел в пол."
    oleg "Двое взорвались на растяжке, троим она отрубила голову.{w} Самого лейтенанта она пытала в поисках ответов, вырезала ему все органы, которые не были жизненно необходимыми."
    liz "Лишь один ефрейтор дезертировал и замаскировался под пионера.{w} Пропал без вести. Может как приедем, разведка скажет что с ним."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "Я надеюсь хоть он вернётся.{w} Может быть расскажет что делать."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Если проще она ищет одного путника. Имя неизвестно, но это явно не Семён.{w} <<Цена грехов>> не показывает никаких имён кроме Семёна и тех, кто уже мёртв."
    "Лиза встала на ноги и посмотрела в окно."
    liz "Знаешь, хоть мы по сути и заняты самой важной работой из возможных в сопротивлении, но мы как раз под ударом."
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Лиза права.{w} Не очень бы хотелось встретиться с ней."
    kt "Да я не думаю, что хоть кто-то из тех кто умер от её рук хотел этого."
    oleg "<<Прорыв>>.{w} Артём был третьим лейтенантом и сам желал этого."
    "Константин пожал плечами."
    kt "Без обид, но самоубийц в расчёт не берём."
    hide image liz_normal
    show image liz_bukal at right
    with byso
    liz "Да что без обид, так и было."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "М-да..."
    stop music fadeout 3
    "Олег неловко потёр шею.{w} Настало неловкое молчание."
    window hide dissolve
    pause 3
    hide image oleg_shy
    show image oleg_smile at left
    with byso
    play music music_list["sweet_darkness"] fadein 5
    window show dissolve
    pause 0.1
    oleg "Народ, а поесть никто не хочет?{w} Нам ещё ехать и ехать."
    oleg "Предлагаю сейчас похавать и прилечь вздремнуть."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Сколько нам ещё ехать?"
    "В ответ он глянул на приборку и махнул рукой."
    hide image oleg_smile
    show image oleg_think at left
    with byso
    oleg "7 часов плюс-минус два.{w} А вы карты не взяли?"
    hide image liz_normal
    show image liz_bukal at right
    with byso
    "Лиза тяжело вздохнула и отвела взгляд."
    liz "Забыла в библиотеке.{w} Кстати, как бинты?"
    hide image oleg_think
    show image oleg_happy at left
    with byso
    "Спросила Лиза у Константин, Олег усмехнулся."
    oleg "Да, мне интересно узнать на кой они тебе."
    kt "Нормально, уже зажило походу."
    kt "А получил пока выбивал дурь из одной пустышки и брата."
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    oleg "Ого, ты с братом попал в инреалку?"
    kt "И да и нет.{w} С одной стороны он мой двоюродный, с другой стороны он не брат а мразь."
    hide image liz_bukal
    show image liz_sad at right
    with byso
    liz "Да, у парня тяжёлая история, ничего не сказать."
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Так что, пожрать?"
    hide image liz_sad
    show image liz_angry at right
    with byso
    "Лиза тяжело вздохнула."
    liz "Тебе лишь бы жрать!{w} Ладно уж, неси..."
    oleg "Момент. Я вроде чего-то брал для нас..."
    kt "А никто не хочет выпить? У меня портвейн с собой."
    hide image liz_angry
    show image liz_laugh at right
    with byso
    "Лиза рассмеялась, а Олег резко обернулся."
    oleg "Шик!{w} Да ты прям швейцарский нож в мире поставок!"
    liz "Повторим!"
    "Константин достал и открыл бутылку портвейна."
    hide image liz_laugh
    show image liz_smile at right
    with byso
    kt "Стаканы есть?"
    liz "Вроде были бумажные..."
    "Лиза начала копаться в сумке."
    liz "Во, держи."
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    "Константин поровну разлил портвейн по трём большим стаканам.{w} Олег притащил три банки консервов и три вилки."
    oleg "Они вроде как все макароны с фаршем, но могу ошибаться.{w} Берите."
    liz "Вы очень любезны."
    kt "Хе, спасибо."
    "Все открыли свои банки.{w} Олег был точен в своём предположении и поднял тост."
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "За нового сержанта!"
    hide image liz_smile
    show image liz_laugh at right
    with byso
    liz "Да, за тебя."
    kt "Спасибо!"
    hide image liz_laugh
    show image liz_smile at right
    with byso
    "Все выпили понемногу и начали поедать содержимое банок."
    oleg "Лиз, а кем ты была до инреальности? Так долго уже катаемся, но об этом не говорили."
    hide image liz_smile
    show image liz_angry at right
    hide image oleg_happy
    show image oleg_shy at left
    with byso
    liz "Сначала прожуй, потом спрашивай!"
    "Недовольно ответила она и поправила волосы."
    hide image liz_angry
    show image liz_bukal at right
    with byso
    liz "Ничего такого. Я работала в банке."
    hide image oleg_shy
    show image oleg_smile at left
    with byso
    oleg "Из под огурцов?"
    hide image liz_bukal
    show image liz_angry at right
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    play sound sfx_face_slap
    "Олег заржал как конь, за что получил от Лизы отвесной подзатыльник."
    liz "Нет!{w} В обычном банке.{w} Кассиром была, а потом бац и Генда, инреальность."
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    "Олег отсмеялся от своей же шутки и погладил себя по затылку."
    liz "Дай угадаю, ты был грузчиком?"
    hide image oleg_smile
    show image oleg_shy at left
    with byso
    oleg "Нет, ты чего.{w} Я был фитнес-тренером. Просто автобус потом сбил и бац, я тута."
    hide image oleg_shy
    show image oleg_smile at left
    with byso
    oleg "А ты, Кость?{w} Как попал сюда?"
    "Константин выпил портвейна и поставил пустую консервную банку на пол."
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Судя по скорости еды солдатом."
    kt "Не-а. Не угадал.{w} Бухгалтер среднего звена..."
    hide image liz_angry 
    show image liz_surp at right
    hide image oleg_happy
    show image oleg_think at left
    with byso
    "Константин кратко пересказал свою историю попадания в инреальность."
    liz "М-да.{w}.. То-то понятно откуда у тебя такие способности..."
    kt "Да какие там. Застрелил тройку человек и чего с того?"
    oleg "Это конечно плохо, но у тебя не то что бы был выбор."
    "Пробубнил Олег и пожал плечами."
    hide image oleg_think
    show image oleg_happy at left
    with byso
    oleg "Но по сюжету катит на неплохой такой боевичок под пивко."
    hide image liz_surp
    show image liz_laugh at right
    with byso
    "Снова усмехнулся Олег, на этот раз Лиза поддержала его шутку."
    kt "Слушайте, а сколько вообще человек в сопротивлении?"
    hide image oleg_happy
    show image oleg_think at left
    with byso
    "Олег задумчиво почесал репу."
    hide image liz_laugh
    show image liz_grin at right
    with byso
    liz "Тебе чесать там нечего.{w}.. Короче, нас всего около пяти сотен."
    hide image liz_grin
    show image liz_angry at right
    with byso
    liz "Всего у нас 15 отрядов спасения помимо нас.{w} У всех правда техника лучше, потому что кое-кто у них не пропивает деньги."
    "Лиза укоризненно посмотрела на Олега."
    liz "И из-за этого не приходится тратить на четыре часа больше в разъездах!"
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "Да чего начинаешь, приедем - разберёмся, а деньги я один раз всего пропил!"
    liz "Ну-ну..."
    "Буркнула она и допила свой портвейн."
    hide image oleg_shy
    show image oleg_happy at left
    with byso
    oleg "Да, за новый двигатель!"
    "Заявил Олег и залпом хлопнул остатки портвейна.{w} Константин сделал так же."
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    oleg "Ну вот поели - можно и поспать.{w}.. Я на руле посижу."
    "После этих слов он пошёл на водительское место."
    hide image liz_angry
    show image liz_grin at right
    with byso
    liz "Храпеть будешь - задушу!"
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Да-да, доброй ночи."
    hide image oleg_happy
    hide image liz_grin
    show image liz_grin
    with byso
    stop music fadeout 3
    "Олег уселся на водительское место и закрыл глаза."
    kt "Да, не похоже что вы сильно сплочённая команда..."
    hide image liz_grin
    show image liz_surp
    with byso
    liz "С чего ты взял?"
    hide image liz_surp
    show image liz_smile
    with byso
    liz "Он может и тунеядец немного, но с ним ещё нормально."
    "Константин усмехнулся и посмотрел в сторону Олега."
    kt "Ну, может и так..."
    hide image liz_smile
    show image liz_grin
    with byso
    play sound BlueJetta fadein 6
    "Лиза посмотрела Константину в глаза."
    liz "А ты хоть как?{w} Перевариваешь что мы тебе сегодня нарассказывали?"
    kt "Да, порядок. Одного только не пойму."
    hide image liz_grin
    show image liz_smile
    with byso
    liz "М-м-м?"
    kt "Зачем Генде всё это? Создал систему симуляций пытать людей, допустим.{w} Но какая ему с того выгода?"
    hide image liz_smile
    show image liz_dontlike
    with byso
    "Лиза задумчиво посмотрела в потолок."
    liz "Да чтоб я знала.{w}.. Не думаю что психам вроде него нужны оправдания."
    hide image liz_dontlike
    show image liz_bukal
    with byso
    liz "Хотя знаешь.{w}.. Может быть он просто решил наконец покарать человечество за его грехи."
    kt "Да, я тоже думаю что это и есть причина."
    "Лиза легла на спину."
    hide image liz_bukal
    show image liz_sad
    with byso
    liz "Честно говоря мне тоже много дерьма пришлось за жизнь наесться."
    liz "Мои родители погибли в автомобильной аварии когда мне исполнилось 17."
    liz "Я два года жила со своей бабушкой у которой был Альцгеймер.{w} Семья у нас была достаточно большая, но все забыли про неё."
    liz "Ухаживая за ней, мне самой становилось хуже."
    "Повернув голову в сторону, она заглянула в глаза Константину."
    liz "Иногда я приходила с учёбы, а она не могла вспомнить моего имени."
    liz "Я ей говорила <<Бабушка, я люблю тебя>>, а она смотрела на меня, словно я никто..."
    liz "Потом и она умерла.{w} Я была одна несколько лет.{w} У меня не было никакого желания вливаться обратно в социум."
    "Лиза снова засмотрелась в потолок."
    hide image liz_sad
    show image liz_bukal
    with byso
    liz "Так что вся эта история с Гендой и Батори меня не сильно пугает.{w} Самое неприятное позади."
    kt "М-да... Тяжёлая история."
    hide image liz_bukal
    show image liz_smile
    with byso
    "В ответ она едва заметно улыбнулась."
    liz "Да я знаю что у тебя не лучше.{w} Самый счастливый тут из нас - Олег."
    kt "Да уж..."
    hide image liz_smile
    show image liz_grin
    with byso
    liz "Ладно, давай спать.{w} Если хочешь - ложись рядом, но если лапать будешь - убью по всем традициям Батори!"
    "С усмешкой предупредила Лиза и, достав ещё пару пледов, протянула один Константину."
    window hide
    menu:
        "Лечь одному.":
            $ renpy.block_rollback()
            "Константин взял у Лизы плед, сел на сиденье и отрицательно помотал головой."
            kt "Нет, спасибо, хотелось бы ещё пожить."
            hide image liz_grin
            show image liz_bukal
            with byso
            liz "Ну и ладно, спокойной ночи."
            kt "Спокойной ночи."
            stop music fadeout 3
            show blink
            "Константин уснул."
            "На этот раз не было никаких игр от Генды.{w} Константин подсознательно чувствовал себя лучше."
            pause 3
            hide image liz_bukal
            scene bg int_avtobus2
            show image oleg_happy at left
            show image liz_angry at right
            show unblink
            play sound sfx_radio_tune
            play music wpstar fadein 3
            "Проснулся Константин от криков Олега и от шума радио, которое он включил."
            oleg "Рота подъём!{w} Мы на подъезде!"
            hide image oleg_happy
            show image oleg_shy at left
            with byso
            play sound2 sfx_soccer_ball_kick
            play sound3 banka2
            "В ответ Лиза взяла лежащую на полу консервную банку и метнула в лоб Олега."
            liz "Будильник из тебя как из палки автомат, нельзя было поспокойнее?!"
            oleg "Хватит тебе кидаться.{w}.. Да ещё и так метко!"
            "Константин встал с сидушки и положил на неё плед."
        "Лечь с Лизой.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            "Константин взял у Лизы плед и лёг рядом."
            kt "Надеюсь проснусь живым."
            hide image liz_grin
            show image liz_smile
            with byso
            "Лиза погладила Константина по плечу."
            liz "Ладно-ладно. Выживешь. Спи давай."
            kt "Спокойной ночи."
            liz "Спокойной ночи."
            stop music fadeout 3
            show blink
            "Константин уснул."
            "На этот раз не было никаких игр от Генды. Константин подсознательно чувствовал себя лучше."
            pause 3
            hide image liz_smile
            scene bg int_avtobus2
            show image oleg_happy at left
            show image liz_angry at right
            show unblink
            play sound sfx_radio_tune
            play music wpstar fadein 3
            "Проснулся Константин от криков Олега и от шума радио, которое он включил."
            oleg "Рота подъём, молодожёны! {w}Мы на подъезде!"
            hide image oleg_happy
            show image oleg_shy at left
            with byso
            play sound2 sfx_soccer_ball_kick
            play sound3 banka2
            "В ответ Лиза взяла лежащую на полу консервную банку и метнула в лоб Олега."
            liz "Если бы ты молчание хранил так же как девственность, цены бы тебе не было!"
            oleg "Это не смешно!{w} И хватит тебе кидаться... Да ещё и так метко!"
            "Константин встал на ноги и положил плед на сидушку."
    "Протерев лоб от неупругого удара, Олег глянул на приборную панель."
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Следующая наша.{w} Пятиминутная готовность."
    hide image liz_angry
    show image liz_bukal at right
    with byso
    "Лиза потёрла глаза и начала складывать пледы обратно в сумку."
    kt "Сколько мы спали?"
    oleg "Часа четыре.{w} Мы вернулись куда раньше чем прибор показывал."
    hide image liz_bukal
    show image liz_angry at right
    with byso
    liz "Ну ничего, доедем, сдадим Гордону нахер.{w} Не знаю как вы, но я не выспалась."
    kt "Я тоже нет, но хоть на этот раз я проснулся не в кошмаре."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "По нашему времени у нас 11 вечера, так что поспать успеете.{w} Вот только я есть хочу, а это уже проблема."
    hide image liz_angry
    show image liz_grin at right
    with byso
    liz "Кто бы мог подумать!"
    "Константин достал новую пачку сигарет и достал три штуки."
    kt "Будете?"
    hide image oleg_shy
    show image oleg_think at left
    with byso
    oleg "Не, если от меня будет шмонить куревом, то подумают что я платёжеспособный и начнут сдирать долги..."
    hide image liz_grin
    show image liz_smile at right
    with byso
    liz "А я не откажусь."
    play sound light_inh
    "Константин протянул Лизе сигарету и дал огня."
    liz "Мерси."
    kt "Не за что."
    "Константин закурил и глянул в окно."
    kt "Шикарная поездочка, ставлю 9/10."
    hide image oleg_think
    show image oleg_shy at left
    with byso
    oleg "А почему не 10?"
    "Вполне справедливо возмутился Олег."
    kt "Еда холодная."
    "С усмешкой проговорил Константин, Олег ухмыльнулся."
    hide image oleg_shy
    show image oleg_happy at left
    with byso
    oleg "Ой, какие мы привереды."
    hide image liz_smile
    show image liz_normal at right
    with byso
    liz "А вот и наша остановочка."
    "Автобус проехал мимо ЛЭП и начинал снижать скорость."
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    oleg "Вот мы и дома..."
    stop music fadeout 3
    "Константин затушил сигарету и надел рюкзак.{w} Лиза пошла к дверям."
    stop ambience fadeout 3
    play sound sfx_bus_stop
    "Автобус издал последний звук и заглох."
    hide image oleg_smile
    show image oleg_angry at left
    hide image liz_normal
    show image liz_bukal at right
    with byso
    oleg "Вот развалюха, а!"
    play sound3 door_break
    "Со всей силы он пнул дверь и она открылась."
    hide image oleg_angry
    show image oleg_happy at left
    with byso
    oleg "Прошу."
    hide image oleg_happy
    hide image liz_bukal
    scene bg ext_bus_night
    show image oleg_smile at left
    show image liz_smile at right
    with byso
    $ volume(1, "ambience")
    play ambience ambience_camp_entrance_night
    play sound sfx_wind_gust volume 0.6
    "Выйдя из автобуса, Константин почувствовал прохладный свежий ветерок."
    hide image oleg_smile
    hide image liz_smile
    scene bg ext_entrance_night_closed
    show image oleg_angry at right
    show image liz_normal at left
    with byso
    play music music_list["heather"] fadein 3
    "Подойдя к воротам, Олег постучал в ворота."
    oleg "Открывайте!"
    ohra "Кто?"
    hide image liz_normal
    show image liz_bukal at left
    hide image oleg_angry
    show image oleg_happy at right
    with byso
    oleg "Я Генда!{w} Пришёл всех вас тут порешать!"
    show image Ohra_normal
    hide image liz_bukal
    show image liz_bukal at left
    hide image oleg_happy
    show image oleg_happy at right
    with byso
    play sound sfx_metal_door_handle_rattle
    play sound sfx_open_door_mines_metal
    "Дверь медленно открылась. {w}Встретил их охранник с плазмоинтегратором."
    ohra "Олег, здорова!{w} Повезло тебе что второго лейтенанта тут нет, она бы тебе башку снесла!"
    hide image oleg_happy
    show image oleg_smile at right
    with byso
    oleg "Здорова, чувак.{w} У нас пополнение - сержант Константин."
    hide image liz_bukal
    show image liz_angry at left
    with byso
    "Охранник оценивающе посмотрел на Константина, Лиза прищурилась и посмотрела на охранника."
    liz "Сержант-сержант, тебе не послышалось."
    ohra "Хорошо-хорошо.{w} Приветствую товарищ лейтенант!"
    ohra "Не забудьте сдать анализы крови. Проходите."
    hide image Ohra_normal
    hide image oleg_smile
    hide image liz_angry
    scene bg ext_clubs_night
    show image oleg_happy at left
    show image liz_smile at right
    with byso
    stop music fadeout 3
    play sound sfx_metal_door_heavy_close
    "Компания прошла вперёд, охранник закрыл ворота и сел на рядом стоящий табурет."
    liz "Вот видишь, сержант уже не так плохо."
    kt "Ладно...{w} А зачем анализы?"
    hide image liz_smile
    show image liz_bukal at right
    hide image oleg_happy
    show image oleg_think at left
    with byso
    play music god fadein 4
    oleg "Есть такая штука..."
    liz "Генмод.{w} Эта муть может тебя превратить в гончую из кошмара. Поверь, это никому не надо."
    oleg "Ага, а ещё передаётся воздушно-капельным..."
    liz "Гордон походу уже не работает.{w} Завтра его обрадуем."
    scene bg ext_square_night
    hide image liz_bukal
    show image liz_normal at right
    hide image oleg_think
    show image oleg_think at left
    with byso
    "Пройдя мимо клубов, они дошли до площади, где стоял тот же самый медный Генда."
    kt "А чего вы его не снесли?"
    hide image oleg_think
    show image oleg_angry at left
    with byso
    oleg "Да хрен ты его снесёшь.{w}.. В лагере нет такого здания у которого фундамент настолько же прочный!"
    "Лиза свернула в сторону административного корпуса."
    liz "Нам туда."
    hide image oleg_angry
    hide image liz_normal
    scene bg ext_admins_night
    show image liz_bukal at right
    show image oleg_think at left
    with byso
    "Дойдя до него, Лиза и Олег остановились."
    liz "Значит смотри.{w} Андрей ещё тот параноик. Делай что угодно, но не давай ему причин в себе сомневаться.{w} И не груби тоже."
    oleg "Угу.{w} Что сказал, то и делай. Скорее всего он вызовет тебя на личную беседу."
    kt "Да про вежливость ясно.{w} Тут без б."
    hide image liz_bukal
    show image liz_smile at right
    with byso
    "Лиза улыбнулась и ткнула Олега локтем."
    liz "Мы доложим о своём возвращении и с Олегом сгоняем в разведпункт.{w} Он находится в библиотеке. Приходи потом к нам, оттуда соберёмся."
    kt "Хорошо, уяснил."
    liz "Класс, пошли к капитану."
    show image rkis_normal with byso
    "У входа их встретила робот-кошкодевочка."
    th "Зачем именно кошкодевочка? Почему не бугай какой-нибудь?"
    rkis "Модель I-62 приветствует вас. {w}Назовите позывные и цель визита."
    hide image oleg_think
    show image oleg_smile at left
    with byso
    oleg "Позывной <<Свинец>>.{w} Цель: доложить капитану о прибытии."
    hide image liz_smile
    show image liz_bukal at right
    with byso
    liz "Позывной <<Дзета>>.{w} Цель: представить капитану новоприбывшего и сообщить о прибытии."
    rkis "Запрос отправлен капитану. {w}Ожидайте."
    th "Музыки из лифта не будет я надеюсь..."
    play sound sfx_radio_squelch_1
    rkis "Запрос принят.{w} Капитан ждёт вас на втором этаже, кабинет 203."
    play sound2 sfx_medpunkt_door_open
    hide image rkis_normal with byso
    "Кошкодевочка открыла дверь и впустила компанию внутрь."
    stop ambience
    play sound door_cl
    hide image liz_bukal
    hide image oleg_smile
    scene bg int_admins
    show image liz_smile at right
    show image oleg_smile at left
    with byso
    kt "<<Свинец>> и <<Дзета>>?{w} Кто вам такие позывные дал?"
    "Олег словно ожидая этого вопроса широко улыбался."
    oleg "Я сам выбирал.{w} Прикольное, да? По своей фамилии брал - Свинцов."
    hide image liz_smile
    show image liz_bukal at right
    with byso
    "Лиза отвела взгляд и тяжело вздохнула."
    liz "Я тоже сама выбирала. Просто буквой греческого алфавита.{w} В физике используется для обозначения коэффициента гидравлического сопротивления.{w} Вот так завуалировала."
    hide image oleg_smile
    show image oleg_think at left
    with byso
    "Олег почесал затылок."
    oleg "Ну моё хоть попроще."
    kt "Тут уж соглашусь."
    hide image liz_grin
    show image liz_bukal at right
    with byso
    liz "Да идите вы."
    play sound sfx_knock_door7_polite
    "С усмешкой ответила Лиза и постучала в дверь."
    andr "Войдите."
    hide image liz_bukal
    hide image oleg_think
    scene bg int_admins_room
    show image liz_bukal at right
    show image oleg_smile at left
    show image andr_normal
    with byso
    play sound door_cl
    play music Gallow fadein 5
    "Все трое вошли в кабинет.{w} В кабинете сидел парень в зелёном костюме, очках и светлыми волосами. Лиза и Олег отдали честь."
    oleg "Здрасте, товарищ капитан! Мы привезли новенького."
    kt "Константин. Рад знакомству."
    "Сказал он и махнул рукой, отдавая честь."
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "Вольно.{w} Я ожидал ваш отряд увидеть ещё через четверть цикла, чего так рано?"
    hide image oleg_smile
    show image oleg_happy at left
    with byso
    oleg "Автобус полон провизии, товарищ капитан, весь багажник заполнен."
    hide image andr_normal3
    show image andr_normal2
    with byso
    "Андрей отвёл взгляд в сторону."
    andr "Хорошо.{w} Завтра разгрузишь, можешь идти."
    hide image oleg_happy
    show image oleg_smile at left
    with byso
    oleg "Без б. До скорой!"
    play sound door_cl
    hide image oleg_smile with byso
    "Отчеканил Олег и покинул кабинет."
    hide image liz_bukal
    show image liz_normal at right
    with byso
    liz "Первостепенной причиной возвращения являются новости.{w} Симуляция Константина содержит в себе много путников, которых можно было бы присоединить к нам."
    liz "Константин вступил как самый способный из них."
    hide image andr_normal2
    show image andr_normal
    with byso
    "Капитан поправил очки и сел за стул."
    andr "Принято.{w} Значит снаряжаетесь и через два дня твоя группа едет их оттуда вытаскивать, если обстоятельства не изменятся."
    hide image andr_normal
    show image andr_normal3
    with byso
    andr "Какое звание ты ему присвоила?"
    hide image liz_normal
    show image liz_smile at right
    with byso
    liz "Я дала ему звание сержанта."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "Приемлемо. Оставь меня с Константином."
    hide image liz_smile
    hide image andr_normal2
    show image andr_normal
    with byso
    play sound door_cl
    "Лиза махнула рукой, после чего удалилась.{w} Константин остался тет-а-тет с Андреем."
    andr "Ещё раз здравствуй."
    kt "Добрый вечер."
    hide image andr_normal
    show image andr_normal2
    with byso
    play sound sfx_open_table
    "Андрей достал из ящика лист бумаги."
    hide image andr_normal2
    show image andr_normal
    with byso
    play sound sfx_paper_bag
    andr "Итак, начнём.{w} Садись на диван. Сейчас немного формальности, нам нужно знать в чём ты можешь пригодиться.{w} Имя твоё я знаю. Позывной?"
    kt "У меня нет такого."
    hide image andr_normal
    show image andr_smile
    with byso
    andr "Логично.{w} Пожелания будут?"
    kt "Хм-м...{w} Пусть будет <<Корсар>>."
    hide image andr_smile
    show image andr_normal2
    with byso
    andr "Принял.{w} Звание сержант. Месяц, год попадания и должность?"
    kt "2022, декабрь.{w} Бухгалтер среднего звена."
    hide image andr_normal2
    show image andr_normal3
    with byso
    hide image andr_normal3
    show image andr_normal2
    with byso
    "Андрей на секунду отвлёкся от бумажки, посмотрел на Константина и продолжил писать."
    andr "Хобби или умения которые могут пригодиться?"
    kt "Стрельба, готовка.{w} Другого сразу не вспомню."
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Ага.{w}.. Как попал в инреальность?"
    kt "Застрелен Гендой."
    hide image andr_normal
    show image andr_normal3
    with byso
    "Андрей косо посмотрел на Константина."
    andr "А теперь серьёзно."
    kt "Ну, застрелил до этого тройку гвардейцев."
    hide image andr_normal3
    show image andr_normal2
    with byso
    "Андрей вернулся к бумажке и что-то записал, после чего вернул бумажку в ящик стола."
    andr "Для отряда Дзеты ты подходишь. {w}Если не устроит, то можешь перевестись в разведку."
    kt "Приму к сведению."
    hide image andr_normal2
    show image andr_normal
    with byso
    "Андрей встал со стула и подошёл к окну."
    andr "Что по твоему лучше?{w} Жить монстром или умереть человеком?"
    "Константин почесал подбородок."
    kt "Смотря что подразумевает слово <<монстр>>."
    hide image andr_normal
    show image andr_smile
    with byso
    andr "М-м... Хорошо."
    "Андрей облокотился на шкаф и пристально смотрел Константину в глаза."
    andr "Что ты думаешь про другие фракции?"
    kt "Сложно сказать. Кроме сопротивления я ещё никого не встречал.{w} Хотя нет, был потерянный пионер, как сказала Же... Лиза, он был из <<усопших>>."
    hide image andr_smile
    show image andr_normal
    with byso
    "Андрей поправил очки и продолжил смотреть в глаза Константину."
    andr "Продолжай."
    kt "Он говорил что может помочь мне, но пока мы ехали, Олег распылил его из плазмоинтегратора."
    hide image andr_normal
    show image andr_normal2
    with byso
    andr "Понял. Что можешь сказать про Генду?"
    kt "Мужик, который обрёл способность творить беспредел."
    hide image andr_normal2
    show image andr_smile
    with byso
    "Андрей непроизвольно улыбнулся, но это было видно буквально пару секунд."
    hide image andr_smile
    show image andr_normal2
    with byso
    andr "Пересекался с путниками вроде тебя?"
    kt "Да. Ничего особенного."
    hide image andr_normal2
    show image andr_normal3
    with byso
    andr "Что думаешь о сопротивлении?"
    "Константин оглянул комнату."
    kt "Как бы сказать.{w} Цель у вас есть, но я не уверен что вы способны что-либо поменять в инреальности."
    hide image andr_normal3
    show image andr_normal2
    with byso
    andr "Критично.{w}.. Но честно. Хорошо."
    kt "Можно я теперь задам вопрос?"
    hide image andr_normal2
    show image andr_normal
    with byso
    andr "Слушаю."
    "Безэмоционально ответил капитан."
    kt "Как вы собрались вообще противостоять порождениям инреальности?{w} Генда, Батори и прочее."
    "Андрей сел на стул и выключил лампу за столом."
    hide image andr_normal
    show image andr_normal2
    with byso
    andr "Впервые слышу такой вопрос от новобранца, я приятно удивлён."
    th "По твоему лицу не сказать."
    andr "Числом и слаженностью.{w} В меньшей степени технологиями и осведомлённостью."
    andr "Как бы тебе не могло показаться, сержант, у нас всё не так просто."
    andr "Отдел исследований хоть и состоит из трёх человек, но работает крайне эффективно."
    andr "Плазмоинтегратор который ты видел - это лишь наработка того, что произвел наш технический отдел."
    hide image andr_normal2
    show image andr_normal3
    with byso
    andr "Я был лично знаком с Мишей.{w} Создателем четвёртого писания."
    andr "На второй цикл мы поняли что надо делать, но наши идеи разошлись.{w} Я собрал сопротивление, а он погиб."
    andr "Генду вполне возможно победить на его правилах."
    andr "После того как мы эвакуируем ещё пару-тройку симуляций и подготовим людей, мы можем начать революцию."
    andr "Так что ты попал сюда в самое подходящее время."
    kt "Почему вы это не сделали за эти 9 лет?"
    hide image andr_normal3
    show image andr_smile
    with byso
    "Андрей призрачно улыбнулся."
    andr "Для нас 9 лет прошли как полтора года. {w}Зато мы набрали достаточно сил и разработали план."
    andr "Соглашусь, много времени прошло, но для Генды это будет ножом в спину, он не ждёт нашего удара."
    kt "И почему он не нашёл вас?"
    hide image andr_smile
    show image andr_normal2
    with byso
    andr "Маскировка симуляции. {w}Техники нашли способ обмануть систему Генды и теперь мы невидимы для него."
    andr "Ещё вопросы?"
    kt "Вроде нет.{w} На этом всё."
    "Андрей встал со стула и вернулся к окну."
    stop music fadeout 3
    andr "Тогда на сегодня свободен. Завтра подойди с утра.{w} Доброй ночи, сержант."
    kt "Доброй ночи, капитан."
    "Спародировал Константин и пошёл на выход."
    scene bg ext_admins_night
    show image rkis_normal
    with fade
    play sound door_cl
    play sound2 light_inh
    play ambience ambience_camp_entrance_night
    "Выйдя из здания, Константин закурил, а к нему обратилась кошкодевочка."
    rkis "Добрый вечер.{w} Сержант, внесите свой позывной в мою базу данных."
    play sound inh
    "Константин сделал затяжку и обернулся."
    kt "Корсар."
    play music umted fadein 3
    rkis "Позывной задан.{w} Вас ожидает <<Дзета>> и <<Свинец>> в отделе разведки."
    kt "Угу, помню."
    rkis "Хорошего вечера."
    hide image rkis_normal with byso
    "Воспроизвёл робот и вернулся к дверям.{w} Константин пошёл в сторону библиотеки."
    scene bg ext_square_night with byso
    th "М-да.{w} И так моя новая жизнь превратилась в милитаризм головного мозга."
    th "Женя, как выяснилось, Лиза.{w} Я сам того нехотя попал в некое сопротивление."
    th "А ещё вчера я говорил с Лизой и даже вообразить подобного не мог."
    th "Может быть так будет лучше.{w} Меня хотя бы не мучают кошмары с Гендой."
    th "Моя новая жизнь начинает походить на какой-нибудь триллер с элементами драмы. {w}Ладно уж, теперь ничего не поделать."
    th "Возможно я смогу стать человеком в новом мире, который отстроят на задворках инрельности."
    th "Хотелось бы в это верить. В армии я не служил, ну вот теперь видимо придётся. Посмотрим что будет дальше."
    scene bg ext_library_night with byso
    stop music fadeout 2
    "Константин дошёл до библиотеки и выкинул бычок."
    scene bg int_library_night2
    show image liz_bukal at left
    show image oleg_think
    show image irr_angry at right
    with byso
    play sound door_cl
    stop ambience
    play music music_list["just_think"] fadein 3
    "Без стука он вошёл. Вокруг стола стояла Лиза, Олег и неизвестная Константину девушка."
    irrp "Ну Олег, ты дурак или да?{w} Какое нахер вернётся когда его имя написано в книжке?"
    hide image oleg_think
    show image oleg_shy
    with byso
    oleg "Может он выжил?"
    hide image liz_bukal
    show image liz_angry at left
    with byso
    liz "Тебе же показали главу в <<Цене грехов>>, чё ты мелешь то?"
    hide image irr_angry
    show image irr_normal at right
    with byso
    "Вдруг девушка заметила присутствие Константина."
    hide image liz_angry
    show image liz_normal at left
    with byso
    irrp "Вау, кто такого красавца нам привёз!"
    "Константин подошёл к столу и помахал рукой."
    kt "Салют. Я Константин.{w} Сержант по званию если это важно."
    hide image oleg_shy
    show image oleg_happy
    with byso
    oleg "Ну ка-ак! Сержант это важно! Сержант это круто!"
    hide image irr_normal
    show image irr_shy at right
    with byso
    "Проскандировал Олег.{w} Девушка усмехнулась и протянула руку."
    irr "Меня Ира.{w} Главная в отделе разведки и по совмещению второй лейтенант.{w} Рада знакомству!"
    hide image irr_shy
    show image irr_normal at right
    with byso
    "Константин пожал руку и с улыбкой кивнул."
    kt "Взаимно.{w} Что обсуждаете?"
    hide image liz_normal
    show image liz_bukal at left
    hide image oleg_happy
    show image oleg_think
    with byso
    liz "Как мы и думали.{w} Батори выследила нашего последнего выжившего."
    hide image irr_normal
    show image irr_angry at right
    with byso
    irr "А для особо недоверчивых я зачитаю."
    stop music fadeout 1
    "Взяв книгу в руки сказала Ира, раздражённо поглядывая на Олега."
    hide image irr_angry
    show image irr_normal at right
    with byso
    play music lim fadein 1
    irr "Дмитрий Лашин. 2019 год.{w} В своей жизни он был самым обычным студентом, грехом которого был гнев."
    irr "Пока он не съехал от родителей, он избивал сверстников, после чего пошёл в ВУЗ и... я это пропущу, мне надоело читать историю этого дегенерата."
    hide image oleg_think
    show image oleg_angry
    with byso
    oleg "Ира!{w} Это грубо!"
    hide image irr_normal
    show image irr_happy at right
    with byso
    "В ответ Ира лишь ухмыльнулась."
    hide image liz_bukal
    hide image irr_happy
    hide image oleg_angry
    scene bg ext_bus_night
    show shum_white
    with flash
    "Очнулся он в пустоте.{w} Пред ним был лишь образ девочки."
    deva "Ты пойдёшь со мной?"
    "Дима утвердительно кивнул."
    irr "Его позор в лагере тоже пропустим."
    hide shum_white
    scene bg ext_camp_entrance_night
    show shum_white
    with flash
    play music paralysis fadein 1
    "Отряд приехал в лагерь.{w} Выходя из автобуса, лейтенант начал давать указания."
    leten "Нейтрализуем всё представляющее опасность. По показаниям разведки стабильность обнулится через час.{w} Снять плазмоинтеграторы с предохранителя и проверить боезапас на табельном оружии."
    "Дима, как и остальные рядовые проверили заряд орудий и пистолетов."
    di "Рядовые к бою готовы."
    leten "Замечательно.{w} Четверо со мной, остальные под руководством Дмитрия!"
    "По плану, лейтенант выдвинулся в библиотеку за выжившими, а отряд Димы отправился на зачистку."
    hide shum_white
    scene bg ext_house_of_mt_night_without_light
    show shum_white
    with byso
    di "Осмотреть домик вожатой!"
    ridov "Есть."
    "Один из рядовых выбил дверь, а второй забежал за ним."
    di "Растяжка!!!"
    "Рядовые не успели и одуматься, как их тела разлетелись по домику."
    "Дима упал на колени."
    di "████.{w}.. █████.{w}.. Друзья..."
    "По его щеке потекла слеза."
    "Он взял рацию."
    di "Кадавр.{w}.. Кремень и Лазурь мертвы... Приём..."
    leten "Что?!{w} Срочно выдвигайся к отряду Альфа! Приём."
    di "Принял... Приём..."
    "Дима встал с колен."
    di "Надо бежать..."
    "Дима побежал в библиотеку."
    hide shum_white
    scene bg ext_square_night_blood
    show shum_white
    with byso
    "Площадь уже была заполнена убитыми пионерами.{w} Радио начало разрываться."
    ridov "Кадавр! Батори..."
    leten "Группа гамма, ответьте, приём!"
    ridov "Кадавр, чёрт возьми у нас тоже..."
    leten "Уцелевшие, выдвигаемся на точку..."
    "Дима понял что он остался последний.{w} На площади открылся портал."
    di "Сбегу - дезертирство.{w}.. Останусь - умру."
    "Не долго думая, он запрыгнул в портал."
    hide shum_white
    scene bg int_clubs_male2_night_nolight
    show shum_white
    with flash
    "Очнулся он в кладовке.{w} Положив плазмоинтегратор на пол, он вышел из неё."
    hide shum_white
    scene bg int_clubs_male_day
    show shum_white
    with byso
    "Оказался он в какой-то мастерской, на него удивлённо смотрели два пионера."
    tech2 "Что ты тут?.."
    "Достав пистолет, Дима застрелил одного пионера и навёлся на другого."
    di "Одежду.{w} Сейчас."
    "Пионер в ужасе достал из шкафа пионерскую одежду и положил на стол."
    "Дима застрелил и его."
    hide shum_white
    scene bg black
    show shum_white
    with byso
    "Переодевшись в пионера, он спрятался в шкафу.{w} Кто-то прибежал на звуки выстрелов."
    pi "Что?!{w} ██████████?!{w} █████?!"
    "Сбежалось ещё больше пионеров.{w} Вдруг, в кладовке раздался странный звук."
    rep "О, а скот уже сам пришёл на убой!"
    "Раздался истерический смех, поднялась паника и все стали бежать прочь из клубов."
    rep "Бежать нет смысла!"
    "Здание быстро опустело."
    hide shum_white
    scene bg int_mine_crossroad
    show shum_white
    with flash
    "Дима решил спрятаться в шахте, где встретил другого пионера."
    di "Значит, ты тоже решил убежать?"
    "Пионер вскочил с места и начал в панике оглядываться."
    di "Не бойся, я тут дать тебе ответы, просто возьми себя в руки."
    "Пионер успокоился, Дима оглянулся."
    pi "Не назвал бы это бегством."
    "Через некоторое время ответил он, растягивая каждое слово."
    di "Да?{w} А как же тогда?"
    pi "Поиск ответов."
    di "Блестяще!"
    "Дима расхохотался."
    pi "Слушай, может, ты расскажешь всё-таки, что здесь происходит, кто ты и чего от меня хочешь?"
    di "Что же, это вполне в нашем духе.{w}.. Убежать, спрятаться..."
    "Дима проигнорировал вопрос пионера."
    di "Тебе не так важно знать кто я, тебе важно знать кто она."
    pi "Я не знаю, что у тебя тут за цирк с конями, но у меня, честно говоря, нет никакого желания участвовать в этом представлении!"
    di "О, почему же...{w} Ты главная звезда!"
    "Дима широко улыбнулся, пионеру стало не по себе."
    pi "Если так, то объясни мне мою роль!"
    di "Знаешь, я вначале тоже был таким, как ты.{w}.. Первый раз всё прошло спокойно."
    di "Потом я убегал, пытался выяснить, что происходит, сходил с ума..."
    "Он заржал как умалишённый."
    di "Но всё бесполезно!"
    "Немного успокоившись, продолжил Дима."
    di "Бесполезно...{w} Она..."
    di "Сначала я слышал её голос – где-то далеко, а иногда у себя в голове."
    di "Она не имеет никаких человеческих качеств!{w} Она монстр!{w} Она словно питается нашей кровью!"
    di "И наконец вошла в мой мир!{w} В поисках меня! Она убила их всех!{w} Порубила на части своим топором..."
    di "Я сбежал из того мира через портал.{w}.. Но она продолжила охоту за мной! Она где-то рядом."
    di "Она хочет меня убить!!!"
    "Он сбился на крик."
    di "И раз за разом всё повторялось.{w}.. Она убивала людей, одного за другим."
    di "Потом я и сам научился попадать в их миры, взаимодействовать с другими.{w} Однако она умеет так же!"
    di "Нам нужно бежать, остальное потом! Сопротивление нам поможет!"
    "Он замолчал.{w} Позади раздался шорох и пионер обернулся."
    pi "Что там..."
    "Дима почувствовал острую боль в горле, он хотел закричать, но его голосовые связки были перерезаны. Пионер обернулся и в шоковом состоянии не мог понять что происходит."
    rep "Приве-етик! С ним ты уже познакомился, говорить вам больше не о чем!"
    "Девочка оторвала голову Димы с позвонков."
    rep "Ой, только не начинай бежать, я хочу сделать это быстро, думаю ты тоже."
    stop music fadeout 1
    scene bg int_library_night2
    show image liz_bukal at left
    show image oleg_shy
    show image irr_angry at right
    with flash
    pause 1
    play music music_list["sunny_day"] fadein 1
    irr "Повествование 42й души завершено. {w}Жил с позором, сдох с позором."
    play sound sfx_open_cabinet_2
    "Ира с отвращением откинула книгу на стол."
    kt "Что-то когда мы были в своей симуляции, она меньше жестила..."
    hide image irr_angry
    show image irr_mad at right
    with byso
    irr "У-у, это ещё не жестила.{w} Ты бы читал то что было на несколько глав ранее.{w} Она одному путнику трепанацию черепа провела. Циркулярной пилой наживую!"
    oleg "Что я слышал было менее ужасающим..."
    hide image liz_bukal
    show image liz_angry at left
    with byso
    liz "Хотелось бы знать кто ей нужен.{w} Отдать ей этого человека и дело с концом."
    hide image irr_mad
    show image irr_sad at right
    with byso
    play sound light_inh
    stop music fadeout 2
    "Ира достала из кармана сигарету и закурила.{w} Константин не долго думая сделал так же."
    kt "Будет кто?"
    hide image liz_angry
    show image liz_smile at left
    with byso
    play music deadrazy2
    liz "Нет, спасибо."
    hide image oleg_shy
    show image oleg_think
    with byso
    oleg "Я тоже не хочу..."
    hide image irr_sad
    show image irr_laugh at right
    with byso
    irr "Какой ты щедрый.{w} Ты же знаешь что сигаретами можешь услуги у Гордона и в столовой оплачивать?"
    kt "Да, мне Лиза рассказала."
    hide image irr_laugh
    show image irr_normal at right
    with byso
    "Ира усмехнулась и пожала плечами."
    hide image liz_smile
    show image liz_bukal at left
    with byso
    liz "Ладно, не знаю как вам, но мне хватит.{w} Спать хочу."
    hide image oleg_think
    show image oleg_shy
    with byso
    "В ответ Олег лениво потянулся."
    oleg "Да, мне б тоже в казарму..."
    kt "А где я сплю?"
    hide image oleg_shy
    show image oleg_think
    with byso
    oleg "Робокошка вроде сказала дом 1-И."
    hide image irr_normal
    show image irr_happy at right
    with byso
    "Ира хихикнула."
    hide image liz_bukal
    show image liz_angry at left
    with byso
    irr "Это мой домик. Ну ничего, я подвинусь."
    "Лизу обидели подобные известия."
    liz "Чёртова консервная банка!{w} А мне никак соседа не найдут, одиноко так-то!"
    hide image liz_angry
    show image liz_rage at left
    with byso
    liz "Да и какого хрена железяка Гордона определяет койки?!"
    hide image oleg_think
    show image oleg_smile
    with byso
    oleg "Ой, всё.{w} Пошли давай, завтра ему и закатишь концерт."
    hide image liz_rage
    show image liz_sad at left
    with byso
    "Лиза тяжело вздохнула и помотала головой."
    kt "Давайте, спокойной ночи."
    irr "Доброй..."
    liz "Споки."
    oleg "Доброй!"
    play sound door_cl
    hide image liz_sad
    hide image oleg_smile
    hide image irr_happy
    show image irr_normal
    with byso
    "Олег и Лиза ушли из библиотеки."
    irr "Давно их знаешь?"
    "Затушив сигарету поинтересовалась Ира."
    kt "Олега вижу первый день. {w}Лизу я знал 2 дня как Женю."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "А, классика. Издержки поисковых отрядов.{w} Ты тут первый цикл?"
    "Константин затушил сигарету и кивнул."
    kt "Это плохо?"
    hide image irr_happy
    show image irr_laugh
    with byso
    irr "Напротив. Очень хорошо.{w} Рассудок не мутнеет и внешность остаётся оригинальной."
    hide image irr_laugh
    show image irr_happy
    with byso
    irr "Пошли в домик?"
    "Константин кивнул."
    hide image irr_happy
    show image irr_normal
    with byso
    irr "Знаешь, вот так иногда глянешь на многих рядовых, так они вообще 1 к 1 как пустышки инреальности."
    hide image irr_normal
    scene bg ext_library_night
    show image irr_normal
    with byso
    play sound door_cl
    play ambience ambience_camp_entrance_night
    "Они вышли из библиотеки."
    kt "Да, неприятно когда ты выглядишь идентично какому-то левому чуваку."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Агась, точно. Наложить ещё то, что этот чувак даже и не человек."
    hide image irr_happy
    show image irr_normal
    with byso
    "Константин усмехнулся, Ира глянула в небо."
    irr "Как вообще сюда попасть угораздило?"
    kt "Ну изначально я работал в <<Полимере>>..."
    "Константин кратко пересказал свою историю."
    hide image irr_normal
    show image irr_shy
    with byso
    irr "Вау. Интересная история, завидую."
    kt "А ты чего?"
    hide image irr_shy
    show image irr_sad
    with byso
    "Ира грустно глянула в небо."
    irr "Я была специалистом по химической технологии.{w} 26 лет, жила я одна.{w} Личность я достаточно вспыльчивая и циничная, потому у меня были проблемы с коллегами."
    irr "Просто в один день пока я была в лаборатории и работала, произошла утечка метана."
    irr "Метан ядовит и взрывоопасен, при том в чистом состоянии он не имеет запаха.{w} Датчики ничего не зафиксировали и когда я зажгла лампу Бунзена..."
    irr "Бух-х."
    irr "И теперь я тут."
    kt "Да-а, жуть.{w} Смерть, которая подкрадывается неожиданно - самая страшная."
    hide image irr_sad
    show image irr_happy
    with byso
    "Ира усмехнулась и перевела взгляд на Константина."
    irr "В точку."
    hide image irr_happy
    scene bg ext_house_of_mi_night
    show image irr_normal
    with fade
    irr "А вот и домик."
    stop music fadeout 3
    $ volume(0.3, "ambience")
    play sound sfx_unlock_medpunkt_door
    hide image irr_normal
    scene bg int_house_of_kt_night 
    show image irr_happy
    with byso
    "Она открыла дверь и дала дубликат Константину."
    irr "Добро пожаловать, собственно."
    kt "Да уж, выглядит получше домика вожатой."
    hide image irr_happy
    show image irr_shy
    with byso
    "В ответ Ира хмыкнула."
    irr "А ты с вожатой был как Семёны?"
    kt "Ага."
    hide image irr_shy
    show image irr_normal
    with byso
    irr "Ух-х, тяжко.{w} Не покурить даже нормально."
    hide image irr_normal
    show image irr_happy
    with byso
    irr "Так что, поболтаем ещё немного или ты спать?"
    window hide
    menu:
        "Давай поболтаем, почему нет.":
            $ renpy.block_rollback()
            $ irrscore += 1;
            hide image irr_happy
            show image irr_laugh
            with byso
            play music exodus fadein 4
            irr "Класс.{w} Садись, у меня есть чем проставиться."
            play sound sfx_open_table
            "Он сел на стул, а Ира достала из тумбочки пару банок пива <<Жигулёвское>>."
            hide image irr_laugh
            show image irr_normal
            with byso
            irr "Пивком не брезгуешь?"
            "Константин был приятно удивлён и улыбнулся."
            kt "Конечно нет.{w} Спасибо.{w} Но откуда у тебя пивас?"
            hide image irr_normal
            show image irr_grin
            with byso
            "Ира игриво подмигнула."
            irr "Есть связи."
            hide image irr_grin
            show image irr_normal
            with byso
            play sound banka
            "Раздался приятный звук открытия пивной банки."
            kt "Ну что, за знакомство?"
            irr "За знакомство."
            "Они стукнулись банками и отпили понемногу.{w} Пиво было вкусным, по всем традициям СССР."
            hide image irr_normal
            show image irr_sad
            with byso
            irr "Знаешь, я иногда задумывалась.{w}.. Как же можно было до такого докатиться."
            kt "Ты про что?"
            "Ира сняла с банки ключ-кольцо и убрала в карман."
            irr "Красный аттестат, красный диплом...{w} А теперь красная инреальность."
            "Константин усмехнулся."
            kt "А почему инреальность то красная?"
            hide image irr_sad
            show image irr_happy
            with byso
            irr "Не знаю. Цвет свитера Генды."
            "С той же усмешкой ответила она."
            hide image irr_happy
            show image irr_normal
            with byso
            kt "Ну, что касается твоего вопроса.{w}.. Не знаю.{w} Сам был тем ещё отбросом."
            kt "25 лет я прожил по сути зря."
            kt "Ничего не достиг.{w} Работал на 40 тысяч в месяц без учёта 30, которые постоянно задерживались и куда-то пропадали.{w} Пил каждый второй день."
            kt "Как по мне это и жизнью назвать сложно."
            kt "Может Генда в этом плане не совсем скотина, в кой то мере я хоть избавился от того ужаса."
            kt "Просто сижу в новом теле думаю о том как свергнуть того же самого Генду."
            "Константин сделал глоток пива."
            kt "Но всё-таки это уже лучше обычного предновогоднего пьяного дня."
            hide image irr_normal
            show image irr_sad
            with byso
            "Ира кивнула и посмотрела в окно."
            irr "Не перестаю задумываться о том что сопротивление слишком переоценивает человеческую жизнь, как это и было в нашем мире."
            irr "Только тут у нас порождения инреальности.{w} Хоть и на половину."
            hide image irr_sad
            show image irr_angry
            with byso
            irr "И тогда спрашивается, захера нам надо спасать этих полу-пустышек из своих симуляций?{w} Пусть там и гниют."
            irr "В отличие от нас они уже частично утеряли свой реальный облик.{w} Может моя мысль чем-то схожа с расизмом, но это даже не раса."
            kt "Насчёт переоценённости согласен, но насчёт полу-пустышек не могу сказать точно."
            hide image irr_angry
            show image irr_grin
            with byso
            irr "Знаешь, а мы может и подружимся."
            kt "Не исключено."
            "С усмешкой ответил Константин и допил пиво."
            hide image irr_grin
            show image irr_normal
            with byso
            irr "Слушай, а тебе случаем капитан не давал рекомендаций по работе в сопротивлении?"
            kt "Давал.{w} Либо отряд Лизы, либо разведка."
            hide image irr_normal
            show image irr_happy
            with byso
            "Лицо Иры расплылось в улыбке."
            irr "А не хочешь со мной в разведку?{w} Мне как раз не хватает умных и интересных людей."
            "Константин пожал плечами и улыбнулся в ответ."
            kt "Не знаю. Ещё подумаю."
            hide image irr_happy
            show image irr_laugh
            with byso
            irr "Думай, но в случае чего я всегда рада видеть тебя в разведпункте."
            hide image irr_laugh
            show image irr_normal
            with byso
            irr "Ну что, по койкам?" 
            kt "Ага."
            "Ответил Константин и сел на кровать."
            stop music fadeout 3
        "Не, прости. Измотали меня покатушки по инреальности.":
            $ renpy.block_rollback()
            $ lizrp += 1;
            hide image irr_happy
            show image irr_sad
            with byso
            irr "Ладненько, всё понимаю."
            "Константин снял с себя пионерский галстук и положил на свою тумбочку."
            th "Мне это больше не нужно."
    irr "Слушай, отвернись на секунду, я разденусь."
    hide image irr_sad
    hide image irr_normal
    with byso
    "Константин повернул голову в другую сторону."
    "Спустя четверть минуты, Ира быстро запрыгнула в кровать."
    "Константин снял с себя рубашку и ботинки, после чего лёг в кровать."
    kt "Спокойной ночи."
    irr "Взаимно."
    show blink
    stop ambience fadeout 2
    "Константин закрыл глаза и мигом провалился в сон."
    jump d4_withspr