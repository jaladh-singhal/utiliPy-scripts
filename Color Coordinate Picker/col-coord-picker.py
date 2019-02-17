import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + '\t\tY: ' + str(y).rjust(4)
        pixCol=pyautogui.screenshot().getpixel((x, y))
        positionStr+='\t\tRGB: (%s,%s,%s)'%(str(pixCol[0]).rjust(3),str(pixCol[1]).rjust(3),str(pixCol[2]).rjust(3))
        print(positionStr, end='\r', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
