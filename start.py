#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, session

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def start():
    try:
        session.pop('nosh')
        session.pop('flash')
    except:
        pass
    return render_template('start.html',
    title = 'Старт',
    msg = '''Приветствую тебя, путник. Это игра в жанре визуальной-новелы. Чтобы начать играть в игру или вообще как-либо на неё влиять,
          тебе нужно просто нажимать на кнопки, соотвествующие твоему ограниченному выбору. Это и есть единственное правило, помимо того, что вам лучше
          читать прежде чем принимать решения.''')


@app.route('/first_steps', methods = ['POST', 'GET'])
def first_steps():
    return render_template('first_steps.html',
    title = 'Вы проснулись',
    img = 'https://sun1.48276.userapi.com/Zq16kPsuPqs1A32B0QThnDFcrbAB08ssQBmBcw/DWBToFrwIto.jpg',
    msg = '''Вы проснулись в неизвестном вам месте.
    Вы встаете и осматриваетесь.
    Но у вас не фига не получается потому что очень темно.
    Что вы будете делать?''')


@app.route('/look-around_first_steps', methods = ['POST'])
def lookaround():
    return render_template('look-around_first-steps.html',
    title = 'Что-то нашел',
    img = 'https://sun1.48276.userapi.com/nteP8EbGfEhfz1iyXSs-ZT5uw4nblWJzAB2p7w/zRxvAyVgblw.jpg',
    msg = '''Вы выбрали: "Попробовать походить и ощупать стены"
            Проанализировав помещение, вы узнаете, что в нем есть 2 двери.
            Одна слева, другая справа, а также, на полу лежат два неизвестных вам предмета.
            Что вы сделаете?''')


@app.route('/up_flash', methods = ['POST'])
def upflash():
    session['flash'] = True
    return render_template('look_around2_first-steps.html',
    title = 'Что-то нашел',
    img = 'https://sun1.48276.userapi.com/2-c5gDwk3quwSI1k9GGCt29WCHphjCZaJbNs5Q/6fRRkrprMW0.jpg',
    msg = '''Вы выбрали: "осмотреть первый предмет"
            Предмет оказался фонариком. Вы его включаете, и свет озаряет помещение.
            Вторым предметом оказался большой острый нож.
            что вы сделаете?''')


@app.route('/up_nosh', methods = ['POST'])
def upnosh():
    if 'flash' in session:
        session['nosh'] = True
        return render_template('look_around3_first-steps.html',
        title = 'Прогресс',
        img = 'https://sun2.48276.userapi.com/qTMYYFo2qJOXHf7DiTtKhouZVMkinJ4T2NIN7g/ErKZr7Rdd7k.jpg',
        msg = '''Вы выбрали: "Подобрать нож"
                Теперь у вас есть нож, а у авторов для вас несколько ответвлений сюжета...
                Что вы сделаете? ''')
    else:
        return render_template('look-around_first-steps.html',
        title= 'Что-то есть',
        img = 'https://sun1.48276.userapi.com/wNwU5iBI0xK1HvEm87IHnfUDdXbll47wjR54jQ/nJA_E6e7q40.jpg',
        msg = ''' Вы выбрали "осмотреть второй предмет"
                На ощупь, вы понимаете, что это что то большое и острое. Брать с собой не осмеливаетесь.
                Что вы сделаете?''')


@app.route('/go_left', methods = ['POST'])
def go_left():
    return render_template('look-around_first-steps.html',
    title = 'Упс...',
    msg = ''' Вы выбрали: "пойти в левую дверь"
              Она оказалась закрытой на замок
              что вы будете делать? ''',
    img = 'https://sun1.48276.userapi.com/OpbhZp6vIRocG52_9O0lbvaRJGN-M2qXVpp4mw/S0xRgfndqUw.jpg')


