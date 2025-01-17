from bson import json_util
import json

def convert_mongo_results_to_dict(results):
    results_list = []
    if results:
        for result in results:
            results_list.append(json.loads(json_util.dumps(result)))
        return results_list
    return None
