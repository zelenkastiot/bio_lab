# 💻 Б10: Креирање на FASTA фајл


```{admonition} Опис на барање
:class: tip
Да се разработи поглавје 5.5 за креирање на сопствени
записи во fasta формат.
```

Правење на FASTA фајл од транслација на протеините до првиот стоп кодон на Yersinia pestis FASTA фајлот. Есенцијално идејата е од ДНА да направам нов FASTA фајл но за преведените протеини. 

from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

def make_protein_record(nuc_record):
    """Returns a new SeqRecord with the translated sequence (default table)."""
    return SeqRecord(
        seq=nuc_record.seq.translate(to_stop=True),
        id="trans_" + nuc_record.id,
        description="translation of CDS, using default table",
    )

proteins = (
    make_protein_record(nuc_rec)
    for nuc_rec in SeqIO.parse("yersinia-pestis-fasta/NC_005816.fna", "fasta")
)
SeqIO.write(proteins, "yersinia-pestis-fasta/NC_005816_translations.fasta", "fasta")

protein_fasta = SeqIO.read("yersinia-pestis-fasta/NC_005816_translations.fasta", "fasta")
print(f'Нов FASTA запис NC_005816_translations.fasta: {protein_fasta.seq}')