class MonopolyBoard:
    squares = []
    squares.append({'name':'Go'})
    squares.append({'name':'Old Kent Road', 'type':'Property', 'colour':'Brown', 'rent':[2, 10, 30, 90, 160, 250]})


    chance = []
    chance.append('Spending fine £15.')
    chance.append('Bank pays you dividend of £50.')
    chance.append('Advance to Trafalgar Square. If you pass GO, collect £200')
    chance.append('Advance to GO')
    chance.append('Pay school fees of £150')
    chance.append('Advance to Mayfair.')
    chance.append('Get out of Jail free – this card may be kept until needed, or traded [{sold})')
    chance.append('You are assessed for street repairs. £40 per house, £115 per hotel.')
    chance.append('Make general repairs on all of your buildings. For each house pay £25. For each hotel pay £100.')
    chance.append('Advance to Pall Mall. If you pass GO collect £200.')
    chance.append('Take a trip to Marylebone Station. If you pass GO collect £200.')
    chance.append('Your building loan matures. Receive £150.')
    chance.append('GO TO JAIL')
    chance.append('Go back three spaces.')
    chance.append('\'Drunk in charge\'. Fine £20.')
    chance.append('You have won a crossword competition. Collect £100')

    def __init__(self):
        pass

