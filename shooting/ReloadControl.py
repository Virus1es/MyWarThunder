class ReloadControl:
    def __init__(self):
        print("Модуль Управление Перезарядкой")

    # Индикация перезарядки: Отображение прогресса перезарядки оружия в виде визуальной шкалы или анимации.
    def PrintRealoadTime(self, time):
        print(f"До кончания перезарядки осталось: {time} c.")

    # Звуковое оповещение: Звуковое оповещение об окончании процесса перезарядки.
    def VoiceAlertReloadEnd(self):
        print("Перезарядка звершена")

    # Автоматическая перезарядка: Автоматическая перезарядка оружия после каждого выстрела
    # (или после окончания обоймы).
    def AutomaticReload(self, isAutoReaload):
        if isAutoReaload:
            print("Включена автоматическая перезарядка")
        else:
            print("Автоматическая перезарядка отключена")

    # Принудительная перезарядка: Возможность принудительной перезарядки оружия в любое время (
    # с возможной задержкой).
    def InitReload(self):
        print("Начата принудительная перезарядка")