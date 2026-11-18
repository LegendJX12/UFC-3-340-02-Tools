

<!-- batch 26 | page 1 -->

### PROBLEM 4A-9. BRITTLE MODE, POST-FAILURE FRAGMENTS 

### Problem:Design an element, which responds to blast impulse, for controlled post-failure fragments. 

## Procedure:

Step 1.Establish design parameters:

a.Impulse load and duration (Chapter 2).

b.Maximum average velocity of post-failure fragments Vf as required by receiver sensitivity.



C.Geometry of element.

d.Support conditions.

e.Materials to be used and corresponding static design strengths.

f.Dynamic increase factors (Table 4-1 (+)).

Step 2.Determine dynamic yield strength and ultimate strength of reinforcement from Equation 4-3.



Step 3.Determine the dynamic design stress for the flexural reinforcement according to the deflection range (support rotation) from Table 4-2 (+)

Step 4.Substitute known quantities of $j_{b}$ (Step 1a),$f_{d s}$ (Step 3), H (Step 1c), and f (Step 1b) into Equation 4-194.



Step 5.Obtain optimum ratio of vertical to horizontal reinforcement $p_{V}/p_{H}$ ,for a given wall thickess $T_{c}$ .



a.Assume a value of $d_{c}$ and substitute it into the equation obtained in Step 4.



b.Read optimum:$p_{V}/p_{H}$ ratio from Figure 4-38 (+)

Note: For one-way elements, the ratio of the main to secondary reinforcement is always 4 to 1 unless minimum conditions govern (Table 4-3 (+)). Obtain $C_{u}$ from Table 4-11 (+) for the given support condition.$C_{f}$ is always equal to 22,500 (Section 4-58)



Step 6.For the optimum $p_{V}/p_{H}$ ratio, determine $C_{u}$ (from Figure 4-33 (+), 4-34 (+)or $4{\scriptstyle-35(\pm))}$ and $C_{f}$ (from Figure 4-73 (+), 4-74 (+) or 4-75 (+)).Calculate $p_{V}$ and $p_{H}$ . Select bar sizes and spacings necessary to furnish the required reinforcement ratios.



<!-- batch 26 | page 2 -->

Step 7.Determine the required lacing and diagonal bars. (Procedure is exactly the same as that for elements designed for the ductile mode for incipient failure or less. See Problem 4A-3.)



Step 8.Determine the required $T_{c}$ for the assumed $d_{c}$ selected flexural and lacing bar sizes and required concrete cover. Adjust $T_{c}$ to the nearest whole inch and calculate the actual $d_{c}$ 



Check flexural capacity of the element based on either blast impulse of post-failure fragment velocity. Generally, lacing bar sizes do not have to be checked since they are not usually affected by a small change in 1$d_{c}$ .

a.Compute the actual impulse capacity of the element using Equation 4-194 and compare with the anticipated blast load. Repeat design (from Step 5 on) if the capacity is less than that required.

b.Compute the actual post-failure fragment velocity using Equation 4194 and compare with the value permitted by the acceptor sensitivity. Repeat design (from Step 5 on) if the actual velocity is greater than that permitted.



Step 10.Determine whether the correct design procedure has been utilized by first computing the response time of the element $t_{u}$ (time to reach ultimate deflection) from Equation 4-192 or 4-193. Then compare the response time $t_{u}$ with the duration of the blast load $\mathfrak{t}_{\circ},$ .For elements that respond to impulse loading $t_{u}/t_{0}>3$ 



Note: To obtain the most economical design, repeat Steps 5 through 10for several wall thicknesses and compare their costs. Percentages of reinforcement can be used to reduce the amount of calculations. In determining the required quantities of reinforcement, the length of the lap splice should be considered.



<!-- batch 26 | page 3 -->

### EXAMPLE 4A-9. BRITTLE MODE, POST-FAILURE FRAGMENTS 

## Required:Design the back wall of an interior cell (Figure 4A-18 (+)) of a multicubicle structure for controlled post-failure fragments

Solution:

Step 1.Given:

a.$i_{b}=4800\ \mathrm{psi-ms},\ \mathrm{and}\ t_{0}=1.0\ \mathrm{ms}$ 

b.$v_{f}=100\ \mathrm{fs}=1.2\ \mathrm{in/ms}$ 

C.$L=360in,\quad H=120in$ 

d.Fixed on three edges and one edge free 

e.Reinforcing bars;.$f_{V}=66,000$ psi and $f_{u}=90,000\ ps$ i 

Concrete,$f_{c}^{\prime}=4.000$ psi 

f.For reinforcement,$DIF=1.23$ for yield stress 

$DIF=1.05$ for ultimate stress 

<div style="text-align: center;">Figure 4A-18</div>


<div style="text-align: center;"><img src="../pages/batch 26/imgs/img_in_image_box_256_887_964_1089.jpg" alt="Image" width="59%" /></div>


<div style="text-align: center;">PLAN </div>


<div style="text-align: center;">ELEVATION </div>


Step 2.Dynamic strength of materials.

$$\begin{aligned}&f_{dy}=DIFf_{y}=1.23\times66,000=81,180\mathrm{psi}\\ &f_{dy}=DIFf_{y}=1.05\times90,000=94,500\mathrm{psi}\\ \end{aligned}$$

Step 3.Dynamic design stress from Table 4-2 (+)

$$f_{ds}=\frac{f_{dy}+f_{du}}{2}=\frac{81.180+94.500}{2}=87.840\mathrm{psi}$$

<!-- batch 26 | page 4 -->

Step 4.Substitute known quantities into Equation 4-194.

$$\begin{aligned}{{I_{b}}^{2}}&{{}={C_{u}}\left[\frac{{{p_{H}}d_{c}^{3}{f_{d s}}}}{H}\right]+{C_{f}}d_{c}^{2}{v_{f}}^{2}}\\ {4800^{2}}&{{}=\frac{{{C_{u}}{p_{H}}d_{c}^{3}\times87,840}}{{120}}+{C_{f}}d_{c}^{2}\times1.2^{2}}\\ {23.04\times10^{6}}&{{}=732{C_{u}}{p_{H}}d_{c}^{3}+1.44{C_{f}}d_{c}^{2}}\end{aligned}$$

Step 5.Optimum reinforcement ratio.

a.Assume $d_{c}=21$ in and substitute into Equation 4-194.

$$23.04\times10^{6}=732C_{u}p_{H}(21)^{3}+1.44C_{f}(21)^{2}$$

Therefore:

$$p_{H}=\frac{23.04\times10^{6}-635\times C_{f}}{6.78\times10^{6}\times C_{u}}$$

b.Read optimum $p_{V}/p_{H}$ value from Figure 4-38 (+) for $L/H=3$ 

$$p_{V}/p_{H}=1.58$$

Step 6.For optimum $p_{V}/p_{H}=1.58$ 

From Figure 4-34 (+),$C_{u}=477$ 

From Figure 4-74 (+),$C_{f}=1.84\times10^{4}$ 

$$\begin{aligned}\boldsymbol{p}_{H}&=\frac{23.04\times10^{6}-635\times1.84\times10^{4}}{6.78\times10^{6}\times477}=0.00351\\\boldsymbol{p}_{V}&=1.58\boldsymbol{p}_{H}=1.58\times0.00351=0.00555\\\boldsymbol{A}_{stH}&=0.00555\times12\times21=1.398\ln^{2}/\mathrm{ft}\\&\quad\text{use}\#8\textcircled{o}6\text{in.}(\boldsymbol{A}_{s}=1.58\ln^{2})\\\boldsymbol{A}_{sv}&=0.00877\times12\times21=2.21\ln^{2}/\mathrm{ft}\\&\quad\text{use}\#10\textcircled{o}6\text{in.}(\boldsymbol{A}_{s}=2.54\ln^{2})\\\boldsymbol{A}&\text{ctuual}\frac{\boldsymbol{p}_{V}}{\boldsymbol{p}_{H}}=\frac{\boldsymbol{A}_{sV}}{\boldsymbol{A}_{stH}}=\frac{2.54}{1.58}=1.610\end{aligned}$$

Step 7.Using lacing method No. 3, No. 7 vertical lacing bars are required.(Calculations are not shown since they are similar to those presented in 

<!-- batch 26 | page 5 -->

example 4A-3 for incipient failure design. Also, the remainder of the design for shear will not be shown.)



Step 8.The actual $d_{c}$ depends upon the details of the base of the wall (region of vertical lacing).



