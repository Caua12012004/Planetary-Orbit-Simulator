#IMPORTANT: YOU NEED THE TO DOWNLOAD THE ASSETS FOLDER AND PLACE IT IN THE SAME FOLDER WHERE YOUR SIMULATION IS
#OTHERWISE YOUR CODE WILL NOT RUN
#ALSO, NOT HAVING THE FONT APPOINTED BELOW WILL CAUSE THE PROGRAM TO LOOK WEIRD/WRONG

#Note on comments: this comments give a general view of what each thing does, a lot of it is repetitive and thus not 
#commented over and over again

#Note on code: this is not an easily edited code, your changes may be restricted to superficial things and/or additions
# (There is a list of suggestions for additions at the end of the code)

#Note: "To blit" something means to draw it on the screen 

#For this code to run, you need the following modules:
        # pygame
		# pygame_gui
		# math
		# os

#Here are all we need to do to import and initialize the modules: 
from cmath import sqrt
from faulthandler import disable
import pygame 
import os 
import math 
import pygame_gui
pygame.init()
pygame.font.init()

#These set the properties of our screen:
WIDTH, HEIGHT =  1400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetary Orbit Simulation")

#These are all the colors we are going to use: 
grey = (200,200,200)
black = (0,0,0)
purple = (160, 160, 160)
white = (255,255,255)
red = (255, 0, 0)

#These are all the fonts we are going to use: 
#I used the "Pokemon GB" font of this link: https://www.fontspace.com/pokemon-gb-font-f9621
#Download and installed it, and copy the path to it in the appropriate r strings
FONT_1 = pygame.font.Font(r"C:\Users\Cauã Rodrigues\Desktop\Pokemon GB.ttf", 9)
FONT_2 = pygame.font.Font(r"C:\Users\Cauã Rodrigues\Desktop\Pokemon GB.ttf", 11)
FONT_3 = pygame.font.Font(r"C:\Users\Cauã Rodrigues\Desktop\Pokemon GB.ttf", 14)
FONT_4 = pygame.font.Font(r"C:\Users\Cauã Rodrigues\Desktop\Pokemon GB.ttf", 16)
FONT_5 = pygame.font.Font(r"C:\Users\Cauã Rodrigues\Desktop\Pokemon GB.ttf", 18)
FONT_6 =  pygame.font.Font(r"C:\Users\Cauã Rodrigues\Desktop\Pokemon GB.ttf", 24)
FONT_7 = pygame.font.Font(r"C:\Users\Cauã Rodrigues\Desktop\Pokemon GB.ttf", 36)
FONT_8 = pygame.font.SysFont("comicsans", 12)
FONT_9 = pygame.font.SysFont("comicsans", 16)

#Some constants we are going to need translated to the International System:
G = 6.67428e-11
MASS_OF_SUN = 1.98892 * 10**30
MASS_OF_EARTH = 5.9742 * 10**24
AU = 149.6e6 * 1000

#Base values for names: 
name_of_p1 = "Planet 1"
name_of_p2 = "Planet 2"
name_of_p3 = "Planet 3"
name_of_star = "Star"

#Base values for mass:
mass_of_p1 = 1
mass_of_p2 = 2
mass_of_p3 = 3
mass_of_star = 1

#Base values for radius:
radius_of_p1 = 1
radius_of_p2 = 2
radius_of_p3 = 3
radius_of_star = 1

#Base values for distances:
distance_of_p1 = 1
distance_of_p2 = 2
distance_of_p3 = 3

#Base values for orbital periods (derived from equations): 
O_P_of_p1 = round(((2*3.14*distance_of_p1*AU*math.sqrt(distance_of_p1*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p1*MASS_OF_EARTH)))/31536000), 2)
O_P_of_p2 = round(((2*3.14*distance_of_p2*AU*math.sqrt(distance_of_p2*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p2*MASS_OF_EARTH)))/31536000), 2)
O_P_of_p3 = round(((2*3.14*distance_of_p3*AU*math.sqrt(distance_of_p3*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + + mass_of_p3*MASS_OF_EARTH)))/31536000), 2)

#These are images/figures for later use:        
background = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'background.jpg')), (WIDTH, HEIGHT))

star = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Sol.png')), (150, 150))