@app.route('/go_right', methods = ['POST'])
def go_right():
    if 'flash' in session:
        return render_template('zombie_room.html',
        title = 'Странно...',
        img = 'https://sun1.48276.userapi.com/x0KTqDJeeuHuj8KzHepi-z_meskSJll-f9KRJQ/gKtVv8r2trQ.jpg',
        msg = ''' Вы выбрали: "Пойти в правую дверь"
                Коридор теперь можно освятить, и вы не боитесь так, как раньше. Проходите дальше и дальше.
                теперь на вашем пути ЗОМБИ! Так вот оно, кто вонял гнилью!.
                Ваши действия? ''')
    else:
        return render_template('look-around_first-steps.html',
        title = 'Странно...',
        img = 'https://sun2.48276.userapi.com/c7TmRE52tuUgrqII7WvXdlDosUAoHLceylieRw/1VL6iTiaM8c.jpg',
        msg = ''' Вы выбрали: "пойти в правую дверь"
                    Вы вышли в такой же темный коридор, как и предыдущее помещение.
                    Здесь сыро и воняет гнилью.
                    Вы слышите чей то грозный рев, пугаетесь и возвращаетесь обратно.
                    Что вы сделаете? ''')


@app.route('/nothing_zombie', methods = ['POST'])
def failed_3():
    return render_template('base.html',
    title = 'Потрачено',
    msg = ''' Вы выбрали: "ничего"
                Зомби просто подошел, посмотрел и откусил вам голову. Вы ничего не делали,
                после он повалил ваше тело, взял ваш нож и воспользовался
                им чтобы проверить, будете ли вы без головы тоже ничего делать.
                Тыкал то здесь, то там, короче потом сожрал)) ''',
    img = 'https://sun2.48276.userapi.com/hlCKkQiEVGXoSoSZd27K1ugQzpFh5qPR-2ZGuw/-BNJQOm8lOk.jpg')


@app.route('/fight_zombie', methods = ['POST'])
def fight_zombie():
    session.pop('nosh')
    return render_template('run_out.html',
    title = 'Порешан',
    msg = ''' Вы выбрали: "сразится"
                Вы Сражаете зомби ударом ножа в голову.
                Но не вытаскиваете обратно нож.''',
    img = 'https://sun2.48276.userapi.com/KELi7n0nhWgbbv4JTDTCsryMNlp0P1gUCw2adw/XdbyXSBCJ5c.jpg')


@app.route('/talk_zombie', methods = ['POST'])
def talk_zombie():
    return render_template('run_out.html',
    title = 'И всего-то',
    msg = ''' Вы выбрали: "поговорить"
            - Привет, старик. Я могу пройти дальше? У меня просто есть дикое желание пройти туда.
            - Ну привет, проходи. Я тут просто стою, потому что так сказали.
            - Кто тебе это сказал?
            - Да какой-то дядька с усами. Старый-престарый. Ты ему привет передавай, если встретишь.
            - Окей, хорошо.''',
    img = 'https://sun2.48276.userapi.com/KELi7n0nhWgbbv4JTDTCsryMNlp0P1gUCw2adw/XdbyXSBCJ5c.jpg')


@app.route('/sleep_zombie', methods = ['POST'])
def nothing_zombie():
    return render_template('run_out.html',
    title = 'Все решает сон',
    msg = ''' Вы выбрали "лечь спать"
                Вы ложитесь спать на пол. Когда вы просыпаетесь,
                вы не обнаруживаете зомби. дальше проход открыт''',
    img = 'https://sun1.48276.userapi.com/NL3thzUlhRx-Zklx5VWRGYRP6aJLCPZajCkK4g/SD8qGNPw3rY.jpg')



@app.route('/said', methods = ['POST'])
def said():
    return render_template('said.html',
    title = 'Хей, тут есть кто?',
    img = 'https://sun1.48276.userapi.com/MaLXMIs72F-yL3ngvrCgzm2PGCSBbBhqpCRKGw/T7YTu7wKE9s.jpg',
    msg = ''' Вы выбрали: "Сказать: Хей, здесь есть кто нибудь?"
    В ответ вы слышите только свое эхо и мертвую тишину после.
    Что вы сделаете?''')


