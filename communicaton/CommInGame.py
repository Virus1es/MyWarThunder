class CommInGame:
    def __init__(self):
        print("Модуль Управление радиосвязью")

    # Выбор каналов связи: Выбор канала связи для общения с союзниками.
    def ChooseChat(self, choose):
        print(f"Выбран канал связи: {choose}")

    # Отправка быстрых сообщений: Отправка заранее определенных быстрых сообщений.
    def SendFastMessage(self, message):
        print(f"Отправлено сообщение: {message}")

    # Голосовая связь: Возможность голосового общения с другими игроками.
    def SpeekWithTeam(self, isReadyToSpeek):
        if isReadyToSpeek:
            print("Микрофон включён")
        else:
            print("Микрофон отключён")

    # Регулировка громкости: Управление громкостью радиосвязи.
    def EditVoiceLoudness(self, voiceLoudness):
        print(f"Громкость голосового чата была изменена на значение: {voiceLoudness}")
