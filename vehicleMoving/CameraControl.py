class CameraControl:
    def __init__(self):
        print("Модуль Управление камерой")

    # Вид от третьего лица: Отображение техники с видом от третьего лица.
    def showThirdPersonView(self):
        print("Включен вид от третьего лица")

    # Вид из кабины: Отображение техники с видом из кабины пилота или командира.
    def showFirstPersonView(self):
        print("Включен вид из кабины")

    # Свободная камера: Возможность перемещения камеры в любом направлении.
    def showFreeCamera(self):
        print("Включён режим свободной камеры")

    # Приближение и отдаление: Управление масштабом изображения.
    def zoomCamera(self, direction):
        if direction:
            print("Включено приближение")
        else:
            print("Включено отдаление")