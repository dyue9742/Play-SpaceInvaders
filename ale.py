from ale_py import ALEInterface
from random import randrange
import sys

sys.path.append("./src")
from WriteFile import write_and_save

if len(sys.argv) < 2:
    print('Usage: %s rom_file' % sys.argv[0])
    sys.exit()

ale = ALEInterface()

USE_SDL = False
if USE_SDL:
    ale.setBool(b'sound', False)
    ale.setBool(b'display_screen', True)

rom_file = str.encode(sys.argv[1])
ale.loadROM(rom_file)

legal_actions = ale.getLegalActionSet()
screen = ale.getScreenRGB()
write_and_save(screen, "png")

total_reward = 0
while not ale.game_over():
    a = legal_actions[randrange(len(legal_actions))]
    reward = ale.act(a)
    total_reward += reward
print(total_reward)

ale.reset_game()
