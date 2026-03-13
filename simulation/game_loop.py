import time
import threading
import sys
import msvcrt

from map.map import Map
from renderer.renderer import Renderer
from actions import turn_actions

# Глобальные флаги + блокировка для потокобезопасности
SIMULATION_RUNNING = False
SIMULATION_PAUSED = False
LOCK = threading.Lock()


def make_one_step(map: Map):
    turn_actions.make_all_move(map)
    Renderer.to_render(map)
    winner = turn_actions.find_winner(map)
    if winner:
        with LOCK:
            SIMULATION_RUNNING = False
        if winner == "herbivore":
            print("\nВся трава съедена. Козы победили!")
        elif winner == "predator":
            print("\nВсе козы съедены. Лисы победили!")
        sys.exit(0)


def start_game_loop(map: Map):
    global SIMULATION_RUNNING, SIMULATION_PAUSED

    with LOCK:
        SIMULATION_RUNNING = True
    try:
        while True:
            with LOCK:
                if not SIMULATION_RUNNING:
                    break
                if SIMULATION_PAUSED:
                    time.sleep(0.1)
                    continue

            make_one_step(map)
            print("Нажмите 'p' для паузы")
            time.sleep(2)
    finally:
        with LOCK:
            SIMULATION_RUNNING = False


def listen_for_input():
    """Поток, слушающий ввод пользователя"""
    global SIMULATION_RUNNING, SIMULATION_PAUSED

    while True:
        with LOCK:
            if not SIMULATION_RUNNING:
                break

        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8").lower()

            if key == "p":
                with LOCK:
                    SIMULATION_PAUSED = True
                print("\n[ПАУЗА] Введите: 'p' — продолжить, 'm' — выйти в меню")

                while SIMULATION_PAUSED and SIMULATION_RUNNING:
                    if msvcrt.kbhit():
                        cmd = msvcrt.getch().decode("utf-8").lower()
                        if cmd == "p":
                            with LOCK:
                                SIMULATION_PAUSED = False
                            print("Продолжение симуляции...")
                        elif cmd == "m":
                            with LOCK:
                                SIMULATION_RUNNING = False
                                SIMULATION_PAUSED = False
                            print("Выход в меню...")
                    time.sleep(0.05)
        time.sleep(0.05)


def main_menu(map):
    global SIMULATION_RUNNING, SIMULATION_PAUSED

    while True:
        print("s — Сделать один ход", end="| ")
        print("q — Начать бесконечную симуляцию", end="| ")
        print("e — Выйти")

        choice = input("Выберите действие: ").strip().lower()

        if choice == "s":
            make_one_step(map)

        elif choice == "q":
            print("Запускаю бесконечную симуляцию... (нажмите 'p' для паузы)")

            with LOCK:
                SIMULATION_RUNNING = False
                SIMULATION_PAUSED = False

            sim_thread = threading.Thread(
                target=start_game_loop, args=(map,), daemon=True
            )
            input_thread = threading.Thread(target=listen_for_input, daemon=True)

            sim_thread.start()
            input_thread.start()

            while sim_thread.is_alive():
                time.sleep(0.1)
            winner = turn_actions.find_winner(map)
            if winner:
                break

        elif choice == "e":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте ещё раз.")