@app.route('/said2', methods = ['POST'])
def said2():
    return render_template('first_steps2.html',
    title = 'Упс',
    img = 'https://sun1.48276.userapi.com/_GYbONVX3ftAuxfnMuKAZRqfMq9vJeQyZ55KoQ/SX9Wq3u8XyY.jpg',
    msg = ''' Вы выбрали: "Сказать: У меня тут девушка в купальнике лежит бес сознания! Ей нужна помощь!"
    В ответ вы слышите как то то говорит за стеной: "Что? Где? ха-ха-ха-ха, вообще-то ты в
    этом помещении один, я это знаю, потому что это я тебя сюда притащил. Упсс... Проболтался". Затем, вы
    слышите, как за стеной открывается люк, и говорящий человек закричал. Его голос плавно становился все тише
    и тише, пока не закончился звуком падения тела об землю.
    Что вы сделаете? ''')


@app.route('/sleep_first_steps', methods = ['POST'])
def sleep():
    return render_template('sleep_first_steps.html',
    title = 'Вы поспали',
    img = 'https://sun1.48276.userapi.com/XCGMpOP1JB2vDzsjps1qwKuJcTO8TdeE5k1NjA/rigxcpe--Vk.jpg',
    msg = '''Вы выбрали: "Лечь спать обратно". Вы просыпаетесь в каком-то мешке, и чувствуете как вас куда-то несут.
    Вы слышите голоса: "Эх жаль опять бракованный попался. спит вместо действий."
    Что вы будете делать?''')


@app.route('/nothing_first_steps', methods = ['POST'])
def nothing():
    return render_template('first_steps.html',
    title = 'Вы ждали',
    img = 'https://sun1.48276.userapi.com/Zq16kPsuPqs1A32B0QThnDFcrbAB08ssQBmBcw/DWBToFrwIto.jpg',
    msg = 'Вы выбрали: "Ничего". Проходит некоторое время, и ничего не происходит.')


@app.route('/nothing_sleep', methods = ['POST'])
def failed():
    return render_template('base.html',
    title = 'Потрачено',
    img = 'https://sun2.48276.userapi.com/hlCKkQiEVGXoSoSZd27K1ugQzpFh5qPR-2ZGuw/-BNJQOm8lOk.jpg',
    msg = ''' Вы выбрали: "ничего". Вас продолжают нести, тем временем, вы слышите как один из них говорит:
        "Ну что же, давай на раз, два три".
        "Раааз, Дваааа и Трииии! - затем сказали они одновременно.
        Вы чувствуете как вас бросают куда-то, полет длился примерно 30 секунд, и после разбиваетесь насмерть.''')

@app.route('/try-to-talk_sleep', methods = ['POST'])
def talk():
    return render_template('talk_sleep.html',
    title = 'Вы решили побазарить',
    img = 'https://sun1.48276.userapi.com/XCGMpOP1JB2vDzsjps1qwKuJcTO8TdeE5k1NjA/rigxcpe--Vk.jpg',
    msg = '''Вы выбрали: "Окликнуть несущих вас людей".
    Вы говорите им: "Хей!? куда вы меня тащите, что происходит?".
    В ответ вы слышите: "Блин, говорил-же, сразу ядом таких надо. Ладно, мне лень ему объяснять что и почему, скажи ты ему.
    И тут вы слышите: "Нее, все равно умрет скоро, а может, ты хочешь жить?"
    Что вы сделаете?''')


