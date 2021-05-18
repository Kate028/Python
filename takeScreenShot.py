# install pyscreenshot

import pyscreenshot

# To capture the screen
image = pyscreenshot.grab()

# for partial ss
# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))

# image = pyscreenshot.grab(bbox=(10, 10, 500, 500))

# To display the captured screenshot
image.show()

# To save the ss
image.save("ss.png")

