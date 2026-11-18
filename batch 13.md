

<!-- batch 13 | page 1 -->

## DYNAMICALLY EQUIVALENT SYSTEMS 

## 3 -16INTRODUCTION

In dynamic analysis, there are only three quantities to be considered: (1) the work done, (2) the strain energy, and (3) the kinetic energy. To evaluate the work done, the displacement at any point on the structure under externally distributed or concentrated loads must be known. The strain energy is equal to the summation of the strain energies in all the structural elements which may be in bending, tension, compression,shear or torsion. The kinetic energy involves the energy of translation and rotation of all the masses of the structure. The actual evaluation of these quantities for a given structure under dynamic load would be complicated. However, for practical problems,this can be avoided by using appropriate assumptions.



In most cases, a structure can be replaced by an idealized (or dynamically equivalent)system which behaves in nearly the same manner as the actual structure. The distributed masses of the given structure are lumped together into a number of concentrated masses. The strain energy is assumed to be stored in several weightless springs which do not have to behave elastically; similarly, the distributed load is replaced by a number of concentrated loads acting on the concentrated masses.Therefore, the equivalent system consists merely of a number of concentrated masses joined together by weightless springs and subjected to concentrated loads which vary with time. This concentrated mass-spring-load system is defined as an equivalent dynamic system.



Although all structural components possess many degrees of freedom, one mode usually predominates in the response to short duration loads; thus, for all practical purposes, this one mode may be considered to define the behavior of the structure and the problem can be simplified by considering a single-degree-of-freedom system whose properties are based on the fundamental response mode of the structural component. A single-degree-of-freedom (SDOF) system is defined as one in which only one type of motion is possible or, in other words, only one coordinate is required to define its motion. Such a system is shown in Figure 3-42 (+) which consists of a concentrated mass on a frictionless surface attached to a weightless spring and subjected to a concentrated load. A single displacement variable x is sufficient to describe its motion.The material presented herein will be limited to single-degree-of-freedom systems only.Components in some structures, however, cannot be adequately modeled by only considering dynamic response in their first mode with a SDOF approach, particularly when consideration of dynamic strain is necessary. For these situations, a two-(or more)-degree-of-freedom analysis may be required. Procedures are presented in section 3-19.2 for performing these analyses.



Two fundamental methods are available for treating simple systems subjected to dynamic forces. The first of these methods solves the differential equations of motion of the system by either classical, numerical, or graphical means. The second method uses analysis and chart solutions determined by the use of the first method and are 

<!-- batch 13 | page 2 -->

approximate solutions. There is a third method which may also be very useful in vibrational problems that involves the energy equation.



In the following paragraphs the design factors used to define the parameters of an equivalent spring-mass system that represents a structural element are defined and the methods used to obtain these factors are discussed.



## 3 -17DYNAMIC DESIGN FACTORS

### 3 -17.1Introduction

The values of the mass and external force used in the equation of motion (Equation 3-1)are the actual values only if all the elements of the mass of the structure experience the same force and, consequently, move as a unit, in which case, the entire mass may be assumed to be concentrated at its center of gravity. In other cases, the assumption of uniform motion of the entire mass cannot be made without introducing serious error.This is true for members with uniformly distributed mass which bend or rotate under load. In such cases, the motion of the particles of mass varies along the length of the member. Beams, slabs, etc., with such distributed mass actually have an infinite number of degrees of freedom; however, such structural elements can be represented by an equivalent single-degree-of-freedom system.



In order to define an equivalent one-degree system, it is necessary to evaluate the parameters of that system; namely, the equivalent mass $M_{E}$ , the equivalent spring constant $K_{F}$ and the equivalent load $F_{E}$ . The equivalent system is selected usually so that the deflection of the concentrated mass is the same as that for a significant point of the structure. The single-degree-of-freedom approximation of the dynamic behavior of the structural element may be achieved by assuming a deflected shape for the element which is usually taken as the shape resulting from the static application of the dynamic loads. The assumption of a deflected shape establishes an equation relating the relative deflection of all points of the element.



The accuracy of the computed response of the single-degree-of-freedom system is dependent on the assumed deflected shape and the loading region. For example, in the impulsive loading realm, if the assumed deformed shape for a simply supported beam is taken to be a parabola, then the exact solution will be obtained for the deflection of the beam. In the quasi-static loading realm, however, the static deformed shape gives the exact answer. For blast resistance design, however, the differences in either a static deformed shape or a first mode approximation is negligible and thus either way is permissible. Usually, though, the static deformed shape is easier to use as it covers both symmetric and asymmetric deformation.



To permit rapid design of structural elements subjected to dynamic loads, it is convenient to introduce design or transformation factors. These factors are used to convert parameters of the actual blast-loaded component to corresponding parameters defining the equivalent system. To obtain them, it is necessary to equate the relations expressing the kinetic energy, strain and work done on the actual structural element 

<!-- batch 13 | page 3 -->

deflecting according to the assumed deflected shape, with the corresponding relations for the equivalent SDOF mass and spring system.



### 3 -17.2Load, Mass,and Resistance Factors

#### 3 -17.2.1Load Factor

The load factor is the design or transformation factor by which the total load applied on the structural element is multiplied to obtain the equivalent concentrated load for the equivalent single-degree-of-freedom system. If the actual total load on the structure is F and the equivalent load is $F_{E},$ the load factor $K_{i}$ is defined by the equation 

$$K_{L}=F_{F}/F $$

The load factor is derived by setting the external work done by the equivalent load $F_{F}$ on the equivalent system equal to the external work done by the actual load F on the actual element deflecting to the assumed deflected shape.



For a structure with distributed loads;

$$\boldsymbol{W}\boldsymbol{D}=\boldsymbol{F}_{E}\boldsymbol{\delta}_{\max}=\int\limits_{0}^{L}\boldsymbol{p}(\boldsymbol{x})\boldsymbol{\delta}(\boldsymbol{x})d\boldsymbol{x}$$

where 

$\delta_{m a x}=m a x i m u m$ I deflection of actual structure p(x) = distributed load per unit length $\delta(\pmb{x})=d e f l e c t i o n$ I at any point of actual structure $L=l e n g t h$ of structure 



rearranging terms 

$$F_{E}=\int\limits_{0}^{L}p(\boldsymbol{x})\phi(\boldsymbol{x})d\boldsymbol{x}$$

where 

$$\phi(\pmb{x})=\delta(\pmb{x})/\delta_{m a x}$$

and is called the shape function.

<!-- batch 13 | page 4 -->

NOTE. The shape function,$\phi({\pmb x})$ is different for the elastic range and the plastic range and therefore the load factor,$K_{L}$ will be different 

For example; the shape factor for a simply supported beam with a uniformly distributed load, in the elastic range is defined as 



$$\phi(x)=(16/5L^{4})(L^{3}x-2L x^{3}+x^{4})$$

while for the plastic range 

$$\phi(x)=2x/L $$

For a structure with concentrated loads 

$$W D=F_{\mathrm{e}}\delta_{\mathrm{m a x}}=\sum_{r=1}^{i}F_{r}\delta_{r}$$

Where 



$F_{r}=r t h\;c o n c e n t r a t e d\;l o a d$ 

$\delta_{r}=d e f l e c t i o n\:a t\:l o a d\:r$ 

i = number of concentrated loads 

rearranging terms 

$$\pmb{F}_{E}=\sum_{r=1}^{i}\pmb{F}_{r}\phi_{r},$$

where the shape factor is defined as 

$$\phi_{r}=\sum_{r=1}^{i}\delta_{r}/\delta_{\mathrm{m a x}}$$

$$x<L/2$$

Again there is a $K_{L}$ for the elastic range and a $K_{L}$ for the plastic range. However, for a single concentrated load located at the point of maximum deflection (i.e. the center of a simply supported or fixed-fixed beam, or the end of a cantilever beam) , is equal to one for both the elastic and plastic ranges and therefore $K_{i}$ is equal to one for both ranges.

<!-- batch 13 | page 5 -->

Values for $K_{L}$ for one-way elements are presented in Table 3-12 (+). Equation 3-41through 3-46 were used to calculate these values. An example calculating $K_{L}$ is shown in Appendix A.



#### 3 -17.2.2Mass Factor

The mass factor is the design or transformation factor by which the total distributed mass of an element is multiplied to obtain the equivalent lumped mass of the equivalent single-degree-of-freedom system. If the total mass of the actual element is M and the mass of the equivalent system is $M_{E}$ ,the mass factor $K_{M}$ is defined by the equation 

$$K_{M}=M_{F}/M $$

$K_{M}$ can be obtained by setting the kinetic energy of the equivalent system equal to the kinetic energy of the actual structural component as determined from its deflected shape.



For a structure with continuous mass 

$$K_{E}=\mathcal{V}M_{E}(\omega\delta_{\mathrm{m a x}})^{2}=\mathcal{V}\int_{0}^{L}m(x)[\omega\delta(x)]^{2}d x $$

where 

$$\begin{array}{r l}&{\omega=n a t u r a l c i r c u l a r f r e q u e n c y}\\ &{m(x)=d i s t r i b u t e d m a s s p e r u n i t l e n g t h}\end{array}$$

rearranging terms 

$$M_{E}=\int\limits_{0}^{L}m(x)\phi^{2}(x)d x $$

