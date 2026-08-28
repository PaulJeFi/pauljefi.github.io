
## Premier problème : une famille de polynômes

Soit $n$ un entier naturel. Pour un entier $k$, compris entre $0$ et $n$, la $k$-ième fonction polynomiale de Bernstein est la fonction $B_k^n$ définie, pour tout $x \in [0, 1]$, par :
$$B_k^n(x) = \binom{n}{k}x^k(1-x)^{n-k}$$
1) Monter que, pour tout entier $k$ compris entre $0$ et $n$ et pour tout $x \in [0, 1]$, on a $B_k^n(x) \geq 0$.
2) a) Montrer que, pour tout entier $k$ compris entre $0$ et $n$ et pour tout $x \in [0, 1]$, on a $B_k^n(x) = B_{n-k}^n(1-x)$.
   b) Que peut-on en déduire sur les courbes représentatives des fonctions $B_k^n$ et $B_{n-k}^n$ ?

3) On suppose désormais que $k < n$.  
   a) À l'aide d'une intégration par parties, montrer que 
   $$\int_0^1 x^k (1-x)^{n-k} \, \mathrm{d}x = \frac{n-k}{k+1} \int_0^1 x^{k+1} (1-x)^{n-k-1} \, \mathrm{d}x.$$  
   b) En déduire que, pour tout entier $k$ tel que $0 \leqslant k < n$,
   $$\int_0^1 B_k^n(x) \, \mathrm{d}x = \int_0^1 B_{k+1}^n(x) \, \mathrm{d}x.$$  
   c) En déduire que, pour tout entier $k$ tel que $0 \leqslant k < n$,
   $$\int_0^1 B_k^n(x) \, \mathrm{d}x = \frac{1}{n+1}.$$

4) On suppose que $n$ et $k$ sont distincts et non nuls. Étudier les variations de la fonction $B_k^n$ sur $[0 \,;\, 1]$.

---
## Deuxième problème : étude d'une intégrale logarithmique

On considère la fonction $F$ définie sur $D = ]0,1[ \cup ]1,+\infty[$ par :

$$F(x) = \int_{x}^{x^{2}} \frac{1}{\ln(t)} \, \mathrm{d}t$$
### Partie A - Dérivabilité et variations

1) Justifier que la fonction $t \mapsto \frac{1}{\ln(t)}$ admet des primitives sur $]1,+\infty[$. En déduire que $F$ est dérivable sur $]1,+\infty[$.
2) En effectuant un raisonnement analogue sur $]0,1[$, montrer que $F$ est dérivable sur $D$ et établir que pour tout $x \in D$ :
   $$F'(x) = \frac{x-1}{\ln(x)}$$
3) Déterminer le signe de $F'(x)$ sur $D$ et en déduire le sens de variation de $F$ sur $]0,1[$ et sur $]1,+\infty[$.

### Partie B - Étude au voisinage de 1 (Prolongement par continuité)

1) Soit $x > 1$. En posant le changement de variable $u = \ln(t)$, montrer que :
   $$F(x) = \int_{\ln(x)}^{2\ln(x)} \frac{\mathrm{e}^{u}}{u} \, \mathrm{d}u$$
2) Pour $u \in [\ln(x), 2\ln(x)]$, encadrer $\mathrm{e}^u$ par deux constantes dépendant de $x$.
3) En déduire que pour tout $x > 1$ :
   $$x \ln(2) \le F(x) \le x^{2} \ln(2)$$
4) Montrer qu'un encadrement similaire existe pour $x \in ]0,1[$ :
   $$x^2 \ln(2) \le F(x) \le x \ln(2)$$
5) Déduire de ce qui précède que $F$ admet une limite finie en $1$ que l'on précisera.
6) Montrer que l'on peut prolonger $F$ en une fonction de classe $\mathcal{C}^{1}$ (continue, dérivable et à dérivée continue) sur $[0,+\infty[$ et donner la valeur de $F'(1)$.

