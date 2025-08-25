def tower_of_hanoi(disk:int, A:int, B:int, C:int, ans:list)->list:

    # step1: define a base case....
    if disk == 0:
        return ans
    # step2: move n-1 disks from A to B
    tower_of_hanoi(disk-1,A,C,B,ans)
    # step3: move nth disk from A to C
    ans.append([disk,A,C])
    # step4: move n-1 disks back from B to C
    tower_of_hanoi(disk-1,B,A,C,ans)
    return ans


if __name__ == '__main__':
    disk = 2
    print(tower_of_hanoi(disk,1,2,3,[]))