where the shape function $\phi(x)$ is based on the deflected shape of the element due to the applied loading and not to the distribution of the mass. Since the deflected shape of the element is different for the elastic and plastic ranges,$\phi({\pmb x})$ , and therefore $K_{M}$ , will also be different.



Using Equations 3-47 and 3-48, values for $K_{M}$ were calculated for one-way elements with constant mass. These values are shown in Table 3-12 (+)

For a concentrated mass system,

<!-- batch 13 | page 6 -->

$$K_{E}=\sqrt[2]{M_{E}(\omega\delta_{\max})^{2}}=\sqrt[2]{\sum_{r=1}^{i}M_{r}(\omega\delta_{r})^{2}}$$

where 

$$M_{r}=r t h\operatorname{m a s s}$$

$$\delta_{r}=d e f l e c t i o n o f m a s s r $$

i = number of lumped masses 

rearranging terms 

$${\cal M}_{E}=\sum_{r=1}^{i}{\cal M}_{r}{\phi_{r}}^{2},$$

An example of calculations for finding $K_{M}$ can be found in Appendix 3A.

#### 3 -17.2.3Resistance Function

The resistance factor is the design factor by which the resistance of the actual structural element must be multiplied to obtain the resistance of the equivalent single-degree-offreedom system. To obtain the resistance factor, it is necessary to equate the strain energy of the structural element, as computed from the assumed deflection shape, and the strain energy of the equivalent single-degree-of-freedom system. If the computed total resistance of the structural element is R and the equivalent total resistance of the equivalent system is ${\bar{R}}_{E}$ , then the resistance factor is defined by the equation 

$$K_{R}=R_{F}/R $$

Since the resistance of an element is the internal force tending to restore the element to its unloaded static position, it can be shown that the resistance factor $K_{R}$ must always equal the load factor $K_{I}$ 



### 3 -17.3Load-Mass Factor

The load-mass factor is a factor formed by combining the two basic transformation factors,$K_{L}$ and $K_{M}$ . It is merely the ratio of the mass factor to the load factor, and it is convenient since the equation of motion may be written in terms of that factor alone.The equation of motion of the actual system is given as 

$$F-R=M a $$

and for the equivalent system 

<!-- batch 13 | page 7 -->

$$K_{L}F-K_{L}R=K_{M}Ma $$

which can be re-written as 

$$F-R=(K_M/K_I)\mathrm{Ma}$$

or 

$$F-R=K_{LM}Ma=M_ea $$

where 

$$K_{LM}=10ad-mass factor=K_M/K_L $$

and 

$$M_{e}=\mathit{e f f e c t i v e~t o t a l~m a s s~o f~t h e~e q u i v a l e n t~s v s t e m}$$

when expressed in terms of the unit area of the element, Equation 3-52c can be written as 



$$f-r=K_{IM}ma=m_{e}a $$

Values of load, mass and load-mass factors are presented in Table 3-12 (+). Equation 3-53 was used to calculate the load mass factor.



Instead of computing the several factors above, the load-mass factors in the elastic and elasto-plastic ranges can be determined by relating the primary mode of vibration of the member to that of an equivalent single-degree-of-freedom system. In the plastic range,it can be assumed that neither the moment, nor the curvature, changes between the plastic hinges under increasing deflection. This assumption can be used to evaluate the effective plastic mass as follows:

In Figure 3-43 (+), a portion of a two-way element bounded by the support and the yield line is shown. The equation of angular motion for this section is 

$$\Sigma M=I_{m}\Theta^{m}$$

<!-- batch 13 | page 8 -->

where 



$\Sigma M={\mathrm{s u m m a t i o n~o f~m o m e n t s}}$ 

$I_{m}=m a s s$ :moment of inertia about the axis of rotation 

$\theta^{\prime\prime}=a n g u l a r a c c e l e r a t i o n$ 



Substituting in equation 

$$F c-(\Sigma M_{N}+\Sigma M_{o})=(I_{m}/L_{1})a $$

where a is the acceleration. Dividing through by c 

$$F-(\Sigma M_{N}+\Sigma M_{n})/c=(I_{m}/c L_{1})a $$

Since the second term is the resistance R 

$$F-R=(I_{m}/c L_{1})a=M_{e}a $$

and the load-mass factor $K_{L M}$ for the sector shown is 

$$K_{L M}=I_{m}/c L_{1}M $$

where c is the distance from the resultant applied load to the axis of rotation,$L_{1}$ is the total length of the sector normal to the axis of rotation and M is the total mass of the sector.



When the element is composed of several sectors, each sector must be considered separately and the contributions then summed to determine the load-mass factor for the entire element.



$$K_{L M}=\Sigma(I_{m}/c L_{2})/M $$

For elements of constant depth and, therefore, of constant unit mass, the above equation can be written in terms of the area moment of inertia I and the areas A of the individual sectors.



$$K_{L M}=\Sigma(1/c L_{1})/A $$

<!-- batch 13 | page 9 -->

Table 3-13 (+) gives the load-mass factors for the elastic and elasto-plastic response ranges for various two-way elements. The values given in the table apply for two-way elements of uniform thickness and supported as indicated. Also if there are openings in the element, they must be compact in shape and small in area compared to the total area of the element.



Figure 3-44 (+) gives the load-mass factors for the plastic response of various two-way elements. The load-mass factors are a junction of support condition and yield line location. These two-way elements must conform to the following limitations:

(1)Element must be of constant thickness.

(2)Opposite support must provide the same restraint so that a symmetrical yield line pattern occurs.



(3)Any openings must be compact in shape and small in area compared to the total area of the element.



### 3 -17.4Natural Period of Vibration

To determine the maximum response of a system either by numerical methods or design charts (both methods are described in Section 3-19), the effective natural period of vibration is required. This effective natural period of vibration, when related to the duration of a blast loading of given intensity and a given structural resistance,determines the maximum transient deflection $X_{m}$ of the structural element.

The effective natural period of vibration is 

$$T_{n}=2\pi(m_{e}/K_{E})^{1/2}=2\pi(K_{L M}m/K_{E})^{1/2}$$

where 



$m_{e}=t h e e f f e c t i v e u n i t m a s s$ 

$K_{E}=t h e e q u i v a l e n t u n i t s t i f f n e s s o f s y s t e m$ 

The values used for the effective mass and stiffness for a particular element depends on the allowable maximum deflection. When designing for completely elastic behavior,the elastic stiffness is used. In all other cases the equivalent elasto-plastic stiffness,$K_{E},$ is used. The elastic value of the effective mass is used for the elastic range, while in the elasto-plastic range the effective mass is the average of the elastic and elasto-plastic values. For small plastic deflections $(\varTheta\leq2^{\circ})$ , the value of the effective mass is equal to the average of the plastic value and the equivalent elastic value. The plastic effective mass is used for large plastic deflections.



<!-- batch 13 | page 10 -->

<div style="text-align: center;">Figure 3-42 Typical Single-Degree-of-Freedom System </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_image_box_225_326_961_656.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 3-43Determination of Load-Mass Factor in the Plastic Range </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_image_box_205_809_972_1200.jpg" alt="Image" width="64%" /></div>


<!-- batch 13 | page 11 -->

<div style="text-align: center;">Figure 3-44Load-Mass Factors in Plastic Range for Two-Way Elements </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_147_309_1045_1290.jpg" alt="Image" width="75%" /></div>


<!-- batch 13 | page 12 -->

