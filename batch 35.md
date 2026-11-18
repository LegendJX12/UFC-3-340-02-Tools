

<!-- batch 35 | page 1 -->

UFC 3-340-025 December 2008Change 2, 1 September 2014

# APPENDIX 6: SPECIAL  CONSIDERATIONS IN EXPLOSIVE  FACILITY DESIGN 

<!-- batch 35 | page 2 -->

# APPENDIX 6A ILLUSTRATIVE EXAMPLES 

\1\

## PROBLEM 6A-1 REINFORCED AND UNREINFORCED MASONRY WALL DESIGN 

### Problem 6A-1a:Design a reinforced masonry wall for an exterior blast load.Procedure:

Step 1.Establish design parameters.

a.Pressure-time loading 

b.Structural configuration including geometry, support conditions, and required Protection Category of wall.



Step 2.Select masonry unit size and the size and spacing of the primary steel reinforcement (i.e. vertical steel reinforcing bars) and secondary joint reinforcement. Also determine the static design strengths for the masonry and the steel reinforcement (Section 6-7.3).



Step 3.Calculate the dynamic design strengths of the masonry and steel reinforcement, using the static strengths from Step 2 and Table 6-2 (+)

Step 4.Using the dynamic design strengths from Step 3, the size and spacing of reinforcement, and d, the depth of the reinforcement, determine the ultimate moment capacity of the wall (Equation 6-2). Check that maximum and minimum requirements for reinforcement ratio and reinforcement spacing are met.



Step 5.Determine the ultimate resistance of the wall using the ultimate moment capacity of Step 4 and the equations of Table 3-1 (+) for one-way spanning elements.



Step 6.Determine the average moment of inertia based on $I_{n}$ and $I_{c}$ (Equation 610). Use Equation 6-1 to find the net moment of inertia of the masonry section $I_{n}$ Use Equation 6-11 and the depth of the reinforcement to calculate the moment of inertia of the cracked section Ic.

Step 7.Calculate the modulus of elasticity of the masonry unit $E_{m}$ from Equation 6-2 and the masonry unit compression strength of Step 2.

Step 8.Use the average moment of inertia from Step 6, the modulus of elasticity from Step 7, and the equations from Table 3-8 (+) to find the equivalent elastic stiffness.



Step 9.Determine the equivalent elastic yield deflection using the ultimate resistance (Step 5), the equivalent stiffness (Step 8), and Equation 3-36.

<!-- batch 35 | page 3 -->

Step 10.Find the load-mass factor,$K_{L M}$ ,for the elastic and plastic ranges from Table 3-12 (+). Average these values to determine the average value of $K_{L M}$ to be used for the wall response calculations. Calculate the areal mass (mass divided by the blast loaded area) of the masonry unit and multiply by $K_{L M}$ to obtain the effective areal mass of the wall.

Step 11.Calculate the natural period of vibration from Equation 3-60, the effective mass from Step 10 and the equivalent stiffness from Step 8.

Step 12.Determine response chart parameters.

a.Peak dynamic loading P (Step 1)

b.Ultimate resistance $r_{u}$ (Step 5)

C.Duration of load T (Step 1)

d.Natural period of vibration T (Step 11)

Calculate the ratio of ultimate resistance to peak dynamic loading (ru/P)and duration of load to natural period (T/T). Using these ratios and the appropriate figures (Figures 3-54 (+) through 3-266 (+/+/+)) determine the ductility ratio $\tilde{X}_{m}/X_{E}$ 



Step 13.Compute the maximum deflection $X_{m}$ by multiplying the ductility ratio by the elastic yield deflection of Step 9. From Table 3-5 (+) and the value of $X_{m}$ , find the maximum support rotation. Find the maximum rotation permitted from Table 6-3 (+) for the required Protection Category in Step 1and compare with the calculated maximum support rotation. If the rotation is larger than that permitted, repeat Steps 1 through 13.

Step 14.Determine the ultimate out-of-plane shear force at d from the support.Calculate the out-of-plane shear capacity based on the shear area (Equation 6-4) and shear strength (Equation 6-3). If the shear force exceeds the shear capacity, consider increasing the wall thickness and reducing the steel reinforcement to cause the wall to have the same ultimate resistance with a larger value of d, which will increase the shear capacity without increasing the shear force. Alternatively, the shear capacity can be increased with shear reinforcement (Equation 6-5) placed in the masonry mortar beds if the block height is less than d/2. However,this is not possible for CMU block unless 12 inch thick CMU is used with two layers of reinforcement.



Step 15.Use the ultimate resistance from Step 5 and equations in Table 3-9 (+) to calculate the ultimate shear load at the support for inbound response. Use $X_{m}/X_{E}$ and $T/T_{N}$ (both values from Step 12) to find the maximum rebound resistance from Figure 3-268 (+). Use this resistance and Table 3-9 (+) to 

<!-- batch 35 | page 4 -->

UFC 3-340-025 December 2008Change 2,1 September 2014calculate the rebound shear load at the support. Design the wal connections to resist both loads.



Step 16.Determine the in-plane shear load for the worst case shear wall and inplane shear area (Equation 6-4) and shear capacity (Equation 6-3) for the wall.  Check that the combined in-plane and out-of-plane shear satisfy the interaction formula (Equation 6-7).



<!-- batch 35 | page 5 -->

## EXAMPLE 6A-1MASONRY WALL DESIGN 

### Problem 6A-1a:Design a reinforced masonry wall for an exterior blast load.Solution:

Step 1.Given:

a.The design blast pressure history from a far range, exterior explosion is shown in Figure 6A-1a (+) below. This blast load has a peak pressure of 2 psi and the duration of 100 milliseconds. The wall will not be exposed to any fragmentation hazard and will not be placed in net tension from static or blast loads.



b.The wall is simply supported and spans vertically between the floor slab and roof diaphragm with a clear span of 150 inches. The wall must be designed for Protection Category 1. The wall is connected to the floor slab and roof diaphragm with dowels matching the wall reinforcement. The CMU walls are shear walls for the building,which has plan dimensions with an aspect ratio of 2:1. Only the grouted cells in the wall are reinforced. Since the design criteria satisfy the direct shear requirements of section 6-7.3.5, no direct shear check is required.



Step 2.Use 8 in thick (nominal thickness), medium weight, concrete masonry units (CMU) reinforced with No. 4 rebar at 16 in o.c. placed at midthickness in the wall. Use ladder or truss joint reinforcement with two longitudinal W1.7 wires in bed joints at every other course (16 inches).Assume the static compressive stress $(\pmb{f}_{m}^{r})$ is 2000 psi per Section 6-7.3.2and the reinforcement yield stress is 60,000 psi. The actual wall thickness T is 7.63 inches.



Step 3.Determine dynamic design stresses. (Table 6-2 (+))

Masonry (f{dm):

Compression $-1.19\ (2,000)=2,380\ \mathrm{ps}$ 

Diagonal tension $-1.00\left(2,000\right)=2,000\ ps$ 

Reinforcement (fdy):$-1.17(60,000)(1.1)=77,200\mathrm{ps}i$ 

Step 4.Determine the ultimate moment capacity of the wall and check that the minimum and maximum criteria for the reinforcement area and spacing are satisfied.



<!-- batch 35 | page 6 -->

a.Determine the ultimate moment capacity of the wall (Equation 6-9)

$$\begin{aligned}\bar{\boldsymbol{a}}=&\frac{A_{s}f_{ds}}{0.85b f_{dc}}\\\bar{\boldsymbol{a}}=&\frac{0.20\times77,200}{0.85\times16\times2380}=0.48i n c h\\M_{u}=&\frac{A_{s}f_{ds}}{b}(d-a/2)\\M_{u}=&\frac{0.20(77,200)(3.81-0.48/2)}{16}=3450i n-1b/i n c h\end{aligned}$$

$$\mathrm{F i g u r e}6A\mathrm{-}1a $$

<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_chart_box_360_630_825_1085.jpg" alt="Image" width="39%" /></div>


b.Check minimum and maximum steel ratio for reinforcement (Table 6-4(+))



$$\begin{aligned}&A_{s}\geq0.0006bd\\&0.2in^{2}\geq0.0006(16)(3.81)=0.037in^{2}\\ \end{aligned}$$

The reinforcing steel area exceeds the minimum requirement - OK 



$$\begin{aligned}&A_{s}\leq0.005bd\\&0.2in^{2}\leq0.005(16)(3.81)=0.30in^{2}\\ \end{aligned}$$

<!-- batch 35 | page 7 -->

The reinforcing steel area does not exceed the maximum requirement – OK 



C.Check that the maximum and minimum reinforcement spacing requirements are met (Section 6-8.3)



The spacing of the vertical rebar is 16 inches. This is not greater than the maximum spacing for walls not fully grouted of 3 times the nominal wall thickness (i.e. 24 inches), and it is not less than the minimum spacing of one bar per cell (i.e.8 inches) - OK 

Step 5.

Calculate ultimate resistance (Table 3-1 (+))

$$r_{u}=\frac{8M_{p}}{L^{2}}=\frac{8(3450)}{150^{2}}$$

Step 6.

Find the average moment of inertia of the wall.

a.Calculate the moment of inertia of net section (Equation 6-1 and Table 6-1 (+))



$$\begin{aligned}&I_{n}=I_{m}+\frac{(t-2t_{s})^{3}}{12}\frac{V}{100}\psi_{m}\\&\quad=27+\frac{(7.63-2(1.25))^{3}}{12}\frac{50}{100}(0.81)^{3}\\&\quad=31.6in^{4}/in\\ \end{aligned}$$

b.Calculate the moment of inertia of cracked section (Equation 6-11)

$$\begin{aligned}&J_{c}=0.005d^{3}\\ &\quad=0.005(3.81)^{3}\\ &\quad=0.27in^{4}/in\\ \end{aligned}$$

C.Calculate the average moment of inertia (Equation 6-10)

$$\begin{aligned}I_{a}=&\frac{I_{n}+I_{c}}{2}\\ =&\frac{31.6+0.27}{2}\\ =&15.9in^{4}/in\end{aligned}$$

<!-- batch 35 | page 8 -->

Step 7.Compute modulus of elasticity of the masonry unit (Equation 6-2).

$$\begin{aligned}E_{m}&=K_{m}f_{m}^{\prime}\\E_{m}&=900(2000)\\&=1.8\times10^{6}\mathrm{psi}\end{aligned}$$

Step 8.Determine the equivalent elastic stiffness of the wall (Table 3-8 (+)).

$$\begin{aligned}K_{E}&=(384E_{m}I_{a})/5L^{4}\\&=(384)(1.8\times10^{6})(15.9)/5(150^{4})\\&=4.34\mathrm{psi/in}\\ \end{aligned}$$

Step 9.Calculate the equivalent elastic deflection of the wall (Equation 3-36).

$$X_{F}=r_{u}/K_{F}=1.23/4.34=0.28\ in $$

Step 10.Calculate the effective areal mass of the wall.

a.Find the average load-mass factor $K_{L M}\left(\mathrm{T a b l e}3-12\underline{{{(+)}}}\right)$ 

Elastic $K_{L M}=0.78$ 

Plastic $K_{L M}=0.66$ 

For limited plastic deflections 

$$K_{LM}=[0.78+0.66]/2=0.72$$

b.Determine the areal weight (w) and areal mass (m) of the wall.Only the reinforced cells are assumed to be grouted, so the percentage of grout-filled cells, V, is 50%.

Using Equation 6-1 and Table 6-1 (+)

$$\begin{aligned}w=&\left(A_{rs}\rho_m+(1-A_{rs})\frac{V}{100}\rho_g\right)T\\=&\left(0.47\frac{115}{1728}+(1-0.47)\frac{50}{100}\frac{120}{1728}\right)7.63\\=&0.379\mathrm{psi}\\=&\frac{w}{g}\\=&\frac{0.379}{32.2(12)(1\times10^{-6})}=981\mathrm{psi}\frac{ms^2}{in}\end{aligned}$$

<!-- batch 35 | page 9 -->

C.Calculate effective areal mass 

$$\begin{aligned}{m_{e}}&{{}=K_{L M}m}\\ {}&{{}=0.72\times981}\\ {}&{{}=706\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}}\end{aligned}$$

Step 11.Determine the natural period of vibration of the wall (Equation 3-60).

$$\begin{aligned}T_{N}&=2\pi\left(m_{e}/K_{E}\right)^{1/2}\\&=2\pi\left(706/4.34\right)^{1/2}\\&=80\mathrm{m s}\\ \end{aligned}$$

Step 12.Determine the response of the wall.

a.Calculate design chart parameters 

$$T/T_{N}=100.0/80=1.25$$

$$r_{u}/P=1.23/2.0=0.62$$

b.From Figure 3-54 (+)

$$\mu=X_{m}/X_{E}=9.0$$

Step 13.Calculate maximum deflection and check support rotation.

a.Compute maximum deflection 

$$\begin{aligned}X_{m}&=\mu X_{E}\\&=9.0\times0.28\\&=2.52in\end{aligned}$$

$$\begin{aligned}\mathsf{Pb.}\quad&\mathsf{Callate support rotation(Table3-5(\pm))}\\&\mathcal{O}=\tan^{-1}(2X_m/L)\\&=\tan^{-1}(2\times2.52/150)\\&=1.9^\circ\end{aligned}$$

C.Compare the maximum support rotation with response criteria from Table 6-3 (+) for unreinforced wall with Protection Category 1.

$$\Theta=1.9^{\circ}\leq2^{\circ}\quad\text{O.K.}$$

<!-- batch 35 | page 10 -->

Step 14.Check out-of-plane shear strength of wall.

a.Calculate ultimate shear force (out-of-plane) at distance d from support.



$$\begin{aligned}V_{u o}&=r_{u}\left(\frac{L}{2}-d\right)\\&=1.23\left(\frac{150}{2}-3.81\right)\\&=87.5\mathrm{~lb}/\mathrm{in}\end{aligned}$$

b.Find shear area for out-of-plane shear (Equation 6-4a)

$$\begin{aligned}A_{no}=\left(A_{rs}+(1-A_{rs})\frac{V}{100}\right)d\\=\left(0.47+(1-0.47)\frac{50}{100}\right)(3.81)\\=2.8\mathrm{in}^2/\mathrm{in}\end{aligned}$$

C.Compute out-of-plane shear strength (Equation 6-3)

