import time
from turtle import Screen
from hero import Hero
from vehicle_manager import VehicleManager
from game_score import GameScore

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

hero = Hero()
vehicle_manager = VehicleManager()
game_score = GameScore()
game_paused = False

screen.listen()
screen.onkey(hero.move_up, "Up")
screen.onkey(lambda: toggle_pause(), "p")
screen.onkey(lambda: restart_game(), "r")

def toggle_pause():
    global game_paused
    game_paused = not game_paused

def restart_game():
    global game_is_on, game_paused
    if not game_is_on:
        hero.reset_position()
        vehicle_manager.reset()
        game_score.reset()
        game_is_on = True
        game_paused = False

game_is_on = True
while True:
    if game_is_on and not game_paused:
        time.sleep(0.1)
        screen.update()

        vehicle_manager.create_vehicle()
        vehicle_manager.move_vehicles()

        for vehicle in vehicle_manager.all_vehicles:
            if vehicle.distance(hero) < 20:
                game_is_on = False
                game_score.display_game_over()

        if hero.has_reached_finish_line():
            hero.reset_position()
            vehicle_manager.increase_speed()
            game_score.increment_level()

    screen.update()