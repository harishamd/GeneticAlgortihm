import numpy
import matplotlib.pyplot

print("==========PROGRAM ALGORITMA GENTIKA==========")
#input_batasan
b_input = [-3,1,2,-1,3,-2]
#batasan
b_panjang =(6) 


#menentukan ukuran populasi
ukur_pop = 10
uk_kawin_ortu = 3
pop_uk = (ukur_pop, b_panjang)

#buat polulasi awal
baru_pop = numpy.random.uniform (low = -3, high = 3, size=pop_uk)
#menampilkan populasi baru berd. input batasan
print("Populasi = \n", baru_pop)
print("============================================================================")

uk_generasi = 6

def pop_kebugaran(b_input, pop):
    fitness = numpy.sum(pop*b_input, axis=1)
    return fitness

def pil_ortu(pop, fitness, uk_ortu):
    ortu = numpy.empty((uk_ortu, pop.shape[1]))
    for uk_ortu in range (uk_ortu):
        maks_fitness = numpy.where(fitness == numpy.max(fitness))
        maks_fitness = maks_fitness[0][0]
        ortu[uk_ortu, :] = pop[maks_fitness] 
        fitness[maks_fitness] = -100
    return ortu

def pindahsilang(ortu, offspring_size):
    offspring = numpy.empty(offspring_size)
    no_pindahsilang = numpy.uint8(offspring_size[1]/2)

    for j in range (offspring_size[0]):
        ortu1 = j%ortu.shape[0]
        ortu2 = (j+1)%ortu.shape[0]
        offspring[j, 0:no_pindahsilang] = ortu[ortu1, 0:no_pindahsilang]
        offspring[j, no_pindahsilang:] = ortu[ortu2, no_pindahsilang]
    return offspring

def mutasi(offspring_silang, uk_mutasi=1):
    mutasi_hit=numpy.uint8(offspring_silang.shape[1] / uk_mutasi)    
    return offspring_silang   

terbaik = []

for generasi in range (uk_generasi):
    fitness = pop_kebugaran(b_input, baru_pop)
    print("Fitness = \n",fitness)
    print("============================================================================")
       
    ortu = pil_ortu (baru_pop, fitness, uk_kawin_ortu)
    print("Parents/Orang tua = \n", ortu)
    print("============================================================================")
    
    keturunan_silang = pindahsilang(ortu, offspring_size = (pop_uk[0]-ortu.shape[0],b_panjang))
    print("Keturunan Silang = \n", keturunan_silang)
    print("============================================================================")

    mutation = mutasi(keturunan_silang, uk_mutasi=2)
    print("Mutasi = \n", mutation)
    print("============================================================================")

    terbaik.append(numpy.max(numpy.sum(baru_pop*b_input, axis=1)))
    print("Terbaik : \n", numpy.max(numpy.sum(baru_pop*b_input, axis=1)))
    print("============================================================================")

    print("Solusi Terbaik (Iterasi) : \n", numpy.max(fitness))
    print("============================================================================")
    print("Solusi Terbaik Fitness : \n", baru_pop,numpy.max(fitness))
    print("============================================================================")
    
   




 






















