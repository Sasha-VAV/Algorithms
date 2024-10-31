<div class="problem__statement text" data-bem="{&quot;problem__statement&quot;:{}}">
<div class="problem-statement"><div class="header"><h1 class="title">C. Надпись на табло</h1><table><tbody><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></tbody></table></div><h2></h2><div class="legend"><p>Вы получили доступ к одной из камер наблюдения в особо секретной огранизации. В зоне видимости камеры находится табло, с которого вы постоянно считываете информацию. Теперь вам нужно написать программу, которая по состоянию табло определяет, какая буква изображена на нём в данный момент. Табло представляет из себя квадратную таблицу, разбитую на <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-1-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-1" class="mjx-math"><span id="MJXc-Node-2" class="mjx-mrow"><span id="MJXc-Node-3" class="mjx-semantics"><span id="MJXc-Node-4" class="mjx-mrow"><span id="MJXc-Node-5" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span><span id="MJXc-Node-6" class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.182em; padding-bottom: 0.361em;">×</span></span><span id="MJXc-Node-7" class="mjx-mi MJXc-space2"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-1"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        n
       </mi>
       <mo>
        ×
       </mo>
       <mi>
        n
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       n\times n
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6667em;vertical-align:-0.0833em;"></span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> равных квадратных светодиодов. Каждый диод либо включён, либо выключен. Введём систему координат, направив ось <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-2-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-8" class="mjx-math"><span id="MJXc-Node-9" class="mjx-mrow"><span id="MJXc-Node-10" class="mjx-semantics"><span id="MJXc-Node-11" class="mjx-mrow"><span id="MJXc-Node-12" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">O</span></span><span id="MJXc-Node-13" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.024em;">X</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-2"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        O
       </mi>
       <mi>
        X
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       OX
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.07847em;">OX</span></span></span></span></span> вправо, а ось <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-3-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-14" class="mjx-math"><span id="MJXc-Node-15" class="mjx-mrow"><span id="MJXc-Node-16" class="mjx-semantics"><span id="MJXc-Node-17" class="mjx-mrow"><span id="MJXc-Node-18" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">O</span></span><span id="MJXc-Node-19" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.182em;">Y</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-3"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        O
       </mi>
       <mi>
        Y
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       OY
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mord mathnormal" style="margin-right:0.22222em;">Y</span></span></span></span></span>&nbsp;— вверх, приняв сторону диода равной&nbsp;1.</p> 
<p>На табло могут быть изображены только следующие буквы:</p> 
<ul> 
 <li><p><strong>I</strong>&nbsp;— прямоугольник из горящих диодов.</p></li> 
 <li><p><strong>O</strong>&nbsp;— прямоугольник из горящих диодов с углами <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-4-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-20" class="mjx-math"><span id="MJXc-Node-21" class="mjx-mrow"><span id="MJXc-Node-22" class="mjx-semantics"><span id="MJXc-Node-23" class="mjx-mrow"><span id="MJXc-Node-24" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-25" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-26" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-27" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-28" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-29" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-30" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-31" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-32" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-4"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_1, y_1)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-5-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-33" class="mjx-math"><span id="MJXc-Node-34" class="mjx-mrow"><span id="MJXc-Node-35" class="mjx-semantics"><span id="MJXc-Node-36" class="mjx-mrow"><span id="MJXc-Node-37" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-38" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-39" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-40" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-41" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-42" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-43" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-44" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-45" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-5"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_2, y_2)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, внутри которого есть прямоугольник из выключенных диодов с координатами углов <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-6-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-46" class="mjx-math"><span id="MJXc-Node-47" class="mjx-mrow"><span id="MJXc-Node-48" class="mjx-semantics"><span id="MJXc-Node-49" class="mjx-mrow"><span id="MJXc-Node-50" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-51" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-52" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-53" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-54" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-55" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-56" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-57" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-58" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-6"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_3, y_3)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-7-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-59" class="mjx-math"><span id="MJXc-Node-60" class="mjx-mrow"><span id="MJXc-Node-61" class="mjx-semantics"><span id="MJXc-Node-62" class="mjx-mrow"><span id="MJXc-Node-63" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-64" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-65" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-66" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-67" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-68" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-69" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-70" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-71" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-7"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_4, y_4)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>. При этом границы выключенного прямоугольника не должны касаться внешнего, то есть <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-8-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-72" class="mjx-math"><span id="MJXc-Node-73" class="mjx-mrow"><span id="MJXc-Node-74" class="mjx-semantics"><span id="MJXc-Node-75" class="mjx-mrow"><span id="MJXc-Node-76" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-77" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-78" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-79" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-80" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-81" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-82" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-83" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-84" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-85" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-86" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-87" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-88" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-89" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-90" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-8"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         x_1 &lt; x_3 &lt; x_4 &lt; x_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-9-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-91" class="mjx-math"><span id="MJXc-Node-92" class="mjx-mrow"><span id="MJXc-Node-93" class="mjx-semantics"><span id="MJXc-Node-94" class="mjx-mrow"><span id="MJXc-Node-95" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-96" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-97" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-98" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-99" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-100" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-101" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-102" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-103" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-104" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-105" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-106" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-107" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-108" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-109" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-9"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         y_1 &lt; y_3 &lt; y_4 &lt; y_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>.</p></li> 
 <li><p><strong>C</strong>&nbsp;— прямоугольник из горящих диодов с углами <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-10-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-110" class="mjx-math"><span id="MJXc-Node-111" class="mjx-mrow"><span id="MJXc-Node-112" class="mjx-semantics"><span id="MJXc-Node-113" class="mjx-mrow"><span id="MJXc-Node-114" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-115" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-116" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-117" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-118" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-119" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-120" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-121" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-122" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-10"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_1, y_1)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-11-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-123" class="mjx-math"><span id="MJXc-Node-124" class="mjx-mrow"><span id="MJXc-Node-125" class="mjx-semantics"><span id="MJXc-Node-126" class="mjx-mrow"><span id="MJXc-Node-127" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-128" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-129" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-130" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-131" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-132" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-133" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-134" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-135" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-11"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_2, y_2)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, внутри которого есть прямоугольник из выключенных диодов с координатами углов <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-12-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-136" class="mjx-math"><span id="MJXc-Node-137" class="mjx-mrow"><span id="MJXc-Node-138" class="mjx-semantics"><span id="MJXc-Node-139" class="mjx-mrow"><span id="MJXc-Node-140" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-141" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-142" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-143" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-144" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-145" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-146" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-147" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-148" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-12"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_3, y_3)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-13-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-149" class="mjx-math"><span id="MJXc-Node-150" class="mjx-mrow"><span id="MJXc-Node-151" class="mjx-semantics"><span id="MJXc-Node-152" class="mjx-mrow"><span id="MJXc-Node-153" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-154" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-155" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-156" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-157" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-158" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-159" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-160" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-161" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-13"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_4, y_4)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>. При этом правая граница выключенного прямоугольника находится на правой границе внешнего прямоугольника, то есть <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-14-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-162" class="mjx-math"><span id="MJXc-Node-163" class="mjx-mrow"><span id="MJXc-Node-164" class="mjx-semantics"><span id="MJXc-Node-165" class="mjx-mrow"><span id="MJXc-Node-166" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-167" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-168" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-169" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-170" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-171" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-172" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-173" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-174" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-175" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-176" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-177" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-178" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-179" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-180" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-14"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         x_1 &lt; x_3 &lt; x_4 = x_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-15-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-181" class="mjx-math"><span id="MJXc-Node-182" class="mjx-mrow"><span id="MJXc-Node-183" class="mjx-semantics"><span id="MJXc-Node-184" class="mjx-mrow"><span id="MJXc-Node-185" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-186" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-187" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-188" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-189" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-190" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-191" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-192" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-193" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-194" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-195" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-196" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-197" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-198" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-199" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-15"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         y_1 &lt; y_3 &lt; y_4 &lt; y_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>.</p> <p><img src="/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..2LBm51IP4OLpPcS5.4L7a3A5U-_6eH2GxS2CR-iW99-CQMnDdAgLVFHf3NggRxrd2Y6-RddsSbB93iYRjYuPkZ1l9vGBJlAJhus-ha2iBqw.a8v5hf100sx7CHgCHCn87g" alt="image"></p></li> 
 <li><p><strong>L</strong>&nbsp;— прямоугольник из горящих диодов с углами <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-16-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-200" class="mjx-math"><span id="MJXc-Node-201" class="mjx-mrow"><span id="MJXc-Node-202" class="mjx-semantics"><span id="MJXc-Node-203" class="mjx-mrow"><span id="MJXc-Node-204" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-205" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-206" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-207" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-208" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-209" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-210" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-211" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-212" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-16"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_1, y_1)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-17-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-213" class="mjx-math"><span id="MJXc-Node-214" class="mjx-mrow"><span id="MJXc-Node-215" class="mjx-semantics"><span id="MJXc-Node-216" class="mjx-mrow"><span id="MJXc-Node-217" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-218" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-219" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-220" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-221" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-222" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-223" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-224" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-225" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-17"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_2, y_2)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, внутри которого есть прямоугольник из выключенных диодов с координатами углов <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-18-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-226" class="mjx-math"><span id="MJXc-Node-227" class="mjx-mrow"><span id="MJXc-Node-228" class="mjx-semantics"><span id="MJXc-Node-229" class="mjx-mrow"><span id="MJXc-Node-230" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-231" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-232" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-233" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-234" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-235" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-236" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-237" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-238" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-18"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_3, y_3)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-19-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-239" class="mjx-math"><span id="MJXc-Node-240" class="mjx-mrow"><span id="MJXc-Node-241" class="mjx-semantics"><span id="MJXc-Node-242" class="mjx-mrow"><span id="MJXc-Node-243" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-244" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-245" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-246" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-247" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-248" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-249" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-250" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-251" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-19"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_4, y_4)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>. При этом правые верхние углы выключенного прямоугольника и внешнего прямоугольника совпадают, то есть <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-20-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-252" class="mjx-math"><span id="MJXc-Node-253" class="mjx-mrow"><span id="MJXc-Node-254" class="mjx-semantics"><span id="MJXc-Node-255" class="mjx-mrow"><span id="MJXc-Node-256" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-257" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-258" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-259" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-260" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-261" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-262" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-263" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-264" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-265" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-266" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-267" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-268" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-269" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-270" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-20"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         x_1 &lt; x_3 &lt; x_4 = x_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-21-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-271" class="mjx-math"><span id="MJXc-Node-272" class="mjx-mrow"><span id="MJXc-Node-273" class="mjx-semantics"><span id="MJXc-Node-274" class="mjx-mrow"><span id="MJXc-Node-275" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-276" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-277" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-278" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-279" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-280" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-281" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-282" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-283" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-284" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-285" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-286" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-287" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-288" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-289" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-21"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         y_1 &lt; y_3 &lt; y_4 = y_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>.</p></li> 
 <li><p><strong>H</strong>&nbsp;— прямоугольник из горящих диодов с углами <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-22-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-290" class="mjx-math"><span id="MJXc-Node-291" class="mjx-mrow"><span id="MJXc-Node-292" class="mjx-semantics"><span id="MJXc-Node-293" class="mjx-mrow"><span id="MJXc-Node-294" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-295" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-296" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-297" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-298" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-299" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-300" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-301" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-302" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-22"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_1, y_1)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-23-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-303" class="mjx-math"><span id="MJXc-Node-304" class="mjx-mrow"><span id="MJXc-Node-305" class="mjx-semantics"><span id="MJXc-Node-306" class="mjx-mrow"><span id="MJXc-Node-307" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-308" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-309" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-310" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-311" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-312" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-313" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-314" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-315" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-23"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_2, y_2)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, внутри которого находятся 2 прямоугольника из выключенных диодов с координатами углов <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-24-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-316" class="mjx-math"><span id="MJXc-Node-317" class="mjx-mrow"><span id="MJXc-Node-318" class="mjx-semantics"><span id="MJXc-Node-319" class="mjx-mrow"><span id="MJXc-Node-320" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-321" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-322" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-323" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-324" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-325" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-326" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-327" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-328" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-24"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_3, y_3)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-25-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-329" class="mjx-math"><span id="MJXc-Node-330" class="mjx-mrow"><span id="MJXc-Node-331" class="mjx-semantics"><span id="MJXc-Node-332" class="mjx-mrow"><span id="MJXc-Node-333" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-334" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-335" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-336" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-337" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-338" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-339" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-340" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-341" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-25"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_4, y_4)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> у первого и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-26-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-342" class="mjx-math"><span id="MJXc-Node-343" class="mjx-mrow"><span id="MJXc-Node-344" class="mjx-semantics"><span id="MJXc-Node-345" class="mjx-mrow"><span id="MJXc-Node-346" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-347" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-348" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-349" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">5</span></span></span></span><span id="MJXc-Node-350" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-351" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-352" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-353" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">5</span></span></span></span><span id="MJXc-Node-354" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-26"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           5
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           5
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_5, y_5)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-27-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-355" class="mjx-math"><span id="MJXc-Node-356" class="mjx-mrow"><span id="MJXc-Node-357" class="mjx-semantics"><span id="MJXc-Node-358" class="mjx-mrow"><span id="MJXc-Node-359" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-360" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-361" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-362" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span><span id="MJXc-Node-363" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-364" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-365" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-366" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span><span id="MJXc-Node-367" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-27"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           6
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           6
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_6, y_6)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> у второго. При этом выключенные прямоугольники должны иметь одинаковую ширину, находиться строго один под другим, один прямоугольник должен касаться верхней стороны, а другой прямоугольник должен касаться нижней стороны внешнего прямоугольника, то есть <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-28-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-368" class="mjx-math"><span id="MJXc-Node-369" class="mjx-mrow"><span id="MJXc-Node-370" class="mjx-semantics"><span id="MJXc-Node-371" class="mjx-mrow"><span id="MJXc-Node-372" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-373" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-374" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-375" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-376" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-377" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-378" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-379" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-380" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-381" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-382" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">5</span></span></span></span><span id="MJXc-Node-383" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-384" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-385" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-386" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-387" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-388" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-389" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-390" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span><span id="MJXc-Node-391" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-392" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-393" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-394" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-28"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           5
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           6
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         x_1 &lt; x_3 = x_5 &lt; x_4 = x_6 &lt; x_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-29-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-395" class="mjx-math"><span id="MJXc-Node-396" class="mjx-mrow"><span id="MJXc-Node-397" class="mjx-semantics"><span id="MJXc-Node-398" class="mjx-mrow"><span id="MJXc-Node-399" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-400" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-401" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-402" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-403" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-404" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-405" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-406" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-407" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-408" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-409" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-410" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-411" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-412" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-413" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">5</span></span></span></span><span id="MJXc-Node-414" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-415" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-416" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-417" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span><span id="MJXc-Node-418" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-419" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-420" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-421" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-29"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           5
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           6
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         y_1 = y_3 &lt; y_4 &lt; y_5 &lt; y_6 = y_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>.</p> <p><img src="/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..SxEZDE9lB9WB6_0G.zgczM1NRGyz9LVM3OsgeohWQpU5JM7hP2UYROmBYk4TXHRAchIpqsZFw6KGb4lRKaNP_BFcCc6eEweEmdszgBZ5e_g.7hp_w-whdDgQS3z2ACY2Lg" alt="image"></p></li> 
 <li><p><strong>P</strong>&nbsp;— прямоугольник из горящих диодов с углами <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-30-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-422" class="mjx-math"><span id="MJXc-Node-423" class="mjx-mrow"><span id="MJXc-Node-424" class="mjx-semantics"><span id="MJXc-Node-425" class="mjx-mrow"><span id="MJXc-Node-426" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-427" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-428" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-429" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-430" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-431" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-432" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-433" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-434" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-30"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_1, y_1)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-31-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-435" class="mjx-math"><span id="MJXc-Node-436" class="mjx-mrow"><span id="MJXc-Node-437" class="mjx-semantics"><span id="MJXc-Node-438" class="mjx-mrow"><span id="MJXc-Node-439" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-440" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-441" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-442" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-443" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-444" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-445" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-446" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-447" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-31"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_2, y_2)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, внутри которого находятся 2 прямоугольника из выключенных диодов с координатами углов <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-32-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-448" class="mjx-math"><span id="MJXc-Node-449" class="mjx-mrow"><span id="MJXc-Node-450" class="mjx-semantics"><span id="MJXc-Node-451" class="mjx-mrow"><span id="MJXc-Node-452" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-453" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-454" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-455" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-456" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-457" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-458" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-459" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-460" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-32"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_3, y_3)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-33-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-461" class="mjx-math"><span id="MJXc-Node-462" class="mjx-mrow"><span id="MJXc-Node-463" class="mjx-semantics"><span id="MJXc-Node-464" class="mjx-mrow"><span id="MJXc-Node-465" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-466" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-467" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-468" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-469" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-470" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-471" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-472" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-473" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-33"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_4, y_4)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> у первого и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-34-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-474" class="mjx-math"><span id="MJXc-Node-475" class="mjx-mrow"><span id="MJXc-Node-476" class="mjx-semantics"><span id="MJXc-Node-477" class="mjx-mrow"><span id="MJXc-Node-478" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-479" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-480" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-481" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">5</span></span></span></span><span id="MJXc-Node-482" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-483" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-484" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-485" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">5</span></span></span></span><span id="MJXc-Node-486" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-34"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           5
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           5
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_5, y_5)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-35-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-487" class="mjx-math"><span id="MJXc-Node-488" class="mjx-mrow"><span id="MJXc-Node-489" class="mjx-semantics"><span id="MJXc-Node-490" class="mjx-mrow"><span id="MJXc-Node-491" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-492" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-493" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-494" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span><span id="MJXc-Node-495" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-496" class="mjx-msub MJXc-space1"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-497" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-498" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span><span id="MJXc-Node-499" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-35"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mo stretchy="false">
          (
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           6
          </mn>
         </msub>
         <mo separator="true">
          ,
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           6
          </mn>
         </msub>
         <mo stretchy="false">
          )
         </mo>
        </mrow>
        <annotation encoding="application/x-tex">
         (x_6, y_6)
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> у второго. При этом правый нижний угол первого выключенного прямоугольника должен совпадать с правым нижним углом внешнего прямоугольника, а другой выключенный прямоугольник должен находиться строго выше и не касаться границ других прямоугольников, также левые границы двух выключенных прямоугольников должны совпадать, то есть <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-36-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-500" class="mjx-math"><span id="MJXc-Node-501" class="mjx-mrow"><span id="MJXc-Node-502" class="mjx-semantics"><span id="MJXc-Node-503" class="mjx-mrow"><span id="MJXc-Node-504" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-505" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-506" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-507" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-508" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-509" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-510" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-511" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-512" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-513" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-514" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">5</span></span></span></span><span id="MJXc-Node-515" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-516" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-517" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-518" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span><span id="MJXc-Node-519" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-520" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-521" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-522" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-523" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-524" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-525" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-526" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-36"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           5
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           6
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           x
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         x_1 &lt; x_3 = x_5 &lt; x_6 &lt; x_4 = x_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
      <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-37-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-527" class="mjx-math"><span id="MJXc-Node-528" class="mjx-mrow"><span id="MJXc-Node-529" class="mjx-semantics"><span id="MJXc-Node-530" class="mjx-mrow"><span id="MJXc-Node-531" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-532" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-533" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-534" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-535" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-536" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-537" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span><span id="MJXc-Node-538" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-539" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-540" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-541" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.361em;">4</span></span></span></span><span id="MJXc-Node-542" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-543" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-544" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-545" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">5</span></span></span></span><span id="MJXc-Node-546" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-547" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-548" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-549" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span><span id="MJXc-Node-550" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-551" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-552" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-553" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-37"><math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           1
          </mn>
         </msub>
         <mo>
          =
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           3
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           4
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           5
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           6
          </mn>
         </msub>
         <mo>
          &lt;
         </mo>
         <msub>
          <mi>
           y
          </mi>
          <mn>
           2
          </mn>
         </msub>
        </mrow>
        <annotation encoding="application/x-tex">
         y_1 = y_3 &lt; y_4 &lt; y_5 &lt; y_6 &lt; y_2
        </annotation>
       </semantics>
      </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">4</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>.</p> <p><img src="/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..0OD_Kk0JvaCv2tJG.I_RalYY-BI-n-8i6YDlCOccESlAEvptglURQnd5xIYuPA8PZ7bhf88jyWDJwDCWoQVuqG1O6T-RfL2GxgBcds_5BNg.h9Zls8GRIFuVkm1NjETNog" alt="image"></p></li> 
 <li><p>Любое другое состояние табло считается буквой <strong>X</strong>.</p></li> 
