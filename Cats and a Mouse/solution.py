import os


def catAndMouse(x, y, z):
    dist_cat_a_mouse = abs(x - z)
    dist_cat_b_mouse = abs(y - z)
    if dist_cat_a_mouse < dist_cat_b_mouse:
        return "Cat A"
    elif dist_cat_b_mouse < dist_cat_a_mouse:
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
