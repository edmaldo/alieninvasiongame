class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		
		#Bullet settings
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = (220, 25, 25)
		self.bullets_allowed = 2

		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_limit = 2

		#Alien settings
		self.fleet_drop_speed = 7

		self.speedup_scale = 1.1

		self.score_scale = 1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 1.7
		self.alien_speed = 1.0

		self.fleet_direction = 1

		self.alien_points = 100

	def increase_speed(self):
		"""increase speed settings."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

