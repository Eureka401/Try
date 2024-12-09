import time


def restart_game(state):
    """Simulates loading time while restarting"""
    print("Restarting Level ", end = "", flush = "True")
    time.sleep(0.3)
    print(".", end = "", flush = "True")
    time.sleep(0.3)
    print(".", end = "", flush = "True")
    time.sleep(0.3)
    print(".", end = "", flush = "True")
    time.sleep(0.6)
    state.restart()
    return state
