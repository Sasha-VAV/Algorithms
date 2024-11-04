<div class="problem__statement text" data-bem="{&quot;problem__statement&quot;:{}}">
<div class="problem-statement"><div class="header"><h1 class="title">A. Префиксные суммы</h1><table><tbody><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></tbody></table></div><h2></h2><div class="legend"><p>По данной последовательности <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-1-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-1" class="mjx-math"><span id="MJXc-Node-2" class="mjx-mrow"><span id="MJXc-Node-3" class="mjx-semantics"><span id="MJXc-Node-4" class="mjx-mrow"><span id="MJXc-Node-5" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-6" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-7" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-8" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-9" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-10" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-11" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-12" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-13" class="mjx-mo MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.361em;">…</span></span><span id="MJXc-Node-14" class="mjx-mo MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-15" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-16" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-17" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-1"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         a
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
         a
        </mi>
        <mn>
         2
        </mn>
       </msub>
       <mo separator="true">
        ,
       </mo>
       <mo>
        …
       </mo>
       <mo separator="true">
        ,
       </mo>
       <msub>
        <mi>
         a
        </mi>
        <mi>
         n
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       a_1, a_2, \ldots, a_n
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="minner">…</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1514em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> вычислите последовательность ее префиксных сумм <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-2-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-18" class="mjx-math"><span id="MJXc-Node-19" class="mjx-mrow"><span id="MJXc-Node-20" class="mjx-semantics"><span id="MJXc-Node-21" class="mjx-mrow"><span id="MJXc-Node-22" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-23" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">b</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-24" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-25" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-26" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-27" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">b</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-28" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-29" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-30" class="mjx-mo MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.361em;">…</span></span><span id="MJXc-Node-31" class="mjx-mo MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-32" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-33" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">b</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-34" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-2"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         b
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
         b
        </mi>
        <mn>
         2
        </mn>
       </msub>
       <mo separator="true">
        ,
       </mo>
       <mo>
        …
       </mo>
       <mo separator="true">
        ,
       </mo>
       <msub>
        <mi>
         b
        </mi>
        <mi>
         n
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       b_1, b_2, \ldots, b_n
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal">b</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">b</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="minner">…</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">b</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1514em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>, где <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-3-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-35" class="mjx-math"><span id="MJXc-Node-36" class="mjx-mrow"><span id="MJXc-Node-37" class="mjx-semantics"><span id="MJXc-Node-38" class="mjx-mrow"><span id="MJXc-Node-39" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-40" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">b</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-41" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.48em;">j</span></span></span></span><span id="MJXc-Node-42" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-43" class="mjx-msubsup MJXc-space3"><span class="mjx-base"><span id="MJXc-Node-44" class="mjx-mo"><span class="mjx-char MJXc-TeX-size1-R" style="padding-top: 0.54em; padding-bottom: 0.54em;">∑</span></span></span><span class="mjx-stack" style="vertical-align: -0.315em;"><span class="mjx-sup" style="font-size: 70.7%; padding-bottom: 0.255em; padding-left: 0px; padding-right: 0.071em;"><span id="MJXc-Node-49" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.48em;">j</span></span></span><span class="mjx-sub" style="font-size: 70.7%; padding-right: 0.071em;"><span id="MJXc-Node-45" class="mjx-mrow" style=""><span id="MJXc-Node-46" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span><span id="MJXc-Node-47" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.063em; padding-bottom: 0.301em;">=</span></span><span id="MJXc-Node-48" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span></span></span><span id="MJXc-Node-50" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-51" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-52" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-3"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         b
        </mi>
        <mi>
         j
        </mi>
       </msub>
       <mo>
        =
       </mo>
       <msubsup>
        <mo>
         ∑
        </mo>
        <mrow>
         <mi>
          i
         </mi>
         <mo>
          =
         </mo>
         <mn>
          1
         </mn>
        </mrow>
        <mi>
         j
        </mi>
       </msubsup>
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
       b_j = \sum\limits_{i=1}^{j} a_i
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.9805em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord mathnormal">b</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:2.5364em;vertical-align:-0.9777em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.5588em;"><span style="top:-2.1223em;margin-left:0em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mrel mtight">=</span><span class="mord mtight">1</span></span></span></span><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span><span class="mop op-symbol small-op">∑</span></span></span><span style="top:-3.9971em;margin-left:0em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight" style="margin-right:0.05724em;">j</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.9777em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>.</p></div><h2>Формат ввода</h2><div class="input-specification"><p>В первой строке дано целое число <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-4-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-53" class="mjx-math"><span id="MJXc-Node-54" class="mjx-mrow"><span id="MJXc-Node-55" class="mjx-semantics"><span id="MJXc-Node-56" class="mjx-mrow"><span id="MJXc-Node-57" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-4"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-5-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-58" class="mjx-math"><span id="MJXc-Node-59" class="mjx-mrow"><span id="MJXc-Node-60" class="mjx-semantics"><span id="MJXc-Node-61" class="mjx-mrow"><span id="MJXc-Node-62" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span><span id="MJXc-Node-63" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-64" class="mjx-mi MJXc-space3"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span><span id="MJXc-Node-65" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-66" class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span><span id="MJXc-Node-67" class="mjx-msup"><span class="mjx-base"><span id="MJXc-Node-68" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">0</span></span></span><span class="mjx-sup" style="font-size: 70.7%; vertical-align: 0.591em; padding-left: 0px; padding-right: 0.071em;"><span id="MJXc-Node-69" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">3</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-5"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
        1
       </mn>
       <msup>
        <mn>
         0
        </mn>
        <mn>
         3
        </mn>
       </msup>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \leq n \leq 10^3
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7719em;vertical-align:-0.136em;"></span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8141em;"></span><span class="mord">1</span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">3</span></span></span></span></span></span></span></span></span></span></span></span>) &nbsp;— количество элементов в последовательности <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-6-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-70" class="mjx-math"><span id="MJXc-Node-71" class="mjx-mrow"><span id="MJXc-Node-72" class="mjx-semantics"><span id="MJXc-Node-73" class="mjx-mrow"><span id="MJXc-Node-74" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-6"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        a
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       a
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">a</span></span></span></span></span>. Во второй строке дано <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-7-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-75" class="mjx-math"><span id="MJXc-Node-76" class="mjx-mrow"><span id="MJXc-Node-77" class="mjx-semantics"><span id="MJXc-Node-78" class="mjx-mrow"><span id="MJXc-Node-79" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-7"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> целых чисел <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-8-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-80" class="mjx-math"><span id="MJXc-Node-81" class="mjx-mrow"><span id="MJXc-Node-82" class="mjx-semantics"><span id="MJXc-Node-83" class="mjx-mrow"><span id="MJXc-Node-84" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-85" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-86" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-87" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-88" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-89" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-90" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-91" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-92" class="mjx-mo MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.361em;">…</span></span><span id="MJXc-Node-93" class="mjx-mo MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-94" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-95" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-96" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-8"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         a
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
         a
        </mi>
        <mn>
         2
        </mn>
       </msub>
       <mo separator="true">
        ,
       </mo>
       <mo>
        …
       </mo>
       <mo separator="true">
        ,
       </mo>
       <msub>
        <mi>
         a
        </mi>
        <mi>
         n
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       a_1, a_2, \ldots, a_n
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="minner">…</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1514em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-9-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-97" class="mjx-math"><span id="MJXc-Node-98" class="mjx-mrow"><span id="MJXc-Node-99" class="mjx-semantics"><span id="MJXc-Node-100" class="mjx-mrow"><span id="MJXc-Node-101" class="mjx-mi"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">∣</span></span><span id="MJXc-Node-102" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-103" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-104" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span></span></span><span id="MJXc-Node-105" class="mjx-mi"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">∣</span></span><span id="MJXc-Node-106" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.48em;">≤</span></span><span id="MJXc-Node-107" class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span><span id="MJXc-Node-108" class="mjx-msup"><span class="mjx-base"><span id="MJXc-Node-109" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">0</span></span></span><span class="mjx-sup" style="font-size: 70.7%; vertical-align: 0.591em; padding-left: 0px; padding-right: 0.071em;"><span id="MJXc-Node-110" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">6</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-9"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi mathvariant="normal">
        ∣
       </mi>
       <msub>
        <mi>
         a
        </mi>
        <mi>
         i
        </mi>
       </msub>
       <mi mathvariant="normal">
        ∣
       </mi>
       <mo>
        ≤
       </mo>
       <mn>
        1
       </mn>
       <msup>
        <mn>
         0
        </mn>
        <mn>
         6
        </mn>
       </msup>
      </mrow>
      <annotation encoding="application/x-tex">
       |a_i| \leq 10^6
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">∣</span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mord">∣</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8141em;"></span><span class="mord">1</span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span></span>) &nbsp;— элементы последовательности.</p></div><h2>Формат вывода</h2><div class="output-specification"><p>Выведите <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-10-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-111" class="mjx-math"><span id="MJXc-Node-112" class="mjx-mrow"><span id="MJXc-Node-113" class="mjx-semantics"><span id="MJXc-Node-114" class="mjx-mrow"><span id="MJXc-Node-115" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-10"><math xmlns="http://www.w3.org/1998/Math/MathML">
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
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> целых чисел <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-11-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-116" class="mjx-math"><span id="MJXc-Node-117" class="mjx-mrow"><span id="MJXc-Node-118" class="mjx-semantics"><span id="MJXc-Node-119" class="mjx-mrow"><span id="MJXc-Node-120" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-121" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">b</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-122" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">1</span></span></span></span><span id="MJXc-Node-123" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-124" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-125" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">b</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-126" class="mjx-mn" style=""><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.361em; padding-bottom: 0.361em;">2</span></span></span></span><span id="MJXc-Node-127" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-128" class="mjx-mo MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.361em;">…</span></span><span id="MJXc-Node-129" class="mjx-mo MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.176em; padding-bottom: 0.54em;">,</span></span><span id="MJXc-Node-130" class="mjx-msub MJXc-space1"><span class="mjx-base"><span id="MJXc-Node-131" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em;">b</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-132" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-11"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         b
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
         b
        </mi>
        <mn>
         2
        </mn>
       </msub>
       <mo separator="true">
        ,
       </mo>
       <mo>
        …
       </mo>
       <mo separator="true">
        ,
       </mo>
       <msub>
        <mi>
         b
        </mi>
        <mi>
         n
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       b_1, b_2, \ldots, b_n
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord"><span class="mord mathnormal">b</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">b</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3011em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="minner">…</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">b</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1514em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> &nbsp;— последовательность префиксных сумм для последовательности <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-12-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-133" class="mjx-math"><span id="MJXc-Node-134" class="mjx-mrow"><span id="MJXc-Node-135" class="mjx-semantics"><span id="MJXc-Node-136" class="mjx-mrow"><span id="MJXc-Node-137" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">a</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-12"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        a
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       a
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">a</span></span></span></span></span>.</p></div><h2>Пример</h2><table class="sample-tests"><thead><tr><th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th><th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th></tr></thead><tbody><tr><td><pre>5
10 -4 5 0 2
</pre></td><td><pre>10 6 11 11 13 
</pre></td></tr></tbody></table></div></div>