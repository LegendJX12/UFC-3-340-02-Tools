

<!-- batch 30 | page 1 -->

EXAMPLE 5A-5 (A)DESIGN OF AN OPEN-WEB STEEL JOIST 

Required:Design a simply-supported open-web steel joist whose capacity is controlled by flexure.



## Solution:

Step 1.Given:

a.Pressure-time loading 

(Figure 5A-4 (+))

b.Clear span =50'-0"

Spacing of joists = 7'-0"

Weight of decking  = 4 psf 

C.Structural steel properties 

Chords $f_{v}=50,000\;\mathrm{p s i}$ 

Web 

$$f_{v}=36,000\mathrm{p s i}$$

Dynamic increase factor (chords only).

$$\mathsf{D I F}=1.19$$

(Table 5-2 (+), for A588)

Dynamic design stress,$\boldsymbol{f}_{d s}=\boldsymbol{D I F}\times\boldsymbol{S I F}\times\boldsymbol{f}_{V}$ (Equation 5-2)

Chords $f_{ds}=1.19\times1.1\times50,000=65,450\mathrm{psi}$ 

d.Design criteria 

(Section 5-35)

Maximum ductility ratio: μmax =4.0

Maximum end rotation:$\mathcal{O}_{\mathrm{m a x}}\qquad=2^{\circ}$ 

<!-- batch 30 | page 2 -->

Figure 5A-4 Joist Cross-Section and Loading, Example 5A-5(a)

<div style="text-align: center;"><img src="../pages/batch 30/imgs/img_in_image_box_226_316_954_884.jpg" alt="Image" width="61%" /></div>


### Step 2.Selection of joist size 

a.Assume a dynamic load factor. For preliminary design, a $\mathsf{D L F}=1.0$ is generally recommended. However, since the span is quite long in this case,a DLF of 0.62 is selectd.



b.Equivalent static load on joist:

$$w_{1}=0.62\times2.0\times144\times7.0=1.250\mathrm{~lb/ft}$$

C.Corresponding allowable design load on joist:

$$w_{2}=w_{1}/(1.7\times1.19\times1.1)=1.250/2.23=561\ \mathrm{lb/ft}$$

d.Using the "Standard Specifications, Load Tables and Weight Tables" of the Steel Joist Institute, for a span of 50'-O", try 32LH11.Joist tables show that capacity is controlled by flexure.

Total load-carrying capacity (including dead load $)=602$ Ib/ft 

Approximate weight of joist and decking 

$$28+(4\times7)=56\ lb/\mathrm{ft}$$

<!-- batch 30 | page 3 -->

Total allowable loadcapacity (excluding dead $\mathrm{load})=602-56=$ 546 Ib/ft 



The following section properties refer to the selected joist 32LH11(Figure 5A-4 (+)):

Top Chord:

$$\begin{aligned}&Two3×3×5/16angles\\ &A=3.56in^2\\ &r_x=0.92in\\ &r_y=1.54in\\ &I_x=3.02in^4\\ \end{aligned}$$

Bottom Chord:

$$\begin{aligned}&Two3×2-1/2×1/4angles\\&A=2.62in^2\\&r_x=0.945in\\&r_y=1.28in\\&I_x=2.35in^4\\&I_{xx}for joist=1,383.0in^4\\&Panel length=51inches\\ \end{aligned}$$

Note: If the moment of inertia for the joist $(\mathsf{I}_{\mathsf{x}\mathsf{x}})$ is not available, it may be estimated from the load causing a given deflection to span ratio (i.e. midspan deflection equal to L/240)stated in the "Standard Specifications, Load Tables and Weight Tables" for the given joist size and span, the corresponding midspan deflection, the elastic modulus for steel,and the theoretical deflection equation for a beam in flexure with simple supports.However, care should be taken for short spans where the allowable load in the "Standard Specifications, Load Tables and Weight Tables" may not be not controlled by flexural response.



Step 3.Resistance per unit length 

$$r_{u}=1.7\times1.19\times1.1\times546=1215\text{lb/ft}$$

Step 4.

$$K_{E}=\frac{384EI}{5L^{3}}=\frac{384\times29\times10^{6}\times1383}{5\times(12\times50)^{3}}=14.260\ lb/ln $$

<!-- batch 30 | page 4 -->

$$X_{E}=\frac{r_{u}L}{K_{E}}=\frac{1215\times50}{14260}=4.26\text{inches}$$

Step 5.Total mass of joist plus decking 

$$M=\frac{56\times50\times10^{6}}{386}=7.25\times10^{6}\mathrm{~lb}-\mathrm{ms}^{2}/\mathrm{in}$$

Total effective mass $M_{e}=K_{L M}M$ 

$$K_{LM}=0.5(0.78+0.66)=0.72$$

(Table 3-12 (+))

$$M_{e}=0.72\left(7.25\times10^{6}\right)=5.22\times10^{6}lb-ms^{2}/in $$

Natural period $T_{N}=2\pi(M_{e}/K_{E})^{1/2}=2\pi(5,220,000/14,260)^{1/2}=120.2\ ms$ 

Behavior controlled by flexure. Use Step 6a.

Step 6a.

a.

$$\mathsf{T}/\mathsf{T}_{\mathsf{N}}=40/120.2=0.332$$

$$\frac{P}{r_{u}}=\frac{2.0\times144\times7}{1.215}=1.66$$

From Figure 3-64a (+),

$$\mu=X_{m}/X_{E}=1.6<4\quad O.K.$$

b.

$$X_{m}=1.6\times3.87=6.2\text{inches}$$

$$\tan\theta=X_{m}/(L/2)=6.2/(25\times12)=0.021$$

$$\Theta=1.2^{\circ}<2^{\circ}\quad O.K.$$

C.Check selection of DIF.

From Figure 3-64a (+), for.$\mu=1.6\mathrm{a n d}T/T_{N}=0.33$ 

$$t_{F}/T=0.65,\ t_{F}=0.65\times40=26\ ms I 
$$

Findε

$$Findε
\dot{\varepsilon}=f_{ds}/E_{s}t_{E}=65.45/30\times10^{3}\times0.026=0.117\ in/in/sec(Equation5-1)$$

From Figure 5-2 (+) (average of A36 and A514)

$DIF=1.18=1.19$ assumed 

O.K.

d.Check top chord as a beam column.

Maximum moment at mid-span 

<!-- batch 30 | page 5 -->

$$M=\frac{r_{u}L^{2}}{8}=\frac{1.105\times50^{2}\times12}{8\times1000}=4.144in-kips $$

Maximum axial load in chords 

$$P=M/d $$

$$\begin{array}{r}{d=\mathsf{d i s t a n c e b e t w e e n c e n t r o i d s o f t o p a n d b o t t o m c h o r d s}}\\ {(\mathsf{s e e F i g u r e5A-4(\underline{{+}})})}\end{array}$$

$$30.22inchees $$

$$P=4.144/30.22=137.1\mathrm{kips}$$

$$I=\mathrm{panel}\mathrm{length}=51\mathrm{inches}$$

Slenderness ratio,$I/r_{x}=51/0.92=55.4<C_{c}$ 

where $C_{c}=(2\pi^{2}E/f_{d s})^{1/2}=95$ 

$$F_{a}=23.5\ \mathrm{ksi}\ \mathrm{for}\ f_{v}=50\ \mathrm{ksi}$$

(AISC Specification)

$$1.31\ (23.5)=30.8\ \mathrm{ksi}\ \mathrm{for}\ f_{ds}=65,450\ \mathrm{psi}$$

$$P_{u}=1.7AF_{a}=1.7\times3.56\times30.8=186.4\ kips $$

Considering the first panel as a fixed, simply supported beam, the maximum moment in the panel is 

$$M=\frac{r_{u}L^{2}}{12}=\frac{1105\times51^{2}}{12\times12\times1000}=19.96in-kips $$

The effective slenderness ratio of the top chord in the first panel is 

$$K I_{b}/r_{x}=(1.0\times51)/0.92=55.4$$

$$F_{ex}=\frac{12\pi^{2}E}{23\left(KI_{b}/r_{x}\right)^{2}}=\frac{12\pi^{2}\times29.000}{23\times55.4^{2}}=48.7\ \mathrm{ksh}$$

$$P_{ex}=(23/12)AF_{ex}=23/12\times3.56\times48.7=333kips $$

$$(1-P/P_{e x})=(1.0-126.6/333)=0.62$$

To determine $M_{m},$ the plastic moment $M_{P}$ is needed and the value of $Z_{x}$ has to be computed. The neutral axis for a fully plastic section is located at a distance x from the flange.



<!-- batch 30 | page 6 -->

$$\begin{aligned}3\overline{x}&=\left(3-\frac{5}{16}\right)\frac{5}{16}+3\left(\frac{5}{16}-\overline{x}\right)\\&=\left(43\times5\right)/\left(16\times16\right)+15/16-3\overline{x}\\\overline{x}&=455/\left(6\times256\right)=0.296\mathrm{inch}\end{aligned}$$

The plastic section modulus,$Z_{x},$ is found to be 

$$Z_{x}=2\left[\frac{0.296^{2}}{2}\times3+(3.0-0.3125)\times\frac{(0.3125-0.296)^{2}}{2}+\frac{(3-0.296)^{2}}{2}\times0.3125\right]$$

$$M_{px}=f_{ds}Z_x=65.45\times2.549=166.8\ in-kips $$

$$M_{mx}=\left[1.07-\frac{\left(I/r_y\right)f_{ds}^{1/2}}{3160}\right]M_{px}\leq M_{px}$$

