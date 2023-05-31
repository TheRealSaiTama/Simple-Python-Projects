import pyscreenshot
import PIL

capture = pyscreenshot.grab() #to capture the screen

#to display captured screen
capture.show()

#to save screenshot
capture.save("capturedthroughscript.jpg")
