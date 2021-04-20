# 💻 Б1: Парсирање на фајлови

```{admonition} Опис на барање
:class: tip

Да се реализираат примери за парсирање на *FASTA* и
*GenBank* формати, онака како што е објаснето во поглавје 2.4
од туторијалот.
```

*FASTA* datasets: 
1. **Setaria italica** strain Yugu1 chromosome VIII, whole genome shotgun sequence <br>
ENA: CM003535 [[1]](https://www.ebi.ac.uk/ena/browser/view/CM003535)
2. **Variola major virus** (strain Bangladesh-1975) complete genome <br>
GenBank: L22579.1 [[2]](https://www.ncbi.nlm.nih.gov/nuccore/L22579.1?report=docsum&log$=seqview)
3. **Bovine papular stomatitis virus**, complete genome <br> 
NCBI Reference Sequence: NC_005337.1 [[3]](https://www.ncbi.nlm.nih.gov/nuccore/NC_005337.1?report=genbank)
4. **Homo sapiens hepatitis A virus cellular receptor 1 (HAVCR1)**, transcript variant 1, mRNA <br>
NCBI Reference Sequence: NM_012206.3 [[4]](https://www.ncbi.nlm.nih.gov/nuccore/NM_012206.3)

Импортирање на главниот модул:

from Bio import SeqIO

## <u>1:</u> **Setaria italica strain Yugu1 chromosome VIII, whole genome shotgun sequence.**

**FASTA** фајл: 

for seq_record in SeqIO.parse("fasta-examples/CM003535.1.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

## <u>2:</u> **Variola major virus (strain Bangladesh-1975) complete genome**

**FASTA** фајл: 

for seq_record in SeqIO.parse("fasta-examples/variola-major-virus-1.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

**Genbank** фајл:

for seq_record in SeqIO.parse("fasta-examples/variola-major-virus-2.gb", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

## <u>3:</u> **Bovine papular stomatitis virus, complete genome**

**FASTA** фајл: 

for seq_record in SeqIO.parse("fasta-examples/bovine-papular-stomatitis-virus-1.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

**Genbank** фајл:

for seq_record in SeqIO.parse("fasta-examples/bovine-papular-stomatitis-virus-2.gb", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

## <u>4:</u> **Homo sapiens hepatitis A virus cellular receptor 1 (HAVCR1), transcript variant 1, mRNA**

**FASTA** фајл: 

for seq_record in SeqIO.parse("fasta-examples/HAVCR1-1.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

**Genbank** фајл: 

for seq_record in SeqIO.parse("fasta-examples/HAVCR1-2.gb", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))