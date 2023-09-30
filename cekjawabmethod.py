def cek_jawaban(kunci_jawaban, jawaban):
    if kunci_jawaban==jawaban:
        return "benar"
    else:
        return "salah"

jawaban = "abdde"
kunci = "abcde"

for i in range(len(jawaban)):
    print(cek_jawaban(kunci[i],jawaban[i]))

