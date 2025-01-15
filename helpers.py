def convert_mongo_results_to_dict(results):
    results_dict = {}
    if results:
        for r in results:
            results_dict.update(r)
        return results_dict
    return None
