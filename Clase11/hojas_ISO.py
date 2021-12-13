def medidas_hoja_A(N):
    if N == 0:
        return (841, 1189)
    else:
        size = medidas_hoja_A(N - 1)
        w = size[1] // 2
        h = size[0]
        # print(w, h)
        return (w, h)