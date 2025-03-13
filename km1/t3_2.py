import random as rnd
import asyncio
from time import asctime
x = 2
player_sleep_time = [i/10 for i in range(40, 51)]
player_awake_time = [0.1*x, 0.2*x, 0.3*x, 0.4*x, 0.5*x]
modeling_time = 50 * x

"""
    output:
    time, Person1, persons remained, phase 
    time, Person2, persons remained, phase
    ...
    time, Person12, persons remained, phase
    
    modeling ended, remained persons
"""

class Person():
    
    def __init__(self, name, role):
        self.name = name
        self.role = role
        if role == "Leader":
            self.sleep_time = 3 * x
            self.awake_time = x
            self.phase = "Sleep"
        elif role == "Player":
            self.sleep_time = rnd.choice(player_sleep_time)
            self.awake_time = rnd.choice(player_awake_time)
            self.phase = "Awake"
        else:
            raise ValueError("Roles can be only \"Player\" or \"Leader\"")

    def change_phase(self, new_phase):
        self.phase = new_phase

async def main():
    playersNumber = 1
    taskArr = []
    playersArr = [Person("Name","Player") for i in range(playersNumber)]
    playersArr[0] = Person("Buzzy", "Player")
#    playersArr[1] = Person("John", "Player")
#    playersArr[2] = Person("Jeffrey", "Player")
#    playersArr[3] = Person("Paul", "Player")
#    playersArr[4] = Person("Dylan", "Player")
#    playersArr[5] = Person("Matt", "Player")
#    playersArr[6] = Person("Chelsea", "Player")
#    playersArr[7] = Person("Simen", "Player")
#    playersArr[8] = Person("Johnatan", "Player")
#    playersArr[9] = Person("Sam", "Player")
#    playersArr[10] = Person("Emmit", "Player")
    leader  = Person("Genry","Leader")
    taskArr.append(asyncio.create_task(status_cycle(leader)))
    taskArr.append(asyncio.create_task(rules_check(leader, playersArr)))
    for i in range (0,len(playersArr)):
        taskArr.append(asyncio.create_task(status_cycle(playersArr[i])))
    for task in taskArr:
        await task


async def rules_check(leader, playersArr):
    print(f"checking rules")
    if leader.phase == "Awake":
        for player in playersArr:
            if player.phase == "Awake":
                print(f"{player.name} is knocked out")
                playersArr.remove(player)

async def status_cycle(person):
    print(f"=== status {person.name} ===")
    while True:
        if person.role == "Player":
            print(f"{asctime()} | {person.name}({person.role}) //{person.phase}// is awake")
            await asyncio.sleep(person.awake_time)
            person.change_phase("Sleep")
            print (f"{asctime()} | {person.name}({person.role}) //{person.phase}// is sleeping")
            await asyncio.sleep(person.sleep_time)
            person.change_phase("Awake")

        if person.role == "Leader":
            print(f"{asctime()} | {person.name}({person.role}) //{person.phase}// is sleeping")
            await asyncio.sleep(person.sleep_time)
            person.change_phase("Awake")
            print (f"{asctime()} | {person.name}({person.role}) //{person.phase}// is awake")
            await asyncio.sleep(person.awake_time)
            person.change_phase("Sleep")


if __name__ == "__main__":
    asyncio.run(main())
