F = open('asdasd.txt', 'r', encoding='utf-8')
all_students = []
for i in F:
    ind = 0
    student_info = i.split()[-23:]
    student = {'Female': '', 'is_18': '', 'Glasses': '', 'Eyes': '', 'Hair': '',
               'Siblings': '', 'Pets': '', 'from_Peter': '', 'Iphone': '', 'Tushavin': '', 'Coffee': '', 'Food': '',
               'Watches': '', 'Name_Ending': '', 'Pizza': '', 'Smoke': '', 'Height': '', 'Love': '', 'Winter_born': '',
               'Games': '', 'Obshaga': '', 'Films': '', 'Anime': ''}
    for key in list(student.keys()):
        if student_info[ind] == 'Да' or student_info[ind] == 'да':
            student[key] = True
        else:
            student[key] = False
        ind += 1
    all_students.append([' '.join(i.split()[2:-23]), student])

def yesno(a):
    if a == 'Да' or a == '+':
        return True
    elif a == 'Нет' or a == '-':
        return False
    return "Неправильный ввод."
def questions(all_students):
    Female = yesno(input('Этот человек девушка?: '))
    is_18 = yesno(input('Ему/ей 18?: '))
    Glasses = yesno(input('Он/она носит очки?: '))
    Eyes = yesno(input('У него/нее карие глаза?: '))
    Hair = yesno(input('У него/нее темные волосы?: '))
    Siblings = yesno(input('У него/нее есть брат или сестра?: '))
    Pets = yesno(input('У него/нее есть домашние питомцы?: '))
    from_Peter = yesno(input('Он из Питера?: '))
    Iphone = yesno(input('У него/нее iPhone?: '))
    Tushavin = yesno(input('У него/нее практику ведет Тушавин?: '))
    Coffee = yesno(input('Он/она предпочитает кофе чаю?: '))
    Food = yesno(input('Он/она любит домашнюю еду, а не фастфуд?:' ))
    Watches = yesno(input('Он/она носит часы?: '))
    Name_Ending = yesno(input('Его/ее имя начинается с гласной?: '))
    Pizza = yesno(input('Ему/ей больше нравится пицца, чем суши?: '))
    Smoke = yesno(input('Он/она курит?: '))
    Height = yesno(input('Его/ее рост больше 175см?: '))
    Love = yesno(input('У него/ее есть вторая половинка?: '))
    Winter_born = yesno(input('Он/она родился зимой или весной?: '))
    Games = yesno(input('Он/она играет в КС или Доту?: '))
    Obshaga = yesno(input('Он/она живет в общаге?: '))
    Films = yesno(input(('Он/она любит смотреть фильмы больше, чем сериалы?: ')))
    Anime = yesno(input('Он/она смотрит аниме?: '))
    student = {'Female': Female, 'is_18': is_18, 'Glasses': Glasses, 'Eyes': Eyes, 'Hair': Hair,
               'Siblings': Siblings, 'Pets': Pets, 'from_Peter': from_Peter, 'Iphone': Iphone, 'Tushavin': Tushavin, 'Coffee': Coffee, 'Food': Food,
               'Watches': Watches, 'Name_Ending': Name_Ending, 'Pizza': Pizza, 'Smoke': Smoke, 'Height': Height, 'Love': Love, 'Winter_born': Winter_born,
               'Games': Games, 'Obshaga': Obshaga, 'Films': Films, 'Anime': Anime}
    for i in all_students:
        if i[1] == student:
            return i[0]
    return 'Человека с такими параметрами нет в группе, или вы неправильно ввели данные.'
print(questions(all_students))