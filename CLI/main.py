import typer
import keyboard
import time
import os

app = typer.Typer()

@app.command()
def siri(question : str):
    keyboard.press('command+space')
    time.sleep(0.3)
    keyboard.release('command+space')
    time.sleep(0.2)  # Wait for Siri to load
    keyboard.write(question)
    keyboard.send('enter')

@app.command()
def mic():
    cmd = """osascript -e 'tell application "System Preferences" to activate'"""
    os.system(cmd)
    cmd = """osascript -e 'tell application "System Preferences"
                                reveal anchor "input" of pane id "com.apple.preference.sound"
                            end tell'"""
    os.system(cmd)
    time.sleep(0.5)
    cmd = """osascript -e 'tell application "System Events" to tell process "System Preferences"
                                tell table 1 of scroll area 1 of tab group 1 of window 1
                                    select (row 1 where value of text field 2 is "Aggregate device")
                                end tell
                            end tell'"""
    os.system(cmd)
    cmd = """osascript -e 'quit application "System Preferences"'"""
    os.system(cmd)

if __name__ == "__main__":
    app()