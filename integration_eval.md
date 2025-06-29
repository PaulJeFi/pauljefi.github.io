# Préparation à l'évaluation sur l'intégration
<br><br>
Ces exercices sont majoritairement tirés du livre (il ne doit y avoir que deux énoncés de moi), mais j'ai légèrement changé les énoncés, ou ai regroupé par thème des petits exercices. Certains sont faciles, d'autres moins. Je les ai classé par niveau de difficulté (le nombre d'étoiles). Nous en avons vu certains en cours avec Mme. Sevette, certains pas du tout. L'exercice 9 et la dernière question du dernier exercice sont particulièrement difficiles. Si besoin d'aide sur ce chapitre, ne surtout pas hésiter à me contacter.




<br><br><br><br>
###   <u>Exercice 1 :</u> ＊


Calculer les primitives des fonctions suivantes.

**a)** $\displaystyle f(x) = \frac{\ln(x)}{x}$ définie sur $\mathbb{R}^{+*}$.

**b)** $\displaystyle f(x) = \tan(x)$ définie sur $\displaystyle \left]-\frac{\pi}{2} \; ; \; \frac{\pi}{2}\right[$.

**c)** $\displaystyle f(x) = \frac{\cos(x)}{\sqrt{\sin(x)}}$ définie sur $\displaystyle \left]-0 \; ; \; \pi \right[$.




<br><br><br><br>
###   <u>Exercice 2 :</u> ＊＊＊
En utilisant une double intégration par parties, calculer les intégrales suivantes :

**a)** $\displaystyle \int_{0}^{\frac{\pi}{3}} x^2\sin(x) dx$

**b)** $\displaystyle \int_{0}^{1} x^2 e^{-x} dx$




<br><br><br><br><br>
###   <u>Exercice 3 :</u> ＊

Calculer la valeur moyenne de la fonction $f$ définie sur $[2 \; ; \; e]$ telle que $\displaystyle f(x) = \frac{1}{x\ln(x)}$.




<br><br><br><br>
###   <u>Exercice 4 :</u> ＊＊

Soient $I = \displaystyle \int_{0}^{1}\frac{1}{\sqrt{x^2+2}}dx$, $J = \displaystyle \int_{0}^{1}\frac{x^2}{\sqrt{x^2+2}}dx$ et $K = \displaystyle \int_{0}^{1}\sqrt{x^2+2} \; dx$.

On considère la fonction $f$ définie par $\displaystyle f(x) = \ln\left(x + \sqrt{x^2+2}\right)$.

**1.a)** Justifier que la fonction $f$ est définie sur $[0\; ; \; 1]$.
**b)** Montrer que la fonction $f$ est une primitive de la fonction définie telle que : $\displaystyle x \longmapsto \frac{1}{\sqrt{x^2 + 2}}$.
**c)** Calculer alors $I$.
**2.a)** Calculer $J + 2I$.
**b)** Montrer, en intégrant par parties, que $K = \sqrt{3} - J$.
**c)** En déduire les valeurs de $J$ et de $K$.




<br><br><br><br>
###   <u>Exercice 5 :</u> ＊＊

Soit $(u_n)$ la suite définie pour tout entier naturel $n$ par :
$$u_n = \int_0^1 \frac{x^n}{1+x} dx$$
**1)** Calculer $\displaystyle u_0$.
**2.a)** Démontrer que :
$$\forall n \in \mathbb{N}, \qquad u_{n+1}+u_n = \frac{1}{n+1}$$
**b)** En déduire la valeur de $u_1$.
**3)** Montrer que la suite $(u_n)$ est décroissante.




<br><br><br><br>
###   <u>Exercice 6 :</u> ＊＊

Soient $(I_n)$ et $(J_n)$ les suites définies sur $\mathbb{N}^*$ par :
$$I_n = \int_0^1 \frac{1}{1+x^n} dx \qquad \text{et} \qquad J_n = \int_0^1 \frac{x^n}{1+x^n} dx$$

