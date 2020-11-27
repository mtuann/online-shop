import pandas as pd
import json
import os


def convert(pathFile="./data_clothes.csv"):
	results = []
	df = pd.read_csv(pathFile)

	df = df.to_dict('records')
	for idx, row in enumerate(df):
		imageUrls = row["imageUrls"].split("\n")

		ulr_local = []

		for idy, img in enumerate(imageUrls):
			# extension = img.split(".")[-1]
			extension = "jpg"
			# print(f'{row["id"]:02}')
			idI = row["id"]
			# print(idI)

			path_file = f"./../public/Images/{idI:02}_{idy + 1:02}.{extension}"
			ulr_local.append(f"/Images/{idI:02}_{idy + 1:02}.{extension}")
			
			if os.path.isfile(path_file):
				continue

			cmd = 'wget "{}" -O "{}"'.format(img, path_file)

			# print(cmd)
			os.system(cmd)
		row["imageUrls"] = ulr_local

			# print(path_file)
			# 

		# break			

	dataWrite = "const sampleProducts =  {}; \n".format(json.dumps(df, indent=2)) + "export {sampleProducts}"

	with open("./data_clothes.js", "w") as fw:
		fw.write(dataWrite)

	# return results


convert()