$$\begin{array}{l}\text{Figure4A-19}\\\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text\text{}\text{}\text{}\text{}\text{}\text{}\text{}\text\text{}\text{}\text{}\text{}\text{}\text\text{}\text{}\text{}\text{}\text\text{}\text{}\text{}\text\text{}\text{}\text{}\text\text{}\text{}\text{}\text\text{}\text{}\text\text{{}\text}\text\text{{}\text}\text\text{{}\text}\text\text{{}\text}\text\text{{}\text\text}\text{{{}\text\text}\text\text{{}\text\text}\text\text{{{}\text\text}\text\text{ $$

$T_{c}=d_{c}+6.52=27.52$ in, use 28 in 

actual $d_{c}=28-6.52=21.48\ in$ 

Step 9.Actual capacity of element 

a.Actual impulse capacity 

$$\begin{aligned}&For p_{V}/p_{H}=1.610,\quad C_{u}=481\\&and\quad C_{f}=1.855\times10^{4}\\&d_{c}=21.48in\\&p_{H}=1.05/(12\times21.48)=0.00407\\ \end{aligned}$$

$$\begin{aligned}{i_{c}^{\quad2}}&{{}={\cal C}_{u}\left[\frac{p_{_{H}}d_{_{c}}^{\quad3}f_{_{d s}}}{H}\right]+{\cal C}_{r}d_{_{c}}^{\quad2}v_{_{r}}^{\quad2}}\\ {}&{{}=48\left[\frac{0.00407\times21.48^{3}\times87,840}{120}\right]+1.855\times10^{4}\times21.48^{2}\times1.2^{2}}\\ {}&{{}=26.752\times10^{6}}\\ {i_{c}}&{{}=5150\mathrm{p s i-m s}>i_{b}=4,800\mathrm{p s i-m s}\qquad\mathrm{O.K.}}\end{aligned}$$

<!-- batch 26 | page 6 -->

b.Actual post-failure fragment velocity 

$$\begin{aligned}i_{b}^{2}&=C_{u}\left[\frac{p_{H}d_{c}^{3}f_{ds}}{H}\right]+C_{r}d_{c}^{2}v_{f}^{2}\\4,&800^{2}=481\times\frac{0.00407\times21.48^{3}\times87,840}{120}+1.855\times10^{4}\times21.48^{2}\times v_{f}^{2}\\v_{f}&=1.10in/ms=92fps<100fps\quad O.K.\end{aligned}$$

Step 10.Response time of element $t_{u};$ ,

$$\begin{aligned}M_{VN2}&=M_{VP}and M_{HN1}=M_{HN1}=M_{HN3}=M_{HP}\\M_{HP}&=A_{sH}f_{ds}(d_c/b)=\frac{1.05\times87.840\times21.48}{12}\\&=165,095in-lbs/in\\M_{VP}&=A_{sv}f_{ds}d_c/b=\frac{1.69\times87.840\times21.48}{12}\\&=265,725in-lbs/in\end{aligned}$$

$$x_{2}/x_{1}=1.0(symmetric-field lines)$$

$$\begin{aligned}&\frac{L}{H}\left[\frac{M_{VP}}{M_{HN1}+M_{HP}}\right]^{1/2}=\frac{360}{120}\left[\frac{26.725}{2\times165.095}\right]^{1/2}=2.69\\ &\frac{M_{VP}}{M_{VN2}}=\frac{265.725}{265.725}=1.0\\ \end{aligned}$$

From Figure 3-11 (+),

$$\begin{aligned}&x_{1}/L=0.358\\&x_{1}=x_{2}=0.358(360)=128.88\\&r_{u}=\frac{5(M_{HN1}+M_{HP})}{{X_{1}}^{2}}for x_{1}<L/2\\&r_{u}=\frac{5(2×165,095)}{120}=99.4psi\\&m=225d_{c}=225(21.48)=4833psi-ms^2/min^2\\&r_{LM})_{u}=0.557\\&m_{u}=0.557(4833)=2692psi-ms^2/in\\&x_{1}=128.88>H=120\\ \end{aligned}$$

<!-- batch 26 | page 7 -->

Therefore, vertical supports fail first and the post-ultimate range resistance is:

$$\begin{aligned}&r_{up}=\frac{8(M_{HN1}+M_{HP})}{L^2}=\frac{8(2\times165,095)}{360^2}=20.4\mathrm{psi}\\ &m_{up}=0.66\times4833=3,190\mathrm{psi}-\mathrm{ms}^2/\mathrm{in}\\ &X_1=H\tan\theta_{\max}=12\times\tan12^\circ=25.51\mathrm{in}\\ \end{aligned}$$

Use Equation 4-192 for $t_{u}$ ,

$$\begin{aligned}t_{u}&=\frac{i_{b}}{m_{u}}+\left[\frac{m_{up}}{m_{u}r_{up}}-\frac{1}{r_{u}}\right]\left[i_{b}^{2}-2m_{u}r_{u}X_{1}\right]^{1/2}-\left[\frac{m_{u}}{r_{up}}\right]V_{t}\\t_{u}&=\frac{4.800}{2.692}+\left[\frac{3190}{2692\times20.4}-\frac{1}{99.4}\right]\left[4800^{2}-2\times2692\times99.4\times25.51\right]^{1/2}\\&-\left(\frac{2692}{20.4}\right)1.1=3.78ms\end{aligned}$$

$\frac{t_{u}}{t_{o}}=\frac{3.78}{1.0}=3.78>3$ , Therefore, correct procedure has been used 

<!-- batch 26 | page 8 -->

### PROBLEM 4A-10. MAXIMUM FRAGMENT PENETRATION 

## Problem:Determine the maximum penetration of a primary metal fragment into a concrete wall and determine if perforation occurs

## Procedure:

Step 1.Establish design parameters:

a.Type of fragment 

b.Weight Wf and diameter d of fragment 

C.Fragment striking velocity $v_{s}$ 

d.Thickness $T_{c}$ and the ultimate compressive strength $f_{c}$ of concrete wall 



Step 2.Determine the maximum penetration $X_{t}$ from Figure 4-78 (+) (or Equation 4-200 or 4-201) for the values of Wf and $v_{s}$ in Step 1. Xf is the maximum penetration of an armor-piercing steel fragment into 4,000 psi concrete.

Step 3.To determine the depth of penetration into concrete with ultimate srength other than 4,000 psi use $X_{t}$ from Step 2, the concrete strength from Step 1d and Equation 4-202:

$$X_{f}^{\prime}=X_{f}(4000/f_{c})^{1/2}$$

Step 4.To obtain the maximum penetration into concrete by metal fragments other than those of armor-piercing fragments use the penetration from Step 3, the penetrability coefficient k from Table 4-16 (+) and Equation 4203.



$$X_{f}^{\prime}=k X_{f}$$

Step 5.Calculate the limiting thickness of concrete at which perforation will occur from Equation 4-204.



$$T_{p f}=1.13\times d^{0.1}+1.311d $$

Where applicable, replace $X_{t}$ with $X_{t}$ from Step 3 or 4. If $T_{p f}$ is less than $T_{0}$ embedment will occur; if $T_{p f}$ is greater than $T_{c}$ the fragment will perforate the wall.



<!-- batch 26 | page 9 -->

### EXAMPLE 4A-10. MAXIMUM FRAGMENT PENETRATION 

Required:Maximum penetration of a primary fragment into a concrete wall;determine if perforation occurs.



Solution:

Step 1.Given:

a.Type of fragment: mild steel 

b.Primary fragment weight:$W_{f}=30ounces$ 

Primary fragment diameter:$d=2.15inche=$ 

C.Striking velocity:$v_{s}=3.500$ fps 

d.Thickness of wall:$T_{c}=18$ inches 

Ultimate concrete compressive strength:$f_{c}^{\prime}=4,000\mathrm{p s i}$ 

Step 2.Maximum penetration:

For:

$$\begin{aligned}&W_{f}=30\mathrm{~oz~and~}v_{s}=3,500\mathrm{~fps}\\&X_{f}=14.5\mathrm{~inches~from~Figure~4-78~(+)}\\ \end{aligned}$$

or from Equation 4-199

$$X_{f}=2.04\times10^{-6}d^{1.2}vs^{1.8}+d\geq2d $$

$$X_{f}>2d=2\times2.15=4.30\ 0.K.$$

Step 3.Concrete strength adjustment 

(Equation 4-202)

$$\begin{aligned}&X_{f}^{\prime}=X_{f}\left(4000/f_{c}^{\prime}\right)^{1/2}\\ &\quad=14.5\times1=14.5\text{in}\\ \end{aligned}$$

Step 4.Fragment material adjustment:

a.

$$k=0.70$$

b.

$$X_{f}^{\prime}=k X_{f}$$

$$0.7\times14.5=10.15in $$

<!-- batch 26 | page 10 -->

Step 5.Calculate minimum thickness to prevent perforation.

$$\begin{aligned}{T_{p f}}&{{}=1.13\;X_{f}^{\prime}d^{0.1}+1.311\;d}\\ {}&{{}=1.13\;(10.15)\;(2.15)^{0.1}+1.311\;(2.15)}\end{aligned}$$

$$T_{pf}=15.20in\leq18in $$

Since $T_{p f}$ is less than $T_{c}$ the fragment does not perforate the slab.

<!-- batch 26 | page 11 -->

# PROBLEM 4A-11. DETERMINATION OF THE OCCURRENCE AND EFFECTS OF  PERFORATION 

### Problem:Determine the residual velocity of a primary fragment if it perforates a concrete wall. 

## Procedure:

Step 1.Determine the type, weight $W_{f},$ and striking velocity $v_{s}$ of the primary fragment. Also, the thickness of the concrete wall $T_{c}$ and the ultimate compressive stress $f_{c}$ of the concrete must be known.

Step 2.Proceed through Steps 2, 3, 4, and 5 of Problem 4A-10.If $T_{p f}$ is greater than $T_{c},$ perforation will occur.



Step 3.If perforation is not indicated by the calculations in Step 2 then discontinue the analysis. lf perforation does result, then compute the value of $T_{o}/T_{p f}$ 

Step 4.Utilizing the value of $T_{c}/T_{p f,}$ 。,obtain $v_{r}/v_{s}$ from Figure 4-79 (+) or 4-80 (+)

Step 5.With the values of $v_{s}$ and $v_{r}/v_{s}$ of Steps 1 and 4, calculate the residual velocity $v_{r}$ .



<!-- batch 26 | page 12 -->

# EXAMPLE 4A-11. DETERMINATION OF THE OCCURRENCE AND EFFECTS OF  PERFORATION 

Required:Residual velocity of a primary fragment if it perforates a concrete wall.Solution:

Step 1.Given:

a.Type of metal: mild steel 

b.Primary fragment weight:$W_{f}=20\text{ounces}$ 

C.Primary fragment diameter:$d=1.89inchees$ 

d.Striking velocity:$v_{s}=4.700$ fps 

e.Thickness of wall:$T_{c}=12$ inches 

f.Ultimate concrete compressive stress:$f_{c}^{\prime}=4.500\mathrm{p s}$ 

Step 2.For given conditions:

$$X_{f}=19.75inchees $$

Actual maximum penetration:

$$\begin{aligned}&X_{f}^{\prime}=19.75\left(4000/4500\right)^{1/2}\\ &\quad\quad=18.6\ i n c h e s\\ &\quad\quad\quad k=0.70\\ &\quad\quad X_{f}^{\prime}=0.7\left(18.6\right)=13.0\ i n c h e s\\ \end{aligned}$$

Since $T_{p f}$ is greater than $X_{f}^{r}$ , and $X_{t}^{r}$ (13.0 inches) already exceeds the wall thickness (12 inches), perforation will occur. It is necessary to determine $T_{p f}$ (Equation 4-204) in order to calculate the residual fragment velocity.Hence:

$$T_{pf}=1.13(13.0)(1.89)^{0.1}+1.311(1.89)$$

Step 3

$$T_{c}/T_{p f}=12.0/18.1=0.663$$

Step 4.

Since the given conditions correspond to a case 

where:

$$X_{f}>2d,$$

<!-- batch 26 | page 13 -->

Step 5.

determine:

$$v_{P}/v_{s}$$

for:$T_{c}/T_{p f}=0.663\mathrm{f r o m}\mathrm{F i g u r e}4-80(\pm).$ 

Obtain:

$$v_{d}/v_{s}=0.55$$

$$v_{r}=0.55\ v_{s}=0.55\ (4,700)=2,585\ \mathrm{fps}$$

UFC 3-340-025 December 2008Change 2, 1 September 2014

<!-- batch 26 | page 14 -->

### PROBLEM 4A-12. DETERMINATION OF THE OCCURRENCE OF SPALLING 

### Problem:To determine if spalling of a concrete wall occurs if there is no perforation by the primary fragment. 

## Procedure:

Step 1.Determine the type, weight $W_{f}$ and striking velocity $v_{s}$ of the primary fragment. Also, the thickness of the concrete wall and the ultimate compressive stress of the concrete $f_{c}$ must be known.

Step 2.Proceed through Steps 2, 3, 4, and 5 of Problem $4A{-}10$ 

Step 3.If embedment of the fragment occurs, compute the limiting concrete thickness at which spalling will occur according to:

$$T_{s o}=1.215X_{f}d^{0.1}+2.12d 一
$$

If $T_{s p}$ is greater than $T_{c},$  spalling will occur.

<!-- batch 26 | page 15 -->

### EXAMPLE 4A-12. DETERMINATION OF THE OCCURRENCE OF SPALLING 

### Required:Determine if spalling of a concrete wall occurs due to penetration by a primary fragment. 

Solution:

Step 1.Given:

a.Type of metal: armor-piercing steel 

b.Primary fragment weight:$W_{f}=40\text{ounces}$ 

C.Primary fragment diameter: 2.38 inches 

d.Striking velocity:$v_{s}=3{,}000\;\mathrm{f p s}$ 

e.Thickness of wall:$T_{c}=19$ inches 

f.Ultimate concrete compressive stress:$f_{c}^{\prime}=5,000\mathrm{p s}$ 

Step 2.For given conditions:

$$\begin{aligned}&X_{f}=12.8inche\\&X_{f}^{\prime}=12.8(4000/5000)^{2}\\&\quad=11.5in\\&k=1.00\\&X_{f}^{\prime}=X_{f}\\ \end{aligned}$$

Then:

$$\begin{aligned}&T_{pf}=1.13(11.5)(2.38)^{0.1}\\ &\quad+1.311(2.38)\\ &\quad=14.2+3.1=17.3inche\\ \end{aligned}$$

Since $T_{c}$ is greater than 17.3 inches, embedment occurs.

Step 3.Determine minimum concrete thickness to prevent spalling from Equation 4-207:

$$\begin{aligned}T_{sp}&=1.215(11.5)(2.38)^{0.1}+2.12(2.38)\\&=20.3inches\end{aligned}$$

Since $T_{s p}$ is greater than 19 inches, spalling will occur.

<!-- batch 26 | page 16 -->

# PROBLEM 4A-13. DETERMINATION OF THE EFFECTS OF A PRIMARY  FRAGMENT ON A COMPOSITE WALL 

Problem:Determine the maximum penetration by a primary fragment into a composite wall and the resulting effects on the donor panel, sand layer and acceptor panel.



## Procedure:

Step 1.Determine the type, weight $W_{f},$ and striking velocity $v_{s}$  of the primary fragment.$\mathsf{A l s o}$ ,the thicknesses of the concrete donor panel $T_{c}$ (donor),the sand layer $T_{s},$ and the concrete receiver panel $T_{c}$ (acceptor) and the ultimate compressive stress $f_{c}$ of the concrete must be known.

Step 2.Proceed through Steps 2, 3, 4, and 5 of Problem 4A-10.

If embedment of the fragment in the donor panel occurs, perform Step 3 of Problem 4A-12 to determine if spalling takes place.



If perforation of the donor panel occurs, compute:

$T_{c}$ (donor)$/T_{p f}$ 

and perform Steps 4 and 5 of Problem 4A-11 to find the residual velocity 

$v_{r}$ 



Step 3.Utilizing $v_{r}(\mathsf{d o n o r})$ as the $v_{s}$ of the sand layer and $W_{f},$ obtain $X_{s}$ from Figure 4-81 (+).



If $X_{s}$ is less than $T_{s}$ , the fragment is embedded in the sand layer and the analysis is discontinued.



If $X_{s}$ is greater than $T_{s},$ perforation of the sand occurs.

Step 4.Compute $T_{s}/X_{s}$ if perforation results. Use this value and Figure $4-80(\pm)$ to obtain $v_{r}/v_{s}$ of the sand layer.



Calculate v,(sand).

Step 5.Utilizing v,(sand) as the $v_{s}$ of the acceptor wall and $W_{f},$ obtain $X_{t}$ (acceptor) from Figure 4-78 (+).



Proceed through Steps 3 and 4 of Problem 4A-10, if necessary.

If embedment of the fragment in the acceptor panel occurs, perform Step 3 of Problem 4A-12 to determine if spalling takes place.

If perforation of the acceptor wall occurs, compute $T_{c}$ (acceptor) and perform Steps 4 and 5 of Problem 4A-11 to find $v_{r}$ 

<!-- batch 26 | page 17 -->

# EXAMPLE 4A-13. DETERMINATION OF THE EFFECTS OF A PRIMARY  FRAGMENT ON A COMPOSITE WALL 

Required:Maximum penetration by a primary fragment into a composite wall and the resulting effects on the donor panel, sand layer and the acceptor panel.



Solution:

Step 1.Given:

a.Type of metal: armor-piercing steel 

b.Primary fragment weight:$W_{f}=20ounces$ 0

C.Primary fragment diameter:$d=1.89inchees$ 

d.Striking velocity:$v_{s}=4,200$ fps 

e.Thicknesses:

$$T_{c}(donor)=12inches $$

$$T_{s}=24inchees $$

$$T_{c}(acceptor)=12inthese $$

f.Ultimate concrete compressive stress:

$$f_{c}^{\prime}=5,000\mathrm{p s i}$$

Step 2.For given condittions:

$$\begin{aligned}&X_{f}=16.5inches\\&X_{f}^{\prime}=16.5(4000/5000)^{2}\\&\quad=14.7inches\\&k=1.00\\&X_{f}^{\prime}=X_{f}\\ \end{aligned}$$

Since $X_{t}^{r}$ is greater than 12 inches, perforation of the donor panel wil certainly occur.$T_{p f}$ must be calculated in order to determine the residual velocity of the fragment.



$$\begin{aligned}&T_{pf}=1.13(14.7)(1.89)^{0.1}+1.311(1.89)\\ &\quad=17.7+2.5=20.2inche\\&T_{c}/T_{pf}=12/20.2=0.594\\ \end{aligned}$$

<!-- batch 26 | page 18 -->

Since $\mathsf{X}_{\mathsf{p f}}$ is greater than 2d,$v_{r}/v_{s}=0.61$ from Figure 4-80 (+).

$$v_{r}(donor)=0.61(4,200)=2.562\mathrm{~fs}$$

Step 3.For:

$$\begin{aligned}&v_{s}(\mathrm{sand})=2,562\mathrm{fs},\\&X_{s}=64.0\mathrm{inches}\\ \end{aligned}$$

Since $T_{s}$ is less than 64.0 inches, perforation of the sand layer will occur.

Step 4.

$$T_{s}/X_{s}=24/64.0=0.375$$

from Figure 4-80 (+)

Step 5.

$$v_{r}/v_{s}=0.77\quad v_{r}(\mathrm{s}\mathrm{and})=0.77\quad v_{s}\quad v_{r}=0.77\quad(2,562)=1,970\quad\mathrm{fps}$$

Step 6.For:

$$\begin{aligned}&V_{s}\left(acceptor\right)=1,970\ fps\\&X_{f}\left(acceptor\right)=5.6\ inches\\&X_{f}^{\prime}=5.6\ (4000/5000)^{1/2}\\&\quad=5.0\ inches\\&k=1.00\\&X_{f}^{\prime}=X_{f}\\&T_{pf}=1.13\ (5.0)\ (1.89)^{0.1}\\&\quad+1.311\ (1.89)\\&\quad=6.0+2.5=8.5\ inches\\ \end{aligned} S $$

Since $T_{p f}$ is less than $T_{c}$ (acceptor), the fragment is embedded in the receiver panel. Calculate $T_{s p}$ to determine if spalling occurs:

$$\begin{aligned}&T_{sp}=1.215(5.0)(1.89)^{0.1}\\ &\quad+2.12(1.89)\\ &\quad=6.5+4.0=10.5inche\\ \end{aligned}$$

Since $T_{s p}$ is less than $T_{c}$ (acceptor), spalling will not occur.

<!-- batch 26 | page 19 -->

## APPENDIX 4B LIST OF SYMBOLS 

a (1) acceleration (in/ms2)

(2) depth of equivalent rectangular stress block (in)

(3) long span of a panel (in)

$a_{0}$ velocity of sold in air (ft/sec)

${\pmb a}_{x}$ acceleration in x direction (in/ms2)

${\pmb a}_{y}$ acceleration in y direction $(\mathsf{i n}/\mathsf{m s}^{2})$ 1

A (1) area $({\mathsf{i n}}^{2})$ 

(2) explosive composition factor $(\mathsf{o z}^{1/2}\mathsf{i n}^{-3/2})$ 

$A_{a}$ area of diagonal bars at the support within a width b (in2)

$A_{b}$ area of reinforcing bar (in2)

$A_{d}$ (1) door area (in2)

(2) area of diagonal bars at the support within a width b $({\mathsf{i n}}^{2})$ 

$A_{D}$ drag area (in2)

$A_{f}$ net area of wall excluding openings (ft2)

$A_{g}$ area of gross section (in2)

$A_{H}$ maximum horizontal acceleration of the ground surface (g's)

$A_{L}$ area of longitudinal torsion reinforcement (in2)

$A_{L}$ lift area (in2)

$A_{n}$ (1) net area of section (in2)

(2) area of individual wall subdivision (ft2)

$A_{o}$ area of openings (ft2)

$A_{p s}$ area of prestressed reinforcement (in2)

$A_{s}$ area of tension reinforcement within a width b (in2)

$A_{s}^{\prime}$ area of compression reinforcement within a width b (in2)

$A_{s}$ area of rebound reinforcement (in2)

$A_{s H}$ area of flexural reinforcement within a width b in the horizontal direction on 

each face $({\mathsf{i n}}^{2})^{\mathsf{^{\ast}}}$ 



<!-- batch 26 | page 20 -->

$A_{s p}$ area of spiral reinforcement $({\mathsf{i n}}^{2})$ 

$A_{s t}$ total area of reinforcing steel $({\mathsf{i n}}^{2})$ 

$A_{s V}$ area of flexural reinforcement within a width b in the vertical direction on each 

face $({\mathsf{i n}}^{2})^{1}$ 

$A_{t}$ area of one leg of a closed tie resisting torsion within a distance $s\;({\mathsf{i n}}^{2})$ 

$\mathsf{A}_{\mathsf{V}}$ total area of stirrups or lacing reinforcement in tension within a distance,c $s_{s}$ or 

S, and a width $\mathsf{b}_{\mathsf{s}}$ or $b_{l}$ (in2)

$A_{V}$ maximum vertical acceleration of the ground surface (g's)

$A_{w}$ area of wall $(\mathsf{f t}^{2})$ 

$A_{I},A_{I I}$ area of sector I and Ill, respectively $({\mathsf{i n}}^{2})$ 

b (1) width of compression face of flexural member (in)

(2) width of concrete strip in which the direct shear stresses at the supports 

are resisted by diagonal bars (in)

(3) short span of a panel (in)

$b_{f}$ width of fragment (in)

$b_{s}$ width of concrete strip in which the diagonal tension stresses are resisted by 

stirrups of area $A_{v}$ (in)

$b_{I}$ width of concrete strip in which the diagonal tension stresses are resisted by 

lacing of area $A_{v}$ (in)

$b_{o}$ failure perimeter for punching shear (in)

$b_{t}$ center-to-center dimension of a closed rectangular tie along b (in)

B explosive constant defined in Table $2-7\;\underline{{{(+)}}}\;(\mathsf{o z}^{1/2}\mathsf{i n}^{7/6})$ 

C (1) distance from the resultant applied load to the axis of rotation (in)

(2) damping coefficient 

(3) width of column capital (in)

$c_{I}$ $c_{I I}$ distance from the resultant applied load to the axis of rotation for sectors I and 

II, respectively (in)

$c_{s}$ dilatational velocity of concrete (ft/sec)

C (1) shear coefficient 

(2) deflection coefficient for flat slabs 



<!-- batch 26 | page 21 -->

$C_{C}$ deflection coefficient for the center of interior panel of flat slab 

$C_{c r}$ critical damping 

$C_{d}$ shear coefficient for ultimate shear stress of one-way elements 

$C_{D}$ drag coefficient 

$C_{D}q$ drag pressure (psi)

$C_{D}q_{o}$ peak drag pressure (psi)

$C_{E}$ equivalent load factor 

$C_{f}$ post-failure fragment coefficient $(\mathsf{I b}^{2}\mathsf{m s}^{4}/\mathsf{i n}^{8})$ 

$C_{H}$ shear coefficient for ultimate shear stress in horizontal direction for two-way 

elements 

$C_{L}$ (1) leakage pressure coefficient from Figure 2-235 (+)

(2) deflection coefficient for midpoint of long side of interior flat slab panel 

(3) lift coefficient 

$C_{M}$ maximum shear coefficient 

$C_{m}$ equivalent moment correction factor 

$C_{p}$ compression wave seismic velocity in the soil from Table 2-10 (+) (in/sec)

$C_{r}$ sound velocity in reflected region from Figure 2-192 (+) (ft/ms)

$C_{R}$ force coefficient for shear at the corners of a window frame 

$C_{r\alpha}$ Peak reflected pressure coefficient at angle of incidence a 

$C_{s}$ shear coefficient for ultimate support shear for one-way elements 

$C_{s H}$ shear coefficient for ultimate support shear in horizontal direction for two-way 

elements 

$C_{s V}$ shear coefficient for ultimate support shear in vertical direction for two-way 

elements 

$C_{S}$ deflection coefficient for midpoint of short side of interior flat slab panel 

$C_{u}$ impulse coefficient at deflection $X_{u}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$ |

$C_{u}^{\prime}$ impulse coefficient at deflection $X_{m}(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n}^{2})$ 

$C_{v}$ shear coefficient for ultimate shear stress in vertical direction for two-way 

elements 



<!-- batch 26 | page 22 -->

$C_{x}$ shear coefficient for the ultimate shear along the long side of window frame 

$C_{y}$ shear coefficient for the ultimate shear along the short side of window frame 

$C_{L}$ confidence level 

$C_{1}$ (1) impulse coefficient at deflection $X_{1}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$ 

(2) ratio of gas load to shock load 

$C_{1}$ impulse coefficient at deflection $X_{m}(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n}^{2})$ 

$C_{2}$ ratio of gas load duration to shock load duration 

d (1) distance from extreme compression fiber to centroid of tension 

reinforcement (in)

(2) diameter (in)

(3) fragment diameter (in)

d distance from extreme compression fiber to centroid of compression 

reinforcement (in)

$d_{b}$ diameter of reinforcing bar (in)

$d_{c}$ distance between the centroids of the compression and tension reinforcement 

(in)

$d_{c H}$ distance between the centroids of the horizontal compression and tension 

reinforcement (in)

$d_{c o}$ diameter of steel core (in)

$d_{c v}$ distance between the centroids of the vertical compression and tension 

reinforcement (in)

$d_{e}$ distance from support and equal to distance d or $d_{c}\left(\mathsf{i n}\right)$ 

$d_{i}$ average inside diameter of explosive casing (in)

$d_{i}$ adjusted inside diameter of casing (in)

$d_{I}$ distance between center lines of adjacent lacing bends measured normal to 

flexural reinforcement (in)

$d_{p}$ distance from extreme compression fiber to centroid of prestressed 

reinforcement (in)

$d_{s p}$ depth of spalled concrete (in)

$d_{1}$ diameter of cylindrical portion of primary fragment (in)



<!-- batch 26 | page 23 -->

D (1) unit flexural rigidity (Ilb-in)

(2) location of shock front for maximum stress (ft)

(3) minimum magazine separation distance (ft)

(4) caliber density $(\mathsf{I b}/\mathsf{i n}^{3})$ 

(5) overall diameter of circular section (in)

(6) damping force (Ib)

(7) displacement of mass from shock load (in)

$D_{E}$ equivalent loaded width of structure for non-planar wave front (ft)

$D_{H}$ maximum horizontal displacement of the ground surface (in)

$D I F$ dynamic increase factor 

$D_{s}$ diameter of the circle through centers of reinforcement arranged in a circular 

pattern (in)

$D_{s p}$ diameter of the spiral measured through the centerline of the spiral bar (in)

$D L F$ dynamic load factor 

$D_{V}$ maximum vertical displacement of the ground surface (in)

e (1) base of natural logarithms and equal to 2.71828...

(2) distance from centroid of section to centroid of pre-stressed reinforcement 

(in)

(3) actual eccentricity of load (in)

$\mathbf{\boldsymbol{e}}_{b}$ balanced eccentricity (in)

$(2E)^{1/2}$ Gurney Energy Constant (ft/sec)

E (1) modulus of elasticity 

(2) internal work (in-lbs.)

$E_{c}$ modulus of elasticity of concrete (psi)

$E_{m}$ modulus of elasticity of masonry units (psi)

$E_{s}$ modulus of elasticity of reinforcement (psi)

(1) unit external force (psi)

(2) frequency of vibration (cps)

$f_{c}$ static ultimate compressive strength of concrete at 28 days (psi)



<!-- batch 26 | page 24 -->

$\pmb{f}_{d c}$ dynamic ultimate compressive strength of concrete (psi)

$\pmb{f}_{d m}$ dynamic ultimate compressive strength of masonry units (psi)

$f_{d s}$ dynamic design stress for reinforcement (a function of $f_{y_{1}}$ ,$f_{u},$ and Θ)(psi)

$f_{d u}$ dynamic ultimate stress of reinforcement (psi)

$f_{d y}$ dynamic yield stress of reinforcement (psi)

$f_{m}$ static ultimate compressive strength of masonry units (psi)

$f_{n}$ natural frequency of vibration (cps)

$f_{p s}$ average stress in the prestressed reinforcement at ultimate load (psi)

$\pmb{f}_{p u}$ specified tensile strength of prestressing tendon (psi)

$\pmb{f}_{p y}$ yield stress of prestressing tendon corresponding to a1 percent elongation 

(psi)

$f_{r}$ reflection factor 

$f_{s}$ static design stress for reinforcement (psi)

$f_{s e}$ effective stress in prestressed reinforcement after allowances for all prestress 

losses (psi)

$f_{u}$ static ultimate stress of reinforcement (psi)

$f_{y}$ static yield stress of reinforcement (psi)

$F$ (1) total external force (lbs)

(2) coefficient for moment of inertia of cracked section 

(3) function of $C_{2}$ and $C_{1}$ for bilinear triangular load 

$F_{o}$ force in the reinforcing bars (lbs)

$F_{E}$ equivalent external force (lbs)

$F_{D}$ drag force (Ibs)

$F_{F}$ frictional force (Ibs)

$F_{L}$ lift force (Ibs)

$F_{N}$ vertical load supported by foundation (lbs)

g acceleration due to gravity (32.2 ft/sec 2)

G shear modulus (psi)



<!-- batch 26 | page 25 -->

$$h_{n}$$

$$h_{t}$$

average clearing distance for individual areas of openings from Section 215.4.2



center-to-center dimension of a closed rectangular tie along h (in)

(2) distance between reflecting surface(s) and/or free edge(s) in vertical direction (ft)



(3) minimum transverse dimension of mean presented area of object (ft)

$$H_{c}$$

$$H_{s}$$

$$H_{T}$$

$$H_{w}$$

$$H^{c}$$

$$H^{d}$$

$$j_{a}$$

$$\overline{{i_{a}}}$$

$$\overline{{\dot{I}_{b}}}$$

$$\overline{{\dot{I}_{b a}}}$$

sum of blast impulse capacity of the receiver panel and the least impulse absorbed by the sand (psi-ms)



sum of scaled unit blast impulse capacity of receiver panel and scaled unit blast impulse attenuated through concrete and sand in a composite element (psi-ms/lb{/³3



scaled unit blast impulse capacity of receiver panel of composite element (psi-ms/lb1/³3)



<!-- batch 26 | page 26 -->

ibd scaled unit blast impulse capacity of donor panel of composite element (psi

$\mathsf{m s}/\mathsf{I b}^{1/3})$ 

$\overline{{j_{b t}}}$ total scaled unit blast impulse capacity of composite element (psi-ms/lb1/3)

$j_{c}$ impulse capacity of an element (psi-ms)

$j_{d}$ total drag and diffraction impulse (psi-ms)

$j_{e}$ unit excess blast impulse (psi-ms)

$j_{f s}$ required impulse capacity of fragment shield (psi-ms)

$j_{g}$ gas impulse (psi-ms)

$j_{r}$ unit positive normal reflected impulse (psi-ms)

$i_{r}^{-}$ unit negative normal reflected impulse (psi-ms)

$i_{r\alpha}$ peak reflected impulse at angle of incidence α (psi-ms)

$j_{s}$ unit positive incident impulse (psi-ms)

$j_{s}$ unit negative incident impulse (psi-ms)

$j_{s t}$ impulse consumed by fragment support connection (psi-ms)

(1) moment of inertia $(\mathsf{i n}^{4}/\mathsf{i n}$ for slabs)$(\mathsf{i n}^{4}\mathsf{f o r\;b e a m s})$ 

(2) total impulse applied to fragment 

$I_{a}$ average of gross and cracked moments of inertia $(\mathsf{i n}^{4}/\mathsf{i n}$ for slabs)$({\mathsf{i n}}^{4}$ for 

beams)

$I_{c}$ moment of inertia of cracked concrete section $(\mathsf{i n}^{4}/\mathsf{i n}$ for slabs)$({\mathsf{i n}}^{4}$ for beams)

$I_{c h}$ moment of inertia of cracked concrete section in horizontal direction $(\mathsf{i n}^{4}/\mathsf{i n})^{^*}$ 

$I_{c V}$ moment of inertia of cracked concrete section in vertical direction $(\mathsf{i n}^{4}/\mathsf{i n})^{*}$ 

$I_{g}$ moment of inertia of gross concrete section $(\mathsf{i n}^{4}/\mathsf{i n}$ for slabs)$({\mathsf{i n}}^{4}$ for beams)

$I_{m}$ mass moment of inertia $(\mathsf{I b}{-}\mathsf{m s}^{2}{-}\mathsf{i n})$ 

$I_{n}$ moment of inertia of net section of masonry unit $({\mathsf{i n}}^{4})$ 

$I_{s}$ gross moment of inertia of slab $(\mathsf{i n}^{4}/\mathsf{i n})$ 

$I_{s t}$ impulse consumed by the fragment support connection (psi-ms)

$I_{w}$ gross moment of inertia of wall $(\mathsf{i n}^{4}/\mathsf{i n})$ 

ratio of distance between centroids of compression and tension forces to the 

depth d 



<!-- batch 26 | page 27 -->

k (1) constant depending on the casing metal 

(2) effective length factor 

$k_{v}$ velocity decay coefficient 

K (1) unit stifness (psi/in for slabs) (Ib/in/in for beams) (Ib/in for springs)

(2) constant defined in Section 2-18.2

$K_{e}$ elastic unit stiffness (psi/in for slabs) (Ib/in/in for beams)

$K_{e p}$ elasto-plastic unit stifness (psi/in for slabs)(Ib/in/in for beams)

$K_{E}$ (1) equivalent elastic unit stiffness (psi/in for slabs) (Ib/in/ in for beams)

(2) equivalent spring constant (Ib/in)

$K_{L}$ load factor 

$K_{L M}$ load-mass factor 

$(K_{L M})_{u}$ load-mass factor in the ultimate range 

$(K_{L M})_{u p}$ , load-mass factor in the post-ultimate range 

$K_{M}$ mass factor 

$K_{R}$ resistance factor 

$K E$ kinetic energy 

charge location parameter (ft)

(1) length of the yield line (in)

(2) width of ½ of the column strip (in)

$I_{d}$ basic development length of reinforcing bar (in)

$I_{d h}$ development length of hooked bar (in)

$I_{c}$ length of cylindrical explosive (in)

$I_{p}$ spacing of same type of lacing bar (in)

$I_{s}$ span of flat slab panel (in)

L (1) span length (in)*

(2) distance between reflecting surface(s) and/or free edge(s) in horizontal 

direction (ft)

$L_{c y l}$ length of cylinder (in)



<!-- batch 26 | page 28 -->

$L_{f}$ length of fragment (in)

$L_{H}$ clear span in short direction (in)

$L_{I}$ length of lacing bar required in distance s/ (in)

$L_{L}$ clear span in long direction (in)

$L_{o}$ embedment length of reinforcing bars (in)

$L_{s}$ length of shaft (in)

$L_{u}$ unsupported length of column (in)

$L_{w}$ wave length of positive pressure phase (t)

$L_{w}$ wave length of negative pressure phase (ft)

$L_{x}$ clear span in long direction (in)

$L_{y}$ clear span in short direction (in)

$L_{w b},L_{w d}$ wave length of positive pressure phase at points b and d, respectively (ft)

$L_{1}$ total length of sector of element normal to axis of rotation (in)

$m$ (1) unit mass $(\mathtt{p s i}\mathtt{-m s}^{2}/\mathsf{i n}$ for slabs )$(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}^{2}}$ for beams)

(2) ultimate unit moment (in-lbs/in)

(3) mass of fragment $(\mathsf{l b s}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$ 

$m_{a}$ average of the effective elastic and plastic unit masses $(\mathtt{p s i}\mathtt{-}\mathtt{m s}^{2}/\mathsf{i n}$ for slabs)

[beams,$\mathtt{l b}\mathtt{-m s}^{2}/\mathsf{i n}^{2}]$ 

$m_{e}$ effective unit mass (psi-ms2/in for slabs)$(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}^{2}}$ for beams )

$m_{s p}$ mass of spalled fragments $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$ 

$m_{u}$ effective unit mass in the ultimate range $(\mathtt{p s i}\mathtt{-m s}^{2}/\mathsf{i n}$ for slabs)$(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}^{2}}$ for 