@app.route('/try-to-escape_sleep', methods = ['POST'])
def tryescape_sleep():
    if 'nosh' in session:
        return render_template('see-2-persons.html',
        title = 'Вы выбрались',
        msg = '''Вы выбрали: "попытаться выбраться"
        вы разрываете мешок ножом и выбираетесь из него в момент когда мешок раскачивали. Вы успели выбраться, а вот мешку не повезло.
        Вы осматриваетесь по быстрому. вы находитесь в каком то освещеном помещение. Видите бездонную яму, двух людей и 1 выход из из помещения.
        что вы сделаете?')''',
        img = 'https://sun2.48276.userapi.com/osW_Yr4yaGhSFjeCIS1gUWX02hbktsb3X3p-ig/izkmn2TjKKM.jpg')
    else:
        return render_template('talk_sleep.html',
        title= 'Вы привлекли внимание',
        img = 'https://sun1.48276.userapi.com/XCGMpOP1JB2vDzsjps1qwKuJcTO8TdeE5k1NjA/rigxcpe--Vk.jpg',
        msg = '''Вы выбрали"Попытаться выбраться". Вы пытаетесь сделать хоть что нибудь. брыкаетесь и толкаетесь.
        Но у вас не получается выбратся. вы слышите как один из них говорит - О ещё живой и энергичный, что ж он спать то решил.
        ладно все равное сделаем работу.
        Или ты хочешь жить?.
        Что вы сделаете?''')


@app.route('/try-to-talk_escape', methods = ['POST'])
def talk_see2():
    return render_template('talk_see2.html',
    title = 'Решили побазарить',
    img = 'https://sun2.48276.userapi.com/osW_Yr4yaGhSFjeCIS1gUWX02hbktsb3X3p-ig/izkmn2TjKKM.jpg',
    msg = ''' Вы выбрали: "Поговорите с двумя людьми'.
        - Где я? Кто вы? Что я ваще тут делаю!? - сказали вы - говорите , а иначе зарежу!
        - Тише, тише. Ты эксперимент одного старика, с которым ты подписал контракт, на проведение опытов.
        - Каких ещё опытов? Я ничего такого не помню!
        - Ну как сказать, опытом считается проверка умственных способностей и морали человека, который оказывается в подобном положении.
          Ничего не помнишь потому что, мы стерли тебе память кто ты и кем был до этого. Хотя, скорее всего ты был бомжом, потому что пришел весь грязный и с рваной одеждой.
        - И что дальше? - спросили вы
        - Ну просто иди в тот выход. Он ведет на свободу.
        Что вы сделаете? ''')


@app.route('/try-to-fight_escape', methods = ['POST'])
def fight():
    return render_template('fight_see2.html',
    title = 'Сражение',
    img = 'https://sun2.48276.userapi.com/-gIdOP1JGLmoGJbx1pesJHN_RAGg_R8CymAs8A/JUSmGkrq_cM.jpg',
    msg = ''' 'Вы выбрали: "сразиться"
            Вы нападаете ножом на первого, ослепляя фонариком второго.
            Вы протыкаете горло первому из них, второй же, пытаясь спрятаться от яркого света фонарика, отходил все назад и назад, пока не упал в яму.
            Первый, находясь в шоке, тоже отходит назад, совсем позабыв про яму, за что и поплатился.
            Мда... Вот результаты теста: ты - ужастный человек.
            Что вы сделаете?''')


@app.route('/nothing_see2', methods = ['POST'])
def nothing_see2():
    return render_template('nothing_see2.html',
    msg = '''Вы выбрали: "Ничего"
    Один из них говорит: "Воу! Никто ещё не выбирался из этого мешка. Многие пытались, но они не брали с собой нож, как ты."
    "Теперь, тебе туда" - сказал главный, указав на единственный выход из помещения.
    Что вы сделаете?''',
    img = 'https://sun2.48276.userapi.com/osW_Yr4yaGhSFjeCIS1gUWX02hbktsb3X3p-ig/izkmn2TjKKM.jpg')


