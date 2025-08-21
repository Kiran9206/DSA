def colorful_number(A:int)->int:

    arr = []; product_arr = []
    while A != 0:
        n = A % 10
        arr.append(n)
        A //= 10

    for start in range(len(arr)):
        product = 1
        for end in range(start, len(arr)):
            product *= arr[end]
            product_arr.append(product)
    for idx in range(len(product_arr)):
        if product_arr[idx] in product_arr[idx+1:]:
            return 0
    return 1
