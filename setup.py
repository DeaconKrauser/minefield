from cx_Freeze import setup, Executable

setup(
    name = "Minefield",
    version = "0.1",
    description = "Minefield game",
    executables = [Executable("minesweeper.py")]
)