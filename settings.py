class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		
		#Bullet settings
		self.bullets_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (190, 20, 20)


		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5