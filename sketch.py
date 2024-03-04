from p5 import *


def setup():
  createCanvas(windowWidth,windowHeight,WEBGL)

  #loadImage('kampua.png','kampua')
  loadImage('2k_sun.jpeg','sun')
  loadImage('2k_mercury.jpeg','mercury')
  loadImage('2k_venus.jpeg','venus')
  loadImage('2k_earth.jpeg','earth')
  loadImage('2k_mars.jpeg','mars')
  loadImage('2k_jupiter.jpeg','jupiter')
  loadImage('2k_saturn.jpeg','saturn')
  loadImage('2k_uranus.jpeg','uranus')
  loadImage('2k_neptune.jpeg','neptune')
  loadImage('2k_ring.png','ring')
  loadImage('2k_stars_milky_way.jpeg','stars')


def draw():

  background("black")
  #drawTickAxes()
  orbitControl()
  noStroke()

  #GALAXY CREATION
  #FRONT BOX
  push()
  translate(0,0,200*10)
  texture(assets['stars'])
  plane(200*20,200*20)
  pop()
  
  #BACK
  push()
  translate(0,0,-200*10)
  texture(assets['stars'])
  plane(200*20,200*20)
  pop()

  #TOP
  push()
  translate(0,200*10,0)
  rotateX(90)
  texture(assets['stars'])
  plane(200*20,200*20)
  pop()

  #BOTTOM
  push()
  translate(0,-200*10,0)
  rotateX(90)
  texture(assets['stars'])
  plane(200*20,200*20)
  pop()

  
  push()
  translate(200*10,0,0)
  rotateY(90)
  texture(assets['stars'])
  plane(200*20,200*20)
  pop()

  push()
  translate(-200*10,0,0)
  rotateY(90)
  texture(assets['stars'])
  plane(200*20,200*20)
  pop()
  #RINGS
  
  #Sun
  push()
  texture(assets['sun'])
  rotateY(millis()/100)
  sphere(110)
  pop()
  
  #mercury
  push()
  texture(assets['mercury'])
  rotateY(millis()/30)  #rev around sun
  translate(150,0,0)
  rotateX(millis()/70) #rot around its own axis
  sphere(10)
  pop()
  #mercury trail
  push()
  noFill()
  stroke("white")
  rotateX(90)
  arc(0,0,150*2,150*2,-millis()/30,0)
  pop()
  

  
  #venus
  push()
  texture(assets['venus'])
  rotateY(millis()/40)  #rev around sun
  translate(200,0,0)
  rotateX(millis()/50) #rot around its own axis
  sphere(20)
  pop()
  #venus trail
  push()
  noFill()
  stroke("orange")
  rotateX(90)
  arc(0,0,200*2,200*2,-millis()/40,0)
  pop()


  
  #earth
  push()
  texture(assets['earth'])
  rotateY(millis()/50)
  translate(250,0,0)
  rotateX(millis()/60)
  sphere(25)
  pop()
  #earths trail
  push()
  noFill()
  stroke("midnightblue")
  rotateX(90)
  arc(0,0,250*2,250*2,-millis()/50,0)
  pop()
  #mars
  push()
  texture(assets['mars'])
  rotateY(millis()/90)
  translate(300,0,0)
  rotateX(millis()/60)
  sphere(15)
  pop()

  #mars trail
  push()
  noFill()
  stroke("pink")
  rotateX(90)
  arc(0,0,300*2,300*2,-millis()/90,0)
  pop()
  #jupiter
  push()
  texture(assets['jupiter'])
  rotateY(millis()/200)
  translate(350,0,0)
  rotateX(millis()/10)
  sphere(40)
  pop()
  #jupiter trail
  push()
  noFill()
  stroke("grey")
  rotateX(90)
  arc(0,0,350*2,350*2,-millis()/200,0)
  pop()
  #saturn
  push()
  texture(assets['saturn'])
  rotateY(millis()/250)
  translate(450,0,0)
  rotateX(millis()/10)
  sphere(35)
  push()
  rotateX(90)
  rotateY(20)
  rotateZ(frameCount)
  torus(50,5)
  pop()
  pop()
  #saturn trail
  push()
  noFill()
  stroke("yellow")
  rotateX(90)
  arc(0,0,450*2,450*2,-millis()/250,0)
  pop()



  
  #uranus
  push()
  texture(assets['uranus'])
  rotateY(millis()/300)
  translate(500,0,0)
  rotateX(millis()/10)
  sphere(30)
  pop()
  #uranus trail
  push()
  noFill()
  stroke("lightblue")
  rotateX(90)
  arc(0,0,500*2,500*2,-millis()/300,0)
  pop()
  #neptune
  push()
  texture(assets['neptune'])
  rotateY(millis()/350)
  translate(550,0,0)
  rotateX(millis()/15)
  sphere(30)
  pop()
  #neptune trail
  push()
  noFill()
  stroke(66, 135, 245)
  rotateX(90)
  arc(0,0,550*2,550*2,-millis()/350,0)
  pop()
  


  '''
  My Very Educated Mother Just Served Us Noodles
  Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune
  
  
  '''
  
  
  











#My Very Educated Mother Just Served Us Noodles
#Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune
#kampua
