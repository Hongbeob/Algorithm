result=[]
def cumulative_sum_recursive(lst,i=0):

    if i == len(lst):
        return result
    
    current_sum = sum(lst[:i+1])
    result.append(current_sum)

    return cumulative_sum_recursive(lst, i + 1)


N=int(input())
Pi=list(map(int,input().split()))
Pi.sort()
cumulative_sum_recursive(Pi)
print_result=sum(result)
print(print_result)