beams)

$m_{u p}$ effective unit mass in the post-ultimate range $(\mathsf{p s i}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$ 

M (1) unit bending moment (in-Ibs/in for slabs) (in-lbs for beams)

(2) total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$ 

(3) design moment (in-lbs)

$M_{e}$ effective total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$ 

$M_{u}$ ultimate unit resisting moment $(\mathsf{i n}-\mathsf{l b s}/\mathsf{i n}^{2}$ for slabs) (in-lbs for beams)

$M_{u}$ ultimate unit rebound moment (in-lbs/in for slabs) (in-Ibs for beams)



<!-- batch 26 | page 29 -->

$M_{c}$ moment of concentrated loads about line of rotation of sector (in-lbs)

$M_{A}$ fragment distribution factor 

$M_{E}$ equivalent total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$ 

$M_{H N}$ ultimate unit negative moment capacity in horizontal direction (in-lbs/in)

$M_{H P}$ ultimate unit positive moment capacity in horizontal direction (in-lbs/in)

$M_{O H}$ $M_{O L}$ total panel moment for direction H and L respectively (in-lbs)

$M_{N}$ ultimate unit negative moment capacity at supports (in-Ibs/in for slabs) (in-lbs 

for beams)

$M_{P}$ ultimate unit positive moment capacity at midspan (in-lbs/in for slabs) (in-lbs 

for beams)

$M_{V N}$ ultimate unit negative moment capacity in vertical direction (in-lbs/in)

$M_{V P}$ ultimate unit positive moment capacity in vertical direction $(\mathsf{i n}{-}\mathsf{l b s}/\mathsf{i n})^{*}$ 

$M_{1}$ value of smaller end moment on column 

$M_{2}$ value of larger end moment on column 

n (1) modular ratio 

(2) number of time intervals 

(3) number of glass pane tests 

(4) caliber radius of the tangent ogive of fragment nose 

N (1) number of adjacent reflecting surfaces 

(2) nose shape factor 

$N_{f}$ number of primary fragments larger than Wf 

$N_{u}$ axial load normal to the cross section 

$N_{T}$ total number of fragments 

$p$ reinforcement ratio equal to As/bd or $\mathsf{A}_{s}/\mathsf{b}\mathsf{d}_{\circ}$ 

$p$ reinforcement ratio equal to $\mathsf{A}^{\prime}s^{\prime}$ bd or $\mathsf{A}^{\prime}s^{\prime}$ bdc 

$p_{b}$ reinforcement ratio producing balanced conditions at ultimate strength 

$p_{o}$ ambient atmospheric pressure (psi)

$p_{p}$ prestressed reinforcement ratio equal to $\mathsf{A}_{\mathsf{p s}}/\mathsf{b d}_{\mathsf{p}}$ 

$p_{m}$ mean pressure in a partially vented chamber (psi)



<!-- batch 26 | page 30 -->

pmo peak mean pressure in a partially vented chamber (psi)

$p_{r}$ average peak reflected pressure (psi)

$p_{H}$ reinforcement ratio in horizontal direction on each face 

$p_{T}$ total reinforcement ratio equal to $p_{H}+p_{V}$ 

$p_{V}$ reinforcement ratio in vertical direction on each face 

$p(x)$ distributed load per unit length 

P (1) pressure (psi)

(2) concentrated load (lbs)

$P$ negative pressure (psi)

$P_{c}$ critical axial load causing buckling (lbs)

$P_{g}$ maximum gas pressure (psi)

$P_{i}$ interior pressure within structure (psi)

$\varDelta P_{i}$ interior pressure increment (psi)

$P_{f}$ fictitious peak pressure (psi)

$P_{m a x}$ maximum average pressure acting on interior face of wall (psi)

$P_{o}$ (1) peak pressure (psi)

(2) maximum axial load (lbs)

(3) atmospheric pressure (psi)

$P_{r}$ peak positive normal reflected pressure (psi)

$P_{r}^{-}$ peak negative normal reflected pressure (psi)

$\bar{P}_{r\alpha}$ peak reflected pressure at angle of incidence α (psi)

$P_{R I B}$ maximum average pressure on backwall (psi)

$P_{s}$ positive incident pressure (psi)

$P_{s b},P_{s e}$ positive incident pressure at points b and e, respectively (psi)

$P_{s o}$ peak positive incident pressure (psi)

$P_{s o}$ peak negative incident pressure (psi)

$P_{s o b},P_{s o d},P_{s o e}$ peak positive incident pressure at points b, d, and e, respectively (psi)

$P_{u}$ ultimate axial load at actual eccentricity e (Ibs)



<!-- batch 26 | page 31 -->

$P_{x}$ ultimate load when eccentricity $\pmb{\epsilon}_{x}$ is present 

$P_{y}$ ultimate load when eccentricity ey is present (lbs)

q dynamic pressure (psi)

$q_{b}$ $q_{e}$ dynamic pressure at points b and e, respectively (psi)

$q_{o}$ peak dynamic pressure (psi)

$q_{o b}$ $q_{o e}$ peak dynamic pressure at points b and e, respectively (psi)

r (1) unit resistance (psi)

(2) radius ofspeial [nsityqualsIb/ft3]charge (ft)

(3) radius of gyration of cross section of column (in)

r unit rebound resistance (psi, for slabs) (Ib/in for beams)

ravail dynamic resistance available (psi)

Δr change in unit resistance (psi, for slabs) (Ib/in for beams)

$r_{d}$ radius from center of impulse load to center of door rotation (in)

$r_{D L}$ uniform dead load (psi)

$r_{e}$ elastic unit resistance (psi, for slabs) (Ib/in for beams)

$r_{e p}$ elasto-plastic unit resistance (psi, for slabs) (Ib/in for beams)

$r_{f s}$ ultimate unit resistance of fragment shield (psi)

$r_{s}$ radius of shaft (in)

$r_{T}$ tension membrane resistance (psi)

$r_{u}$ ultimate unit resistance (psi, for slabs) (Ib/in for beams)

$r_{u p}$ post-ultimate unit resistance (psi)

$r_{1}$ radius of hemispherical portion of primary fragment (in)

R (1) total internal resistance (lbs)

(2) slant distance (ft)

(3) ratio of S/G 

(4) standoff distance (f)

$R_{e f f}$ effective radius (ft)



<!-- batch 26 | page 32 -->

$R_{f}$ (1) distance traveled by primary fragment (ft)

(2) distance from center of detonation (ft)

$R_{g}$ uplift force at corners of window frame (lbs)

$R_{I}$ radius of lacing bend (in)

$R_{t}$ target radius (ft)

$R_{A}$ normal distance (t)

$R_{E}$ equivalent total internal resistance (lbs)

$R_{G}$ ground distance (ft)

$R_{u}$ total ultimate resistance (lb)

$R_{I},R_{I I}$ total internal resistance of sectors I and Il, respectively (lbs)

s (1) sample standard deviation 

(2) spacing of torsion reinforcement in a direction parallel to the longitudinal 

reinforcement (in)

(3) pitch of spiral (in)

$s_{s}$ spacing of stirrups in the direction parallel to the longitudinal reinforcement 

(in)

S_{1$spacing of lacing in the direction parallel to the longitudinal reinforcement (in)

S height of front wall or one-half its width, whichever is smaller (ft)

S'weighted average clearing distance with openings (ft)

SE strain energy 

t time (ms)

Δt time increment (ms)

$t_{a}$ any time (ms)

$\mathbf{\mathit{t}}_{b},\mathbf{\mathit{t}}_{e},\mathbf{\mathit{t}}_{f}$ time of arrival of blast wave at points b, e, and f, respectively (ms)

$t_{c}$ (1) clearing time for reflected pressures (ms)

(2) average casing thickness of explosive charges (in)

$\mathbf{f}_{\circ}$ (1) adjusted casing thickness (in)

(2) Clearing time for reflected pressures adjusted for wall openings (ms)

$t_{d}$ rise time (ms)



<!-- batch 26 | page 33 -->

$t_{E}$ time to reach maximum elastic deflection (ms)

$t_{g}$ fictitious gas duration (ms)

$t_{m}$ time at which maximum deflection occurs (ms)

$t_{0}$ duration of positive phase of blast pressure (ms)

$t_{0}$ duration of negative phase of blast pressure (ms)

$t_{o f}$ fictitious positive phase pressure duration (ms)

$t_{o f}$ fictitious negative phase pressure duration (ms)

$t_{r}$ fictitious reflected pressure duration (ms)

$t_{u}$ time at which ultimate deflection occurs (ms)

$t_{y}$ time to reach yield (ms)

$t_{A}$ time of arrival of blast wave (ms)

$t_{A G}$ time of arrival of ground shock (ms)

$t_{1}$ time at which partial failure occurs (ms)

$T$ (1) duration of equivalent triangular loading function (ms)

(2) thickness of masonry wall (in)

(3) toughness of material (psi-in/in)

$T_{c}$ thickness of concrete section (in)

$\overline{{T}}_{c}$ scaled thickness of concrete section $(\mathsf{f t}/\mathsf{I b}^{1/3})$ )

$T_{g}$ thickness of glass (in)

$T_{H}$ force in the continuous reinforcement in the short span direction (lbs)

$T_{i}$ angular impulse load (lb-ms-in)

$T_{L}$ force in the continuous reinforcement in the long span direction (lbs)

$T_{N}$ effective natural period of vibration (ms)

$T_{p f}$ minimum thickness of concrete to prevent perforation by a given fragment (in)

$T_{r}$ rise time (ms)

$T_{s}$ (1) thickness of sand fill (in)

(2) thickness of slab (in)



<!-- batch 26 | page 34 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td colspan="2">minimum concrete thickness to prevent spalling (in) $T_{s p}$</td></tr></thead><tbody><tr><td>$\overline{{T}}_{s}$</td><td>scaled thickness of sand fill 1 $(\mathsf{f t}/\mathsf{I b}^{1/3})$</td></tr><tr><td>$T_{u}$</td><td>total torsional moment at critical section (in-lbs)</td></tr><tr><td>$T_{w}$</td><td>thickness of wall (in)</td></tr><tr><td>$T_{y}$</td><td>force of the continuous reinforcement in the short direction (lbs)</td></tr><tr><td>u</td><td>particle velocity (ft/ms)</td></tr><tr><td>$u_{u}$</td><td>ultimate flexural or anchorage bond stress (si)</td></tr><tr><td>U</td><td>shock front velocity (ft/ms)</td></tr><tr><td>$U_{s}$</td><td>strain energy</td></tr><tr><td>$v$</td><td>velocity (in/ms)</td></tr><tr><td>$v_{a}$</td><td>instantaneous velocity at any time (in/ms)</td></tr><tr><td>$v_{b}$</td><td>boundary velocity for primary fragments (ft/sec)</td></tr><tr><td>$\mathsf{v_{c}}$</td><td>ultimate shear stress permitted on an unreinforced web (psi)</td></tr><tr><td>$v_{f}$</td><td>maximum post-failure fragment velocity (in/ms)</td></tr><tr><td>Vf(avg)</td><td>average post-failure fragment velocity (in/ms)</td></tr><tr><td>$v_{i}$</td><td>velocity at incipient failure deflection (in/ms)</td></tr><tr><td>$v_{o}$</td><td>initial velocity of primary fragment (ft/sec)</td></tr><tr><td>$v_{r}$</td><td>residual velocity of primary fragment after perforation (ft/sec)</td></tr><tr><td>$v_{s}$ $v_{u}$ $v_{t u}$</td><td>striking velocity of primary fragment (ft/sec)</td></tr><tr><td>$v_{t c}$</td><td>maximum torsion capacity of an unreinforced web (psi)</td></tr><tr><td></td><td>nominal torsion stress in the direction of (psi) $v_{u}$</td></tr><tr><td>ultimate shear stress (psi)</td><td></td></tr><tr><td>$v_{u H}$</td><td>ultimate shear stress at distance  from the horizontal support (psi) $d_{e}$</td></tr><tr><td>$v_{u V}$</td><td>ultimate shear stress at distance from the vertical support (psi) $d_{e}$</td></tr><tr><td>$v_{x}$</td><td>velocity in x direction (in/ms)</td></tr><tr><td>$v_{y}$</td><td>velocity in y direction (in/ms)</td></tr></tbody></table></body></html></div>


<!-- batch 26 | page 35 -->

V (1) volume of partially vented chamber $(\mathsf{f t}^{3})$ 

(2) velocity of compression wave through concrete (in/sec)

(3) velocity of mass under shock load (in/sec)

$V_{d}$ ultimate direct shear capacity of the concrete of width b (Ibs)

$V_{d H}$ shear at distance $d_{e}$ from the vertical support on a unit width (Ibs/in*

$V_{d V}$ shear at distance $d_{e}$ from the horizontal support on a unit width (Ibs/in)

$V_{f}$ free volume $(\mathsf{f t}^{3})$ 1

$V_{H}$ maximum horizontal velocity of the ground surface (in/sec)

$V_{o}$ volume of structure (ft³)

$V_{s}$ shear at the support (Ib/in, for panels) (Ibs for beam)

$V_{s H}$ shear at the vertical support on a unit width (Ibs/in)*

$V_{s V}$ shear at the horizontal support on a unit width (Ibs/in)*

$V_{u}$ total shear on a width b (Ibs)

$V_{V}$ maximum vertical velocity of the ground surface (in/sec)

$V_{x}$ unit shear along the long side of window frame (lb/in)

$V_{\gamma}$ unit shear along the short side of window frame (lbs/in)

$w$ applied uniform load (lbs-in2)

$w_{c}$ (1) unit weight (psi, for panels) (Ib/in for beam)

(2) weight density of concrete (lbs/ft³)

$w_{s}$ weight density of sand (lbs/ft³3)

$W$ (1) design charge weight (Ibs)

(2) external work (in-lbs)

(3) width of wall (ft)

$W_{A}$ weight of fluid (Ibs)

$W_{A C T}$ actual quantity of explosives (lbs)

$W_{c}$ total weight of explosive containers (Ilbs)

$W_{E}$ effective charge weight (lbs)

$W_{E g}$ effective charge weight for gas pressure (Ib)



<!-- batch 26 | page 36 -->

$W_{E X P}$ weight of explosive in question (Ibs)

$W_{t}$ weight of primary fragment (oz)

$\overline{{W}}_{f}$ average fragment weight (oz)

$W_{F}$ weight of frangible element (b/ft2)

$W_{C I}$ weight of inner casing (lbs)

$W_{c o}$ total weight of steel core (lbs)

$W_{c o}$ weight of outer casing (lbs)

$W_{c1}$ 1,$W_{c2}$ total weight of plates 1 and 2, respectively (lbs)

$W_{s}$ width of structure (ft)

WD work done 

X yield line location in horizontal direction (in)*

X (1) deflection (in)

(2) distance from front of object to location of largest cross section to plane of 

shock front (ft)

$X_{a}$ any deflection (in)

$X_{c}$ lateral deflection to which a masonry wall develops no resistance (in)

$X_{D L}$ deflection due to dead load (in)

$X_{e}$ elastic deflection (in)

$X_{E}$ equivalent elastic deflection (in)

$X_{e p}$ elasto-plastic deflection (in)

$X_{t}$ maximum penetration into concrete of armor-piercing fragments (in)

$X_{f}$ maximum penetration into concrete of fragments other than armor-piercing 

(in)

$X_{m}$ maximum transient deflection (in)

$X_{p}$ plastic deflection (in)

$X_{s}$ (1) maximum penetration into sand of armor-piercing fragments (in)

(2) static deflection (in)

$X_{u}$ ultimate deflection (in)



<!-- batch 26 | page 37 -->

$X{1$(1) partial failure deflection (in)

(2) deflection at maximum ultimate resistance of masonry wall (in)

y yield line location in vertical direction (in)*

y_t distance from the top of section to centroid (in)

Z scaled slant distance (ft/b"3)

ZA scaled normal distance (ft/lb1/3)

$ZG$scaled ground distance (ft/lb1/3)

α(1) angle formed by the plane of stirups, lacing, or diagonal reinforcement 

and the plane of the longitudinal reinforcement (deg)

(2) angle of incidence of the pressure front (deg)

(3) acceptance coefficient 

(4) trajectory angle (deg.)

αec ratio of flexural stiffness of exterior wall to flat slab 

αecH, αecL ratio offlexural stifness of exterior wall to slab in direction Hand L 

respectively 

B (1) coefficient for determining elastic and elasto-plastic resistances 

(2) particular support rotation angle (deg)

(3) rejection coefficient 

(4) target shape factor from Figure 2-212 (+/+)

$\beta_{1}$ factor equal to 0.85 for concrete strengths up to 4,000 psi and is reduced by 

0.05 for each 1,000 psi in excess of 4,000 psi 

γcoefficient for determining elastic and elasto-plastic deflections 

$γ_p$factor for type of prestressing tendon 

δmoment magnifier 

$\delta_{n}$ clearing factor 

Δdeflection at sector's displacement (in)

$\varepsilon_{c}^{\prime}$ average strain rate for concrete (in/in/ms)

εm unit strain in mortar (in/in)

$\varepsilon_{s}^{\prime}$ average strain rate for reinforcement (in/in/ms)

4A-124



<!-- batch 26 | page 38 -->

εu rupture strain (in/in/ms)

日(1) support rotation angle (deg)

(2) angular acceleration (rad/ms2)

Θmax maximum support rotation angle (deg)

ΘH horizontal rotation angle (deg)

ΘV vertical rotation angle (deg)*

λincrease in support rotation angle after partial failure (deg)

μ(1) ductility factor 

(2) coefficient of friction 

V Poisson's ratio 

ρ(1) mass density (lbs-ms2/in4)

(2) density of air behind shock front (Ibs/ft3)

ρa density of air (oz/in3)

ρc density of casing (oz/in^³)

ρf mass density of fragment (oz/in³3)

ρo mass density of medium (Ib-ms2/in4)

Ou fracture strength of concrete (psi)

∑0effective perimeter of reinforcing bars (in)

ΣM summation of moments (in-lbs)

ΣMN sum of the ultimate unit resisting moments acting along the negative yield 

lines (in-lbs)

ΣMp sum of the ultimate unit resisting moments acting along the positive yield lines 

(in-lbs)

Ts maximum shear stress in the shaft (psi)

φ(1) capacity reduction factor 

(2) bar diameter (in)

(3) TNT conversion factor 

φr assumed shape function for concentrated loads 



<!-- batch 26 | page 39 -->

UFC 3-340-025 December 2008Change 2,1 September 2014φ(x)assumed shape function for distributed loads free edge ωangular velocity (rad./ms)



simple support 

77777777fixed support 

XXXXXXXX either fixed, restrained, or simple support 

<!-- batch 26 | page 40 -->

## APPENDIX 4C BIBLIOGRAPHY 

1.ACI Design Handbook: Beams, One-Way Slabs, Brackets, Footings, Pile Caps,Columns, Two-Way Slabs, and Seismic Design, Special Publication 17,American Concrete Institute, 1997.
2.ACI Detailing Manual, Special Publication 66(04), American Concrete Institute,
Detroit, MI, 2004.
3.Building Code Requirements for Structural Concrete (ACI 318-08) and Commentary, ACI Committee 318, American Concrete Institute, Detroit, MI,
January 2008.
4.Design and Analysis of Hardened Structures to Conventional Weapons Effects,
The Departments of the Army, Air Force, and Navy and the Defense Special Weapons Agency, Army TM 5-855-1, Air Force Manual AFPAM 32-1147(I), Navy NAVFAC P-1080, DSWA DAHSCWEMAN-97, October 1998.5.Design Criteria for Deflection Capacity of Conventionally Reinforced Concrete Slabs, an investigation conducted by Construction Technology Laboratories,
Structural Analytical Section, 5420 Öld Orchard Road, Skokie,IIlinois 60077, for Civil Engineering Laboratory, Naval Construction Battalion Center, Port Hueneme, CA, sponsored by Naval Facilities Engineering Command, Phase IState-of-the-Art Report, CR 80.026, October 1980, Phase-lI - Design and Construction Requirements, CR 80.027. October 1980, Phase II - Summary of Design Criteria and Design and Construction Details - Design Examples, CR 80.028, October 1980.
6.Design Manual, AEC Test Structures , Volumes Il and Il, by Holmes and Narver,
Inc., under Contract AT (29-2)-20, for U.S. Atomic Energy Commission,
Albuquerque Operations Office, Albuquerque, NM, December 1961.7.Design of Structures to Resist Nuclear Weapons Effects, ASCE Manual of Engineering Practice No.42, American Society of Civil Engineers, New York, NY,
1961.
8.Design of Structures to Resist the Effects of Nuclear Weapons, Department of the Army Technical Manual TM 5-856-2, 3 and 4, Washington, D.C.9.Dynamic Tests of Concrete Reinforcing Steels, Technical Report R 394, U.S.
Naval Civil Engineering Laboratory, Port Hueneme, CA, September 1965.10.Effects of Impact and Explosion, Volume 1, Office of Scientific Research and Development, National Defense Research Committee, Washington, D.C., 1946(Confidential).
11.Fundamentals of Protective Design (Non-Nuclear), Department of the Army,
Technical Manual TM 5-855-1, Washington, D.C., July 1965.

<!-- batch 26 | page 41 -->

12.Impact Design Criteria for Blockhouses Subjected to Abortive Launch Environments, Technical Publication PMR-TR-70-2, Mechanics Research, Inc.,for the Pacific Missile Range, Point Mugu, CA, July 1970.13.Industrial Engineering Study to Establish Safety Design Criteria for Use in Enqineering of Explosive Facilities and Operations, by Ammann & Whitney Consulting Engineers, New York, NY, under Contract DA-28-017-501-0RD-3889,for Process Engineering Branch, A.P.M.E.D., Picatinny Arsenal, Dover, NJ, April 1963.
14.Non-Nuclear Weapons Effects on Protective Structures (U). Technical Report No. AFWL-TR-69-57, (SECRET), Mechanics Research, Inc., for the Air Force Weapons Laboratory, Kirtland Air Force Base, NM, September 199.15.Strenqth and Behavior of Laced Reinforced Concrete Slabs Under Static and Dynamic Load, Technical Report R620, prepared by Naval Civil Engineering Laboratory, Port Hueneme, California, Sponsored by Department of the Army,
Picatinny Arsenal, April 1969.
16.Summary of One-Third Scale Slab Tests and Scaled Bay Structure Tests, by Ammann & Whitney, Consulting Engineers, New York, NY, under Contract DA28-017-AMC-423(A) for Picatinny Arsenal, Dover, NJ, March 199.17.Ultimate Strength Design Handbook, Volume No.1, Special Publication No. 17.
ACI Committee 340, American Concrete Institute, Detroit, MI, 1967.18.Ultimate Strength Design of Reinforced Concrete Columns, Publication SP-7,
Interim Report of ACl Commitee 340, American Concrete Institute, Detroit, M,
1964.
19.U.S. Army Engineer Waterways Experiment Station, Technical Report N-72-10,
Design and Testing of a Blast-Resistant Reinforced Concrete Slab System,
Criswell, M.E., Vicksburg, MS, 1972.
20.Amirian, A., Dobbs, N. and Dede, M., Technical Approach for Structural Design Procedures for a Family of Horseshoe-Shaped MTC (Phase I), prepared for Naval Civil Engineering Laboratory, Port Hueneme, CA, by Ammann and Whitney, Consulting Engineers, New York, N.Y., August 1985.21.Ayvazian, H. and DeDe, M., Development of Preliminary Desiqns for NAVFAC MTCs and Preparation of Construction Cost Estimates, prepared for Naval Civil Engineering Laboratory, Port Hueneme, CA, by Ammann and Whitney,
Consulting Engineers, New York, N.Y., Draft 22.Ball, J. W., Baylot, J.T. and Kiger, S.A., Kirtland Underground Munitions Storage Complex Model Designs, Construction, and Test Data, Technical Report SL-8414, prepared by Structures Laboratory, Department of the Army, Waterways Experiment Station, Corps of Engineers, P.O. Box 631, Vicksburg, Mississippi 39180-0631,for Defense Nuclear Agency, Washington, D.C. 20305, Under DNA 

<!-- batch 26 | page 42 -->

Subtask B990AXRE, Work Unit 0004 and Subtask B99QAXRD, Work Unit 0013,"Advanced Design Explosive Tests," September 1984.
23.Baylot, J.T., Kiger, S.A. and Ball, J.W., Structural Design of Blast-Containment Facilities, Abstract for the Twenty-First Explosive Safety Seminar, prepared by U.S. Army Engineer Waterways Experiment Station, Vicksburg, Mississippi,
August 1984.
24.Baylot, J.T., Vulnerability of an Underground Weapon Storage Facility, Technical Report SL-84-16, prepared by Structures Laboratory, Department of the Army,
Waterways Experiment Station, Corps. of Engineers, P.O. Box 631, Vicksburg,
Mississippi 39180-0631, for Defense Nuclear Agency, Washington, DC 20305,
Under Subtask A99QAXFC, Work Unit 00046, September 1984.25.Bergstrom, P., et al., Hard-Structures Munitions -Phase I: Warhead (U), AFATLTR-67-13, Volume II (AD-379, 468), (SECRET), Chamberlain Corporation,
February 1967.
26.Beth, R. A., Final Report on Concrete Penetration, Report No. A-388, National Defense Research Committee, Office of Scientific Research and Development,
March 1946.
27.Beth, R. A. and Stipe, J. G., Penetration and Explosion Tests on Concrete Slabs,
Report I: Data, Interim Report No. 20, Committee on Passive Protection Aainst Bombing, National Research Council, January 1943.
28.Branson, D., Deformation of Concrete Structures, McGraw-Hill, Inc., New York,
NY, 1977.
29.Brown, J. W., Response of Selected Materials to High-Speed Fragment Impact,
U.S. Army Engineer Waterways Experiment Station, Vicksburg, MS, 1970.30.Cohen, E. and Dobbs, N., Design Procedures and Details for Reinforced Concrete Structures Utilized in Explosive Storage and Manufacturing Facilities,
Ammann & Whitney, Consulting Engineers, New York, NY, Annals of the New York Academy of Sciences, Conference on Prevention of and Protection Against Accidental Explosion of Munitions , Fuels and Other Hazardous Mixtures,
Volume 152, Art. 1, October 1968.
31.Cohen, E. and Dobbs, N., Models for Determining the Response of Reinforced Concrete Structures to Blast Loads, Ammann & Whitney, Consulting Engineers,
New York, NY, Annals of the New York Academy of Sciences, Conference on Prevention of and Protection Against Accidental Explosion of Munitions, Fuels and Other Hazardous Mixtures, Volume 152, Art. 1, October 1968.32.Cohen, E. and Dobbs, N., Supporting Studies to Establish Safety Design Criteria for Storage and Processing of Explosive Materials - Interim Re-port No. 1.
Summary of One-Third Scale Reinforced Concrete Slab Tests, Technical Memorandum C-1, by Ammann & Whitney, Consulting Engineers, New York, NY,

<!-- batch 26 | page 43 -->

under Contract: DA-28-017-AMC-423(A) for Picatinny Arsenal, Dover, NJ, June 1965.
33.Coltharp, D.R., Vitayaudom, K.P. and Kiger, S.A., NATO Semihardened Facility Design Criteria Improvement, Final Report, prepared by Engineering and Services Laboratory, Air Force Engineering and Services Center, Tyndall Air Force Base, Florida 32403. June 1985.
34.Criswell, M.E., Design and Testing of a Blast-Resistant Reinforced Concrete Slab System, Technical Report N-72-10, Conducted by U.S. Army Engineer Waterways Experiment Station, Weapons Effects Laboratory, Vicksburg,
Mississippi, sponsored by Defense Civil Preparedness Agency, Work Order No.
DAH C20-68-W-0192, Work Unit 1127E, November 1972.35.Dede, M. and Amirian, A., Test Plan to Verify Failure Criteria for Conventionally Reinforced Concrete Slabs, prepared for Naval Civil Engineering Laboratory,
Port Hueneme, California, by Ammann and Whitney, Consulting Engineers, New York, N.Y., April 1985.
36.Doyle, J. M., Klein, M. J. and Shah, H., Design of Missile Resistant Concrete Panels, Preprints of the 2nd International Conference on Structural Mechanics in Reactor Technology, Vol. 4, Commission of the European Communities,
Brussels, 1973, Paper No. J 3/3.
37.Fisher, E. M., Explosion Effects Data Sheets, Report 2986, U.S. Naval Ordnance Laboratory, Silver Spring, MD, 1955.
38.Getchell, J.V. and Kiger, S.A., Vulnerability of Shallow-Buried Flat-Roof Structures, Technical Report SL-80-7, prepared by Structures Laboratory, U.S.
Army Engineer Waterways Experiment Station, P.O. Box 631, Vicksburg,
Mississippi 39180, for Defense Nuclear Agency, Washington, D.C. 20305 and Office, Chief of Engineers, U.S. Army, Washington, D.C. 20314, under DNA Subtask Y99QAXSC062, Work Unit 42, and Subtask H191AXSX337, Work Unit 02, and OCE R&D Project 4A762719AT40, Task AO, Work Unit 008, Report 2,
Foam HEST 4, October 1980, Report 3, Foam HEST 5, February 1981, Report 4,
Foam HEST 3 and 6, December 1981 and Report 5, Foam HEST 7, February 1982.
39.Gewaltney, R. C., Missile Generation and Protection in Light-Water-Cooled Power Reactor Plants, Nuclear Safety, 10(4): July-August 199.40.Giere, A. C., Calculating Fragment Penetration and Velocity Data for Use in Vulnerability Studies, NAVORD Report 6621, U.S. Naval Nuclear Evaluation Unit, Albuquerque, NM, October 1959.
41.Hoffman, P.R., McMath, R.R. and Migotsky, E., Projectile Penetration Studies AFWL Technical Report No. WL-TR-64-102, Avco Corporation for the Air Force Weapons Laboratory, Kirtland Air Force Base, NM, December 1964.

<!-- batch 26 | page 44 -->

42.Ingraham, J. M. and Abbott, K. N., Feasibility Study of Laminated Metallic Armor (U), AMRA TR 63-30, (CONFIDENTIAL), U.S. Army Materials Research Agency,Watertown, MA, December 1963.
43.Iqbal, M. and Derecho, A., Design Criteria for Deflection Capacity of Conventionally Reinforced Concrete Slabs, Phase I- State-of-the-Art Report,
Report No. CR 80.026, Naval Civil Engineering Laboratory, Port Hueneme, CA,
October 1980.
44.Johnson, C. and Moseley, J.W., Preliminary Warhead Terminal Ballistic Handbook. Part 1: Terminal Ballistic Effects, NAVWEPS Report No. 7673, U.S.
Naval Weapons Laboratory, Dahlgren, VA, March 194.45.Keenan, W. A., Strength and Behavior of Laced Reinforced Concrete Slabs Under Static and Dynamic Load, Technical Report R-620, U.S. Naval Civil Engineering Laboratory, Port Hueneme, CA, April 1969.46.Keenan, W., Tancreto, J., Meyers, G., Johnson, F., Hopkins, J., Nickerson, H.
and Armstrong, W., NCEL Products Supporting DOD Revision of NAVFAC P397,
Technical Memorandum 2591TM, prepared by Naval Civil Engineering Laboratory, Port Hueneme, California 93043, Program No.: Y0995-01-003-201,
Sponsored by Naval Facilities Engineering Command, Alexandria, Virginia 22332, March 1983.
47.Kiger, S.A. and Albritton, G.E., Response of Burried Hardened Box Structures to the Effects of Localized Explosions, Technical Report SL-80-1, prepared by Structures Laboratory, U.S. Army Engineer Waterways Experiment Station, P.O.
Box 631, Vicksburg, Mississippi 39180,for Defense Nuclear Agency,
Washington, D.C. 20305 and Office, Chief of Engineers, U.S. Army, Washington,
D.C. 20314, under DNA Subtask Y99QAXSC062, Work Unit 04, and OCE R&D Project 4A762719AT40, Task A1, Work Unit 027, March 1980.48.Kymer, J. R., Penetration Performance of Arrow Type Projectiles, Report R1814,
U.S. Army Frankford Arsenal, Philadelphia, PA, May 1966.49.Liu, T.C., Strength Design of Reinforced Concrete Hydraulic Structures,
Preliminary Strength Design Criteria, Technical Report SL-80-4, Report 1 of a series, prepared by Structures Laboratory, U.S. Army Engineer Waterways Experiment Station, P.O. Box 631, Vicksburg, Mississippi 39180, for Office, Chief of Engineers, U.S. Army, Washington, D.C. 20314, under CWIS 31623, July 1980.
50.Malvar, L. J., Review of Static and Dynamic Properties of Steel Reinforcing Bars,
ACI Materials Journal, vol. 95, no. 5, September-October 1998, pp. 60-616.51.Malvar, L. J. and Crawford, J. E., Dynamic Increase Factors for Steel Reinforcing Bars, Twenty-Eighth DOD Explosive Safety Seminar Proceedings, Orlando, FL,
August 1998.


<!-- batch 26 | page 45 -->

52.Malvar, L. J. and Ross, C. A., Review of Static and Dynamic Properties of Concrete in Tension, ACI Materials Journal, vol. 95, no. 6, November-December 1998, pp. 735-739.
53.Mascianica, F. S., Summary of Terminal Ballistic Data on Lightweight Armor Materials (U), AMMRC TR 69-17, (CONFIDENTIAL), U.S. Army Materials and Mechanics Research Center, Watertown, MA, July 1969.54.Nara, H. R. and Denington, R. J. Ricochet and Penetration of Steel Spheres in Clay and Sand Soils, TM-E7, AD-059 883, Case Institute of Technology, Project DOAN BROOK, October 1954.
55.Newmark, N. M. and Haltiwanger, J. D., Air Force Design Manual, Principles and Practices for Design of Hardened Structures, Technical Documentary Report No.
AFSWC-TDR-62-138, by Department of Civil Engineering, University of Ilinois,
Urbana, Ilinois, under Contract AF29 (601)-2390 for Research Directorate, Air Force Special Weapons Center, Air Force Systems Command, Kirtland Air Force Base, NM, December 1962.
56.Park, R. and Gamble, W. L., Reinforced Concrete Slabs, Second Edition, ISBN 978-0-471-34850-4, John Wiley & Sons, New York, NY, December 1999.57.Pecone, G., Design of Flat Slabs Subjected to Blast Loads, prepared for Northern Division, Naval Facilities Engineering Command, U.S. Naval Base,
Philadelphia, PA, by Ammann and Whitney, Consulting Engineers, New York,
N.Y., Contract No. N 62472-76-C-1148, June 1982.
58.Recht, R., et al., Application of Ballistic Perforation Mechanics to Target Vulnerability and Weapons Effectiveness Analysis (U), NWC TR 4333(Confidential), Denver Research Institute for the Naval Weapons Center, China Lake, CA, October 1967.
59.Richey, H. M., Armed Services Explosives Safety Board Dividing Wall Pro- gram,
Phase C, Tests 1 through 13, U.S. Naval Weapon Center, China Lake, CA, 1964(Secret Restricted Data).
60.Rindner, R. M., Establishment of Safety Design Criteria for Use in Engineering of Explosive Facilities and Operations, Report No.2, Detonation by Fraqment Impact, Technical Report DB-TR: 6-59, Picatinny Arsenal, Dover, NJ, March 1959.
61.Robertson, H.P., Terminal Ballistics, Preliminary Report, Committee on Passive Protection Against Bombing, National Research Council, January 1941.62.Rohani, B., Fragment and Projectile Penetration Resistance of Soils: Report 2,
High-Velocity Fragment Penetration into Laboratory-Prepared Soil Targets,
Miscellaneous Paper S-71-12, U.S. Army Engineer Waterways Experiment Station, Vicksburg, MS, June 1973.


<!-- batch 26 | page 46 -->

63.Stipe, J. G., et al., Ballistic Tests on Small Concrete Slabs, Interim Report No.28, Committee on Fortification Design, National Research Council, June 1944.64.Schumacher, R.N., Kingery, C.N. and Ewing, Jr., W.O., Airblast and Structural Response Testing of a 1/4 Scale Category 1 Suppressive Shield, BRL Memorandum Report No. 2623, by U.S.A. Ballistic Research Laboratories,Aberdeen Proving Ground, Maryland, May 1976.
65.Schwartz, A., et. al., Establishment of Safety Design Criteria for Use in Enqineering of Explosive Facilities and Operations, Report No. 6, Test of OneTenth Scale Bay Structure, Technical Report 3439, by Picatinny Arsenal, Dover,
NJ, and Ammann & Whitney, Consulting Engineers, New York, NY, under Contract DA-28-017-AMC-423(A), July 1966.
66.Takayahagi, T. and Derecho, A., Design Criteria for Deflection Capacity of Conventionally Reinforced Concrete Slabs, Phase Il - Summary of Desiqn Criteria and Construction Details - Design Examples, Report No. CR 80.028,
Naval Civil Engineering Laboratory, Port Hueneme, CA, October 180.67.Takayanagi, T., Derecho, A. and Iqbal, M., Design Criteria for Deflection Capacity of Conventionally Reinforced Concrete Slabs, Phase lI - Design and Construction Requirements, Report No. CR 80.027, Naval Civil Engineering Laboratory, Port Hueneme, CA, October 1980.
68.Tancreto, J., Design Criteria for Deflection Capacity of Conventionally Reinforced Concrete Slabs, Naval Civil Engineering Laboratory, Special Project 1311 SP,
Port Hueneme, CA, 1980.
69.Thomas, L.H., Computing the Effect of Distance on Damage by Fragments,
Report No. 468, Ballistic Research Laboratories, Aberdeen Proving Ground, MD,
May 1944.
70.Timoshenko, S. and Woinowsky-Krieger, S., Theory of Plates and Shells,
McGraw-Hill Book Co., New York, NY, 1959.
71.Vanderbilt, M., Sozen, M. and Seiss, C., Deflections of Multiple-Panel Reinforced Concrete Floor Slabs, Journal of the Structural Division, Proceedings of the American Society of Civil Engineers, August 1965.
72.Vargas's, L. M., Hokanson, J. C. and Rinder, R. M., Explosive Fraqmentation of Dividing Walls, by Southwest Research Institute, San Antonio, TX, Contractor Report ARLCD-CR-81018, U.S. Army Armament Research and Development Command, Large Caliber Weapons Systems Laboratory, Dover, NJ, July 1981.73.Wachtell, S., Comparison of Blast Response-Scaled vs. Full-Size Concrete Structures, Picatinny Arsenal, Dover, NJ, Annals of the New York Academy of Sciences, Conference on Prevention of and Protection Against Accidental Explosions of Munitions, Fuels and Other Hazardous Mixtures, Volume 152, Art.
1, October 1968.


<!-- batch 26 | page 47 -->

74.Wang, Chu-Kia and Salmon, Charles G., and Pincheira, Jose A., Reinforced Concrete Design, Seventh Edition, ISBN: 978-0-471-26286-2, John Wiley and Sons, Inc., New York, NY, July 2006.
75.Whitney, C. S., Plastic Theory of Reinforced Concrete Design, Transactions of the American Society of Civil Engineers, Vol. 107, ASCE, New York, NY, 1942.76.Whitney, C. S. and Cohen, E., Guide for Ultimate Strength Design of Reinforced Concrete, Ammann & Whitney, Consulting Engineers, New York, NY, Journal of the American Concrete Institute, November 1956.
77.Whitney, C. S., et. al., Design of Blast-Resistant Construction for Atomic Explosions, Ammann & Whitney, Consulting Engineers, New York, NY, Journal of the American Concrete Institute, March 1955.
78.Wood, R. W., Plastic and Elastic Design of Slabs and Plates, The Ronald Press Company, New York, NY, 1961.
79.Woodson, S. C. and Zehrt, W. H., Jr., Investigation of Army TM 5-1300/NAVFAC P-397/AFR 88-22 Diagonal Tension Requirements at Low Scaled Distances,
Thirty-Second DOD Explosives Safety Seminar Proceedings, Philadelphia, PA,
August 2006.
80.Zehrt, W. H., Jr., Woodson, S. C., and Beck, D. C., Investigation of Army TM 51300/NAVFAC P-397/AFR 8-22 Bar Bend Requirements for Single Leg Stirrups used as Diagonal Tension Reinforcement, Thirty-Second DOD Explosives Safety Seminar Proceedings, Philadelphia, PA, August 2006.
81.Hentz, S., Donze, F., and Daudeville, L.2004a), "Discrete element modeling of concrete submitted to dynamic loading at high strain rates," Computer and Structures, 82, pp. 2509-2524
82.Hentz, S., Daudeville, L, and. Donze, F. (2004b), "Identification and validation of a discrete element for concrete," Journal of Engineering Mechanics, ASCE, Vol.
130, No. 6, June, pp. 709-719.
83.Zheng, D. and Li, Q., (2004), "An explanation for rate effect of concrete strength based on fracture toughness including free water viscosity," Engineering Fracture Mechanics, 71, pp. 2319-2327.
84.Ozbolt, Josko, Weerheijm, J., and Sharma, A, (2013), "Dynamic Tensile Resistance of Concrete- Split Hopkinson Bar Test," Vll International Conference on Fracture Mechanics of Concrete and Concrete Structures, FraMCoS-S.85.Haussler-Combe, U. and Kuhn, T., (2013), "A viscoelastic retarded damage material law for concrete structures exposed to impact and explosions," VilI International Conference on Fracture Mechanics of Concrete and Concrete Structures, FraMCoS-S.


<!-- batch 26 | page 48 -->

86.Rossi, P,(1991), "A physical phenomenon which can explain the mechanical behavior or concrete under high strain rates," Materials and Structures, 24, 422424.
87.Rossi, P, Van Mier, JGM, Toutlemode, R., Le Maou, F., and Boulay, C., (194),
"Effect of loading rate on the strength of concrete subjected to uniaxial tension,
Materials and Structures, 27, pp. 260-264.
88.Janach, W., (1976), "The role of bulking in brittle failure of rocks under rapid compression," International Journal of Rock Mechanics and Mineral Science Geomechanics, 13, pp. 177-186
89.Reinhardt, H.W., and Weerheigm, J., (1991) "Tensile fracture of concrete at high loading rates taking account of inertia and crack velocity effects," International Journal of Fracture, 51, pp. 31-42. (high strain rate effects due to inertia)90.Eibl, J. and Schmidt-Hurtienne, B., (1999) "Strain rate-sensitive constitutive law for concrete," Journal of Engineering Mechanics, 125, pp. 1411-1420. (high strain rate effects due to inertia)
91.Rowell, S. P., Grey, C. E., Woodson, S.C. and Hager, K. P., "High Strain-Rate Testing of Mechanical Couplers," ERDC TR-09-8, US Army Corps of Engineers,
Engineer Research and Development Center, September 2009.