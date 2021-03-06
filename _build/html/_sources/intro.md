# Вовед

**Опис на книга:** Лабораториска вежба по предметот *Вовед во биоинформатика* <br>
**Рок за изработка на вежба:** 01-Јуни-2021 <br>
**Изработил:** Кирил Зеленковски [161141] <br>
**Линк до фајлови:** https://osf.io/pc7q9/ <br>


## Детален опис на барања [1-13]

<details><summary> <b>💻 Барање 1:</b> Парсирање на фајлови </font> </summary><br>
Да се реализираат примери за парсирање на FASTA и
GenBank формати, онака како што е објаснето во поглавје 2.4
од туторијалот. <br> <hr>
</details> 


<details><summary> <b>💻 Барање 2:</b> Поврзување со биолошки бази </font> </summary><br>
Да се напишат 3 примери за поврзување со различни
биолошки бази, како што е опишано во поглавје 2.5 од
туторијалот. <br><hr>
</details>


<details><summary> <b>💻 Барање 3:</b> Seq објекти </font> </summary><br>
Да се напише пример за работа со Seq објекти, како што е
опишано во поглавје 3, и да се обрне внимание на процесите
транскрипција и транслација. <br><hr>
</details>


<details><summary> <b>💻 Барање 4:</b> Yersinia pestis ДНА секвенца </font> </summary><br>
Да се преземе комплетната ДНА секвенца на Yersinia pestis
(бактерија која ги инфектира белите дробови и предизвикува
пневмонија). До неа се пристапува со употреба на
идентификациониот број **NC_005816** во GeneBank базата
(работете со **SeqIO** објекти, имате детали во
документацијата). <br><hr>
</details>


<details><summary> <b>💻 Барање 5:</b> Репликација на секвенца </font> </summary><br>
Имплеметирајте репликација на секвенцијата потпомогнатаод функции во BioPython. <br><hr>
</details>


<details><summary> <b>💻 Барање 6:</b> Пронаоѓање на сите CDS </font> </summary><br>
Со помош на biopython, пронајдете ги секвенциите на
различните кодни региони означени како (CDS). CDS се
регионите добиени после процедурата на отсекување на
интроните.<br><hr>
</details>


<details><summary> <b>💻 Барање 7:</b> Старт/стоп кодони во произволен CDS </font> </summary><br>
Одберете еден CDS (во мојот случај "pim") и најдете ги сите старт и стоп кодони во
неговата РНА.<br><hr>
</details>


<details><summary> <b>💻 Барање 8:</b> Транслација на секвенца </font> </summary><br>
Од произволниот CDS што го избравте добивте стоп/старт кодони. Направете транслација за да ги добиете сите можни
протеински секвенции.<br><hr>
</details>


<details><summary> <b>💻 Барање 9:</b> Мутација на секвенца </font> </summary><br>
Одберете еден од кодните региони и направете мутација со
поместување на рамката за 2 нуклеотиди. Анализирајте ги
новите протеински секвенции. Внимавајте, сега има нови
старт и стоп кодони.<br><hr>
</details>


<details><summary> <b>💻 Барање 10:</b> Креирање на FASTA фајл </font> </summary><br>
Да се разработи поглавје 5.5 за креирање на сопствени
записи во fasta формат.<br><hr>
</details>


<details><summary> <b>💻 Барање 11:</b> Предвидување на структурата на
оперон со SVM </font> </summary><br>
Да реализира примерот за предвидување на структурата на
оперонот кај бактеријата Bacillus subtilis опишан во поглавје
16 од туторијалот. Да се употреби методот на Логистичка
регресија и Машини со Поддржувачки Вектори (SVM) и да се
споредат резултатите.<br><hr>
</details>


<details><summary> <b>💻 Барање 12:</b> Имплементација на Nussinov функција </font> </summary><br>
Да се испрограмира алгоритмот на Nussinov како функција во
python која на влез ќе добива стринг од нуклеотиди, а на
излезе ќе ја дава нивната секундарна структура.<br><hr>
</details>


<details><summary> <b>💻 Барање 13:</b> BioPython за предвидување на секундарна структура</font> </summary><br>
Да се истражи можноста на biopython за одредување на
секундарна структура опишана во поглавје 11.6.9.<br><hr>
</details>

## Користење на Jupyter-book

Форматот на извештајот за решенијата на лабораториската вежба е во облик на книга (jupyter-book) која е: <br>

**Интерактивна:** Книгата содржи голем број на интерактивни графици кои ја користат *Python* библиотеката [Plotly](https://plotly.com/), каде може да се манипулираат исходите на кривите со променување на иницијалните вредности со помош на лизгачи, 
мени со опции и временски зависни лизгачи. 


**Репродусибилна:** Тетратките во книгата се <u>репродусибилни</u> (или во фаза да бидат) во две инстанци: 
- [Binder](https://gist.github.com/zelenkastiot/ca6f8dc92d1a9722a6e73dfb9ecd3265) (Linux container, [повеќе за Binder](https://blog.jupyter.org/mybinder-org-serves-two-million-launches-7543ae498a2a#:~:text=What%20is%20mybinder.org%3F,a%20collection%20of%20interactive%20notebooks.&text=All%20they%20have%20to%20do,without%20having%20to%20install%20anything.)) 
- [Google Colab](https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d#:~:text=What%20is%20Google%20Colab%3F,TensorFlow%2C%20PyTorch%2C%20and%20OpenCV.) тетратка

**Надградба на PDF:** Извештајот од ваков облик нуди можност за highlighting и додавање на annotations при потреба. Доколку селектирате текст ви овозможува да бирате дали сакате да додадете highlight или annotation. Оваа карактеристки користи [Hypothes](https://web.hypothes.is/). Повеќе за Hypothes може да прочитате на следниот [линк](https://web.hypothes.is/about/). 


За *Google Colab* и *Hypothes* потребно е само gmail профил, додека за *Binder* нема потреба од никакво поврзување. 


<br>

<p align="center">
<img src="https://raw.githubusercontent.com/zelenelez/images/master/finki.jpg" width=70%;></img> <br>
Пролет, 2021
</p>
