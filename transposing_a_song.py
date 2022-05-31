def transpose(song, interval):
    sharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    flat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    f_ind = []
    s_ind = []

    for i in song:
        f_ind.append(flat.index(i) + interval)

    for i in f_ind:
        if i not in len(sharp):
            if sharp[i] > 0:
                j = sharp[i] - len(sharp)
                s_ind.append(sharp[j])
            else:
                j = sharp[i] + len(sharp)
                s_ind.append(sharp[j])
        else:
            s_ind.append(sharp[i])

    print(s_ind)

transpose(["A", "Db"], 1)