$$\begin{aligned}&\mathrm{where}\ r_{y}\ \mathrm{is\ least\ r\_a\_\_\_\_\_\_\_\_\_\_\_}\\ &=[1.07-(55.4/391)]\ 166.8=154.8\ \mathrm{in\_kips}\\ &C_{m}=0.85\ \mathrm{(AlSC\_Specifically)}\\ &\mathrm{(P/P_{u}+C_{m}M/[(1-P/P_{ex})M_{mx}]\leq1.10\ (Equation\ 5-44))}\\ &\mathrm{(\frac{137.1}{186.4}+\frac{0.85\times19.96}{0.62\times154.8}\leq1.0=0.736+0.176=0.912<1.0\ \mathrm{O.K}}\\ \end{aligned}$$

Step 7.Check bottom chord for rebound.

a.Calculate required resistance in rebound.

$$\mathsf{T}/\mathsf{T}_{\mathsf{N}}=0.33$$

From Figure 5-13 (+), 100% rebound 

$$\begin{aligned}&\bar{r}/r_{u}=1.0\\&\bar{r}=r_{u}=1.105\mathrm{lb/ft}\\ \end{aligned}$$

b.Moment and axial forces in rebound 

$$M=\frac{\overline{r}L^{2}}{8}=4,144\ln-\mathrm{kips}$$

Maximum axial force in bottom chord 

$$P=M/d=137.1\;\mathrm{k i p s}\;(\mathrm{c o m p r e s s i o n})$$

<!-- batch 30 | page 7 -->

C.Ultimate axial load capacity 

Stability in vertical direction (about x-axis)

$$I=51inchees\quad r_x=0.945$$

$$I/r=51/0.945=54.0<C_{c}$$

$$where$C_{c}=[(2\pi^{2}E)/f_{d s}]^{1/2}=\;95$ $$

$$F_{a}=23.72\ \mathrm{ksi}\ \mathrm{for}\ f_{v}=50\ \mathrm{ksi}\ \mathrm{(AlSC\_specification)}$$

$$1.31(23.72)=31.1\ \mathrm{ksi}\ \mathrm{for}\ f_{ds}=65,450\ \mathrm{psi}$$

$$P_{u}=1.7AF_{a}=1.7\times2.62\times31.1=138.5\ kips $$

d.Check bracing requirements.

$$P=137.1<P_u=138.5\quad0.K.$$

Adding a vertical member between panel joints of bottom chord would have been required had $P>P_{u}$ . This additional bracing would have been needed in mid-span but may be spared at the  joist ends.



Stability in the lateral direction (about y-axis)

$$P_{u}=137.1\ kips $$

$$r_{v}=1.28\ inches,\quad A=2.62\ in^{2}$$

$$F_{a}=P_{u}/(1.7\times1.31A)=137.1/(1.7\times1.31\times2.62)=23.5\mathrm{ksi}$$

For a given $F_{a}=23.5$ , the corresponding slenderness ratio is 

$$1/r\approx55$$

(AISC Specification)

Therefore, the maximum unbraced length in mid-span is 

$$J_{b}=55\times1.28=70.4inches $$

Use lateral bracing at panel points, i.e., 51 inches at midspan. The unbraced length may be increased at joist ends, but not greater than specified for bridging requirements in the joist specification.

<!-- batch 30 | page 8 -->

EXAMPLE 5A-5 (B)ANALYSIS OF EXISTING OPEN-WEB STEEL JOIST 

Required:Analyze a simply supported, open-web steel joist whose capacity is controlled by shear.



## Solution:

Step 1.Given:

a.Pressure-time loading [Figure 5A-5 (+)]

Joist 22H11

b.Clear span = 32'-0"

Spacing of joists = 6'-0"

Weight of decking = 4 psf 

Figure 5A-5 Joist Cross-Section and Loading, Example 5A-5(b)

<div style="text-align: center;"><img src="../pages/batch 30/imgs/img_in_image_box_251_744_919_1211.jpg" alt="Image" width="56%" /></div>


C.Properties of structural steel:

Chords 

Web 

$$f_{y}=50,000\;\mathrm{p s i}$$

Dynamic increase factor 

(chords only)

$DIF=1.19$ (Table 5-2 (+) for A588)

Dynamic design stress $\boldsymbol{f}_{d s}=\boldsymbol{D I F}\times\boldsymbol{S I F}\times\boldsymbol{f}_{v}$ 

<!-- batch 30 | page 9 -->

Chords 

$$f_{ds}=1.19\times1.1\times50,000=65,450\mathrm{psi}$$

d.Design criteria 

(Section 5-35)

For members controlled by shear:

$$\begin{aligned}&\mu_{max}=1.0\\&\varTheta_{max}=1^{\circ}\\ \end{aligned}$$

Step 2.

a.Assume the $\mathsf{D L F}=1.25$ 

b.Overpressure load on joist 

$$w_{1}=1.25\times1.0\times144\times6=1.080\mathrm{~lb}/\mathrm{ft}$$

C.Equivalent service load 

$$w_{2}=w_{1}/1.7\times SIF\times DIF=1.080/2.23=485\ lb/ft $$

d.From the "Standard Specifications and Load Tables" of the Steel Joist Institute:

Total allowable load capacity (including dead load) = 506 Ib/ft.

Approximate weight of joist plus decking =

$$17+(6\times4)=41\ lb/ft $$

Total allowable load capacity (excluding dead load) =

$$506-41=465$$

From the steel joist catalog, the following are the section properties of Joist 22H11 (Figure 5A-5 (+)):

Panel length = 24 inches 

Top Chord:

$$\begin{aligned}&A=1.935in^2\\&I_x=0.455in^4\\&r_x=0.485in^4\\&r_y=1.701in^4\\ \end{aligned}$$

Bottom Chord:

$$A=1.575\mathrm{i n}^{2}$$

<!-- batch 30 | page 10 -->

$$\begin{aligned}&I_{x}=0.388\;in^{4}\\&r_{x}=0.497\;in\\&r_{y}=1.469\;in\\&I_{xx}\;for\;joist=396.0\;in^{4}\\ \end{aligned}$$

Step 3.Resistance per unit length 

$$r_{u}=2.23\times465=1,035\text{lb/ft}$$

Step 4.

$$K_{E}=\frac{384EI}{5L^{3}}=\frac{384\times29\times10^{6}\times396}{5\times(12\times32)^{3}}=15.580\ lb/m $$

$$X_{E}=\frac{r_{u}L}{K_{E}}=\frac{1035\times32}{15580}=2.13inches $$

Step 5.Mass of joist plus decking 

$$M=\frac{41\times32\times10^{6}}{386}=3.4\times10^{6}\mathrm{~lb}-\mathrm{ms}^{2}/\mathrm{in}$$

Effective mass $M_{e}=K_{L M}M$ 

$$0.78\times3.4\times10^{6}=2.65\times10^{6}\mathrm{~lb}-\mathrm{ms}^{2}\mathrm{ln}$$

Natural period $T_{N}=2\pi(M_{e}/K_{E})^{1/2}$ 

$$2\pi(2650000/15580)^{1/2}=81.8\ ms $$

Behavior controlled by shear. Use Step 6b of the procedure.

Step 6b.

a.

$$\begin{aligned}&T/T_{N}=25/81.8=0.305\\ &\frac{P}{r_{u}}=\frac{6\times144\times1.0}{1.035}=0.835\\ \end{aligned}$$

b.From Figure 3-64a (+) of Chapter 3:

$$\mu=X_{m}/X_{E}<1.0;elastic,O.K.$$

$$\begin{aligned}\tan\theta&=X_{m}/(L/2)\\&=2.13/(16.0\times12)=0.0111\end{aligned}$$

$$\Theta=0.64^{\circ}<1^{\circ}\quad\text{O.K.}$$

<!-- batch 30 | page 11 -->

C.Check selection of DIF from Figure 3-49 (+) of Chapter 3, for 

$T/T_{N}=0.305,\;t_{m}/T=1.12;\;t_{m}=1.12\times25=28\;ms$ 

Find ε

$$\dot{\varepsilon}={{f_{d s}}\mathord{\left/{\vphantom{{f_{d s}}{E_{s}}{t_{E}}}}\right.}{E_{s}}{t_{E}}}\qquad\left({{t_{E}}={t_{m}}}\right)$$

(Equation 5-1)

$$65.45/30\times10^{3}\times0.028=0.078in/in/sec $$

From Figure 5-2 (+) (average of A36 and A514)

DIF = 1.18 = 1.19 assumed, O.K.

d.Check of top chord as a beam-column is not necessary.

Check bottom chord in rebound.

a.For $\mu=1$ and $T/T_{N}=0.305$ ,rebound is 100%(Figure 5-13 (+))

$\overline{{r}}=r_{u}$ 



b.Determine axial load in bottom chord,$P=M/d$ 

For an elastic response,$\mu\leq1.0$ ,where $T/T_{N}=0.305$ the $\mathsf{DLF}=0.87$ (Figure 3-49 (+))Equivalent static load, w 

$$w=\mathrm{DLF}\times b\times p=0.87\times12\times12\times6\times1.0=751\ \mathrm{lb/ft}$$

Maximum moment in rebound,$M=w L^{2}/8$ 

$$M=[751\times(32)^2/8]\times12=1,155,000in-lb $$

$$P=M/d=1,155,000/21.28=54,300\;lb=54.3\;kips $$

C.Check bracing requirements.

(1)Vertical bracing of bottom chord:

Panel length = 24 inches 

$$r_{x}=0.497,r_{y}=1.469,A=1.575\mathrm{i n}^{2}$$

$$I/r_{x}=24/0.497=48.3$$

Allowable $P=1.7\times S I F\times D I F\times A\times F_{a}$ 

$$1.7\times1.1\times1.19\times1.575\times24.6=86.2kips>54.3kips $$

(Fa from AISC Specification)

No extra bracing required.

<!-- batch 30 | page 12 -->

(2)Lateral bracing of bottom chord:

$$P=54.3kips,A=1.575i n^2$$

$$F_{a}=P/1.7A=54.3/(1.7\times1.575\times1.1\times1.19)=15.5\ \mathrm{ksi}$$

For $f_{v}=50\ \mathrm{ksi}\ \mathrm{and}\ F_{a}=15.5$ ksi 

$$1/r=96$$

$$J=96\times1.469=141in these $$

(1/r from AISC Specification)

Therefore, use lateral bracing at every fifth panel point close to midspan. The unbraced length may be increased at joist ends, but not greater than specified for bridging requirements in the joist specification.



<!-- batch 30 | page 13 -->

# PROBLEM 5A-6DESIGN OF SINGLE-STORY RIGID FRAMES FOR PRESSURE TIME LOADING 

Problem:Design a single-story, multi-bay rigid frame subjected to a pressuretime loading.



## Procedure:

Step 1.Establish the ratio α between the design values of the horizontal and vertical blast loads.



Step 2.Using the recommended dynamic load factors presented in Section 5-41.3establish the magnitude of the equivalent static load w for:

a.Local mechanisms of the roof and blastward column 

b.Panel or combined mechanisms for the frame as a whole.

Step 3.Using the general expressions for the possible collapse mechanisms from Table 5-13 (+) and the loads from Step 2, assume values of the moment capacity ratios C and $C_{1}$ and proceed to establish the required design plastic moment $M_{P}$ considering all possible mechanisms. In order to obtain a reasonably economical design, it is desirable to select C and $C_{1}$ so that the least resistance (or the required value of $M_{p})$ corresponds to a combined mechanism. This will normally require several trials with assumed values of C and $C_{1}$ 



Step 4.Calculate the axial loads and shears in all members using the approximate method of Section 5-41.4.



Step 5.Design each member as a beam-column using the ultimate strength design criteria of Sections 5-37.3, 5-38, and 5-39.A numerical example is presented in Problem 5A-4.



Step 6.Using the moments of inertia from Step 5, calculate the sidesway natural period using Table 5-14 (+) and Equations 5-50 and 5-51. Enter the response charts in Chapter 3 with the ratios of $T/T_{N}$ and $P/R_{u}$ . In this case,$P/R_{u}$ is the reciprocal of the panel or sidesway mechanism dynamic load factor used in the trial design. Multiply the ductility ratio by the elastic deflection given by Equation 5-53 and establish the peak deflection $X_{m}$ from Equation 5-54. Compare the maximum sidesway deflection $X_{m}$ ih the criteria of Section 5-35. Note that the sidesway deflection δin Table 58$(+)$ ,is $X_{m}$ ..1.



Step 7.Repeat the procedure of Step 6 for the local mechanisms of the roof and blastward column. The stiffness and natural period may be obtained from Table 3-8 (+) of Chapter 3 and Equation 5-15, respectively. The resistance of the roof girder and the blastward column may be obtained from Table 5

<!-- batch 30 | page 14 -->

13 (+) using the values of $M_{P}$ and $C M_{p}$ determined in Step 3. Compare the ductility ratio and rotation with the criteria of Section 5-35.

## Step 8

a.If the deflection criteria for both sidesway and beam mechanisms are satisfied, then the member sizes from Step 5 constitute the results of this preliminary design. These members would then be used in a more rigorous dynamic frame analysis. Several computer programs are available through the repositories listed in Section 5-4.



b.If the deflection criterion for a sidesway mechanism is exceeded,then the resistance of all or most of the members should be increased.



C.If the deflection criterion for a beam mechanism of the front wall or roof girder is exceeded, then the resistance of the member in question should be increased. The member sizes to be used in a final analysis should be the greater of those determined from Steps 8b and 8c.



<!-- batch 30 | page 15 -->

## EXAMPLE 5A-6DESIGN OF A RIGID FRAME FOR PRESSURE-TIME LOADING 

Required:Design a four-bay, single-story, reusable, pinned-base rigid frame subjected to a pressure-time loading in its plane.

Given:

a.Pressure-time loading (Figure 5A-6 (+))

b.Design criteria: It is required to design the frame structure for more than one incident. The deformation limits shall be half that permitted for personnel protection, that is:

$$\delta=\mathsf{H}/50\;\mathrm{and}$$

$$\Theta_{max}=1^{\circ}for individual members $$

C.Structural configuration (Figure 5A-6 (+)

d.A36 steel 

e.Roof purlins spanning perpendicular to frame $(b_{v}=b_{n}$ ,Figure 5-26(+))



f.Frame spacing,$b=17f t$ 

g.Uniform dead load of deck, excluding frame 

Roof dead $\mathrm{l o a d}=\mathrm{w}_{\mathrm{d r}}=13.5$ psf 

Wall dead load = Wdw = 16.5 psf 

Step 1.$\begin{aligned}&\mathsf{Determine}\alpha\\&b_{h}=b_{v}=17\mathsf{ft}\\&q_{h}=5.8\times17\times12=1,183\mathsf{lb/in}\\&q_{v}=2.5\times17\times12=510\mathsf{lb/in}\\&\alpha=q_{h}/q_{v}=2.32\\ \end{aligned}$ 

$$\begin{aligned}&\mathsf{Determine}\alpha\\&b_{h}=b_{v}=17\mathsf{ft}\\&q_{h}=5.8\times17\times12=1,183\mathsf{lb/in}\\&q_{v}=2.5\times17\times12=510\mathsf{lb/in}\\&\alpha=q_{h}/q_{v}=2.32\\ \end{aligned}$$

(Section 5-41.1)

<!-- batch 30 | page 16 -->

Figure 5A-6 Preliminary Design of Four-Bay, Single-Story Rigid Frame,Example 5A-6

<div style="text-align: center;"><img src="../pages/batch 30/imgs/img_in_image_box_288_345_882_930.jpg" alt="Image" width="49%" /></div>


Step 2.Establish equivalent static loads 

(Section 5-41.3)

a.Local beam mechanism,$w=\mathsf{DLF}\times q_v$ 

$$w=\frac{1.25\times510\times12}{1000}=7.65\mathrm{k/ft}$$

b.Panel or combined mechanism,$w=\mathsf{D L F}\times q_{h}$ 

$$w=\frac{0.625\times510\times12}{1000}=3.83\mathrm{k/ft}$$

The required plastic moment capacities for the frame members are determined from Table $5-13(+)$ based upon rational assumptions for the moment capacity ratios $C_{1}$ and C. In general, the recommended starting values are $C_{1}$ equal to 2 and C greater than 2. From Table 5-13, for $n=4$ $\alpha=2.32,H=15.167$ ft,$L=16.5$ ft and pinned bases, values of $C_{1}$ and C were substituted and after a few trials, the following solution is obtained:

$$M_{p}=130\ \mathrm{kip-ft},\ C_{1}=2.0\ \mathrm{and}\ C=3.5.$$

<!-- batch 30 | page 17 -->

The various collapse mechanisms and the associated values of $M_{P}$ are listed below:


<div style="text-align: center;"><html><body><table border="1"><tr><td>Collapse Mechanism</td><td>w (k/ft)</td><td>(k-ft) $M_{p}$</td></tr><tr><td>1</td><td>7.65</td><td>130</td></tr><tr><td>2</td><td>7.65</td><td>128</td></tr><tr><td>3a,3b</td><td>3.83</td><td>128</td></tr><tr><td>4</td><td>3.83</td><td>129</td></tr><tr><td>5a, 5b</td><td>3.83</td><td>110</td></tr><tr><td>6</td><td>3.83</td><td>116</td></tr></table></body></html></div>


The plastic design moments for the frame members are established as follows:

Girder,$M_{0}=130\ k-ft$ 

Interior column,$C_{1}M_{p}=260\ k-ft$ 

Exterior column,$C M_{p}=455\mathrm{k-f t}$ 

Step 4.

a.Axial loads and shears due to horizontal blast pressure.

$w=3.83$ k/ft 

From Figure 5-27 (+),$R=a w H=2.32\times3.83\times15.167=135$ kips 

1.Member 1, axial load 

$$P_{1}=R/2=67\mathrm{k i p s}$$

2.Member 2, shear force 

$$V_{2}=R/2(4)=135/8=16.8\;\mathrm{k i p s}$$

3.Member 3, shear force 

$$V_{3}=R/2=67\;\mathrm{k i p s}$$

<!-- batch 30 | page 18 -->

b.Axial loads and shears due to vertical blast pressure,

$$w=7.65\;\mathrm{k/f t}$$

1.Member 1, shear force 

$$V_{1}=w\times L/2=7.65\times16.5/2=63.1\mathrm{~kips}$$

2.Member 2, axial load 

$$P_{2}=w\times L=7.65\times16.5=126.2\mathrm{~kips}$$

3.Member 3, axial load 

$$P_{3}=w\times L/2=63.1\mathrm{~kips}$$

Note:

The dead loads are small compared to the blast loads and are neglected in this step.



Step 5.

Step 6.

The members are designed using the criteria of Sections 5-37.3, 5-38, and 5-39 with the following results:


<div style="text-align: center;"><html><body><table border="1"><tr><td>Member</td><td>$M_{p}(k-f t)$</td><td>$P\left(\mathbf{k}\right)$</td><td>V(k)</td><td>Use</td><td>$I_{x}(\mathsf{i n}^{4})$</td></tr><tr><td>1</td><td>130</td><td>67.0</td><td>63.1</td><td>w12x35</td><td>285</td></tr><tr><td>2</td><td>260</td><td>126.2</td><td>16.8</td><td>w14x61</td><td>640</td></tr><tr><td>3</td><td>455</td><td>63.1</td><td>67.0</td><td>w14x74</td><td>796</td></tr></table></body></html></div>


Determine the frame stiffness and sway deflection.

$$\begin{aligned}&I_{ca}=\frac{(3\times640)+(2\times796)}{5}=702\ln^4\\ &I_g=285\ln^4\\ &\beta=0\\ &D=\frac{I/L_g}{0.75I_{ca}/H}=\frac{285/16.8}{0.75(702/15.167)}=0.498\\ &C_2=4.65\\ &K=\frac{EI_{ca}C_2}{H^3}[1+(0.7-0.1\beta)(n-1)]\\ \end{aligned}$$

<!-- batch 30 | page 19 -->

$$\begin{aligned}&=\frac{30×10^{3}×702×4.65×\left[1+0.7(3)\right]}{\left(15.167×12\right)^{3}}=50.2k/in\\&K_{L}=0.55\ (1\ -\ 0.25\beta)=0.55\ \quad(Equation\ 5-51)\\&\text{Calculate dead wicight,}W_{L}\\&W=b[(4Lw_{dr})+(1/3)\left(Hw_{dw}\right)]+(35×66)\\&\quad+1/3\ (15.167)\left[(3×61)+(2×74)\right]=20.548\ lb\\&m_{e}=W/g=20.548/32.2=638\ lb-set^{2}/t=638×10^{6}\ lb-ms^{2}/t\\&T_{N}=2\pi[m_{e}/KK_{L}]^{1/2}\quad(Equation\ 5-50)\\&\quad2\pi[m_{e}/K_{L}]^{1/2}\quad(50.2\ ×12×10^{3}×0.55)]^{1/2}=276\ ms\\&T/T_{N}=78/276=0.283\\&P/R_{u}=1.6\\&\mu=X_{m}/X_{E}=1.40\quad(Figure\ 3-54\ (\pm)\ or Figure\ 3-64a\ (\pm))\\&X_{E}=\frac{R_{u}}{K_{E}}=\frac{\alpha wH}{K_{E}}=\frac{2.32×3.83×15.167}{50.2}=2.68\ inches\\ \end{aligned}$$

(Equation 5-52 and 5-53)

$$X_{m}=\delta=1.40\times2.68=3.75\ inche $$

(Equation 5-54)

$$\delta=[3.75/(15.167\times12)]\times H=0.0206H=H/48.5$$

Step 7.Check deflection of possible local mechanisms.

a.Roof girder mechanism (investigate W12 × 35 from Step 5)

$$\begin{aligned}&T_{N}=2\pi\left(m_{e}/K_{E}\right)^{1/2}\\&m_{e}=K_{LM}\times m\\ \end{aligned}$$

For an elasto-plastic response, take the average load-mass factor for the plastic and elastic response, or:

$$K_{LM}=(0.77+0.66)/2=0.715$$

$$m=W/g $$

$$w=w_{dw}b+\mathrm{g}\mathrm{i}\mathrm{r}\mathrm{d}\mathrm{e}\mathrm{~s}\mathrm{~l}\mathrm{b}\mathrm{~w}\mathrm{~s}\mathrm{~l}\mathrm{b}\mathrm{~h}\mathrm{~t}=(13.5\times17)+35=265\mathrm{~lb}/\mathrm{ft}$$

$$W=w\times L=265\times16.5=4372lb $$

$$m_{F}=0.715\times4372/386.4=8.1\mathrm{~lb}-\mathrm{sec}^{2}/\mathrm{in}.$$

<!-- batch 30 | page 20 -->

UFC 3-340-025 December 2008Change 2,1 September 2014

$$\begin{aligned}&K_{E}=307\ E/I/L^{3}\\ &\quad K_{E}=\frac{307\times30\times10^{8}\times285}{\left(16.5\times12\right)^{3}}=332000\ lb/ln\\ &\quad T_{N}=2\pi\left(8.1/332000\right)^{1/2}\times1000=31.0\ ms\\ &\quad T/T_{N}=78/31.0=2.52\\ &\quad R_{u}=16M_{p}/L=(16\times130)/16.5=126\ kN\\ &\quad P=pbL=(2.5)\left(17\right)(144)\left(16.5\right)/1000=101\ kPa\\ &\quad P/R_{u}=10/126=0.80\\ &\quad\mu=\ X_{m}/X_{E}=1.80\quad(Figure3-54(\pm))\\ &\quad CK_{E}=R_{u}/K_{E}=126/332=0.380\ inch\\ &\quad X_{m}=1.80\times0.380=0.69\ inch\\ &\quad X_{m}/(L/2)=0.69/[(8.25)\left(12\right)]=0.0069=tan\ \Theta,\\ &\quad\Theta=0.40^{\circ}<1^{\circ}\quad\ \textcircled{O}\quad\textcircled{K}.\\ \end{aligned} \mu=X_{m}/X_{E}=1.80\quad(\mathrm{F i g u r e~3–54~(\pm)~o r~F i g u r e~3–64a~(\pm)}) s \mu=X_{m}/X_{E}=1.80\quad(\mathrm{F i g u r e~3–54~(\pm)~o r~F i g u r e~3–64a~(\pm)})$$

(Table 3-8 (+))

Exterior column mechanism (investigate $\mathsf{W}14\times74$ from Step 5).

$$\begin{aligned}&T_{N}=2\pi\left(m_{e}/K_{E}\right)^{1/2}\\ &m_{e}=K_{LM}×m=\frac{0.78+0.66}{2}×\frac{w}{g}\\ &\quad=0.72\frac{w}{g}\\ &w=\left(16.5×17\right)+74=354\ lb/th\\ &W=354×15.167=5369\ lb\\ &M_{e}=0.72\left(5369/386.4\right)=10.0\ lb-sec^{2}/in\\ &K_{E}=160\ E/L^{3}\\ &K_{E}=\frac{160×30×10^{6}×796}{182^{3}}=632,000\ lb/in\\ &T_{N}=2\pi(10.0/632,000)^{1/2}×1000=25.0\ ms\\ &T/T_{N}=78/25.0=3.12\\ \end{aligned}$$

<!-- batch 30 | page 21 -->

$$R_{u}=\frac{4M_{p}(2C+1)}{H}=\frac{4\times130\times[(2\times3.5)+1]}{15.167}=275\ kips(Table5-13(\pm))$$

$$P=(2.32)(7.65/1.25)(15.167)=215kips $$

$$P/R_{u}=215/275=0.78$$

$$\mu=X_{m}/X_{E}=1.80\quad(\mathrm{F i g u r e~3–54~(+)~o r~F i g u r e~3–64a~(+)})$$

Check end rotation of columns.

$$X_{F}=R_{u}/K=275/632=0.435\ inch $$

$$X_{m}=1.80\times0.435=0.78\text{inch}$$

$$X_{m}/(L/2)=0.78/[(7.58)(12)]=0.0086=\tan\theta $$

Step 8.

$$\Theta=0.49^{\circ}<1^{\circ}\quad O.K.$$

The deflections of the local mechanisms are within the criteria. The sidesway deflection is acceptable.



Summary:The member sizes to be used in a computer analysis are as follows:


<div style="text-align: center;"><html><body><table border="1"><tr><td>Member</td><td>Size</td></tr><tr><td>1</td><td>$\mathsf{W12}\times\mathsf{35}$</td></tr><tr><td>2</td><td>$\mathsf{W14\times61}$</td></tr><tr><td>3</td><td>$\mathsf{W}14\times74$</td></tr></table></body></html></div>


<!-- batch 30 | page 22 -->

## PROBLEM 5A-7DESIGN OF DOORS FOR PRESSURE-TIME LOADING 

### Problem:Design a steel-plate blast door subjected to a pressure-time loading.Procedure:

Step 1.Establish the design parameters 

a.Pressure-time load 

b.Design criteria: Establish support rotation,$\varTheta_{m a x}$ ,and whether seals and rebound mechanisms are required 

C.Structural configuration of the door including geometry and support conditions 



d.Properties of steel used:

Minimum yield strength,$\pmb{f}_{y}$ , for door components (Table 5-1 (+))

Dynamic increase factor, DIF (Table 5-2 (+))Step 2.Select the thickness of the plate.

Step 3.Calculate the elastic section modulus, S, and the plastic section modulus,Z, of the plate.



Step 4.Calculate the design plastic moment,$M_{p},$ of the plate (Equation 5-7)

Step 5.Compute the ultimate dynamic shear,$V_{p}$ 

Step 6.Calculate maximum support shear, V, using a dynamic load factor of 1.25and determine $V/V_{p}$ .lf $V/V_{p}$ is less than 0.67, use the plastic design moment as computed in Step 4 (Section 5-31). If $V/V_{p}$ is greater than 0.7,use Equation 5-23 to calculate the effective $M_{P}$ 



Step 7.Calculate the ultimate unit resistance of the section (Table 3-1$(\pm))$ __,using the equivalent plastic moment as obtained in Step 4 and a dynamic load factor of 1.25.



Step 8.Determine the moment of inertia of the plate section.

Step 9.Compute the equivalent elastic unit stiffness,$K_{E}$ , of the plate section.

(Table 3-8 (+))

Step 10.Calculate the equivalent elastic deflection,$X_{E}$ , of the plate as given by $X_{E}=r_{u}/K_{E}$ :

Step 11.Determine the load-mass factor $K_{L M}$ and compute the effective unit mass,

$m_{e}$ 



Step 12.Compute the natural period of vibration,$T_{N}$ 

<!-- batch 30 | page 23 -->

Step 13.Determine the door plate response using the values of $P/r_{u}$ and $T/T_{N}$ and the response charts of Chapter 3. Determine $X_{m}/X_{E}$ and $T_{E}$ 

Step 14.Determine the support rotation,

tan $\Theta=(X_{m})/(L/2)$ 

Compare  with the design criteria of Step 1b.

Step 15.Determine the strain rate, ε, using Equation 5-1. Determine the dynamic increase factor using Figure 5-2 (+) and compare with the DIF selected in Step 1d.



If the criteria of Step 1 is not satisfied, repeat Steps 2 to 15 with a new plate thickness.



Step 16.Design supporting flexural element considering composite action with the plate (if so constructed).



Step 17.Calculate elastic and plastic section moduli of the combined section.

Step 18.Follow the design procedure for a flexural element as described in Section 5A-1.



<!-- batch 30 | page 24 -->

## EXAMPLE 5A-7 (A)DESIGN OF A BLAST DOOR FOR PRESSURE-TIME LOADING 

Required:Design a double-leaf, built-up door (6 ft by 8 ft) for the given pressure-time loading.



### Step 1.Given:

a.Pressure-time loading 

(Figure 5A-7 (+))

b.Design criteria: This door is to protect personnel from exterior loading. Leakage into the structure is permitted but the maximum end rotation of any member is limited to $2^{\circ}$ c 

C.Structural configuration (Figure 5A-7 (+))

Note:

This type of door configuration is suitable for low-pressure range applications.



d.Steel used:A36

Figure 5A-7 Door Configuration and Loading, Example 5A-7(a)

<div style="text-align: center;"><img src="../pages/batch 30/imgs/img_in_image_box_213_806_984_1317.jpg" alt="Image" width="64%" /></div>


Yield strength,$f_{y}=36$ ksi (Table 5-1 (+))Dynamic increase factor,$DIF=1.29$ (Table 5-2 (+))Average yield strength increase factor,$S I F=1.1$ (Section 5-12.1)Hence, the dynamic design stress,

<!-- batch 30 | page 25 -->

$$f_{ds}=1.1\times1.29\times36=51.1\mathrm{ksi}$$

and the dynamic yield stress in shear,

$$f_{dv}=0.55f_{ds}=0.55\times51.1=28.1\mathrm{ksi}$$

Step 2.Assume a plate thickness of 5/8 inch.

Step 3.Determine the elastic and plastic section moduli (per unit width).

$$\frac{bd^{2}}{6}=\frac{1\times(5/8)^{2}}{6}=6.515\times10^{-2}\ln^{3}/\ln^{2}$$

Step 4.Calculate the design plastic moment,$M_{p}$ 

$$\begin{aligned}&M_{p}=f_{ds}\left(S+Z\right)/2=51.1\left[\left(6.515\times10^{-2}\right)\right.\\ &\left.\quad+\left(9.765\times10^{-2}\right)\right]/2=51.1\times8.14\times10^{-2}=4.16\ in-k/in\\ \end{aligned}$$

Step 5.Calculate the dynamic ultimate shear capacity,$V_{p},$ ,for a 1-inch width.

$$V_{p}=f_{dv}A_{w}=28.1\times1\times5/8=17.56\ kips/in $$

Step 6.Evaluate the support shear and check the plate capacity. Assume 

$D L F=1.25$ 



$$V=DLF\times P\times L/2=\frac{1.25\times14.8\times36\times1}{2}=333\ lb/in=0.333\ kPa/in $$

$$V/V_{p}=0.333/17.56=0.0190<0.67$$

No reduction in equivalent plastic moment is necessary.

Note:

When actual DLF is determined, reconsider Step 6.

Step 7.Calculate the ultimate unit resistance,$r_{u}$ , (assuming the plate to be simplysupported at both ends).



$$r_{u}=\frac{8M_{p}}{L^{2}}=\frac{8\times4.16\times10^{3}}{36^{2}}=25.7\ ps $$

Step 8.Compute the moment of inertia, 1, for a 1-inch width.

$$I=\frac{bd^{3}}{12}=\frac{1\times(5/8)^{3}}{12}=0.02035in^{4}/in $$

<!-- batch 30 | page 26 -->

Step 9.Calculate the equivalent elastic stiffness,$K_{E}$ 

$$K_{E}=\frac{384EI}{5bL^{4}}=\frac{384\times29\times10^{6}\times0.02035}{5\times1\times36^{4}}=27.0\mathrm{psi/in}$$

Step 10.Determine the equivalent elastic deflection,$X_{E}$ 

$$X_{F}=r_{u}/K_{F}=25.7/27.0=0.95\ inch $$

Step 11.Calculate the effective mass of element.

$$\begin{array}{r l r}{\mathsf{a.}}&{}&{K_{L M}(\mathsf{a v e r a g e\;e l a s t i c\;a n d\;p l a s t i c})}\\ &{}&{=(0.78+0.66)/2=0.72}\end{array}$$

b.Unit mass of element, m 

$$m=\frac{w}{g}=\frac{5/8\times1\times1\times490\times10^{6}}{1728\times32.2\times12}=458.0\mathrm{~ps}i-\mathrm{ms}^{2}/\mathrm{in}$$

C.Effective unit of mass of element,$m_{e}$ 

$$m_{e}=K_{LM}m=0.72\times458.0$$

Step 12.Calculate the natural period of vibration,$T_{N}$ 

$$T_{N}=2\pi\left(330/27.0\right)^{1/2}=22\mathrm{m s}$$

Step 13.Determine the door response.

Peak overpressure $P=14.8\mathrm{psi}$ 

Peak resistance $r_{u}=25.7\mathrm{p s i}$ 

Duration 

$$T=13.0ms $$

Natural period of vibration $T_{N}=22~\mathrm{m s}$ 

$$P/r_{u}=14.8/25.7=0.58\quad\mathrm{~}\quad T/T_{N}=13.0/22.0=0.59$$

From Figure 3-64a (+) of Chapter 3,

$$X_{m}/X_{F}<1$$

Since the response is elastic, determine the DLF from Figure 3-49$(\pm)$ of Chapter 3.



$$\mathrm{DLF}=1.3\mathrm{for}T/T_N=0.59$$

<!-- batch 30 | page 27 -->

Step 14.Determine the support rotation.

$$X_{m}=\frac{1.3\times14.8\times0.95}{25.7}=0.713\text{inch}$$

$$\tan\Theta=X_{m}/(L/2)=0.713/(36/2)=0.0396$$

$$\Theta=2.27^{\circ}>2^{\circ}\quad N.G.$$

Step 15.Evaluate the selection of the dynamic increase factor.

Since this is an elastic response, use Figure 3-49 (b) (+) of Chapter 3 to determine $t_{m}$ . For $T/T_{N}=0.59,\;t_{m}/T=0.7\;and\;t_{m}=9.1\;ms$ i. The strain rate is:

$$\dot{\varepsilon}=\dot{t}_{d s}/\dot{E}_{s}\dot{t}_{E}$$

(Equation 5-1)

Since the response is elastic,

$$f_{ds}=51.1\times\frac{X_m}{X_E}=51.1\times\frac{0.713}{0.95}=38.4\mathrm{ksi}$$

and $t_{E}=t_{m}=0.0091\mathrm{s e c}$ .Hence,

$$\dot{\varepsilon}=\frac{38.4}{29.6\times10^{3}\times0.0091}=0.142\mathrm{~in}/\mathrm{~se}/\mathrm{~se}$$

Using Figure $5-2(+),DIF=1.31$ . The preliminary selection of $DIF=1.29$ is acceptable.



Since the rotation criterion is not satisfied, change the thickness of the plate and repeat the procedure. Repeating these calculations, it can be shown that a 3/4-inch plate satisfies the requirements.

Step 16.Design of the supporting flexural element.

Assume an angle $\mathsf{L4\times3\times1/2}$ and attached to the plate as shown in Figure 5A-8 (+).



Determine the effective width of plate which acts in conjunction with the angle 



$$b_{f}/2t_{f}<8.5$$

where $b_{f}/2$ is the half width of the outstanding flange or overhang and tf is the thickness of the plate.



With $t_{f}=3/4\ inch,\ b_{f}/2<8.5\times3/4,\ i.e.,\ 6.38\ inches$ 

Use overhang of 6 inches.

<!-- batch 30 | page 28 -->

Hence, the effective $\mathrm{width}=6+2=8$ inches.The angle together with plate is shown in Figure 5A-8 (+)



Step 17.Calculate the elastic and plastic section moduli of the combined section.Let y be the distance of c.g. of the combined section from the outside edge of the plate as shown in Figure 5A-8 (+), therefore 

$$\bar{y}=\frac{\left(8\times3/4\times3/8\right)+\left(4+3/4-1.33\right)\times3.25}{\left(8\times3/4\right)+3.25}=1.445\ inche $$

Let $y_{p}$ be the distance to the N.A. of the combined section for full plasticity 

$$\begin{aligned}&y_{p}=\frac{1}{8\times2}\left[\left(8\times3/4\right)+3.25\right]=0.578\text{inch}\\ &\quad I=\frac{8\times\left(3/4\right)^{3}}{12}+8\times3/4\times\left(1.45-3/8\right)^{2}\\ &\quad+5.05+3.25\times\left(4.75-1.33-1.45\right)^{2}=24.88\text{in}^{4}\\ &\text{Hence,}S_{min}=24.881/(4.75-1.445)=7.54\text{in}^{3}\\ &\quad Z=8\left(0.578\right)^{2}/2+8\left(0.75-0.578\right)^{2}/2\\ &\quad+3.25\left(4.75-1.33-0.578\right)=10.69\text{in}^{3}\\ \end{aligned}$$

Figure 5A-8 Detail of Composite Angle/Plate Supporting Element,Example 5A-7(b)



<div style="text-align: center;"><img src="../pages/batch 30/imgs/img_in_image_box_332_1018_847_1330.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">Step 18.Follow the design procedure for the composite element using Steps 4through 13. Calculate the design plastic moment $M_{P}$ of the supporting flexural element. </div>


$$M_{p}=51.1\ (7.54+10.69)/2=465.8\ in-kips $$

<!-- batch 30 | page 29 -->

Calculate the ultimate dynamic shear capacity,$V_{p}$ .

$$V_{p}=f_{dv}A_{w}=28.1\left(4.0-1/2\right)1/2=49.2\ kips $$

Calculate support shear and check shear capacity.

Calculate the ultimate unit resistance,$r_{u}$ 

Assuming the angle to be simply supported at both ends:

$$r_{u}=8M_{p}/L^{2}=(8\times465.8\times1000)/(96)^{2}=405\ lb/in $$

Calculate the unit elastic stiffness,$K_{E}$ 

$$K_{E}=\frac{384EI}{5L^{4}}=\frac{384\times29\times10^{6}\times24.881}{5\times96^{4}}=652.51b/in^{2}$$

Determine the equivalent elastic deflection,$X_{E}$ 

$$X_{F}=r_{u}/K_{F}=405/652.5=0.620\ inch $$

Calculate the effective mass of the element using the full width of plate over the 18 inch wide blast-loaded area.



$$K_{L M}=0.72$$

$$w=\frac{11.1}{12}+\frac{3}{4}\times18\times\frac{490}{1728}=(0.925+3.825)=4.750\ lb/in $$

Effective unit mass of element,

$$m_{e}=0.72\times\frac{4.75\times10^{6}}{32.2\times12}=0.89\times10^{4}\mathrm{~lb}-\mathrm{ms}^{2}/\mathrm{in}^{2}$$

Calculate the natural period of vibration,$T_{N}.$ 

$$T_{N}=2\pi[(89\times10^{2})/652.5]^{1/2}=23.2\ ms $$

Determine the response parameters. (Figure 3-54 (+) or Figure 3-64a (+)

$$\mathrm{P}\mathrm{e}\mathrm{a}\mathrm{k}\ \mathrm{o}\mathrm{v}\mathrm{e}\mathrm{p}\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{s}\mathrm{u}\mathrm{r}\mathrm{e}\ \mathrm{p}=14.8\times36/2=266.5\mathrm{~lb}/\mathrm{in}$$

Peak resistance $r_{u}=405\mathrm{{I b/i n}}$ 

Duration 

$$T=13.0ms $$

Natural period of vibration,$T_{N}=23.2\mathrm{m s}$ 

$$P/r_{u}=266.5/405=0.658$$

$$T/T_{N}=13/23.2=0.56$$

<!-- batch 30 | page 30 -->

From Figure 3-64a (+),

$$\mu=X_{m}/X_{E}<1$$

From Figure 3-49 (+) for $T/T_{N}=0.56$ 

$$\mathsf{D L F=1.28}$$

$$\mathrm{Hence},X_{m}=\frac{1.28\times14.8\times36/2}{652.5}=0.522\mathrm{in}$$

$$\tan\Theta=X_{m}/(L/2)=0.522/48=0.0109$$

$$\Theta=0.69^{\circ}<2^{\circ}\quad0.K.$$

Calculate support shear (V) and check shear capacity.

$$L=8^{\circ}-0=96inchees $$

$$\begin{aligned}&V=(P\times DLF\times36/2\times L)/2\\ &V=(14.8\times1.28\times36/2\times96)/2=16367\quad lb=16.37\quad kips<V_p\quad O.K.\\ \end{aligned}$$

Check stresses at the connecting point.

$$\sigma=M y/I=392\times10^{3}\times(1.445-0.75)/24.881$$

$$=10950\mathrm{ps}\mathrm{i}\mathrm{where}\left(M=\frac{X_m}{X_E}\times M_p=\frac{0.522}{0.62}\times466=392\right)$$

$$\frac{VQ}{Ib}=\frac{16.37\times10^{3}\times8\times3/4\times(1.445-0.75/2)}{24.881\times1/2}=8.500\mathrm{ps}i $$

Effective stress at the section of connecting point 

$$(\sigma^{2}+\tau^{2})^{1/2}=10^{3}\times(10.5.^{2}+8.5.^{2})^{1/2}=13.860\mathrm{p s i}<39.600\mathrm{p s i}\quad\mathrm{O.K.}$$

<!-- batch 30 | page 31 -->

# EXAMPLE 5A-7 (B)DESIGN OF A PLATE BLAST DOOR FOR PRESSURE-TIME  LOADING 

Required:Design a single-leaf door (4 ft by 7 ft) for the given pressure-time loading.



Step 1.Given:

a.Pressure-time loading [Figure 5A-9 (+)]

b.Design criteria: Door shall be designed to contain blast pressures from an internal explosion. Gasket and reversal mechanisms shal be provided. Support rotation shall be limited to 3°

<!-- batch 30 | page 32 -->

Figure 5A-9 Door Configuration and Loading, Example 5A-7(b)

<div style="text-align: center;"><img src="../pages/batch 30/imgs/img_in_image_box_166_313_1004_802.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">PLAN/SECTION </div>


## Legend:

A-Steel frame embedded in concrete 

B-Steel sub-frame 

C-Reversal bolt housing 

D Reversalbolt 

E-Blast door plate 

F-Continuous gasket 

G-Continuous bearing block 



<div style="text-align: center;"><img src="../pages/batch 30/imgs/img_in_chart_box_302_1172_777_1466.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">5A-58</div>


<!-- batch 30 | page 33 -->

C.Structural configuration (see Figure 5A-9 (+))

Note:

This type of door is suitable for high pressure range applications.

d.Steel used: ASTM A588

Yield strength,$f_{v}=50\mathrm{k s i}$ 

Dynamic increase factor,$DIF=1.24$ (preliminary, Table 5-2 (+))

Average strength increase factor,$S I F=1.1$ (Section 5-12.1)

Hence, the dynamic design stress,

$$f_{ds}=1.1\times1.24\times50=68.2\mathrm{ksi}$$

Note:

It is assumed, for the limited design rotation of $3^{\circ}$ ,that $\mu<10$ ,and,therefore, that Equation 5-3 does not govern.



The dynamic design stress in shear 

$$f_{dv}=0.55f_{ds}=37.5\mathrm{ksi}$$

Step 2.Assume a plate thickness of 2 inches 

Step 3.Determine the elastic and plastic section moduli (per unit width)

$$\begin{aligned}&S=\frac{bd^{2}}{6}=\frac{1\times2^{2}}{6}=0.667\ln^{3}/\ln^{3}\\ &Z=\frac{bd^{2}}{4}=\frac{1\times2^{2}}{4}=1.0\ln^{3}/\ln\\ \end{aligned}$$

Step 4.Calculate the design plastic moment,$M_{P}$ 

$$M_{p}=f_{ds}(S+Z)/2=68.2(0.667+1.0)/2=56.8\mathrm{in}-\mathrm{k/in}$$

Step 5.Calculate the dynamic ultimate shear capacity,$V_{p},$ ,for a 1-inch width.

$$V_{p}=f_{dv}A_{w}=37.5\times2=75.0\ kips/in $$

Step 6.Evaluate the support shear and check the plate shear capacity.

Assume $\mathsf{D L F}=1.0$ 

For simplicity, assume the plate is a one-way member, hence:

$$V=DLF\times P\times L/2=1.0\times1100\times48/2=26.400\;lb/in $$

$=26.4$ kips/in 

<!-- batch 30 | page 34 -->

$$V/V_{p}=26.4/75.=0.352<0.67$$

No reduction in equivalent plastic moment is necessary.

Calculate the ultimate unit resistance,$r_{u}$ ,

For a plate, simply-supported on four sides (direct load)

$$r_{u}=5M_{p}/X^{2}$$

where $M_{HP}=M_{p}and M_{HN}=0and$ 

$$\frac{X}{L}=0.35\mathrm{for}\frac{L}{H}=1.75$$

thus,$X=0.35\times12\times7=29.4$ 

$$r_{u}=5\times56.8/(29.4)^{2}=329\mathrm{psi}$$

Step 8.Compute the moment of inertia, 1, for a 1-inch width 

$$I=\frac{bd^{3}}{12}=\frac{1\times2^{3}}{12}=0.667\ln^{4}/\ln $$

Step 9.Calculate the equivalent elastic stiffness,$K_{E}$ 

$$K_{E}=r/\mathbf{x}=D/\gamma H^{4}$$

where 

$$\gamma=0.0083\qquad(\mathrm{for}\;H/L=0.57)$$

$$D=E I/[b(1-v^{2})]$$

$$D=29.6\times10^{6}\times0.667\left[\left[1\left(1-0.3^{2}\right)\right]=2.17\times10^{7}\right]$$

$$K_{E}=2.17\times10^{7}/0.0083\times48^{4}=492\mathrm{~ps}/\mathrm{in}$$

Step 10.Determine the equivalent elastic deflection,$X_{E}$ 

$$X_{E}=r_{u}/K_{E}=329/492=0.669\ in $$

Step 11.Calculate the effective mass of the element 

$$\begin{aligned}&a.\quad&K_{LM}(average elastic and plastic)\\&\quad&=(0.78+0.66)/2=0.72\\ \end{aligned}$$

b.Unit mass of element 

$$m=\frac{w}{g}=\frac{2\times1\times1\times490\times10^{6}}{1.728\times32.2\times12}=1.468\frac{\mathrm{psi}-\mathrm{ms}^{2}}{\mathrm{in}}$$

<!-- batch 30 | page 35 -->

C.Effective unit mass of element,$m_{e}$ 

$$m_{e}=K_{LM}\times m=0.72\times1.468=1.057\frac{\mathrm{psi}-\mathrm{ms}^{2}}{\mathrm{in}}$$

Step 12.Calculate the natural period of vibration,$T_{N}$ 

$$T_{N}=2\pi\left(1,057/492\right)^{1/2}=9.2\mathrm{m s}$$

Step 13.Determine the door plate response for:

$$\begin{aligned}&P/r_{u}=1100/329=3.34\\&T/T_{N}=1.0/9.2=0.109\\&C_{1}=100/1100=0.091\\&C_{2}>1000\\ \end{aligned}$$

(Figure 3-62 (+), Region C)

Using Figure 3-253 (+/+/+),

$$X_{m}/X_{E}=1.5$$

$$X_{m}=1.5\times0.669=1.00in $$

Step 14.Determine the support rotation.

$$\Theta=\tan^{-1}\left(1/24\right)=2.39^{\circ}<3^{\circ}$$

Step 15.Evaluate the selection of the dynamic increase factor.

$$\dot{\varepsilon}=\dot{t}_{d s}/\dot{E}_{s}\dot{t}_{E}$$

$$t_{E}/T=1.8,t_{E}=1.8\mathrm{m s}$$

(Figure 3-253 (+/+/+))

$$\dot{\varepsilon}=68.2/(29.6\times10^{3}\times0.0018)=1.28in/in/sec $$

$$\mathsf{D I F}=1.3$$

(Figure 5-2 (+), average of A36 and A514)

Initial selection of $\mathrm{DIF}=1.24$ is adequate.

Since the support rotation criteria has been satisfied and the preliminary selection of the DIF is acceptable, a 2 inch thick plate is used in design.

Steps 15These steps are bypassed since the door plate has no stiffening elements.through 18



<!-- batch 30 | page 36 -->

# PROBLEM 5A-8DESIGNOF DOUBLY SYMMETRICBEAMSSUBJECTED TO  INCLINED PRESSURE-TIME LOADING 

Problem:Design a purlin or girt as a flexural member which is subjected to a transverse pressure-time load acting in a plane other than a principal  plane.



## Procedure:

Step 1.Establish the design parameters.

a.Pressure-time load 

b.Angle of inclination of the load with respect to the vertical axis of the section 



C.Design criteria: Maximum support rotation limited to 2.

d.Member spacing, b 

e.Type and properties of steel used:

Minimum yield strength for the section (Table 5-1 (+))

Dynamic increase factor, DIF 

(Table 5-2 (+))

Step 2.Preliminary sizing of the beam.

a.Determine the equivalent static load, w, using a preliminary dynamic load factor equal to 1.0.



$$w=1.0\times p\times b $$

b.Using the appropriate resistance formula from Table 3-1 (+) and the equivalent static load derived in Step 2a, determine the required 

$M_{p}$ 



C.Determine the required section properties using Equation 5-7.Select a larger section since the member is subjected to unsymmetrical bending.



Note that for a load inclination of 10, it is necessary to increase the required average section modulus, (1/2) (S + Z), by 40 percent.

Step 3.Check local buckling of the member.(Section 5-24).

Step 4.Calculate the inclination of the neutral axis.(Equation 5-24).

Step 5.Calculate the elastic and plastic section moduli of the section.

(Equation 5-25).

Step 6.Compute the design plastic moment, Mp, (Equation 5-6).

<!-- batch 30 | page 37 -->

Step 7.Calculate ultimate unit resistance,$r_{u},$ of the member.

Step 8.Calculate elastic deflection,$\delta_{-}$ 

Step 9.Determine the equivalent elastic unit stiffness,$K_{E}$ , of the beam section using δfrom Step 8.



Step 10.Compute the equivalent elastic deflection,$X_{E},$ of the member as given by 

$X_{E}=r_{u}/K_{E}$ 



Step 11.Determine the load-mass factor,$K_{L M_{1}}$ ,and obtain the effective unit mass,$m_{e}$ _, of the element.



Step 12.Evaluate the natural period of vibration,$T_{N}$ 

Step 13.Determine the dynamic response of the beam. Evaluate $P/r_{u}$ and $T/T_{N}$ ..,using the response charts of Chapter 3 to obtain $X_{m}/X_{E}$ and Θ.Compare with criteria.



Step 14.Determine the ultimate dynamic shear capacity,$V_{p}$ (Equation 5-16) and maximum support shear, V, using Table 3-9 (+) of Chapter 3 and check adequacy.



<!-- batch 30 | page 38 -->

# EXAMPLE 5A-8DESIGN AN I-SHAPED BEAM FOR UNSYMMETRICAL  BENDING DUE TO INCLINED PRESSURE-TIME LOADING 

Required:Design a simply-supported l-shaped beam subjected to a pressuretime loading acting at an angle of 10° with respect to the principal vertical plane of the beam. This beam is part of a structure designed to protect personnel.



Step 1.Given:

a.Pressure-time loading 

b.Design criteria: The structure is to be designed for more than one "shot." A maximum end rota $\mathrm{t i o n=1^{\circ}}$ ', is therefore assigned 

C.Structural configuration 

(Figure 5A-10 (+))

d.Steel used: A36

Yield strength,,$f_{v}=36\mathrm{k s i}$ 

Dynamic increase factor,$DIF=1.29$ 

Average yield strength increase factor,$S I F=1.1$ (Section 5-12.1)

Dynamic design strength,

$$f_{ds}=1.1\times1.29\times36=51.1\mathrm{ksi}$$

Dynamic yielding stress in shear,

$$f_{dv}=0.55f_{ds}=0.55\times51.1=28.1\mathrm{ksi}$$

Modulus of elasticity,$E=29,000,000ps$ 

Step 2.Preliminary sizing of the member.

a.Determine equivalent static load.

Select DL.$F=1.2$ 

$$w=1.25\times4.5\times4.5\times144/1.000=3.65\mathrm{k/ft}$$

<!-- batch 30 | page 39 -->

Figure 5A-10 Beam Configuration and Loading, Example 5A-8(a)

$$b=4.5$$

$$\phi=10^{\circ}$$

b.Determine minimum required $M_{P}$ 

$$M_{p}=(wL^{2})/8=(3.65\times19^{2})/8=165\ k-ft $$

C.Selection of a member.

For a load acting in the plane of the web,

$$\begin{aligned}&(S+Z)=2M_{p}/f_{ds}=(2\times165\times12)/51.1\\&(S+Z)=77.5in^{3}\\ \end{aligned}$$

(S + Z) required $1.4\times77.5=109in^3$ 

$$\begin{aligned}&\mathsf{Try}\mathsf{W}14\times38,S_x=54.6\mathsf{in}^3,Z_x=61.5\mathsf{in}^3,\\&(S+Z)=116.1\mathsf{in}^3,I_x=385\mathsf{in}^4\\&I_y=26.7\mathsf{in}^4\\ \end{aligned}$$

Step 3.Check against local buckling.

For $\mathsf{W14}\times\mathsf{38}$ 

$$\begin{aligned}&d/t_{w}=45.5<(412/(36)^{1/2})(1-1.4\times P/P_{y})=68.66\quad O.K.\quad(Equation5-17)\\&b_{f}/2t_{f}=6.6<8.5\quad O.K.\quad(Section5-24)\\ \end{aligned}$$

<!-- batch 30 | page 40 -->

Step 4.

Inclination of elastic and plastic neutral axes with respect to the x-axis.

$$\begin{aligned}&\tan\alpha=(I_x/I_y)\tan\phi=(385/26.7)\tan10^\circ=2.546\quad(\text{Equation5-24})\\&\alpha=68.5^\circ\\ \end{aligned}$$

Calculate the equivalent elastic section modulus.

$$\begin{aligned}&S=(S_x S_y)/(S_y\cos\phi+S_x\sin\phi)\\&S_x=54.6in^3,S_y=7.88in^3,\phi=10^\circ\\&\sin10^\circ=0.174,\cos10^\circ=0.985\\&S=(54.6)(7.88)/(7.88\times0.985+54.7\times0.174)=24.9in^3\\ \end{aligned}$$

Step 5.Calculate the plastic section modulus, Z.

$$\begin{aligned}&Z=A_{c}m_{1}+A_{t}m_{2}\\&A_{c}=A_{t}=A/2=11.2/2=5.6in^{2}\\ \end{aligned}$$

(Equation 5-6)

Let y be the distance of the c.g. of the area of cross section in compression from origin as shown in Figure 5A-11 (+)

$$\bar{y}=\frac{1}{5.6}\left[6.770\times0.515\times\left(\frac{14.10}{2}-\frac{0.515}{2}\right)\right]\times\frac{1}{2}\left(14.10-2\times0.515\right)\times0.310\times\frac{1}{2}\left(\frac{14.10}{2}-0.515\right)\times5.42\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}\times\frac{1}\times\frac{1}{2}\times\frac{1}{2}\times\times\frac{1}{2}\times\frac{1}{2}\times\times\frac{1}{2}\times\frac{2}\times\frac{1}{2}\times\times\frac{1}{2}\times\frac{2}\times\frac{1}{2}\times\times\frac{1}{2}\times\times\frac{2}\times\frac{1}{2}\times\times\frac{2}\times\frac{1}{2}\times\times\frac{2}\times\times\frac{1}{2}\times\times\frac{2}\times\times\frac{1}{2}\times\times\times\frac{1}\times\times\frac{2}\times\times\frac{1}{2}\times\times\times\frac{2}\times\times\frac{1}\times\times\frac{2}\times\times\frac{1}\times\times\times{2}\times\times\frac{2}\times\times\frac{1}\times\times\times\frac{2}\times\times\frac{1}\times\times\times\times\frac{2}\times\times\times\frac{\frac{1}\times\times\times\times\times\frac{\frac{1}\times\times\times\times\times\frac{\frac{\frac{\frac{1}\times\times\times\times\times\times\times\frac{\frac{\frac{\frac{\frac{\frac\frac{\frac\frac\frac\frac{\frac\frac{\frac\frac{\frac\frac{\frac\frac{\frac\frac\frac{\frac\frac\frac{\frac{\frac\frac{\frac\frac\frac{\frac\frac\frac{\frac\frac\frac{\frac\frac{\frac\frac\frac{\frac\frac\frac{\frac\frac{\frac\frac\frac\frac{\frac\frac{\frac\frac\frac\frac\frac{\frac\frac\frac{\frac{\frac\frac\frac\frac{\frac\frac\frac\frac\frac{\frac\frac\frac{\frac\frac\frac{\frac\frac\frac\frac{\frac\frac\frac\frac{\frac\frac\frac{\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac{\frac\frac\frac\frac{\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac{\frac\frac\frac{\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac{\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\frac\$$

$$m_{1}=m_{2}=\bar{y}\sin\alpha=5.42\sin(68^{\circ}30')=5.05\mathrm{~in}\mathrm{c}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~}m_{~}\mathrm{~}\mathrm{~}\mathrm{~}\mathrm{~$$

<!-- batch 30 | page 41 -->

Figure 5A-11 Loading on Beam Section, Example 5A-8(b)

<div style="text-align: center;"><img src="../pages/batch 30/imgs/img_in_image_box_341_316_854_718.jpg" alt="Image" width="43%" /></div>


Step 6.Determine design plastic moment,$M_{P}$ 

$$\begin{aligned}M_{p}&=f_{ds}(S+Z)/2=51.1(24.9+56.5)/2\\&=51.1\times40.7=2.080in-kips\end{aligned}$$

Step 7.Calculate ultimate unit resistance,$r_{u}.$ 

$$r_{u}=8M_{p}/L^{2}=(8)(2,080)(1,000)/(19\times12)^{2}=320\ lb/in $$

Step 8.Compute elastic deflection, δ.

$$\begin{aligned}\delta=&\left[\left(\delta_{x}^{2}+\delta_{y}^{2}\right)\right]^{1/2}\\\delta_{y}=&\frac{5w\cos\phi L^{4}}{384EI_{x}}\\\delta_{x}=&\frac{5w\sin\phi L^{4}}{384EI_{y}}\\w=&\mathrm{e}_{\mathrm{equiv}}\mathrm{int}_{\mathrm{int}}\mathrm{static}\mathrm{load}+\mathrm{head}\mathrm{load}\\=&2.92+\frac{(4.8\times4.5)+38}{1000}\mathrm{kps}/\mathrm{ft}=2.94\mathrm{kps}/\mathrm{ft}\\\delta=&\left[\frac{\left(5w\sin\phi L^{4}\right)^{2}}{384EI_{y}}+\frac{\left(5w\cos\phi L^{4}\right)^{2}}{384EI_{x}}\right]^{1/2}\\=&\frac{5w L^{4}}{38400E}\times\left[0.652^{2}+0.256^{2}\right]^{1/2}=2.08\mathrm{mech}\end{aligned}$$

<!-- batch 30 | page 42 -->

Step 9.Calculate the equivalent elastic unit stiffness,$K_{E}$ 

$$K_{E}=\frac{w}{\delta}=\frac{2.94\times1.000\times1}{12\times2.085}=117.81b/in^{2}$$

(Get w from Step 8)

Step 10.Determine the equivalent elastic deflection,$X_{E}$ 

$$X_{E}=r_{u}/K_{E}=320/117.8=2.72\ inche $$

Step 11.Calculate the effective mass of the element,$m_{e}$ 

a.Load-mass factor,$K_{L M}$ 

KLM (average elastic and plastic)

$$(0.78+0.66)/2=0.72$$

b.Unit mass of element, m 

$$m=\frac{w}{g}=\frac{\left[(4.5\times4.8)+38\right]\times10^{6}}{32.2\times12\times12}=1.286\times10^{4}\mathrm{~lb}-\mathrm{ms}^{2}/\mathrm{in}^{2}$$

C.Effective unit mass of element,$\mathsf{m_{e}}$ 

$$m_{e}=K_{LM}m=0.72\times1.286\times10^{4}=0.93\times10^{4}\ lb-ms^{2}/in^{2}$$

Step 12.Calculate the natural period of vibration,$T_{N}$ 

$$T_{N}=2\pi\left[(93\times10^{2})/117.8\right]^{1/2}=55.8~\mathrm{m s}$$

(Section 5-22.2)

Step 13.Determine the beam response.

$$\begin{aligned}&\mathsf{Pexak overpressure}\quad&P&=4.5\times4.5\times12=243\mathsf{Ib/in}\\&\mathsf{Pexak}\mathsf{resistance}\quad&r_u&=320\mathsf{Ib/in}\\&\mathsf{Duration}\quad&T&=20\mathsf{ms}\\ \end{aligned}$$

Natural period of vibration $T_{N}=55.8~\mathrm{m s}$ 

$$P/r_{u}=243/320=0.76一
$$

$$T/T_{N}=20/55.8=0.358$$

From Figure 3-64a (+)

$$X_{m}/X_{E}<1$$

From Figure 3-49 (+), for $T/T_{N}=0.358$ 

DL $F=0.97$ 

$$Hence X_{m}=0.97\times4.5\times4.5\times12/117.8=2.0in $$

<!-- batch 30 | page 43 -->

Find end rotation, Θ.

$$\begin{aligned}&\tan\Theta=X_{m}/(L/2)=2.0/[(19\times12)/2]=0.0175\\ &\quad\Theta=1.0^{\circ}\quad\text{O.K.}\\ \end{aligned}$$

Step 14.Calculate the dynamic ultimate shear capacity,$V_{p},$ and check for adequacy.



$$\begin{aligned}&V_{p}=f_{dv}A_{w}=28.1(14.10-2\times0.515)(0.310)=113.9kips(Equation5-16)\\&V=DLF\times P\times b\times L/2\\&\quad=0.97\times4.5\times4.5\times19\times144/(2\times1,000)\\&\quad=26.9kips<89.2kips<V_{p}\quad O.K.\quad(Table3-9(+))\\ \end{aligned}$$

<!-- batch 30 | page 44 -->

## APPENDIX 5B LIST OF SYMBOLS 


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>SIF</td><td>yield stress increase factor</td></tr><tr><td>A</td><td>Area of cross section | $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{b}$</td><td>Area of bracing member $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{c}$</td><td>Area of cross section in compression $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{t}$</td><td>Area of cross section in tension 1 $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{w}$</td><td>Web area $({\mathsf{i n}}^{2})$</td></tr><tr><td>b</td><td>Width of tributary loaded area (ft)</td></tr><tr><td>$b_{f}$</td><td>Flange width (in)</td></tr><tr><td>$b_{h}$</td><td>Tributary width for horizontal loading (ft)</td></tr><tr><td>$b_{v}$</td><td>Tributary width for vertical loading (ft)</td></tr><tr><td>DIF</td><td>Dynamic increase factor</td></tr><tr><td>C</td><td>Distance from neutral axis to extreme fiber of cross-section in flexure (in)</td></tr><tr><td>$C_{1}$ $c$</td><td>Coefficients indicating relative column to girder moment capacity (Section 5-42.1)</td></tr><tr><td>$C_{b}$ $C_{c}$</td><td>Bending coefficient defined in Section 1.5.1.4.5 of the AISC Specification Column slenderness ratio indicating the transition from elastic to inelastic</td></tr><tr><td>$C_{m x},C_{m y}$</td><td>buckling Coefficients applied to the bending terms in interaction formula (AiSC</td></tr><tr><td>$C_{2}$</td><td>Specification Section 1.6.1) Coefficient in approximate expression for sidesway stiffness factor</td></tr><tr><td>D</td><td>(Table 5-14 (+)) Coefficient indicating relative girder to column stffness (Table 5-14 (+))</td></tr><tr><td>DLF</td><td>Dynamic load factor</td></tr><tr><td>d</td><td>Web depth (in)</td></tr><tr><td></td><td>(1)</td></tr><tr><td></td><td>(2) Diameter of cylindrical portion of fragment (in)</td></tr><tr><td>E</td><td>Young's modulus of elasticity (psi)</td></tr><tr><td>f</td><td>(1) Maximum bending stress (psi)</td></tr><tr><td></td><td>(2) Shape factor, S/Z</td></tr></tbody></table></body></html></div>


<!-- batch 30 | page 45 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>$f_{a}$</td><td>Axial stress permitted in the absence of bending moment from Section 5-37.3 (psi)</td></tr><tr><td>$f_{b}$</td><td>Bending stress permitted in the absence of axial force (psi)</td></tr><tr><td>$f_{c r}$</td><td>Web buckling stress (psi)</td></tr><tr><td>$f_{d}$</td><td>Maximum dynamic design stress for connections (psi)</td></tr><tr><td>$f_{d s}$</td><td>Dynamic design stress for bending, tension and compression (psi)</td></tr><tr><td>$\pmb{f}_{d v}$</td><td>Dynamic yielding shear stress (psi)</td></tr><tr><td>$\pmb{f}_{d v}$</td><td>Dynamic ultimate stress (psi)</td></tr><tr><td>$f_{d y}$</td><td>Dynamic yield stress (psi)</td></tr><tr><td>$F_{\mathit{e x}}^{\prime},F_{\mathit{e y}}^{\prime}$</td><td>Euler buckling stresses divided by safety factor (psi)</td></tr><tr><td>$F_{H}$</td><td>Horizontal component of force in bracing member (Ib)</td></tr><tr><td>$F_{s}$</td><td>Allowable static design stress for connections (psi)</td></tr><tr><td>$f_{u}$</td><td>Ultimate tensile stress (psi)</td></tr><tr><td>$f_{y}$</td><td>Minimum static yield stress (psi)</td></tr><tr><td>g</td><td>Acceleration due to gravity (386 in/sec2)</td></tr><tr><td>$H$</td><td>Story height (ft)</td></tr><tr><td>$h$</td><td>Web depth for cold-formed, light gauge steel panel sections (in)</td></tr><tr><td>1</td><td>Moment of inertia $({\mathsf{i n}}^{4})$</td></tr><tr><td>$I_{c a}$</td><td>Average column moment of inertia for single-story multi-bay frame $({\mathsf{i n}}^{4})$</td></tr><tr><td>$I_{20}$</td><td>Effective moment of inertia for cold-formed section at a service stress of</td></tr><tr><td>$I_{x}$</td><td>20 ksi per foot width) $({\mathsf{i n}}^{4}$</td></tr><tr><td>$I_{y}$</td><td>Moment of inertia about the x-axis $(\mathsf{i n}^{4})$</td></tr><tr><td>K (1）</td><td>Moment of inertia about the y-axis $({\mathsf{i n}}^{4})$</td></tr><tr><td></td><td>Effective length factor for a compression member</td></tr><tr><td>(2) Table 5-14 (+)</td><td>Stiffness factor for rigid single-story, multi-bay frame from</td></tr><tr><td></td><td>Horizontal stiffness of diagonal bracing (Ib/ft)</td></tr><tr><td>$\begin{array}{r}{K_{b}}\\ {K_{E}}\\ {K_{L}}\end{array}$</td><td>Equivalent elastic stiffness (Ilb/in or psi/in)</td></tr><tr><td>Load factor</td><td></td></tr></table></body></html></div>


<!-- batch 30 | page 46 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>Load-mass factor $K_{L M}$</td><td></td></tr><tr><td>Mass factor $K_{M}$</td><td></td></tr><tr><td>L</td><td>(1) Span length (ft or in)</td></tr><tr><td></td><td>(2) Frame bay width (ft)</td></tr><tr><td>/</td><td>Distance between cross section braced against twist or lateral</td></tr><tr><td></td><td>displacement of compression flange or distance between points of lateral support for beams or columns</td></tr><tr><td>$1/r$</td><td>Slenderness ratio</td></tr><tr><td>$I_{b}$</td><td>Actual unbraced length in the plane of bending (in)</td></tr><tr><td>$I_{c r}$</td><td>Critical unbraced length (in)</td></tr><tr><td>$M$</td><td>Total effective mass 1 $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{m x},M_{m y}$</td><td>Moments about the x- and y-axis that can be resisted by member in the</td></tr><tr><td>$M_{p}$</td><td>absence of axial load Design plastic moment capacity</td></tr><tr><td>$M_{2}$ $M_{1}$</td><td>Design plastic moment capacities (Figures 5-6 (+) and 5-10 (+))</td></tr><tr><td>$M_{\mathsf{p x}},M_{\mathsf{p y}}$</td><td>Plastic bending moment capacities about the x- and y-axes</td></tr><tr><td>$M_{p u}$</td><td>Ultimate dynamic moment capacity</td></tr><tr><td>$M_{u p}$</td><td>Ultimate positive moment capacity for unit width of panel</td></tr><tr><td>$M_{u n}$</td><td></td></tr><tr><td>$M_{v}$</td><td>Ultimate negative moment capacity for unit width of panel</td></tr><tr><td>m</td><td>Moment corresponding to first yield</td></tr><tr><td></td><td>(1) Unit mass of panel (psi-ms2/in)</td></tr><tr><td>$m_{e}$</td><td>(2) Number of braced bays in multi-bay frame Effective unit mass</td></tr><tr><td>$m_{1}$</td><td>Distance from plastic neutral axis to the centroid of the area in $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$</td></tr><tr><td>$m_{2}$</td><td>compression in a fully plastic section (in) Distance from plastic neutral axis to the centroid of the area in tension in a</td></tr><tr><td></td><td>fully plastic section (in)</td></tr><tr><td>N</td><td>Bearing length at support for cold-formed steel panel (in)</td></tr><tr><td>n</td><td>Number of bays in multi-bay frame</td></tr></table></body></html></div>


<!-- batch 30 | page 47 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>P</td><td>(1) Applied compressive load (Ib)</td></tr><tr><td>(2)</td><td>Peak pressure of equivalent triangular loading function, (psi) [when used with,or peak total blast load (Ib) [when used with $[R_{u}]$ $r_{u}]$</td></tr><tr><td>$P_{e x},P_{e y}$</td><td>Euler buckling loads about the x- and y-axes</td></tr><tr><td>$P_{p}$</td><td>Ultimate capacity for dynamic axial load, (Ib) $A f_{d y}$</td></tr><tr><td>$P_{u}$</td><td>Ultimate axial compressive load (Ib)</td></tr><tr><td>$P_{y}$</td><td>Ultimate capacity for static axial load (Ib) $A{\boldsymbol{f}}_{y}$</td></tr><tr><td>$P_{h}$</td><td>Reflected blast pressure on front wall (psi)</td></tr><tr><td>$P_{v}$</td><td>Blast overpressure on roof (psi)</td></tr><tr><td>$Q_{u}$</td><td>Ultimate support capacity (Ib)</td></tr><tr><td>$q_{h}$</td><td>Peak horizontal load on rigid frame (Ib/t)</td></tr><tr><td>$q_{v}$</td><td>Peak vertical load on rigid frame (Ib/ft)</td></tr><tr><td>$R$</td><td>Equivalent total horizontal static load on frame (Ib)</td></tr><tr><td>$R_{u}$</td><td>Ultimate total flexural resistance (b)</td></tr><tr><td>$r_{b}$</td><td>Radius of gyration of bracing member (in)</td></tr><tr><td>$r_{T}$</td><td>Radius of gyration, Equation 5-22 (in)</td></tr><tr><td>$r_{u}$</td><td>Ultimate unit flexural resistance (Ib/in or psi)</td></tr><tr><td>$r_{x},r_{y}$</td><td>Radii of gyration about the x- and y-axes (in)</td></tr><tr><td>$\overline{{r}}$</td><td>Required resistance for elastic behavior in rebound (psi)</td></tr><tr><td>S</td><td>Elastic section modulus | $({\mathsf{i n}}^{3})$</td></tr><tr><td>$\mathcal{S}_{\gamma}$ ${\mathcal{S}}_{x}$</td><td>Elastic section modulus about the x- and y-axes (in3)</td></tr><tr><td>$\mathcal{S}^{+}$</td><td>Effective section modulus of cold-formed section for positive moments $({\mathsf{i n}}^{3})$</td></tr><tr><td>$s$</td><td>Effective section modulus of cold-formed section for negative moments $({\mathsf{i n}}^{3})$</td></tr><tr><td>T</td><td>Load duration (sec)</td></tr><tr><td>$T_{N}$</td><td>Natural period of vibration (sec)</td></tr><tr><td>t</td><td>(1) Thickness of plate element (in)</td></tr><tr><td></td><td>(2) Thickness of panel section (in)</td></tr></tbody></table></body></html></div>


<!-- batch 30 | page 48 -->

tE Time to yield (sec)

tf Flange thickness (in)

tm Time to maximum response (sec)

tw Web thickness (in)

V Support shear (Ib)

V Ultimate shear capacity (Ib)

$V_{r}$ Residual velocity of fragment (fps)

$V_{s}$ Striking velocity of fragments (fps)

$V_{x}$ Critical perforation velocity of fragment (fps)

W Total weight (Ib)

$W_{c}$ Total concentrated load (Ilb)

$W_{E}$ External work (Ilb-in)

Wf$Fragment weight (oz)

$W_{I}$ Internal work (Ib-in)

w (1)Flat width of plate element (in)

(2)Load per unit area (psi)

(3)Load per unit length (Ib/ft)

$X_{o}$ Deflection at design ductility ratio (in) (Figure 5-12 (+))

$X_{E}$ Equivalent elastic deflection (in)

$X_{m}$ Maximum deflection (in)

X Depth of penetration of steel fragments (in)

Z Plastic section modulus (in³)

$Z_{x},$ $Z_{y}$ Plastic section moduli about the x- and y-axes (in3)

α(1)Angle between the horizontal principal plane of the cross section 

and the neutral axis (deg)

(2)Ratio of horizontal to vertical loading on a frame 



<!-- batch 30 | page 49 -->

B (1)Base fixity factor (Table 5-14 (+))

(2)Support condition coefficient (Section 5-34.3)

(3)Critical length for bracing correction factor (Section 5-26.3)

γAngle between bracing member and a horizontal plane (deg)

δ(1)Total transverse elastic deflection (in)

(2)Lateral (sidesway) deflection (in)

εStrain (in/in)

εAverage strain rate (in/in/sec)

?(1)Member end rotation (deg)

(2)Plastic hinge rotation (deg)

Θmax Maximum permitted member end rotation 

μDuctility ratio 

μmax Maximum permitted ductility ratio 

φAngle between the plane of the load and the vertical principal plane of the 

cross section (deg)



<!-- batch 30 | page 50 -->

## APPENDIX 5C BIBLIOGRAPHY 

1.Healey, J., et al., Design of Steel Structures to Resist the Effects of HE Explosions, by Ammann & Whitney, Consulting Engineers, New York, New York,Technical Report 4837, Picatinny Arsenal, Dover, New Jersey, August 1975.2.Keenan, W., Tancreto, J., Meyers, G., Johnson, F., Hopkins, J., Nickerson, H.and Armstrong, W., NCEL Products Supporting DOD Revision of NAVFAC P397, Program No. Y0995-01-003-201, Technical Memorandum 2591TM,sponsored by Naval Facilities Engineering Command, Alexandria, Virginia and Naval Civil Engineering Laboratory, Port Hueneme, California, March 1983.3.Stea, W., Tseng, G. and Kossover, D., Nonlinear Analysis of Frame Structures Subjected to Blast Overpressures, by Ammann & Whitney, Consulting Engineers,New York, New York, Contractor Report ARLCD-CR-77008, U.S. Army Research and Development Command, Large Caliber Weapons Systems Laboratory, Dover, New Jersey, May 1977.
4.Stea, W., and Sock, F., Blast-resistant Capacities of Cold-formed Steel Panels,
by Ammann & Whitney, Consulting Engineers, New York, New York, Contractor Report ARLCD-CR-81001, U.S. Army Research and Development Command,
Large Caliber Weapon Systems Laboratory, Dover, New Jersey, May 1981.5.Stea, W., Dobbs, N. and Weissman, S., Blast Capacity Evaluation of Preenqineered Buildinq, by Ammann & Whitney, Consulting Engineers, New York,
New York, Contractor Report ARLCD-CR-79004, U.S. Army Research and Development Command, Large Caliber Weapons Laboratory, Dover, New Jersey, March 1979.
6.Healey, J., Weissman, S., Werner, H. and Dobbs, N., Primary Fragment Characteristics and Impact Effects on Protective Barriers, by Ammann &
Whitney, Consulting Engineers, New York, New York, Technical Report 493,
Picatinny Arsenal, Dover, New Jersey, December 1975.7.Manual of Steel Construction, Eighth Edition, American Institute of Steel Construction, New York, New York, 1980.
8.Specification for the Design, Fabrication and Erection of Structural Steel for Buildings and Commentary thereon, American Institute of Steel Construction,
New York, New York, 1978.
9.Specification for the Design of Cold-Formed Steel Structural Members and Commentary thereon, American Iron and Steel Institute, New York, New York 1968.
10.Design of Structures to Resist the Effects of Atomic Weapons, Department of the Army Technical Manual TM 5-856-2, 3 and 4, Washington, D.C., August 1965.

<!-- batch 30 | page 51 -->

11.Bleich, F., Buckling Strength of Metal Structures, McGraw-Hill, New York, 1952.12.Newmark, N.M, and Haltiwanger, J.D., Principles and Practices for Design of Hardened Structures, Air Force Design Manual, Technical Documentary Report Number AFSWC, TDR-62-138, Air Force Special Weapons Center, Kirtland Air Force Base, New Mexico, December 192.
13.Seely, F.B., and Smith, J.O., Advanced Mechanics of Materials, Second Edition,
J. Wiley & Sons, New York, New York, 1961.
14.Bresler, B., et al., Design of Steel Structures, J. Wiley & Sons, New York, New York, 198.
15.Johnston, B.G., ed., Guide to Design Criteria for Metal Compression Members,
Second Edition, J. Wiley & Sons, New York, New York 1966.16.McGuire, W., Steel Structures, Prentice Hall, Englewood, New Jersey, 198.17.Tall, L., et al., Structural Steel Design, Ronald Press, New York, New York, 194.18.Beedle, L.S., Plastic Design of Steel Frames, J. Wiley & Sons, New York, New York, 1958.
19.Hodge, P.G., Plastic Analysis of Structures, McGraw-Hill, New York, 1959.20.Massonet, C.E., and Save, M.A., Plastic Analysis and Design, Blaisdell, New York, New York, 1965.
21.Plastic Design in Steel, A Guide and Commentary, Second Edition, Joint Committee of the Welding Research Council and the American Society of Civil Engineers, ASCE, 1971.
