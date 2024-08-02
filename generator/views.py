from django.shortcuts import render
import random

def generate_nicks(n):
    names = [
        'Accidental Genius',
        'Gerald Theking',
        'Buckshot',
        'ALappy',
        'Diablo',
        'Wrath',
        'Pain',
        'Trigger Kill',
        'Callyping',
        'Skull Crusher',
        'Titanium',
        'Cosma',
        'Smoke-Air',
        'Head-Fire',
        'Victorious',
        'Hellblade',
        'Savior',
        'Gladiator',
        'Mercenary',
        'Berserker',
        'Scourge',	
        'Bunny',
        'Billy',
        'Scooby-Doo',
        'Dynamo',
        'Batman',
        'Robin',
    ]
    

    nicks = []
    for _ in range(n):
        name = random.choice(names)
        nick = f"{name}"
        nicks.append(nick)
    
    return nicks

def home(request):
    nicknames = []
    if request.method == 'POST':
        try:
            n = int(request.POST.get('n', 0))
            if n > 0:
                nicknames = generate_nicks(n)
        except ValueError:
            pass
    
    return render(request, 'home.html', {'nicknames': nicknames})
