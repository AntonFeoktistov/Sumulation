from Map.Map import Map
from Renderer.Renderer import Renderer
from Actions import init_actions

map = Map(15, 10)
init_actions.initialize_map(map)
Renderer.to_render(map)
