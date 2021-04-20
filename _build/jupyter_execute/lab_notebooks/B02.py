# 💻 Б2: Поврзување со биолошки бази

```{admonition} Опис на барање
:class: tip
Да се напишат 3 примери за поврзување со различни
биолошки бази, како што е опишано во поглавје 2.5 од
туторијалот.
```


Од наведените можности за поврзување со различни биолошки бази одлучив да се обидам со: 
- [**NCBI BLAST web server**](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome)
- [**Entrez**](https://www.ncbi.nlm.nih.gov/Web/Search/entrezfs.html)
- [**SwissProt**](https://www.uniprot.org/)
- [**ExPASy**](https://prosite.expasy.org/)

## <u>1 Пример:</u> Со користење на **NCBI Blast server**

Пример сме изолирале некое парче од ДНА во лабораторија и сме ја добиле соодветната секвенца. Потоа сакаме да видиме на каков организам припаѓа таа ДНА. Доколку прашаме некој биолог ќе ни речe: "BLAST it" ~ што е слично на "Google it" во овој свет на биоинформатика. 

**BLAST** е алгритам за совпаѓање (aligment) што ја пребарува секвенцата што ја имаме од интерес во енормна база од податоци за вакви секвенци чии корени се познати. Доколку не користиме BioPython можеме да земеме едноставна секвенца да одиме на [NCBI BLAST web server](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome) и со неколку кликови да добиеме дека пример таа припаѓа на црв или мајмун. Но, со помош на BioPython ова може да го правиме со неколку линии код. 
 

Qblast методот од <code>Bio.Blast.NCBIWWW</code> есенцијално ја праќа секвенцата која ја даваме како влез до овој BLAST веб сервер. Во примерот кој ќе го користам за демонстрирање го користам "nucleotice BLAST" алгоритамот така што може да речеме дека користиме дата база од сите вакви нуклеотидни секвенци кои се викаат <code>nt</code>:

from Bio.Blast import NCBIWWW
from Bio.Seq import Seq

result_handle = NCBIWWW.qblast("blastn", "nt", Seq("AAAAGGAGAGAGAGTTTATA"))

Чекаме неколку секунди и добиваме резултат во <code>result_handle</code>, што е еден вид на привремен објект од кој ќе читаме. Форматот на овој фајл е <u><code>XML</code></u> така што не е лесно да се чита, но благодарение на BioPython кој има XML parser може лесно да се екстрахира оваа информација:

from Bio.Blast import NCBIXML

blast_records = NCBIXML.parse(result_handle)

Значи добиваме еден вид на итератор од BLAST објекти или "резултати од пребарување". Можеме да ги итрерираме сите во циклус и да принтаме одредени информации. 

Следната ќелија код е итерирање низ сите резултати, и секаде каде има некакви совпаѓања со секвенци од организми во дата базата во која пребарувавме тие се печтатат: 

for b in blast_records:
    for alignment in b.alignments:
        for hsp in alignment.hsps:
            print('----Alignment----')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')

## <u> 2 Пример:</u> Со користење на **Entrez** 

from Bio import Entrez
from Bio import SeqIO

Entrez.email = "zelenkastiot@gmail.com"  
handle = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")

print(record.id)
print(record.description)
print(len(record.features))

print(f'Првите 20 бази: {record.seq[0:20]}')

## <u> 3 Пример:</u> Со користење на **SwissProt** 

from Bio import SwissProt
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/biopython/biopython/master/Tests/SwissProt/F2CXE6.txt"
handle = urlopen(url)
record = SwissProt.read(handle)

print(record.description)

print(record.sequence)

## <u>4 Пример:</u> Со користење на **ExPASy**

from IPython.core.display import display, HTML
from Bio import ExPASy
from Bio.ExPASy import Prodoc
# Земен од: https://prosite.expasy.org/
# Fibronectin type-II collagen-binding domain signature and profile

handle = ExPASy.get_prosite_entry("PS51092")
html = handle.read() 
with open("html/Fibronectin.html", "w") as out_handle:
    out_handle.write(html)
display(HTML("Fibronectin.html"))