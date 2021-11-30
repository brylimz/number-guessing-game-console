# # Scope
#
# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function : {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
#
# # local scope
#
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()
#
#
# # Global scope
# player_health = 10
# # global scope
#
#
# def drink_potion():
#     potion_strenght = 2
#     print(player_health)
#
#
# drink_potion()

# python no block scope

# Modifying Global Scope
# enemies = 2
#
#
# def increase_enemies():
#     # global enemies
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1
#
#
# enemies = increase_enemies()
# print(f"Enemies outside function: {enemies}")


# global constants