$$\begin{aligned}&V_{mo}=2\sqrt{f_m^{'}A_n}\\ &\quad=2\sqrt{2000}(2.8)\\ &\quad=250lb/in>87.5lb/in\\ \end{aligned}$$

The shear strength exceeds the shear force – OK 

Step 15.Design connections 

a.Find maximum rebound resistance 

$$\begin{aligned}{T/T_{N}=1.25}\\ {X_{m}/X_{E}=9.0}\end{aligned}$$

From Figure 3-268 (+)

$$r^{-}/r_{u}=0.98$$

$$r^{-}=0.98\times1.23=1.21\mathrm{ps}$$

The maximum rebound resistance is nearly equal to the ultimate resistance. The inbound and rebound connection force can both be based on the ultimate shear load at the support.

b.Calculate connection design load, which is equal to ultimate shear 

<!-- batch 35 | page 11 -->

force at support.

$$\begin{aligned}V_{u}=&\frac{r_{u}L}{2}\\ =&\frac{1.23(150)}{2}=92\ lb/in\end{aligned}$$

C.Check connection strength of dowels matching wall reinforcement acting in shear friction at supports (Equation 6-8). Note that the dynamic increase factor for shear reinforcing steel in Table 6-2 (+)is 1.0.



$$\begin{aligned}&V_{dm}=0.6A_{vd}f_{dy}\\ &\quad=0.6(\frac{0.2in^2}{16in})(66000)\\ &\quad=495Ib/j\eta>92Ib/j\eta\\ \end{aligned}$$

The direct shear strength of the dowels across the top and bottom support of the wall exceeds the connection design load – OK 

Step 16.Check the response of the wall as a shear wall resisting the dynamic reaction at the top of the wall on the perpendicular side of the building to blast load. Since the building plan has a 2:1 aspect ratio $(\mathsf{i.e.}~\mathsf{L_{2}}/\mathsf{L_{1}}=2)$ ,the in-plane shear can be calculated as shown below using $\mathsf{V}_{\mathsf{u}}$ in Step 15b.

a.Calculate in-plane shear force for the worst case shear wall.

$$\begin{aligned}V_{ui}=&\frac{V_{u}L_{2}}{2L_{1}}\\ =&\frac{(92lb/in)2}{2}\\ =&92lb/in\end{aligned}$$

b. Find the in-plane shear area (Equation 6-4b).$K_{v}=0$ for a partially grouted wall. The face shell thickness $t_{s}$ is shown in Table 6-1 (+)

$$\begin{aligned}{A_{n i}}&{{}=(K_{v}T+(1-K_{v})2t_{s})\frac{L_{v}}{L}}\\ {}&{{}=(0(7.63)+(1-0)(2)(1.25))0.8}\\ {}&{{}=2.0i n^{2}/i n}\\ \end{aligned}$$

<!-- batch 35 | page 12 -->

c. Compute the in-plane shear strength of the wall (Equation 6-3).

$$\begin{aligned}V_{mi}=2\sqrt{f_m}A_n\\=2\sqrt{2000}(2.0)\\=179lb/j\eta\end{aligned}$$

d. Check that the interaction equation for in-plane and out-of-plane shear is satisfied (Equation 6-7).  Note that t $\mathsf{V}_{\mathsf{s o}}$ and $\mathsf{V}_{\mathsf{s i}}$ are the in-plane and out-of-plane shear forces, respectively, resisted by shear reinforcement, which are both equal to zero in this case (i.e. wall has no shear reinforcement).



$$\begin{aligned}&\left(\frac{V_{u o}}{V_{m o}+V_{s o}}\right)^{2}+\left(\frac{V_{u i}}{V_{m i}+V_{s i}}\right)^{2}\leq1.0\\&\left(\frac{87.5}{250+0}\right)^{2}+\left(\frac{92}{179+0}\right)^{2}=0.38\leq1.0\\ \end{aligned}$$

The combined effect of in-plane and out-of-plane shear stress satisfy the interaction formula – OK.



<!-- batch 35 | page 13 -->

### PROBLEM 6A-1B:ANALYZE AN UNREINFORCED MASONRY WALL FOR AN EXTERIOR BLAST LOAD. 

## Procedure:

Step 1.Establish design parameters.

a.Pressure-time loading.

b.Structural configuration including geometry, support conditions, and required Protection Category of wall.



Step 2.Determine masonry unit size. Also determine a conservative estimate for the static strength for the masonry (Section 6-7.3).

Step 3.Calculate the dynamic design compressive and flexural strengths of the masonry using the static strength from Step 2, Table 6-2 (+), and Section 6-7.3.3.



Step 4.Using the dynamic flexural strength from Step 3, determine the ultimate moment capacity of the wall (Equation 6-12). Use cross sectional properties from Table 6-1 (+)



Step 5.Calculate the ultimate flexural resistance of the wall using the ultimate moment capacity of Step 4 and the equations of Table 3-1 (+) for one-way spanning elements.



Step 6.Determine the moment of inertia of the masonry section from Table 6-1(+).



Step 7.Calculate the modulus of elasticity of the masonry unit $E_{m}$ from Equation 6-2 and the masonry unit compression strength of Step 2.

Step 8.Use the moment of inertia from Step 6, the modulus of elasticity from Step 7, and the equations from Table 3-8 (+) to find the elastic stiffness.

Step 9.Determine the elastic yield deflection using the ultimate resistance (Step 5), the stiffness (Step 8), and Equation 3-36.



Step 10.Calculate the areal mass (mass divided by the blast loaded area) of the wall.



Step 11.Calculate the ultimate resistance from axial load arching using Equation 613.



Step 12.Construct the resistance-deflection curve for the wall response based on Figure 6-13 (+).



<!-- batch 35 | page 14 -->

Step 13.Determine the load-mass factor, KLm, for each stiffness region of the resistance-deflection curve.



Step 14.Calculate the natural period of vibration from Equation 3-6, using the areal mass from Step 10, the elastic stiffness from Step 8, and $\mathsf{K}_{\mathsf{L M}}$ for elastic flexural response from Step 13.



Step 15.Use a time-stepping dynamic analysis to determine the wall response.This is necessary because of the complex shape of the resistancedeflection curve. Use a time-stepping method to solve the equation of motion for the acceleration of the equivalent SDOF system representing the wall at each time step and use numerical integration to determine the corresponding velocity and displacement. See Section 3-19.2.1.1 for more explanation. Apply this method until a maximum deflection $X_{m}$ is calculated.



Step 16.Calculate the maximum support rotation of the wall using Table 3-5 (+)and the value of $X_{m}$ ,from Step 15. Use the information in Table 6-3 (+) to determine the maximum support rotation for the Protection Category in Step 1 and compare with the calculated rotation. If the calculated rotation is larger than that permitted, the wall must be structurally upgraded.

Step 17.Determine the ultimate out-of-plane shear force at d from the support based on the maximum resistance of the wall from Step 15. Calculate the out-of-plane shear capacity based on the shear area (Equation 6-4) and shear strength (Equation 6-3). If the shear force exceeds the shear capacity, the wall must be upgraded.



Step 18.Use the ultimate flexural resistance from Step 5 and equations in Table 39 (+) to calculate the ultimate shear load at the support for inbound response. Use this shear load as the connection load for inbound and rebound response. Compare this load to the capacity of the wall connections to its supports. Design upgrades for the wall connections if necessary.



Step 19.Determine the in-plane shear load for the worst case shear wall and inplane shear area (Equation 6-4) and shear capacity (Equation 6-3) for the wall. Check that the combined in-plane and out-of-plane shear satisfy the interaction formula (Equation 6-7).



<!-- batch 35 | page 15 -->

## PROBLEM 6A-1B:ANALYZE AN UNREINFORCED MASONRY WALL FOR EXTERIOR BLAST LOAD  

## Solution:

### Step 1.Given:

a.The design blast pressure history from a far range, exterior explosion has the same shape shown in Figure 6A-1a (+), except the peak pressure is 1.4 psi and the duration is 40 milliseconds.The wall will not be exposed to any fragmentation hazard and will not be placed in net tension from static or blast loads.

b.The 8 inch CMU wall spans vertically with simple supports at the floor slab and roof diaphragm with a clear span of 120 inches. It laterally supports a 4 inch brick non-structural veneer wall. The wall must provide Protection Category 1. The wall has #4 rebar dowels at 48 inches o.c. and a bond beam at the top. The CMU walls are shear walls for the building, which has plan dimensions with an aspect ratio of 2:1. The wall is ungrouted and is not a load-bearing wall. Since the design criteria satisfy the direct shear requirements of section 6-7.3.5,,no direct shear check is required.

Step 2.The wall is 8 in thick (nominal thickness), light weight, concrete masonry units (CMU) without any steel reinforcement or grouted cells. Assume the static compressive stress $(\pmb{f}_{m})$ is 1300 psi based a review of recommended values for ungrouted CMU. The actual wall thickness Tis 7.63 inches.

Step 3.Determine dynamic design stresses. (Table 6-2 (+))

Masonry:

$$\mathrm{Comprecision(f_{dm})-1.19(1,300)=1.547\mu ps i}$$

Flexural tension (fdt) - 200 psi (per Section 6-7.3.3)

Determine the ultimate moment capacity of the wal 

a. Determine the section modulus (S) for the CMU wall based on the moment of inertia (I) from Table 6-1 (+)



$$S=\frac{I}{T/2}=\frac{28}{3.81}=7.34\frac{in^{3}}{in}$$

b. Determine the ultimate moment capacity of the CMU wall based on the flexural tension strength (ft) from Step 3 and the section modulus using Equation 6-12. The axial load P is zero.



<!-- batch 35 | page 16 -->

$$\begin{aligned}&M_{du}=S\left(f_{dt}+\frac{P}{A}\right)\\&\quad=7.34(200+0)=1.468lb-in/in\\ \end{aligned}$$

Step 5.Calculate flexural ultimate resistance,$\mathsf{r}_{\mathsf{u}}$ , of the wall based on the ultimate moment capacity from Step 4 and equations in Table 3-1 (+)

$$\begin{aligned}r_{u}=&\frac{8M_{p}}{L^{2}}\\ =&\frac{8(1468)}{120^{2}}\\ =&0.82\mathrm{ps}i\end{aligned}$$

Step 6.Find the moment of inertia (I) of the CMU wall from Table 6-1 (+)

$$1=28\mathrm{i n}^{4}/\mathrm{i n}$$

Step 7.Compute the modulus of elasticity of the CMU masonry unit (Equation 62).



$$\begin{aligned}E_{m}&=K_{m}f_{m}^{\prime}\\E_{m}&=900(1300)\\&=1.2\times10^{6}\mathrm{psi}\end{aligned}$$

Step 8.Determine the elastic stiffness of the CMU wall (Table 3-8 (+))

$$\begin{aligned}K_{E}&=(384E_{m}I)/5L^{4}\\&=(384)(1.2\times10^{6})(28)/5(120^{4})\\&=12.4\mathrm{psi/in}\\ \end{aligned}$$

Step 9.Calculate the elastic deflection of the CMU wall (Equation 3-36).

$$X_{F}=r_{u}/K_{F}=0.82/12.4=0.07\ln $$

Step 10.Calculate the areal mass of the CMU wall and brick veneer wall. Assume the density of the light weight CMU is 95$\mathsf{I b}/\mathsf{f t}^{3}$ and the density of the brick is 120 Ib/ft3}.



a.Determine the areal weight of CMU using Equation 6-1 and Table 6-1 (+) and add the weight of the laterally supported brick veneer (W). The percentage of grout-filled voids, V, is zero.

<!-- batch 35 | page 17 -->

$$\begin{aligned}\boldsymbol{w}&=\left(\boldsymbol{A}_{rs}\rho_m+(1-\boldsymbol{A}_{rs})\frac{\boldsymbol{V}}{100}\rho_g\right)\boldsymbol{T}+\boldsymbol{w}_s\\&=\left(0.47\frac{95}{1728}+(1-0.47)\frac{0}{100}\frac{120}{1728}\right)\boldsymbol{T}\boldsymbol{\rho}_{63}+\left(\frac{120}{1728}\right)\boldsymbol{3}\boldsymbol{\rho}_{63}\\&=0.45\mathrm{ps}\boldsymbol{i}\\ \end{aligned}$$

b. Covert the areal weight of wall to areal mass (m).

$$\begin{aligned}m=&\frac{\mathrm{W}}{\mathrm{g}}\\=&\frac{0.45}{32.2(12)(1\times10^{-6})}=1165psj\frac{ms^{2}}{in}\end{aligned}$$

Step 11.Calculate the peak resistance from axial load arching $r_{a}$ (Equation 6-13).Use $X_{e}$ from Step 9 and w from Step 10.



$$\begin{aligned}&r_{a}=\frac{8}{L^{2}}\left(T-2X_{E}\right)\left(P+\frac{wL}{2}\right)\\ &=\frac{8}{\left(120\right)^{2}}\left(7.63-2(0.07)\right)\left(0+\frac{(0.45)(120)}{2}\right)=0.11ps i\\ \end{aligned}$$

Step 12.Construct the resistance-deflection curve for the wall (Figure 6-13 (+)).

This is shown below in Figure 6A-1b (+). This figure also shows a negative response region for the resistance-deflection curve, although it is acceptable to only model the inbound portion of the curve if the peak rebound resistance is assumed equal to the peak inbound resistance (as is typical). The rebound portion of the resistance-deflection curve is based on axial load arching without brittle flexural response since the wall is assumed to crack all the way through the thickness after peak flexural response (at deflections greater than $\mathsf{X}_{\mathsf{e}})$ during inbound response.The wall can be assumed to initially rebound with a stiffness equal to the initial flexural stiffness until the resistance becomes zero, and then to deflect with zero resistance until the deflection is negative and axial load arching can begin in the rebound direction as shown in Figure 6A-1b.

Step 13.Determine $K_{L M}$ for each stiffness region of resistance-deflection curve Section 6-9.2).



a.Find the values of K for elastic and plastic response (Table 3-12(+)).



Elastic $K_{L M}=0.78$ (applicable for deflections not exceeding $\mathsf{X}_{\mathsf{e}})$ (,)

<!-- batch 35 | page 18 -->

Plastic $K_{L M}=0.66$ (applicable for all larger deflections)

c. Assign the elastic and plastic $K_{L M}$ _to each stiffness region.

Response during the initial elastic stiffness has the elastic $K_{L M}.~A11$ subsequent response occurs with the plastic $K_{L M}$ as explained in Section 6-9.2.



<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_image_box_132_452_1043_959.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">Step 14.Determine the natural period of vibration (Equation 3-60). Because most of the wall deflection from blast load is expected to exceed the very small yield deflection $(\mathsf{X}_{\mathsf{e}})$ of 0.07 inches, the plastic value of $K_{\mathrm{L M}}=0.6\dot{6}$ from Step 13a will be used to calculate the natural period for the wall.</div>


$$\begin{aligned}T_{N}&=2\pi\left(\mathsf{K}_{\mathsf{L M}}m/\mathsf{K}_{E}\right)^{1/2}\\&=2\pi\left\{(0.66)(1165)/12.4\right\}^{1/2}\\&=49\;\mathrm{m s}\\ \end{aligned}$$

Step 15.Given the complex shape of the resistance-deflection function, a numerical integration procedure must be used to determine the wall deflection. This procedure is discussed in Section 3-19.2.1.1. The procedure calculates the wall's deflection in discrete time intervals. To ensure sufficient accuracy, these time intervals should be less than onetenth of the wall's natural period. The time step should also be based on the type of numerical integration that is used. If a simplified integration 

<!-- batch 35 | page 19 -->

method is used, a smaller time step is needed to accurately model the large changes in slope in the resistance-deflection curve. In this case a simple constant velocity integration method was used, with a time step of 0.1 ms. The calculated deflection history of the wall is shown below. The same result was obtained when the time step was reduced by a factor of 2.



<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_chart_box_144_449_1042_698.jpg" alt="Image" width="75%" /></div>


Step 16.Determine maximum deflection and check support rotation.

a.Determine maximum deflection from the calculated deflection history for the wall 



$$X_{m}=1.6inchees $$

b.Calculate support rotation (Table 3-5 (+))

$$\begin{aligned}&\Theta=\tan^{-1}(2X_m/L)\\ &=\tan^{-1}(2\times1.6/120)\\ &=1.5^{\circ}\\ \end{aligned}$$

C.Compare the maximum support rotation with response criteria from Table 6-3 (+) for unreinforced walls with Protection Category 1

$$\Theta=1.5^{\circ}\leq1.5^{\circ}\quad\text{Q.K.}$$

d.Compare the maximum deflection to wall thickness ratio with response criteria from Table 6-3 (+) for unreinforced walls with Protection Category 1



$$X_{m}/T=1.6/7.63=0.21\leq0.5$$

### Step 17.Check wall shear strength 

a.Calculate maximum shear force at distance d from support. This is the full wall thickness for an unreinforced wall.

<!-- batch 35 | page 20 -->

$$\begin{aligned}V_{u o}&=r_{u}\left(\frac{L}{2}-T\right)\\&=0.82\left(\frac{120}{2}-7.63\right)\\&=43\mathrm{~lb}/\mathrm{in}\end{aligned}$$

b.Find shear area for out-of-plane shear (Equation 6-4a). The percentage of grout-filled voids Vis zero.

$$\begin{aligned}A_{no}=\left(A_{fs}+(1-A_{fs})\frac{V}{100}\right)T\\=\left(0.47+(1-0.47)\frac{0}{100}\right)(7.63)\\=3.6\ln^2/\ln\end{aligned}$$

C.Calculate the out-of-plane shear strength (Equation 6-3)

