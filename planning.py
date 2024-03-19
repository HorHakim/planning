import pandas
from infrastructure import Infrastructure
from building import Building

class Planning:
	def __init__(self, csv_path):
		self.network_df = pandas.read_csv(csv_path).drop_duplicates()




	def prepare_data(self):
		self.network_df = self.network_df[self.network_df["infra_type"] != "infra_intacte"] # on ne garde que les infra à remplacer


		dict_infrastructures = {}

		for infra_id, infra_subdf in self.network_df.groupby(by="infra_id"):
			length = infra_subdf["longueur"].iloc[0]
			infra_type = infra_subdf["infra_type"].iloc[0]
			nb_houses = infra_subdf["nb_maisons"].sum()

			dict_infrastructures[infra_id] = Infrastructure(infra_id, length, infra_type, nb_houses)
			

		list_buildings = []

		for id_building, building_subdf in self.network_df.groupby(by="id_batiment"):

			list_infra = [dict_infrastructures[infra_id] for infra_id in building_subdf["infra_id"].values]

			list_buildings.append(Building(id_building, list_infra))

		return list_buildings



	def run_plannification(self, list_buildings):
		sorted_infrastructure = []
		sorted_buildings = []

		while list_buildings:
			easiest_building = min(list_buildings)
			
			for infra in easiest_building.list_infra:
				infra.repair_infra()
				if infra not in sorted_infrastructure:
					sorted_infrastructure.append(infra)

			sorted_buildings.append(easiest_building)
			list_buildings.remove(easiest_building)


		return sorted_infrastructure, sorted_buildings



if __name__ == "__main__":
	plannification_object = Planning("../data/reseau_en_arbre.csv")

	list_buildings = plannification_object.prepare_data()
	sorted_infrastructure, sorted_buildings = plannification_object.run_plannification(list_buildings)


	for index_building, building in enumerate(sorted_buildings):
		print(index_building, building)