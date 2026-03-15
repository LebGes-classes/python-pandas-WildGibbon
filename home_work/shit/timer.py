import tkinter as tk
import os

def set_shutdown_timer(timing: float) -> None:
    """
    Планирует выключение системы через указанное количество часов.

    Args:
        timing: Задержка в часах перед выключением системы.
    """
    os.system(f"shutdown -s -t {int(timing * 3600)}")

def cancel_shutdown() -> None:
    """
    Отменяет ранее запланированное выключение системы.
    """
    os.system("shutdown -a")

def main() -> None:
    """
    Создает простой графический интерфейс для установки и отмены таймера выключения системы.
    """
    window = tk.Tk()
    window.geometry("300x200")
    window.title("Таймер выключения")

    entry = tk.Entry(window)
    entry.pack()

    tk.Button(window, text="Установить таймер (часы)", command=lambda: set_shutdown_timer(float(entry.get()))).pack()
    tk.Button(window, text="Отмена", command=cancel_shutdown).pack()

    window.mainloop()

if __name__ == "__main__":
    main()