$$\begin{aligned}&V_{mo}=2\sqrt{f_m^{'}}A_n\\&\quad=2\sqrt{1300}(3.6)\\&\quad=260Ib/j\eta>43Ib/j\eta\\ \end{aligned}$$

The shear strength exceeds the shear force –OK 

### Step 18.Design connections 

a.Calculate the connection design load, which is equal to the ultimate shear force at the support. This will be used for the inbound and rebound design connection load. The calculated maximum resistance in rebound from the time-stepping SDOF analysis is less than $\mathsf{r}_{\mathsf{u}}$ . However, a lesser blast load could cause a maximum inbound deflection less than $\mathsf{X_{e}}$ and the maximum rebound resistance could be nearly equal to $\mathsf{r}_{\mathsf{u}}$ in this case.

$$\begin{aligned}V_{u}=&\frac{r_{u}L}{2}\\ =&\frac{0.82(120)}{2}=49lb/in\end{aligned}$$

b.Check the connection strength of the dowels at the bottom of the wall (Equation 6-8).A comparison of the dowel development length in the wall (24 inches) with the required length to develop the full dynamic yield strength of the #4 dowel bars per TMS 402/ACI 

<!-- batch 35 | page 21 -->

530/ASCE 5 (32 inches) shows that the dowels can develop 24/32$0.75,\mathrm{or}75\%$ 1. of their dynamic yield strength. Note that the dynamic increase factor for shear reinforcing steel in Table 6-2 (+)is 1.0.



$$\begin{aligned}&V_{dm}=0.6A_{vd}f_{dy}\\ &\quad=0.6(\frac{0.2in^2}{48in})(66000)=165lb/in\\ &\quad=(165lb/in)0.75=124lb/in>49lb/in\\ \end{aligned}$$

The direct shear strength of the dowels at the bottom support of the wall exceeds the connection design load –OK 

C.The structural plans do not provide sufficient details on the connection of the roof diaphragm to the walls. The connection should be upgraded with a ledge angle that is connected to the roof deck with self-drilling screws and connected to the bond beam with drilled anchor bolts. The connections should be designed to resist a factored load of 49 Ib/in using LRFD or an allowable load of 49

$\mathrm{l b}/\mathrm{i n}/1.7=29\mathrm{l b}/\mathrm{i n}$ 



Step 19.

Check the response of the wall as a shear wall resisting the dynamic reaction at the top of the wall on the perpendicular side of the building to blast load. Since the building plan has a 3:1 aspect ratio $(\mathsf{i.e.}~\mathsf{L_{2}}/\mathsf{L_{1}}=3)$ the in-plane shear can be calculated from as shown below using $\mathsf{V}_{\mathsf{u}}$ in Step 18a.



a.Calculate in-plane shear force for the worst case shear wall.

$$\begin{aligned}V_{ui}=&\frac{V_{u}L_{2}}{2L_{1}}\\ =&\frac{49Ib/\ln(3)}{2}\\ =&74lb/\ln\end{aligned}$$

b.Find the in-plane shear area (Equation 6-4b). The face shell thickness $t_{s}$ is shown in Table 6-1 (+)



$$\begin{aligned}A_{ni}=(K_v T+(1-K_v)2t_s)\frac{L_v}{L}\\=(0(T)+(1-0)(2)(1.25))0.8\\=2.0in^2/in\end{aligned}$$

<!-- batch 35 | page 22 -->

C.Compute the in-plane shear strength (Equation 6-3).

$$\begin{aligned}&V_{mi}=2\sqrt{f_{m}^{'}}A_{ni}\\&\quad=2\sqrt{1300}(2.0)\\&\quad=144Ib/j\eta\\ \end{aligned}$$

d.Check that the interaction equation for in-plane and out-of-plane shear is satisfied (Equation 6-7). Note that $\mathsf{V}_{\mathsf{s o}}$ and $\mathsf{V}_{\mathsf{s i}}$ are the inplane and out-of-plane shear forces,respectively, resisted by shear reinforcement, which are both equal to zero in this case (i.e. wall has no shear reinforcement).



$$\begin{aligned}&\left(\frac{V_{u o}}{V_{m o}+V_{s o}}\right)^{2}+\left(\frac{V_{u i}}{V_{m i}+V_{s i}}\right)^{2}\leq1.0\\&\left(\frac{43}{260+0}\right)^{2}+\left(\frac{74}{144+0}\right)^{2}=0.29\leq1.0\\ \end{aligned}$$

The combined effect of in-plane and out-of-plane shear stress satisfy the interaction formula – OK.



<!-- batch 35 | page 23 -->

## PROBLEM 6A-2DESIGN OF PRESTRESSED PRECAST ROOF BEAM 

### Problem:Design a prestressed precast roof beam for a given blast load.Procedure:

Step 1.Establish design parameters.

a.Pressure-time loading 

b.Material strength 

C.Span length 

d.Static loads 

e.Deflection criteria 

Step 2.Select a standard precast section from the PCI Design Handbook or manufacturer's catalogs. Also select a standard strand pattern.

Step 3.Determine dynamic increase factors for concrete and reinforcement from Section 6-12. Increase the static design stress of the reinforcing bars and welded wire fabric 10 percent for the average yield stress. Calculate the dynamic design stresses using the above DiF and the static stresses.

Step 4.From Chapter 4 and a unit weight of concrete equal to 150 pcf, calculate the modulus of elasticity for concrete. With the above modulus for concrete and those for reinforcing bars and prestressing tendons,calculate the modular ratio.



NOTE: If the section has a flange (e.g. a single or double tee section) it must be designed according to the principles of Chapter 4. The flange is a one-way, non-prestressed slab spanning between webs. The critical section is usually a cantilever.



Step 5.Calculate the properties of the section.

a.Gross area 

b.Gross moment of inertia 

C.Unit weight 

d.Distance from extreme compression fiber to the centroid of the prestressing tendon, dp 



e.Area of prestressing tendons 

f.Prestressed reinforcement ratio (Equation 6-17)

<!-- batch 35 | page 24 -->

Step 6.Given the type of prestressing tendon, determine $\gamma_{p}$ . Using the dynamic concrete stress from Step 3, calculate β. Using Equation 6-21, 6-22 or 623 and the values of $\gamma_{p}$ and $\beta_{1}$ from above, calculate the average stress in the prestressing tendon.



Step 7.With the reinforcement ratio from Step 5e, the average stress in the prestressing tendon and the value of $\beta_{1}$ from Step 6, and the dynamic strength of materials from Step 3, check that reinforcement ratios are less than the maximum permitted by Equation 6-24 or 6-25.

Step 8.Using the area of reinforcement and the value of $d_{p}$ from Step 5, the dynamic stresses of Step 3, and the average stress in the prestressing tendon from Step 6, calculate the moment capacity of the element (Equations 6-14 and 6-15).



Step 9.With the equations of Table 3-1 (+) and the moment capacity of Step 8,calculate the ultimate unit resistance. As precast buildings are only subject to low blast pressures, the static loads become significant. To determine the resistance available to resist the blast load, subtract the static dead and live loads from the ultimate unit resistance.



Step 10.Calculate the moment of inertia of the cracked section $I_{\tt c},$ using Equation 6-27, the modular ratio from Step 4 and the area of prestressing tendons,the value of $d_{p}$ and the prestressed reinforcement ratio from Step 5. Using this value of $I_{c}$ and the gross moment of inertia of Step 5b, find the average moment of inertia from Equation 6-26.



Step 11.Using the equations of Table 3-8 (+), the modulus of elasticity for concrete from Step 4 and the average moment of inertia from Step 10, calculate the elastic stiff ness of the section.



Step 12.Determine the load-mass factor $K_{L M_{1}}$ ,in the elastic range for the appropriate loading condition from Table 3-12 (+). Also, calculate the unit mass of the section and multiply it by $K_{L M}$ to obtain the effective unit mass of the element.



Step 13.With Equation 3-54, the effective mass from Step 12 and the elastic stiffness from Step 11, calculate the natural period of vibration $T_{N}$ , of the section.



Step 14.Determine the response chart parameters.

a.Duration of load T (Step 1)

b.Natural period of vibration $T_{N}$ (Step 13).

Calculate the ratio $T/T_{N}$ and using this ratio, determine the dynamic load factor DLF from Figures 3-49 (+) through 3-53 (+). Section must remain 

<!-- batch 35 | page 25 -->

elastic, and hence the actual resistance obtained by the element (which is equal to the peak dynamic load from Step 1 multiplied by the DLF) must be less than the resistance available.



If the section does not remain elastic Steps 1 through 14 must be repeated.



NOTE: For bilinear loads, calculate the ratio of the peak dynamic load Pto the resistance available. Using $P/r_{u}$ and the value of $T/T_{N}$ calculated above, enter the appropriate response chart (Figures 3-64$(\underline{{\pm}}/\underline{{\pm}})$ through 3266$(\underline{{+}}/\underline{{+}}/\underline{{+}}))$ Iand find the ductility ratio $X_{m}/X_{E}$ . For the section to remain elastic the ductility ratio must be less than or equal to one.

Step 15.Calculate the deflection of the element $X_{m}$ by adding the dead and live loads (Step 1), and the resistance obtained by the structure (Step 14) and dividing by the elastic stiffness (Step 11). Using the deflection and the equations of Table 3-5 (+), determine the support rotation. Compare the rotation with deflection criteria of Step 1e. If comparison is satisfactory continue with Step 16. If comparison is not satisfactory repeat Steps 1through 15.



Step 16.Calculate the elastic deflection $X_{m}$ from Equation 3-30, using the ultimate resistance of Step 9 and the elastic stiffness of Step 11. Then calculate the ductility ratio $X_{m}/X_{E}$ using the value of $X_{m}$ from Step 15. With the ductility ratio and the ratio $T/T_{N}$ from Step 14, enter Figure 3-28 (+) and find the percentage of rebound. Extrapolate if necessary.

Step 17.Find the required rebound resistance by multiplying the ultimate unit resistance by the ratio from Step 16 and subtracting the dead load. In no case should the required rebound resistance be less than half the resistance available during the loading phase. With equations of Table 3-1(+) and the required rebound resistance, find the required rebound moment capacity.



Step 18.Calculate an approximate value of d and the amount of concrete strength available for rebound (Equation 6-29). Assume a depth of the equivalent rectangular stress block and, by a trial and error method, using Equation 6-34 find the area of rebound reinforcement required. Check that the amount of reinforcement does not exceed the maximum permitted by Equation 6-30 or 6-31.



Step 19.Calculate the shear stress at $d_{p}$ away from the support. Also calculate the allowable shear stress on an unreinforced web using the dynamic design stress (Step 16). Design the shear reinforcement.

Step 20.Calculate the shear at the support $V_{d}$ from the equations of Table 3-9 (+)and the value of the total load. Calculate the maximum allowable direct shear using the dynamic concrete strength.



<!-- batch 35 | page 26 -->

Compare the allowable shear with $V_{d}$ .If $V_{d}$ is greater than the size of the section must be increased.



Step 21.Check if section is adequate for service loads using the PCl Design Handbook and the ACI Code.



<!-- batch 35 | page 27 -->

## EXAMPLE 6A-2DESIGNOF A PRESTRESSED PRECAST ROOF BEAM 

#### Required:Design a prestressed precast roof beam subject to a blast load. Use a double tee section. 

Solution:

Step 1.Given:

a.Pressure-time loading (Figure 6A-2 (+)).

b.Material strengths 

Concrete:

$$\begin{array}{r l r}{f_{c}^{\prime}}&{{}=}&{5000\;\mathrm{p s i}}\end{array}$$

Prestressing Steel:

$$\begin{array}{r l r}{f_{p u}}&{{}=}&{270,000\;\mathrm{p s i}}\end{array}$$

$$f_{p v}/f_{p u}=0.85$$

Welded Wire Fabric 

$$\begin{array}{r l r}{f_{v}}&{{}=}&{65,000\;\mathrm{p s i}}\end{array}$$

Reinforcing Bars 

$$\begin{array}{r l r}{f_{v}}&{{}=}&{60,000\;\mathrm{p s i}}\end{array}$$

C.Span length is $40ft=480in$ 

d.Live load is 15 psf 

e.Maximum ductility $\mathsf{r a t i o}<1.0$ 

Maximum support rotation < 2°

Step 2.Select a double tee section and strand pattern.

Try 8DT24 (Figure 6A-2 (+)

Section properties from PCI Design Handbook:

$$\begin{aligned}&A=401in^2\quad&y_t=6.85in\\&I=20.985in^2\quad&w=418lb/ft\\ \end{aligned}$$

Try strand pattern 48-S, two 1/2 inch diameter straight strands in each tee.

Area of each $\mathrm{strand}=0.153\mathrm{in}^{2}$ 

$$e=14.15in $$

<!-- batch 35 | page 28 -->

<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_chart_box_499_299_725_543.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">PRESSURE-TIME LOADING </div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_image_box_267_620_921_1080.jpg" alt="Image" width="54%" /></div>


#### Step 3.Determine design stresses. (From Section 6-12)

a.Dynamic Increase Factors Concrete flexure:1.19Concrete diagonal tension:1.00Concrete direct shear:1.10Prestressing Steel:1.00Welding Wire Fabric:1.10Reinforcing Steel flexure:1.17

<!-- batch 35 | page 29 -->

Reinforcing Steel shear:1.00

b.Dynamic strengths 

Concrete 

-flexure:

$$f_{dc}=1.19\times5,000=5950\mathrm{psi}$$

- diagonal tension:$f_{dc}=1.0\times5,000=5000\mathrm{ps}$ 

- direct shear:$f_{dc}=1.1\times5,000=5500\mathrm{psi}$ 

Prestressing Steell:

$$f_{dv}=1.0\times270,000=270,000ps $$

Welded Wire Fabric:

$$f_{dv}=1.10\times1.10\times65,000=78,650\mathrm{psi}$$

Reinforcing Bars 

-flexure:

$$f_{d v}=1.17\times1.10\times60,000=77,220\mathrm{~ps}$$

- shear:

$$f_{dv}=1.0\times1.10\times60,000=66,000ps $$

Step 4. Calculate modulus of elasticity and modular ratio.

a.Concrete 

$$\begin{aligned}{E_{c}}&{{}=33w_{c}^{1.5}(f_{c}^{\prime})^{1/2}}\\ {}&{{}=33(150)^{1.5}(5000)^{1/2}}\\ {}&{{}=4.29\times10^{6}\mathrm{p s i}}\end{aligned}$$

b.Steel 

$$E_{s}=29.0\times10^{6}\mathrm{p s i}$$

$$n=\frac{E_s}{E_c}=\frac{29.0\times10^6}{4.29\times10^6}=6.76$$

NOTE: The flange is designed in accordance with the principles of Chapter 4. Considering the flange a one-way non-prestressed slab, the cantilever portion was found to be critical. In order to remain elastic the flange thickness must be increased to 3 inches. The reinforcement is two layers of welded wire fabric;$6\times6-\mathsf{W1.4}\times\mathsf{W2.0}$ in the top and $\mathtt{6}\times\mathtt{6}$ 二$\mathsf{W}1.4\times\mathsf{W}1.4$ in the bottom.



Calculate the section properties of the double tee with a 3 inch flange.

a.new $A=497in^2$ 

b.new.$y_{t}=6.43in$ 

<!-- batch 35 | page 30 -->

$$\begin{aligned}&new I_{g}=25180in^{4}\\&c.\quad&w=497×150pcf/12^{3}=43.1lb/in\\&d.\quad&d_{p}=7.85+14.15=22.0in\\&e.\quad&A_{ps}=4×0.153=0.612in^{2}\end{aligned}$$

f.Prestressed reinforcement ratio (Equation 6-17)

$$p_{p}=A_{ps}/bd_{p}=0.612/(96\times22.0)=0.000290$$

Step 6.

Determine the average stress in the prestressing tendon.

$$\begin{aligned}&a.\quad&f_{\rho y}/f_{\rho u}=0.85\quad so\quad\gamma_{\rho}=0.40\\&b.\quad&\beta_{1}=0.85-0.05(5950-4000)/1000=0.7525\\ \end{aligned}$$

C.Average stress (Equation 6-21)

$$\begin{aligned}\boldsymbol{f}_{ps}&=\boldsymbol{f}_{pu}\left[1-\frac{\gamma_{p}\rho_{p}\boldsymbol{f}_{pu}}{\beta_{1}\boldsymbol{f}_{dc}}\right]\\&=270,000\left[1-\frac{0.40\times0.000290\times270,000}{0.7525\times5950}\right]\\&=268,111\mathrm{ps}i\\ \end{aligned}$$

Step 7.Check maximum reinforcement ratio (Equation 6-24).

$$\begin{aligned}&\rho_{p}f_{ps}/f_{dc}^{\prime}\leq0.36\ \beta_{1}\\&\rho_{p}f_{ps}/f_{dc}^{\prime}=0.000290\times268,111/5950=0.0131\\&0.36\ \beta_{1}=0.36\times0.7525=0.2709>0.0131\quad O.K.\\ \end{aligned}$$

Step 8.Calculate moment capacity of beam.

From Equation 6-15

$$a=\frac{A_{ps}f_{ps}}{0.85f_{dc}^{'}b}=\frac{0.612\times268,111}{0.85\times5950\times96}=0.34in $$

$c=a/\beta_{1}=0.34/0.7525=0.45<3.0$ inch thick flange 

Hence the neutral axis is within the flange and the section can be analyzed as a rectangular section. If the neutral axis had extended into the web, a strain compatibility analysis would be required.

<!-- batch 35 | page 31 -->

From Equation 6-14

$$\begin{aligned}M_{u}&=A_{ps}f_{ps}(d_{p}-a/2)\\&=0.612\times268.111(22.0-0.34/2)\\M_{u}&=3582k-in\end{aligned}$$

Step 9.Find the resistance available to resist blast load.

a.Find the ultimate resistance (Table 3-1 (+))

$$\begin{aligned}{r_{u}}&{{}=8M_{u}/L^{2}}\\ {}&{{}=8\times3582/480^{2}=0.124\;\mathrm{k/i n}}\\ {}&{{}=124\;\mathrm{l b s/i n}}\end{aligned}$$

b.Resistance available for blast load 

$$\begin{aligned}{r_{a v a i l}}&{{}=r_{u}-D L-L L}\\ {}&{{}=124-43.1-(15\mathrm{p s f}\times8\mathrm{f t}/12)}\\ {}&{{}=124-43.1-10.0}\\ {}&{{}=70.9\mathrm{l b}/\mathrm{i n}}\end{aligned}$$

Step 10.Determine the average moment of inertia.

a.Moment of inertia of cracked section (Equation 6-27)

$$\begin{align*}I_{c}&=nA_{ps}d_{p}^{2}\left[1-(p)^{1/2}\right]\\&=6.76\times0.612(22.0)^{2}\left[1-(0.00029)^{1/2}\right]=1970in^{4}\end{align*}$$

b.Average moment of inertia (Equation 6-26)

$$\begin{aligned}&I_{a}=(I_{g}+I_{c})/2\\&\quad=(25180+1970)/2=13575in^{4}\\ \end{aligned}$$

Step 11.Using equations of Table 3-8 (+), calculate the elastic stifness.

$$K_{E}=\frac{384E_{c}I_{a}}{5L^{4}}=\frac{384\times4.29\times10^{6}\times13575}{5\times480^{4}}$$

<!-- batch 35 | page 32 -->

Step 12.Calculate the effective mass.

a.Load-mass factor (Table 3-12 (+))

In the elastic range 

$$K_{L M}=0.78$$

b.Unit mass 

$$\begin{aligned}m&=w/g=43.1/(32.2\times12)\\&=0.1116\mathrm{lb}-\mathrm{s}^2/\mathrm{in}^2\\&=11.16\times10^4\mathrm{lb}-\mathrm{ms}^2/\mathrm{in}^2\\ \end{aligned}$$

C.Effective mass 

$$\begin{aligned}{m_{e}}&{{}=K_{L M}m}\\ {}&{{}=0.78\times11.16\times10^{4}}\\ {}&{{}=8.70\times10^{4}\mathrm{{\sf{l b}}{-}m s^{2}/\mathrm{{i n^{2}}}}}\end{aligned}$$

Step 13.Calculate the natural period of vibration (Equation 3-54).

$$\begin{aligned}T_{N}&=2\pi\left(m_{e}/K_{E}\right)^{1/2}\\&=2\pi\left(8.70\times10^{4}/84.25\right)^{1/2}=201.9ms\end{aligned}$$

Step 14.Determine response of beam.

$$\begin{aligned}&T=duration of load=43.9ms(Step1a)\\&T_{N}=natural period=201.9ms(Step13)\\&T/T_{N}=43.9/201.9=0.217\\ \end{aligned}$$

From Figure 3-49 (+),$D L F=0.65$ 

Actual resistance obtained $r=D L F\times P\leq r_{a v a i l}$ 

$$P=\mathrm{peak\;d}\mathrm{y}\mathrm{n}\mathrm{a}\mathrm{m}\mathrm{i}\mathrm{c}\mathrm{l}\mathrm{a}\mathrm{d}$$

$$=1.1\;\mathrm{p s i}\;(\mathrm{S t e p}\;1\mathrm{a})$$

$$r=0.65\times(1.1\times96)$$

$$=68.4\ \mathrm{lb/in}<70.9\ \mathrm{lb/in}\ (r_{avall},\ \mathrm{Step}\ 9)\ \mathrm{O.K}.$$

<!-- batch 35 | page 33 -->

Step 15.Check rotation.

$$\begin{aligned}a.\quad&Total load on beam=(DLF\times p)+DL+LL\\&=68.4+43.1+10.0\\&=121.5lb/in\end{aligned}$$

b.Maximum deflection 

$$\begin{aligned}{X_{m}}&{{}=(121.5\mathrm{I b}/\mathrm{i n})/K_{E}}\\ {}&{{}=121.5/84.25}\\ {}&{{}=1.44\mathrm{i n}}\end{aligned}$$

$$\begin{aligned}&\mathsf{Support}\;\mathsf{rot}\;\mathsf{1}\;(\mathsf{Table}\;3-5\;(+))\\&\Theta=\tan^{-1}(2X_m/L)\\&\quad=\tan^{-1}(2\times1.44/480)\\&\quad=0.34^\circ<2^\circ\quad\mathsf{O}.\mathsf{K}.\\ \end{aligned}$$

Step 16.Calculate percent of rebound.

a.Calculate elastic deflection (Equation 3-30)

$$\begin{aligned}X_{E}&=r_{u}/K_{E}\\&=124/84.25\\&=1.47in\end{aligned}$$

b.Calculate ductility ratio 

$$\begin{aligned}{\mu}&{{}=X_{m}/X_{E}}\\ {}&{{}=1.44/1.47}\\ {}&{{}=0.98}\end{aligned}$$

C.Find percent of rebound from Figure 3-268 (+)

$$\begin{aligned}&X_{m}/X_{E}=0.98\ and\ T/T_{N}=0.216\\ &r^{-}/r=1.0\\ \end{aligned}$$

so, 100 percent rebound 

<!-- batch 35 | page 34 -->

Step 17.Determine required rebound moment capacity.

a.Required rebound resistance 

$$r_{req}^{-}=r^{-}-DL>r_{avail}/2$$

Use 35.4 Ib/in or considering a single tee 

$$r_{\mathrm{r e g}}^{-}=17.7\mathrm{I b/i n}$$

b.Required moment capacity (Table 3-1 (+))

$$\begin{aligned}{M_{u}^{-}}&{{}=r_{r e q}^{-}L^{2}/8}\\ {}&{{}=17.7\times480^{2}/8}\\ {M_{u}^{-}}&{{}=509,760\mathrm{i n-l b/s t e m}}\end{aligned}$$

Step 18.Determine rebound reinforcement.

a.Approximate value of.$d^{-}$ 

$$\begin{aligned}d^{-}&=h-c o v e r-\phi_{w i r e}-\phi_{t i e}-(\phi_{b a r}/2)\\&=25-0.625-0.135-0.375-0.5/2\\&=23.62\ln\\ \end{aligned}$$

b.Rebound concrete strength 

$$f=0.47f_{dc}=0.47\times5950=2796.5\mathrm{psi}$$

C.Required rebound reinforcement 

Assume $a=2.0$ in 

$$\begin{aligned}{A_{s}^{-}}&{{}=M_{u}^{-}/[f_{d y}(d^{-}-a/2)]}&{(\mathrm{E q u a t i o n~6-28})}\\ {}&{{}=509,760/[77,220(23.62-2.0/2)]}&{=0.29\;\mathrm{i n}^{2}}\\ \end{aligned}$$

<!-- batch 35 | page 35 -->

$$\bar{a}=\frac{A_{s}^{-1}f_{dy}}{0.47f_{dc}^{'}b}=\frac{0.29\times77,200}{2796.5\times3.75}=2.1in\approx2.0in O.K.$$

Use 2 No. 4 bars in each stm 

$$A_{s}^{-}=0.40\ in^{2}$$

d.Check maximum reinforcement (Equation 6-30)

$$\begin{aligned}A_{s}&\leq\frac{0.47f_{dc}^{\prime}\beta_{1}}{f_{d_{y}}}\left[\frac{87,000-0.378nf_{dc}^{\prime}}{87,000-0.378nf_{dc}^{\prime}+f_{d_{y}}}\right]bd^{-}\\&=\frac{2796.5\times0.7525}{77,220}\left[\frac{87,000-0.378\times6.76\times5950}{87,000-0.378\times6.76\times5950+77,220}\right]\\&\quad\times3.75\times23.62\\&=1.16\ln^{2}>0.40\ln^{2}\quad\text{O.K.}\end{aligned}$$

Step 19.Design the shear reinforcement.

$$\begin{aligned}&a.\quad&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&v}}}\left(L/2\right.\right.\end{aligned}\quad&\begin{aligned}&\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\right.\left.\right.\left.\left.\left.\right.\right.\left.\left.\left.\left.\right.\right.\left.\right.\left.\right.\left.\left.\left.\right.\right.\right.\right.\left.\left.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\right.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.$$

b.Maximum allowable shear stress 

$$\begin{aligned}10\left(\bar{r}_{c}\right)^{1/2}&=10\times\left(5000\right)^{1/2}\\&=707\mathrm{ps}i>127\mathrm{ps}i\quad\mathrm{O.K.}\end{aligned}$$

C.Allowable shear stress on unreinforced web 

$$\begin{aligned}&v_{c}=1.9(f_{c})^{1/2}+2500p_{p}\leq2.28(f_{c})^{1/2}\\ &=1.9\times5000^{1/2}+2500\frac{0.612}{2\times4.75\times22}=142\mathrm{ps}i\\ \end{aligned}$$

$$\begin{aligned}&2.28(f_{c}^{\prime})^{1/2}=2.28(5000)^{1/2}\\ &=161\mathrm{ps}>142\mathrm{ps}\mathrm{i}\quad\mathrm{O.K.}\\ \end{aligned}$$

<!-- batch 35 | page 36 -->

d.Excess shear 

$$\begin{aligned}&v_{u}-v_{c}\leq v_{c}\\&v_{u}-v_{c}=127-142=-15\mathrm{psi}\\ \end{aligned}$$

so, use Vc 

e.Shear reinforcement 

Assume #3 closed ties 

$$\begin{aligned}A_{v}&=2\times0.11=0.22\ln^{2}\\s_{s}&=\frac{A_{v}\Phi f_{y}}{v_{c}b}=\frac{0.22\times0.85\times66,000}{142\times4.75}\\&=18.3\ln\end{aligned}$$

$$\begin{aligned}&if.\quad&&\textsf{Check maximum spacing and minimum required reinforcement}\\&&&s\;\leq\;d_p/2=22.0/2=11.0\;in\\&&&\textsf{A}_v\leq\;0.0015bs_s\\&&&\quad=0.0015\times4.75\times11.0\quad=0.08\;in^2\;>0.22\;in^2\end{aligned}$$

Shear reinforcement is thus #3 ties at 11 inches in both stems.

Step 20.Check direct shear.

a.Calculate shear at the support (Table 3-9 (+))

$$\begin{aligned}\dot{V}_{d}&=rL/2\\&=121.5\times480/2\\&=29.160lbs\\ \end{aligned}$$

b.Calculate allowable direct shear 

$$\begin{aligned}V_{d}&\leq0.18\ f_{c}^{\prime}\ bd\\ &=0.18\times5,500\times(2\times4.75)\times22.0\\ &=206,910\ lbs>29,160\ lbs\quad O.K.\end{aligned}$$

Step 21.Check section for conventional loads.

This section as designed for blast loads is shown in Figure $6A-3(+)$ .Using the PCI Design Handbook and the latest ACl code, the section must be checked to make sure it is adequate for service loads.

<!-- batch 35 | page 37 -->

<div style="text-align: center;">Figure 6A-3</div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_image_box_318_303_855_855.jpg" alt="Image" width="45%" /></div>


<!-- batch 35 | page 38 -->

## PROBLEM 6A-3DESIGNOFWINDOWS 

## Problem:Determine the minimum thickness of glazing to resist a given blast load, and the design loads for the framing

## Procedure:

Step 1.Establish design parameters.

a.Pressure-time loading 

b.Dimensions of pane(s)

C.Type of glazing 

Step 2.Calculate aspect ratio of pane.

Step 3.With the parameters of Steps 1 and 2, enter Figures 6-28 (+/+) to 6-42(+/+) to determine which one applies. Using the peak pressure of the dynamic load, its duration and the dimensions of the pane, determine the minimum required glazing thickness.



NOTE: If given window geometry differs from chart parameters,interpolation as outlined in Section 6-28.4 may be required.

Step 4.Find the static ultimate resistance $r_{u}$ of the glazing from Table 6-7(+/+/+/+/+/+/+) for the given aspect ratio, the short dimension and the thickness of the glazing (interpolate if required).

Step 5.From Table 6-10 (+) and the aspect ratio determine the design coefficients $C_{R}$ $C_{X}$ and $C_{Y}$ for the window frame loading. With these coefficients, th dimensions of the pane from Step 1b, the static ultimate resistance of Step 4 and Equation 6-49, calculate the uplift force in each corner. Then using Equations 6-47 and 6-48 calculate the design loads along the long and short spans of the pane. Finally from Table 6-12 (+/+/+/+/+/+/+),determine the fundamental period,$T_{N},$ and check for rebound requirements in accordance with Section 6-30.4

<!-- batch 35 | page 39 -->

## EXAMPLE 6A-3DESIGN OF WINDOWS 

Required:Find the minimum glazing thickness and the design loads on the frame of a non-openable window consisting of four equal size panes of glass.



## Solution:

Step 1.Given:

a.Pressure-time loading (Figure 6A-4 (+)

b.Each pane is 37.5 inches long by 30 inches high 

C.The glazing is heat-treated tempered glass meeting Federal Specification DO-G-1403B and ANSI Z97.1-1984

<div style="text-align: center;">Figure 6A-4</div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_chart_box_485_720_771_974.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">TIME $(m\leq)$ </div>


Step 2.Calculate aspect ratio.

$$a/b=37.5/30=1.25$$

Step 3.Determine minimum glazing thickness.

a.For $a/b=1.25$ and tempered glass use Figure 6-36$(\pm/\underline{{\pm}})$ 

b.From Figure $6-36$ $t=3/4$ ·inch 

Step 4.Find static ultimate resistance $r_{u}$ (Table 6-7 (+/+/+/+/+/+/+).

$$r_{u}=24.6\mathrm{p s i}$$

The window frame must be designed to safely support, without undue deflections, a static uniform load of 24.6 psi applied normal to both the glazing and the exposed frame members.



<!-- batch 35 | page 40 -->

Step 5.Compute design loads on the window frame.

Note: The exposed surface width of the frame is 2 inches.

a.Determine design coefficients from Table 6-10 (+), interpolating for 

$a/b=1.25$ 



$$\begin{aligned}&C_{R}=0.077\\&C_{x}=0.545\\&C_{y}=0.543\\ \end{aligned}$$

b.Calculate the unit shear along the long span of the frame (Equation 6-47)



$$\begin{aligned}V_{x}&=C_{x}r_{u}b\sin(\pi x/a)+r_{u}w\\&=0.545\times24.6\times30\sin(\pi x/37.5)+24.6\times24\\&=402\sin(\pi x/372.5)+49.2\ lb/in\\ \end{aligned}$$

C.Calculate the unit shear along the short span of the frame (Equation 6-48)



$$\begin{aligned}V_{y}&=C_{y}r_{u}b\sin(\pi y/b)+r_{u}w\\&=0.543\times24.6\times30\sin(\pi y/30)+24.6\times20\\&=400\sin(\pi y/18)+49.2\ lb/in\\ \end{aligned}$$

d.Calculate the uplift force at the corners of the panes (Equation 649)



$$\begin{aligned}&R=-C_{R}r_{u}b^{2}\\&\quad=-0.077\times24.6\times30^{2}\\&\quad=-1705\text{lbs}\\ \end{aligned}$$

Distribution of the design load of the pane on the frame is shown in Figure 6-55 (+).



e.From Table 6-12$(\underline{{+}}/\underline{{+}}/\underline{{+}}/\underline{{+}}/\underline{{+}}/\underline{{+}})$ $T_{N}=8.74$ msec,$T/T_{N}=500/8.74=$ 57.2



Since $T/T_{\mathrm{N}}=57.2>10$ , design for rebound is not necessary.

<!-- batch 35 | page 41 -->

## PROBLEM 6A-4DESIGNOF SHOCK ISOLATIONSYSTEM 

### Problem:Design an overhead pendulum shock isolation system using a platform for a given loading. 

Step 1.Establish design parameters.

a.Structural configuration 

b.Magnitude and location of loads on platform 

C.Shock spectra for horizontal and vertical motion 

d.Maximum allowable motion 

Step 2.Compute member sizes of platform.

Step 3.Compute center of gravity of the loads (live and dead) on platform.

Step 4.Compute the elastic center of the spring supporting system.

Step 5.Determine the required weight and location of ballast to balance the system (i.e. to move the center of gravity of loads to coincide with the elastic center of the spring supporting system).

Step 6.Compute the total weight of the isolation system. Additional ballast equal to 25% of the weight of the equipment and ballast from Step 5 is added to provide for future changes in equipment. Also determine the equivalent uniform load equal to the total load divided by the area of the platform.

Step 7.Determine the natural frequency of the individual members of the platform (using the equivalent uniform load computed in Step 6). The natural frequency is 



$$f=\frac{9.87}{2\pi}=\frac{EI_{g}}{wL^{4}}$$

for a simply supported beam with a uniform load.

Step 8.Using the shock spectrum for vertical motion, determine the required frequency of the system that will reduce the input accelerations to the maximum allowable. In addition, determine the displacement at this frequency.



Step 9.Verify rigid body motion of the platform.

The natural frequency of the individual members of the platform should be at least 5 times greater than the natural frequency of the system for rigid body motion of the platform to occur.



<!-- batch 35 | page 42 -->

To increase the frequency of the individual members, increase member sizes, and repeat Steps 3 through 7.



Step 10.Determine the natural frequency for horizontal motion (pendulum action)of the platform where 



$$f_{h o r i z o n t a l m o t i o n}=1/2\pi(386.4/L)^{1/2}$$

where L is the suspended length.

Step 11.Verify that dynamic coupling will not occur between vertical and horizontal motions. According to Section 6-47.3.2 dynamic coupling will not occur if 

$$f_{h o r i z o n t a l m o t i o n}<1/2f_{v e r t i c a l m o t i o n}$$

Step 12.From the shock spectra for horizontal motion, determine the maximum dynamic displacement, velocity and acceleration using the frequency computed in Step 10.



Verify that the maximum acceleration is less than the allowable.

Step 13.Compute the load in each spring.

$$\mathrm{Load}\;\mathrm{ineach}\;\mathrm{spring}=\frac{\mathrm{TotalLoad}}{\mathrm{Number of}\;\mathrm{Springs}}$$

Step 14.Determine stiffness of springs to produce the required frequency of the system. Compute the static and maximum displacement. Using the static displacement and the load in each spring from Step 13, calculate the required spring stiffness K from,

$$K=\frac{\bmod{\min}\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad $$

Or using the vertical frequency from Step 8, and the mass on each spring the stiffness can be calculated from 



$$K=[2\pi f_{v e r t}]m^{2}$$

In addition, compute the travel of the spring according to Section 6-48.2,i.e.



$$\mathrm{travel}=\frac{\mathrm{Maximum displacement}}{0.85}$$

<!-- batch 35 | page 43 -->

## EXAMPLE 6A-4DESIGN SHOCK ISOLATION SYSTEM 

Required:Design an overhead pendulum shock isolation system using a platform for a given loading.



### Step 1.Given:

a.Structural configuration shown in Figure 6A-5 (+)

<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_image_box_311_482_880_743.jpg" alt="Image" width="47%" /></div>


<div style="text-align: center;">（a)ELEVATION </div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_image_box_312_806_940_1047.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">(b)PLATFORM(PLAN)</div>


b.Magnitude and location of loads on platform (Figure 6A-6 (+))

$$\begin{aligned}&E_{1}=4960\mathrm{Ibs}\\&E_{2}=4960\mathrm{Ibs}\\&E_{3}=4960\mathrm{Ibs}\\ \end{aligned}$$

Floor panel = 5.5 psf (covers the whole area of platform)

Grating = 7.2 psf 

Live load = 150 psf 

<!-- batch 35 | page 44 -->

<div style="text-align: center;">Figure 6A-6</div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_image_box_227_321_953_614.jpg" alt="Image" width="60%" /></div>


<div style="text-align: center;">PLATFORM(PLAN)</div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_image_box_323_727_743_890.jpg" alt="Image" width="35%" /></div>


C.Shock spectra for horizontal and vertical motions are given in Figure 6A-7 (+)



d.Maximum allowable acceleration 

Vertical $\mathrm{Motion}=0.50\mathrm{g}$ c 

Horizontal $\mathrm{Motion}=0.75\mathrm{g}$ 」

<!-- batch 35 | page 45 -->

<div style="text-align: center;">Figure 6A-7</div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_chart_box_209_316_1011_802.jpg" alt="Image" width="67%" /></div>


### Step 2.Member sizes 

Design Loads:

$$\begin{aligned}&\mathsf{D e a d\;l o a d=20\;p s f\;(a s s u m e)}\\&\mathsf{L i v e\;L o a d=150\;p s f}\\ \end{aligned}$$

Primary Member (a): See Figure 6A-5a (+).

$$w=170\times(7.05+8.05)=2567\mathrm{~lb}\mathrm{~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\mid\$$

$$\begin{aligned}&\mathsf{Maximum}\;\mathsf{Bending}\;\mathsf{moment}=(wL^2)/8\;\;(\mathsf{at}\;\mathsf{center})\\ &\;\;=\;(2567\times10.8^2)\;/\;8\\ &\;\;=\;37427\;\mathsf{lb}\;\mathsf{-ft}\\ \end{aligned}$$

Using allowable stress design,

Allowable bending stress $s=0.66\times F_v$ (for compact shapes AlSC).

<!-- batch 35 | page 46 -->

$$\begin{aligned}so,Required S_{x}=&\frac{MaximumBending Moment}{Allowable Bending Sress}\\=&\left(37427\times12\right)/\left(0.66\times36,000\right)\\=18.9in^3\end{aligned}$$

Try section W10x21,

$$S_{x}=21.5\ in^{3}>18.9\ in^{3}\quad O.K.$$

Check deflection:

$$ Maximum allowable deflection=\frac{L}{360}=\frac{10.8\times12}{360}=0.36in $$

Maximum deflectior $h=(5w L^{4})/384E I$ (at center)

For $\mathsf{W10}\times\mathsf{21}$ 

$$I=107\mathrm{i n}^{4}$$

$$\begin{aligned}&Maximum deflection=\frac{5\times(2567/12)\times(10.8\times12)^4}{384\times29,000\times10^3\times107}\\ &\quad=0.25in<0.36in\quad O.K.\\ \end{aligned}$$

So,use $\mathsf{W10\times21}$ for all primary members.

Secondary Member (b): See Figure 6A-5a (+)

$$w=170(1.0+1.2)=374\mathrm{lb/ft}$$

$$\begin{aligned}Maximum Bending moment&=(wL^{2})/8\quad(at center)\\&=(374\times16.1^{2})/8=12.118lb-ft\end{aligned}$$

Using allowable stress design,

Allowable bending stres:$s=0.66~F_{V}$ (for compact shapes, AlSC).

so, Required $S_{x}=\frac{12118\times12}{0.66\times36.000}=6.12\mathrm{~in}^{3}$ 

Try section $\mathsf{W8\times13}$ 

$$S_{x}=9.90\ in^{3}>6.12\ in^{3}\quad O.K.$$

<!-- batch 35 | page 47 -->

Check deflection:

$$\begin{aligned}Maximum allowable deflecion&=\frac{L}{360}\\&=\frac{16.1\times12}{360}\\&=0.54in\end{aligned}$$

For $W8\times13,\ I=39.6in^4$ 

$$\begin{aligned}Maximumdeflection&=\frac{5\pi L^{4}}{384EI}\\&=\frac{5\times(374/12)\times(16.1\times12)^{4}}{384\times29.000\times10^{3}\times39.6}\\&=0.49<0.54\quad O.K.\end{aligned}$$

So,use $\mathsf{W8\times13}$ for all secondary members.

NOTE: Members should be checked for concentrated equipment loads.

Step 3.

Find center of gravity of the loads on the platform (see Figure 6A-8 (+)).

Center of gravity of loads $(\mathrm{d e a d}+\mathrm{I i v e})=\{\overline{{X}}_{1},\overline{{Y}}_{1}\}$ 

$$\begin{aligned}Then,\overline{X}_{1}=&\frac{\Sigma W_{1}\overline{X}}{\Sigma W_{1}}\\=&\frac{484,&540}{23751.4}\\=&20.4ft\\\overline{Y}_{1}=&\frac{\Sigma W_{1}Y}{\Sigma W_{1}}\\=&\frac{62,&786.7}{23,&751.4}\\=&2.64ft\end{aligned}$$

<!-- batch 35 | page 48 -->

<div style="text-align: center;">Figure 6A-8</div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_image_box_205_318_972_568.jpg" alt="Image" width="64%" /></div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>ltem</td><td>, 21.65 1.2</td><td>X (ft)</td><td>Y (ft)</td><td>W₁X (Ib-ft)</td><td>W_{₁Y (Ib-ft)</td></tr><tr><td>$\mathsf{A_{1}A_{2}...A_{6}}$</td><td>226.8</td><td>0.0</td><td>5.4</td><td>0.0</td><td>1224.7</td></tr><tr><td>B_{B{2} B6$</td><td>226.8</td><td>13.1</td><td>5.4</td><td>2971.1</td><td>1224.7</td></tr><tr><td>$\mathsf{C_{1}C_{2}...C_{6}}$</td><td>226.8</td><td>27.2</td><td>5.4</td><td>6169.0</td><td>1224.7</td></tr><tr><td>D_{₁D_2..D6$</td><td>226.8</td><td>43.3</td><td>5.4</td><td>9820.4</td><td>1224.7</td></tr><tr><td>$\mathsf{A}_{1}\mathsf{B}_{1}\mathsf{C}_{1}\mathsf{D}_{1}$</td><td>562.9</td><td>21.65</td><td>10.8</td><td>12187.0</td><td>6079.3</td></tr><tr><td>$\mathsf{A_{2}B_{2}C_{2}D_{2}}$</td><td>562.9</td><td>21.65</td><td>8.4</td><td>12187.0</td><td>4728.4</td></tr><tr><td>$\mathsf{A_{3}B_{3}C_{3}D_{3}}$</td><td>562.9</td><td>21.65</td><td>6.4</td><td>12187.0</td><td>3602.6</td></tr><tr><td>$\mathsf{A}_{4}\mathsf{B}_{4}\mathsf{C}_{4}\mathsf{D}_{4}$</td><td>562.9</td><td>21.65</td><td>4.4</td><td>12187.0</td><td>2476.8</td></tr><tr><td>$\mathsf{A}_{5}\mathsf{B}_{5}\mathsf{C}_{5}\mathsf{D}_{5}$</td><td>562.9</td><td>21.65</td><td>2.4</td><td>12187.0</td><td>1351.0</td></tr><tr><td>$\mathsf{A_{6}B_{6}C_{6}D_{6}}$</td><td>562.9</td><td>21.65</td><td>0.0</td><td>12187.0</td><td>0.0</td></tr><tr><td>$E1</td><td>4960.0</td><td>5.9</td><td>1.0</td><td>29264.0</td><td>4960.0</td></tr><tr><td>$E2$</td><td>4960.0</td><td>20.3</td><td>1.0</td><td>100688.0</td><td>4960.0</td></tr><tr><td>$E3$</td><td>4960.0</td><td>34.8</td><td>1.0</td><td>172608.0</td><td>4960.0</td></tr><tr><td>$\mathsf{A}_{1}\mathsf{D}_{1}\mathsf{D}_{2}\mathsf{A}_{2}$</td><td>748.2</td><td>21.65</td><td>9.6</td><td>16199.0</td><td>7183.0</td></tr><tr><td>$\mathsf{A}_{5}\mathsf{D}_{5}\mathsf{D}_{6}\mathsf{A}_{6}$</td><td>748.2</td><td>21.65</td><td>1.2</td><td>16199.0</td><td>897.8</td></tr><tr><td>$\mathsf{A}_{2}\mathsf{G}_{11}\mathsf{G}_{12}\mathsf{A}_{5}$</td><td>259.2</td><td>3.0</td><td>5.4</td><td>777.6</td><td>1400.0</td></tr><tr><td>$\mathsf{D_{2}}\mathsf{D_{5}}\mathsf{G_{14}}\mathsf{G_{15}}$</td><td>259.2</td><td>4.0</td><td>5.4</td><td>1036.8</td><td>1400.0</td></tr><tr><td>Floor Panel</td><td>2572.0</td><td>21.65</td><td>5.4</td><td>55684.0</td><td>13889.0</td></tr><tr><td>∑</td><td>23751.4</td><td></td><td>∑</td><td>484540</td><td>62786.7</td></tr></tbody></table></body></html></div>


<!-- batch 35 | page 49 -->

Step 4.Elastic center of the spring support system.

Elastic center of spring support system $=\{\overline{{X}}_{s},\overline{{Y}}_{s}\}$ 

$$\begin{aligned}\overline{X}_{s}=&\frac{\Sigma W X}{\Sigma W}\\=&\frac{167.2P}{8P}=20.9ft\\\overline{Y}_{s}=&\frac{\Sigma W Y}{\Sigma W}\\=&\frac{43.2P}{8P}=5.4ft\end{aligned}$$

<div style="text-align: center;">Figure 6A-9</div>


<div style="text-align: center;"><img src="../pages/batch 35/imgs/img_in_chart_box_339_709_859_871.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">NOTE: All springs have the same stiffness </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Spring No.</td><td>Force (W)</td><td>X (ft)</td><td>Y (ft)</td><td>WX</td><td>WY</td></tr><tr><td>$\mathsf{S}_{1}$</td><td>P</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>$\mathsf{S_{2}}$</td><td>P</td><td>0</td><td>10.8</td><td>0</td><td>10.8P</td></tr><tr><td>$\mathsf{S}_{3}$</td><td>P</td><td>13.1</td><td>0</td><td>13.1P</td><td>0</td></tr><tr><td>$\mathsf{S}_{4}$</td><td>P</td><td>13.1</td><td>10.8</td><td>13.1P</td><td>10.8P</td></tr><tr><td>$\mathsf{S}_{5}$</td><td>P</td><td>27.2</td><td>0</td><td>27.2P</td><td>0</td></tr><tr><td>$\mathsf{S_{6}}$</td><td>P</td><td>27.2</td><td>10.8</td><td>27.2P</td><td>10.8P</td></tr><tr><td>$\mathsf{S}_{7}$</td><td>P</td><td>43.3</td><td>0</td><td>43.3P</td><td>0</td></tr><tr><td>$\mathsf{S}_{8}$</td><td>P</td><td>43.3</td><td>10.8</td><td>43.3P</td><td>10.8P</td></tr><tr><td>$\Sigma$</td><td>8P</td><td></td><td>∑</td><td>167.2P</td><td>43.2P</td></tr></tbody></table></body></html></div>


<!-- batch 35 | page 50 -->

Find the weight and location of ballast to balance the system (relocate the c.g. of the platform to coincide with the elastic center of the isolation system).



a.For the x direction, try placing ballast at $x=30.3\ ft$ ,i.e.4 feet from the right edge of the platform. The ballast is placed symmetrically about the x axis of the elastic center so as not to affect the location of the center of gravity in the y direction.



Weight of ballast = WBX 

$$\begin{aligned}&\Sigma W_{1}X+39.3W_{BX}=\overline{X}_{s}\left[\Sigma W_{1}+W_{BX}\right]\\&484.540+39.3W_{BX}=20.9\left(23.751.4+W_{BX}\right)\\&W_{BX}=11.864/18.4=644.8Ibs\\ \end{aligned}$$

b.For the y direction, try placing ballast at $y=9.6$ feet, i.e.1.2 feet from the top of the platform. The ballast is placed symmetrically about the y axis of the elastic center so as not to affect the location of the center of gravity in the x direction.



Weight of ballast = WBY 

$$\begin{aligned}\Sigma W_{1}Y+9.6W_{BY}&=\overline{Y}_{s}[\Sigma W_{1}+W_{BY}]\\62,786.7+9.6W_{BY}&=5.4(23,571.4+W_{BY})\\W_{BY}&=65,470.9/4.2=15,588.3Ibs\end{aligned}$$

C.Total ballast 

$$W_{B}=W_{BX}+W_{BY}=644.8+15588.3=16233\ lb $$

Total load on the platform and equivalent uniform load.

a.Total load.

Dead Load:

$${\begin{array}{l l}{{\mathsf{F l o o r p a n e l}}}&{=2572{\mathsf{I b s}}}\\ {{\mathsf{M e m b e r s}}}&{=4284.6}\\ {{\mathsf{G r a t i n g}}}&{={\underline{{2014.8}}}}\\ {{\underline{{\Sigma}}}}&{=8871.4{\mathsf{I b s}}}\end{array}}$$

Live Load:

Equipment 

Ballast 

$$\begin{aligned}&=14880\;lbs\\ &=16233\\ \end{aligned}$$

<!-- batch 35 | page 51 -->

$${\begin{array}{r l}{{\mathsf{A d d i t i o n a l~B a l l a s t}}=0.25(30606)\quad=\quad7651.6}\\ {{\mathsf{P e r s o n n e l~(5~@~150~l b)}}\quad=\quad{\underline{{750}}}}\\ {\Sigma\quad=\quad39514.6~{\mathsf{l b s}}}\\ {{\mathsf{T o t a l}}\quad=\quad8871.4+39514.6}\\ {=\quad48386~{\mathsf{l b s}}}\end{array}}$$

b.Equivalent uniform load 

$$W=\frac{48386}{10.8\times43.3}\quad(\mathrm{H})=103.5\mathrm{~ps}f\leq170\mathrm{~ps}f\quad\mathrm{O}.\mathrm{K}.$$

Preliminary design of platform members is O.K. However, members supporting ballast must be checked as their actual load may be higher than the equivalent uniform load.



Step 7.Natural frequency of the individual members of the platform.

For a simply supported member with a uniform load,

$$\mathrm{Natural\ frequency}f_{n}=\frac{9.87}{2\pi}\frac{\mathrm{E}\mathrm{I}g}{\mathrm{W}L^{4}}$$

Primary Members (a): A portion of the adjacent slab acts with the beam. Add 20% of the mass of the slab on each side of the beam to the actual mass of the beam.



$$\begin{aligned}&J=107in^4\\&L=10.8\times12\\&\quad=129.6inches\\&b=0.40(7.05+8.05)\\&\quad=6.04leet\\&g=386.4in/sec^2\\&E=29000\times10^3psi.\\ \end{aligned}$$

<!-- batch 35 | page 52 -->

w: (Use equivalent uniform load)

$$\begin{aligned}\overline{w}&=102.4\times6.04\\&=618.5\mathrm{lb/rt}\\&=51.54\mathrm{lb/ln}\\f_{n}&=\frac{9.87}{2\pi}\left[\frac{29000\times10^3\times107\times386.4}{51.54\times29.6^4}\right]^{1/2}\\&=14.3\mathrm{cps}\end{aligned}$$

Secondary Members (b): Since the spacing of the secondary beams is less than 1/4 of the length of the beams the total mass of the slab acts with the beam.



$$\begin{aligned}W8×13\\I&=39.6in^4\\L&=16.1×12\\&=193.2in\\b&=2.2 早 \\w&=102.4×2.2\\&=225.3lb/f t\\&=18.78lb/in\\E&=29000×10^3psi\\g&=386.4in/sec^2\\f_n&=\frac{9.87}{2\pi}\left[\frac{29,000×10^3×39.6×386.4}{18.78×193.2^4}\right]^{1/2}\\&=6.5psi\end{aligned}$$

Step 8.Required frequency of system to limit motions.

To limit the maximum acceleration of the system to 0.5g or less, choose the frequency of the system from Figure 6A-7 (+) as 

$$f=1~\mathrm{c p s}$$

which produces a maximum acceleration of 0.4g and a maximum dynamic displacement of 4.7 inches.



<!-- batch 35 | page 53 -->

Step 9.Verification of rigid body motion of platform.

findividual member >5× fsystem 

From Step 8,

$$f_{s y s t e m}=1\mathrm{c p s}$$

From Step 7,

fprimary member = 14.2 cps > 5 cps O.K.

fsecondary member = 6.5 cps > 5 cpsO.K.

Therefore, platform is in rigid body motion.

Step 10.Natural frequency of platform for horizontal motion (i.e. pendulum type action).



Assume the center of gravity of supported mass is located at the top of the platform so that the length of the pendulum arm is 17.4 feet.

Frequency of platform for horizontal motion 

$$f=1/(2\pi)(386.4/L)^{1/2}$$

= 0.22 cps 

Step 11.Check for dynamic coupling of vertical and horizontal motion.

From Step 8,

fvertical motion =1 cps 

From Step 10,

$$f_{h o r i z o n t a l,m o t i o n}=0.22\;\mathrm{c p s}<1/2\;f_{v e r t i c a l,m o t i o n}=0.5\;\mathrm{c p s}$$

Dynamic coupling will not occur.

Step 12.Maximum dynamic displacement, velocity and acceleration for horizontal motion.



From shock spectra for horizontal motion, (Figure 6A-7 (+)) for $f=0.22$ cps,

Maximum acceleration = 0.007g<0.75g O.K.

Maximum velocity = 0.9 in/sec 

Maximum dynamic displacement = 1.3 in 

The maximum dynamic displacement is the required "rattle space" or the 

<!-- batch 35 | page 54 -->

minimum horizontal clearance between the platform and the structure or anything attached to the structure.



Step 13.Load in each spring.

$$\begin{aligned}Load in each spring&=\frac{Total Load}{Number of Springs}\\&=\frac{47.878.9}{8}\\&=5985lb\end{aligned}$$

Step 14.Design the springs.

a.Static displacement 

From Step 8,

For a maximum acceleration of 0.48g the maximum dynamic dis,${\tt s p l a c e m e n t}=4.7$ in 



So, static displacement = 4.7/0.48

b.Stiffness of spring = 4.7/0.48 = 9.79

$$\begin{aligned}K=&\frac{Loadin each spring}{Static displacement}\\ =&\frac{5985}{9.79}=611.2lb/in\end{aligned}$$

or 

$$\begin{aligned}{K}&{{}=(2\pi f_{v e r t})^{2}m}\\ {}&{{}=(2\pi\times1\;\mathrm{c p s})^{2}(5985/386.4)}\end{aligned}$$

$$K=611.5\mathrm{~lb}/\mathrm{in}$$

C.Maximum travel of spring 

Maximum displacement = (static + dynamic) displacement 

<!-- batch 35 | page 55 -->

From Section 6-48.2

$$\begin{aligned}Travel of spring=&\frac{maximum displacement}{0.85}\\ =&\frac{14.49}{0.85}\\ =&17.0in\end{aligned}$$

Thus the vertical rattle space (clearance) is 17.0 inches.

<!-- batch 35 | page 56 -->

## APPENDIX 6B LIST OF SYMBOLS 


<div style="text-align: center;"><html><body><table border="1"><tr><td>a (1)</td><td>acceleration (in/ms2)</td></tr><tr><td></td><td>(2) depth of equivalent rectangular stress block (in)</td></tr><tr><td>(3)</td><td>long span of a panel (in)</td></tr><tr><td>A</td><td>area $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{a}$</td><td>area of diagonal bars at the support within a width b $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{d}$</td><td>door area $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{g}$</td><td>area of gross section $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{f s}$</td><td>solid area ratio of masonry cross sectional area</td></tr><tr><td>$A_{n}$</td><td>net area of section $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{n o}$</td><td>net cross section for out-of-plane shear 1 $(\mathsf{i n}^{2}/\mathsf{i n})$</td></tr><tr><td>$A_{o}$</td><td>area of openings $(\mathsf{f t}^{2})$</td></tr><tr><td>$A_{p s}$</td><td>area of prestressed reinforcement $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{s}$</td><td>area of tension reinforcement within a width b (in2)</td></tr><tr><td>$A_{s}^{\prime}$</td><td>area of compression reinforcement within a width b (in2)</td></tr><tr><td>$A_{s}$</td><td>area of rebound reinforcement (in2)</td></tr><tr><td>$A_{s H}$</td><td>area of flexural reinforcement within a width b in the horizontal direction on each face ${(\mathsf{i n}^{2})}^{\star}$</td></tr><tr><td>$A_{s V}$</td><td>area of flexural reinforcement within a width b in the vertical direction on each face $(\mathsf{i n^{2}})^{\star}$</td></tr><tr><td>$A_{v}$</td><td>total area of stirrups or lacing reinforcement in tension within a distance, $\mathcal{S}_{V}$</td></tr><tr><td>$A_{v d}$</td><td>unit area of reinforcing steel for direct shear plane along suport 1 $(\mathsf{i n}^{2}/\mathsf{i n})$ $({\mathsf{i n^{2}}})$</td></tr><tr><td>$A_{I},A_{I I}$</td><td>area of sector I and Il, respectively $({\mathsf{i n}}^{2})$</td></tr><tr><td>(1) $b$</td><td>width of compression face of flexural member (in)</td></tr><tr><td>(2)</td><td>width of concrete strip in which the direct shear stresses at the</td></tr><tr><td></td><td>supports are resisted by diagonal bars (in)</td></tr><tr><td></td><td></td></tr><tr><td>(3)</td><td>short span of a panel (in)</td></tr></table></body></html></div>


<!-- batch 35 | page 57 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>by stirrups of area $b_{s}$ $b_{1}$</td><td>width of concrete strip in which the diagonal tension stresses are resisted $A_{v}\left(\mathsf{i n}\right)$</td></tr><tr><td></td><td>width of concrete strip in which the diagonal tension stresses are resisted by lacing of area (in) $A_{v}$</td></tr><tr><td>B</td><td>peak blast overpressure capacity</td></tr><tr><td>C</td><td>shear coefficient</td></tr><tr><td>C</td><td>(1) distance from the resultant applied load to the axis of rotation (in)</td></tr><tr><td></td><td>(2) damping coefficient</td></tr><tr><td>$c_{I I}$ $c_{I}$</td><td>(3) distance from extreme compression fiber to neutral axis (in) distance from the resultant applied load to the axis of rotation for sectors I</td></tr><tr><td></td><td>and Il, respectively (in)</td></tr><tr><td>$C_{c r}$ $C_{d}$</td><td>critical damping</td></tr><tr><td>$C_{D}$</td><td>shear coefficient for ultimate shear stress of one-way elements</td></tr><tr><td></td><td>(1) drag coefficient</td></tr><tr><td>$C_{D}q$</td><td>(2) coefficient for center deflection of glass</td></tr><tr><td>$C_{D}q_{o}$</td><td>drag pressure (psi)</td></tr><tr><td></td><td>peak drag pressure (psi)</td></tr><tr><td>$C_{E}$</td><td>equivalent load factor</td></tr><tr><td>$C_{f}$</td><td>post-failure fragment coefficient $(\mathsf{I b}^{2}\mathrm{-}\mathsf{m s}^{4}/\mathsf{i n}^{8})$</td></tr><tr><td>$C_{H}$</td><td>shear coefficient for ultimate shear stress in horizontal direction for two- way elementst</td></tr><tr><td>$C_{L}$</td><td>leakage pressure coefficient</td></tr><tr><td>$C_{M}$</td><td>maximum shear coefficient</td></tr><tr><td>$C_{R}$</td><td>force coefficient for shear at the corners of a window frame</td></tr><tr><td>$C_{r}$</td><td>coefficient for effective resistance of glass</td></tr><tr><td>$C_{r\alpha}$</td><td>peak reflected pressure coefficient at angle of incidence α</td></tr><tr><td></td><td></td></tr><tr><td>$c_{s}$</td><td>dilatational velocity of concrete (ft/sec)</td></tr></table></body></html></div>


<!-- batch 35 | page 58 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>shear coefficient for ultimate support shear for one-way elements $C_{s}$</td><td></td></tr><tr><td>$C_{s H}$</td><td>shear coefficient for ultimate support shear in horizontal direction for two- way elements*</td></tr><tr><td>$C_{s V}$</td><td>shear coefficient for ultimate support shear in vertical direction for two-way elements*</td></tr><tr><td>$C_{T}$</td><td>coefficient for period of vibration for glass</td></tr><tr><td>$C_{u}$</td><td>impulse coefficient at deflection $X_{u}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>$C_{u}^{\prime}$</td><td>impulse coefficient at deflection $X_{m}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>$C_{v}$</td><td>shear coefficient for ultimate shear stress in vertical direction for two-way elements</td></tr><tr><td>$C_{x}$</td><td>shear coefficient for the ultimate shear along the long side of window frame</td></tr><tr><td>$C_{y}$</td><td>shear coefficient for the ultimate shear along the short side of window frame</td></tr><tr><td>$C_{1}$</td><td>(1) impulse coefficient at deflection $X_{1}~(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td></td><td>(2) ratio of gas load to shock load</td></tr><tr><td>$C_{1}^{\prime}$</td><td>impulse coefficient at deflection $X_{m}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>$C_{2}$</td><td></td></tr><tr><td>$d$</td><td>ratio of gas load duration to shock load duration distance from extreme compression fiber to centroid of tension</td></tr><tr><td>$d^{\prime}$</td><td>reinforcement (in)</td></tr><tr><td>$d_{c}$</td><td>distance from extreme compression fiber to centroid of compression reinforcement (in)</td></tr><tr><td>$d_{c o}$</td><td>distance between the centroids of the compression and tension reinforcement (in)</td></tr><tr><td></td><td>diameter of steel core (in)</td></tr><tr><td>$d_{e}$</td><td>distance from support and equal to distance d or $d_{c}\left(\mathsf{i n}\right)$</td></tr><tr><td>$d_{i}$</td><td>inside diameter of cylindrical explosive container (in)</td></tr><tr><td>$d_{1}$</td><td>distance between center lines of adjacent lacing bends measured normal to flexural reinforcement (in)</td></tr></table></body></html></div>


<!-- batch 35 | page 59 -->

dp distance from extreme compression fiber to centroid of prestressed 

reinforcement (in)

$d_{1$diameter of cylindrical portion of primary fragment (in)

D (1)unit flexural rigidity (lb-in)

(2)location of shock front for maximum stress (ft)

(3)minimum magazine separation distance (ft)

$D_{o}$ nominal diameter of reinforcing bar (in)

$D_{E}$ equivalent loaded width of structure for non-planar wave front (ft)

DIF dynamic increase factor 

DLF dynamic load factor 

e (1)base of natural logarithms and equal to 2.71828...

(2)distance from centroid of section to centroid of prestressed 

reinforcement (in)

(2E')$Gurney Energy Constant (ft/sec)

E modulus of elasticity 

$E_{c}$ modulus of elasticity of concrete (psi)

$E_{m}$ modulus of elasticity of masonry units (psi)

$E_{s}$ modulus of elasticity of reinforcement (psi)

f (1) unit external force (psi)

(2) frequency of vibration (cps)

$f_{c}$ static ultimate compressive strength of concrete at 28 days (psi)

$\pmb{f}_{d c}$ dynamic ultimate compressive strength of concrete (psi)

$f^{d$dynamic ultimate compressive strength of masonry units (psi)

fds dynamic design stress for reinforcement (psi)

$f_{d u}$ dynamic ultimate stress of reinforcement (psi)

$f_{d y}$ dynamic yield stress of reinforcement (psi)

$f_{m}$ static ultimate compressive strength of masonry units (psi)

$f_{n}$ natural frequency of vibration (cps)



<!-- batch 35 | page 60 -->

fps average stress in the prestressed reinforcement at ultimate load (psi)

加yield stress of prestressing tendon corresponding to a1 percent specified tensile strength of prestressing tendon (psi)

elongation (psi)

f_s$static design stress for reinforcement (a function of fy, f & p) (psi)

fse effective stress in prestressed reinforcement after allowances for all 

prestress losses (psi)

f_u static ultimate stress of reinforcement (psi)

$f_}$static yield stress of reinforcement (psi)

F (1)total external force (lbs)

(2)coefficient for moment of inertia of cracked section 

(3)function of C2& C{₁ for bilinear triangular load 

Fo$force in the reinforcing bars (lbs)

FE equivalent external force (lbs)

g (1)variable defined in Table 4-3 (+)

(2)acceleration due to gravity (ft/sec2)

G shear modulus (psi)

h (1)charge location parameter (ft)

(2)height of masonry wall 

h'clear height between floor slab and roof slab 

H (1)span height (in)

(2)distance between reflecting surface(s) and/or free edge(s) in 

vertical direction (ft)

$H_{c}$ (1)height of charge above ground (ft)

(2)scaled height of charge above ground (ft/lb1/3)

$H_{s}$ height of structure (ft)

$H_{T}$ scaled height of triple point (ft/|b1/3)

i unit positive impulse (psi-ms)

i unit negative impulse (psi-ms)



<!-- batch 35 | page 61 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>$\{}$</td><td>sum of scaled unit blast impulse capacity of receiver panel and scaled unit</td></tr><tr><td></td><td>blast impulse attenuated through concrete and sand in a composite element $(\mathsf{p s i}{\tt-m s}/\mathsf{I b}^{1/3})$</td></tr><tr><td>$j_{b}$</td><td>unit blast impulse (psi-ms)</td></tr><tr><td>$j_{b}$</td><td>scaled unit blast impulse $(\mathsf{p s i}{\tt-m s}/\mathsf{I b}^{1/3})$</td></tr></thead><tbody><tr><td>ibt</td><td>total scaled unit blast impulse capacity of composite element (psi-ms/lb1/3)</td></tr><tr><td>$\overline{{\dot{I}_{b a}}}$</td><td>scaled unit blast impulse capacity of receiver panel of composite element (psi-ms/lb1/³3)</td></tr><tr><td>$\overline{{\dot{I}_{b d}}}$</td><td>scaled unit blast impulse capacity of donor panel of composite element (psi-ms/|b{/³3)</td></tr><tr><td>ie</td><td>unit excess blast impulse (psi-ms)</td></tr><tr><td>$i$</td><td>unit positive normal reflected impulse (psi-ms)</td></tr><tr><td>$i_{r}$</td><td>unit negative normal reflected impulse (psi-ms)</td></tr><tr><td>$j_{s}$</td><td>unit positive incident impulse (psi-ms)</td></tr><tr><td>$j_{s}\bar{}$</td><td>unit negative incident impulse (psi-ms)</td></tr><tr><td></td><td>moment of inertia (in4)</td></tr><tr><td>$I_{a}$</td><td>average of gross and cracked moments of inertia of width b (in4)</td></tr><tr><td>$I_{c}$</td><td>moment of inertia of cracked concrete section of width b (i4)</td></tr><tr><td>$I_{g}$</td><td>moment of inertia of gross concrete section of width b (in4)</td></tr><tr><td>$I_{m}$</td><td>(1) mass moment of inertia $(\mathsf{I b}{-}\mathsf{m s}^{2}{-}\mathsf{i n})$</td></tr><tr><td></td><td>(2) moment of inertia of masonry block per unit width $(\mathsf{i n}^{4}/\mathsf{i n})$</td></tr><tr><td>$I_{n}$</td><td>moment of inertia of net section of masonry unit $(\mathsf{i n}^{4}/\mathsf{i n})$</td></tr><tr><td>j</td><td>ratio of distance between centroids of compression and tension forces to the depth d</td></tr><tr><td>K</td><td>(1)t)))</td></tr><tr><td>$K_{e}$</td><td>elastic unit stifness (psi/in for slabs) (Ib/in/in for beams)</td></tr><tr><td>$K_{e p}$</td><td>elasto-plastic unit stfness (psi-in for slabs) (psi for beams)</td></tr></tbody></table></body></html></div>


<!-- batch 35 | page 62 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>(1) $K_{E}$</td><td>equivalent elastic unit stiffness (psi-in for slabs) (psi for beams)</td></tr><tr><td>(2)</td><td>equivalent spring constant</td></tr><tr><td>load factor $K_{L}$</td><td></td></tr><tr><td>$K_{L M}$</td><td>load-mass factor</td></tr><tr><td>$(K_{L M})_{u}$</td><td>load-mass factor in the ultimate range</td></tr><tr><td>$(K_{L M})_{u p}$</td><td>load-mass factor in the post-ultimate range</td></tr><tr><td>$K_{M}$</td><td>mass factor</td></tr><tr><td>$K_{m}$</td><td>Constant defined in section 6-7.3.2</td></tr><tr><td>$K_{v}$</td><td>Constant defined in section 6-7.3.4</td></tr><tr><td>$K_{R}$</td><td>resistance factor</td></tr><tr><td>$K E$</td><td>kinetic energy</td></tr><tr><td></td><td>charge location parameter (ft)</td></tr><tr><td>$I_{p}$</td><td>spacing of same type of lacing bar (in)</td></tr><tr><td>L</td><td>(1) span length $(\mathsf{i n})\S$</td></tr><tr><td>(2)</td><td>distance between reflecting surface(s) and/or free edge(s) in horizontal direction (ft)</td></tr><tr><td>$L_{I}$</td><td>length of lacing bar required in distance s, (in)</td></tr><tr><td>$L_{o}$</td><td>embedment length of reinforcing bars (in)</td></tr><tr><td>$L_{s}$</td><td>length of shaft (in)</td></tr><tr><td>$L_{w}$</td><td>wave length of positive pressure phase (ft)</td></tr><tr><td>$L_{w}^{\mathrm{~1~}}$</td><td>wave length of negative pressure phase (ft)</td></tr><tr><td>$L_{w b},L_{w d}$</td><td>wave length of positive pressure phase at points b and d, respectively (ft)</td></tr><tr><td>$L_{v}$</td><td>shear wall length resisting in-plane shear (in)</td></tr><tr><td>$L_{1}$</td><td>total length of sector of element normal to axis of rotation (in)</td></tr><tr><td>unit mass $m$</td><td>$(\mathsf{p s i}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$m_{a}$</td><td>average of the effective elastic and plastic unit masses $(\mathsf{p s i}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr></table></body></html></div>


<!-- batch 35 | page 63 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>$m_{u}$ $m_{e}$</td><td>effective unit mass effective unit mass in the ultimate range $(\mathsf{p s i}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$m_{u p}$</td><td>effective unit mass in the post-ultimate range $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$ $(\mathsf{p s i}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>(1) $M$</td><td></td></tr><tr><td>(2)</td><td>unit bending moment (in-Ibs/in) total mass. $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{e}$</td><td>1 effective total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{u}$</td><td>ultimate unit resisting moment (in-Ibs/in)</td></tr><tr><td>$M_{u}^{-}$</td><td>ultimate unit rebound moment (in-lbs/in)</td></tr><tr><td>$M_{c}$</td><td>moment of concentrated loads about line of rotation of sector $(\mathsf{i n-l b s})$</td></tr><tr><td>$M_{A}$</td><td>fragment distribution parameter</td></tr><tr><td>$M_{E}$</td><td>equivalent total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{H N}$</td><td>ultimate unit negative moment capacity in horizontal direction $(\mathsf{i n-l b s/i n})^{\star}$</td></tr><tr><td>$M_{H P}$</td><td>ultimate unit positive moment capacity in horizontal direction $(\mathsf{i n-l b s/i n})^{\star}$</td></tr><tr><td>$M_{N}$</td><td>ultimate unit negative moment capacity at supports (in-lbs/in)</td></tr><tr><td>$M_{P}$</td><td>ultimate unit positive moment capacity at midspan (in-lbs/in)</td></tr><tr><td>$M_{V N}$</td><td>ultimate unit negative moment capacity in vertical direction $\left(\mathrm{i n}\mathrm{-}\mathrm{l b s}/\mathrm{i n}\right)^{\star\star}$</td></tr><tr><td>$M_{V P}$</td><td></td></tr><tr><td>n (1)</td><td>ultimate unit positive moment capacity in vertical direction $(\mathsf{i n}{-}\mathsf{l b s}/\mathsf{i n})^{\star}$</td></tr><tr><td>(2)</td><td>modular ratio</td></tr><tr><td>(3)</td><td>number of time intervals</td></tr><tr><td>$N$</td><td>number of glass pane tests</td></tr><tr><td></td><td>number of adjacent reflecting surfaces</td></tr><tr><td>$N_{f}$</td><td>number of primary fragments larger than $W_{f}$</td></tr><tr><td>$p$</td><td>reinforcement ratio equal to $(A_{s}/b d)\;\mathrm{o r}\;(A_{s}/b d_{c})$</td></tr><tr><td>$p^{\prime}$</td><td>reinforcement ratio equal to or $(A^{\prime}{}_{s}/b d_{c})$ $(A^{\prime}{}_{s}/b d)$</td></tr><tr><td>$p_{b}$</td><td>reinforcement ratio producing balanced conditions at ultimate strength</td></tr><tr><td>$p_{p}$</td><td>prestressed reinforcement ratio equal to $A_{p s}/b d_{p}$</td></tr></table></body></html></div>


<!-- batch 35 | page 64 -->

$p_{m}$ mean pressure in a partially vented chamber (psi)

$p_{m o}$ peak mean pressure in a partially vented chamber (psi)

$p_{H}$ reinforcement ratio in horizontal direction on each face*

$p_{T}$ reinforcement ratio equal to $p_{H}+p_{v}$ 

$p_{v}$ reinforcement ratio in vertical direction on each face*

$p(x)$ distributed load per unit length 

$P$ (1) pressure (psi)

(2)concentrated load (lbs)

$P$ negative pressure (psi)

$P_{i}$ (1)interior pressure within structure (psi)

(2)interior pressure increment (psi)

$P_{f}$ fictitious peak pressure (psi)

$P_{o}$ peak pressure (psi)

$P_{r}$ peak positive normal reflected pressure (psi)

$P_{r}^{-}$ peak negative normal reflected pressure (psi)

$p_{r a}$ peak reflected pressure at angle of incidence a (psi)

$P_{s}$ positive incident pressure (psi)

$P_{s b},P_{s e}$ positive incident pressure at points b and e, respectively (psi)

$P_{s o}$ peak positive incident pressure (psi)

$P_{s o}$ peak negative incident pressure (psi)

$P_{s o b},P_{s o d},P_{s o e}$ peak positive incident pressure at points b, d, and e, respectively (psi)

$P(F)$ probability of failure of glass pane 

q dynamic pressure (psi)

$q_{b},q_{e}$ dynamic pressure at points b and e, respectively (psi)

$q_{o}$ peak dynamic pressure (psi)

$q_{o b},q_{o e}$ peak dynamic pressure at points b and e, respectively (psi)

r (1)unit resistance (psi)

(2)radius of spherical TNT (density equals 95 Ib/ft3) charge (ft)



<!-- batch 35 | page 65 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>r</td><td>unit rebound resistance (psi for panels) (Ilb/in for beams)</td></tr><tr><td>$r_{d}$ $\Delta r$</td><td>change in unit resistance (psi for panels) (Ib/in for beams)</td></tr><tr><td></td><td>radius from center of impulse load to center of door rotation (in)</td></tr><tr><td>$r_{e}$</td><td>elastic unit resistance (psi for panels) (Ib/in for beams)</td></tr><tr><td>$r_{s}$ $r_{e p}$</td><td>elasto-plastic unit resistance (psi for panels) (Ib/in for beams)</td></tr><tr><td>$r_{u}$</td><td>radius of shaft (in) ultimate unit resistance (psi for panels) (Ilb/in for beams)</td></tr><tr><td>$r_{u p}$</td><td>post-ultimate unit resistance (psi)</td></tr><tr><td>$r_{1}$</td><td>radius of hemispherical portion of primary fragment (in)</td></tr><tr><td>(1) $R$</td><td></td></tr><tr><td></td><td>total internal resistance (Ibs) (2) slant distance (ft)</td></tr><tr><td>$R_{f}$</td><td>distance traveled by primary fragment (ft)</td></tr><tr><td>$R_{g}$</td><td>uplift force at corners of window frame (Ibs)</td></tr><tr><td>$R_{I}$</td><td>radius of lacing bend (in)</td></tr><tr><td>$R_{A}$</td><td>normal distance (ft)</td></tr><tr><td>$R_{E}$</td><td>equivalent total internal resistance (Ilbs)</td></tr><tr><td>$R_{G}$</td><td>ground distance (ft)</td></tr><tr><td>$R_{u}$</td><td>total ultimate resistance</td></tr><tr><td>$R_{L},R_{I I}$</td><td>total internal resistance of sectors I and Il, respectively (Ibs)</td></tr><tr><td>S</td><td>sample standard deviation</td></tr><tr><td>$\mathcal{S}_{V}$</td><td>spacing between shear stirrups (in)</td></tr><tr><td>S</td><td>height of front wall or one-half its width, whichever is smaller (ft)</td></tr><tr><td>$S_{E}$</td><td>strain energy</td></tr><tr><td>t</td><td>time (ms)</td></tr><tr><td>$\Delta\pmb{t}$</td><td></td></tr><tr><td></td><td>time increment (ms)</td></tr><tr><td>$t_{a}$</td><td>any time (ms)</td></tr><tr><td>$t_{b}$ $t_{e}$ $t_{f}$</td><td>time of arrival of blast wave at points b, e, and f, respectively (ms)</td></tr></tbody></table></body></html></div>


<!-- batch 35 | page 66 -->

tc (1)clearing time for reflected pressures (ms)

(2)container thickness of explosive charges (in)

t{$rise time (ms)

tE time to reach maximum elastic deflection 

tm$time at which maximum deflection occurs (ms)

to duration of positive phase of blast pressure (ms)

$t_{}$duration of negative phase of blast pressure (ms)

tof fictitious positive phase pressure duration (ms)

tof fictitious negative phase pressure duration (ms)

t{r fictitious reflected pressure duration (ms)

t_s$CMU face shell thickness 

tu time at which ultimate deflection occurs (ms)

ty time to reach yield (ms)

tA time of arrival of blast wave (ms)

$t_{1$time at which partial failure occurs (ms)

T (1)duration of equivalent triangular loading function (ms)

(2)thickness of masonry wall 

Tc$(1)thickness of concrete section (in)

(2)scaled thickness of concrete section (ft/lb1/3)

Tg thickness of glass (in)

Ti angular impulse load (lb-ms-in)

$T_{N}$ effective natural period of vibration (ms)

$T_{r}$ rise time (ms)

$T_{s}$ thickness of sand fill (in)

$\overline{{T_{s}}}$ scaled thickness of sand fill(ft/lb1/^3)

u particle velocity (ft/ms)

uu ultimate flexural or anchorage bond stress (psi)



<!-- batch 35 | page 67 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>U</td><td colspan="2">shock front velocity (ft/ms)</td></tr></thead><tbody><tr><td>$U_{s}$ $v$</td><td colspan="2">strain energy</td></tr><tr><td>$v_{a}$</td><td colspan="2">velocity (in/ms)</td></tr><tr><td></td><td colspan="2">instantaneous velocity at any time (in/ms)</td></tr><tr><td>$v_{b}$</td><td colspan="2">boundary velocity for primary fragments (ft/sec)</td></tr><tr><td>$v_{c}$</td><td colspan="2">ultimate shear stress permitted on an unreinforced web (psi)</td></tr><tr><td>$v_{f}$</td><td colspan="2">maximum post-failure fragment velocity (in/ms)</td></tr><tr><td>$f(avg.)</td><td colspan="2">average post-failure fragment velocity (in/ms)</td></tr><tr><td>$v_{i}$</td><td colspan="2">velocity at incipient failure deflection (in/ms)</td></tr><tr><td>$v_{o}$</td><td colspan="2">initial velocity of primaFry fragment (ft/sec)</td></tr><tr><td>$v_{r}$</td><td colspan="2">residual velocity of primary fragment after perforation (ft/sec)</td></tr><tr><td>$v_{s}$</td><td colspan="2">striking velocity of primary fragment (ft/sec)</td></tr><tr><td>$v_{u}$</td><td colspan="2">ultimate shear stress (psi)</td></tr><tr><td>$v_{u H}$</td><td colspan="2">ultimate shear stress at distancefrom the horizontal support(psi)tt $d_{e}$</td></tr><tr><td>$v_{u V}$</td><td colspan="2">ultimate shear stress at distance from the vertical support (psi)* $d_{e}$</td></tr><tr><td>V</td><td colspan="2">percent of voids that are grouted</td></tr><tr><td>$V_{d}$</td><td colspan="2">ultimate direct shear capacity of the concrete of width b (Ibs)</td></tr><tr><td>$V_{d m}$</td><td colspan="2">dynamic shear friction strength of masonry per unit width along wall (Ib/in)</td></tr><tr><td>$V_{d H}$</td><td>$d_{e}$</td><td>shear at distance from the vertical support on a unit width (Ibs/in)*</td></tr><tr><td>$\mathsf{V}_{\mathsf{d V}}$</td><td>$d_{e}$</td><td>shear at distance from the horizontal support on a unit width (Ibs/in)*</td></tr><tr><td>$V_{m}$</td><td colspan="2">dynamic shear strength of masonry (Ib/in)</td></tr><tr><td>$V_{0}$</td><td colspan="2">volume of structure $(\mathsf{f t}^{3})$</td></tr><tr><td>$V_{s}$</td><td colspan="2">shear force resisted by shear reinforcement (Ib/in)</td></tr><tr><td>$V_{m i}$</td><td colspan="2">in-plane shear force resisted by masonry (Ib)</td></tr><tr><td>$V_{m o}$</td><td colspan="2">out-of-plane shear force resisted by masonry (lb)</td></tr><tr><td>$V_{s i}$</td><td colspan="2">in-plane shear force resisted by shear reinforcement (Ib)</td></tr></tbody></table></body></html></div>


<!-- batch 35 | page 68 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>shear at the vertical support on a unit width (Ibs/in)* $V_{s o}$</td><td>out-of-plane shear force resisted by shear reinforcement (lb)</td></tr></thead><tbody><tr><td>$\mathsf{V}_{\mathsf{s}\mathsf{V}}$ $V_{s H}$</td><td>shear at the horizontal support on a unit width (Ibs/in)*</td></tr><tr><td>total shear on a width b (lbs)</td><td></td></tr><tr><td>$V_{u}$</td><td>peak applied in-plane shear force to masonry wall (Ib)</td></tr><tr><td></td><td>peak applied out-of-plane shear force to masonry wall unit shear $(\mathsf{I b})V_{x}$</td></tr><tr><td>$V_{u i}$ $V_{u o}$</td><td>along the long side of window frame (Ib/in)</td></tr><tr><td>$V_{y}$</td><td>unit shear along the short side of window frame (Ibs/in)</td></tr><tr><td>$w$</td><td>unit weight (psi for panels) (Ib/in for beams)</td></tr><tr><td>$w_{c}$</td><td>weight density of concrete $(\mathsf{I b s}/\mathsf{f t}^{3})$</td></tr><tr><td>$w_{s}$</td><td>weight density of sand $(\mathsf{I b s}/\mathsf{f t}^{3})$</td></tr><tr><td>(1) $W$</td><td>charge weight (Ibs)</td></tr><tr><td>(2)</td><td>weight (lbs)</td></tr><tr><td>$W_{c}$</td><td>total weight of explosive containers (Ilbs)</td></tr><tr><td>$W_{f}$</td><td>weight of primary fragment (oz)</td></tr><tr><td>$W_{c o}$</td><td>total weight of steel core (lbs)</td></tr><tr><td>$W_{c1},W_{c2}$</td><td>total weight of plates 1 and 2, respectively (lbs)</td></tr><tr><td>$W_{s}$</td><td>width of structure (ft)</td></tr><tr><td>WD</td><td>work done</td></tr><tr><td>X</td><td>yield line location in horizontal direction $(\mathsf{i n})^{\ddagger\ddagger}$</td></tr><tr><td>$X$</td><td>deflection (in)</td></tr><tr><td>$X_{a}$</td><td>any deflection (in)</td></tr><tr><td>$X_{c}$</td><td>lateral deflection to which a masonry wall develops no resistance (in)</td></tr><tr><td>$X_{e}$</td><td>elastic deflection (in)</td></tr><tr><td>$X_{e p}$</td><td>elasto-plastic deflection (in)</td></tr><tr><td>$X_{t}$</td><td>maximum penetration into concrete of armor-piercing fragments (in)</td></tr></tbody></table></body></html></div>


<!-- batch 35 | page 69 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td colspan="2">maximum penetration into concrete of fragments other than armor-piercing (in) $X_{f}^{r}$</td></tr><tr><td colspan="2">maximum transient deflection (in) $X_{m}$ $X_{u}$ $X_{p}$ $X_{s}$</td></tr><tr><td colspan="2">plastic deflection (in)</td></tr><tr><td colspan="2">(1) maximum penetration into sand of armor-piercing fragments (in)</td></tr><tr><td colspan="2">(2) static deflection (in)</td></tr><tr><td colspan="2">ultimate deflection (in)</td></tr><tr><td colspan="2">equivalent elastic deflection (in)</td></tr><tr><td colspan="2">(1) partial failure deflection (in)</td></tr><tr><td colspan="2">(2) deflection at maximum ultimate resistance of masonry wall (in)</td></tr><tr><td colspan="2">y yield line location in vertical direction (in) $X_{1}$ $X_{E}$</td></tr><tr><td colspan="2">yt distance from the top of section to centroid (in)</td></tr><tr><td colspan="2">Z scaled slant distance (ft/|b1/"3)</td></tr><tr><td colspan="2">scaled normal distance (ft/b/3) $Z_{A}$</td></tr><tr><td colspan="2">scaled ground distance (ft/lb1/{3) angle formed by the plane of stirrups, lacing, or diagonal</td></tr><tr><td colspan="2">α (1) $Z_{G}$</td></tr><tr><td>(2)</td><td>reinforcement and the plane of the longitudinal reinforcement (dg) angle of incidence of the pressure front (deg)</td></tr><tr><td>(3)</td><td>acceptance coefficient</td></tr><tr><td colspan="2">B (1) coefficient for determining elastic and elasto-plastic resistances</td></tr><tr><td colspan="2">(2) particular support rotation angle (deg)</td></tr><tr><td colspan="2">(3) rejection coefficient $\beta_{1}$</td></tr><tr><td colspan="2">factor equal to 0.85 for concrete strengths up to 4,000 psi and is reduced by 0.05 for each 1,000 psi in excess of 4,000 psi</td></tr><tr><td colspan="2">coefficient for determining elastic and elasto-plastic deflections</td></tr><tr><td colspan="2">7 $γp</td></tr><tr><td colspan="2">factor for type of prestressing tendon unit strain in mortar (in/in) $\varepsilon_{m}$</td></tr></table></body></html></div>


<!-- batch 35 | page 70 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>?</td><td>(1)</td><td>support rotation angle (deg)</td></tr><tr><td></td><td>(2)</td><td>angular acceleration (rad/ms2)</td></tr><tr><td>$\varTheta_{m a x}$</td><td colspan="2">maximum support rotation angle (deg)</td></tr></thead><tbody><tr><td>ΘH</td><td colspan="2">horizontal rotation angle (deg)*</td></tr><tr><td>QV</td><td colspan="2">vertical rotation angle (deg)*</td></tr><tr><td>λ</td><td colspan="2">increase in support rotation angle after partial failure (deg)</td></tr><tr><td>μ</td><td colspan="2">ductility factor</td></tr><tr><td>V</td><td colspan="2">Poisson's ratio</td></tr><tr><td>∑o</td><td colspan="2">effective perimeter of reinforcing bars (in)</td></tr><tr><td>ΣM</td><td colspan="2">summation of moments (in-lbs)</td></tr><tr><td>$\Sigma M_{N}$</td><td colspan="2">sum of the ultimate unit resisting moments acting along the negative yield lines (in-lbs)</td></tr><tr><td>$\Sigma M_{p}$</td><td colspan="2">sum of the ultimate unit resisting moments acting along the positive yield lines (in-lbs)</td></tr><tr><td>ρm</td><td colspan="2">density of CMU material</td></tr><tr><td>ρg</td><td colspan="2">density of grout (equal to 120 pcf)</td></tr><tr><td>ts</td><td colspan="2">maximum shear stress in the shaft (psi)</td></tr><tr><td>φ</td><td colspan="2">(1) capacity reduction factor</td></tr><tr><td></td><td colspan="2">(2) bar diameter (in)</td></tr><tr><td>$\Psi_{\mathsf{m}}$</td><td colspan="2">ratio of width of voids in CMU masonry block to overall block width</td></tr><tr><td>Φ$</td><td colspan="2">assumed shape function for concentrated loads</td></tr><tr><td>$φ(x)</td><td colspan="2">assumed shape function for distributed loads free edge</td></tr><tr><td>ω</td><td colspan="2">angular velocity (rad/ms) simple support</td></tr><tr><td colspan="2"></td><td colspan="2"></td></tr><tr><td colspan="2">77777 fixed support</td><td colspan="2"></td></tr><tr><td colspan="2">XXXXXXXX</td><td colspan="2">either fixed, restrained, or simple support</td></tr></tbody></table></body></html></div>


<!-- batch 35 | page 71 -->

UFC 3-340-025 December 2008Change 2,1 September 2014Note:This symbol was developed for two-way elements which are used as walls. When roof slabs or other horizontal elements are under construction, this symbol will also be applicable if the element is treated as being rotated into a vertical position.



<!-- batch 35 | page 72 -->

## APPENDIX 6C BIBLIOGRAPHY 

## Masonry 

1.Design of Masonry Structures to Resist the Effects of HE Explosions, prepared by Ammann & Whitney, Consulting Engineers, New York, NY, for Picatinny Arsenal, Dover, NJ, 1976.
2.Gabrielsen, G., Wilton, C., and Kaplan, K., Response of Arching Walls and Debris from Interior Walls Caused by Blast Loading, URS 7030-23, URS Research Company, San Mateo, CA, February 1976.
3.McDowell, E., McKee, K., and Sevin, E., Arching Action Theory of Masonry Walls, Journal of the Structural Division, Journal of the Structural Division, ASCE,
Vol. 82,No. ST 2, March 1956.
4.Wilton, C., and Gabrielsen, B., Shock Tunnel Tests of Pre-Loaded and Arched Wall Panels, URS 7030-10, URS Research Company, San Mateo, CA. June 1973.
\1\
5.Bowles, P.K., Grosch, D.J., Goodlin, D. and Plenge, B.T., "Fragment Penetration Effects Model,”AFRL-MN-EG-TR-1998-7029., March, 199.6.NCMA TEK 2-1A, "Typical Sizes and Shapes of Concrete Masonry Units,"
National Concrete Masonry Association, 2002.
7.NCMA TEK 3-6B, "Concrete Masonry Veneers," National Concrete Masonry Association, 2005.
8.NCMA TEK 12-2B, "Joint Reinforcement for Concrete Masonry Units," National Concrete Masonry Association, 2005.
9.Oswald, C.J., Nebuda, D., Holgado, D., and Diaz, M." Shock Tube Testing on Reinforced Masonry Walls," Proceedings from the 32nd DoD Explosives Safety Seminar, 2006.
10.Oswald, C.J., Nebuda, D., Diaz, M., "Component Explosive Damage Assessment Workbooks for Masonry Walls," Proceedings from the 31rst DoD Explosives Safety Seminar, 2004.
/1/


## Precast Concrete 

11.PCI Design Handbook Precast Prestressed Concrete, Prestressed Concrete Institute, Chicago, IL, 1978.



<!-- batch 35 | page 73 -->

12.PCI Manual for Structural Design of Architectural Precast Concrete, Prestressed Concrete Institute, Chicago, IL.
13.PCI Manual on Design of Connections for Precast Prestressed Concrete,
Prestressed Concrete Institute, Chicago, IL.
14.Lin, T.Y., Design of Prestressed Concrete Structures, John Wiley & Sons, New York, NY, July 1955.
Pre-Engineered Buildings 15.American National Standard Minimum Design Loads for Buildings and Other Structures, ANSI A58.1-1982, American National Standards Institute, New York,
NY, March 12.
16.Specification for the Design of Cold-Formed Steel Structural Members, American Iron and Steel Institute, New York, NY, 1968.
17.Specification for the Design, Fabrication and Erection of Structural Steel for Buildings, Manual of Steel Construction, American Institute of Steel Construction,
New York, NY, 1969.
18.Uniform Building Code (1979 Edition), International Conference of Building Officials, Whittier, CA, 1979.
19.Healey, J. J., et al., Design of Steel Structures to Resist the Effects of HE Explosions, Technical Report 4837, Picatinny Arsenal, Dover, NJ, August 1975.20.Stea, W., et al, Blast Capacity Evaluationof Pre-Engineered Building, Contractor Report ARLCD-CR-79004,U.S. Army Armament Research and Development Command, Dover, NJ, March 1979.
21.Stea, W., et al., Nonlinear Analysis of Frame Structures to Blast Overpressures,
by Ammann & Whitney, Consulting Engineers, New York, NY, Contractor Report ARLCD-CR-77008, U.S. Army Armament Research and Development Command, Dover, NJ, May 1977.
22.Tseng, G., et al., Design Charts for Cold-Formed Steel Panels and Wide-Flange Beams Subjected to Blast Loads, Technical Report 4838, Picatinny Arsenal,
Dover, NJ, August 1975.
Suppressive Shielding 23.Final Report Application of Suppressive Structure Concepts to Chemical Agent Munitions Demilitarization System (CAMDS), Report EA-FR-2B02, Edgewood Arsenal, Aberdeen Proving Ground, MD, June 27, 1973.24.Shields Operational for Ammunition Operations, Criteria for Design of, and Tests for Acceptance, MIL STD 398, U.S. Government Printing Office, Washington,
D.C., November 5, 1976.


<!-- batch 35 | page 74 -->

25.Study of Suppressive Structures Applications to an 81 mm Automated Assembly Facility, Report EA 1002, Edgewood Arsenal, Aberdeen Proving Ground, MD,April 16, 1973.
26.Suppressive Shielding, AAI Corporation, Cockeysville, MD, DAAA15-75-C-0120,
U.S. Army Armament Research and Development Command, Chemical Systems Laboratory, Aberdeen Proving Ground, MD, April 1977.27.Suppressive Shields Structural Design and Analysis Handbook, HNDM 1110-1-2,
U.S. Army Corps of Engineers, Huntsville Division, Huntsville, AL, November 1977.
28.System Safety Program Requirements, MIL STD 882A, U. S. Government Printing Office, Washington, D.C., June 28, 1977.
29.Baker, W. E., et al., Design Study of a Suppressive Structure for a Melt Loading Operation, EM-CR-76043, Report No. 9, Edgewood Arsenal, Aberdeen Proving Ground, MD, December 1975.
30.Baker, W. E. and Oldham, G. A., Estimates of Blowdown of Quasi-Static Pressures in Vented Chambers, EM-CR-76029, Edgewood Arsenal, Aberdeen Proving Ground, MD, November 1975.
31.Baker, W. E. and Westine, P. S., Methods of Predicting Blast Loads Inside and Outside Suppressive Structures, EM-CR-76026, Report No. 5, Edgewood Arsenal, Aberdeen Proving Ground, MD, 1975.
32.Cox, P.A., et al., Analysis and Evaluation of Suppressive Shields, Edgewood Arsenal Contractor Report ARCFL-CR-77028, Report No. 10, Contract No.
DAAA15-75-C-0083, Edgewood Arsenal, Aberdeen Proving Ground, MD,
January 1978.
33.Dutton, S. R. and Katsanis, D., Computer-Aided Design of Suppressive Shields,
EM-CR-76080, AAI Corporation, Baltimore, MD, Report for Edgewood Arsenal,
Aberdeen Proving Ground, MD, June 1976.
34.Esparza, E. D., Estimating External Blast Loads from Suppressive Structures,
Edgewood Arsenal Contract Report EM-CR-76030, Report No. 3, Edgewood Arsenal, Aberdeen Proving Ground, MD, November 1975.35.Esparza, E. D., Baker, W. E., and Oldham, G. A., Blast Pressures Inside and Outside Suppressive Structures, Edgewood Arsenal Contractor Report EM-CR76042, Report No. 8, Edgewood Arsenal, Aberdeen Proving Ground, MD,
December 1975.
36.Gregory, F. H., Blast Loading Calculations and Structural Response Analyses of the 1/4-Scale Category I Suppressive Shield, BRL Report No. 2003, U.S. Army Ballistic Research Laboratory, Aberdeen Proving Ground, MD, August 1977.

<!-- batch 35 | page 75 -->

37.Hubich, H. O. and Kachinski, R. L., Explosive Waste Removal Systems for Suppressive Shields, Edgewood Arsenal Contractor Report No. EM-CR76002,Edgewood Arsenal, Aberdeen Proving Ground, MD, August 1975.38.Jezek, B. W., Suppressive Shielding for Hazardous Munitions Production Operations, Technical Report No. ARCSL-TR-77020, U.S. Army Armament Research and Development Command, Chemical Systems Laboratory,Aberdeen Proving Ground, MD, April 1977.
39.Kachinski, R. L., et al., Technical Feasibility of Suppressive Shields for Improved Hawk Launch Sites, Edgewood Arsenal Contractor Report No. EM-CR-76057,
Edgewood Arsenal, Aberdeen Proving Ground, MD, February 1976.40.Katsanis, D. J., Safety Approval of Suppressive Shields, Edgewood Arsenal Technical Report No. EM-TR-76088, Edgewood Arsenal, Aberdeen Proving Ground, MD, August 1976.
41.Katsanis, D. J. and Jezek, B. W., Suppressive Shielding of Hazardous Ammunition Production Operations, Technical Report No. EM-TR-76015,
Edgewood Arsenal, Aberdeen Proving Ground, MD, December 1975.42.Kingery, C. N., Coulter, G., and Pearson, R., Venting of Pressure through Perforated Plates, Technical Report No. ARBRL-TR-02105, U.S. Army Ballistic Research Laboratory, Aberdeen Proving Ground, MD, September 1978.43.Kingery, C. N., Pearson, R., and Coulter, G., Shock Wave Attenuation by Perforated Plates with Various Hole Sizes, BRL Memorandum Report No. 2757,
U.S. Army Materiel Development and Readiness Command, Alexandria, VA,
June 1977.
44.Kingery, C. N., Schumacher, R., and Ewing, W., Internal Pressure from Explosions in Suppressive Shields, BRL Memorandum Report No. ARBRL-MR02848, U.S. Army Armament Research and Development Command, Aberdeen Proving Ground, MD, June 1978.
45.Koger, D. M and McKown, G. L., Category 5 Suppressive Shield Test Report No.
EM-TR-76001, Edgewood Arsenal, Aberdeen Proving Ground, MD, October 1975.
46.Kusher, A. S., et al., Recommended Design and Analysis Procedures for Suppressive Shield Structures, Technical Report No. NSWC/WOL/TR 76112,
Naval Surface Weapons Center, White Oak Laboratory, White Oak, Silver Spring, MD, March 1977.
47.Nelson, K. P., Spherical Shields for the Containment of Explosions, Edgewood Arsenal Technical Report No. EM-TR-76096, Edgewood Arsenal, Aberdeen Proving Ground, MD, March 1977.


<!-- batch 35 | page 76 -->

48.Nelson, K. P., The Economics of Applying Suppressive Shielding to the M483A1Improved Conventional Munitions Loading, Assembling and Packing Facility,Technical Report No. EM-TR-76087, Edgewood Arsenal, Aberdeen Proving Ground, MD, January 1977.
49.Oertel, F. H., Evaluation of Simple Models for the Attenuation of Shock Waves by Vented Plates, BRL Report No. 1906, U.S. Army Ballistic Research Laboratory,
Aberdeen Proving Ground, MD, August 1976.
50.Pei, R., A Design Aid and Cost Estimate Model for Suppressive Shielding Structures, Department of Safety Engineering USAMC Intern Training Center,
Report No. YTC-02-08-76-413, Red River Army Depot, Texarkana, TX,
December 1975.
51.Ricchiazzi, A. J. and Barb, J. C., Test Results for 608 Gram Fraqments Aqainst Category I Suppressive Structures, BRL Memorandum Report No. 2592, U.S.
Army Ballistic Research Laboratory, Aberdeen Proving Ground, MD, February 1976.
52.Schroeder, F. J., et al., Engineering Design Guidelines, Drawings and Specifications for Support Engineering of Suppressive Shields, Edgewood Arsenal Contractor Report No. EM-CR-76097, Edgewood Arsenal, Aberdeen Proving Ground, MD, December 1976.
53.Schumacher, R. N., Air Blast and Structural Response Testing of a Prototype Category Il Suppressive Shield, BRL Memorandum Report No. 2701, U.S. Army Ballistic Research Laboratory, Aberdeen Proving Ground, MD, November 1976.54.Schumacher, R. N. and Ewing, W. O., Blast Attenuation Outside Cubical Enclosures Made Up of Selected Suppressive Structures Panel Configurations,
BRL Memorandum Report No. 2537, U.S. Army Ballistic Research Laboratory,
Aberdeen Proving Ground, MD, September 1975.
55.Schumacher, R. N., Kingery, C. N., and Ewing, W. O., Air Blast and Structural Response Testing of a 1/4-Scale Category I Suppressive Shield, BRL Memorandum Report No. 2623, U.S. Army Ballistic Research Laboratory,
Aberdeen Proving Ground, MD, May 1976.
56.Spencer, A. F. and McKivrigan, J. L., Preliminary Design Procedures for Suppressive Shields, Technical Report No. EM-TR-76089, Edgewood Arsenal,
Aberdeen Proving Ground, MD, December 1976.
57.Westine, P. S. and Baker, W. E., Energy Solutions for Predicting Deformations in Blast-Loaded Structures, Edgewood Arsenal Contractor Report No. EM-CR76027, Report No. 6, Edgewood Arsenal, Aberdeen Proving Ground, MD,
November 1975.


<!-- batch 35 | page 77 -->

58.Westine, P. S. and Cox, P.A., Additional Energy Solutions for Predicting Structural Deformations, Edgewood Arsenal Contractor Report No. EM-CR76031, Report No. 4, Edgewood Arsenal, Aberdeen Proving Ground, MD.November 1975.
59.Westine, P. S. and Kineke, J. H., "Prediction of Constrained Secondary Fragment Velocities," The Shock and Vibration Bulletin, Part 2, Isolation and Damping,
Impact, Blast, Bulletin 48, September 1978.
Blast Resistant Windows 60.Federal Specification Glass, Plate, Sheet, Figured (Float, Flat, for Glazing.
Corrugated, Mirrors and Other Uses), General Service Administration, Federal Specification DD-G-451d, Washington, D.C., 1977.
61.Glass, Plate (Float), Sheet, Figured, and Spandrel (Heat Strengthened and Fully Tempered), General Service Administration, Federal Specification DD-G-1403B,
Washington, D.C., 1972.
62.A Method for Improving the Shatter Resistance of Window Glass, U.S. Army Picatinny Arsenal, National Bomb Data Center, General Information Bulletin 739, Dover, NJ, November 1973.
63.PPG Glass Thickness Recommendations to Meet Architect's Specified 1-Minute Wind Load, PPG Industries, Pittsburgh, PA, March 1981.64.Safety Performance Specifications and Methods of Test for Safety Glazing Material Used in Buildings, American National Standards Institute, ANSI Z97.11975, New York, NY, 1975.
65.Structural Performance of Glass in Exterior Windows, Curtain Walls, and Doors Under the Influence of Uniform Static Loads by Destructive Method, American Society for Testing Materials, ASTM Standard (draft), Draft of Proposed Standard by ASTM Committee E06.51, Philadelphia, PA, October 1982.66.Anians, D., Experimental Study of Edge Displacements of Laterally Loaded Window Glass Plates, Institute for Disaster Research, Texas Technical University, Lubbock, TX, June 1980.
67.Beason, W. L., A Failure Prediction Model for Window Glass, Texas Technical University, NSF/RA 800231, Lubbock, TX, May 1980.
68.Beason, W. L., TAMU Glass Failure Prediction Model, Preliminary Report, Texas A&M University, College Station, TX, March 1982.
69.Beason, W. L., and Morgan, J. R., A Glass Failure Prediction Model, submitted for publication in the Journal of the Structural Division, American Society of Civil Engineers.


<!-- batch 35 | page 78 -->

70.Levy, S., Bending of Rectangular Plates with Large Deflections, NACA Technical Note No. 845, 1942.
71.Meyers, G. E., Interim Desiqn Procedure for Blast-Hardened Window Panes,
567th Shock and Vibration Bulletin, Monterey, CA, October 1985.72.Meyers, G. E., A Review of Adaptable Methodology for Development of a Design Procedure for Blast Hardened Windows, Naval Civil Engineering Laboratory,
Special Report, Port Hueneme, CA, August 1982.
73.Moore, D. M., Proposed Method for Determining the Thickness of Glass in Solar Collector Panels, Jet Propulsion Laboratory, Publication 8034, Pasadena, CA,
March 1980.
74.Moore, D. M., Thickness Sizing of Glass Plates Subjected to Pressure Loads,
FSA Task Report No. 5101-291, Pasadena, CA, August 1982.75.Timoshenko, S. and Woinowsky-Krieger, S., Theory of Plates and Shells,
McGraw-Hill Book Company, New York, NY, 1959.
76.Vallabhan, C. V. G. and Wang, B.Y., Nonlinear Analysis of Rectangular Glass Plates by Finite Difference Method, Texas Technical University, Institute for Disaster Research, Lubbock, TX, June 1981.
77.Weissman, S., et al., Blast Capacity Evaluation of Glass Windows and Aluminum Window Frames, U.S. Army Armament Research and Development Command,
ARLCO-CR-78016, Dover, NJ, June 1978.
Underground Structures 78.Fundamentals of Protective Design for Conventional Weapons, TM 5-8551,
prepared by U.S. Army Engineer Waterways Experimental Station, Vicksburg,
MS, November 1983 (Draft).
79.Arya, et al., Blast Capacity Evaluation of Below-Ground Structures, by Ammann & Whitney, Consulting Engineers, New York, NY, Contractor Report ARLCO-CR77006, U.S. Army Armament Research and Development Command, Dover, NJ,
May 1977.
Earth-Covered Arch-Type Magazine 80.DoD Ammunition and Explosives Safety Standards, Department of Defense Standard, 6055.9-STD 
81.Flathou, W. J., et al., Blast Loading and Response of Underground ConcreteArch Protective Structures, WT-1420, U.S. Waterways Experiment Station,
Jackson, MS, Operation Plumbbob, Project 3.1, Chief, Defense Atomic Support Agency, Washington, D.C.


<!-- batch 35 | page 79 -->

82.Sound, A. R., Summary Report of Earth-Covered, Steel-Arch Magazine Tests,Technical Progress Report No. 401, U.S. Naval Weapon Center, China Lake,CA, July 1965.
83.Weals, F.H., Tests to Determine Separation Distances of Earth-Covered Magazines, U.S. Naval Weapon Center, China Lake, CA, Annals of the New York Academy of Sciences, Conference on Prevention of and Protection against Accidental Explosion of Munitions, Fuels and Other Hazardous Moistures,
Volume 152, Art. 1, October 1968.


## Blast Valves 

84.Investigations Concerning Feasibility of Various Designs for a Blast Closure Device, by American Machine and Foundry Co., Chicago, IL, under Contract No.NBy-13030, for U.S. Navy, Bureau of Yards and Docks, Washington, D.C.85.Shock Tube Test of Mosler Safe Company Blast Valve, BRL Information Memorandum No. 20, Explosion Kinetics Branch, Ballistic Research Laboratories, Aberdeen Proving Ground, MD, August 1959.86.Shock Tube Test of Mosler Safe Company Blast Valve, Phase II, BRL Information Memorandum No. 25, Explosion Kinetics Branch, Ballistic Research Laboratories, Aberdeen Proving Ground, MD, August 1959.87.Study of Blast-Closure Devices, AFSWC-TDR-62-10, by American Machine and Foundry Co., Chicago, IL, for Air Force Special Weapons Center, Kirtland Air Force Base, NM, February 192.
88.Allen, F.C. et al., Test and Evaluation of Anti-Blast Valves for Protective Ventilating Systems, WT-1460, Operation Plumbbob, Project 31.5, available from the Office of Technical Services, Department of Commerce, Washington, D.C.89.Bayles, J. J., Development of the B-D Blast-Closure Valve, Technical Note No.
N-546, U.S. Naval Civil Engineering Laboratory, Port Hueneme, CA, December 1963.
90.Bergman, S. and Staffors, B., Blast Tests on Rapid-Closing Anti-Blast Valves,
Royal Swedish Fortification Administration, Stockholm, Sweden, November 1963.
91.Breckenridge, T. A., Preliminary Development and Tests of a Blast- Closure Valve, Technical Note No. N-460, U.S. Naval Civil Engineering Laboratory, Port Hueneme, CA, September 192.
92.Chapler, R. S., Evaluation of Four Blast Closure Valves, Technical Report R 347,
DASA-13.154, U.S. Naval Civil Engineering Laboratory, Port Hueneme, CA,
January 1965 (Official Use Only).


<!-- batch 35 | page 80 -->

93.Cohen, E., Blast Vulnerability of Deep Underground Facilities as Affected by Access and Ventilation Openings, Ammann & Whitney, Consulting Engineers,New York, NY, Proceedings of the Second Protective Construction Symposium,R-341, Volume I, The RAND Corporation, Santa Monica, CA, 1959.94.Cohen, E. and Weissman, S., Blast Closure Systems, Ammann & Whitney,Consulting Engineers, New York, NY, Proceedings of the Symposium on Protective Structures for Civil Populations, Subcommittee on Protective Structures, Advisory Committee on Civil Defense, National Academy of Sciences and National Research Council, April 1965.
95.Hassman, M. and Cohen, E., Review of Blast Closure Systems, Ammann &
Whitney, Consulting Engineers, New York, NY, 29th Symposium on Shock,
Vibration and Associated Environments, Part Il, Bulletin No. 29, U.S. Naval Research Laboratory, Washington, D.C., July 1961, available from the Offce of Technical Services, Department of Commerce, Washington, D.C.96.Hellberg, E. N., Performance of the Swedish Rapid-Closing Anti-Blast Valve,
Technical Note No. 439, Task Y-F 008-10-11, U.S. Naval Civil Engineering Laboratory, Port Hueneme, CA, May 1962.
97.Jones, W.A., et al., A Simple Blast Valve, Suffield Technical Note No. 113,
Suffield Experimental Station, Ralston, Alberta, Canada, Defense Research Board, Department of National Defense, Canada, DRB Project No. D89-16-0109, February 1963.
98.Ort, F. G. and Mears, M. D., Development of the Closure, Protective Shelter,
Anti-Blast, 600 cfm, E19R1, Technical Report CWLR-2269, Chemical Warfare Laboratories, U.S. Army Chemical Center, Edgewood, MD, January 1959.99.Stephenson, J. M., Preliminary Tests of the Stephenson Valve, 2nd Report,
Technical Note No. N-619, U.S. Naval Civil Engineering Laboratory, Port Hueneme, CA, July 1964.
100.Stephenson, J. M., Test of German Sand-Type Filter, Technical Report R263,
U.S. Naval Civil Engineering Laboratory, Port Hueneme, CA, November 163.
Shock Isolation Systems 101.A Guide for the Design of Shock Isolation Systems for Underground Protective Structures, AFSWC TDR 62-64, Air Force Special Weapons Center, Kirtland AFB, NM, December 192.
102.Handbook of Mechanical Spring Design, Associated Spring Corporation, Bristol,
CT, 1964.
103.Study of Shock Isolation for Hardened Structures, Department of the Army,
Office of the Chief of Engineers, Washington, D.C., AD 639 303, June 196.

<!-- batch 35 | page 81 -->

104. Crawford, R. E. Higgins, C. J., and Bultmann, E.H., A Guide for the Design of Shock Isolation Systems for Ballistic Missile Defense Facilities, TR S-23, U.S.Army Construction Engineering Research Laboratory, Champaign, IL, August 1973.
105.Harris, C.M. and Crede, C.E., Shock and Vibration Handbook, McGraw-Hill Book Company, New York, NY, 191.
106.Hirsch, A.E., Man's Response to Shock Motions, David Taylor Model Basin Report 1797, Washington, D.C. AD 4 36809, January 1964.107.Platus, David L., et al., Investigation of Optimum Passive Shock Isolation Systems, AFWL-TR-72-148, Air Force Weapons Laboratory, Kirtland Air Force Base, NM, November 1972.
108.Saffell, H.R., Development of Standard Desiqn Specifications and Techniques for Shock Isolation Systems, Document No. SAF-37, Vol. I, U.S. Army Engineer Division, Huntsville, AL, August 1971.
109.Shigley, J.E., Mechanical Enqineering Design, McGraw-Hill Book Company, New York, NY, 1963.
110.Veletnor, A., Design Procedures for Shock Isolation System for Underground Protective Structures, RTD-TDR-63-3096, Vol. III, Air Force Weapons Laboratory, Kirtland Air Force Base, NM, January 1964.