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
    """Один шаг симуляции: ход существ + отрисовка"""
    turn_actions.make_all_move(map)
    Renderer.to_render(map)
    winner = turn_actions.find_winner(map)
    if winner:
        with LOCK:
            SIMULATION_RUNNING = False
        if winner == "herbivore":
            print("\n🎉 Вся трава съедена. Козы победили!")
        elif winner == "predator":
            print("\n🎉 Все козы съедены. Лисы победили!")
        sys.exit(0)


def start_game_loop(map: Map):
    """Бесконечный цикл симуляции"""
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

            # Выполняем шаг и рендерим
            make_one_step(map)
            print("Нажмите 'p' для паузы")
            winner = turn_actions.find_winner(map)
            if winner:
                sys.exit(0)
            time.sleep(2)  # пауза между шагами

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

            if key == "p":  # Пауза
                with LOCK:
                    SIMULATION_PAUSED = True
                print("\n[ПАУЗА] Введите: 'p' — продолжить, 'm' — выйти в меню")

                # Режим паузы: ждём команду
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
    """Основное меню"""
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

            # Запускаем потоки
            sim_thread = threading.Thread(
                target=start_game_loop, args=(map,), daemon=True
            )
            input_thread = threading.Thread(target=listen_for_input, daemon=True)

            sim_thread.start()
            input_thread.start()

            # Ждём завершения симуляции
            while sim_thread.is_alive():
                time.sleep(0.1)
            break

        elif choice == "e":
            print("Программа завершена. До свидания!")
            break

        else:
            print("Неверный ввод. Попробуйте ещё раз.")