@app.route('/nothing2_see2', methods = ['POST'])
def failed_2():
    return render_template('base.html',
    title = 'Потрачено',
    img = 'https://sun2.48276.userapi.com/hlCKkQiEVGXoSoSZd27K1ugQzpFh5qPR-2ZGuw/-BNJQOm8lOk.jpg',
    msg = '''Вы выбрали: "ничего"
        - "Мужик. Иди. Мы тебя отпускаем." - сказал первый!
        - "Знаешь как уходить?" - спросил второй?
        - "Мне кажется, он просто в шоке. Ладно, кидани в него камень. Вдруг очухаеться." - заявил тот, что слева.
        В вас кидают камень. Вы ничего не делаете.
        "Походу он из этих ленивых, которые ничего не делают, ну или просто аутист. Фиг знает. Раз он не реагирует на нас не как, то просто скинем его к старику тому." - констатировал другой.
        К вам подходят, берут за руки, бросают в яму. Вы падаете 30 секунд и после разбиваетесь насмерть.''')


@app.route('/jump_out', methods = ['POST'])
def jump_out():
    return render_template('base.html',
    title = 'Потрачено',
    img = 'https://sun2.48276.userapi.com/hlCKkQiEVGXoSoSZd27K1ugQzpFh5qPR-2ZGuw/-BNJQOm8lOk.jpg',
    msg = '''Вы выбрали: "Прыгнуть в яму"
            Вы разбегаетесь со всей скорости и прыгаете в бездонную яму.
            Вы начинаете долго падать, а точнее, примерно 30 секунд. Вслед за падением вы слышите как те двое говорят: "Оу,
            че он раньше так не сделал? Всю работу бы за нас выполнил. зря тащили...".
            Вы разбиваетесь на смерть.''')


@app.route('/run_out', methods = ['POST'])
def run_out():
    return render_template('run_out.html',
    title = 'Вы сбежали',
    msg = 'Вы выбрали: "сбежать", ну или же "уйти". Вы выходите, идете, или же бежите в единственный выход в помещения. После 2 минут, вы замечаете, что за вами никто не следует.',
    img = 'https://sun2.48276.userapi.com/uuQo8oDlIf0sC0uH18RbcNmiHLV62jmtmOVGoA/lhgnjQDykUc.jpg')


@app.route('/escape', methods = ['POST'])
def escape():
    return render_template('end.html',
    title = 'Вы выбрались',
    msg = '''Вы обнаруживаете дверь, открываете и
     закрываете глаза, от внезапно прилынувшего потока света. Ощущете свежий воздух. Идете дальше, слышите пение птиц.
     Как только первый восторг и слепота проходят, вы обнаруживаете, что прошли до середины дороги.''',
     img = 'https://sun2.48276.userapi.com/lMlWpdItR7xMS1Tu9LK3j5hTQYacXL6kNJ5ccg/1mqTks--TeQ.jpg')


@app.route('/final', methods = ['POST'])
def final():
    return render_template('base.html',
    title = 'Ура!)',
    msg = '''Вы слышите справа сигнал машины.
            Вы не успеваете отойти и вас сбивает машина.
            Но не насмерть.
            Продолжение следует.
            Поздравляем, вы прошли игру UnderBlockade На одну из двух концовок.
            Если эта игра окупит свои старания, то продолжение не заставит себя долго ждать.
            В планах: сделать её не такой короткой как эту, но как следствие: менее вариативную.
            Разработчики этой части игры - Саша Фризен и Герман Покровский.
            Это тип титры. ""Ето"" творение - тестовая игра. Для проверки отклика людей.
            Свои комментарии и отзывы к игре можете писать в отдельном обсуждении - https://vk.com/topic-193716797_44287288
            Спасибо за то, что прошли нашу тестовую первую игру''',
    img = 'https://sun2.48276.userapi.com/Rrd6OQJ6ybezdlg9aa1OPUHQbPOuNdkLMAc3xQ/CGHc_PoU9W0.jpg')

app.secret_key = 'itisverysecretkey'

if __name__ == '__main__':
    app.run()
