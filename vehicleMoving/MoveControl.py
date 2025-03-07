class VehicleMoving:
    def __init__(self):
        print("Модуль Управление движением")

    # Акселерация и торможение: Управление скоростью техники с помощью клавиш газа и тормоза.
    def moveForwardAndBack(self, direction):
        if direction == "Forward":
            print("Движение вперёд")
        else:
            print("Начато тормажение")

    # Поворот: Управление направлением движения с помощью клавиш поворота или мыши.
    def rotateVehicle(self, direction):
        if direction == "Left":
            print("Начат поворот влево")
        else:
            print("Начат поворот вправо")

    # Управление форсажем (для самолетов): Включение форсажа для кратковременного увеличения скорости.
    def controleForce(self, onForce):
        if onForce:
            print("Форсаж включён")
        else:
            print("Форсаж выключен")

    # Индикация скорости: Отображение текущей скорости техники на экране.
    def showSpeed(self, speed):
        print(f"Текущая скорость: {speed} км/ч")