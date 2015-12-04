#!/usr/bin/python3

import time, random, sys

def choosePerson(wantedInfo):
    assert wantedInfo == 'person' or wantedInfo == 'item', 'Bad argument.'
    person = random.choice(people)
#    if random.randint(0, 1) == 0:
#        item = random.choice(peopleHelpers)
#    else:
    item = random.choice(weapons)
    if wantedInfo == 'person':
        return person
    elif wantedInfo == 'item':
        return item


def getWeaponPower(item):
    return weaponPower[item]


def getBestInventoryWeapon():
    bestItemPower = 0
    for item in inventory:
        if getWeaponPower(item) > bestItemPower:
            bestItemPower = getWeaponPower(item)
    return bestItemPower


def personInteraction():
    newPerson = choosePerson('person')
    npi = choosePerson('item')
    print('You see a(n) ' + newPerson + ' in the distance. Do you choose to approach (y/n)?')
    time.sleep(2)
    if input() == 'y':
        print()
        print('The ' + newPerson + ' pulls out a(n) ' + npi + ' threateningly.')
        time.sleep(1)
        if getBestInventoryWeapon() + playerPower > getWeaponPower(npi) + peoplePower[newPerson]:
            print('The ' + newPerson + ' has been defeated!')
        elif getBestInventoryWeapon() == weaponPower[npi]:
            print('Draw!')
        else:
            print('You\'re dead!')

    else:
        print()

people = ['old lady', 'baby']
peoplePower = {'old lady': 1, 'baby': 1}
weapons = ['knife', 'gun', 'cane', 'fist', 'sword']
peopleHelpers = []
weaponPower = {'stick': 5, 'gun': 50, 'cane': 6, 'fist': 3, 'sword': 40, 'knife': 10}
inventory = ['stick']
health = 100
coins = 100
playerPower = 5


personInteraction()
