first =  'Мама мыла раму'
second = 'Рамена мало было'
ram = list(map(lambda x , y: x==y, first, second))
print(ram)




def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a', encoding = 'utf-8')
        for i in data_set:
           file.write(f'{i}\n')
        file.close()
    return write_everything

write = (get_advanced_writer('example.txt'))
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
write('Это строчка', ['А', 'число', 5, 'в', 'списке'], 'это', 'уже')




from random import choice
class MysticBall:
    def __init__(self, words):
        self.words = words
    def __call__(self):
        word = choice(words[0:])
        return word

words = ['snow', 'rain', 'cloudy']
first_ball = MysticBall(words)

print(first_ball())
print(first_ball())
print(first_ball())