def convert_mongo_results_to_dict(results):
    results_list = []
    if results:
        for result in results:
            results_list.append(result)
        return results_list
    return None
