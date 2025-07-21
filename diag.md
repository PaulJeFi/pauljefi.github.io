# Diagonalisation des matrices carrées réelles de rang 1


Soit $n \in \mathbb{N}^*$. On s'intéresse à la diagonalisabilité et diagonalisation des matrices de $\mathcal{M}_{n}(\mathbb{R})$. Dans un premier temps, on cherche à montrer le théorème suivant :

__Théorème :__
    Une matrice $A \in \mathcal{M}_{n}(\mathbb{R})$ est de rang $1$ si et seulement s'il existe $X, Y \in \mathcal{M}_{n, 1}(\mathbb{R})$ tels que $A = XY^\top$.

_Démonstration :_
	$\boxed{\Rightarrow}$ Soit $A \in \mathcal{M}_{n}(\mathbb{R})$ une matrice de rang $1$. On note $c_1, c_2, \dots, c_n$ ses colonnes. Si $A$ est la matrice nulle, le sens direct du théorème est évidemment vrai. On suppose donc que $A$ n'est pas la matrice nulle. Il existe alors $i \in ⟦ 1, n ⟧$ telle que $c_i$ n'est pas la colonne nulle. Il existe donc $\left(\lambda_k\right)_{k \in ⟦ 1, n ⟧} \in \mathbb{R}^{⟦ 1, n ⟧}$ tel que pour tout $k \in ⟦ 1, n ⟧$, $c_k = \lambda_k c_i$. On a alors :
    
    $$\begin{align*}
        A &= [c_1, c_2, \dots , c_n]\\
        &= [\lambda_1 c_i, \lambda_2 c_i, \dots , \lambda_n c_i]\\
        &= c_i \begin{pmatrix}\lambda_1 & \lambda_2 & \dots & \lambda_n \end{pmatrix}\\
        &= \begin{pmatrix}c_{i1} \\ c_{i2} \\ \vdots \\ c_{in} \end{pmatrix} \begin{pmatrix}\lambda_1 & \lambda_2 & \dots & \lambda_n \end{pmatrix}\\
        &= \begin{pmatrix}c_{i1} \\ c_{i2} \\ \vdots \\ c_{in} \end{pmatrix} \begin{pmatrix}\lambda_1 \\ \lambda_2 \\ \vdots \\ \lambda_n \end{pmatrix}^\top\\
        &= XY^\top \qquad \text{en posant}   \quad X = \begin{pmatrix}c_{i1} \\ c_{i2} \\ \vdots \\ c_{in} \end{pmatrix} \quad \text{et} \quad Y = \begin{pmatrix}\lambda_1 \\ \lambda_2 \\ \vdots \\ \lambda_n \end{pmatrix}
    \end{align*}$$
	$\boxed{\Leftarrow}$ Réciproquement, il suffit de remonter le raisonnement ci-dessus pour montrer que si $X, Y \in \mathcal{M}_{n, 1}(\mathbb{R})$, alors $\operatorname{rg}\left(XY^\top\right)=1$.

Bien que ce théorème soit inutile (ou du moins pas le plus rapide) pour traiter notre problème, il est intéressant car permet de montrer avec les théorèmes suivants que le produit scalaire de $\mathcal{M}_{n, 1}(\mathbb{R})$ défini par, pour tout $X, Y \in \mathcal{M}_{n, 1}(\mathbb{R})$, $(X|Y) = \operatorname{Tr}\left(XY^\top\right)$, renvoie l'unique valeur propre non-nulle de $XY^\top$ (le cas $n=1$ est évident).
On s'intéresse réellement au théorème suivant :

__Théorème :__
    Si $n \neq 1$ et que la matrice $A \in \mathcal{M}_{n}(\mathbb{R})$ est de rang $1$, alors $0$ est une valeur propre de $A$ et $\dim(E_0(A)) = n-1$.

_Démonstration :_
    Par le théorème du rang, on a $\dim(\ker(A)) = n - \operatorname{rg}(A) = n-1$.
    Pour que $0$ soit une valeur propre de $A$, il faut qu'il existe $X \in \mathcal{M}_{n,1}(\mathbb{R})$ non-nul tel que $AX = 0X = 0$, autrement dit $X$ doit être un vecteur non-nul de $\ker(A)$. Or comme $\ker(A)$ est de dimension $n-1 > 0$, alors il existe bien un tel $X$ non-nul. $0$ est bien une valeur propre de $A$ et le sous-espace propre associé vérifie $\dim(E_0(A)) = \dim(\ker(A-0 I_n)) = \dim(\ker(A)) = n-1$.

On en déduit alors le théorème ci-après :

__Théorème :__
    Si $n \neq 1$ et que la matrice $A \in \mathcal{M}_{n}(\mathbb{R})$ est de rang $1$, alors $A$ est diagonalisable si et seulement si $m_0(A) = n-1$. Dans ce cas, $\lambda = \operatorname{Tr}(A)$ est l'autre valeur propre de $A$, avec $m_\lambda(A) = 1$.

_Démonstration :_
    $A$ est diagonalisable si et seulement si pour tout $\mu \in \operatorname{Sp}(A)$, $\dim(E_\mu(A)) = m_\mu(A)$. Il faut donc, d'après ce qui précède, $m_0(A) = \dim(E_0(A)) = n-1$ et une autre valeur propre $\lambda \neq 0$ avec $m_\lambda(A) = 1$. On a de plus $\displaystyle \operatorname{Tr}(A) = \sum_{\mu \in \operatorname{Sp}(A)} \mu \times m_\mu(A) = 1\times \lambda + 0(n-1) = \lambda$.

On remarque que si $n=1$, alors $A \in \mathcal{M}_{n}(\mathbb{R})$ est déjà diagonale, et son unique valeur propre est son seul coefficient. On est alors en mesure de diagonaliser de tête des matrices de rang $1$.

_Exemple :_
    Diagonaliser $M = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$.
	$M$ est de rang $1$, et diagonalisable d'après le théorème spectral car symétrique réelle. D'après ce qui précède, on sait que $0$ est valeur propre de $M$ d'ordre de multiplicité $2$ et que son unique autre valeur propre est $\operatorname{Tr}(M) = 3$. Ainsi, $M$ est semblable à la matrice diagonale $D = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$.

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
