n = int(input())
arr = []
for i in range(n):
    arr.append(input())

class_I = [-2, -2, -2, -2]  # x_start, y_start, x_end, y_end
class_O = [[-2, -2], [-2, -2], [-2, -2], [-2, -2]]  # [up_bar_start, up_bar_end],
#  [left_pillar_start, left_pillar_end], [right_pillar_start, right_pillar_end], [down_bar_start, down_bar_end]
class_C = [[-2, -2], [-2, -2, -2], [-2, -2]]  # [up_bar_y_start, up_bar_y_end],
#  [left_pillar_start, left_pillar_end, up_bar_x_end], [down_bar_y_start, down_bar_y_end]
class_L = [[-2, -2, -2], [-2, -2, -2]]  # [left_pillar_start, left_pillar_end, down_bar_end], [down_bar_start, down_bar_end, left_pillar_up_start]
class_H = [[-2, -2], [-2, -2], [-2, -2], [-2, -2]]  # [center_bar_start, center_bar_end], [left_pillar_start, left_pillar_end], [right_pillar_start, right_pillar_end]
class_P = [[-2, -2], [-2, -2], [-2, -2], [-2, -2, -2]]

def check_for_i(layer, s, m):
    a = s.find("#")
    b = s.rfind("#")
    c = s.find(".", a)
    if m[0] == -1:
        return m
    if a == -1:
        if m[1] > -1 and m[3] == -2:
            m[3] = layer
        return m
    if a > -1 and m[1] == -2:
        m[1] = layer
    elif a > -1 and m[3] != -2:
        m[0] = -1
        return m
    if m[0] == -2 or m[0] == a:
        m[0] = a
    else:
        m[0] = -1
    if m[2] == -2 or m[2] == b + 1:
        m[2] = b + 1
    else:
        m[2] = -1
    if a < c < b:
        m[0] = -1
        m[2] = -1
    return m


def check_for_o(layer, s, m):
    a = s.find("#")
    b = s.find(".", a)
    c = s.rfind("#")
    d = s.rfind(".", b, c)
    e = s.find("#", b)
    if m[0][0] == -1:
        return m
    if a == -1:
        if m[3][0] > 0 and m[3][1] == -2:
            m[3][1] = layer
        return m
    if m[0][0] == -2:
        if -1 < b < c:
            m[0][0] = -1
        else:
            m[0][0] = layer
    elif (a < d) and m[0][0] > -1 and m[0][1] == -2:
        m[0][1] = layer
    if m[0][1] > -1 and m[3][0] == -2 and (b == -1 or b > c):
        m[3][0] = layer
    if m[0][1] == -2 or (m[3][0] > -1 and m[3][1] == -2):
        if m[1][0] == -2 or m[1][0] == a:
            m[1][0] = a
        else:
            m[0][0] = -1
        if m[2][1] == -2 or m[2][1] == c + 1:
            m[2][1] = c + 1
        else:
            m[0][0] = -1
        if a < b < c:
            m[0][0] = -1
    else:
        if m[1][0] != a:
            m[0][0] = -1
        if m[1][1] == -2 or m[1][1] == b:
            m[1][1] = b
        else:
            m[0][0] = -1
        if m[2][0] == -2 or m[2][0] == d + 1:
            m[2][0] = d + 1
        else:
            m[0][0] = -1
        if m[2][1] != c + 1:
            m[0][0] = -1
        if a < e < d:
            m[0][0] = -1
    return m


def check_for_c(layer, s, m):
    a = s.find("#")
    b = s.find(".", a)
    c = s.rfind("#")
    if m[0][0] == -1 or a < b < c:
        m[0][0] = -1
        return m
    if a == -1:
        if m[2][0] > 0 and m[2][1] == -2:
            m[2][1] = layer
        if m[0][0] > 0 and m[2][0] == -2:
            m[0][0] = -1
        return m
    if m[0][0] == -2:
        m[0][0] = layer
    elif a < b and m[0][0] > -1 and m[0][1] == -2:
        m[0][1] = layer
    if m[0][1] > -1 and m[2][0] == -2 and (m[1][2] == c + 1):
        m[2][0] = layer
    if m[0][1] == -2 or (m[2][0] > -1 and m[2][1] == -2):
        if m[1][0] == -2 or m[1][0] == a:
            m[1][0] = a
        else:
            m[0][0] = -1
        if m[1][2] == -2 or m[1][2] == c + 1:
            m[1][2] = c + 1
        else:
            m[0][0] = -1
    else:
        if m[1][0] != a:
            m[0][0] = -1
        if m[1][1] == -2 or m[1][1] == b:
            m[1][1] = b
        else:
            m[0][0] = -1
        if m[1][1] >= m[1][2]:
            m[0][0] = -1
    return m


