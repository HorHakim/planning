class Infrastructure:
	def __init__(self, infra_id, length, infra_type, nb_houses):
		self.infra_id = infra_id
		self.length = length
		self.infra_type = infra_type
		self.nb_houses = nb_houses

	def repair_infra(self):
		self.infra_type = "infra_intacte"

	def get_infra_difficulty(self):
		return 0 if self.infra_type == "infra_intacte" else self.length / self.nb_houses


	def __radd__(self, other_object):
		return self.get_infra_difficulty() + other_object