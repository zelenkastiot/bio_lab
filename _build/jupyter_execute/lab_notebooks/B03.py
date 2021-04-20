# 💻 Б3: Seq објекти

```{admonition} Опис на барање
:class: tip
Да се напише пример за работа со Seq објекти, како што е
опишано во поглавје 3, и да се обрне внимание на процесите
транскрипција и транслација.
```

```{image} http://compeau.cbd.cmu.edu/wp-content/uploads/2016/08/rosalindlogo.jpg
:alt: rosalind
:class: bg-primary mb-1
:width: 210px
:height: 72px
:align: right
```

На [**Rosalind**](http://rosalind.info/problems/list-view/) има многу интересни проблеми каде мислев дека можеби е интересно да се обидам да ги решам со користење на <code>Bio.Seq</code> објекти. За ова барање ги решив точно следните проблеми: 

1. **Complementing a Strand of DNA**: http://rosalind.info/problems/revc/
2. **Transcribing DNA into RNA:** http://rosalind.info/problems/rna/
3. **Translating RNA into Protein:** http://rosalind.info/problems/prot/
4. **Computing GC Content**: http://rosalind.info/problems/gc/
5. **Finding a Motif in DNA**: http://rosalind.info/problems/subs/


```{admonition} **Rosalind** профил
:class: note

Профилот каде може да се види дека ги решив: http://rosalind.info/users/zelenkastiot/
```

## 1. [Complementing a Strand of DNA](http://rosalind.info/problems/revc/)

Овој проблем е поврзан со стрингови од ДНА, каде комплементи се паровите: A-T и C-G. 

Обратен комплемент (reverse complement) од ДНА стринг а стринг формиран со зимање на стрингот во обратен редослед и применување на комплемент, т.е. менување на базните парови со своите комплементарни парови (пример "*GTCA*" ако е влез, соодветен излез е "*TGAC*")


- **Влез:** <code>/rosalind/rosalind_revc.txt</code>текст фајл со ДНА стринг со должина од најмногу 1000 базни парови 
- **Излез:** Обратен комплемент од стрингот 

from Bio.Seq import Seq 

with open('rosalind/rosalind_revc.txt', 'r') as file:
    sample_dataset = file.read().replace('\n', '')

input_dna = Seq(sample_dataset)
output_rna = input_dna.reverse_complement()
print(output_rna)

## 2. [Transcribing DNA into RNA](http://rosalind.info/problems/rna/)

Овој проблем е поврзан со процесот на *транскрипција* каде идејата е при даден фајл со ДНА стринг преку процесот на *транскрипција* да се добие соодветната РНА. 

- **Влез:** <code>/rosalind/rosalind_rna.txt</code> - текст фајл со ДНА стринг со должина од најмногу 1000 базни парови 
- **Излез:** РНА стринг добиен од транскрипција на ДНА стрингот 

**Решение (Со примена на Bio.Seq):**

from Bio.Seq import Seq

with open('rosalind/rosalind_rna.txt', 'r') as file:
    sample_dataset = file.read().replace('\n', '')

input_dna = Seq(sample_dataset)
output_rna = input_dna.transcribe()
print(output_rna)

**Решение (Со операции на стрингови):**

rna = sample_dataset.replace("T", "U")
print(output_rna)

**Проверка за излезот:**

print(output_rna == rna)

## 3. [Translating RNA into Protein](http://rosalind.info/problems/prot/)

Овој проблем е поврзан со *транскрипција* од РНА во протеини. 20 најчести аминокиселни се означуваат користејќи ги сите 20 букви од Англиската азбука (сите освен B, J, O, U, X и Z). Стрингови од протеини се создаваат од овие 20 симболи. Овие секвенци заедно со ДНА и РНА секвенците исто така се вика генетски стринг.   

- **Влез:** <code>/rosalind/rosalind_prot.txt</code>текст фајл со РНА стринг со должина од најмногу 1000 базни парови 
- **Излез:** Протеинска секвенца (без стоп кодони)

Следната табeла е таа што се користи за процесот на транслација: 

from Bio.Data import CodonTable

standard_rna_table = CodonTable.unambiguous_rna_by_name["Standard"]
print(standard_rna_table)

**Решение:**

from Bio.Seq import Seq 

with open('rosalind/rosalind_prot.txt', 'r') as file:
    sample_dataset = file.read().replace('\n', '')

messenger_rna = Seq(sample_dataset)
protein_seq = messenger_rna.translate(to_stop=True)

print(protein_seq)

## 4. [Computing GC Content](http://rosalind.info/problems/gc/)

Овој проблем е поврзан со процентот на GC во ДНА секвенца.  

- **Влез:** <code>/rosalind/rosalind_gc.txt</code>FASTA фајл со неколку ID и своите секвенци 
- **Излез:** Најголемиот GC процент од целиот FASTA фајл

dict_records = {}
for seq_record in SeqIO.parse("rosalind/rosalind_gc.fasta", "fasta"):
    seq_temp = seq_record.seq
    dict_records[seq_record.id] = 100 * float(seq_temp.count("G") + seq_temp.count("C")) / len(seq_temp)

dict_records

max_value = max(dict_records.values())  # најголема вредност
max_keys = [k for k, v in dict_records.items() if v == max_value] # клуч со максимална вредност

print(max_keys[0])
print(f'{max_value:.6f}')

## 5. [Finding a Motif in DNA](http://rosalind.info/problems/subs/)

Овој проблем е поврзан со стрингови од ДНА и подстрингови од ДНА, познати како Motif. Наоѓање на вакви интерави од ДНА во геноми од различни организми (најчесто различен вид) покажува кон тоа дека тој подинтервал има иста функција кај двата организми. 

Motif е често споделувано парче од DNA, честа задача во молекуларна биологија е да се бараат вакви подстрингови.


- **Влез:** <code>/rosalind/rosalind_subs.txt</code> текст фајл со ДНА (прв ред), подстринг т.е. парче ДНА (втор ред)
- **Излез:** Сите позиции каде се јавува тој подстринг

file = open('rosalind/rosalind_subs.txt', 'r')

Lines = file.readlines()

dna_string = Lines[0].strip()
sub_string = Lines[1].strip()

found = []

k = 0
while k < len(dna_string)-3:
    current_codon = dna_string[k:k+(len(sub_string))]
    if current_codon == sub_string:
        found.append(k+1)
    k+=1

for i in range(len(found)):
    print(found[i], end=" ")