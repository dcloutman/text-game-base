from src.content.lands.generic import PlainLandNode
from src.content.lands.generic import HillyLandNode

default_spawn_point = PlainLandNode()
hill_country_w1_0 = HillyLandNode()
hill_country_w1_n1 = HillyLandNode()
hill_country_w1_n1.connect_neighbor_south(hill_country_w1_0)
default_spawn_point.connect_neighbor_west(hill_country_w1_0)

print(default_spawn_point)