**1.a)** Montrer que :
$$\forall x \in [0\; ; \; 1], \qquad \frac{1}{1+x^n} \leq 1$$
**b)** en déduire que la suite $(I_n)$ est majorée par $1$.
**2.a)** Montrer que :
$$\forall n \in \mathbb{N}^*, \qquad 0 \leq J_n \leq \frac{1}{n+1}$$
**b)** En déduire la limite de la suite $(J_n)$.
**3.a)** Calculer $I_n + J_n$ pour $n$ dans $\mathbb{N}^*$.
**b)** Déterminer la limite de la suite $(I_n)$.




<br><br><br><br>
###   <u>Exercice 7 :</u> ＊＊＊

Soient $(x_n)$ et $(y_n)$ les suites définies pour tout entier naturel $n$ non nul par :
$$x_n = \int_0^1 t^n \cos(t) dt \qquad \text{et} \qquad y_n = \int_0^1t^n \sin(t) dt$$
**1.a)** Montrer que la suite $(x_y)$ est à termes positifs.
**b)** Étudier le sens de variation de la suite $(x_n)$.
**c)** Montrer que $(x_n)$ converge.
**2.a)** Démontrer que :
$$\forall n \in \mathbb{N}^*, \qquad x_n \leq \frac{1}{n+1}$$
**b)** En déduire la limite de la suite $(x_n)$.
**3.a)** En intégrant par parties, montrer que :
$$\forall n \in \mathbb{N}^*, \qquad x_{n+1} = -(n+1)y_n + \sin(1)$$
**b)** En déduire la limite de la suite $(y_n)$.




<br><br><br><br>
###   <u>Exercice 8 :</u> ＊＊

Soit $f$ la fonction définie sur $\mathbb{R}^{+*}$ par $\displaystyle f(x) = x - \frac{\ln(x)}{x}$. On note $\mathcal{C}$ sa courbe représentative et $(d)$ la droite d'équation $y = x$ dans un repère orthonormé du plan.

**1)** Déterminer la position relative de $\mathcal{C}$ par rapport à $(d)$.
**2)** Soit $\alpha \in ]1 \; ; \; +\infty[$. On désigne par $\mathcal{A}(\alpha)$ l'aire, en unité d'aire, de la partie du plan délimitée par la courbe $\mathcal{C}$, la droite $(d)$ et les droites d'équations $x = 1$ et $x = \alpha$.
**a)** Écrire $\mathcal{A}(\alpha)$ à l'aide d'une intégrale.
**b)** Déterminer  $\displaystyle \lim_{\alpha \rightarrow +\infty}\mathcal{A}(\alpha)$ et interpréter ce résultat.




<br><br><br><br>
###   <u>Exercice 9 :</u> ＊＊＊＊＊

Calculer  $\displaystyle \int_{0}^{\pi} e^x \cos(2x) dx$.




<br><br><br>
###   <u>Exercice 10 :</u> ＊＊＊＊＊

Dans chacun des cas suivants, pour tout entier naturel $n$, exprimer le terme général de la suite $(I_n)$ en fonction de $n$, puis en déduire la limite de la suite $(I_n)$.

**1)** Par primitive :
$$I_n = \int_{e^n}^{e^{n+2}}\frac{\ln(x)}{x}dx$$
**2)** En intégrant par parties :
$$I_n = \int_0^1 (x+2)e^{-nx} dx$$

**3)** En intégrant par parties :
$$I_n = \int_{1}^{e} x^{n-1} \ln(x) dx$$

**4)** Sans indice, sinon ce n'est pas amusant (hardcore celui-ci) :
$$I_n = \int_{0}^{\pi}x^2\cos(nx)dx$$

<!-- Configuration MathJax -->
<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  },
  options: {
    renderActions: {
      findScript: [10, function (doc) {
        for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
          const display = !!node.type.match(/; *mode=display/);
          const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display);
          const text = document.createTextNode('');
          node.parentNode.replaceChild(text, node);
          math.start = { node: text, delim: '', n: 0 };
          math.end = { node: text, delim: '', n: 0 };
          doc.math.push(math);
        }
      }, '']
    }
  }
};
</script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

<!-- (optionnel) Un peu de style pour centrer mieux -->
<style>
mjx-container[display="true"] {
  display: block;
  text-align: center;
  margin: 1em 0;
}
</style>
