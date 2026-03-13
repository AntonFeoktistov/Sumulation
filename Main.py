from map.map import Map
from renderer.renderer import Renderer
from actions import init_actions
from simulation.game_loop import main_menu

if __name__ == "__main__":
    print("Добро пожаловать в симуляцию!")
    map = Map(15, 10)
    init_actions.initialize_map(map)
    Renderer.to_render(map)
    main_menu(map)
