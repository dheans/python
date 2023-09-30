
import random

pelajaran = ["Matematika", "Bahasa Inggris", "Fisika", "Kimia", "Biologi",
            "Sejarah", "Geografi", "Ekonomi", "Sosiologi", "Seni Budaya",
            "Pendidikan Jasmani", "Fikih", "Quran Hadis",
            "B. Arab", "Aqidah Akhlak", "B Asing"]
            
clas = ["Kelas 1A", "Kelas 1B", "Kelas 2A", "Kelas 2B", "Kelas 3A", "Kelas 3B"]

jadwal = {}


for class_name in clas:
    
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday=[]
    
    for subject in pelajaran:
        day = random.choice([monday, tuesday, wednesday, thursday, friday])
        day.append(subject)
    
    
    jadwal[class_name] = [monday, tuesday, wednesday, thursday, friday]


for class_name, class_schedule in jadwal.items():
    print(f"{class_name}:")
    for i, day in enumerate(class_schedule):
        print(f"Hari ke-{i+1}: {', '.join(day)}")
    print()
