    min_, index_min = get_elem_index(med1, elem='min')
    max_, index_max = get_elem_index(med1, elem='max')
    med1 = [ex[0] for ex in req_ex]

    for i in range(n):
        print(i+1)        
        print(index_min +1, min_)
        print(index_max +1, max_)
        print(index_min + 1)
        print(index_max + 1)
        print('{:.2f} {:.2f} {:.2f}'.format(min_max_avg[i][0],min_max_avg[i][1], min_max_avg[i][2]))
        print('{:.2f}'.format(get_avg_per_patient(req_ex[i], bra_count[i])))
        print(final_ex[i])
        print(min_max_avg)


        print('{:.2f} {:.2f} {:.2f}'.format(min_max_avg[i][0], min_max_avg[i][1], min_max_avg[i][2]))
        print('{:.2f}'.format(get_avg_per_patient(request_ex[i], branch_count[i])))

    med1 = [ex[0] for ex in req_ex]    
    min_, index_min = get_elem_index(med1, elem='min')
    max_, index_max = get_elem_index(med1, elem='max')
    print(index_min + 1, min_)
    print(index_max + 1, max_)