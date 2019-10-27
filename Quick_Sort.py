def quicksort(numberlist):
    i = 0

    if len(numberlist) == 1 or len(numberlist) == 0:
        return numberlist

    else:
        pivot = numberlist[i]

        for j in range(len(numberlist)-1):
            if numberlist[j + 1] < pivot:
                x = numberlist[j + 1]
                y = numberlist[i + 1]
                numberlist[j + 1] = y
                numberlist[i + 1] = x
                i += 1

        numberlist[0], numberlist[i] = numberlist[i], numberlist[0]
        lefthalf = quicksort(numberlist[:i])
        righthalf = quicksort(numberlist[i+1:])
        lefthalf.append(numberlist[i])
        return lefthalf + righthalf


def main():
    mynumbers = [23, 30, 91, 21, 88, 45, 9, 72, 186, 5]
    print("Unsorted List: " + str(mynumbers))
    mynumbers = quicksort(mynumbers)
    print("Sorted List: " + str(mynumbers))


main()
