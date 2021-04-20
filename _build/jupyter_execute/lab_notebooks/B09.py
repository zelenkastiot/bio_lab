# 💻 Б9: Мутација на секвенца


```{admonition} Опис на барање
:class: tip
Одберете еден од кодните региони и направете мутација со
поместување на рамката за 2 нуклеотиди. Анализирајте ги
новите протеински секвенции. Внимавајте, сега има нови
старт и стоп кодони.
```

Бидејќи во претходните две барања работев со кодниот регион <code>"pim"</code>, ќе продложам и тука со мутација за поместување на рамката. Мутација е со поместување за 2 нуклеотида десно: 

 > Модифицирање на рамката на <code>"pim"</code><br>43<mark><b>42</b></mark>:47<mark><b>80</b></mark> &#8594; 43<mark><b>44</b></mark>:47<mark><b>82</b></mark>

from Bio import SeqIO
from Bio.Data import CodonTable

gene_record = SeqIO.read("yersinia-pestis-fasta/NC_005816.gb", "genbank")
mito_table = CodonTable.unambiguous_rna_by_id[11]

sub_record2 = gene_record[4344:4782]

sub_rna2 = sub_record2.seq.transcribe()
print(f"Мутирана 'pim' секвенца:\n{sub_rna2}\n")
print(f"Должина на секвенца: {len(sub_rna2)}")

За најдобро да ја согледаме мутацијата нужно е да ја преведеме оваа *РНА*, т.е.да ги најдеме соодветните старт и стоп региони кои очекуваме да се разликуваат од првобитната верзија на <code>"pim"</code> *РНА* и нив да ги преведеме во соодветните амино киселини. 

# Листи за позиции на старт и стоп кодони
start_codon_positions2 = []
stop_codon_positions2 = []
# Листи за имињата на најдените кодони
start_found2 = []
stop_found2 = []
# Конверзија во стринг, за полесна работа
rna_string2 = str(sub_rna2)

"""
Идеја на пребарување: 
- Започни од 0 и движи се до целата секвенца -2
- Земи го моменталниот триплет 
- Провери дали е во старт кодоните -> Ако е зачувај торка (позиција, триплет)
- Ако не, провери дали е во стоп кодоните -> Ако е зачувај торка (позиција, триплет)
- Зголеми го бројачот 
"""

k = 0
while k < len(rna_string2)-2:
    # extract a three-nucleotide subsequence
    current_codon = rna_string2[k:k+3]
    if current_codon in mito_table.start_codons:
        start_found2.append((k, current_codon))
    elif current_codon in mito_table.stop_codons:
        stop_found2.append((k, current_codon))
    k += 1

print(f"Вкупна должина на CBS: {len(sub_rna2)}")
print(sub_rna2)
print()
print(f'Вкупен број на старт кодони: {len(start_found2)}')
print(f'Најден старт кодон со позиција: {start_found2}')
print()
print(f'Вкупен број на стоп кодони: {len(stop_found2)}')
print(f'Најден стоп кодон со позиција: {stop_found2}')