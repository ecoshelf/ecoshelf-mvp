def convert_mongo_results_to_dict(results):

    results_list = []
    if results:
        for result in results:
            result_dict = {}
            id = result['_id']
            result_dict.update({'id': str(id)})

            for key, value in result.items():
                if key != '_id':
                    result_dict.update({key: value})
            results_list.append(result_dict)
        return results_list
    return None
