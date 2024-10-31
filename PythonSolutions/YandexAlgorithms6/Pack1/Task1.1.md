<div class="problem__statement text" data-bem="{&quot;problem__statement&quot;:{}}">
<div class="problem-statement"><div class="header"><h1 class="title">A. Плот</h1><table><tbody><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></tbody></table></div><h2></h2><div class="legend"><p>НиПосередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов. Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота имеет координаты (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-1-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-1" class="mjx-math"><span id="MJXc-Node-2" class="mjx-mrow"><span id="MJXc-Node-3" class="mjx-semantics"><span id="MJXc-Node-4" class="mjx-mrow"><span id="MJXc-Node-5" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-6" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-7" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-1"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
      </mrow>
      <annotation encoding="application/x-tex">
       x_1
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-2-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-8" class="mjx-math"><span id="MJXc-Node-9" class="mjx-mrow"><span id="MJXc-Node-10" class="mjx-semantics"><span id="MJXc-Node-11" class="mjx-mrow"><span id="MJXc-Node-12" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-13" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-14" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-2"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
      </mrow>
      <annotation encoding="application/x-tex">
       y_1
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>), северо-восточный угол – координаты (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-3-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-15" class="mjx-math"><span id="MJXc-Node-16" class="mjx-mrow"><span id="MJXc-Node-17" class="mjx-semantics"><span id="MJXc-Node-18" class="mjx-mrow"><span id="MJXc-Node-19" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-20" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-21" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-3"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
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
       x_2
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-4-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-22" class="mjx-math"><span id="MJXc-Node-23" class="mjx-mrow"><span id="MJXc-Node-24" class="mjx-semantics"><span id="MJXc-Node-25" class="mjx-mrow"><span id="MJXc-Node-26" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-27" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-28" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-4"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
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
       y_2
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>).</p> 
<p>Пловец находится в точке с координатами (x, y). Определите, к какой стороне плота (северной, южной, западной или восточной) или к какому углу плота (северо-западному, северо-восточному, юго-западному, юго-восточному) пловцу нужно плыть, чтобы как можно скорее добраться до плота.</p> 
<p><img src="/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..6CMsvF2XIVzlRGhv.StYk-67AwM9jvEgmoXMQpzQ3OO7oWopSd9PWbkH9_EV2Ubbqf_gW9VDDNA-whe9Rx3wb00uMgMBGLkaweE8dwVpmi5YvzA.eWmOfrYYfAWEt-Bo29wLKg" alt="image"></p></div><h2>Формат ввода</h2><div class="input-specification"><p>Программа получает на вход шесть чисел в следующем порядке: <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-5-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-29" class="mjx-math"><span id="MJXc-Node-30" class="mjx-mrow"><span id="MJXc-Node-31" class="mjx-semantics"><span id="MJXc-Node-32" class="mjx-mrow"><span id="MJXc-Node-33" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-34" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-35" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-5"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
      </mrow>
      <annotation encoding="application/x-tex">
       x_1
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-6-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-36" class="mjx-math"><span id="MJXc-Node-37" class="mjx-mrow"><span id="MJXc-Node-38" class="mjx-semantics"><span id="MJXc-Node-39" class="mjx-mrow"><span id="MJXc-Node-40" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-41" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-42" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-6"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
      </mrow>
      <annotation encoding="application/x-tex">
       y_1
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> (координаты юго-западного угла плота), <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-7-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-43" class="mjx-math"><span id="MJXc-Node-44" class="mjx-mrow"><span id="MJXc-Node-45" class="mjx-semantics"><span id="MJXc-Node-46" class="mjx-mrow"><span id="MJXc-Node-47" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-48" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-49" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-7"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
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
       x_2
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-8-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-50" class="mjx-math"><span id="MJXc-Node-51" class="mjx-mrow"><span id="MJXc-Node-52" class="mjx-semantics"><span id="MJXc-Node-53" class="mjx-mrow"><span id="MJXc-Node-54" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-55" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-56" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-8"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
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
       y_2
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> (координаты северо-восточного угла плота), <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-9-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-57" class="mjx-math"><span id="MJXc-Node-58" class="mjx-mrow"><span id="MJXc-Node-59" class="mjx-semantics"><span id="MJXc-Node-60" class="mjx-mrow"><span id="MJXc-Node-61" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-9"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        x
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       x
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">x</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-10-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-62" class="mjx-math"><span id="MJXc-Node-63" class="mjx-mrow"><span id="MJXc-Node-64" class="mjx-semantics"><span id="MJXc-Node-65" class="mjx-mrow"><span id="MJXc-Node-66" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-10"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        y
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       y
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">y</span></span></span></span></span> (координаты пловца). Все числа целые и по модулю не превосходят 100. Гарантируется, что <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-11-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-67" class="mjx-math"><span id="MJXc-Node-68" class="mjx-mrow"><span id="MJXc-Node-69" class="mjx-semantics"><span id="MJXc-Node-70" class="mjx-mrow"><span id="MJXc-Node-71" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-72" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-73" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-74" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-75" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-76" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-77" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-11"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
         2
        </mn>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       x_1 &lt; x_2
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-12-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-78" class="mjx-math"><span id="MJXc-Node-79" class="mjx-mrow"><span id="MJXc-Node-80" class="mjx-semantics"><span id="MJXc-Node-81" class="mjx-mrow"><span id="MJXc-Node-82" class="mjx-msub"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-83" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-84" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-85" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.241em; padding-bottom: 0.361em;">&lt;</span></span><span id="MJXc-Node-86" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-87" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-88" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-12"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
         2
        </mn>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       y_1 &lt; y_2
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-13-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-89" class="mjx-math"><span id="MJXc-Node-90" class="mjx-mrow"><span id="MJXc-Node-91" class="mjx-semantics"><span id="MJXc-Node-92" class="mjx-mrow"><span id="MJXc-Node-93" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span><span id="MJXc-Node-94" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.54em;">≠</span></span><span id="MJXc-Node-95" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-96" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-97" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-13"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        x
       </mi>
       <mo mathvariant="normal">
        ≠
       </mo>
       <msub>
        <mi>
         x
        </mi>
        <mn>
         1
        </mn>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       x \ne x_1
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal">x</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span class="mord vbox"><span class="thinbox"><span class="rlap"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="inner"><span class="mord"><span class="mrel"></span></span></span><span class="fix"></span></span></span></span></span><span class="mrel">=</span></span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-14-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-98" class="mjx-math"><span id="MJXc-Node-99" class="mjx-mrow"><span id="MJXc-Node-100" class="mjx-semantics"><span id="MJXc-Node-101" class="mjx-mrow"><span id="MJXc-Node-102" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span><span id="MJXc-Node-103" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.54em;">≠</span></span><span id="MJXc-Node-104" class="mjx-msub MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-105" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">x</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-106" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-14"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        x
       </mi>
       <mo mathvariant="normal">
        ≠
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
       x \ne x_2
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal">x</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span class="mord vbox"><span class="thinbox"><span class="rlap"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="inner"><span class="mord"><span class="mrel"></span></span></span><span class="fix"></span></span></span></span></span><span class="mrel">=</span></span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-15-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-107" class="mjx-math"><span id="MJXc-Node-108" class="mjx-mrow"><span id="MJXc-Node-109" class="mjx-semantics"><span id="MJXc-Node-110" class="mjx-mrow"><span id="MJXc-Node-111" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span><span id="MJXc-Node-112" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.54em;">≠</span></span><span id="MJXc-Node-113" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-114" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-115" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-15"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        y
       </mi>
       <mo mathvariant="normal">
        ≠
       </mo>
       <msub>
        <mi>
         y
        </mi>
        <mn>
         1
        </mn>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       y \ne y_1
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span class="mord vbox"><span class="thinbox"><span class="rlap"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="inner"><span class="mord"><span class="mrel"></span></span></span><span class="fix"></span></span></span></span></span><span class="mrel">=</span></span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-16-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-116" class="mjx-math"><span id="MJXc-Node-117" class="mjx-mrow"><span id="MJXc-Node-118" class="mjx-semantics"><span id="MJXc-Node-119" class="mjx-mrow"><span id="MJXc-Node-120" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span><span id="MJXc-Node-121" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.42em; padding-bottom: 0.54em;">≠</span></span><span id="MJXc-Node-122" class="mjx-msub MJXc-space3"><span class="mjx-base" style="margin-right: -0.006em;"><span id="MJXc-Node-123" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.48em; padding-right: 0.006em;">y</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-124" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-16"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        y
       </mi>
       <mo mathvariant="normal">
        ≠
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
       y \ne y_2
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span class="mord vbox"><span class="thinbox"><span class="rlap"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="inner"><span class="mord"><span class="mrel"></span></span></span><span class="fix"></span></span></span></span></span><span class="mrel">=</span></span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:-0.0359em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, координаты пловца находятся вне плота.</p></div><h2>Формат вывода</h2><div class="output-specification"><p>Если пловцу следует плыть к северной стороне плота, программа должна вывести символ ”N”, к южной&nbsp;— символ ”S”, к западной&nbsp;— символ ”W”, к восточной&nbsp;— символ ”E”. Если пловцу следует плыть к углу плота, нужно вывести одну из следующих строк: ”NW”, ”NE”, ”SW”, ”SE”.</p></div><h2>Пример</h2><table class="sample-tests"><thead><tr><th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem button_js_inited" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th><th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th></tr></thead><tbody><tr><td><pre>-1
-2
5
3
-4
6
</pre></td><td><pre>NW
</pre></td></tr></tbody></table></div></div>