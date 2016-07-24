import png

#Change these variables
width = 600
height = 500
c = -.75
iterations = 20
color_multiplier = 10
x_start = -2
x_end = 2
y_start = -1.5
y_end = 1.5
filename = 'julia.png'

def isBounded(z,c): #returns iterations to become unbounded if false and -1 if true
  for i in range(iterations):
    z = pow(z,2) + c
    if abs(z) >= 2:
      return i+1

  return -1

f = open(filename,'wb')
writer = png.Writer(width,height,greyscale=True)

pixels = []

x_step = (abs(x_start) + abs(x_end))/width
y_step = (abs(y_start) + abs(y_end))/height
x = x_start
y = y_start

for png_y in range(height):
  temp = []
  for png_x in range(width):
    var = isBounded(complex(x,y),c) #pass (0,complex(x,y)) for Mandelbrot set, (complex(x,y),c) for Julia set
    if(var == -1): #set color to black if within bounds
      temp.append(0)

    elif(var*color_multiplier > 255): #set color to white if it takes more than 255 tries (when the tries are multiplied by the color multiplier)
      temp.append(255)

    else: #set color to a gradient based on tries and the color multiplier
      temp.append(var*color_multiplier)

    x = x + x_step

  pixels.append(temp)
  y = y + y_step
  x = x_start

writer.write(f,pixels)
