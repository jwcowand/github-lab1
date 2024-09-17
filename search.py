import json

def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    #data = json.load(json_data)
    
    results = [lines for lines in json_data if any(search_string in str(value)for value in lines.values() or lines.objects())]
    return results