### Partie C - Comportement asymptotique en $+\infty$

1) En utilisant les questions 3) et 4) de la partie précédente, calculer $\displaystyle \lim_{x \to 0} F(x)$ et $\displaystyle \lim_{x \to +\infty} F(x)$.
2) Démontrer que pour tout $x > 1$, on a :
   $$\frac{x^{2}-x}{4\ln^2(x)} \le \int_x^{x^2} \frac{1}{\ln^2(t)} \mathrm{d}t\le \frac{x^{2}-x}{\ln^2(x)}$$
3) La notation $\displaystyle F(x) \mathop{\sim}_{x \to +\infty} g(x)$ signifie que $\displaystyle \lim_{x \to +\infty} \frac{F(x)}{g(x)} = 1$. En utilisant une intégration par parties sur $F(x)$, établir l'équivalent asymptotique suivant au voisinage de $+\infty$ :
$$F(x) \mathop{\sim}_{x \to +\infty} \frac{x^{2}}{2\ln(x)}$$
---
## Troisième problème : un calcul de $\zeta(2)$

On définit la fonction Zêta de Riemann pour tout $x \in \mathbb{R}$ par :
$$\zeta (x) = \sum_{n=0}^{+\infty} \frac{1}{n^x}$$
### Partie I : le lemme de Riemann-Lebesgue

On considère deux réels $a$ et $b$ tels que $a < b$, et une fonction $f$, de classe $\mathcal{C}^1$ sur $[a, b]$.

1) Montrer qu'il existe une constante positive $M$ telle que, pour tout réel $t$ de $[a, b]$,
$$\left|f'(t)\right| \le M.$$

2) Que vaut $\displaystyle \lim_{k \to +\infty} \frac{1}{k} \int_a^b f'(t) e^{ikt} \, \mathrm{d}t$ ?

3) À l'aide d'une intégration par parties, montrer que
$$\lim_{k \to +\infty} \int_a^b f(t) e^{ikt} \, \mathrm{d}t = 0.$$
4) En déduire que
$$\lim_{k \to +\infty} \int_a^b f(t) \cos(kt) \, \mathrm{d}t = 0.$$
### Partie II : calcul de $\zeta(2)$

1) a) Pour $n$ dans $\mathbb{N}^*$, calculer :
$$\int_0^\pi t \cos(nt) \, \mathrm{d}t \quad \text{et} \quad \int_0^\pi t^2 \cos(nt) \, \mathrm{d}t.$$

   b) Déterminer deux constantes réelles $a$ et $b$ telles que :
$$\forall n \in \mathbb{N}^*, \quad \int_0^\pi (at^2 + bt) \cos(nt) \, \mathrm{d}t = \frac{1}{n^2}.$$

2) Pour $n$ dans $\mathbb{N}^*$ et $t$ dans $\mathbb{R}$, soit :
$$C_n(t) = \sum_{k=1}^n \cos(kt).$$

Montrer que, pour $n$ dans $\mathbb{N}^*$ et $t$ dans $\mathbb{R}$ non multiple entier de $2\pi$ :
$$C_n(t) = -\frac{1}{2} + \frac{\sin\left(\frac{2n+1}{2}t\right)}{2\sin\left(\frac{t}{2}\right)}.$$

3) Déduire de ce qui précède que
$$\forall n \in \mathbb{N}^*, \quad \sum_{k=1}^n \frac{1}{k^2} = \frac{\pi^2}{6} + \int_0^\pi \varphi(t) \sin\left(\frac{2n+1}{2}t\right) \, \mathrm{d}t$$

où $\varphi$ est une fonction définie et continue sur $[0, \pi]$ que l'on précisera.

4) On admet si nécéssaire que $\varphi$ est dérivable sur $[0, \pi]$ et que sa dérivée est continue. Montrer, en utilisant le lemme de Riemann-Lebesgue, que
$$\zeta(2) = \frac{\pi^2}{6}.$$

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
