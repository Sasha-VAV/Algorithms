<div class="problem__statement text" data-bem="{&quot;problem__statement&quot;:{}}">
<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Город Че</h1>
      <table>
         <tbody><tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </tbody></table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>В центре города Че есть пешеходная улица - одно из самых популярных мест для прогулок жителей города. По этой улице очень
            приятно гулять, ведь вдоль улицы расположено n забавных памятников.
         </p></span><p>Девочке Маше из города Че нравятся два мальчика из ее школы, и она никак не может сделать выбор между ними. Чтобы принять
         окончательное решение, она решила назначить обоим мальчикам свидание в одно и то же время. Маша хочет выбрать два памятника
         на пешеходной улице, около которых мальчики будут ее ждать. При этом она хочет выбрать такие памятники, чтобы мальчики не
         увидели друг друга. Маша знает, что из-за тумана мальчики увидят друг друга только в том случае, если они будут на расстоянии
         не более r метров.
      </p>
      <p>Маше заинтересовалась, а сколько способов есть выбрать два различных памятника для организации свиданий.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке входного файла находятся два целых числа n и r (<span class="tex-math-text">2 ≤ n ≤ 300000</span>, <span class="tex-math-text">1 ≤ r ≤ 10<sup>9</sup></span>) - количество памятников и максимальное расстояние, на котором мальчики могут увидеть друг друга.
         </p></span><p>Во второй строке задано n положительных чисел <span class="tex-math-text">d<sub>1</sub>, …, d<sub>n</sub></span>, где <span class="tex-math-text">d<sub>i</sub></span> - расстояние от i-го памятника до начала улицы. Все памятники находятся на разном расстоянии от начала улицы. Памятники приведены
         в порядке возрастания расстояния от начала улицы (<span class="tex-math-text">1 ≤ d<sub>1</sub>, d<sub>2</sub>, …, d<sub>n</sub> ≤ 10<sup>9</sup></span>).
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите одно число - число способов выбрать два памятника для организации свиданий.</p></span><p></p>
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th>
            <th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem button_js_inited" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>4 4
1 3 5 8
</pre></td>
            <td><pre>2
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>В приведенном примере Маша может выбрать памятники 1 и 4 или памятники 2 и 4.</p></span><p></p>
   </div>
</div></div>