def welcome(): #This is our welcome page
	#These are some variables for our event loop:
	run = True
	clock = pygame.time.Clock()

	#These are our images and texts:
	Continue_button_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button.png')), (125,50))
	welcome_text = FONT_6.render("Hello, welcome to our planetary orbit simulator!", 1, white )
	
	#Things blitted onto the screen:
	Continue_button = Button(Continue_button_image, 1200, 700, "Continue")
	screen.blit(background, (0,0))
	screen.blit(welcome_text, (WIDTH//2 - welcome_text.get_width()//2, HEIGHT//2 - welcome_text.get_height()//2))

	#Our event loop:
	while run:
		clock.tick(60)

		for event in pygame.event.get(): #checks if we are quitting 
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN: #checks if we pressed the mouse and calls the next page
				Continue_button.checkForInput(pygame.mouse.get_pos())
				number_of_planets_page()
		
		Continue_button.update()
		Continue_button.changeColor(pygame.mouse.get_pos())

		pygame.display.update()

def number_of_planets_page(): #This is the page for getting how many planets the user wants to design
	
	MANAGER = pygame_gui.UIManager((WIDTH,HEIGHT)) #Initializes the UI Manager

	#This creates our answer box:
	number_of_planets_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((650, 455),(100,50)), manager = MANAGER, 
	object_id = "#number_of_planets")
	number_of_planets_input.set_allowed_characters('numbers') #This allows only numbers to be typed in the answer box

	#All our texts:
	Number_question = FONT_5.render("How many planets do you wish your solar system to have? (Up to 3)", 1, white)
	message = FONT_4.render("press enter when you are ready", 1, white)

	#Things blitted onto the screen:
	screen.blit(background, (0,0))
	screen.blit(Number_question, (WIDTH//2 - Number_question.get_width()//2, HEIGHT//2 - Number_question.get_height()//2))
	screen.blit(message, (WIDTH//2 - message.get_width()//2, HEIGHT//2 - message.get_height()//2 + 35))

	#Variables of our event loop:
	run = True
	clock = pygame.time.Clock()
	
	#Our event loop:
	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#number_of_planets": #This checks if we pressed enter in the answer box
				
				global planet_number #This makes the planet number a global variable for later use
				planet_number = int(number_of_planets_input.get_text())

				if planet_number == 1 or planet_number == 2 or planet_number == 3: #This checks if the answer is within our limits
					#If the answer is within our limits, we call the next page: 
					star_design_screen()

				else: # This prints an error message at the screen 
					error_message = FONT_4.render("PLANET NUMBER NOT ALLOWED", 1, red)
					screen.blit(error_message, (WIDTH//2 - error_message.get_width()//2, HEIGHT//2 - error_message.get_height()//2 + 135) )
			
			MANAGER.process_events(event)
		
		MANAGER.update(clock.tick(60)/1000)
		MANAGER.draw_ui(screen)
		pygame.display.update()

def star_design_screen(): #This is the page for designing the star
	MANAGER = pygame_gui.UIManager((WIDTH,HEIGHT))

	#These are all the images/texts/figures we are going to use:
	Continue_button_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button.png')), (125,50))
	Yes_check_mark_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button 1 check.png')), (25,20))
	star_text1 = FONT_7.render("It's time to design your star!", 1, white)
	star_text2 = FONT_3.render("What is the name of your star?", 1, white)
	star_text3 = FONT_3.render("What is the mass of your star (in units of Mass of the Sun)?", 1, white)
	star_text4 = FONT_3.render("What is the radius of your star (in units of Radius of the Sun)?", 1, white)
	star_text4 = FONT_3.render("What is the radius of your star (in units of Radius of the Sun)?", 1, white)
	message = FONT_1.render("(press enter to confirm or the check mark to type other value)", 1, white)
	Star_design_rect = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Star design.jpg')), (205, 205))

	global base_values_text #This is global for later use
	base_values_text = FONT_8.render("(The base values are written in the answer boxes, confirm your changes in case you have any!)", 1, red)

	global blow_up_message #This is global for later use
	blow_up_message = FONT_8.render("Blow up:", 1, red)

	scale_note = FONT_8.render("NOTE: changes in the mass of the star cause changes in the scale of the simulation", 1, red)

	#These are all the buttons:
	Continue_button = Button(Continue_button_image, 1199, 700, "Continue")
	Button1 = Button(Yes_check_mark_image, 245, 255, "")
	Button2 = Button(Yes_check_mark_image, 245, 405, "")
	Button3 = Button(Yes_check_mark_image, 245, 555, "")

	#These make our answer boxes global for later use:
	global name_of_star_input
	global mass_of_star_input
	global radius_of_star_input

	#These are our answer boxes with the allowed characters and the base values written:
	name_of_star_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((120, 230),(100,50)), manager = MANAGER, 
	object_id = "#name_of_star")
	name_of_star_input.set_text("Star")

	mass_of_star_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((120, 380),(100,50)), manager = MANAGER, 
	object_id = "#mass_of_star")
	mass_of_star_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	mass_of_star_input.set_text("1")

	radius_of_star_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((120, 530),(100,50)), manager = MANAGER, 
	object_id = "#radius_of_star")
	radius_of_star_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	radius_of_star_input.set_text("1")

	#These are all the thins blitted onto the screen:
	screen.blit(background, (0,0))
	screen.blit(star_text1, (100, 50))
	screen.blit(star_text2, (120, 195))
	screen.blit(star_text3, (120, 345))
	screen.blit(star_text4, (120, 495))
	screen.blit(message,(119, 217))
	screen.blit(message,(119, 367))
	screen.blit(message,(119, 517))
	screen.blit(Star_design_rect, (1098, 240))
	screen.blit(base_values_text,(105, 65 + star_text1.get_height()//2))
	screen.blit(blow_up_message, (1098, 240))
	screen.blit(star, (1125, 270))
	screen.blit(scale_note, (120, 700))

	run = True
	clock = pygame.time.Clock()

	while run:
		clock.tick(60)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#name_of_star": #This checks if we pressed enter in this specific answer box
				Button1.update() #Creates our check mark (which is a button in case we want to change the value passed)
				
				global name_of_star #This makes the variable global for later use
				name_of_star = name_of_star_input.get_text() #This stores the user input in a variable
				
				name_of_star_input.disable() #This disables the answer box so the user can not type in it anymore

			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#mass_of_star": #This checks if we pressed enter in this specific answer box
				Button2.update() #Creates our check mark (which is a button in case we want to change the value passed)
				
				global mass_of_star #This makes the variable global for later use
				mass_of_star = float(mass_of_star_input.get_text()) #This stores the user input in a variable
				
				mass_of_star_input.disable() #This disables the answer box so the user can not type in it anymore
				
				if mass_of_star >= 2: #If the user wants a star mass 2 solar masses or more, this informs him that this choice might cause unstable orbits
					error_message1 = FONT_3.render("RISK OF UNSTABLE ORBIT", 1, red)
					screen.blit(error_message1, (270, 407 - error_message1.get_height()//2))

				
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#radius_of_star": #This checks if we pressed enter in this specific answer box
				Button3.update() #Creates our check mark (which is a button in case we want to change the value passed)
				
				global radius_of_star #This makes the variable global for later use
				radius_of_star = float(radius_of_star_input.get_text()) #This stores the user input in a variable
				
				radius_of_star_input.disable() #This disables the answer box so the user can not type in it anymore
				
				global new_star_design_rect #This makes the variable global for later use
				new_star_design_rect = pygame.transform.scale(Star_design_rect, (205 + radius_of_star, 205 + radius_of_star)) #This will create a bigger background for star design in case the user wants a big radius
				
				new_star = pygame.transform.scale(star, (150 + radius_of_star, 150 + radius_of_star)) # This will create a bigger star in case the user wants a star with a bigger radius
				
				#These blits the bigger images in the screen:
				screen.blit(new_star_design_rect, (1098 - radius_of_star//2, 240 - radius_of_star//2))
				screen.blit(new_star,(1125 - radius_of_star//2, 270 - radius_of_star//2))
				screen.blit(blow_up_message, (1098 - radius_of_star//2 , 240 - radius_of_star//2)) #This is a message indicating that the image is a blow up of the original one

			if event.type == pygame.MOUSEBUTTONDOWN: #This checks if we pressed our mouse
				#These will check which button was pressed and execute its functions
				Button1.checkForInput(pygame.mouse.get_pos()) 
				Button2.checkForInput(pygame.mouse.get_pos())
				Button3.checkForInput(pygame.mouse.get_pos())
				Continue_button.checkForInput(pygame.mouse.get_pos())

			Continue_button.update()
			Continue_button.changeColor(pygame.mouse.get_pos())
			MANAGER.process_events(event)

		MANAGER.update(clock.tick(60)/1000)
		MANAGER.draw_ui(screen)
		pygame.display.update()

def planets_design_control(): #This function is used to control how many planets are going to be designed 
	#We create a list with all planets:
	global list_of_planets
	list_of_planets = ["planet1", "planet2", "planet3"]
	
	#We check which was the number of planets chosen and adapt the list for later use
	if planet_number == 1: 
		list_of_planets.remove("planet2")
		list_of_planets.remove("planet3")

	if planet_number == 2: 
		list_of_planets.remove("planet3")
	
	
	global list_of_distances
	list_of_distances = [] #This list is used for knowing if the user wants more than one planet with the same distance from the star
	#We are going to append each of the distances to the list
	#Later, we will check if any of the numbers on the list are equal
	#If they are, we raise an error message (if we continued, the program would crash)

	if "planet1" in list_of_planets:
		list_of_distances.append(distance_of_p1)
	
	if "planet2" in list_of_planets:
		list_of_distances.append(distance_of_p2)
	
	if "planet3" in list_of_planets:
		list_of_distances.append(distance_of_p3)

def planet1_design_page():
	MANAGER = pygame_gui.UIManager((WIDTH,HEIGHT))

	#These are all the images/texts/figures we are going to use:
	Continue_button_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button.png')), (125,50))
	Yes_check_mark_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button 1 check.png')), (25,20))
	planet1_text1 = FONT_7.render("It's time to design your planets!", 1, white)
	planet1_text2 = FONT_3.render("What is the name of this planet?", 1, white)
	planet1_text3 = FONT_3.render("What is the mass of this planet (in units of Mass of the Earth)?", 1, white)
	planet1_text4 = FONT_3.render("What is the radius of this planet (in units of Radius of the Earth)?", 1, white)
	planet1_text5 = FONT_3.render("What is the distance from this planet to your star(in Astronomical Units)?", 1, white)
	planet1_text6 = FONT_3.render("What is the orbital period of this planet? (in years)", 1, white)
	message = FONT_1.render("(press enter to confirm or the check mark to type other value)", 1, white)
	planet_design_rect = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space design rectangle.jpg')), (120, 120))

	global blow_up_message1
	blow_up_message1 = FONT_8.render("Blow up:", 1, red)

	global planet1
	planet1 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Planeta 1.png')), (80, 80))

	#These are all the buttons:
	Continue_button = Button(Continue_button_image, 1200, 701, "Continue")
	Button1 = Button(Yes_check_mark_image, 195, 160, "")
	Button2 = Button(Yes_check_mark_image, 195, 285, "")
	Button3 = Button(Yes_check_mark_image, 195, 410, "")
	Button4 = Button(Yes_check_mark_image, 195, 535, "")
	Button5 = Button(Yes_check_mark_image, 195, 660, "")

	#These make our answer boxes global for later use:
	global name_of_planet1_input
	global mass_of_planet1_input
	global radius_of_planet1_input
	global distance_of_planet1_input
	global orbital_period_of_planet1_input

	#These are our answer boxes with the allowed characters and the base values written:
	name_of_planet1_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 135),(100,50)), manager = MANAGER, 
	object_id = "#name_of_p1")
	name_of_planet1_input.set_text("Planet 1")

	mass_of_planet1_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 260),(100,50)), manager = MANAGER, 
	object_id = "#mass_of_p1")
	mass_of_planet1_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	mass_of_planet1_input.set_text("1")

	radius_of_planet1_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 385),(100,50)), manager = MANAGER, 
	object_id = "#radius_of_p1")
	radius_of_planet1_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	radius_of_planet1_input.set_text("1")

	distance_of_planet1_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 510),(100,50)), manager = MANAGER, 
	object_id = "#distance_of_p1")
	distance_of_planet1_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	distance_of_planet1_input.set_text("1")

	orbital_period_of_planet1_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 635),(100,50)), manager = MANAGER, 
	object_id = "#O_P_of_p1")
	orbital_period_of_planet1_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	orbital_period_of_planet1_input.set_text("1")

	#These are all the thins blitted onto the screen:
	screen.blit(background, (0,0))
	screen.blit(planet1_text1, (50, 35))
	screen.blit(planet1_text2, (80, 105))
	screen.blit(planet1_text3, (80, 230))
	screen.blit(planet1_text4, (80, 355))
	screen.blit(planet1_text5, (80, 480))
	screen.blit(planet1_text6, (80, 605))
	screen.blit(message,(80, 122))
	screen.blit(message,(80, 247))
	screen.blit(message,(80, 372))
	screen.blit(message,(80, 497))
	screen.blit(message,(80, 622))
	screen.blit(planet_design_rect, (1150, 240))
	screen.blit(base_values_text,(55, 50 + planet1_text1.get_height()//2))
	screen.blit(blow_up_message1, (1150, 240))
	screen.blit(planet1, (1170, 260))

	run = True
	clock = pygame.time.Clock()

	while run:
		clock.tick(60)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#name_of_p1": #This checks if we pressed enter in this specific answer box
				Button1.update() #Creates our check mark (which is a button in case we want to change the value passed)
				
				global name_of_p1
				name_of_p1 = name_of_planet1_input.get_text() #This stores the user input in a variable
				
				name_of_planet1_input.disable() #This disables the answer box so the user can not type in it anymore

			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#mass_of_p1": #This checks if we pressed enter in this specific answer box
				Button2.update() #Creates our check mark (which is a button in case we want to change the value passed)
				
				global mass_of_p1
				mass_of_p1 = float(mass_of_planet1_input.get_text()) #This stores the user input in a variable
				
				mass_of_planet1_input.disable() #This disables the answer box so the user can not type in it anymore		 
				
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#radius_of_p1": #This checks if we pressed enter in this specific answer box
				Button3.update() #Creates our check mark (which is a button in case we want to change the value passed)
				
				global radius_of_p1
				radius_of_p1 = float(radius_of_planet1_input.get_text()) #This stores the user input in a variable
				
				radius_of_planet1_input.disable() #This disables the answer box so the user can not type in it anymore
				
				global new_planet_design_rect
				#The following will create a bigger planet and background in case the user wants a planet with a different radius:
				new_planet_design_rect = pygame.transform.scale(planet_design_rect, (120 + radius_of_p1//2, 120 + radius_of_p1//2))
				new_planet1 = pygame.transform.scale(planet1, (80 + (radius_of_p1//2), 80 + (radius_of_p1//2)))
				
				#These blits the bigger images in the screen:
				screen.blit(new_planet_design_rect, (1150 - radius_of_p1//4, 240 - radius_of_p1//4))
				screen.blit(new_planet1,(1170 - radius_of_p1//4, 260 - radius_of_p1//4))
				screen.blit(blow_up_message1, (1150 - radius_of_p1//4, 240 - radius_of_p1//4)) #This is a message indicating that the image is a blow up of the original one
			
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#distance_of_p1": #This checks if we pressed enter in this specific answer box
				Button4.update() #Creates our check mark (which is a button in case we want to change the value passed)
				
				global distance_of_p1
				distance_of_p1 = float(distance_of_planet1_input.get_text()) #This stores the user input in a variable
				
				distance_of_planet1_input.disable() #This disables the answer box so the user can not type in it anymore
				
				planets_design_control() #This call the planets_design_control() function to store the distance in the list of distances
			
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#O_P_of_p1": #This checks if we pressed enter in this specific answer box
				Button5.update() #Creates our check mark (which is a button in case we want to change the value passed)

				global O_P_of_p1
				O_P_of_p1 = float(orbital_period_of_planet1_input.get_text()) #This stores the user input in a variable
				
				orbital_period_of_planet1_input.disable() #This disables the answer box so the user can not type in it anymore

			if event.type == pygame.MOUSEBUTTONDOWN:
				#These will check which button was pressed and execute its functions:
				Button1.checkForInput(pygame.mouse.get_pos())
				Button2.checkForInput(pygame.mouse.get_pos())
				Button3.checkForInput(pygame.mouse.get_pos())
				Button4.checkForInput(pygame.mouse.get_pos())
				Button5.checkForInput(pygame.mouse.get_pos())
				Continue_button.checkForInput(pygame.mouse.get_pos())

			Continue_button.update()
			Continue_button.changeColor(pygame.mouse.get_pos())
			MANAGER.process_events(event)
		
		MANAGER.update(clock.tick(60)/1000)
		MANAGER.draw_ui(screen)
		pygame.display.update()

def planet2_design_page():
	MANAGER = pygame_gui.UIManager((WIDTH,HEIGHT))

	#These are all the images/texts/figures we are going to use:
	Continue_button_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button.png')), (125,50))
	Yes_check_mark_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button 1 check.png')), (25,20))
	planet2_text1 = FONT_7.render("It's time to design your planets!", 1, white)
	planet2_text2 = FONT_3.render("What is the name of this planet?", 1, white)
	planet2_text3 = FONT_3.render("What is the mass of this planet (in units of Mass of the Earth)?", 1, white)
	planet2_text4 = FONT_3.render("What is the radius of this planet (in units of Radius of the Earth)?", 1, white)
	planet2_text5 = FONT_3.render("What is the distance from this planet to your star (in Astronomical Units)?", 1, white)
	planet2_text6 = FONT_3.render("What is the orbital period of this planet? (in years)", 1, white)
	message = FONT_1.render("(press enter to confirm or the check mark to type other value)", 1, white)
	planet_design_rect = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space design rectangle.jpg')), (120, 120))

	global planet2
	planet2 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Planet 2.png')), (80, 80))

	#These are all the buttons:
	Continue_button = Button(Continue_button_image, 1201, 701, "Continue")
	Button1 = Button(Yes_check_mark_image, 196, 160, "")
	Button2 = Button(Yes_check_mark_image, 196, 285, "")
	Button3 = Button(Yes_check_mark_image, 196, 410, "")
	Button4 = Button(Yes_check_mark_image, 196, 535, "")
	Button5 = Button(Yes_check_mark_image, 196, 660, "")

	#These make our answer boxes global for later use:
	global name_of_planet2_input
	global mass_of_planet2_input
	global radius_of_planet2_input
	global distance_of_planet2_input
	global orbital_period_of_planet2_input

	#These are our answer boxes with the allowed characters and the base values written:
	name_of_planet2_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 135),(100,50)), manager = MANAGER, 
	object_id = "#name_of_p2")
	name_of_planet2_input.set_text("Planet 2")

	mass_of_planet2_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 260),(100,50)), manager = MANAGER, 
	object_id = "#mass_of_p2")
	mass_of_planet2_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	mass_of_planet2_input.set_text("2")

	radius_of_planet2_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 385),(100,50)), manager = MANAGER, 
	object_id = "#radius_of_p2")
	radius_of_planet2_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	radius_of_planet2_input.set_text("2")

	distance_of_planet2_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 510),(100,50)), manager = MANAGER, 
	object_id = "#distance_of_p2")
	distance_of_planet2_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	distance_of_planet2_input.set_text("2")

	orbital_period_of_planet2_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 635),(100,50)), manager = MANAGER, 
	object_id = "#O_P_of_p2")
	orbital_period_of_planet2_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	orbital_period_of_planet2_input.set_text("2.83")

	#These are all the thins blitted onto the screen:
	screen.blit(background, (0,0))
	screen.blit(planet2_text1, (50, 35))
	screen.blit(planet2_text2, (80, 105))
	screen.blit(planet2_text3, (80, 230))
	screen.blit(planet2_text4, (80, 355))
	screen.blit(planet2_text5, (80, 480))
	screen.blit(planet2_text6, (80, 605))
	screen.blit(message,(80, 122))
	screen.blit(message,(80, 247))
	screen.blit(message,(80, 372))
	screen.blit(message,(80, 497))
	screen.blit(message,(80, 622))
	screen.blit(planet_design_rect, (1150, 240))
	screen.blit(blow_up_message1, (1150, 240))
	screen.blit(base_values_text,(55, 50 + planet2_text1.get_height()//2))
	screen.blit(planet2, (1170, 260))

	run = True
	clock = pygame.time.Clock()

	while run:
		clock.tick(60)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#name_of_p2":
				Button1.update()
				
				global name_of_p2
				name_of_p2 = name_of_planet2_input.get_text()
				
				name_of_planet2_input.disable()

			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#mass_of_p2":
				Button2.update()
				
				global mass_of_p2
				mass_of_p2 = float(mass_of_planet2_input.get_text())
				
				mass_of_planet2_input.disable()		
				
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#radius_of_p2":
				Button3.update()
				
				global radius_of_p2
				radius_of_p2 = float(radius_of_planet2_input.get_text())
				
				radius_of_planet2_input.disable()
				
				global new_planet_design_rect
				
				new_planet2 = pygame.transform.scale(planet2, (80 + (radius_of_p2//2), 80 + (radius_of_p2//2)))
				new_planet_design_rect = pygame.transform.scale(planet_design_rect, (120 + radius_of_p2//2, 120 + radius_of_p2//2))
				
				screen.blit(new_planet_design_rect, (1150 - radius_of_p2//4, 240 - radius_of_p2//4))
				screen.blit(new_planet2,(1170 - radius_of_p2//4, 260 - radius_of_p2//4))
				screen.blit(blow_up_message1, (1150 - radius_of_p2//4, 240 - radius_of_p2//4))
			
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#distance_of_p2":
				Button4.update()
				
				global distance_of_p2
				distance_of_p2 = float(distance_of_planet2_input.get_text())
				
				distance_of_planet2_input.disable()
				
				planets_design_control() #This call the planets_design_control() function to store the distance in the list of distances
			
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#O_P_of_p2":
				Button5.update()
				
				global O_P_of_p2
				O_P_of_p2 = float(orbital_period_of_planet2_input.get_text())
				
				orbital_period_of_planet2_input.disable()

			if event.type == pygame.MOUSEBUTTONDOWN:
				Button1.checkForInput(pygame.mouse.get_pos())
				Button2.checkForInput(pygame.mouse.get_pos())
				Button3.checkForInput(pygame.mouse.get_pos())
				Button4.checkForInput(pygame.mouse.get_pos())
				Button5.checkForInput(pygame.mouse.get_pos())
				Continue_button.checkForInput(pygame.mouse.get_pos())

			Continue_button.update()
			Continue_button.changeColor(pygame.mouse.get_pos())
			MANAGER.process_events(event)
		
		MANAGER.update(clock.tick(60)/1000)
		MANAGER.draw_ui(screen)
		pygame.display.update()

def planet3_design_page():
	MANAGER = pygame_gui.UIManager((WIDTH,HEIGHT))

	#These are all the images/texts/figures we are going to use:
	Continue_button_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button.png')), (125,50))
	Yes_check_mark_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Button 1 check.png')), (25,20))
	planet3_text1 = FONT_7.render("It's time to design your planets!", 1, white)
	planet3_text2 = FONT_3.render("What is the name of this planet?", 1, white)
	planet3_text3 = FONT_3.render("What is the mass of this planet (in units of Mass of the Earth)?", 1, white)
	planet3_text4 = FONT_3.render("What is the radius of this planet (in units of Radius of the Earth)?", 1, white)
	planet3_text5 = FONT_3.render("What is the distance from this planet to your star(in Astronomical Units)?", 1, white)
	planet3_text6 = FONT_3.render("What is the orbital period of this planet? (in years)", 1, white)
	message = FONT_1.render("(press enter to confirm or the check mark to type other value)", 1, white)
	planet_design_rect = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space design rectangle.jpg')), (120, 120))
	
	global planet3
	planet3 = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Planeta 3.png')), (80, 80))
	
	#These are all the buttons:
	Continue_button = Button(Continue_button_image, 1202, 700, "Continue")
	Button1 = Button(Yes_check_mark_image, 196, 161, "")
	Button2 = Button(Yes_check_mark_image, 196, 286, "")
	Button3 = Button(Yes_check_mark_image, 196, 411, "")
	Button4 = Button(Yes_check_mark_image, 196, 536, "")
	Button5 = Button(Yes_check_mark_image, 196, 661, "")

	#These make our answer boxes global for later use:
	global name_of_planet3_input
	global mass_of_planet3_input
	global radius_of_planet3_input
	global distance_of_planet3_input
	global orbital_period_of_planet3_input

	#These are our answer boxes with the allowed characters and the base values written:
	name_of_planet3_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 135),(100,50)), manager = MANAGER, 
	object_id = "#name_of_p3")
	name_of_planet3_input.set_text("Planet 3")

	mass_of_planet3_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 260),(100,50)), manager = MANAGER, 
	object_id = "#mass_of_p3")
	mass_of_planet3_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	mass_of_planet3_input.set_text("3")

	radius_of_planet3_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 385),(100,50)), manager = MANAGER, 
	object_id = "#radius_of_p3")
	radius_of_planet3_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	radius_of_planet3_input.set_text("3")

	distance_of_planet3_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 510),(100,50)), manager = MANAGER, 
	object_id = "#distance_of_p3")
	distance_of_planet3_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	distance_of_planet3_input.set_text("3")

	orbital_period_of_planet3_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 635),(100,50)), manager = MANAGER, 
	object_id = "#O_P_of_p3")
	orbital_period_of_planet3_input.set_allowed_characters(["0","1","2","3","4","5","6","7","8","9","."])
	orbital_period_of_planet3_input.set_text("5.20")

	#These are all the thins blitted onto the screen:
	screen.blit(background, (0,0))
	screen.blit(planet3_text1, (50, 35))
	screen.blit(planet3_text2, (80, 105))
	screen.blit(planet3_text3, (80, 230))
	screen.blit(planet3_text4, (80, 355))
	screen.blit(planet3_text5, (80, 480))
	screen.blit(planet3_text6, (80, 605))
	screen.blit(message,(80, 122))
	screen.blit(message,(80, 247))
	screen.blit(message,(80, 372))
	screen.blit(message,(80, 497))
	screen.blit(message,(80, 622))
	screen.blit(planet_design_rect, (1150, 240))
	screen.blit(blow_up_message1, (1150, 240))
	screen.blit(base_values_text,(55, 50 + planet3_text1.get_height()//2))
	screen.blit(planet3, (1170, 260))

	run = True
	clock = pygame.time.Clock()

	while run:
		clock.tick(60)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#name_of_p3":
				Button1.update()
				
				global name_of_p3
				name_of_p3 = name_of_planet3_input.get_text()
				
				name_of_planet3_input.disable()

			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#mass_of_p3":
				Button2.update()
				
				global mass_of_p3
				mass_of_p3 = float(mass_of_planet3_input.get_text())
				
				mass_of_planet3_input.disable()		
				
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#radius_of_p3":
				Button3.update()
				
				global radius_of_p3
				radius_of_p3 = float(radius_of_planet3_input.get_text())
				
				radius_of_planet3_input.disable()
				
				global new_planet_design_rect
				
				new_planet3 = pygame.transform.scale(planet3, (80 + (radius_of_p3//2), 80 + (radius_of_p3//2)))
				new_planet_design_rect = pygame.transform.scale(planet_design_rect, (120 + radius_of_p3//2, 120 + radius_of_p3//2))
				
				screen.blit(new_planet_design_rect, (1150 - radius_of_p3//4, 240 - radius_of_p3//4))
				screen.blit(new_planet3,(1170 - radius_of_p3//4, 260 - radius_of_p3//4))
				screen.blit(blow_up_message1, (1150 - radius_of_p3//4, 240 - radius_of_p3//4))
			
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#distance_of_p3":
				Button4.update()
				
				global distance_of_p3
				distance_of_p3 = float(distance_of_planet3_input.get_text())
				
				distance_of_planet3_input.disable()
				
				planets_design_control()
			
			if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#O_P_of_p3":
				Button5.update()
				
				global O_P_of_p3
				O_P_of_p3 = float(orbital_period_of_planet3_input.get_text())
				
				orbital_period_of_planet3_input.disable()

			if event.type == pygame.MOUSEBUTTONDOWN:
				Button1.checkForInput(pygame.mouse.get_pos())
				Button2.checkForInput(pygame.mouse.get_pos())
				Button3.checkForInput(pygame.mouse.get_pos())
				Button4.checkForInput(pygame.mouse.get_pos())
				Button5.checkForInput(pygame.mouse.get_pos())
				Continue_button.checkForInput(pygame.mouse.get_pos())

			Continue_button.update()
			Continue_button.changeColor(pygame.mouse.get_pos())
			MANAGER.process_events(event)
		
		MANAGER.update(clock.tick(60)/1000)
		MANAGER.draw_ui(screen)
		pygame.display.update()

class Button(): #This class creates our buttons and define the functions of each
	
	def __init__(self, image, x_pos, y_pos, text_input): #This defines the properties of the buttons
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = FONT_2.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self): #This will draw the button on the screen
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)
	
	def checkForInput(self, position): #This will check if you pressed the button

		Not_check_mark_image = pygame.transform.scale(pygame.image.load(
			os.path.join('Assets', 'Button_off.png')), (25, 20)) #This loads the image of the not check mark

		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): 
		#This function determines what to do based on the x and y positions of the button pressed
		#Each button appears to be in the same place on different pages, but its moved 1 pixel sideways or downwards for identification

			if self.x_pos == 245 and self.y_pos == 255: #This identifies which button was pressed
				name_of_star_input.rebuild() #This rebuilds the answer box
				name_of_star_input.enable() #This enables the user to type in that box again
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2)) #This blits a not check mark in the screen

			if self.x_pos == 245 and self.y_pos == 405: #This identifies which button was pressed
				mass_of_star_input.rebuild() #This rebuilds the answer box
				mass_of_star_input.enable() #This enables the user to type in that box again
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2)) #This blits a not check mark in the screen
				
			if self.x_pos == 245 and self.y_pos == 555:
				#The three following blits return the image of the star to its original size (the new_star_design_rect remains the same size if it was once increased )
				screen.blit(new_star_design_rect, (1098 - radius_of_star//2, 240 - radius_of_star//2))
				screen.blit(star, (1125, 270))
				screen.blit(blow_up_message, (1098 - radius_of_star//2 , 240 - radius_of_star//2))
				
				radius_of_star_input.rebuild()
				radius_of_star_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 1199 and self.y_pos == 700: #This is the continue button and calls the next page if pressed
				planet1_design_page()

			if self.x_pos == 195 and self.y_pos == 160:
				name_of_planet1_input.rebuild()
				name_of_planet1_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 195 and self.y_pos == 285:
				mass_of_planet1_input.rebuild()
				mass_of_planet1_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 195 and self.y_pos == 410:
				#The three following blits return the image of the planet to its original size (the new_planet_design_rect remains the same size if it was once increased )
				screen.blit(new_planet_design_rect, (1150 - radius_of_p1//4, 240 - radius_of_p1//4))
				screen.blit(planet1, (1170, 260))
				screen.blit(blow_up_message1, (1150 - radius_of_p1//4, 240 - radius_of_p1//4))
				
				radius_of_planet1_input.rebuild()
				radius_of_planet1_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 195 and self.y_pos == 535:
				distance_of_planet1_input.rebuild()
				distance_of_planet1_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 195 and self.y_pos == 660:
				orbital_period_of_planet1_input.rebuild()
				orbital_period_of_planet1_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 1200 and self.y_pos == 701: #This is the continue button
				#(2*3.14*distance_of_p1*AU*math.sqrt(distance_of_p1*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p1*MASS_OF_EARTH)))/31536000) is the minimum orbital period for a stable orbit
				#The following if statement prints an error message if the minimum orbital period is not matched or surpassed
				if O_P_of_p1 < round(((2*3.14*distance_of_p1*AU*math.sqrt(distance_of_p1*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p1*MASS_OF_EARTH)))/31536000), 2):
					
					error_message2 = FONT_9.render(f"NOT STABLE ORBIT - MIN = {round(((2*3.14*distance_of_p1*AU*math.sqrt(distance_of_p1*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p1*MASS_OF_EARTH)))/31536000), 2)} yrs", 1 , red)
					
					screen.blit(error_message2, (225, 660 - error_message2.get_height()//2))
					screen.blit(Not_check_mark_image, (195 - Not_check_mark_image.get_width()//2, 660 - Not_check_mark_image.get_height()//2))
				
				#If you match or surpass the minimum orbital period for a stable orbit, the following if statement is executed:
				elif O_P_of_p1 >= round(((2*3.14*distance_of_p1*AU*math.sqrt(distance_of_p1*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p1*MASS_OF_EARTH)))/31536000), 2):
					planets_design_control() #This calls the planets_design_control() function to see if the user wants more than one planet
					if "planet2" in list_of_planets: #If planet2 is in the list, then the user wants at least to planets and moves to the next design page
						planet2_design_page()
					else: #If planet2 is not in the list, the user only wants 1 planet and can move directly to the final page
						final_simulation_page()
			
			if self.x_pos == 196 and self.y_pos == 160:
				name_of_planet2_input.rebuild()
				name_of_planet2_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 196 and self.y_pos == 285:
				mass_of_planet2_input.rebuild()
				mass_of_planet2_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 196 and self.y_pos == 410:
				screen.blit(new_planet_design_rect, (1150 - radius_of_p2//4, 240 - radius_of_p2//4))
				screen.blit(planet2, (1170, 260))
				screen.blit(blow_up_message1, (1150 - radius_of_p2//4, 240 - radius_of_p2//4))
				
				radius_of_planet2_input.rebuild()
				radius_of_planet2_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 196 and self.y_pos == 535:
				distance_of_planet2_input.rebuild()
				distance_of_planet2_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 196 and self.y_pos == 660:
				orbital_period_of_planet2_input.rebuild()
				orbital_period_of_planet2_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 1201 and self.y_pos == 701:

				if distance_of_p2 in list_of_distances: #This will see if the user wants to have a second planet, if he wants, distance_of_p2 will be on the list
					if list_of_distances[0] == list_of_distances[1]: #This checks if the distances of planet 1 and 2 are equal
						#If they are, the following will print an error message and the user will not move on:
						error_message5 = FONT_9.render("2 PLANETS CAN NOT HAVE THE SAME DISTANCE", 1 , red)
						
						screen.blit(error_message5, (226, 535 - error_message5.get_height()//2))
						screen.blit(Not_check_mark_image, (196 - Not_check_mark_image.get_width()//2, 535 - Not_check_mark_image.get_height()//2))

				if O_P_of_p2 < round(((2*3.14*distance_of_p2*AU*math.sqrt(distance_of_p2*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p2*MASS_OF_EARTH)))/31536000), 2):
					error_message3 = FONT_9.render(f"NOT STABLE ORBIT - MIN = {round(((2*3.14*distance_of_p2*AU*math.sqrt(distance_of_p2*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p2*MASS_OF_EARTH)))/31536000), 2)} yrs", 1 , red)
					
					screen.blit(error_message3, (225, 660 - error_message3.get_height()//2))
					screen.blit(Not_check_mark_image, (196 - Not_check_mark_image.get_width()//2, 660 - Not_check_mark_image.get_height()//2))
				
				if distance_of_p2 in list_of_distances:
					#The following if statement will allow you to move on only if the minimum orbital period for stable orbit and distances conditions are met
					if O_P_of_p2 >= round(((2*3.14*distance_of_p2*AU*math.sqrt(distance_of_p2*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p2*MASS_OF_EARTH)))/31536000), 2) and list_of_distances[0] != list_of_distances[1]:
						planets_design_control()
						if "planet3" in list_of_planets:
							planet3_design_page()
						else:
							final_simulation_page()
			
			if self.x_pos == 196 and self.y_pos == 161:
				name_of_planet3_input.rebuild()
				name_of_planet3_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 196 and self.y_pos == 286:
				mass_of_planet3_input.rebuild()
				mass_of_planet3_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 196 and self.y_pos == 411:
				screen.blit(new_planet_design_rect, (1150 - radius_of_p3//4, 240 - radius_of_p3//4))
				screen.blit(planet3, (1170, 260))
				screen.blit(blow_up_message1, (1150 - radius_of_p3//4, 240 - radius_of_p3//4))
				
				radius_of_planet3_input.rebuild()
				radius_of_planet3_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 196 and self.y_pos == 536:
				distance_of_planet3_input.rebuild()
				distance_of_planet3_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 196 and self.y_pos == 661:
				orbital_period_of_planet3_input.rebuild()
				orbital_period_of_planet3_input.enable()
				
				screen.blit(Not_check_mark_image, (self.x_pos - Not_check_mark_image.get_width()//2, self.y_pos - Not_check_mark_image.get_height()//2))
			
			if self.x_pos == 1202 and self.y_pos == 700:

				if distance_of_p3 in list_of_distances: #This will see if the user wants to have a third planet, if he wants, distance_of_p3 will be on the list
					if list_of_distances[2] == list_of_distances[1] or list_of_distances[2] == list_of_distances[0]: #This will check if distance of planet 3 is not equal to distance of planet 1 or planet2
						error_message6 = FONT_9.render("2 PLANETS CAN NOT HAVE THE SAME DISTANCE", 1 , red)
						
						screen.blit(error_message6, (226, 536 - error_message6.get_height()//2))
						screen.blit(Not_check_mark_image, (196 - Not_check_mark_image.get_width()//2, 536 - Not_check_mark_image.get_height()//2))

				if O_P_of_p3 < round(((2*3.14*distance_of_p3*AU*math.sqrt(distance_of_p3*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + + mass_of_p3*MASS_OF_EARTH)))/31536000), 2):
					error_message4 = FONT_9.render(f"NOT STABLE ORBIT - MIN = {round(((2*3.14*distance_of_p3*AU*math.sqrt(distance_of_p3*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + mass_of_p3*MASS_OF_EARTH)))/31536000), 2)} yrs", 1 , red)
					screen.blit(error_message4, (225, 660 - error_message4.get_height()//2))
					screen.blit(Not_check_mark_image, (196 - Not_check_mark_image.get_width()//2, 661 - Not_check_mark_image.get_height()//2))
					
				if distance_of_p3 in list_of_distances:
					#The following if statement will allow you to move on only if the minimum orbital period for stable orbit and distances conditions are met
					if O_P_of_p3 >= round(((2*3.14*distance_of_p3*AU*math.sqrt(distance_of_p3*AU)/math.sqrt(G*(mass_of_star*MASS_OF_SUN + + mass_of_p3*MASS_OF_EARTH)))/31536000), 2) and list_of_distances[2] != list_of_distances[1] and list_of_distances[2] != list_of_distances[0]:
						final_simulation_page()
				
	def changeColor(self, position): #This makes the text in the button change color when the mouse pass over it. 
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = FONT_2.render(self.text_input, True, purple)
		else:
			self.text = FONT_2.render(self.text_input, True, "white")

class Planet: #This class creates our planets and their orbits
	
	#These are the constants we need:
	G = 6.67428e-11
	MASS_OF_SUN = 1.98892 * 10**30
	MASS_OF_EARTH = 5.9742 * 10**24
	AU = 149.6e6 * 1000
	TIMESTEP = 3600*24 # 1 day
	
	def __init__(self, x, y, radius, orbital_period, mass, image, name): #These define the properties of our planets
		self.x = x
		self.y = y
		self.radius = radius
		self.orbital_period = orbital_period
		self.mass = mass
		self.image = image
		self.name = name

		self.orbit = []
		self.star = False
		self.distance_to_star = 0

		self.x_vel = 0
		self.y_vel = 0	

		self.SCALE = (100 + (mass_of_star - 1)*50) / AU #This changes the scale in case the mass of the star is big

		global scale_for_text
		scale_for_text = self.SCALE #This is to print the scale on the final screen 

	def draw(self, screen): #This will draw the orbits of the planets
		x = self.x * self.SCALE + WIDTH / 2 
		y = self.y * self.SCALE + HEIGHT / 2 

		if len(self.orbit) > 2:
			updated_points = []
			for point in self.orbit:
				x, y = point
				x = x * self.SCALE + WIDTH / 2 
				y = y * self.SCALE + HEIGHT / 2 
				updated_points.append((x, y))
			
			pygame.draw.lines(screen, white, False, updated_points, 2) #This will draw a white circle as the path of the orbit

		list_of_radii = [radius_of_p1, radius_of_p2, radius_of_p3]
		list_of_radii.sort() #This will create a list in crescent order of radii
		#It will be used to control the sizes of each planet and make sure the bigger ones are actually drawn bigger in the final screen

		#The following if statements will check what is the position of the respective radius in the list 
		#After that, it will blit the planets with an appropriate size				
		if self.radius == list_of_radii[0]:
			new_image = pygame.transform.scale(self.image,(20, 20))
			screen.blit(new_image, (x - new_image.get_width()//2, y - new_image.get_height()//2))
				
		if self.radius == list_of_radii[1]:
			new_image = pygame.transform.scale(self.image,(30, 30))
			screen.blit(new_image, (x - new_image.get_width()//2, y - new_image.get_height()//2))
				
		if self.radius == list_of_radii[2]:
			new_image = pygame.transform.scale(self.image,(40, 40))
			screen.blit(new_image, (x - new_image.get_width()//2, y - new_image.get_height()//2))
				
		if not self.star: #This blits the name of the planet on top of the planet
			name_text = FONT_1.render(f"{self.name}", 1, white)
			screen.blit(name_text, (x - name_text.get_width()/2, y - name_text.get_height()/2))
		
		#This blits the image of the star:
		new_star = pygame.transform.scale(star,(80, 80))
		screen.blit(new_star, (WIDTH//2 - new_star.get_width()//2, HEIGHT/2 - new_star.get_height()//2))
			
	
	def attraction(self, other): #This calculates the force of attraction being exerted by all of the other objects in a given planet
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x
		distance_y = other_y - self.y
		distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

		if other.star:
			self.distance_to_star = distance
		
		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distance_y, distance_x)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force
		return force_x, force_y
	
	def update_position(self, list): #This calculates the displacement of a planet as a result of the forces being applied to it
		total_fx = total_fy = 0

		for planet in LIST_OF_PLANETS:
			if self == planet:
				continue

			fx, fy = self.attraction(planet)
			total_fx += fx
			total_fy += fy

		self.x_vel += total_fx / self.mass * self.TIMESTEP
		self.y_vel += total_fy / self.mass * self.TIMESTEP

		self.x += self.x_vel * self.TIMESTEP
		self.y += self.y_vel * self.TIMESTEP
		self.orbit.append((self.x, self.y))

def final_simulation_page(): #This is the final page, which hosts the simulation

	planets_design_control() # This function is called to see which planets are going to be in the final simulation

	global Star
	Star = Planet(0, 0, radius_of_star, 0, mass_of_star*MASS_OF_SUN, star, name_of_star) #Makes the star
	Star.star = True

	global planet1_S
	planet1_S = Planet(-distance_of_p1*AU, 0, radius_of_p1, O_P_of_p1, mass_of_p1*MASS_OF_EARTH, planet1, name_of_p1) #Makes planet 1
	planet1_S.y_vel = (2*3.14*distance_of_p1*AU)/(31536000*O_P_of_p1) #calculates planet 1 y velocity

	if "planet2" in list_of_planets:
		global planet2_S
		planet2_S = Planet(-distance_of_p2*AU, 0, radius_of_p2, O_P_of_p2, mass_of_p2*MASS_OF_EARTH, planet2, name_of_p2) # Makes planet 2 if the user wants
		planet2_S.y_vel = (2*3.14*distance_of_p2*AU) / (31536000*O_P_of_p2) #calculates planet 2 y velocity

	if "planet3" in list_of_planets:
		global planet3_S
		planet3_S = Planet(-distance_of_p3*AU, 0, radius_of_p3, O_P_of_p3, mass_of_p3*MASS_OF_EARTH, planet3, name_of_p3) # Makes planet 3 if the user wants
		planet3_S.y_vel = (2*3.14*distance_of_p3*AU)/(31536000*O_P_of_p3) #calculates planet 3 y velocity
	
	global LIST_OF_PLANETS
	LIST_OF_PLANETS = [Star, planet1_S]
	#The following if statements will add the planets created to the final list if the user wants it 
	if "planet2" in list_of_planets:
		LIST_OF_PLANETS.append(planet2_S)
	
	if "planet3" in list_of_planets:
		LIST_OF_PLANETS.append(planet3_S)
	

	screen.blit(background, (0,0))

	run = True
	clock = pygame.time.Clock()

	while run:
		screen.blit(background, (0,0))
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
		
		for planet in LIST_OF_PLANETS: #This calls the update_position method with the final list as a parameter, which creates the simulation
			planet.update_position(LIST_OF_PLANETS)
			planet.draw(screen)
		
		#This blits the name of the star on top of the star:
		name_text_star = FONT_1.render(name_of_star, 1, black)
		screen.blit(name_text_star, (WIDTH/2 - name_text_star.get_width()//2, HEIGHT/2 - name_text_star.get_height()//2))

		#These blit the scale and a note about scales:
		scale_text = FONT_8.render(f"Scale: 1AU - {100*(scale_for_text/(250/AU))} pixels", 1, red)
		screen.blit(scale_text, (100, 50))

		scale_text2 = FONT_8.render("Objects are not drawn to any scale", 1, red)
		screen.blit(scale_text2, (100, 65))

		pygame.display.update()

welcome() #This will initialize everything

#Suggestions for code improvement:
    # Place a limit on planet radii (it can not be bigger than the star's radius)
	# Make possible to go back to past pages
	# Make possible to the user to load an image for the objects
	# Make a page with all the given properties of the objects and some derived (e.g. radius, mass, density, velocity... )
	# Make the scale change as a function of a given planet's distance, so you can represent more distant planets
