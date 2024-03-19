import pandas

import infrastructure, building


class Planning:
	def __init__(self, csv_path):
		self.network_df = pandas.read_csv(csv_path)


	def prepare_data(self):
		dict_infrastructures = {}
		list_buildings = []

		#algo

		return dict_infrastructures, list_buildings



	def run_plannification(self, dict_infrastructures, list_buildings):
		sorted_infrastructure = []
		sorted_buildings = []
		
		# algo
		return sorted_infrastructure, sorted_buildings



if __name__ == "__main__":
	plannification_object = Planning("../data/reseau_en_arbre.csv")*

	dict_infrastructures, list_buildings = plannification_object.prepare_data()
	plannification_object.run_plannification(sorted_infrastructure, sorted_buildings)