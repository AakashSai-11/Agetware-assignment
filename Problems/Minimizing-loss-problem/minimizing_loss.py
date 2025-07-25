def minimize_loss(arr):
    current_min = (None,None,float('inf'))
    
    if len(arr) < 2:
        return (None, None, float('inf'))
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            result = arr[i] - arr[j]
            if result < current_min[2] and result > 0:
                current_min = (i,j,arr[i]-arr[j])
    
    if current_min[2] == float('inf'):
        return 'No valid years for minimum loss'
    return current_min
    
    

print(minimize_loss([20,15,7,2,13]))