class GameStats():
	"""Track stats for Alien Invasion"""

	def __init__(self, ai_settings):
		"""Initailize stats"""
		self.ai_settings = ai_settings
		self.reset_stats()
		#Start game in an active state.
		self.game_active = True

	def reset_stats(self):
		"""initialize stats that can change during the game"""
		self.ships_left = self.ai_settings.ship_limit