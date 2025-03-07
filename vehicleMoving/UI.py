class UserInterface:
    def __init__(self):
        print("Модуль Интерфейс пользователя")

    # Отображение доступных модулей внизу экрана.
    def showAvalibeModules(self, moduleList):
        print(f"Доступные модули: {moduleList}")

    # Напоминания по управлению сверху экрана.
    def NotifyControlHelp(self):
        print("Вывод напоминания по управлению")

    # Мини-карта в правом нижнем углу экрана.
    def showMiniMap(self):
        print("Вывод миникарты")