<div style="text-align: center;">Table 3-12Transformation Factors for One-Way Elements </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Edge Conditions and Loading Diagrams</td><td>Range of Behavior</td><td>Load Factor KL</td><td>Mass Factor KM</td><td>Load-Mass Factor KLM</td></tr><tr><td>L</td><td>Elastic Plastic</td><td>0.64 0.50</td><td>0.50 0.33</td><td>0.78 0.66</td></tr><tr><td>↓P L/2 L/2</td><td>Elastic Plastic</td><td>1.0 1.0</td><td>0.49 0.33</td><td>0.49 0.33</td></tr><tr><td>L</td><td>Elastic Elasto-Plastic Plastic</td><td>0.58 0.64 0.50</td><td>0.45 0.50 0.33</td><td>0.78 0.78 0.66</td></tr><tr><td>↓P L/2 L/2</td><td>Elastic Elasto-Plastic Plastic</td><td>1.0 1.0 1.0</td><td>0.43 0.49 0.33</td><td>0.43 0.49 0.33</td></tr><tr><td>L</td><td>Elastic Elasto-Plastic Plastic</td><td>0.53 0.64 0.50</td><td>0.41 0.50 0.33</td><td>0.77 0.78 0.66</td></tr><tr><td>↓P L/2 L/2</td><td>Elastic Plastic</td><td>1.0 1.0</td><td>0.37 0.33</td><td>0.37 0.33</td></tr><tr><td>L</td><td>Elastic Plastic</td><td>0.40 0.50</td><td>0.26 0.33</td><td>0.65 0.66</td></tr><tr><td>⊥P L</td><td>Elastic Plastic</td><td>1.0 1.0</td><td>0.24 0.33</td><td>0.24 0.33</td></tr><tr><td>$\frac{\frac{\mathrm{p}/2}{\mathrm{~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\textcent~\text~\textcent~\textcent~\text~\textcent~\text~\textcent~\text~\text{\text~\text~\text{~\text~}~~}}}}\frac{\mathrm{p}/2}{\mathrm{~\text~\text{~\text~\text{~\text~\text{~~\text~}~}}}}\frac{\mathrm{p}/2}{\mathrm{~\text{~\text~\text{~\text{~~\text{~~\text{~~~}~}~}}}}}\frac{\mathrm{p}/2}{\mathrm{~\text{~\text{~~\text{~~\text{~~}~}~}}}}\frac{\mathrm{p}/2}{\mathrm{~{~\text{~~\text{~~\text{~~{~~}~}~}~}}}}\frac{\mathrm{p}/2}{\mathrm{~{~\text{~~~\text{~{~~~}~}~}}}}\frac{\mathrm{p}//2}{\mathrm{{~~~\text{~~{~~\text{~~{~~}~}~}~}}}}\frac{\mathrm{p/}/2}{\mathrm{{~~~~{~~\text{~~{~~~{~~}~}~}~}}}}\frac{\mathrm{p//2}/}{\mathrm{{~~~{~~~{~~~{~~~{~~}~{~~~}~}~}}}}}\frac{\mathrm{p///2}}{/\mathrm{{~~~~{~~~{~~~{~~~{~~~}{~~~~{~~~}~{~~~}~}~}}}}}}\frac{\mathrm{p/////2}}{//}\mathrm{//{~~~{~~~{~~~{~~~~{~~~{~~~{~~~}~{~~~{~~~~}~~{~~~}~{~~~~}~}}}}}}}}}\frac{\frac{{\mathrm///{///////}}}}\frac{{/////}\mathrm{///}}\frac{{///////}}\frac{///{/////}///}\frac{////}{//////}///////}\frac{/////}{/////////}/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// $</td><td>Elastic Plastic</td><td>0.87 1.0</td><td>0.52 0.56</td><td>0.60 0.56</td></tr></tbody></table></body></html></div>


<!-- batch 13 | page 13 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td colspan="2" rowspan="2">Support Conditions</td><td rowspan="2">Value of L/H ALL</td><td colspan="5">Elastic and Elasto-Plastic Ranges (Support Conditions) One Support Simple Three Supports Two Supports Simple Other Supports Simple Other Other Supports Fixed Fixed Supports Fixed</td><td></td></tr><tr><td>One Support Simple Other Supports Fixed 0.66</td><td>Three Supports Simple Other Supports Fixed</td><td>All Supports Simple 0.66</td><td>All Supports Fixed 0.65</td><td></td></tr><tr><td>Two adjacent</td><td>H L</td><td></td><td>edges supported and two edges free</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Three edges supported and one edge free</td><td>H L</td><td>LIH<0.5 0.5≤LH≤2 LIH≥2</td><td>0.77 L 0.65-0.16 -1 2H 0.65</td><td>0.77 L 0.66–0.144 -1 2H 0.66</td><td>0.79 L 0.65–0.186 -1 2H 0.65</td><td></td><td>0.79 L 0.66-0.175 -1 2H 0.66</td><td>H L +</td></tr></tbody></table></body></html></div>


<div style="text-align: center;">ee eee ee e rrere  re e e or ee  e </div>


See eee e 

ee 

12-20002



<!-- batch 13 | page 14 -->

## DYNAMIC ANALYSIS 

## 3 -18INTRODUCTION

Structural elements must develop an internal resistance sufficient to maintain all motion within the limits of deflection prescribed for the particular design. The load capacity of the member depends on the peak strength developed by the specific member (see Chapters 4 and 5) and on the ability of the member to sustain its resistance for a specific though relatively short period of time. This section describes the methods used for the analysis of structural elements subjected to dynamic loads, and these elements are divided into three groups, namely: (1) elements which respond to the pressure only (low pressure range), (2) elements which respond to pressure-time relationship (intermediate-pressure design range) and (3) elements which respond to the impulse which corresponds to the high pressure design range.



The method of analysis is different for the groups of elements. Those elements that respond to pressure only (this is still a pressure-time relation) and those that respond to pressure-time relationship may be analyzed using either numerical methods or design charts, while elements that respond to the impulse are analyzed using either design charts for large deflection or an impulse method for designs with limited deflections.

The method of analysis employing numerical techniques provides a solution that is obtained by a step-by-step integration, and is generally applicable for any type of load and resistance function. This method of analysis is presented in this section. Also presented is the result of a systematic analysis of single-degree dynamic systems for several idealized loadings plotted in nondimensional design charts.

## 3 -19

### ELEMENTS WHICH RESPOND TO PRESSURE ONLY AND PRESSURE-TIME RELATIONSHIP. 

### 3 -19.1General

To analyze these elements, the true magnitudes for the pressure-time relationship of the applied blast loads must be known. The determination of the dynamic response of these systems is accomplished using numerical techniques or design charts which relate the dynamic properties of the element (natural period of vibration, resistance, and deflection) to those of the blast overpressures.



### 3 -19.2Analysis By Numerical Methods

The numerical method of analysis involves a step-by-step integration procedure,starting at zero time, when displacement and the velocity of the system are presumably known. The time scale is divided into several discrete intervals, and one progresses by successively extrapolating the displacement from one time station to the next. As the time interval in the sequence of time is reduced, i.e., as the number of discrete intervals is increased, the accuracy of the numerical method is improved.

<!-- batch 13 | page 15 -->

#### 3 -19.2.1Single-Degree-of-Freedom Systms

As stated previously, a single degree of freedom system is one in which only one coordinate is essential to define its motion. The equation of motion for the singledegree-of-freedom system shown in Figure 3-42 (+) can be expressed as:

$$F-kx-cv=Ma $$

## where c= damping constant 

There are several methods that can be used to numerically integrate Equation 3-61, but the two procedures applied to this problem will be the average acceleration, and the acceleration-impulse extrapolation methods.



##### 3 -19.2.1.1 Average Acceleration Method

In the average acceleration method, the velocity and displacement at any time t are expressed as 



$$\begin{aligned}&v_{t}=v_{t-1}+1/2\left(a_{t}+a_{t-1}\right)\Delta t\\&x=x_{t-1}+1/2\left(v_{t}+v_{t-1}\right)\Delta t\\ \end{aligned}$$

Substituting Equation 3-62 into Equation 3-63,

$$\boldsymbol{x}=\boldsymbol{x}_{t-1}+\boldsymbol{v}_{t-1}\boldsymbol{\Delta t}+1/4\left(\boldsymbol{a}_t+\boldsymbol{a}_{t-1}\right)\boldsymbol{\Delta t}^2$$

Substituting Equations 3-62 and 3-63 into Equation 3-61, we have 

$$F-k J x_{t-1}+1/2(v_t+v_{t-1})\Delta t J-c J v_{t-1}+1/2(a_t+a_{t-1})\Delta t J=M a $$

Equation 3-65 can be simplified to 

$$\boldsymbol{a}=\frac{1}{m+\gamma_{2}c\Delta t+\gamma_{4}k\Delta t^{2}}\left[\boldsymbol{F}-k\left(\boldsymbol{x}_{t-1}+\boldsymbol{v}_{t-1}\Delta t+\gamma_{4}\boldsymbol{a}_{t-1}\Delta t^{2}\right)-c\left(\boldsymbol{v}_{t-1}+\gamma_{2}\boldsymbol{a}_{t-1}\Delta t\right)\right]$$

The integrating procedure can be summarized as follows:

Step 1.$\mathrm{A t}t=0$ :Compute:${\pmb a}_{o}$ using Equation 3-61 and specified values for $x_{o}(t=$ 0),$v_{o}(t=0),\mathrm{a n d}F(t=0)$ 



<!-- batch 13 | page 16 -->

Step 2.Increment time:$t=t+\Delta t$ 

Step 3.$\mathrm{A t}\;t=t+\Delta t.$ :Compute a.$(t=t+\Delta t)$ using Equation 3-66, v $(t=t+\Delta t)$ using Equation 3-62 and x $(t=t+\Delta t)$ ,using Equation 3-63.

Step 4.Repeat steps 2 and 3 until some specified time or until the maximum displacement is reached.



It should be noted that if x $(t=0)$ and v.$(t=0)$ are zero, then the system will not move as long as $F(t=0)$ is zero; however, if $F(t=0)$ is not zero, Equation 3-66 will give an acceleration and motion will start. Thus the system of equation is self-starting and requires no special starting provisions.



The procedure outlined above for an elastic single-degree-of-freedom system can be easily extended to accommodate elastic-plastic behavior. To do so, Equation 3-61 is rewritten to include the restoring force R which replaces the spring restoring force kx,Equation 3-61 becomes 



$$F-R-c v=m a $$

Substituting Equations 3-62 and 3-63 into Equation 3-67, the following equation for acceleration is obtained:

$$\boldsymbol{a}_{t}=\frac{1}{m_{+}(c\Delta t)}\left[\boldsymbol{F}-\boldsymbol{R}-c\left[\boldsymbol{v}_{t-1}+\Delta t\boldsymbol{a}_{t-1}/2\right]\right]$$

Unlike Equation 3-66, Equation 3-68 has a non-linear term R, and it depends on the displacement x at time t. Therefore, instead of using the direct integration approach as in the previous case, a predictor-corrector method is utilized. Briefly, the displacement x at time tis estimated (predicted) and then corrected and convergence of this procedure can be obtained in a single iteration if the value of Δt is small enough. The step-by-step procedure is outlined as follows:

Step 1.$\mathrm{A t}t=0$ :Compute at $(t=t_{O})$ from Equation 3-67 and the initial conditions.

Step 2.Increment time:$t=t+\Delta t$ 

Step 3.$At t=t+\Delta t\cdot\mathrm{Set}a_{t}=a_{t-1}(t-1=0,\mathrm{initally})$ 

Step 4.Compute $v_{t}$ and $x_{t}$ from Equations 3-62 and 3-63

Step 5.Compute R 

Step 6.Compute $a_{t}$ from Equation 3-68

<!-- batch 13 | page 17 -->

Step 7.If you are in the predicting pass, return to Step 4, if in the correcting pass,set $\mathbf{\chi}_{t-1}=\mathbf{\chi}_{t},\mathbf{\chi}_{t-1}=\mathbf{\chi}_{t},\mathbf{\bar{a}}_{t}=\mathbf{\bar{a}}_{t-1}$ and go to Step 2.



##### 3 -19.2.1.2Acceleration Impulse Extrapolation Method

Suppose the acceleration of the system is defined by Figure 3-4a (+). The acceleration-impulse extrapolation method assumes that the actual acceleration curve can be replaced by a series of equally spaced impulses occurring at $t_{O},t_{1},t_{2},...,t_{n}$ ,as shown in Figure 3-45b.



The magnitude of the acceleration impulse at $t_{n}$ is given by 

$$I(t_{n})=\boldsymbol{a}_{n}(\Delta t)$$

where $t-t_{1}-t_{0}=t_{2}-t_{1}=\ldots=t_{n}-t_{n-1}$ . This is shown in Figure 3-45b $(\pm)$ .Since an impulse is applied at $t_{n},$ there is a discontinuity in the value of velocity at $t_{n}$ In the time interval from t to $t_{n-i}$ , the velocity is constant and the displacement varies linearly with time. The velocity and displacement thus obtained are shown in Figure 3-45c (+) and Figure 3-45d 

$(\pm)$ 



Suppose $t_{n}^{\dagger}$ and $t_{n}^{\mathrm{~+~}}$ indicate the time immediately before and after the application of the impulse at $t_{n},$ and let $v_{n}$ and ${v_{n}}^{+}$ indicate respectively the velocity at $t_{n}$ and $t_{n}^{\mathrm{~\#~}}$ ; these two velocities are related by the following equation:

$$v_{n}^{+}=v_{n}^{-}+\bar{a}_{n}(\Delta t)$$

The relationship between $\pmb{X}_{n-1}$ and $x_{n}$ , and between ${\pmb x}_{n}$ and $\pmb{X}_{n\pm\mathcal{I}}$ are given by:

$$\begin{aligned}&\boldsymbol{x}_{n}-\boldsymbol{x}_{n-1}=\boldsymbol{v}_{n}^{-}(\Delta t)\\ &\boldsymbol{x}_{n+1}-\boldsymbol{x}_{n}=\boldsymbol{v}_{n}^{+}(\Delta t)\\ \end{aligned}$$

Combining Equations 3-70 and 3-71, the three successive displacements are related by:

$$x_{n+1}=2x_{n}-x_{n-1}+a_{n}(\Delta t)^{2}$$

This is the basic recurrence formula for the acceleration impulse extrapolation method.Once the values of x at $t_{n-1}$ and $t_{n}$ are known, the value at $t_{n+1}$ can be directly computed without resorting to a trial and error procedure.



<!-- batch 13 | page 18 -->

It is necessary, however, to use a special procedure in the first time interval because, at $t=0$ ,no value of $X_{n-1}$ is available. Two different procedures may be used. The first assumes the acceleration varies linearly up to the first time station, in which case, the displacement of the system at that time can be expressed as:

$$x_{1}=(1/6)(2a_{0}+a_{1})(\Delta t)^{2}$$

The second procedure assumes that the acceleration is constant during the first time interval and is equal to the initial value. This assumption results in the following expression for $\pmb{x}_{1};$ ,

$$x_{1}=(1/2)a_{0}(\Delta t)^{2}$$

It should be noted that Equation 3-73 has to be solved by trial and error since $a_{1}$ depends on $x_{1}$ . This trial-and-error procedure can be avoided by taking the value of $a_{1}\mathrm{t o}$ be $f(t)/m$ instead of the exact value of $\left[f(t_{1})-R(t_{1})\right]$ J/m. In Figure 3-46a (+)if $a_{o}=0,a_{o}$ _is equal to $a_{o}/6$ and in Figure 3-46b (+) if ${\pmb a}_{o}$ and $a_{1}$ are approximately equal to each other,the value $a_{o}/2$ 'may be used for ${\pmb a}_{o}$ . The recurrence formula is directly applicable for the evaluation of $\pmb{x}_{2},\pmb{x}_{3},...,\pmb{x}_{n+1}$ : whenever the acceleration is a continuous function. When there is a discontinuity in the acceleration, this equation can still be used but not before some modifications are made to reflect this discontinuity. In Figure 3-46a there is a discontinuity at $t_{4}$ which occurs at the end of the time interval Δt. Under this condition,the value of $a_{n}$ used in the numerical procedure is the average value at discontinuity,namely $1/2\left(a_{4}+a_{4}\right)$ for ${\pmb a}_{4},$ In Figure 3-46b the discontinuity occurs within time interval,t. The correct value for ${\pmb a}_{3}$ in this procedure is:

$$\boldsymbol{a}_{3}=(1/2)[\boldsymbol{a}_{3}+\boldsymbol{a}_{3}+(\boldsymbol{a}_{3}-\boldsymbol{a}_{3})(\Delta t/\Delta t)^{2}]$$

When there are more than two discontinuities, this procedure becomes cumbersome and it is more convenient to replace the given acceleration by a smooth curve. Equation 3-73 must be used if there is zero force (and hence zero acceleration) at zero time, for in no other way can $x_{\mathcal{I}}$ be determined. lf acceleration at $t=0$ is not zero, Equation 3-74may be used without appreciable error, provided the force does not change greatly in the first interval.



The tedious method of numerical analysis is made somewhat easier if the computation procedure is set up as shown in Table 3-14 (+). In the first time interval, the value used for the acceleration,${\pmb a}_{o}$ ,depends on the forcing function.If the value of the forcing function is zero at time zero, then ${\pmb a}_{o}$ is taken as one-sixth of $\pmb{a}_{\mathtt{I}},$ where a, is the ratio of the value of the forcing function at $t,$ to the mass of the system $\rho_{o}=f(t_{\perp})/6m J$ . When the value of the forcing function is not zero at time zero, and if the values of the forcing 

<!-- batch 13 | page 19 -->

function at times $t=0\mathrm{a n d}t=t_{1}$ are approximately equal, then ${\pmb a}_{o}$ may be taken as $(P_{o})$ $R_{o})/2$ . The recurrence formula (Equation 3-72) is used in the other intervals.

It may be necessary during the computational procedure, to increase the value of t so as to reduce the number of time intervals. In Figure 3-47 (+), for example, the forcing function varies linearly after time j. For the next time station $(j+1)^{\mathrm{s t}}$ ,the value of ∆t, can be increased $(\Delta t_{2}=2\Delta t_{1}$ for example) without introducing any errors in the computations.In such cases, caution has to be exercised when using the recurrence formula. In Table $3-14(\pm)$ ,the value of Δt changes after the $j^{\mathrm{{ 严 }}}$ step, to $\Delta t_{2}=2\Delta t_{1}$ .In the $(j+1)^{\mathrm{s t}}$ step,$X_{n-1}$ should be the value of x for the $(j-1)^{\mathsf{n d}}$ step and $x_{n}$ will be the value of $\pmb{X}_{n+1}$ for the $(j{-}1)^{\mathrm{s t}}$ step.



#### 3 -19.2.2A Two-Degree-of-Freedom-System

A two-degree-of-freedom system is shown in Figure 3-48 (+) where the coordinates defining the configuration of the system are $X_{i}$ and $X_{2}$ The equation of motion for each of the two masses can be expressed as follows:

$$\begin{aligned}&F_{1}+R_{2}-R_{1}=M_{1}\bar{a}_{1}\\&F_{2}-R_{2}=M_{2}\bar{a}_{2}\\ \end{aligned}$$

Equation 3-76 can be rewritten as:

$$\begin{aligned}\boldsymbol{a}_{1}&=F_{1}/M_{1}+R_{2}/M_{1}-R_{1}/M_{1}\\\boldsymbol{a}_{2}&=F_{2}/M_{2}-R_{2}/M_{2}\end{aligned}$$

The integration procedures described for a single-degree-of-freedom system can also be applied to two-degrees-of-freedom systems. In the average acceleration procedure,if the equations are placed in the same form as Equation 3-61, i.e., if the acceleration at time tare written in terms of displacements and velocities at time $\boldsymbol{t}-\Delta\boldsymbol{t},$ ,then two equations are obtained which must be solved simultaneously for $a_{1}$ and ${\pmb a}_{2},$ In the other numerical integration procedure, the recurrence formula (Equation 3-72) applies to each of the two displacements independently.



#### 3 -19.2.3Damping

The effects of damping are hardly ever considered in blast design because of the following reasons:

(1)Damping has very little effect on the first peak of response, which is usually the only cycle of response that is of interest.



(2)The energy dissipated through plastic deformation is much greater than that dissipated by normal structural damping.



<!-- batch 13 | page 20 -->

(3) lgnoring damping is a conservative approach.

If damping has to be considered in an analysis, however, it should be expressed as some percentage of critical damping. For free vibration, this is the amount of damping that would remove all vibration from the system and allow it to return to its neutral position. Critical damping is expressed as 



$$C_{c r}=2k M $$

where 

$$\begin{array}{l}{k=s t i f f n e s s o f t h e s y s t e m}\\ {M=m a s s o f t h e s y s t e m}\end{array}$$

The damping coefficient,$c,$ in Equations 3-61 and 3-67 is expressed as a percentage of critical damping,$C_{c r}$ . For steel structures, c should be taken as $0.05C_{c r}$ and $0.01~C_{c r}$ for reinforced concrete structures.



### 3 -19.3Design Charts for Idealized Loadings

#### 3 -19.3.1General

The response of single-degree-of-freedom systems subjected to idealized blast loadings is presented in the form of non-dimensional curves. In order to utilize these response charts, both the blast loads (pressure - time history) and the resistance-deflection curve of the structural system are idealized to linear or bilinear functions. Methods for computing these idealized blast loads are given in Chapter 2 while the methods for computing the resistance-deflection functions as well as converting the actual system to an elastic or elasto-plastic single-degree-of-freedom system have been presented in previous sections of this chapter.



The response of a structural system subjected to a dynamic load is defined in terms of its maximum deflection $X_{m}$ and the time $t_{m}$ to reach this maximum deflection. The dynamic load is defined by its peak value $P,$ duration $T,$ and shape. The response of the single-degree-of-freedom system with elastic response is defined in terms of the dynamic load factor (DLF). The response of the single-degree-of-freedom system with elasto-plastic response is defined in terms of its ultimate resistance $r_{u},$ yield deflection $X_{E}$ ,and natural period $T_{N}$ .Response charts relate the dynamic properties of the blast load (P and T) to those of the element $(r,X,T_{N})$ ,that is,$X_{m}X_{E}$ :and $t_{m}/T$ 'are plotted as a function of $r_{u}/P$ and $T T_{N}$ .More information is provided in the following sections.

Response charts have been prepared for simplified loads as well as for the more complex bilinear loadings. The simplified loadings include triangular, rectangular, step load with finite rise time, triangular with rise time and sinusoidal pulse. The idealized triangular loading is utilized in the analyses of acceptor structures. These structures are subjected to the effects of unconfined explosions, such as free-air or surface bursts or 

<!-- batch 13 | page 21 -->

partially confined explosions in donor structures which are fully vented. On the other hand, idealized instantaneously applied or gradually applied flat top loads are usually encountered in the design of roof elements of acceptor structures. These structures are subjected to very long duration loads produced by very large explosive quantities. The triangular loading with a rise time is similar to the previously mentioned triangular load except that it is an equivalent loading produced by the blast traversing an element. The sinusoidal loadings is usually associated with the vibrational type of load rather than blast induced input. The bilinear loading is utilized in the analysis of containment structures which allow partial venting of an explosion and in the analysis of acceptor structures where reflected pressures clear rapidly around the structure.

The effects of damping have not been included in the preparation of the response charts. In the design of the blast resistant structures, the first peak of response is usually the only cycle of response that is of interest since the maximum resistance and deflection is attained in that cycle. Damping has very little effect on this first peak and consequently, neglecting damping has negligible effects on maximum response calculations.



#### 3 -19.3.2Maximum Response of Linear Elastic System to Simplified Loads

To obtain the response of a linear elastic system, it is convenient to consider the concept of the dynamic load factor. This factor is defined as the ratio of the maximum dynamic deflection to the deflection which would have resulted from the static application of the peak load P, which is used in specifying the load-time variation. Thus the dynamic load factor (DLF) is given by:

$$D L F=X_{m}/X_{s}$$

where 

$X_{s}=$ static deflection or, in other words, the displacement produced in the system when the peak load is applied statically.



$X_{m}=$ maximum dynamic deflection 

Since deflections, spring forces, and stresses in an elastic system are all proportional,the dynamic load factor may be applied to any of these to determine the ratio of dynamic to static effects. Therefore, the dynamic load factor may be considered as the ratio of the maximum resistance attained to the peak load or:

$$D L F=r/p $$

<!-- batch 13 | page 22 -->

## where 

$r=$ maximum dynamic resistance $p=$ peak load used in specifying the load-time variation.

For a linear elastic system subjected to a simplified dynamic load, the maximum response is defined by the dynamic load factor, DLF and maximum response time,$t_{m}$ The dynamic load factor and time ratio $t_{m}/T$ are plotted versus the time ratio $T T_{N}$ for a triangular load, rectangular load, step load with finite rise time $(T_{r})$ ,triangular load with rise time, and sinusoidal pulse in Figure 3-49 through Figure 3-53.

In many structural problems only the maximum value of the $D L F$ is of interest. For the most prevalent load case, namely, the triangular load as well as the rectangular and step load with rise time, the maximum value of the $D L F$ is 2. This immediately indicates that all maximum displacements, forces, and stresses due to the dynamic load are twice the value that would be obtained from a static analysis for the maximum load P.

The above response charts apply for elastic systems. However, the charts can be applied to the entire elasto-plastic range if the actual resistance-deflection curve (two step system, three step system, etc.) is replaced by the equivalent elastic system where the equivalent elastic stiffness $K_{E}$ and the equivalent elastic deflection $X_{E}$ are obtained according to previously explained procedures (see Section 3-14).

In a typical design example, the pressure-time loading is calculated and idealized to one of the simplified loads defined by P and Tor $T_{r}$ . A structural member is assumed and its corresponding dynamic properties are calculated. For a completely elastic response, the values of $r_{e}$ and $T_{N}$ are calculated while for a response in the elasto-plastic range,$r_{u},X_{E}$ and $T_{N}$ are obtained. It should be noted that for a response in the elasto-plastic range,the value of $T_{N}$  is calculated using the effective mass which is an average of the elastic and elasto-plastic values. Knowing the ratio of $T T_{N}$ the dynamic load factor (DLF) and the time ratio can be read from the appropriate figures. The maximum resistance r attained by the structural member is calculated from the DLF and the response time is obtained from the time ratio. If the resistance r is greater than $r_{e}$ for a completely elastic response in the elasto-plastic range, then the analysis is not valid and the procedure is repeated. The maximum deflection is obtained from the resistance rand the stiffness $K_{e}$ or $K_{F}$ 



#### 3 -19.3.3Maximum Plastic Response of an Elasto-Plastic System to Simplified Loads

An elasto-plastic system may have an elastic or plastic response depending upon the magnitude of the blast load. If the response is elastic, that is, the member attains a resistance r which is less than its ultimate resistance $r_{u},$ then the charts of the preceding section are used. The response charts presented in this section are only for the plastic response of members where the ultimate resistance $r_{u}$ is attained.

<!-- batch 13 | page 23 -->

The maximum plastic response of an elasto-plastic system subjected to a blast load is defined by the maximum deflection,$X_{m}$ it attains and the time,$t_{m}$ it takes to reach this deflection. The blast load is defined by its peak value P and duration T while the singedegree-of-freedom system is defined by its ultimate resistance $r_{u},$ elastic deflection $X_{E}$ and natural period $T_{N}$ . A nondimensional response chart is constructed by plotting the ductility ratio $X_{m}/X_{E}$ and the time ratio $t_{m}/T$ as a function of $r_{u}/P$ 'and $T/T_{N}$ .Response charts are given for a triangular load, rectangular load, step load with finite rise time $T_{r}$ and triangular load with rise time in Figure 3-54 through Figure 3-61. It should be noted that for the step load with finite rise time, the load is defined by the rise time $T_{r}$ and,consequently, the response curves are plotted using $T_{r}$ rather than T.

In a typical example, the pressure-time loading is calculated and idealized to one of the simplified loads defined by either P and Tor P and $T_{r}$ . A structural member is assumed and its corresponding dynamic properties $(r_{u},X_{E},T_{N})$ are calculated. Knowing the ratios of $r_{v}P$ 'and $T/T_{N}(\mathrm{o r}~T_{r}/T_{N})$ 1, the ductility ratio $X_{m}X_{E}$ and the time ratio $t_{m}/T$ 'can be read from the appropriate figures. The maximum deflection $X_{m}$ and response time $t_{m}$ can readily be calculated. If the ductility ratio $X_{m}X_{E}$ or the maximum deflection $X_{m}$ and corresponding response time $t_{m}$ are unsatisfactory, the procedure is repeated.

It should be noted that the value of the natural period of vibration $T_{N}$ used in conjunction with the response charts varies according to the magnitude of the ductility ratio $X_{m}X_{E}$ For small plastic deformations $(X_{m}/X_{E}$ · less than 5), the calculations of $T_{N}$ is based on an average of the equivalent elastic and plastic masses. Whereas, for larger plastic deformations $(X_{m}/X_{E}$ greater than 5), the equivalent plastic mass is used to obtain $T_{N}$ 

#### 3 -19.3.4Maximum Plastic Response of an Elasto-Plastic System to Idealized Bilinear Loads

Response charts have been prepared for bilinear loads in much the same manner as for simplified loads. However, four parameters are required to define the bilinear loading rather than two parameters which are required for the simplified loads. These additional parameters greatly increase the number of charts required for the rapid prediction of the dynamic response of an elasto-plastic system. However, the computational procedures remain comparatively simple.



A bilinear load is ilustrated in Figure 3-62 (+). Four parameters are required to define this load shape, namely:

$P=\mathtt{p e a k}$ : pressure of shock load (primary pulse)

$C_{1}P=\operatorname{p e a k}$ : pressure of gas load (secondary pulse)

T = duration of shock load 

C2 T = duration of gas load 

It can be seen from Figure 3-62 (+) that the value of $C_{1}$ will always be less than 1 while the value of $C_{2}$ will always be greater than 1.



<!-- batch 13 | page 24 -->

Response charts for the bilinear load are prepared in the same way as the simplified loads except that each chart is prepared for a given value of $C_{1}$ and $C_{2}$ . The ductility ratio $X_{m}X_{E}$ versus $T T_{N}$ is plotted on each chart for various values of $P/r_{u},t_{m}/T_{N}$ and $t_{F}/T$ (where $t_{E}$ is the time to reach the maximum elastic deflection $\pmb{x}_{E})$ Therefore,each chart contains three families of curves. In addition, each chart contains one, two or three boundaries which are formed by symbols. These boundaries delineate regions of each chart where certain approximations are preferable to chart interpolation. These approximations involve modification of the bilinear load for the various regions. The loads considered for each of the regions are given in Figure 3-62 (+) while the boundaries for the various regions are defined in Figure 3-63 (+).

Numerous response charts are required for bilinear loads. Table 3-15 (+) lists the figure numbers of the response charts prepared for the selected values of $C_{1}$ and $C_{2}$ . These response charts are presented in Figure 3-64 through Figure 3-266.

To use the response charts, the first step is to enter Table 3-15 (+) with the required values of $C_{1}$ and $C_{2}$ . Locate the points in the table with coordinates $C_{1}$ _and $C_{2}$ The number in the box containing the point is the appropriate figure number to use to solve the problem. If the point is not located in a box having a number, the two or, more frequently, four numbers bracketing the point are the appropriate figure numbers to use.Interpolation for the required values of $C_{1}$ and $C_{2}$ must be performed. A graphical and mathematical interpolation procedure is presented in subsequent sections.

In a typical design, a structural member is assumed and the idealized resistance function defined by $r_{u},X_{E}$ and $K_{F}$ can be determined along with the natural period.$\mathsf{A s}$ previously explained for simplified loads; the equivalent mass used to calculated $T_{N}$ varies according to the amount of plastic deformation. Knowing the ratio of $P r_{u}$ and $T T_{N}$ , note if the intersection point corresponding to these parameters, is located in region A, B, C or D on the response chart(s) for the required values of $C_{1}$ and $C_{2}$ .The boundaries for these regions are represented by a line of asterisks, solid circles, and solid squares, as illustrated in Figure 3-63 (+).



The final step in obtaining the solution depends on which region of the response chart(s) is applicable. These regions were established to reduce the amount of calculations required for a solution by eliminating, where possible, interpolation between charts. Except for one of the four regions, the actual bilinear blast load is replaced by a simplified load. Solution of the response for these simplified loads will predict a solution which is within 10 percent of the exact solution. Of course, the exact solution of the response for the structural member in these three regions can be obtained by using the required response charts and interpolating, where required, between charts.

##### 3 -19.3.4.1 Region A

This region is defined as the area to the left of the solid circles on the response charts. If a chart does not have a line of solid circles, then region A does not exist. Figure 3-221(+), Figure 3-222 (+) and Figure 3-223 (+) illustrate this case.



<!-- batch 13 | page 25 -->

In region A the maximum dynamic response depends primarily upon the total impulse in the blast loading (area under the pressure-time curve). The actual pressure-time distribution does not significantly affect the maximum dynamic response because in these regions the durations T and $C_{2}T$ are small in comparison to the response time,$t_{m}$ of the structural member. In this region the response charts are not used and a solution is obtained by considering the modified loading shown in Figure 3-62a (+). This load shape yields the following equations:

$$\frac{X_{m}}{X_{E}}=\frac{1}{2}+\frac{\pi^{2}}{2}\left[\frac{P}{r_{u}}\frac{T}{T_{n}}F\right]^{2}$$

and 

$$\frac{t_{m}}{T_{n}}=\frac{1}{2}F\frac{P}{r_{u}}\frac{T}{T_{n}}$$

where 

$$F=C_{2}+\frac{C_{2}\left[1-C_{1}\right]\left[1-C_{2}\right]}{C_{2}-C_{1}}$$

##### 3 -19.3.4.2Region B

This region is defined as the area in the chart to the left of the asterisks. If a chart has no line of asterisks, then region B does not exist. Figure 3-65 (+/+/+) illustrates the case where region B does not exist.



In region B the maximum dynamic response depends primarily upon the gas load which is described by $C_{1}P$ and $C_{2}\dot{T}$ : The shock load described by P and T is neglected. This load condition is shown in Figure 3-62b (+). Therefore the solution is obtained from consideration of a single triangular load. The dynamic response is obtained from Figure 3-64 (+/+) which like Figure 3-54 (+) and Figure 3-55 (+) is for a triangular load and will yield the same results. When using Figure 3-64 it must be realized that the Pand T used in the chart are actually $C_{1}P$ and $C_{2}T$ ,respectively. In a typical design, enter Figure 3-64 with the normalized parameters,$C_{1}P/r_{u}$ and $C_{2}T/T_{N},$ ,and read the solution,

$X_{m}/X_{E},t_{m}/T_{N},\mathrm{a n d}t_{E}/C_{2}T$ 



Figure 3-63 (+) depicts region B as the area between the line of solid circles and the line of asterisks. lt should be understood that the solution technique associated with region B (i.e., neglect the shock load and use Figure 3-64 (+/+)) applies everywhere to the left 

<!-- batch 13 | page 26 -->

of the line of asterisks, including region A. In other words, two solution techniques are available in region A.



##### 3 -19.3.4.3Region D

This region is defined as the area in the charts to the right of the line of solid squares. If a chart has no line of solid squares, then region D does not exist. Figure 3-69 (+/+/+)illustrates the case where region D does not exist.



In region D the maximum dynamic response depends primarily upon the shock load which is described by P and T. The gas load described by $C_{1}P$ and $C_{2}T$ is neglected.This load condition is shown in Figure 3-62d (+). Therefore, the solution is obtained from consideration of a single triangular load. Similar to region B, the dynamic response is obtained from Figure 3-64$(\pm/\pm)$ which is for a triangular load. Unlike region B, the parameters, P and T which describe the load are used in the figure. Therefore, in a typical design, enter Figure 3-64 with the normalized parameters $P/r_{u}$ and $T T_{N}$ ,and read the solution,$X_{m}/X_{E},t_{m}/T_{N}$ and $t_{F}/_{I}$ _



##### 3 -19.3.4.4RegionC

This is the region in the charts which do not meet the definitions of regions A, B and D.In most charts, region C is the area to the left of the line of solid squares and to the right of the line of asterisks, as illustrated in Figure 3-63 (+). Region C does not exist in some charts, such as Figure 3-97$(\pm/\pm/\pm)$ which have over lapping regions A and D.

In region C, both the shock and gas load must be considered. Replacement of the actual bilinear load with a simplified load, as done for the other regions, will yield an incorrect solution. Therefore, in this region the response charts must be used. If the required values of $C_{1}$ and/or $C_{2}$ do not correspond to the response chart values,interpolation between response charts will be required to obtain a solution. In a few cases one or two response charts are needed, however, in general four response charts are required for a solution.



##### 3 -19.3.4.5Response Chart Interpolation

Interpolation between four response charts will usually be required for region C. For regions A, B, or D, if conditions warrant an exact solution rather than the approximate solution usually used in these regions, interpolation between charts may be required.Either a graphical or mathematical interpolation procedure may be employed. The method selected depends upon personal choice. A brief description of each procedure is presented below and an example of each is given in Appendix A.

Graphical interpolation requires a sheet of log-log graph paper. A convenient size is $2\times$ 1 cycle with the single-cycle axis representing $C_{1}$ and $C_{2},$ and the two-cycle axis representing the desired parameter $(X_{m}/X_{E},t_{m}/T_{N}\mathrm{o r}t_{E}/T)$ ,called Yfor ease of presentation. The appropriate figures to be used for a solution are obtained from Table 3-15 (+) for the required values of $C_{1}$ and $C_{2}$ . The procedure will illustrate the interpolation between four figures since this is by far the usual case. For the values of 

<!-- batch 13 | page 27 -->

$P r_{u}$ and $T T_{N}$ corresponding to the structural system selected, determine the desired parameter Y for each of the four figures. Organize a table in the same format as Table 3-16 (+) and enter each figure number and corresponding value of $C_{1},C_{2}$ and Y.

In the table,$C_{11}$ and $C_{21}$ are the values of $\complement_{1}$ and $\complement_{2}$ ,respectively, from Figure 1.Likewise,$C_{12}$ and $C_{22}$ are the values of $C_{1}$ and $C_{2}$ , respectively,from Figure 2, etc. The symbol $\mathsf{Y_{1}},$ is the desired parameter, such as $X_{m}/X_{E},$ , which is read from Figure 1. The symbol $\mathsf{Y}_{2}$ is the value read from Figure 2, etc. The interpolation is first performed for the required value of $C_{1}$ and then for the required value of $C_{2}$ . That is, with $C_{21}$ __constant,graphically interpolate on the log-log paper between points $(\mathsf{Y}_{1},\bar{C}_{11})$ and $(\mathsf{Y}_{2},\bar{C}_{12})$ to find $\mathsf{Y}_{a}$ corresponding to $C_{1}$ and $C_{21}$ , as shown on Figure 3-267$(\pm)$ .Similarly,with $C_{23}$ constant, graphically interpolate between $(\mathsf{Y}_{3},\bar{C}_{13})$ and $(\mathsf{Y}_{4},\bar{C}_{14})$ to find $\Upsilon_{b}$ corresponding to $C_{1}$ and $C_{23}$ also shown in Figure 3-267. The values of $\Upsilon_{d}$ and $\Upsilon_{b}$ are recorded in Table $3-16(+)$ Finally, with $C_{1}$ constant, graphically interpolate on the log-log paper between $(\mathsf{Y}_{a},\bar{C}_{i})$ and $(\mathsf{Y}_{b},\bar{C}_{23})$ to find Y corresponding to the required $C_{1}$ and $C_{2}$ as shown on Figure 3-267. The value of Y is the solution. Since there are three parameters to define the response of a structural, namely,$X_{m}/X_{E},t_{m}/T_{N}$ and $t_{F}/T$ ,the interpolation procedure is repeated three times, once for each parameter.



Mathematical interpolation requires the same initial steps as graphical interpolation.That is, the appropriate figures to be used for a solution are obtained from Table 3-15(+) and the required parameters are determined and entered into Table 3-16 (+).

Logarithmic equations are used to obtain the values of $\mathsf{Y}_{a},\mathsf{Y}_{b}$ and Y. The value of In $\Upsilon_{\alpha}$ is obtained from:

$$\ln Y_{a}=\ln Y_{1}+\frac{\ln\left(Y_{2}/Y_{1}\right)\ln\left(C_{1}/C_{11}\right)}{\ln\left(C_{12}/C_{11}\right)}$$

and the value of In $\Upsilon_{b}$ is obtained from:

$$\ln Y_{b}=\ln Y_{3}+\frac{\ln\left(Y_{4}/Y_{3}\right)\ln\left(C_{1}/C_{13}\right)}{\ln\left(C_{14}/C_{13}\right)}$$

Using the values of In $\Upsilon_{d}$ and In $\mathsf{Y}_{b};$ the value of InY is obtained from:

$$\mathrm{lnY}=\mathrm{lnY}_a+\frac{\left(\mathrm{lnY}_b-\mathrm{lnY}_a\right)\ln\left(C_2/C_{21}\right)}{\ln\left(C_{23}/C_{21}\right)}$$

The desired parameter Y is then obtained from:

<!-- batch 13 | page 28 -->

$$\boldsymbol{\mathsf{Y}}=\boldsymbol{\mathsf{e}}^{I n Y}$$

The above equations use natural logarithms. Common logarithms can be used to solve the above equations and then solve for Y using:

$$\gamma=10^{l o g Y}$$

It should be noted that if $C_{2}$ is represented by a response chart, then only two charts will be involved, and only Equation 3-83 will apply.



##### 3 -19.3.4.6Accuracy

The prediction error is less than 10 percent for the approximate solutions obtained in regions A, B and D. This is true provided the recommended procedures are employed,that is, the actual load is replaced by the approximate loads as shown on Figure 3-62$(+)$ and the solution is obtained using the equations provided for region A and using Figure 3-64$(\pm/\underline{{\pm}})$ for regions B and D.



Exact solutions are obtained from the response charts if the required values of $C_{1}$ and $C_{2}$ correspond to those given in the charts. This is true for all four regions. Errors result from interpolation between the response charts. The prediction error in $X_{m}X_{E}$ ·for region C, where interpolation between charts is required, is less than 10 percent provided response charts bounded by the dashed or solid lines on Table $3-15(+)$ are not used.The prediction error in $X_{m}X_{E}$ · will range from 55 to 100 percent for solutions in region C,if the point $(C_{1},C_{2})$  lies in the area bounded by the solid line in Table 3-15, and will range from 10 to 55 percent for the area bounded by the dashed line. If the solution involves charts from both sides of either the dashed or solid lines, the prediction error will range from 10 to 55 percent. The large interpolation error for these charts result from the big change in $X_{m}/X_{E}$ for a small change in $P/r_{u}$ which is peculiar to this chart.

It should be noted that the large errors described above will always be on the high side,that is, the predicted value of $X_{m}/X_{E}$ will always be greater than the exact value. Hence,a conservative design will always result. In addition, it should be noted that the prediction error in $t_{m}/T_{N}$ is about half the error in $X_{m}X_{E}$ 



While the errors produced from interpolation between the charts in Table 3-15 (+)bounded by the dashed and solid lines is large, the area in which they apply is small. As can be seen, region C is rather small on these charts. It is for points in this small area where interpolation must be performed. For the remaining areas (A, B and D), the approximate solutions may be used rather than interpolation. These approximate solutions will result in an error of less than 10 percent.



Solutions involving $0.920<C_{1}<1.00$ and $C_{2}\geq100$ can result in very large errors if interpolating procedures are employed. In this region, the dynamic response is primarily due to the gas load. Therefore, Figure 3-64 (+/+) is used to obtain $X_{m}/X_{F}$ for the gas 

<!-- batch 13 | page 29 -->

load. However, this value is too low and should be increased by 20 percent. The value of $t_{m}/T_{N}$ :corresponding to the increased value of $X_{m}X_{E}$ is then obtained from Figure 3-64.



#### 3 -19.3.5Determination of Rebound

In the design of elements which respond to the pressure only and pressure-time relationship, the element must be designed to resist the negative deflection or rebound which can occur after maximum positive deflection has been reached. The ratio of the required unit rebound resistance to the ultimate unit resistance $r r_{u}$ , such that the element will remain elastic during rebound is presented in Figure 3-268 (+) for a singledegree-of-freedom system subjected to a triangular loading function. Entering with ratios $X_{m}X_{E}$ and $t T_{N}$ , previously determined for design, the required unit rebound resistance $r$ can be read in terms of the originally designed ultimate unit resistance $r_{u}$ To obtain the rebound resistance for an element subjected to another form of load other than the triangular loading function, a time-history analysis such as the one described in Section 3-19 has to be performed.



It may be noted that if the loading is applied in a relatively short time compared to the natural period of vibration of the system, the required rebound resistance can be equal to the resistance in the initial design direction. When the loading is applied for a relatively long time, the maximum deflection is reached when the positive forces are stll large and the rebound resistance is reduced.



#### 3 -20ELEMENTS WHICH RESPOND TO IMPULSE.3-20.1General

When an element responds to the impulse, the maximum response depends upon the area under the pressure time curve (impulse of blast loading). The magnitude and time variation of the pressure are not important. The response charts presented in Section 319, which are based on pressure-time relationship are therefore not required for these problems. Instead, the element resistance required to limit the maximum deflection to a specific value is obtained through the use of a semigraphical method of analysis.

Consider the pressure-time and resistance-time functions shown in Figure 3-269 (+)The resistance curve depicted is for a two-way element with a resistance-deflection function having a post-ultimate range. From Newton's equation of motion it can be shown that the summation of the areas (considering area A as positive and area B as negative) under the load-time curves up to any time $t_{a}$ divided by the corresponding effective masses is equal to the instantaneous velocity of that time:

$$v_{a}=\int_{0}^{t_{a}}\frac{(f-r)d t}{m_{e}}$$

<!-- batch 13 | page 30 -->

The displacement at time $t_{\alpha}$ is found by multiplying each differential area divided by the appropriate effective mass by its distance to $t_{a}$ and summing the values algebraically:

$$X_{a}=\int\limits_{0}^{t_{a}}\frac{(f-r)}{m_{e}}[t_{a}-t]d t $$

In each range the mass is the effective plastic mass:


<div style="text-align: center;"><html><body><table border="1"><tr><td>Time Interval</td><td>Resistance</td><td>Effective Mass</td></tr><tr><td>$0\leq t\leq t_{1}$</td><td>$r_{u}$</td><td>$m_{u}=[K_{L M}]\;m_{u}$</td></tr><tr><td>$t_{1}\leq t\leq t_{m}$</td><td>$r_{u p}$</td><td>$m_{u p}=[K_{L M}]\;m_{u p}$</td></tr></table></body></html></div>


Time $t_{1}$ is the time at which the partial failure deflection $X_{\tau}$ occurs, and time $t_{m}$ is the time at which maximum deflection $X_{m}$ is reached $(X_{m}<X_{u})$ 1.



For an element to be in equilibrium at its maximum deflection, its impulse capacity must be numerically equal to the impulse of the applied blast load. With the use of the foregoing equations, the expressions which define the motion and capacity of elements subjected to impulse type loads, can be defined. These expressions are presented for both large and limited deflection criteria. This criteria varies for the different materials used in protective design. The criteria for each material is obtained from the chapter that describes the design procedures for that material.



## Case 1 - large deflections

Utilizing Equation 3-88 and by taking moments of the areas under the pressure-time and resistance-time curves (Figure 3-269$\left(\pm\right)$ about time $t_{m},$ assuming that the unit blast impulse $j_{b}$ is applied instantaneously at time $t=0$ ,and that time to reach yield $t_{\gamma}$ is also close to zero the expression for the maximum deflection is 

$$X_{m}=\frac{i_{b}t_{m}}{m_{u}}-\frac{r_{u}t_{1}[t_{m}-t_{1}/2]}{m_{u}}-\frac{r_{up}[t_{m}-t_{1}]}{2m_{up}}[t_{m}-t_{1}]$$

If moments of the areas are taken about $t_{1},$ then the deflection at partial failure (cid)$X_{\tau}$ , is 

$$X_{1}=\frac{\dot{I}_{b}t_{1}}{m_{u}}-\frac{r_{u}t_{1}^{2}}{2m_{u}}$$

<!-- batch 13 | page 31 -->

Using Equation 3-87 and summing the areas of $t_{m}$ and recognizing that the instantaneous velocity at $t_{m}$ equals zero.



$$\frac{i_{b}}{m_{u}}-\frac{r_{u}t_{1}}{m_{u}}-\frac{r_{u p}[t_{m}-t_{1}]}{m_{u p}}=0$$

Solution of the above three simultaneous equations is accomplished by solving Equation 3-91 for $t_{m}$ and substituting this expression into Equation 3-89, and solving Equation 3-90 for $t_{I}$ and substituting this expression into the modified Equation 3-89.After continuing and rearranging terms, the general response equation becomes 

$$\frac{{{i}_{b}}^{2}}{2m_{u}}=r_{u}X_{1}+\frac{m_{u}}{m_{u p}}r_{u p}(X_{m}-X_{1})$$

The left side of this equation is simply the initial kinetic energy resulting from the applied blast impulse and the right side is the modified potential energy of the element. The modification is required since the above analysis requires the use of two equivalent dynamic systems (before and after time $t_{1})$ .The modification factor $m_{u}/m_{u p}$ equates the two dynamic systems. If the effective mass in each range was the same,$m_{u}/m_{u}p$ would equal one and the right side of the expression would be $r_{u}X_{m}$ ,which is the potential energy.



For one-way elements which do not exhibit the post-ultimate resistance range, or for two-way panels where the maximum deflection $X_{m}$ is less than $X_{1}$ , Equation 3-92becomes 



$$\frac{{{i}_{b}}^{2}}{2m_{u}}=r_{u}X_{m}$$

The above solutions are valid only for what is considered large deflection design since the variation of resistance with deflection in the elasto-plastic range has been ignored.This limitation is based on the assumption that the time to reach yield $t_{\gamma}$ and the duration of the impulse $t_{o}$ are small in comparison to $t_{m}$ 1

## Case 2 - limited deflections

For elements which respond to the impulse with limited deflections where the time to reach maximum deflection $t_{m}$ is greater than three times the duration $t_{o}$ of the load, but where the support rotations are equal to or less than the established criteria, the elastoplastic range behavior of the element must be accounted for in determining the overall response of the element to the applied blast load. For this case, Equation 3-92 becomes 

<!-- batch 13 | page 32 -->

$$\frac{i_{b}^{2}}{2m_{a}}=\frac{r_{u}X_{E}}{2}+\frac{m_{a}}{m_{u}}r_{u}(X_{m}-X_{E})$$

where $m_{o}$  is the average of the effective elastic and plastic masses and $X_{E}$ the equivalent yield deflection.



When the response time $t_{m}$ of an element is less than three times the load duration $t_{o},$ the element will respond to the pressure pulse rather than to the impulse alone. In this case the response of the element may be obtained through the use of a response chart considering a simplified pressure pulse as outlined in Chapter 2. However, if the element's maximum deflection is greater than given in the response charts (ductility ratio $X_{m}X_{E}$ : greater than 100), the response of the element may be obtained through use of the semigraphical method of analysis as outlined in this paragraph considering the simplified pressure pulse. lt should be noted that the resistance time relationship used in the analysis to express the element's response should include the elasto-plastic region.



### 3 -20.2Determination of Time to Reach Maximum Deflection

The time $t_{m}$ for each of the cases covered previously can be determined by applying Equations 3-87 and 3-88 to the particular problem. The resulting equations are as follows:

Case 1 - large deflections.

A.$\mathsf{X_{1}}<\mathsf{X_{m}}\leq\mathsf{X_{u}}$ 

$$t_{m}=\frac{i_{b}}{r_{u}}+\left[\frac{m_{u p}}{m_{u}r_{u p}}-\frac{1}{r_{u}}\left[\dot{i}_{b}^{2}-2m_{u}r_{u}X_{1}\right]^{1/2}\right]$$

B.$\mathsf{X}_{\mathsf{m}}\leq\mathsf{X}_{1}$ 

$$t_{m}=i_{b}/r_{u}$$

Case 2 - limited deflections.

Since the variation of resistance with time is not known in the elasto-plastic range,$t_{m}$ can only be determined approximately by assuming a linear variation of resistance with time.



$$t_{m}(appox)=\frac{i_{b}}{r_{u}}\left[3-\frac{m_{u}}{2m_{a}}\right]+\frac{1}{r_{u}}\left[\frac{m_{u}}{2m_{a}}-1\right]\left[9i_{b}^{2}-6m_{a}r_{u}X_{E}\right]^{1/2}$$

<!-- batch 13 | page 33 -->

<div style="text-align: center;">Figure 3-45Acceleration Impulse Extrapolation Method </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_274_319_816_870.jpg" alt="Image" width="45%" /></div>


<div style="text-align: center;">Figure 3-46Discontinuities in the Acceleration Curve </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_164_1012_941_1350.jpg" alt="Image" width="65%" /></div>


<!-- batch 13 | page 34 -->

<div style="text-align: center;">Figure 3-47 Pressure-Time Function with Two Different Time Intervals </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_344_321_801_609.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;">TIME (t)</div>


<div style="text-align: center;">Figure 3-48A Two-Degrees-of-Freedom System </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_image_box_265_800_891_931.jpg" alt="Image" width="52%" /></div>


<!-- batch 13 | page 35 -->

<div style="text-align: center;">Figure 3-49Maximum Response of Elastic, One-Degree-of-Freedom System for Triangular Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_144_339_1026_1485.jpg" alt="Image" width="74%" /></div>


<!-- batch 13 | page 36 -->

<div style="text-align: center;">Figure 3-50Maximum Response of Elastic, One-Degree-of-Freedom System for Rectangular Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_152_340_1037_1480.jpg" alt="Image" width="74%" /></div>


<!-- batch 13 | page 37 -->

<div style="text-align: center;">Figure 3-51Maximum Response of Elastic, One-Degree-of-Freedom System for Gradually Applied Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_163_343_1017_1444.jpg" alt="Image" width="71%" /></div>


<!-- batch 13 | page 38 -->

<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_192_199_1011_1472.jpg" alt="Image" width="68%" /></div>


<!-- batch 13 | page 39 -->

<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_191_202_1011_1475.jpg" alt="Image" width="68%" /></div>


<!-- batch 13 | page 40 -->

<div style="text-align: center;">Figure 3-54Maximum Deflection of Elasto-Plastic, One-Degree-of-Freedom System for Triangular Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_149_331_1039_1414.jpg" alt="Image" width="74%" /></div>


<!-- batch 13 | page 41 -->

<div style="text-align: center;">Figure 3-55Maximum Response Time of Elasto-Plastic, One-Degree-ofFreedom System for Triangular Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_150_342_1042_1403.jpg" alt="Image" width="74%" /></div>


<!-- batch 13 | page 42 -->

<div style="text-align: center;">Figure 3-56Maximum Deflection of Elasto-Plastic, One-Degree-of-Freedom System for Rectangular Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_149_332_1035_1408.jpg" alt="Image" width="74%" /></div>


<!-- batch 13 | page 43 -->

<div style="text-align: center;">Figure 3-57Maximum Response Time of Elasto-Plastic, One-Degree-ofFreedom System for Rectangular Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_150_340_1039_1393.jpg" alt="Image" width="74%" /></div>


<!-- batch 13 | page 44 -->

<div style="text-align: center;">Figure 3-58Maximum Deflection of Elasto-Plastic, One-Degree-of-Freedom System for Gradually Applied Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_150_342_1029_1427.jpg" alt="Image" width="73%" /></div>


<!-- batch 13 | page 45 -->

<div style="text-align: center;">Figure 3-59Maximum Response Time of Elasto-Plastic, One-Degree-ofFreedom System for Gradually Applied Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_150_342_1028_1429.jpg" alt="Image" width="73%" /></div>


<!-- batch 13 | page 46 -->

<div style="text-align: center;">Figure 3-60Maximum Deflection of Elasto-Plastic, One-Degree-of-Freedom System for Triangular Pulse Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_149_335_1040_1416.jpg" alt="Image" width="74%" /></div>


<!-- batch 13 | page 47 -->

<div style="text-align: center;">Figure 3-61Maximum Response Time of Elasto-Plastic, One-Degree-ofFreedom System for Triangular Pulse Load </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_152_340_1027_1437.jpg" alt="Image" width="73%" /></div>


<!-- batch 13 | page 48 -->

<div style="text-align: center;">Figure 3-62Various Bilinear Triangular Loads </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_image_box_275_320_902_834.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">Figure 3-63Regions of Figures 3-64 Through 3-266, Labeling of Axis and Curves </div>


<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_image_box_191_934_993_1457.jpg" alt="Image" width="67%" /></div>


<!-- batch 13 | page 49 -->

<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_270_387_979_1309.jpg" alt="Image" width="59%" /></div>


(0==)

are rarr re ee r ser r e e e ee 

e eees e 

ee 

12120-020



<!-- batch 13 | page 50 -->

<div style="text-align: center;"><img src="../pages/batch 13/imgs/img_in_chart_box_249_390_1007_1316.jpg" alt="Image" width="63%" /></div>


(00 0000=)

are rar re ee r sr r e ee ee 