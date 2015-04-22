class Character:
	def _init_(self):
		# Characteristics
		self.name = None
		self.species = None
		self.career = None
		self.specializations = []
		self.gender = None
		self.Age = None
		self.Height = None
		self.Build = None
		self.Hair = None
		self.Eyes = None
		self.notable_features = []
		self.player = None

		# Ability Scores
		self.brawn = 0
		self.agility = 0
		self.intellect = 0
		self.cunning = 0
		self.willpower = 0
		self.presence = 0

		# Combat Stats
		self.wound_threshold = 0
		self.curr_wounds = 0
		self.strain_threshold = 0
		self.curr_strains = 0
		self.melee_defense = 0
		self.ranged_defense = 0
		self.weapons = []
		self.total_experience = 0
		self.available_experience = 0

		# Skills and Talents
		self.general_skills = []
		self.combat_skills = []
		self.knowledge_skills = []
		self.custom_skills = []
		self.talents_specials = {}

		# Other Info
		self.motivations = []
		self.obligations = []
		self.equipment_log = []
		self.credits = 0
		self.max_encumberance = 0
		self.curr_encumberance = 0
		self.background = None
		self.notes = None
	

	def saveSpecies(self,in_species):
		self.species = str(in_species) # This might not work because I am sending the result of the key -> value
		self.brawn = in_species["brawn"]
		self.agility = in_species["agility"]
		self.intellect = in_species["intellect"]
		self.cunning = in_species["cunning"]
		self.willpower = in_species["willpower"]
		self.presence = in_species["presence"]
		self.available_experience = in_species["start_xp"]
		self.wound_threshold = in_species["wound_threshold"]
		self.strain_threshold = in_species["strain_threshold"]
		self.talents_specials = in_species["special_abilities"]