def check_for_l(layer, s, m):
    # [left_pillar_start, left_pillar_end, down_bar_end], [down_bar_start, down_bar_end, left_pillar_up_start]
    a = s.find("#")
    b = s.find(".", a)
    c = s.rfind("#")
    if m[0][0] == -1 or a < b < c:
        m[0][0] = -1
        return m
    if a == -1:
        if m[1][0] > 0 and m[1][1] == -2:
            m[1][1] = layer
        return m
    elif m[1][1] > -1:
        m[0][0] = -1
        return m
    if m[1][2] == -2:
        m[1][2] = layer
    elif m[1][0] == -2 and m[0][2] == -2 and m[0][1] < c + 1:
        m[1][0] = layer
    if m[1][0] > -1 and m[1][1] == -2:
        if m[0][0] != a:
            m[0][0] = -1
        if m[0][2] == -2 or m[0][2] == c + 1:
            m[0][2] = c + 1
        else:
            m[0][0] = -1
    else:
        if m[0][0] == -2 or m[0][0] == a:
            m[0][0] = a
        else:
            m[0][0] = -1
        if m[0][1] == -2 or m[0][1] == b:
            m[0][1] = b
        else:
            m[0][0] = -1
    return m


def check_for_h(layer, s, m):
    a = s.find("#")
    b = s.find(".", a)
    c = s.rfind("#", b)
    d = s.rfind(".", b, c)
    e = s.find("#", b, d)
    if e > -1:
        m[0][0] = -1
    elif a == -1:
        m = check_for_o(layer, s, m)
    else:
        if m[1][1] == -2 and m[2][0] == -2:
            m[1][1] = b
            m[2][0] = d + 1
        a = m[1][1]
        b = m[2][0]
        s_start = s[:a]
        s_end = s[b:]
        s = s[a:b]
        s = s.replace(".", "w")
        s = s.replace("#", ".")
        s = s.replace("w", "#")
        s = s_start + s + s_end
        m = check_for_o(layer, s, m)
    return m


def check_for_p(layer, s, m):
    a = s.find("#")
    c = s.rfind("#")
    b = s.find(".", a, c)
    if m[3][0] == -2 or c + 1 == m[2][1]:
        return check_for_o(layer, s, m)
    m2 = [0]*4
    m2[0] = m[1][0]
    m2[1] = m[3][1]
    m2[2] = m[1][1]
    m2[3] = m[3][2]
    m2 = check_for_i(layer, s, m2)
    if m2[0] == -1:
        m[0][0] = -1
    m[1][0] = m2[0]
    m[3][1] = m2[1]
    m[1][1] = m2[2]
    m[3][2] = m2[3]
    return m


for i in range(n):
    class_I = check_for_i(i, arr[i], class_I)
    class_O = check_for_o(i, arr[i], class_O)
    class_C = check_for_c(i, arr[i], class_C)
    class_L = check_for_l(i, arr[i], class_L)
    class_H = check_for_h(i, arr[i], class_H)
    class_P = check_for_p(i, arr[i], class_P)

if -1 < class_I[0] < class_I[2] and (class_I[1] < class_I[3] or (class_I[3] == -2 and class_I[1] > -1)):
    print("I")
elif class_O[0][0] > -1 and -1 < class_O[1][1] <= class_O[2][0] and class_O[3][0] > 0:
    print("O")
elif class_C[0][0] > -1 and class_C[2][0] > -1 and class_C[1][1] < class_C[1][2]:
    print("C")
elif class_L[0][0] > -1 and class_L[1][0] > -1 and class_L[0][1] < class_L[0][2]:
    print("L")
elif class_H[0][0] > -1 and -1 < class_H[1][1] <= class_H[2][0] and class_H[3][0] > 0:
    print("H")
elif (class_P[0][0] > -1 and -1 < class_P[1][1] <= class_P[2][0] and class_P[3][0] > 0
      and -1 < class_P[1][0] < class_P[1][1] and (class_P[3][1] < class_P[3][2] or (class_P[3][2] == -2 and class_P[3][1] > -1))):
    print("P")
else:
    print("X")
