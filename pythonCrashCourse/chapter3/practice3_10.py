idols = ['Toyama Kasumi', 'Ichigaya Arisa', 'Ushigome Rimi', 'Hanazono Tae', 'Yamabuki Saya']
print(idols)

t = sorted(idols)
print(t)

t.reverse()
print(t)

kasumi = idols.pop(0)
print(idols)

idols.insert(len(idols), kasumi)
print(idols)

idols.sort()
print(idols)

for i in range(len(idols)):
    del idols[0]

print(idols)
