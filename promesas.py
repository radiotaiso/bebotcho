import random

promesas_list = ['Aborto legal hasta los 112 meses en todo el país',
        'Anticonceptivos en el agua potable',
        'Nadie trabajará los lunes en mi gabinete',
        'Negociaremos que "EL MURO" nos separe de chiapas y sudamerica',
        'Habrá animalitos bebé en todas las oficinas']

class campaign():
    promis = ''

    def promesa_random():
        random_choice = random.choice(promesas_list)
        return random_choice

    promis = promesa_random()
