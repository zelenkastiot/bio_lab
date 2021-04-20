# 💻 Б8: Транслација на секвенца


```{admonition} Опис на барање
:class: tip
Од произволниот CDS што го избравте добивте стоп/старт кодони. Направете транслација за да ги добиете сите можни
протеински секвенции.
```

from Bio import SeqIO
from Bio.Data import CodonTable

gene_record = SeqIO.read("yersinia-pestis-fasta/NC_005816.gb", "genbank")
mito_table = CodonTable.unambiguous_rna_by_id[11]

# Читање на 'pim'
sub_record = gene_record[4342:4780]
# Транскрипција на 'pim'
sub_rna = sub_record.seq.transcribe()
# Листи за позиции на старт и стоп кодони за 'pim'
start_codon_positions = []
stop_codon_positions = []
# Листи за имињата на најдените кодони за 'pim'
start_found = []
stop_found = []
# Конверзија во стринг, за полесна работа
rna_string = str(sub_rna)

"""
Идеја на пребарување: 
- Започни од 0 и движи се до целата секвенца -2
- Земи го моменталниот триплет 
- Провери дали е во старт кодоните -> Ако е зачувај торка (позиција, триплет)
- Ако не, провери дали е во стоп кодоните -> Ако е зачувај торка (позиција, триплет)
- Зголеми го бројачот 
"""

k = 0
while k < len(rna_string)-2:
    # екстрахирај моментална три-нуклеотидна суб-секвенца
    current_codon = rna_string[k:k+3]
    if current_codon in mito_table.start_codons:
        start_found.append((k, current_codon))
    elif current_codon in mito_table.stop_codons:
        stop_found.append((k, current_codon))
    k += 1

Во претходното барање (💻 Б7) ги доззнавме сите **64 старт кодони** и **21 стоп кодони**. Овие две бројки ни укажуваат на тоадека можеме да комбинираме на различни начини за да екстрахираме *протеински* секвенци т.е. да ги добиеме соодветните амино-киселени за протеинската секвенца од тоа парче на РНА. 

````{margin}
```{admonition} Важно за **транслација**
:class: caution
Многу важен услов при транслација меѓу старт/стоп кодони е тоа дека позицијата каде е пронајден старт кодонот, првата позиција на РНА секвенцата која ја преведуваме, мора да е помал број (позиција) од таа на стоп кодонот. 


Ова е повеќе логичка грешка што може да настане доколку сакаме да ги најдеме сите можно комбинации од старт и стоп кодони (мора да имаме услов кој би проверувал позициите да се соодветни. 
```
````

print(f'Вкупен број на старт кодони: {len(start_found)}')
print(f'Старт кодон со позиција: {start_found}')
print()
print(f'Вкупен број на стоп кодони: {len(stop_found)}')
print(f'Стоп кодон со позиција: {stop_found}')

Сега бидејќи има голем број на комбинации ќе изберам неколку (3-4) за да демонстрирам како изгледа процесот на **транслација** од таа РНА-субсеквенца, која:
- **почнува** на позицијата на <u>првата база</u> од избраниот <u>старт кодон</u> 
- **завршува** на позицијата на <u>последната база</u> од избраниот <u>стоп кодон</u> (позиција + 2; за последните 2 бази од стоп кодонот)

## Траснлација 1

````{margin}
```{admonition} Екстрахирана секвенца 1 
:class: note
<code>protein_seq1</code>
- Старт кодон (0, 'AUG') 
- Стоп кодон (13, 'UGA')
```
````

print(f"Старт кодон: {start_found[0]}")
print(f"Стоп кодон: {stop_found[0]}")
read_seq1 = sub_rna[start_found[0][0]:stop_found[0][0]+2]
print(f'Екстрахирана секвенца од избраните кодони: {read_seq1}')
print(f'Должина: {len(read_seq1)}')

Излез по преведување: 

protein_seq1 = read_seq1.translate(table='Bacterial')
print(f'Протеинска секвенца 1:\n{protein_seq1}')
print(f'Должина: {len(protein_seq1)}')

## Траснлација 2

````{margin}
```{admonition} Екстрахирана секвенца 2
:class: note
<code>protein_seq2</code>
- Старт кодон (315, 'AUC')
- Стоп кодон (334, 'UAG')
```
````

print(f"Старт кодон: {start_found[2]}")
print(f"Стоп кодон: {stop_found[13]}")
read_seq2 = sub_rna[start_found[2][0]:stop_found[12][0]+2]
print(f'Екстрахирана секвенца од избраните кодони: {read_seq2}')
print(f'Должина: {len(read_seq2)}')

Излез по преведување: 

protein_seq2 = read_seq2.translate(table='Bacterial')
print(f'Протеинска секвенца 2:\n{protein_seq2}')
print(f'Должина: {len(protein_seq2)}')

## Траснлација 3

````{margin}
```{admonition} Екстрахирана секвенца 
:class: note
<code>protein_seq3</code>
- Старт кодон (251, 'AUC')
- Стоп кодон  (435, 'UAA')
```
````

print(f"Старт кодон: {start_found[34]}")
print(f"Стоп кодон: {stop_found[20]}")
read_seq3 = sub_rna[start_found[34][0]:stop_found[20][0]+2]
print(f'Екстрахирана секвенца од избраните кодони: {read_seq3}')
print(f'Должина: {len(read_seq3)}')

Излез по преведување: 

protein_seq3 = read_seq3.translate(table='Bacterial')
print(f'Протеинска секвенца 3:\n{protein_seq3}')
print(f'Должина: {len(protein_seq3)}')

## Транслација 4

````{margin}
```{admonition} Пример 4
:class: note
<code>protein_seq4</code>
- Старт кодон (0, 'AUG')
- Стоп кодон  (435, 'UAA')
```
````

print(f"Старт кодон: {start_found[0]}")
print(f"Стоп кодон: {stop_found[-1]}")
read_seq4 = sub_rna[start_found[0][0]:stop_found[20][0]+2]
print(f'Екстрахирана секвенца од избраните кодони: {read_seq4}')
print(f'Должина: {len(read_seq4)}')

Излез по преведување: 

protein_seq4 = read_seq4.translate(table='Bacterial')
print(f'Протеинска секвенца 4:\n{protein_seq4}')
print(f'Должина: {len(protein_seq4)}')