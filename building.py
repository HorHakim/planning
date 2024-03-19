class Building:
	def __init__(self, id_building, list_infra):
		self.id_building = id_building
		self.list_infra = list_infra

	def get_building_difficulty(self):
		return sum(self.list_infra)

	def __lt__(self, other_building):
		return self.get_building_difficulty() < other_building.get_building_difficulty()

	def __repr__(self):
		return self.id_building