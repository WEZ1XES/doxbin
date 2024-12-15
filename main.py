import platform
import socket

def show_system_info():
    print("Информация о компьютере:")
    print(f"Имя компьютера: {socket.gethostname()}")
    print(f"Имя пользователя: {socket.getfqdn()}")
    print(f"Операционная система: {platform.system()}")
    print(f"Версия ОС: {platform.version()}")
    print(f"Архитектура системы: {platform.architecture()[0]}")
    print(f"Процессор: {platform.processor()}")
    print(f"Платформа: {platform.platform()}")

if __name__ == "__main__":
    show_system_info()
