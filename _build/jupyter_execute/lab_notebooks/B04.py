# 💻 Б4: Yersinia pestis ДНА секвенца

```{admonition} Опис на барање
:class: tip
Да се преземе комплетната ДНА секвенција на Yersinia pestis
(бактерија која ги инфектира белите дробови и предизвикува
пневмонија). До неа се пристапува со употреба на
идентификациониот број **NC_005816** во GeneBank базата
(работете со **SeqIO** објекти, имате детали во
документацијата).
```

Читање на **Genbank** фајл и принтање на секвенцата:

from Bio import SeqIO

record = SeqIO.read("yersinia-pestis-fasta/NC_005816.gb", "genbank")
# print(record)

print(f'Секвенцата: {record.seq[:15]}...{record.seq[-1]}')
print(f'Сите влезови во feature табалета: {len(record.features)}')
print(f'Извор за базата:  {record.annotations["source"]}')

**Транскрипција** на прочитаната секвенца: 

rna_seq = record.seq.transcribe()
print(f'РНА од секвенцата: {rna_seq[:20]}...{rna_seq[-2]}{rna_seq[-1]}')

**Транслација** на нуклеотидите:

protein_seq = record.seq.translate()
print(f'Протеинска секвенца: {protein_seq[:40]}...{protein_seq[-2]}{protein_seq[-1]}')

**Транслација** на нуклеотидите то првиот стоп кодон и потоа прекинува:

protein_seq_w = record.seq.translate(to_stop=True)
print(f'Протеинска секвенца до прв стоп кодон: {protein_seq_w}')