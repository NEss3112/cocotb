import asyncio
import random

class Game:
    def __init__(self, x):
        self.x = x
        self.players = [f'Игрок {i}' for i in range(1, 12)]
        self.leader = 'Ведущий'
        self.leader_awake = asyncio.Event()
        self.running = True
        self.start_time = asyncio.get_event_loop().time()

    def log_event(self, event):
        elapsed = round(asyncio.get_event_loop().time() - self.start_time, 2)
        print(f'[{elapsed} сек] {event}')

    async def leader_behavior(self):
        while self.running:
            sleep_time = 3 * self.x
            awake_time = self.x
            self.log_event(f'{self.leader} засыпает на {sleep_time} сек.')
            self.leader_awake.clear()
            await asyncio.sleep(sleep_time)
            
            self.log_event(f'{self.leader} проснулся!')
            self.leader_awake.set()
            await asyncio.sleep(awake_time)
    
    async def player_behavior(self, name):
        while self.running:
            sleep_time = random.uniform(4 * self.x, 5 * self.x)
            awake_time = random.uniform(0.1 * self.x, 0.5 * self.x)
            
            self.log_event(f'{name} засыпает на {sleep_time:.2f} сек.')
            await asyncio.sleep(sleep_time)
            
            if not self.running:
                return
            
            if self.leader_awake.is_set():
                self.log_event(f'\033[91m{name} проснулся, но ведущий не спит! {name} выбывает из игры!\033[0m')
                self.players.remove(name)
                if not self.players:
                    self.running = False
                return
            
            self.log_event(f'{name} проснулся и движется {awake_time:.2f} сек.')
            await asyncio.sleep(awake_time)
            
            if self.leader_awake.is_set():
                self.log_event(f'\033[91m{name} выбывает из игры!\033[0m')
                self.players.remove(name)
                if not self.players:
                    self.running = False
                    return
                        
    async def run(self):
        leader_task = asyncio.create_task(self.leader_behavior())
        player_tasks = [asyncio.create_task(self.player_behavior(name)) for name in self.players]
        
        await asyncio.sleep(50 * self.x)
        self.running = False
        
        await leader_task
        await asyncio.gather(*player_tasks, return_exceptions=True)
        
        self.log_event(f'Игра окончена. Осталось {len(self.players)} игроков.')

if __name__ == "__main__":
    x = 1      
    game = Game(x)
    asyncio.run(game.run())

