from cx_Freeze import setup, Executable

setup(
    name = "File Manager",
    version = "0.1",
    description = "че сюда писать",
    # если приложение консольное то пишем - base=None
    # если приложение с графическим интерфейсом то пишем - base='Win32GUI'
    executables = [Executable("main.py" , base="Win32GUI" , icon="5845-Photoroom.ico")]
)