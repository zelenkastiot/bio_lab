# 💻 Б5: Репликација на секвенца

```{admonition} Опис на барање
:class: tip
Имплеметирајте репликација на секвенцијата потпомогнатаод функции во **BioPython**.
```

Процесот на репликација е доста тривијален во однос на кодирање, се прави копија од самата ДНА секвенца. Пример за репликација врз рандом секвенца (од консултации): 

from Bio.Seq import Seq

seq = Seq("ATTGGGTTAAC")
print(f'Оригинална секвенца:  {seq}')

seq_3 = seq.complement()
print(f'Реплицирана секвенца: {seq_3.complement()}')

Пример врз **Yersinia pestis** [9609 базни парови] ДНА секвенцата: 

from Bio import SeqIO

record = SeqIO.read("yersinia-pestis-fasta/NC_005816.gb", "genbank")
print(f'Оригинална секвенца:  {record.seq[:15]}...{record.seq[-1]}')

record_comp = record.seq.complement()
dna_rep = record_comp.complement()
print(f'Реплицирана секвенца: {dna_rep[:15]}...{dna_rep[-1]}')