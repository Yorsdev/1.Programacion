def list_oper(a,b,oper='add'): #funcion para realizar operaciones
    lista1=[]
    if oper=='add':
        for i in range(len(a)):
            lista1.append(a[i]+b[i])
    elif oper=='sub':
        for i in range(len(a)):
            lista1.append(a[i]-b[i])
    elif oper=='mult':
        for i in range(len(a)):
            lista1.append(a[i]*b[i])
    elif oper=='div':
        for i in range(len(a)):
            lista1.append(a[i]/b[i])
    return lista1

def matrix_oper(a,b,oper='add'): #funcion para iterar entre las dos listas a modo de matriz.
    lista2=[]
    for i in range(len(a)):
        if oper=='add':
            lista2.append(list_oper(a[i],b[i],oper=oper))
        elif oper=='sub':
            lista2.append(list_oper(a[i],b[i],oper=oper))
        elif oper=='mult':
            lista2.append(list_oper(a[i],b[i],oper=oper))
        elif oper=='div':
            lista2.append(list_oper(a[i],b[i],oper=oper))
    return lista2

def get_elem_index(a,elem=None): #funcion para obtener el indice de las listas
    if elem=='min':
        return min(a),a.index(min(a))
    elif elem=='max':
        return max(a),a.index(max(a))
    else:
        return elem,a.index(elem)

def get_average(ext_list): #funcion para promedio
    if len(ext_list)>0:
        return sum(ext_list)/len(ext_list)
    return 0

def get_min_max_avg(existences): #funcion para obtener mínimo y máximo del total de existencias del medicamento
    resultados=[]
    for existencias in existences:
        if len(existencias)>0:
            resultados.append([min(existencias),get_average(existencias),max(existencias)])
        else:
            resultados.append([0 for i in range(3)])
    return resultados

def get_avg_per_patient(meds,n_pat):
    if n_pat>0:
        return sum(meds)/n_pat
    return 0

def main():
    n,k = 0,0
    while n<1 or k<1:
        ini_data=input().split(' ')
        n,k,m=int(ini_data[0]),int(ini_data[1]),int(ini_data[2])
    actual_ex,req_ex,bra_count=[],[],[]
    for i in range(n):
        read_ex = list(map(lambda x: int(x), input().split(' ')))
        actual_ex.append(read_ex)
        req_ex.append([0 for i in range(k)])
        bra_count.append(0)
    for i in range(m):
        read_info=input().split(' ')
        bra,med_type,n_dosis,s,d=int(read_info[0]),int(read_info[1]), int(read_info[2]), int(read_info[3]), int(read_info[4])
        if 0<bra<=n and 0<med_type<=k and n_dosis>= 0:
            if s<90 and d<70:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif 140<=s<150 and 95<=d<100:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif 150<=s<170 and 100<=d<110:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif 170<=s<190 and 110<=d<120:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif s>=190 and d>=120:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif s>=150 and d<100:
                req_ex[bra-1][med_type-1]+= n_dosis
            bra_count[bra-1]+= 1

    final_ex=matrix_oper(actual_ex,req_ex,oper='sub')    
    min_max_avg=get_min_max_avg(req_ex)

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

if __name__ == "__main__":
    main()