# lista que contiene diccionarios
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # list comprehensions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    # funciones superiores filter y map
    all_python_devs1 = list(filter(lambda worker: worker["language"]=="python", DATA))
    all_python_devs1 = list(map(lambda worker: worker["name"], all_python_devs1))

    # list comprehensions
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    # funciones superiores filter y map
    all_Platzi_workers1 = list(filter(lambda worker: worker["organization"]=="Platzi", DATA))
    all_Platzi_workers1 = list(map(lambda worker: worker["name"], all_Platzi_workers1))

    # funciones superiores filter y map
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    # list comprehensions
    adults1 = [worker["name"] for worker in DATA if worker["age"] > 18]

    # funciones superiores filter y map
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70},DATA)) #agrego una nueva
    # list comprehensions
    old_people1 = [worker | {"old": worker["age"] > 70} for worker  in DATA]


    #print(all_python_devs)
    #print(all_python_devs1)
    #print(all_Platzi_workers)
    #print(all_Platzi_workers1)
    #print(adults)
    #print(adults1)
    print(old_people)
    print(old_people1)

if __name__ == "__main__":
    run()