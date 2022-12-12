from flatten import flatten_json

# the purpose of this program is to take as an input a folder with
# many jsons, where each json contains a "results" key, which is a list,
# and then it will flatten each json in the folder and output a new json
# the folder for the output is ./out/

input_folder = "./input_folder/"
output_folder = "./out/"

import os
import json

# get all the files in the input folder
files = os.listdir(input_folder)

output_list = []

# loop through each file
for file in files:
    # open the file
    
    with open(input_folder + file, "r") as f:
        # load the json
        data = json.load(f)
        # get the results list
        results = data["results"]
        # loop through each result
        for result in results:
            # flatten the result
            flattened = flatten_json(result)
            flattened["file_name"] = file
            # write the flattened result to a new file
            output_list.append(flattened)
    
# write the output list to a new file
with open(output_folder + "all.json", "w") as f:
    json.dump(output_list, f)

            