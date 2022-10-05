def list_oper(a,b,oper='add'):
    c=[]
    if oper=='add':
        for i in range(len(a)):
            c.append(a[i]+b[i])
    elif oper=='sub':
        for i in range(len(a)):
            c.append(a[i]-b[i])
    elif oper=='mult':
        for i in range(len(a)):
            c.append(a[i]*b[i])
    elif oper=='div':
        for i in range(len(a)):
            c.append(a[i]/b[i])
    return c

def get_elem_index(a,elem=None):
    if elem=='min':
        return min(a),a.index(min(a))
    elif elem=='max':
        return max(a),a.index(max(a))
    else:
        return elem,a.index(elem)

def main():
    n,k = 0,0
    while n<1 or k<1:
        initial_data=input().split(' ')
        n,k,m=int(initial_data[0]),int(initial_data[1]),int(initial_data[2])
    actual_existences,required_existences,bra_count=[],[],[]
    for i in range(n):
        read_ex = list(map(lambda x: int(x), input().split(' ')))
        actual_existences.append(read_ex)
        required_existences.append([0 for i in range(k)])
        bra_count.append(0)
#     for i in range(m):
#         read_info=input().split(' ')
#         bra,med_type,n_dosis,s,d=int(read_info[0]),int(read_info[1]), int(read_info[2]), int(read_info[3]), int(read_info[4])
#         if 0<bra<=n and 0<med_type<=k and n_dosis>= 0:
#             if s<90 and d<70:
#                 required_existences
#                 [bra-1][med_type-1]+=n_dosis
#             elif 140<=s<150 and 95<=d<100:
#                 required_existences
#                 [bra-1][med_type-1]+=n_dosis
#             elif 150<=s<170 and 100<=d<110:
#                 required_existences
#                 [bra-1][med_type-1]+=n_dosis
#             elif 170<=s<190 and 110<=d<120:
#                 required_existences
#                 [bra-1][med_type-1]+=n_dosis
#             elif s>=190 and d>=120:
#                 required_existences
#                 [bra-1][med_type-1]+=n_dosis
#             elif s>=150 and d<100:
#                 required_existences
#                 [bra-1][med_type-1]+= n_dosis
#             bra_count[bra-1]+= 1
#     final_ex=matrix_oper(actual_existences,required_existences
#     ,oper='sub')
#     min_max_avg=get_min_max_avg(required_existences
#     )
# if __name__ == "__main__":
#     main()

def main():
    while n < 1:
        initial_data = input().slpit(' ')
        n, m = (int(initial_data[0]), int(initial_data[1]))
    actual_existences, request_existences = [], []
    
    for i in range(n):
        read_existences=0
        while read_existences < 1:
            read_existences = int(input())
            actual_existences.append(read_existences)