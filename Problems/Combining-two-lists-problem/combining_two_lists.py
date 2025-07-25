def combining_lists(list1, list2):
    combined = list1.copy()  

    for item2 in list2:
        start2, end2 = item2["positions"]
        values2 = item2["values"]

        merged = False

        for item1 in combined:
            start1, end1 = item1["positions"]
            
            overlap_start = max(start1, start2)
            overlap_end = min(end1, end2)
            overlap_length = overlap_end - overlap_start
            
            item2_length = end2 - start2
            
            if overlap_length > 0 and overlap_length >= (item2_length / 2):
                item1["values"].extend(values2)  
                merged = True
                break  

        if not merged:
            combined.append(item2)

    combined.sort(key=lambda x: x["positions"][0])
    return combined


list1 = [
    {"positions": [2, 10], "values": [2,5,7]},
    {"positions": [15, 20], "values": [4,5]}
]

list2 = [
    {"positions": [5, 8], "values": [9,4,2]},
    {"positions": [16, 19], "values": [3,4]}
]

print(combining_lists(list1, list2))