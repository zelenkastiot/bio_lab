# 💻 Б7: Старт/стоп кодони во произволен CDS

```{admonition} Опис на барање
:class: tip
Одберете еден CDS и најдете ги сите старт и стоп кодони во
неговата РНА.
```

За произволен CDS врз кој ќе експериментирам, се одлучив да одам со "<code>pim</code>" генот, ;**YP_pPCP05**:

from Bio import SeqIO
gene_record = SeqIO.read("yersinia-pestis-fasta/NC_005816.gb", "genbank")

print(gene_record.features[21])

Локацијата ја зимам од главната секвенца и истотака табелата за преведување на RNA е со вредност 11! Ова е доста корисно за транслација.

Зимање на подстринг од главната секвенца:

sub_record = gene_record[4342:4780]
print(sub_record)
print(len(sub_record))

Добивање на **RNA** со транскрипција од подстрингот:

sub_rna = sub_record.seq.transcribe()
print(sub_rna)

Табела за процесот на транслација:

from Bio.Data import CodonTable

mito_table = CodonTable.unambiguous_rna_by_id[11]
print(mito_table)

Соодветните старт/стоп кодони според табелата со број 11:

print(f"Старт кодони: {mito_table.start_codons}")
print(f"Стоп кодони: {mito_table.stop_codons}")

# Листи за позиции на старт и стоп кодони
start_codon_positions = []
stop_codon_positions = []
# Листи за имињата на најдените кодони
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
    # extract a three-nucleotide subsequence
    current_codon = rna_string[k:k+3]
    if current_codon in mito_table.start_codons:
        start_found.append((k, current_codon))
    elif current_codon in mito_table.stop_codons:
        stop_found.append((k, current_codon))
    k += 1

print(gene_record.features[21])
print(f"Вкупна должина на CBS: {len(sub_rna)}")
print(sub_rna)
print()
print(f'Вкупен број на старт кодони: {len(start_found)}')
print(f'Најден старт кодон со позиција: {start_found}')
print()
print(f'Вкупен број на стоп кодони: {len(stop_found)}')
print(f'Најден стоп кодон со позиција: {stop_found}')

Ова е конечниот резултат од пребарувањето и интересното што може да се забележи е дека некои од кодоните старт и стоп се поклопуваат и во следното барање при процесот на **транслација** можеме да видиме дека може произволно да зимаме комбинации од еден старт и стоп за да читаме триплети во процесот на транслација од РНА во протеинска секвенца.  