</ul> 
<p>По виду табло определите, какая буква на нём изображена.</p></div><h2>Формат ввода</h2><div class="input-specification"><p>В первой строке входных данных находится одно число <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-38-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-554" class="mjx-math"><span id="MJXc-Node-555" class="mjx-mrow"><span id="MJXc-Node-556" class="mjx-semantics"><span id="MJXc-Node-557" class="mjx-mrow"><span id="MJXc-Node-558" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-38"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-39-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-559" class="mjx-math"><span id="MJXc-Node-560" class="mjx-mrow"><span id="MJXc-Node-561" class="mjx-semantics"><span id="MJXc-Node-562" class="mjx-mrow"><span id="MJXc-Node-563" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span><span id="MJXc-Node-564" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-565" class="mjx-mi MJXc-space3"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span><span id="MJXc-Node-566" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-567" class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">10</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-39"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        1
       </mn>
       <mo>
        ≤
       </mo>
       <mi>
        n
       </mi>
       <mo>
        ≤
       </mo>
       <mn>
        10
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le n \le 10
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7719em;vertical-align:-0.136em;"></span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">10</span></span></span></span></span>)&nbsp;— сторона табло.</p> 
<p>В следующих <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-40-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-568" class="mjx-math"><span id="MJXc-Node-569" class="mjx-mrow"><span id="MJXc-Node-570" class="mjx-semantics"><span id="MJXc-Node-571" class="mjx-mrow"><span id="MJXc-Node-572" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-40"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> строках находятся строки длины <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-41-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-573" class="mjx-math"><span id="MJXc-Node-574" class="mjx-mrow"><span id="MJXc-Node-575" class="mjx-semantics"><span id="MJXc-Node-576" class="mjx-mrow"><span id="MJXc-Node-577" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-41"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> из символов «.» и «#»&nbsp;— строки таблицы. «.» обозначает выключенный квадратный диод табло, а «#»&nbsp;— горящий.</p></div><h2>Формат вывода</h2><div class="output-specification"><p>Программа должна вывести единственный символ: если данная таблица подходит под одно из описаний букв <strong>I</strong>, <strong>O</strong>, <strong>C</strong>, <strong>L</strong>, <strong>H</strong>, <strong>P</strong>, то выведите её (все буквы&nbsp;— английские). Если же данная таблица не подходит ни под какие условия, то выведите <strong>X</strong>.</p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th><th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th></tr></thead><tbody><tr><td><pre>4
.##.
.##.
.##.
....
</pre></td><td><pre>I
</pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th><th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th></tr></thead><tbody><tr><td><pre>5
#...#
.#.#.
..#..
.#.#.
#...#
</pre></td><td><pre>X
</pre></td></tr></tbody></table></div></div>