<div class="problem-statement"><div class="header"><h1 class="title">E. Наибольшее произведение двух чисел (составление тестов)</h1></div><h2></h2><div class="legend"><p>На соревновании участникам была предложена следующая задача:</p> 
<p>——</p> 
<p>Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых максимально. Выведите эти числа в порядке неубывания.</p> 
<p>Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.</p> 
<p>Решение должно иметь сложность <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-1-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-1" class="mjx-math"><span id="MJXc-Node-2" class="mjx-mrow"><span id="MJXc-Node-3" class="mjx-semantics"><span id="MJXc-Node-4" class="mjx-mrow"><span id="MJXc-Node-5" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">O</span></span><span id="MJXc-Node-6" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-7" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span><span id="MJXc-Node-8" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-1"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        O
       </mi>
       <mo stretchy="false">
        (
       </mo>
       <mi>
        n
       </mi>
       <mo stretchy="false">
        )
       </mo>
      </mrow>
      <annotation encoding="application/x-tex">
       O(n)
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>, где <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-2-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-9" class="mjx-math"><span id="MJXc-Node-10" class="mjx-mrow"><span id="MJXc-Node-11" class="mjx-semantics"><span id="MJXc-Node-12" class="mjx-mrow"><span id="MJXc-Node-13" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-2"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        n
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       n
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> - размер списка.</p> 
<p>——</p> 
<p>Вам предстоит разработать набор тестов (только входных данных) для этой задачи, тщательно проверяющий решения участников.</p></div><h2>Формат вывода</h2><div class="output-specification"><p>Сдавать следует не программу, а текстовый файл.</p> 
<p>В первой строке файла запишите число <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-3-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-14" class="mjx-math"><span id="MJXc-Node-15" class="mjx-mrow"><span id="MJXc-Node-16" class="mjx-semantics"><span id="MJXc-Node-17" class="mjx-mrow"><span id="MJXc-Node-18" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.085em;">N</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-3"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        N
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       N
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-4-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-19" class="mjx-math"><span id="MJXc-Node-20" class="mjx-mrow"><span id="MJXc-Node-21" class="mjx-semantics"><span id="MJXc-Node-22" class="mjx-mrow"><span id="MJXc-Node-23" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span><span id="MJXc-Node-24" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-25" class="mjx-mi MJXc-space3"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.085em;">N</span></span><span id="MJXc-Node-26" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-27" class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">20</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-4"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        1
       </mn>
       <mo>
        ≤
       </mo>
       <mi>
        N
       </mi>
       <mo>
        ≤
       </mo>
       <mn>
        20
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le N \le 20
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8193em;vertical-align:-0.136em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">20</span></span></span></span></span>)&nbsp;— количество тестов, которые вы разработали.</p> 
<p>В следующих <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-5-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-28" class="mjx-math"><span id="MJXc-Node-29" class="mjx-mrow"><span id="MJXc-Node-30" class="mjx-semantics"><span id="MJXc-Node-31" class="mjx-mrow"><span id="MJXc-Node-32" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.085em;">N</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-5"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        N
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       N
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> строках запишите по одному тесту. Каждый тест должен состоять из одной строки, в которой записано число <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-6-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-33" class="mjx-math"><span id="MJXc-Node-34" class="mjx-mrow"><span id="MJXc-Node-35" class="mjx-semantics"><span id="MJXc-Node-36" class="mjx-mrow"><span id="MJXc-Node-37" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.04em;">K</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-6"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        K
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       K
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">K</span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-7-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-38" class="mjx-math"><span id="MJXc-Node-39" class="mjx-mrow"><span id="MJXc-Node-40" class="mjx-semantics"><span id="MJXc-Node-41" class="mjx-mrow"><span id="MJXc-Node-42" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span><span id="MJXc-Node-43" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-44" class="mjx-mi MJXc-space3"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.04em;">K</span></span><span id="MJXc-Node-45" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-46" class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">10</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-7"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        2
       </mn>
       <mo>
        ≤
       </mo>
       <mi>
        K
       </mi>
       <mo>
        ≤
       </mo>
       <mn>
        10
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       2 \le K \le 10
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">2</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8193em;vertical-align:-0.136em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">K</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">10</span></span></span></span></span>)&nbsp;— количество чисел в последовательности, а затем <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-8-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-47" class="mjx-math"><span id="MJXc-Node-48" class="mjx-mrow"><span id="MJXc-Node-49" class="mjx-semantics"><span id="MJXc-Node-50" class="mjx-mrow"><span id="MJXc-Node-51" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.04em;">K</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-8"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        K
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       K
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">K</span></span></span></span></span> чисел <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-9-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-52" class="mjx-math"><span id="MJXc-Node-53" class="mjx-mrow"><span id="MJXc-Node-54" class="mjx-semantics"><span id="MJXc-Node-55" class="mjx-mrow"><span id="MJXc-Node-56" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-57" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-58" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-9"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         a
        </mi>
        <mi>
         i
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       a_i
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-10-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-59" class="mjx-math"><span id="MJXc-Node-60" class="mjx-mrow"><span id="MJXc-Node-61" class="mjx-semantics"><span id="MJXc-Node-62" class="mjx-mrow"><span id="MJXc-Node-63" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.301em; padding-bottom: 0.42em;">−</span></span><span id="MJXc-Node-64" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">100</span></span><span id="MJXc-Node-65" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-66" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-67" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-68" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span></span></span><span id="MJXc-Node-69" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-70" class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">100</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-10"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mo>
        −
       </mo>
       <mn>
        100
       </mn>
       <mo>
        ≤
       </mo>
       <msub>
        <mi>
         a
        </mi>
        <mi>
         i
        </mi>
       </msub>
       <mo>
        ≤
       </mo>
       <mn>
        100
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       -100 \le a_i \le 100
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">−</span><span class="mord">100</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.786em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">100</span></span></span></span></span>).</p></div><h2>Примечания</h2><div class="notes"><p>Пример формата файла для сдачи:</p> 
<p>2</p> 
<p>3 1 2 3</p> 
<p>5 -1 1 0 -2 3</p></div></div>