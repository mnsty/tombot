import telebot


token = '7002082878:AAFkxOlM93FSnU4oJCk8xU7_uxvIZf42DQQ git'
bot = telebot.TeleBot(token)

name = 'Tom'
energy = 70
satiety = 10
happiness = 100

def feed():
    global satiety, energy
    satiety += 10
    energy += 5

def play():
    global satiety, happiness, energy
    satiety -= 5
    energy -= 10
    happiness += 10

def sleep():
    global energy, happiness, satiety
    satiety -= 5
    happiness -= 5
    energy = 70


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'working!')

@bot.message_handler(commands=['game'])
def game(message):
    bot.send_message(message.chat.id, 'Вы начали игру с Томом')

@bot.message_handler(commands=['feed'])
def feed_handler(message):
    bot.send_message(message.chat.id, 'Вы покормили Тома')
    feed()
    check(message)

def check(message):
    global energy, satiety, happiness, name
    if satiety <= 0:
        bot.send_message(message.chat.id, f'{name} умер от голода. Не забывайте его кормить!')
    elif satiety <= 10:
        bot.send_message(message.chat.id, f'{name} очень хочет кушать!!!')
    elif satiety >= 15:
        bot.send_message(message.chat.id, f'{name} наелся и счастлив.')
    elif happiness < 0:
        bot.send_message(message.chat.id, f'{name} умирает от скуки и очень хочет играть!')
    elif energy <= 20:
        bot.send_message(message.chat.id, f'{name} очень устал и хочет отдохнуть.')
    elif energy <= 0:
        bot.send_message(message.chat.id, f'{name} умер от нехватки энергии!')
    elif energy > 20:
        bot.send_message(message.chat.id, f'{name} полон сил и энергии!')

@bot.message_handler(commands=['specific'])
def specific(message):
    global name, energy, satiety, happiness
    bot.send_message(message.chat.id, f'Питомца зовут: {name}\nУровень энергии: {energy}\nУровень сытости: {satiety}\nУровень счастья: {happiness}\n')




bot.polling(none_stop=True)
