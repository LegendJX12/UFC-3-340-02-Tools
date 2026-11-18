

<!-- batch 10 | page 1 -->

## PROBLEM 2A-12INTERIOR PRESSURE BUILDUP IN A STRUCTURE 

### Problem:Determine the interior pressure-time curve for a structure with an opening in one of its walls and subjected to an applied blast pressure. 

## Procedure:

Step 1.Determine the pressure-time history of the applied blast pressure P acting on the wall surrounding the opening in the structure as presented in Problem 2A-10. Also the area of the opening $A_{o}$ and the volume of the structure $V_{o}$ must be known.



Step 2.Divide the duration $t_{0}$  of the applied pressure into n equal intervals $\Re,$ each interval being approximately $t_{o}/10$ to $t_{o}/20$ ,and determine the pressures at the end of each interval.



Step 3.Compute the pressure differential $P–P_{i}$ where $P_{i}$ is the interior pressure.Obtain the leakage pressure coefficient $C_{L}$ for each $P–P_{i}$ from Figure 2-235

$(\pm)$ 



Step 4.Calculate $\delta\mathcal{P}_{i}$ from 

$$\delta\pmb{P}_{i}=\pmb{C}_{L}\frac{\pmb{A}_{o}}{V_{o}}\delta\pmb{t}$$

using the proper values for $C_{L}$ and δt.Add $\delta{\mathcal{P}}_{i}$ to $P_{i}$ for the interval being considered to obtain the new value of $P_{i}$ for the next interval.

Step 5.Repeat Steps 3 and 4 for each interval using the proper values of P and $P_{i}$ .. Plot curve of pressure buildup.



## Note:

When $P–P_{i}$ becomes negative, the value of $C_{L}$ must be taken as negative also.

<!-- batch 10 | page 2 -->

## EXAMPLE 2A-12 INTERIOR PRESSURE BUILDUP IN A STRUCTURE 

Required:Interior pressure-time curve for a structure with an opening in one of its walls and subjected to an applied blast pressure.

## Solution:

Step 1.The curve of the applied blast pressure P for the wall in question is shown in Figure 2A-24 (+). (Only the positive phase of the blast wave is considered in this example.)




<div style="text-align: center;"><html><body><table border="1"><tr><td>Area of opening</td><td>$A_{0}=3^{\circ}\times3^{\circ}=9\mathrm{~sq}\mathrm{ft}$</td></tr><tr><td>Volume of structure</td><td>$V_{o}=10^{\circ}\times10^{\circ}\times10^{\circ}$ $V_{o}=1,000\mathrm{c u f t}$</td></tr></table></body></html></div>


Step 2.$t_{0}=55\ ms$ 

Use..$n=10$ 」δt= 5.5 ms 

For the first interval,$P=3.5\mathrm{~ps}\mathrm{i}\mathrm{~at}t=0$ 

Step 3.$P_{i}=0$ for the first interval 

$$P-P_{i}=3.50-0=3.50\mathrm{psi}$$

(Figure 2-235 (+))

Step 4.

$$\delta P_{i}=C_{L}\frac{A_{o}}{V_{o}}\delta t $$

(Equation 2-31)

$$\delta P_{i}=8.75\left(9.0/1000\right)\left(5.5\right)=0.433\ \mathrm{psi}$$

new $P_{i}=0+0.433=0.433\ \mathrm{ps}i$ 

Step 5.The remainder of the analysis is presented in tabular form and the pressure buildup within the structure is plotted in Figure 2A-24 (+).

<!-- batch 10 | page 3 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>(ms) $\pmb{t}^{(1)}$</td><td>◼ (psi) $P$</td><td>■ (psi) $P_{i}$</td><td>(psi) $P-P_{i}$</td><td>■ (psi-ft/ms) $C_{L}$</td><td>(psi) $\pmb{\delta P}_{i}$</td></tr><tr><td>0.0</td><td>3.50</td><td>0.0</td><td>3.50</td><td>8.75</td><td>0.433</td></tr><tr><td>5.5</td><td>3.15</td><td>0.433</td><td>2.72</td><td>7.00</td><td>0.347</td></tr><tr><td>11.0</td><td>2.80</td><td>0.780</td><td>2.02</td><td>5.45</td><td>0.270</td></tr><tr><td>16.5</td><td>2.45</td><td>1.05</td><td>1.40</td><td>3.78</td><td>0.187</td></tr><tr><td>22.0</td><td>2.10</td><td>1.24</td><td>0.86</td><td>2.32</td><td>0.115</td></tr><tr><td>27.5</td><td>1.75</td><td>1.36</td><td>0.39</td><td>1.05</td><td>0.052</td></tr><tr><td>33.0</td><td>1.40</td><td>1.41</td><td>-0.01</td><td>-0.027</td><td>-0.0013</td></tr><tr><td>38.5</td><td>1.05</td><td>1.41</td><td>-0.36</td><td>-0.972</td><td>-0.048</td></tr><tr><td>44.0</td><td>0.70</td><td>1.36</td><td>-0.66</td><td>-1.78</td><td>-0.088</td></tr><tr><td>49.5</td><td>0.35</td><td>1.27</td><td>-0.92</td><td>-2.48</td><td>-0.123</td></tr><tr><td>55.0</td><td>0.0</td><td>1.14</td><td>-1.14</td><td>-3.50</td><td>-0.173</td></tr><tr><td>60.5</td><td>0.0</td><td>0.97</td><td>-0.97</td><td>-3.00</td><td>-0.148</td></tr><tr><td>66.0</td><td>0.0</td><td>0.82</td><td>-0.82</td><td>-2.50</td><td>-0.124</td></tr><tr><td>71.5</td><td>0.0</td><td>0.70</td><td>-0.70</td><td>-2.25</td><td>-0.111</td></tr><tr><td>77.0</td><td>0.0</td><td>0.59</td><td>-0.59</td><td>-2.00</td><td>-0.099</td></tr><tr><td>82.5</td><td>0.0</td><td>0.49</td><td>-0.49</td><td>-1.80</td><td>-0.089</td></tr><tr><td>88.0</td><td>0.0</td><td>0.40</td><td>-0.40</td><td>-1.60</td><td>-0.079</td></tr><tr><td>93.5</td><td>0.0</td><td>0.32</td><td>-0.32</td><td>-1.45</td><td>-0.071</td></tr><tr><td>99.0</td><td>0.0</td><td>0.25</td><td>-0.25</td><td>-1.30</td><td>-0.064</td></tr><tr><td>104.5</td><td>0.0</td><td>0.19</td><td>-0.19</td><td>-1.15</td><td>-0.056</td></tr><tr><td>110.0</td><td>0.0</td><td>0.13</td><td>-0.13</td><td>-1.0</td><td>-0.050</td></tr><tr><td>115.5</td><td>0.0</td><td>0.08</td><td>-0.08</td><td>-0.85</td><td>-0.042</td></tr><tr><td>121.0</td><td>0.0</td><td>0.04</td><td>-0.04</td><td>-0.05</td><td>-0.025</td></tr><tr><td>126.5</td><td>0.0</td><td>0.01</td><td>-0.01</td><td>-0.2</td><td>-0.01</td></tr><tr><td>132.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></tbody></table></body></html></div>


<div style="text-align: center;">(1) Maximum $P_{i}$ occurs between $t=27.5and t=33.0ms$ </div>


<!-- batch 10 | page 4 -->

<div style="text-align: center;">Figure 2A-24</div>


<div style="text-align: center;"><img src="../pages/batch 10/imgs/img_in_chart_box_212_297_972_1060.jpg" alt="Image" width="63%" /></div>


<!-- batch 10 | page 5 -->

# PROBLEM 2A-13 PRIMARY FRAGMENTS FROM CASED CYLINDRICAL  CHARGES 

Problem:Determine the average fragment weight for a primary fragment ejected from a uniform cylindrical steel casing; the total number of fragments, the design fragment weight and the number of fragments weighing more than the design fragment.



## Procedure:

Step 1.Establish design parameters:

a.type of explosive 

b.average casing thickness,$t_{c}$ 

C.average inside diameter of casing,$d_{i}$ 

d.total casing weight,$W_{c}$ 

e.confidence level,$C_{L}$ 

Step 2.Determine the value of the explosive constant B for the given type of explosive from Table 2-6 (+/+). With this value and the values of $t_{c}$ and $d_{i}$ from Step 1, calculate the fragment distribution $M_{A}$ from 

$$M_{A}=B t_{c}^{5/6}d_{i}^{1/3}\left[1+\left(t_{c}/d_{i}\right)\right]$$

(Equation 2-37)

Step 3.With the value of $M_{A}$ from Step 2, calculate the average weight of the fragments from 



$$\overline{{W_{f}}}=2{M_{A}}^{2}$$

Step 4.Calculate the total number of fragments using the value of $W_{c}$ from Step 1d and $M_{A}$ .from Step 2 and Equation 2-37.



$$N_{T}=8W_{C}/M_{A}^{2}$$

or:With the values of $d_{i}$ and $t_{c}$ from Step 1, enter Figure 2-241 (+) and determine $B^{2}N_{\tau}/W_{0}$ From this value, the value of B from Step 2 and $W_{c}$ from Step 1, find $N_{T}$ 



Step 5.Find the design fragment weight for the confidence level $C_{L}$ , given in Step 1, using the value of $M_{A}$ and 



$$W_{f}=M_{A}^{2}\ln^{2}(1-C_{L})\mathrm{for}C_{L}<0.9999$$

(Equation 2-42)

or Equation 2-43 if $C_{L}>0.9999$ 

<!-- batch 10 | page 6 -->

Step 6.Using the value of $W_{c}$ from Step 1,$M_{A}$ from Step 2 and $W_{f}$ from Step 5,determine the number of fragments which weigh more than the design fragment from 



$$N_{f}=\frac{8W_{c}e^{-\left[\left(W_{f}\right)^{1/2}/M_{A}\right]}}{M_{A}^{2}}$$

or:Calculate the number of fragments which weigh more than the design fragment using the confidence level of Step 1, the total number of fragments from Step 4 and Equation 2-244.



<!-- batch 10 | page 7 -->

## EXAMPLE 2A-13 PRIMARY FRAGMENTS FROM CASED CYLINDRICAL 

## CHARGES 

Required:The average fragment weight, the total number of fragments, the design fragment weight and the number of fragments weighing more than the design fragment.



## Solution:

Step 1.

Given:

a. type of explosive: Comp B 

b. average casing thickness:$t_{c}=0.50$ inch 

c. average inside diameter of casing:$d_{i}=12.0$ inches 

d. total casing weight:$W_{c}=65.0$ lbs 

e. confidence level:$C_{L}=0.95$ 



Step 2.For Comp B,$B=0.22$ 

$$\begin{array}{r l}{M_{A}}&{{}=B t_{c}^{5/6}d_{i}^{1/3}(1+t_{c}/d_{i})}\\ &{{}=0.22(0.5)^{5/6}(12)^{1/3}(1+0.5/12)=0.294.}\end{array}$$

Step 3.Average weight of fragments.

$$\overline{W_{f}}=2M_{A}^{2}=2\times(0.294)^{2}=0.17\mathrm{~o}z $$

Step 4.Total number of fragments.

$$N_{T}=8W_{c}/M_{A}^{2}=8\times65/0.294^{2}=6016\ fragments $$

or:

$$\frac{B^{2}N_{\tau}}{W_{c}}=0.28$$

$$N_{T}=0.28\times(65\times16)/0.22^{2}=6016\ fragments $$

Step 5.Design fragment weight.

$$W_{f}=M_{A}^{2}\ln^{2}(1-C_{L})=0.294^{2}\ln^{2}(1-0.95)=0.78\ \mathrm{~o}z $$

<!-- batch 10 | page 8 -->

Step 6.

Number of fragments weighing more than $W_{f}=0.78\;^{\circ}z$ 

$$N_{t}=\frac{8W_{c}e^{-\left[\left(W_{f}\right)^{1/2}/M_{A}\right]}}{M_{A}^{2}}=\frac{(8\times65)e^{-(0.78)^{1/2}/0.294}}{(0.294)^{2}}$$

<!-- batch 10 | page 9 -->

## PROBLEM 2A-14 PRIMARY FRAGMENT VELOCITY 

### Problem:Determine the initial velocity of a primary fragment and its striking velocity. 

## Procedure:

Step 1.Establish design parameters.

a. shape of charge 

b. dimensions of charge 

c. type and density of explosive 

d. type and density of casing 

e. distance from center of charge to impact location 

f. weight of fragment 

Step 2.Calculate the total weight of the explosive W and increase it 20%. Find the weight of the casing $W_{c}$ . Also calculate the ratio of the explosive weight to the casing weight $W/W_{o}$ ∴



Step 3.Determine the Gurney Energy Constant $(2E)^{1/2}$ for the explosive charge from Table 2-5 (+). With this value and the value of $W/W_{c}$ from Step 2,calculate the initial $v_{o}$ of the primary fragments from the equation chosen from Table 2-6$(\pm/\underline{{\pm}})$ 



or:Calculate the casing to charge weight ratio $W_{c}/W$ :With $W_{c}/W,$ ,find the initial velocity from Figure 2-237 (+) for proper shape.

Step 4.For the distance traveled by the fragment $R_{f},$ calculate the striking velocity $v_{s}$ using the initial velocity from Step 3, the weight of the fragment from Step 1g and 



$$\pmb{V}_{s}=\pmb{V}_{o}\pmb{\mathscr{E}}^{-.004R_{f}/W_{f}^{\prime}1/3}$$

(Equation 2-48)

or:With the fragment weight $W_{t}$ and striking distance $R_{f}$ from Step 1, enter Figure 2-243 (+) and find the ratio of the striking velocity to initial velocity.Multiply the ratio by the initial velocity $v_{o}$ from Step 3 to find the striking velocity $v_{s}$ .



<!-- batch 10 | page 10 -->

# EXAMPLE 2A-14 PRIMARY FRAGMENT VELOCITY 

Required:The initial velocity and striking velocity of a primary fragment.

Step 1.Given:

a. spherical charge 

b. inner diameter of charge:$d_{i}=6$ inches 

average casing thickness:$t_{c}=0.25\ inchees$ 

C. type of explosive TNT 

$$\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}$$

d. mild steel casing 

$$\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}\mathrm{d}$$

e. striking distance $R_{f}=35\ ft$ 

f. weight of fragment,$W_{f}=2\;0z$ 

Step 2.

a. weight of the explosive 

$$W=4/3\pi(6/2)^3\times0.0558=6.31\mathrm{~lb}$$

b. Increase weight of explosive 20 percent 

$$W=1.20\times6.31=7.57lb $$

c. Weight of casing 

$$W_{c}=4/3\ \pi\left(3.25^{3}-3^{3}\right)\times0.283=8.69\ lb $$

d. Explosive weight to casing weight ratio.

$$W/W_{c}=7.57/8.69=0.871$$

Step 3.For TNT,$(2E^{\prime})^{1/2}=8000$ 

(Table 2-5 (+))

Initial velocity from Table 2-6$(\pm/\pm)$ 

<!-- batch 10 | page 11 -->

UFC 3-340-025 December 2008Change 2, 1 September 2014

$$v_{o}=\left(2E^{\prime}\right)^{1/2}\left[\frac{W/W_{c}}{1+\left(3W/5W_{c}\right)}\right]^{1/2}$$

$$\begin{aligned}for:\quad&\quad\mathsf{W_c}\mathsf{N}=8.69/7.57=1.15\\&\quad from Figure2-237(+)\\&\quad v_o/(2E')^{1/2}=0.76\\&\quad v_o=0.76\times8000=6080ft/sec\end{aligned}$$

Step 4.Striking velocity 

$$\boldsymbol{v}_{s}=\boldsymbol{v}_{o}\boldsymbol{e}^{-0.004R_{t}/W_{t}^{1/3}}=6080\boldsymbol{e}^{-0.004\left[35/\left(2^{1/3}\right)\right]}$$

(Equation 2-48)

$$v_{s}=5440\mathrm{f t/s e c}$$

or:from Figure 2-243 (+) for $W_{f}=2$ Oz and $R_{f}=35\:\mathrm{f t}$ 

$$v_{s}/v_{o}=0.895$$

$$v_{s}=0.895\times6080=5440ft/sec $$

<!-- batch 10 | page 12 -->

# PROBLEM 2A-15 UNCONSTRAINED SECONDARY FRAGMENTS "CLOSE" TO A  CHARGE 

## Problem:Determine the velocity of an unconstrained object close to an explosive charge and its maximum range

## Procedure:

Step 1.Establish design parameters 

a.weight W and shape of TNT equivalent explosive 

b.radius of explosive $R_{e}$ 

C.shape, dimensions and weight of target 

d.distance from the center of the explosive charge to the surface of the target, R 



e.orientation of target with respect to the explosive charge 

f.mass density of air.$\rho_{0}$ 

Step 2.

2.Calculate the ratio of standoff distance to radius of the explosive $R/R_{e}$ using the values from Step 1.



From Figure 2-249 (+), determine target shape factor, B.

Step 4.

a.If $R/R_{e}$ is less than or equal to 10 for cylindrical charges, or less than equal to 5.0 for spherical charges, determine the specific acquired impulse either from Figure 2-250 (+) or Equations 2-60, or 2-61.

b.If $10<R/R_{\mathrm{e}}\leq20$ for a cylindrical charge, or $5\leq R/R_{\mathrm{e}}\leq20$ for a spherical charge, calculate the scaled standoff distance $Z_{A}=$ $\dot{R}/W^{1/3}$ . With that value of $Z_{A}$ , obtain the normal reflected impulse from Figure 2-7 (+). The normal reflected impulse is then used as the specific acquired impulse.



Calculate the mean presented area A of the target and the mass M using the values of Step 1.



Step 6.With the area and mass from Step 4, the target shape factor β from Step 2and the impulse from Step 3, calculate the velocity from 

$$v_{o}=\frac{1000A\beta i}{12M}$$

(Equation 2-59)

<!-- batch 10 | page 13 -->

Step 7.Determine the drag coefficient $C_{D}$ from Table 2-8 (+). Using that value of $C_{D},$ , the area and mass of the target from Step 5, the velocity from Step 6and the mass density of air from Step 1f,

evaluate the term:$12\rho_{o}C_{D}A_{D}v_{o}{}^{2}/M g$ 

Step 8.With the term calculated in Step 7, enter Figure 2-252 (+) and read the value of 12.$\rho_{o}C_{D}A_{D}R/M$ from which the range R is calculated.

<!-- batch 10 | page 14 -->

# EXAMPLE 2A-15UNCONSTRAINED SECONDARY FRAGMENTS "CLOSE" TO A  CHARGE 

Required:The velocity and maximum range of a steel tool holder resting on a lathe when a charge being held by the lathe explodes.

Solution:

Step 1.Given:

a.spherical charge of TNT 

$$W=15\mathrm{l b s}$$

b.radius of explosive:$R_{\mathrm{e}}=0.33\mathrm{f t}$ 

C.cylindrical target;$\mathrm{l e n g t h}=8.0\mathrm{i n}$ 

$$R_{t}=1.0\ in=0.083\ ft $$

$$W_{t}=7.13\ \mathrm{lb}$$

d.standoff distance:$R=1.0\mathrm{f t}$ 

e.tool holder is resting so that its longitudinal axis is perpendicular to the radial line from the charge 

f.mass density of air:$\rho_{o}=0.115\mathrm{~l b}-\mathrm{m s}^{2}/\mathrm{i n}^{4}$ 

Step 2.Ratio of standoff distance to radius of explosive:

$$R/R_{\mathrm{e}}=1.0/0.33=3.03$$

Step 3.Target shape factor.

$\beta=\pi/4$ from Figure 2-249 (+)

Step 4.Determine specific acquired impulse 

a.

$$\frac{i}{\beta R_{eff}}\left[\frac{R_{e}}{R_{t}}\right]^{0.158}=8000\frac{\mathrm{psi-ms}}{\mathrm{ft}}$$

(Figure 2-250 (+))

b.

$$R_{\mathrm{e f f}}=R_{\mathrm{e}}=0.33\mathrm{f t}$$

(Equation 2-61)

C.

$$j=\pi/4\left(0.33ft\right)\left(0.083/0.33\right)^{0.158}\times8000psi-ms/ft $$

$$i=1667~\mathrm{p s i-m s}$$

<!-- batch 10 | page 15 -->

Step 5.Calculate area and mass of target.

a.Mean presented area 

$$A=2.0in\times8.0in=16in^2$$

b. Mass 

$$M=\frac{W_{t}}{g}=\frac{7.13lb}{32.2\times12\times10^{-6}in/ms^{2}}=18.450\frac{lb-ms^{2}}{in}$$

Step 6.Find the velocity.

$$v_{o}=\frac{1000A\beta i}{12M}=\frac{1000\times16\times(\pi/4)\times1667}{12\times18450}$$

$$v_{o}=95\;\mathrm{f t/s e c}$$

Step 7.Evaluate the term $12\rho_{0}C_{D}A_{D}{v_{o}}^{2}/M g$ 

a.

$$C_{D}=1.2$$

b.

$$\frac{12\rho_{o}C_{D}A_{D}V_{o}^{2}}{Mg}=\frac{12\times0.115\times1.2\times16\times(95)^{2}}{18450\times32.2}=0.40$$

Step 8.Calculate the range.

a.

$$\frac{12\rho_{o}C_{D}A_{D}R}{M}=0.33$$

b.

$$\begin{aligned}&R=0.33M/(12\rho_{o}C_{D}A_{D})\\ &\quad=0.33\ (18450)/[12\ (0.115)\ 1.2\ (16)]=230\ ft\\ \end{aligned}$$

<!-- batch 10 | page 16 -->

# PROBLEM: 2A-16 UNCONSTRAINED SECONDARY FRAGMENTS "FAR" FROM A  CHARGE 

### Problem:Determine the velocity of an unconstrained object "far" from an explosive charge. 

## Procedure:

Step 1.Establish design parameters:

a. weight W of TNT equivalent explosive 

b. shape, dimensions and weight of target 

c. distance from the center of explosive charge to surface of the target 

d.orientation and location of target with respect to the explosive charge 



e. velocity of sound in air,$a_{o}$ ,

f. atmospheric pressure,.$p_{o}$ 

Step 2.Calculate the scaled standoff distance from:

$$Z_{A}=R_{A}/W^{1/3}$$

From Figure 2-7 (+) and the scaled distance find the peak incident overpressure and the incident specific impulse.

Step 3.Determine the drag coefficient $C_{D}$ from Table 2-8 (+) based on the shape and orientation of target (Step 1).



Step 4.Calculate the mass of the target. Determine the distance from the front of the target to the location of its largest cross-sectional area, X. Also,determine the minimum transverse distance of the mean presented area,H, and the presented area.



Step 5.Determine the constant K, which is equal to 4 if the object is on the ground or reflecting surface. If the target is in the air, K is equal to 2.

Step 6.With the peak incident overpressure $P_{s o}$ from Step 2 and the atmospheric pressure $p_{o}$ from Step 1f, find $P_{s o}/p_{o}$ 



Step 7.Evaluate the term $12C_{D}i_{s}a_{o}/10^{3}[P_{s o}(K H+X)]$ using $j_{s}$ and $P_{s o}$ from Step 2,$C_{D}$ from Step 3,$a_{0}$ from Step 1e, K from Step 5 and H and X from Step 4.Step 8.With two terms calculated in Steps 6 and 7 enter Figure 2-248$(+)$ and read $144v_{o}M a_{o}/[10^{6}P_{o}A(K H+X)]$ from which the velocity is calculated.

<!-- batch 10 | page 17 -->

# EXAMPLE 2A-16 UNCONSTRAINED SECONDARY FRAGMENTS "FAR" FROM  CHARGE 

Required:The initial velocity of a steel tool holder resting on a nearby table, when a charge explodes.



Solution:

Step 1.Given:

a. weight of explosive:$W=15$ Ibs of TNT 

b. cylindrical target: length = 8.0 in 

$$R_{t}=1.0\ in\ W_{t}=7.13\ lb $$

C. standoff distance:$R=10\mathrm{f t}$ 

d.tool holder is resting on a table so that its longitudinal axis is perpendicular to the radial line from the charge 

e. velocity of sound in air:$a_{o}=1100$ ft/sec 

f. atmospheric pressure:$p_{o}=14.7$ psi 

Step 2.

Find the peak incident overpressure and the incident specific impulse.

a. Scaled distance 

$$Z_{A}=R/W^{1/3}=10/(15)^{1/3}=4.05\mathrm{f t/l b^{1/3}}$$

b. Peak incident overpressure.

$$P_{s o}=46~\mathrm{p s i}$$

c. Incident specific impulse.

$$\begin{aligned}&j_{s}/W^{1/3}=12\ psi-ms/lb^{1/3}\\ &j_{s}=12\ (15)^{1/3}=29.6\ psi-ms\\ \end{aligned}$$

Step 3.Drag coefficient.

$C_{D}=1.2$ (from Table 2-8 (+) for cylinder loaded perpendicular to axis.)

<!-- batch 10 | page 18 -->

Step 4.

a. Mass of target.

$$M=\frac{W_{t}}{g}=\frac{7.131b}{32.2\times12\times10^{-6}in/ms^{2}}=18.450\frac{lb-ms^{2}}{in}$$

b. Location of largest cross-section.

$$X=1\quad(\mathrm{r a d i u s~o f~o b j e c t~i n~t h i s~c a s e~-s e e~F i g u r e~}2\mathrm{A}\mathrm{-}21(\pm/\pm/\pm/\pm))$$

c. Transverse distance of presented ara.

H = 2.0 in (diameter of object in this case - see Figure 2A-25 (+))

d. Mean presented area.

$$A=2\times8=16in^2$$

Step 5.Reflection constant.

Target is resting on table which is a reflecting surface so:

$$K=4$$

Step 6.Evaluate $\mathsf{P}_{\mathsf{s o}}/\mathsf{p}_{\circ}$ 

$$P_{s o}/p_{o}=46/14.7=3.13$$

Step 7.$\mathrm{\sf Evaluate~}12C_{D}i_{s}a_{o}/[10^{3}P_{so}\left(KH+X\right)]$ 

$$\frac{12C_{D}i_{s}a_{o}}{10^{3}P_{so}(KH+X)}=\frac{12\times1.2\times29.6\times1100}{10^{3}\times46\times(2\times4+1)}=1.13$$

Step 8.Calculate the velocity.

$$\frac{144v_{o}Ma_{o}}{10^{6}p_{o}A(KH+X)}=7.5$$

(Figure 2-248 (+))

$v_{o}=5.43$ ft/sec 

<!-- batch 10 | page 19 -->

<div style="text-align: center;">Figure 2A-25</div>


<div style="text-align: center;"><img src="../pages/batch 10/imgs/img_in_image_box_359_321_782_886.jpg" alt="Image" width="35%" /></div>


<!-- batch 10 | page 20 -->

## PROBLEM 2A-17 CONSTRAINED SECONDARY FRAGMENTS 

### Problem:Determine the velocity of a constrained object close to an exploding charge. 

## Procedure:

Step 1.Establish design parameters:

a. fragment material.

b. dimensions of object.

c. boundary condition, cantilever or fixed-fixed.

d. specific impulse imparted to object.

Step 2.Determine the fragment toughness T from Table 2-9 (+) and the fragment mass density pf.



Step 3.Calculate the loaded area of the object.

Step 4.Evaluate the term ib $(2L/b)^{0.3}/[A(\rho_{r}T)^{0.5}]$ ,using the specific impulse and object dimensions from Step 1, the fragment density and toughness from Step 2 and the loaded area from Step 3. With this term, enter Figure 2-251(+) and read the value of 12V/1000$\dot{(\rho_{f}/T)}^{0.5}$ from which the velocity is calculated.



or:Using the specific impulse and object dimensions from Step 1, the fragment density and toughness from Step 2, and the loaded area from Step 3. Calculate the velocity of the object from Equation 2-66.

<!-- batch 10 | page 21 -->

## EXAMPLE 2A-17 CONSTRAINED SECONDARY FRAGMENTS 

Required:The velocity of a cylindrical tool holder after it breaks free of its moorings.Solution:

Step 1.Given:

a. fragment material; A36 steel 

b. dimensions of object:$b=2.0$ inches,$L=8.0$ inches 

c. boundary conditions; cantilever 

d. specific impulse:$i=1667$ psi-ms (see Step 4 of Example 2A-15).

Step 2.

a. Fragment toughness.

$$T=12.000in-lb/in^3$$

b. Mass density of steel.

$$\rho_{r}=\frac{490lb/ft^{3}\left(ft^{3}/1728\mathrm{in}^{3}\right)}{32.2ft/s^{2}\left(12\mathrm{in}/ft\right)\left(s^{2}/10^{8}\mathrm{ms}^{2}\right)}=734\frac{lb-ms^{2}}{\mathrm{in}^{4}}$$

Step 3.Loaded area.

$$A=\pi r^{2}=\pi(1.0)^{2}=3.14in^{2}$$

Step 4.Calculate the velocity.

$$\frac{ib}{A(\rho_{\mathrm{f}}T)^{0.5}}\left[\frac{2L}{b}\right]^{0.3}=\frac{1667\times2.0}{3.14\times(734\times12,000)^{0.5}}\left[\frac{2\times8}{2}\right]^{0.3}=0.668$$

from Figure 2-251 (+)

$$12/1000\left[\rho_{f}/T\right]^{1/2}V=0.025$$

so 

$$V=\frac{1000}{12}\left[\frac{T}{\rho_f}\right]^{1/2}0.025=\frac{1000}{12}\left[\frac{12,000}{734}\right]^{1/2}0.025=8.4\mathrm{~fps}$$

<!-- batch 10 | page 22 -->

or from Equation 2-66

$$\begin{aligned}V=&\frac{1000}{12}\left[\frac{T}{\rho_{r}}\right]^{1/2}\left[-.2369+0.393\left[\frac{ib}{\left(\rho_{r}T\right)^{1/2}A}\right]\frac{2L}{b}\right]^{0.3}\\ =&\frac{1000}{12}\left[\frac{12,000}{734}\right]^{1/2}\left(-.2369+0.3931\times0.668\right)\\ =&8.6\mathrm{fps}\end{aligned}$$

<!-- batch 10 | page 23 -->

# PROBLEM 2A-18 GROUND SHOCK LOAD 

### Problem:Determine the air blast and direct induced ground shock parameters.Procedure:

Air Blast-Induced Ground Shock 

Step 1.Determine the charge weight, ground distance R, height of burst $H_{\tt c},$ if any,and structure dimensions.



Step 2.Apply a 20% safety factor to the charge weight.

Step 3.Calculate the scaled distance Z.

Read: From Figure 2-15 (+)

a. Peak positive incident pressure $P_{s o}$ 

b.Scaled unit positive incident impulse $j_{s}/W^{1/3}$ . Multiply scaled value by $W^{1/3}$ to obtain absolute value.



c. Shock front velocity U.

Step 4.Determine the maximum vertical ground motions.

a. Calculate maximum vertical velocity.

$$V_{v}=\frac{P_{s o}}{\rho C_{p}}$$

where:

ρ = Mass density of soil 

Cp = Compression wave seismic velocity in the soil (Table 2-11 (+))

b. Calculate maximum vertical displacement 

$$\dot{D}_{v}=\frac{\dot{I}_{s}}{1{,}000\rho C_{p}}$$

c. Calculate maximum vertical acceleration of the ground surface.

$$A_{v}=\frac{100P_{s o}}{\rho C_{p}g}$$

<!-- batch 10 | page 24 -->

where:

g= Gravitational constant equal to 32.2 ft/sec2

Step 5.Determine the maximum horizontal ground motions parameters.

a. Check $C_{P}/(12000U)>.707$ 

b. Calculate maximum horizontal velocity.

$$V_{H}=V_{V}\tan{[\sin^{-1}{(C_{p}/(12,000U))}]}$$

c. Calculate maximum horizontal displacement.

$$D_{H}=D_{V}\tan{[\sin^{-1}{(C_{p}/(12,000U))}]}$$

d. Calculate maximum horizontal acceleration.

$$A_{H}=A_{V}\tan\left[\sin^{-1}\left(C_{p}/(12,000U)\right)\right]$$

Step 6.Determine arrival time $t_{A}$ and duration $t_{0};$ ,

a. Read from Figure 2-15 (+)

$t_{A}/W^{1/3}$ scaled time of arrival of blast wave and,

$t_{o}/W^{1/3}$ scaled duration of positive phase.

b. Multiply scaled value by $W^{1/3}$ to obtain absolute value.

Direct-Induced Ground Shock 

Step 7.Determine the maximum vertical ground motions.

a. Calculate maximum vertical displacement.

$$D_{V}=\frac{0.025{R_{G}}^{1/3}W^{1/3}}{{Z_{G}}^{1/3}}$$

(Equation 2-80, rock media)

or 

$$D_{v}=\frac{0.017{R_{G}}^{1/3}W^{1/3}}{Z_{G}^{2.3}}\quad(\text{Equation2-83,dry or saturated solid})$$

b.Calculate the maximum vertical velocity.

$$V_{V}=150/{Z_{G}}^{1.5}$$

c. Calculate the maximum vertical acceleration.

$$A_{V}=10,000/W^{1/3}{Z_{G}}^{2}$$

<!-- batch 10 | page 25 -->

## Step 8

Determine the maximum horizontal ground motion parameters.

a. Calculate the maximum horizontal displacement.

$$D_{H}=0.5~D_{V}$$

(Equation 2-82, rock media)

or 

$$D_{H}=D_{V}$$

(Equation 2-84, dry or saturated soill)

b. Calculate the maximum horizontal velocity.

$$V_{H}=V_{V}$$

(Equation 2-86, all ground media)

c. Calculate the maximum horizontal acceleration.

$$A_{H}=0.5A_{V}$$

(Equation 2-88, dry soil)

$$A_{H}=A_{V}$$

(Equation 2-89, wet soil or rock media)

Step 9.Determine arrival time $t_{A G}\colon$ 

$$t_{A G}=12000R_{G}/C_{D}$$

(Equation 2-92)

<!-- batch 10 | page 26 -->

## EXAMPLE 2A-18GROUND SHOCK LOADS 

Required:Maximum acceleration, velocity, and displacement at a point 155 ft away from a surface burst of 5,000 Ibs. Also required are: times of arrival and duration of air-blast induced ground shock.



## Solution:

Air blast-induced ground shock.

Step 1.$Given:��\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ C $Given:��\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ 

Step 2.

$$W=1.2(5,000)=6,000lbs $$

Step 3.Calculate the scaled distance Z.

$$Z=\frac{R}{W^{1/3}}=\frac{155}{(6.000)^{1/3}}=8.53\pi/1b^{1/3}$$

Read from Figure 2-15 (+).

a.$P_{s o}=13\mathrm{p s i}$ 

b.

$$\frac{i_{s}}{W^{1/3}}=9p s i\cdot m s/b^{1/3}$$

$$j_{s}=9\times W^{1/3}=9\times(6,000)^{1/3}=163.54\times\mathrm{ps}$$

C.$U=1.5f t/ms$ 

Step 4.

Determine the maximum vertical ground motion.

a.

$$V_{v}=\frac{P_{s o}}{\rho C_{p}}$$

$$V_{v}=\frac{13}{1.65\times10^{-4}\times70.000}=1.125\mathrm{~in}/\mathrm{sec}$$

b.

$$\pmb{D}_{v}=\frac{\dot{I}_{s}}{1{,}000\rho C_{p}}$$

$$D_{v}=\frac{163.5}{1.000(1.65\times10^{-4})/70.000}=0.0142\mathrm{~in}$$

<!-- batch 10 | page 27 -->

C.

$$A_{v}=\frac{100P_{s o}}{\rho C_{p}g}$$

$$A_{v}=\frac{100\times12.8}{\left(1.65\times10^{-4}\right)/70,000\times32.2}=3.44g $$

Step 5.Determine the maximum horizontal ground motion.

a. Check $C_{p}/(12000U)>0.707$ 

$$70,000/(12,000\times1.5)=3.89>0.707$$

b.

$$V_{H}=V_{V}=1.125\mathrm{i n/s e c}$$

C.

$$D_{H}=D_{V}=0.0142\ in $$

d.$A_{H}=A_{V}=3.44\mathrm{g}$ 

Step 6.Arrival time $t_{A}$ 

$$\begin{aligned}&a.\ \mathsf{R e a d}\;\mathsf{f r o m}\;\mathsf{F i g u r e}\;2-15\;\underline{(+)}.\\&\quad\;t_{A}/W^{1/3}=3.35\;\mathsf{m s}/\mathsf{I b}^{1/3}\\&\quad\;t_{o}/W^{1/3}=2.35\;\mathsf{m s}/\mathsf{I b}^{1/3}\\&\quad\;\mathsf{t}_{A}=3.35\;\mathsf{x}\;\mathsf{W}^{1/3}=3.35\;(6,000)^{1/3}\\&\quad\;t_{A}=60.90\;\mathsf{m s}\\&\quad\;t_{o}=2.35\;\mathsf{x}\;W^{1/3}=2.35\;\mathsf{x}\;(6,000)^{1/3}\\&\quad\;t_{o}=42.70\;\mathsf{m s}\end{aligned}$$

Direct-induced ground shock.

Step 7.Maximum vertical ground motions.

a.

b.

$$\begin{aligned}&D_{v}=\frac{0.17{R_{G}}^{1/3}W^{1/3}}{{Z_{G}}^{2.3}}\\ &=\frac{0.17\left(155\right)^{1/3}\left(6.000\right)^{1/3}}{\left(8.53\right)^{2.3}}=0.1198\mathrm{~in}\\ &V_{V}=150/{Z_{G}}^{1.5}\\ &V_{V}=150/8.53^{1.5}=6.020\mathrm{~in}/\mathrm{sec}\\ \end{aligned}$$

<!-- batch 10 | page 28 -->

UFC 3-340-025 December 2008Change 2,1 September 2014

C.

$$\begin{aligned}&A_{V}=10,000/W^{1/3}Z_{G}^{2}\\&A_{V}=10,000/[(6,000)^{1/3}(8.53)^{2}]=7.56g\\ \end{aligned}$$

Step 8.Horizontal ground motions.

$$\begin{aligned}&a.\quad&D_{H}&=D_{V}\\&&D_{H}&=0.1198\quad&in\\&b.\quad&V_{H}&=V_{V}\\&&V_{H}&=6.020\quad&in/sec\\&c.\quad&A_{H}&=0.5\quad&A_{V}\\&&A_{H}&=0.5\quad&(7.56)\\&&A_{H}&=3.78\quad&g\end{aligned} ;$$

Step 9.Arrival time $t_{A G}$ 

$$t_{AG}=12,000\ R_{G}/C_{p}=(12,000\times155)/70,000$$

$$t_{AG}=26.6ms $$

<!-- batch 10 | page 29 -->

## PROBLEM 2A-19 STRUCTURE MOTION DUE TO AIR SHOCK 

## Problem:Determine the maximum horizontal acceleration, displacement and velocity of an above ground structure subjected to air shock

## Procedure:

Step 1.Determine external loadings acting on the roof, front and rear walls according to the procedure outlined in Problem 2A-10.

Step 2.Construct the horizontal force-time load curve by combining the front and rear wall loadings from Step 1 applied over the area of front and rear walls. Use times of arrival to phase these two loads.

Step 3.Calculate the dead weight and mass of the structure.

Step 4.Construct the downward force-time curve by adding the weight of the structure and total roof load. The roof load is the pressure time loading from Step 1 applied over the total area of the roof.

Step 5.Determine the coefficient of friction between soil and the structure from Table 2-12 (+).



Step 6.Determine maximum horizontal acceleration, displacement and velocity using the acceleration impulse extrapolation method outlined in Chapter 3,Section 3-19.2.1.2 of this manual. The resisting force at each time interval is equal to the value of downward force curve of Step 4 multiplied by the coefficient of friction determined in Step 5. The resisting force is assumed to be effective when the total horizontal movement is equal to or larger than 1/4 inch as mentioned in Section 2-22.2.



<!-- batch 10 | page 30 -->

## EXAMPLE 2A-19 STRUCTURE MOTION DUE TO AIR SHOCK 

Required:Maximum horizontal acceleration, velocity and displacement of the square structure shown in Figure 2A-9 (+) from Problem 2A-10 for a surface burst of 5,000 lbs at a distance from the front wall of 155 ft. Assume a coarse and compact soil. Roof, floor slab and side walls are 1 foot thick reinforced concrete slabs and assume a 50 psf of internal dead load for the structure.Step 1.External loadings on the structure are determined according to the procedure in Example 2A-10. See Figure 2A-10 (+), Figure 2A-12 (+) and Figure 2A-13 (+). The arrival time (tA) for these loads are tabulated in Step 3d of Example 2A-10.



$$\begin{aligned}&t_{Af}\left(\mathrm{f}\mathrm{r}\mathrm{o}\mathrm{n}\mathrm{t}\mathrm{w}\mathrm{a}\mathrm{l}\right)=60.9\mathrm{~m}\mathrm{s}\\ &t_{Ab}\left(\mathrm{r}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{w}\mathrm{a}\mathrm{l}\right)=83.6\mathrm{~m}\mathrm{s}\\ \end{aligned}$$

Step 2.

a. Calculate area of front and rear walls.

$$\mathrm{A}\mathrm{r}\mathrm{e}\mathrm{a}\left(\mathrm{f}\mathrm{r}\mathrm{o}\mathrm{n}\mathrm{d}\mathrm{r}\mathrm{e}\mathrm{a}\right)=30\times12\times\left(12\right)^{2}=51840\mathrm{~in}^{2}$$

b.Calculate the time difference between the rear and front walls from Step 1.



$$\delta t=t_{Ab}-t_{Af}=83.6-60.9=22.7ms $$

C.Construct the horizontal force-time load curve by multiplying the values of the front and rear wall curves from Step 1 by the area from Step 2a. Rear wall load starts at time equal to .$\delta t=22.7$ from Step 2b. See Figure 2A-26 (+).



<!-- batch 10 | page 31 -->

<div style="text-align: center;"><img src="../pages/batch 10/imgs/img_in_chart_box_186_305_1002_1076.jpg" alt="Image" width="68%" /></div>


Step 3.

a.Calculate dead weight of structure $\mathsf{W_{d}}$ . Assume concrete weight is 150 psf.



$$W_{d}=150\left[4\left(30-1\right)\left(12-1\right)+2\left(30\right)^{2}\right]+50\left(30-2\right)^{2}=500,600\ \mathrm{Ibs}$$

b. Calculate total mass.

$$m=\frac{W_{d}}{g}=\frac{500,600(1000)^{2}}{32.2\times12}=1295.55\times10^{6}\frac{lb-ms^{2}}{in}$$

<!-- batch 10 | page 32 -->

Step 4.

a. Calculate area of the roof.

$$\mathrm{Area}(\mathrm{roof})=30^{2}\times(12)^{2}=129,600\mathrm{in^{2}}$$

b.Construct the downward force-time curve by multiplying the values of the roof curve from Step 1 by the roof area from Step 4a, and adding the dead weight of structure $W_{d}=500,600$ Ibs from Step 3a.(If the resulting value is negative, assume zero). See Figure 2A-27(+) below.



<div style="text-align: center;">Figure 2A-27</div>


<div style="text-align: center;"><img src="../pages/batch 10/imgs/img_in_chart_box_189_600_998_1363.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">Step 5.Coefficient of friction μ from Table 2-12 (+) for coarse and compact soil. $\mu=0.60$  </div>


<!-- batch 10 | page 33 -->

Using the acceleration impulse extrapolation method from Chapter 3 of this manual determine maximum horizontal acceleration, displacement and velocity of the structure due to load curve (P) from Step 2c. Resisting force R is the friction force produced due to the downward load curve F from Step 4b after an initial lateral translation of 1/4 inch. Use two ms time intervals for extrapolation. The following are the equations used in the extrapolation shown in Table 2A-3 (+)



$$\begin{aligned}&P_{n}-R_{n}=m a_{n}\\&R_{n}=\mu F_{n}\\&X_{n+1}=2X_{u}-X_{n-1}+a_{n}(\delta t)^{2}\\&V_{n}=V_{n-1}+a_{n}(\delta t)\\ \end{aligned}$$

where 

Pn = Load at time of step n (Stp 2c)

Rn = Resisting Friction Force at time step n 

m = Mass (Step 3b)

an = Acceleration at time step n 

 = Friction coefficient (Step 5)

Fn = Downward force at time step n (Step 4b)

X = Deflection at time step n 

$$V_{n}=\operatorname{V e l o c i t y}\operatorname{a t}\operatorname{t i m e}\operatorname{s t e p}n $$

The maximum motions from Table 2A-3 (+) are:

$$\begin{aligned}&a_{max}=0.00122in/ms^2<<101.67ft/sec^2<<3.16g's\\ &V_{max}=0.01231in/ms<<1.026ft/sec\\ &D_{max}=0.355in\\ \end{aligned}$$

<!-- batch 10 | page 34 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>n</td><td>t</td><td>Pn lbs</td><td>Rn lbs</td><td>$P_{n-}Rn$ lbs</td><td>an = (Pn-Rn)m in/ms²</td><td>a_n(δt)2 in</td><td>2Xn in</td><td>$X_n-1$ in</td><td>$X_{n}+$ in</td><td>anδt in/ms</td><td>Vn-1 in/ms</td><td>$Vn in/ms</td></tr><tr><td>ms</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>0</td><td>1,781,208</td><td>0</td><td>1,781,208</td><td>(0.00138)/2</td><td>(0.00550)/2</td><td>0</td><td>0</td><td>0.00275</td><td>(0.00275)/2</td><td>0</td><td>0.00138</td></tr><tr><td>1</td><td>2</td><td>1,582,190</td><td>0</td><td>1,582,190</td><td>0.00122</td><td>0.00489</td><td>0.00550</td><td>0</td><td>0.01038</td><td>0.00244</td><td>0.00138</td><td>0.00382</td></tr><tr><td>2</td><td>4</td><td>1,383,173</td><td>0</td><td>1,383,173</td><td>0.00107</td><td>0.00427</td><td>0.02077</td><td>0.00275</td><td>0.02229</td><td>0.00214</td><td>0.00382</td><td>0.00596</td></tr><tr><td>3</td><td>6</td><td>1,184,155</td><td>0</td><td>1,184,155</td><td>0.00091</td><td>0.00366</td><td>0.04458</td><td>0.01038</td><td>0.03786</td><td>0.00182</td><td>0.00596</td><td>0.00778</td></tr><tr><td>4</td><td>8</td><td>985,137</td><td>0</td><td>985,137</td><td>0.00076</td><td>0.00304</td><td>0.07571</td><td>0.02229</td><td>0.05646</td><td>0.00152</td><td>0.00778</td><td>0.00930</td></tr><tr><td>5</td><td>10</td><td>786,120</td><td>0</td><td>786,120</td><td>0.00061</td><td>0.00243</td><td>0.11292</td><td>0.03786</td><td>0.07749</td><td>0.00122</td><td>0.00930</td><td>0.01052</td></tr><tr><td>6</td><td>12</td><td>587,102</td><td>0</td><td>587,102</td><td>0.00045</td><td>0.00181</td><td>0.15497</td><td>0.05646</td><td>0.10032</td><td>0.00090</td><td>0.01052</td><td>0.01142</td></tr><tr><td>7</td><td>14</td><td>388,084</td><td>0</td><td>388,084</td><td>0.00030</td><td>0.00120</td><td>0.20064</td><td>0.07749</td><td>0.12435</td><td>0.00060</td><td>0.01142</td><td>0.01202</td></tr><tr><td>8</td><td>16</td><td>189,067</td><td>0</td><td>189,067</td><td>0.00015</td><td>0.00058</td><td>0.24870</td><td>0.10032</td><td>0.14896</td><td>0.00029</td><td>0.01202</td><td>0.01231</td></tr><tr><td>9</td><td>18</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.29793</td><td>0.12435</td><td>0.17358</td><td>0</td><td>0.01231</td><td>0.01231</td></tr><tr><td>10</td><td>20</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.34716</td><td>0.14896</td><td>0.19820</td><td>0</td><td>0.01231</td><td>0.01231</td></tr><tr><td>11</td><td>22</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.39640</td><td>0.17358</td><td>0.22282</td><td>0</td><td>0.01231</td><td>0.01231</td></tr><tr><td>12</td><td>24</td><td>-50,013</td><td>0</td><td>-50,013</td><td>-0.00004</td><td>-0.00015</td><td>0.44564</td><td>0.19820</td><td>0.24728</td><td>-0.00008</td><td>0.01231</td><td>0.01223</td></tr><tr><td>13</td><td>26</td><td>-126,956</td><td>0</td><td>-126,956</td><td>-0.00010</td><td>-0.00039</td><td>0.49456</td><td>0.22282</td><td>0.27135</td><td>-0.00020</td><td>0.01223</td><td>0.01203</td></tr><tr><td>14</td><td>28</td><td>-203,890</td><td>733,536</td><td>-937,426</td><td>-0.00072</td><td>-0.00289</td><td>0.54270</td><td>0.24728</td><td>0.29253</td><td>-0.00142</td><td>0.01203</td><td>0.01061</td></tr><tr><td>15</td><td>30</td><td>-280,843</td><td>713,896</td><td>-994,739</td><td>-0.00077</td><td>-0.00307</td><td>0.58505</td><td>0.27135</td><td>0.310629</td><td>-0.00153</td><td>0.01061</td><td>0.00908</td></tr><tr><td>16</td><td>32</td><td>-357,786</td><td>694,256</td><td>-1,052,042</td><td>-0.00081</td><td>-0.00325</td><td>0.62126</td><td>0.29253</td><td>0.32548</td><td>-0.00162</td><td>0.00908</td><td>0.00746</td></tr><tr><td>17</td><td>34</td><td>-337,457</td><td>674,617</td><td>-1,012,074</td><td>-0.00078</td><td>-0.00312</td><td>0.65096</td><td>0.310629</td><td>0.33721</td><td>-0.00156</td><td>0.00746</td><td>0.00590</td></tr><tr><td>18</td><td>36</td><td>-317,128</td><td>654,977</td><td>-972,105</td><td>-0.00075</td><td>-0.00300</td><td>0.67441</td><td>0.32548</td><td>0.34593</td><td>-0.00150</td><td>0.00590</td><td>0.00440</td></tr><tr><td>19</td><td>38</td><td>-296,780</td><td>635,337</td><td>-932,117</td><td>-0.00072</td><td>-0.00288</td><td>0.69186</td><td>0.33721</td><td>0.35177</td><td>-0.00144</td><td>0.0044</td><td>0.00296</td></tr><tr><td>20</td><td>40</td><td>-276,471</td><td>615,697</td><td>-892,168</td><td>-0.00069</td><td>-0.00275</td><td>0.70354</td><td>0.34593</td><td>0.35486</td><td>-0.00138</td><td>0.00296</td><td>0.00158</td></tr><tr><td>21</td><td>42</td><td>-256,142</td><td>596,057</td><td>-852,199</td><td>-0.00066</td><td>-0.00263</td><td>0.70972</td><td>0.35177</td><td>0.35532</td><td>-0.00132</td><td>0.00158</td><td>0.00026</td></tr><tr><td>22</td><td>44</td><td>-240,745</td><td>555,710</td><td>-796,455</td><td>-0.00061</td><td>-0.00244</td><td>0.71064</td><td>0.35486</td><td>0.35332</td><td>-0.00122</td><td>0.00026</td><td>0.00096</td></tr><tr><td>24</td><td>48</td><td>-215,263</td><td>452,718</td><td>0.35332</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table></body></html></div>


<div style="text-align: center;">S- e </div>


aee neee e 

e eeeeeee 

2-000-02



<!-- batch 10 | page 35 -->

## PROBLEM 2A-2O SHOCK RESPONSE SPECTRA 

Problem:Construct the elastic shock response spectra for the interior components of an above ground structure subject to an external explosion.



## Procedure:

Step 1.Determine maximum acceleration, velocity and displacement due to ground shock according to procedure outlined in Problem 2A-18.

Step 2.Determine maximum acceleration, velocity and displacement due to air shock according to the procedure outlined in Problems 2A-10 and 2A-19.

Step 3.Determine if the ground shock is outrunning or superseismic (Section 223.2). For outrunning ground shock the maximum values of displacement,velocity and acceleration in horizontal and vertical directions are the algebraic summation of the maximum motions from Steps 1 and 2.Otherwise proceed to Step 4.



Step 4.For superseismic ground shock the maximum values of displacement,velocity and acceleration are the numerically larger values of direct-induced ground shock or the algebraic sum of the maximum motions from air shock and airburst induced ground shock.



Step 5.Calculate the magnitude of acceleration, velocity and displacement for response spectra in horizontal and vertical directions by multiplying the maximum values of motions from Step 3 or Step 4 by their appropriate factor from Section 2-24.3.



Step 6.Draw the horizontal and vertical shock response spectras.

<!-- batch 10 | page 36 -->

## EXAMPLE 2A-2OSHOCK RESPONSE SPECTRA 

Required:Shock response spectra for the structure defined in Examples 2A-18and 2A-19.



Solution:

Step 1.Maximum values of motion in vertical and horizontal directions due to ground shock according to the procedure outlined in Example 2A-18 are:

a. Air blast-induced 

$$\begin{aligned}&A_{H}=A_{V}=3.44g\\&V_{H}=V_{V}=1.125in/sec\\&D_{H}=D_{V}=0.014in\\ \end{aligned}$$

b. Direct-induced 

$$\begin{aligned}A_{H}&=3.78g\\A_{V}&=7.56g\\V_{H}&=V_{V}=6.02in/sec\\D_{H}&=D_{V}=.120in\end{aligned}$$

Step 2.Maximum horizontal acceleration, velocity and displacement due to air shock following the procedure outlined in Examples 2A-10 and 2A-19.

$$\begin{aligned}A_{max}&=3.16g\\V_{max}&=12.31in/sec\\D_{max}&=0.355in\end{aligned}$$

Step 3.

a. Check for outrunning ground shock 

$$\begin{aligned}T_{AG}<T_{A}:\\\mathsf{From}\;&\mathsf{Example}\;2\mathsf{A}-18\\T_{AG}=26.6\;\mathsf{ms}\\&T_{A}=60.9\;\mathsf{ms}\\&T_{AG}<T_{A}\;\mathsf{Outrunning\;ground\;shock}\end{aligned}$$

<!-- batch 10 | page 37 -->

b.  Add the values of maximum motions from Step 1 and Step 2.

$$\begin{aligned}&A_{Hmax}=3.16+3.44+3.78=10.38g\\&V_{Hmax}=12.310+1.108+6.020=19.438in/sec\\&D_{Hmax}=0.355+0.014+0.120=.489in\\ \end{aligned}$$

and 

$$\begin{aligned}&A_{Vmax}=3.44+7.56=11.00g\\&V_{Vmax}=1.108+6.020=7.128in/sec\\&D_{Vmax}=0.014+0.120=0.134in\\ \end{aligned}$$

Step 4.

Does not apply, the ground shock is not superseismic.

Step 5.Magnitude of the motions for response spectra.

$$\begin{aligned}&A_{H}=10.38\times2.0=20.76g\\&V_{H}=19.438\times1.5=29.157in/sec\\&D_{H}=0.489\times1.0=0.489in\\ \end{aligned}$$

and 

$$\begin{aligned}&A_{V}=11.00\times2.0=22.00g\\&V_{V}=7.128\times1.5=10.692in/sec\\&D_{V}=0.134\times1.0=0.134in\\ \end{aligned}$$

Step 6.See the shock response spectra for the values from Step 6 in Figure 2A-28(+).



<div style="text-align: center;">Figure 2A-28</div>


<div style="text-align: center;"><img src="../pages/batch 10/imgs/img_in_chart_box_243_1121_957_1437.jpg" alt="Image" width="59%" /></div>


<!-- batch 10 | page 38 -->

## APPENDIX 2B LIST OF SYMBOLS 

a (1) acceleration (in/ms2)

(2) depth of equivalent rectangular stress block (in)

(3) long span of a panel (in)

ao velocity of sound in air (ft/sec)

$ax$acceleration in x direction (in/ms2)

ay acceleration in y direction (in/ms2)

A (1) area (in 2

(2) explosive composition factor $(\mathsf{o z}^{1/2}\mathrm{-i n}^{-3/2})$ 

$A_{a}$ area of diagonal bars at the support within a width b (in2)

$A_{b}$ area of reinforcing bar (in2)

Ad$(1) door area (in 2)

(2) area of diagonal bars at the support within a width b (in2)

AD drag area (in 2)

$A_{f}$ net area of wall excluding openings (ft2)

$A_{g}$ area of gross section (in2)

$A_{H}$ maximum horizontal acceleration of the ground surface (g's)

$A_{L}$ area of longitudinal torsion reinforcement (in2)

$A_{L}$ lift area (in2)

$An$(1) net area of section (in2)

(2) area of individual wall subdivision (ft2)

$A_{o}$ area of openings (ft2)

$A_{p s}$ area of prestressed reinforcement (in2)

$A_{s}$ area of tension reinforcement within a width b (in)

$A_{s}{'}$ area of compression reinforcement within a width b (in2)

$A_{s}-$ area of rebound reinforcement (in 2)



<!-- batch 10 | page 39 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>each face $A_{s H}$ $(\mathsf{i n}^{2})^{\star}$</td><td>area of flexural reinforcement within a width b in the horizontal direction on</td></tr><tr><td>$A_{s p}$</td><td>area of spiral reinforcement $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{s t}$</td><td>total area of reinforcing steel $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{s V}$</td><td>area of flexural reinforcement within a width b in the vertical direction on each face $({\mathsf{i n}}^{2})^{*}$</td></tr><tr><td>$A_{t}$</td><td>area of one leg of a closed tie resisting torsion within a distance $s(\mathsf{i n}^{2})$</td></tr><tr><td>$A_{v}$</td><td>total area of stirrups or lacing reinforcement in tension within a distance, or and a width $s_{s}$ $\dot{b}_{s}\mathrm{o r}b_{I}(\mathsf{i n}^{2})$ $s_{I}$</td></tr><tr><td>$A_{V}$</td><td>maximum vertical acceleration of the ground surface (g's)</td></tr><tr><td>$A_{w}$ $A_{1},A_{11}$</td><td>area of wall (ft{2)</td></tr><tr><td>$b$</td><td>area of sector I and ll, respectively 1 $({\mathsf{i n}}^{2})$</td></tr><tr><td></td><td>(1) width of compression face of flexural member (in)</td></tr><tr><td></td><td>(2) width of concrete strip in which the direct shear stresses at the supports are resisted by diagonal bars (in)</td></tr><tr><td></td><td>(3) short span of a panel (in)</td></tr><tr><td>$b_{f}$</td><td>width of fragment (in)</td></tr><tr><td>$b_{s}$</td><td>width of concrete strip in which the diagonal tension stresses are resisted</td></tr><tr><td>$b_{I}$</td><td>by stirrups of area width of concrete strip in which the diagonal tension stresses are resisted by $A_{v}\left(\mathsf{i n}\right)$</td></tr><tr><td>$b_{o}$</td><td>lacing of area $A_{v}\left(\mathsf{i n}\right)$</td></tr><tr><td>$b_{t}$</td><td>failure perimeter for punching shear (in) center-to-center dimension of a closed rectangular tie along b (in)</td></tr><tr><td>B</td><td></td></tr><tr><td></td><td>explosive constant defined in Table $2-7\;\underline{{{(\pm)}}}\;(\mathsf{o z}^{1/2}\;\mathsf{i n}^{-7/6})$</td></tr><tr><td>C</td><td>(1) distance from the resultant applied load to the axis of rotation (in)</td></tr><tr><td></td><td>(2) damping coefficient (3) width of column capital (in)</td></tr></table></body></html></div>


<!-- batch 10 | page 40 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>$c_{||}$ $c_{1}$</td><td>distance from the resultant applied load to the axis of rotation for sectors I and Il, respectively (in)</td></tr><tr><td>$c_{s}$</td><td>dilatational velocity of concrete (ft/sec)</td></tr><tr><td>C</td><td>(1) shear coefficient</td></tr><tr><td></td><td>(2) deflection coefficient for flat slabs</td></tr><tr><td>$C_{C}$</td><td>deflection coefficient for the center of interior panel of flat slab</td></tr><tr><td>$C_{c r}$</td><td>critical damping</td></tr><tr><td>$C_{d}$</td><td>shear coefficient for ultimate shear stress of one-way elements</td></tr><tr><td>$C_{D}$</td><td>drag coefficient</td></tr><tr><td>$C_{D}q$</td><td>drag pressure (psi)</td></tr><tr><td>$C_{D}q_{o}$</td><td>peak drag pressure (psi)</td></tr><tr><td>$C_{E}$</td><td>equivalent load factor</td></tr><tr><td>$C_{f}$</td><td>post-failure fragment coefficient $(\mathsf{I b}^{2}\mathrm{-}\mathsf{m s}^{4}/\mathsf{i n}^{8})$</td></tr><tr><td>$C_{H}$</td><td>shear coefficient for ultimate shear stress in horizontal direction for two-way</td></tr><tr><td>$C_{L}$</td><td>elements* (1) leakage pressure coefficient from Figure 2-235 (+)</td></tr><tr><td></td><td>(2) deflection coefficient for midpoint of long side of interior flat slab</td></tr><tr><td></td><td>panel (3) lift coefficient</td></tr><tr><td>$C_{M}$</td><td>maximum shear coefficient</td></tr><tr><td>$C_{m}$</td><td>equivalent moment correction factor</td></tr><tr><td>$C_{p}$</td><td>compression wave seismic velocity in the soil from Table 2-10 (+) (in/sec)</td></tr><tr><td>$C_{r}$</td><td></td></tr><tr><td></td><td>sound velocity in reflected region from Figure 2-192 (+) (ft/ms)</td></tr><tr><td>$C_{R}$</td><td>force coefficient for shear at the corners of a window frame</td></tr><tr><td>$C_{r\alpha}$</td><td>peak reflected pressure coefficient at angle of incidence α</td></tr><tr><td>$C_{s}$</td><td>shear coefficient for ultimate support shear for one-way elements</td></tr></table></body></html></div>


<!-- batch 10 | page 41 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>shear coefficient for ultimate support shear in horizontal direction for two- way elements $C_{s V}$ $C_{s H}$</td></tr><tr><td>shear coefficient for ultimate support shear in vertical direction for two-way elements</td></tr><tr><td>deflection coefficient for midpoint of short side of interior flat slab panel $C_{s}$</td></tr><tr><td>impulse coefficient at deflection $C_{u}$ $X_{u}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>impulse coefficient at deflection $C_{u}{'}$ $X_{m}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>shear coefficient for ultimate shear stress in vertical direction for two-way elements* $C_{v}$</td></tr><tr><td>shear coefficient for the ultimate shear along the long side of window frame $C_{x}$</td></tr><tr><td>shear coefficient for the ultimate shear along the short side of window frame $C_{y}$</td></tr><tr><td>confidence level $C_{L}$</td></tr><tr><td>(1) impulse coefficient at deflection $C_{1}$ $X_{1}\;(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>(2) ratio of gas load to shock load</td></tr><tr><td>impulse coefficient at deflection $C_{1}{'}$ $X_{m}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>ratio of gas load duration to shock load duration $C_{2}$</td></tr><tr><td>(1) distance from extreme compression fiber to centroid of tension reinforcement (in) $d$</td></tr><tr><td>(2) diameter (in)</td></tr><tr><td>(3) fragment diameter (in)</td></tr><tr><td>distance from extreme compression fiber to centroid of compression $d^{\prime}$</td></tr><tr><td>reinforcement (in) diameter of reinforcing bar (in) $d_{b}$</td></tr><tr><td>distance between the centroids of the compression and tension $d_{c}$</td></tr><tr><td>reinforcement (in)</td></tr><tr><td>distance between the centroids of the horizontal compression and tension reinforcement (in) diameter of steel core (in) $d_{c o}$ $d_{c H}$</td></tr></table></body></html></div>


<!-- batch 10 | page 42 -->

dcv distance between the centroids of the vertical compression and tension 

reinforcement (in)

de distance from support and equal to distance d or dc (in)

di average inside diameter of explosive casing (in)

$d_i'}$adjusted inside diameter of casing (in)

dp distance between center lines of adjacent lacing bends measured normal to 

flexural reinforcement (in)

d_$distance from extreme compression fiber to centroid of prestressed 

reinforcement (in)

dsp depth of spalled concrete (in)

$d_{1$diameter of cylindrical portion of primary fragment (in)

D (1) unit flexural rigidity (Ib-in)

(2) location of shock front for maximum stress (ft)

(3) minimum magazine separation distance (ft)

(4) caliber density (Ib/in3)

(5) overall diameter of circular section (in)

(6) damping force (lb)

(7) displacement of mass from shock load (in)

$D_{E}$ equivalent loaded width of structure for non-planar wave front (ft)

$D_{H}$ maximum horizontal displacement of the ground surface (in)

DIF dynamic increase factor 

$D_{s}$ diameter of the circle through centers of reinforcement arranged in a circular 

pattern (in)

Dsp diameter of the spiral measured through the centerline of the spiral bar (in)

DLF dynamic load factor 

$D_{V}$ maximum vertical displacement of the ground surface (in)

e (1) base of natural logarithms and equal to 2.71828..…

(2)distance from centroid of section to centroid of prestressed 

reinforcement (in)



<!-- batch 10 | page 43 -->

(3) actual eccentricity of load (in)

$\mathbf{\boldsymbol{e}}_{b}$ balanced eccentricity (in)

$(2E)$ 1/2Gurney Energy Constant (ft/sec)

E (1) modulus of elasticity 

(2) internal work (in-lbs)

$E_{c}$ modulus of elasticity of concrete (psi)

$E_{m}$ modulus of elasticity of masonry units (psi)

$E_{s}$ modulus of elasticity of reinforcement (psi)

f (1) unit external force (psi)

(2) frequency of vibration (cps)

$f_{c}^{\prime}$ static ultimate compressive strength of concrete at 28 days (psi)

$f_{d c}{'}$ dynamic ultimate compressive strength of concrete (psi)

$f_{d m}{'}$ dynamic ultimate compressive strength of masonry units (psi)

$f_{d s}$ dynamic design stress for reinforcement (a function of $f_{y_{1}}$ ,$f_{u}$ and Θ) (psi)

$f_{d u}$ dynamic ultimate stress of reinforcement (psi)

$f_{d y}$ dynamic yield stress of reinforcement (psi)

$f_{m}{'}$ static ultimate compressive strength of masonry units (psi)

$f_{n}$ natural frequency of vibration (cps)

$f_{p s}$ average stress in the prestressed reinforcement at ultimate load (psi)

$\pmb{f}_{p u}$ specified tensile strength of prestressing tendon (psi)

$\pmb{f}_{p y}$ yield stress of prestressing tendon corresponding to a 1 percent elongation 

(psi)

$f_}$reflection factor 

$f_{s}$ static design stress for reinforcement (psi)

$f_{s e}$ effective stress in prestressed reinforcement after allowances for all 

prestress losses (psi)

$f_{u}$ static ultimate stress of reinforcement (psi)

$f_}$static yield stress of reinforcement (psi)



<!-- batch 10 | page 44 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>F</td><td>(1) total external force (lbs)</td></tr><tr><td></td><td>(2) coefficient for moment of inertia of cracked section</td></tr><tr><td></td><td>(3) function of _and for bilinear triangular load $C_{2}$ $C_{1}$</td></tr><tr><td>$F_{o}$</td><td>force in the reinforcing bars (lbs)</td></tr><tr><td>$F_{E}$</td><td>equivalent external force (Ilbs)</td></tr><tr><td>$F_{D}$</td><td>drag force (lbs)</td></tr><tr><td>$F_{F}$</td><td>frictional force (Ibs)</td></tr><tr><td>$F_{L}$</td><td>lift force (Ibs)</td></tr><tr><td>$F_{N}$</td><td>vertical load supported by foundation (lbs)</td></tr><tr><td>g</td><td>acceleration due to gravity (32.2 ft/sec 2)</td></tr><tr><td>G</td><td>shear modulus (psi)</td></tr><tr><td>$h$</td><td>(1) charge location parameter (ft)</td></tr><tr><td>$h_{n}$</td><td>(2) height of masonry wall average clearing distance for individual areas of openings from Section 2-</td></tr><tr><td></td><td>15.4.2</td></tr><tr><td>$h_{t}$ $h^{\prime}$</td><td>center-to-center dimension of a closed rectangular tie along h (in)</td></tr><tr><td>$H$</td><td>clear height between floor slab and roof slab</td></tr><tr><td></td><td>(1) span height (in)*</td></tr><tr><td></td><td>(2) distance between reflecting surface(s) and/or free edge(s) in vertical direction (ft)</td></tr><tr><td>$H_{c}$</td><td>(3) minimum transverse dimension of mean presented area of object (ft)</td></tr><tr><td>$H_{s}$</td><td>height of charge above ground (ft)</td></tr><tr><td></td><td>height of structure (ft)</td></tr><tr><td>$H_{T}$</td><td>height of triple point (ft)</td></tr><tr><td>$H_{w}$</td><td>height of wall (ft)</td></tr><tr><td>$H_{c}$</td><td>heat of combustion (ft-lb/lb)</td></tr></table></body></html></div>


<!-- batch 10 | page 45 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>$Hd}$</td><td>heat of detonation (ft-Ib/lb)</td></tr><tr><td>i</td><td>unit positive impulse (psi-ms)</td></tr><tr><td>$ia$</td><td>sum of blast impulse capacity of the receiver panel and the least impulse absorbed by the sand (psi-ms)</td></tr><tr><td>iba</td><td>blast impulse capacity of receiver panel (psi-ms)</td></tr><tr><td>i</td><td>unit negative impulse (psi-ms)</td></tr><tr><td></td><td>sum of scaled unit blast impulse capacity of receiver panel and scaled unit</td></tr><tr><td></td><td>blast impulse attenuated through concrete and sand in a composite element</td></tr><tr><td>$ib$</td><td>(psi-ms/lb{/{3 unit blast impulse (psi-ms)</td></tr><tr><td>1</td><td>scaled unit blast impulse (psi-ms/lb1/3)</td></tr><tr><td>$\overline{{\overline{{i}}_{b a}}}$</td><td>scaled unit blast impulse capacity of receiver panel of composite element</td></tr><tr><td></td><td>(psi-ms/lb/{3)</td></tr><tr><td>$\overline{{\dot{I}_{b d}}}$</td><td>scaled unit blast impulse capacity of donor panel of composite element (psi-ms/lb1/{3)</td></tr><tr><td>$\overline{{\dot{I}_{b t}}}$</td><td>total scaled unit blast impulse capacity of composite element (psi-ms/lb1/3)</td></tr><tr><td>$ic$</td><td>impulse capacity of an element (psi-ms)</td></tr><tr><td>$j_{d}$</td><td>total drag and diffraction impulse (psi-ms)</td></tr><tr><td>ie</td><td></td></tr><tr><td>ifs</td><td>unit excess blast impulse (psi-ms)</td></tr><tr><td></td><td>required impulse capacity of fragment shield (psi-ms)</td></tr><tr><td>$j_{g}$</td><td>gas impulse (psi-ms)</td></tr><tr><td>$ir$</td><td>unit positive normal reflected impulse (psi-ms)</td></tr><tr><td>i</td><td>unit negative normal reflected impulse (psi-ms)</td></tr><tr><td>$i_{r\alpha}$</td><td>peak reflected impulse at angle of incidence α (psi-ms)</td></tr><tr><td>$is$</td><td>unit positive incident impulse (psi-ms)</td></tr><tr><td></td><td></td></tr><tr><td>$is}$</td><td>unit negative incident impulse (psi-ms)</td></tr><tr><td>ist</td><td>impulse consumed by fragment support connection (psi-ms)</td></tr></table></body></html></div>


<!-- batch 10 | page 46 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>(1) moment of inertia for slabs） for beams) $({\mathsf{i n}}^{4}$ $(\mathsf{i n}^{4}/\mathsf{i n}$</td></tr><tr><td>(2) total impulse applied to fragment</td></tr><tr><td>average of gross and cracked moments of inertia for slabs) for beams) $({\mathsf{i n}}^{4}$ $I_{a}$ $(\mathsf{i n}^{4}/\mathsf{i n}$</td></tr><tr><td>moment of inertia of cracked concrete section for slabs) for $({\mathsf{i n}}^{4}$ $I_{c}$ $(\mathsf{i n}^{4}/\mathsf{i n}$</td></tr><tr><td>beams) moment of inertia of cracked concrete section in horizontal direction $I_{c H}$ $(\mathsf{i n}^{4}/\mathsf{i n})^{*}$</td></tr><tr><td>moment of inertia of cracked concrete section in vertical direction $I_{c V}$ $(\mathsf{i n}^{4}/\mathsf{i n})^{*}$</td></tr><tr><td>moment of inertia of gross concrete section for slabs) for beams) $I_{g}$ $({\mathsf{i n}}^{4}$ $(\mathsf{i n}^{4}/\mathsf{i n}$</td></tr><tr><td>mass moment of inertia 1 $(\mathsf{I b}{-}\mathsf{m s}^{2}{-}\mathsf{i n})$ $I_{m}$</td></tr><tr><td>moment of inertia of net section of masonry unit 1 $I_{n}$ $({\mathsf{i n}}^{4})$</td></tr><tr><td>gross moment of inertia of slab $I_{s}$ $(\mathsf{i n}^{4}/\mathsf{i n})$</td></tr><tr><td>impulse consumed by the fragment support connection (psi-ms) $I_{s t}$</td></tr><tr><td>gross moment of inertia of wall ratio of distance between centroids of compression and tension forces to the $I_{w}$ $(\mathsf{i n}^{4}/\mathsf{i n})$</td></tr><tr><td>depth d $j$</td></tr><tr><td>(1) constant depending on the casing metal $k$</td></tr><tr><td>(2) effective length factor</td></tr><tr><td>velocity decay coefficient K (1) unit stifness (psi/in for slabs) (Ib/in/in for beams) (Ib/in for springs) $k_{v}$</td></tr><tr><td>(2) constant defined in Section 2-18.2</td></tr><tr><td>elastic unit stifness (psi/in for slabs) (Ib/in/in for beams) $K_{e}$</td></tr><tr><td>elasto-plastic unit stiffness (psi/in for slabs) (Ib/in/in for beams) $K_{e p}$</td></tr><tr><td>(1) equivalent elastic unit stiffness (psi/in for slabs) (Ib/in/in for beams) $K_{E}$</td></tr><tr><td>(2) equivalent spring constant (lb/in)</td></tr><tr><td></td></tr><tr><td>load factor load-mass factor $K_{L M}$ $K_{L}$</td></tr></tbody></table></body></html></div>


<!-- batch 10 | page 47 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>load-mass factor in the ultimate range $(K_{L M})_{u}$</td></tr><tr><td>load-mass factor in the post-ultimate range $(K_{L M})_{u p}$</td></tr><tr><td>mass factor $K_{M}$</td></tr><tr><td>resistance factor $K_{R}$</td></tr><tr><td>kinetic energy $K_{E}$</td></tr><tr><td>charge location parameter (ft)</td></tr><tr><td>(1) length of the yield line (in)</td></tr><tr><td>(2) width of 1/2 of the column strip (in)</td></tr><tr><td>basic development length of reinforcing bar (in) $I_{d}$</td></tr><tr><td>development length of hooked bar (in) $I_{d h}$</td></tr><tr><td>length of cylindrical explosive (in) $I_{c}$</td></tr><tr><td>spacing of same type of lacing bar (in) $I_{p}$</td></tr><tr><td>span of flat slab panel (in) $I_{s}$</td></tr><tr><td>L (1) span length (in)*</td></tr><tr><td>(2) distance between reflecting surface(s) and/or free edge(s) in horizontal direction (ft)</td></tr><tr><td>length of cylinder (in) $L_{c y l}$</td></tr><tr><td>length of fragment (in) $L_{f}$</td></tr><tr><td>clear span in short direction (in) $L_{H}$</td></tr><tr><td>length of lacing bar required in distance s, (in) $L_{I}$</td></tr><tr><td>clear span in long direction (in) $L_{L}$</td></tr><tr><td>embedment length of reinforcing bars (in) $L_{o}$</td></tr><tr><td></td></tr><tr><td>unsupported length of column (in) $L_{u}$</td></tr><tr><td>wave length of positive pressure phase (ft) $L_{w}$</td></tr><tr><td>wave length of negative pressure phase (ft) $L_{w}^{-}$</td></tr></tbody></table></body></html></div>


<!-- batch 10 | page 48 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>$L_{x}$</td><td>clear span in long direction (in)</td></tr><tr><td>$L_{y}$</td><td>clear span in short direction (in)</td></tr><tr><td>$L_{w b},L_{w d}$</td><td>wave length of positive pressure phase at points b and d, respectively (ft)</td></tr><tr><td>$L_{1}$</td><td>total length of sector of element normal to axis of rotation (in)</td></tr><tr><td>m</td><td>(1) unit mass for slabs) [beams, $(\mathtt{p s i}\mathtt{-}\mathtt{m s}^{2}/\mathsf{i n}$ $(\mathsf{I b}/\mathsf{i n}-\mathsf{m s}^{2})/\mathsf{i n}]$</td></tr><tr><td></td><td>(2) ultimate unit moment (in-lbs/in)</td></tr><tr><td></td><td>(3) mass of fragment $(\mathsf{I b s}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$m_{a}$</td><td>average of the effective elastic and plastic unit masses for slabs) $(\mathtt{p s i-}\mathtt{m s}^{2}/\mathrm{i n}$</td></tr><tr><td>$m_{e}$</td><td>[beams, effective unit mass for slabs) [beams, $(\mathtt{p s i}\mathtt{-m s}^{2}/\mathsf{i n}$ $(\mathsf{I b}/\mathsf{i n}-\mathsf{m s}^{2})/\mathsf{i n}]$ $(\mathsf{l b}/\mathsf{i n}-\mathsf{m s}^{2})/\mathsf{i n}]$</td></tr><tr><td>$m_{s p}$</td><td>mass of spalled fragments $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$</td></tr><tr><td>$m_{u}$</td><td>effective unit mass in the ultimate range for slabs) [beams, (Ib/in- $(\mathtt{p s i}\mathtt{-}\mathtt{m s}^{2}/\mathsf{i n}$</td></tr><tr><td>$m_{u p}$</td><td>effective unit mass in the post-ultimate range $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$ $\mathsf{m s}^{2})/\mathsf{i n}]$</td></tr><tr><td>M</td><td>(1) unit bending moment (in-Ibs/in for slabs) (in-lbs for beams)</td></tr><tr><td></td><td>(2) total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td></td><td></td></tr><tr><td>$M_{e}$</td><td>(3) design moment (in-lbs)</td></tr><tr><td>$M_{u}$</td><td>effective total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{u}^{-}$</td><td>ultimate unit resisting moment (in-lbs/in for slabs) (in-lbs for beams) ultimate unit rebound moment (in-Ibs/in for slabs) (in-lbs for beams)</td></tr><tr><td>$M_{c}$</td><td></td></tr><tr><td>$M_{A}$</td><td>moment of concentrated loads about line of rotation of sector (in-lbs)</td></tr><tr><td></td><td>fragment distribution factor</td></tr><tr><td>$M_{E}$</td><td>equivalent total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{H N}$</td><td>ultimate unit negative moment capacity in horizontal direction (in-lbs/in)*</td></tr><tr><td>$M_{H P}$</td><td>ultimate unit positive moment capacity in horizontal direction (in-lbs/in)</td></tr><tr><td>$M_{O H},M_{O L}$</td><td>total panel moment for direction H and L respectively (in-lbs)</td></tr></tbody></table></body></html></div>


<!-- batch 10 | page 49 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>Ibs for beams) $M_{N}$</td><td>ultimate unit negative moment capacity at supports (in-lIbs/in for slabs) (in-</td></tr><tr><td>$M_{P}$</td><td>ultimate unit positive moment capacity at midspan (in-lbs/in for slabs) (in-lbs for beams)</td></tr><tr><td>$M_{V N}$</td><td>ultimate unit negative moment capacity in vertical direction (in-lbs/in)*</td></tr><tr><td>$M_{V P}$</td><td>ultimate unit positive moment capacity in vertical direction (in-lbs/in)</td></tr><tr><td>$M_{1}$</td><td>value of smaller end moment on column</td></tr><tr><td>$M_{2}$</td><td>value of larger end moment on column</td></tr><tr><td>n</td><td>(1) modular ratio</td></tr><tr><td></td><td>(2) number of time intervals</td></tr><tr><td></td><td>(3) number of glass pane tests</td></tr><tr><td></td><td>(4) caliber radius of the tangent ogive of fragment nose</td></tr><tr><td>$N$</td><td>(1) number of adjacent reflecting surfaces</td></tr><tr><td></td><td>(2) nose shape factor</td></tr><tr><td>$N_{f}$</td><td>number of primary fragments larger than $W_{f}$</td></tr><tr><td>$N_{u}$</td><td>axial load normal to the cross section</td></tr><tr><td>$N_{T}$</td><td>total number of fragments</td></tr><tr><td>$p$</td><td>reinforcement ratio equal to $A_{s}/b d\mathrm{o r}A_{s}/b d_{c}$</td></tr><tr><td>$p^{\prime}$</td><td></td></tr><tr><td>$p_{b}$</td><td>reinforcement ratio equal to or $A_{s}/b d_{c}$ $A_{s}//b d$</td></tr><tr><td>$p_{o}$</td><td>reinforcement ratio producing balanced conditions at ultimate strength ambient atmospheric pressure (psi)</td></tr><tr><td>$p_{p}$</td><td>prestressed reinforcement ratio equal to $A_{p s}/b d_{p}$</td></tr><tr><td>$p_{m}$</td><td>mean pressure in a partially vented chamber (psi)</td></tr><tr><td></td><td></td></tr><tr><td>$p_{m o}$</td><td>peak mean pressure in a partially vented chamber (psi)</td></tr><tr><td>$p_{r}$</td><td>average peak reflected pressure (psi)</td></tr><tr><td>$p_{H}$</td><td>reinforcement ratio in horizontal direction on each face</td></tr></table></body></html></div>


<!-- batch 10 | page 50 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>total reinforcement ratio equal to $p_{T}$</td><td>$p_{H}+p_{V}$</td></tr><tr><td>$p_{V}$</td><td>reinforcement ratio in vertical direction on each face</td></tr><tr><td>$p(x)$</td><td>distributed load per unit length</td></tr><tr><td>$P$</td><td>(1) pressure (psi)</td></tr><tr><td></td><td>(2) concentrated load (Ibs)</td></tr><tr><td>$P$</td><td>negative pressure (psi)</td></tr><tr><td>$P_{c}$</td><td>critical axial load causing buckling (lbs)</td></tr><tr><td>$P_{g}$</td><td>maximum gas pressure (psi)</td></tr><tr><td>$P_{i}$</td><td>interior pressure within structure (psi)</td></tr><tr><td>$\delta\mathcal{P}_{i}$</td><td>interior pressure increment (psi)</td></tr><tr><td>$P_{f}$</td><td>fictitious peak pressure (psi)</td></tr><tr><td>$P_{m a x}$ $P_{o}$</td><td>maximum average pressure acting on interior face of wall (psi)</td></tr><tr><td></td><td>(1) peak pressure (psi)</td></tr><tr><td></td><td>(2) maximum axial load (lbs)</td></tr><tr><td></td><td>(3) atmospheric pressure (psi)</td></tr><tr><td>$P_{r}$</td><td>peak positive normal reflected pressure (psi)</td></tr><tr><td>$P_{r}^{-}$</td><td>peak negative normal reflected pressure (psi)</td></tr><tr><td>$\bar{P}_{r\alpha}$</td><td>peak reflected pressure at angle of incidence α (psi)</td></tr><tr><td>$P_{R I B}$</td><td>maximum average pressure on backwall (psi)</td></tr><tr><td>$P_{s}$</td><td>positive incident pressure (psi)</td></tr><tr><td>$P_{s b},P_{s e}$</td><td>positive incident pressure at points b and e, respectively (psi)</td></tr><tr><td>$P_{s o}$</td><td>peak positive incident pressure (psi)</td></tr><tr><td>$P_{s o}^{-}$</td><td>peak negative incident pressure (psi)</td></tr><tr><td>$P_{s o b},P_{s o d},P_{s o e}$</td><td>peak positive incident pressure at points b,d and e, respectively (psi)</td></tr><tr><td>$P_{u}$</td><td>ultimate axial load at actual eccentricity c (Ibs)</td></tr><tr><td>$P_{x}$</td><td>ultimate load when eccentricity is present (lbs) $\pmb{\epsilon}_{x}$</td></tr><tr><td>$P_{y}$</td><td>ultimate load when eccentricity  is present (Ibs) $\pmb{\mathscr{e}}_{y}$</td></tr></table></body></html></div>


<!-- batch 10 | page 51 -->

q dynamic pressure (psi)

q_b_{}_e dynamic pressure at points b and e, respectively (psi)

9o peak dynamic pressure (psi)

qob, qoe peak dynamic pressure at points b and e, respectively (psi)

r (1) unit resistance (psi)

(2)radius of spherical TNT (density equals 95Ib/ft3) charge (f)

(3) radius of gyration of cross section of column (in)

r unit rebound resistance (psi, for slabs) (Ib/in for beams)

ravail dynamic resistance available (psi)

δr change in unit resistance (psi, for slabs) (Ib/in for beams)

rd$radius from center of impulse load to center of door rotation (in)

rDL uniform dead load (psi)

re elastic unit resistance (psi, for slabs) (Ib/in for beams)

rep elasto-plastic unit resistance (psi, for slabs) (Ib/in for beams)

rfs ultimate unit resistance of fragment shield (psi)

rT tension membrane resistance (psi)

ru ultimate unit resistance (psi, for slabs) (Ib/in for beams)

rup post-ultimate unit resistance (psi)

$r_}$radius of hemispherical portion of primary fragment (in)

R (1) total internal resistance (lbs)

(2) slant distance (t)

(3) ratio of S/G 

(4) standoff distance (ft)

Reff effective radius (ft)

$R_{f}$ (1) distance traveled by primary fragment (ft)

(2) distance from center of detonation (ft)

$R_{g}$ uplift force at corners of window frame (lbs)



<!-- batch 10 | page 52 -->

$R_{I}$ radius of lacing bend (in)

$R_{t}$ target radius (ft)

$R_{A}$ normal distance (ft)

$R_{E}$ equivalent total internal resistance (lbs)

$R_{G}$ ground distance (ft)

$R_{u}$ -total ultimate resistance (lb)

$R_{1},R_{11}$ total internal resistance of sectors I and Il, respectively (Ibs)

s (1) sample standard deviation 

(2)spacing of torsion reinforcement in a direction parallel to the 

longitudinal reinforcement (in)

(3) pitch of spiral (in)

$s_{s}$ spacing of stirups in the direction parallel to the longitudinal reinforcement 

(in)

$s_{1}$ spacing of lacing in the direction parallel to the longitudinal reinforcement 

(in)

S height of front wall or one-half its width, whichever is smaller (ft)

$s^{\prime}$ weighted average clearing distance with openings (ft)

SE strain energy 

t time (ms)

$\delta\bar{\mathbf{t}}$ time increment (ms)

$t_{a}$ any time (ms)

$t_{b}$ $t_{e}$ $t_{f}$ time of arrival of blast wave at points b, e and f, respectively (ms)

$t_{c}$ (1) clearing time for reflected pressures (ms)

(2) average casing thickness of explosive charges (in)

$t_{c}^{\prime}$ (1) adjusted casing thickness (in)

(2) clearing time for reflected pressures adjusted for wall openings (ms)

$t_{d}$ rise time (ms)

$t_{E}$ time to reach maximum elastic deflection (ms)



<!-- batch 10 | page 53 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>$t_{g}$</td><td>fictitious gas duration (ms)</td></tr><tr><td>$t_{m}$</td><td>time at which maximum deflection occurs (ms)</td></tr><tr><td>$t_{0}$</td><td>duration of positive phase of blast pressure (ms)</td></tr><tr><td>$t_{o}^{-}$</td><td>duration of negative phase of blast pressure (ms)</td></tr><tr><td>$t_{o f}$</td><td>fictitious positive phase pressure duration (ms)</td></tr><tr><td>$t_{o f}$</td><td>fictitious negative phase pressure duration (ms)</td></tr><tr><td>$t_{r f}$</td><td>fictitious reflected pressure duration (ms)</td></tr><tr><td>tu</td><td>time at which ultimate deflection occurs (ms)</td></tr><tr><td>$t_{y}$</td><td>time to reach yield (ms)</td></tr><tr><td>tA</td><td>time of arrival of blast wave (ms)</td></tr><tr><td>tAG</td><td>time of arrival of ground shock (ms)</td></tr><tr><td>$t_{1}$</td><td>time at which partial failure occurs (ms)</td></tr><tr><td>T</td><td>(1) duration of equivalent triangular loading function (ms)</td></tr><tr><td></td><td>(2) thickness of masonry wall (in)</td></tr><tr><td></td><td>(3) toughness of material (psi-in/in)</td></tr><tr><td>$\frac{T_{c}}{T_{c}}$</td><td>thickness of concrete section (in)</td></tr><tr><td></td><td>scaled thickness of concrete section $(\mathsf{f t}/\mathsf{I b}^{1/3})$</td></tr><tr><td>$T_{g}$</td><td>thickness of glass (in)</td></tr><tr><td>$T_{H}$</td><td>force in the continuous reinforcement in the short span direction (lbs)</td></tr><tr><td>$T_{i}$</td><td>angular impulse load (Ib-ms-in)</td></tr><tr><td>$T_{L}$</td><td>force in the continuous reinforcement in the long span direction (lbs)</td></tr><tr><td>$T_{N}$</td><td>effective natural period of vibration (ms)</td></tr><tr><td>$T_{p f}$</td><td>minimum thickness of concrete to prevent perforation by a given fragment (in)</td></tr><tr><td>$T_{r}$</td><td>rise time (ms)</td></tr><tr><td>$T_{s}$</td><td></td></tr><tr><td></td><td>(1) thickness of sand fill (in) (2) thickness of slab (in)</td></tr></tbody></table></body></html></div>


<!-- batch 10 | page 54 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>$T_{s p}$</td><td colspan="2">minimum concrete thickness to prevent spalling (in)</td></tr><tr><td>$\overline{{T_{s}}}$</td><td colspan="2">scaled thickness of sand fill 1 $(\mathsf{f t}/\mathsf{I b}^{1/3})$</td></tr><tr><td>$T_{u}$</td><td colspan="2">total torsional moment at critical section (in-lbs)</td></tr><tr><td>$T_{w}$</td><td colspan="2">thickness of wall (in)</td></tr><tr><td>$T_{y}$</td><td colspan="2">force of the continuous reinforcement in the short direction (lbs)</td></tr><tr><td>$u$</td><td colspan="2">particle velocity (ft/ms)</td></tr><tr><td>$u_{u}$</td><td colspan="2">ultimate flexural or anchorage bond stress (psi)</td></tr><tr><td>$U$</td><td colspan="2">shock front velocity (ft/ms)</td></tr><tr><td>$U_{s}$</td><td colspan="2">strain energy</td></tr><tr><td>V</td><td colspan="2">velocity (in/ms)</td></tr><tr><td>$v_{a}$</td><td colspan="2">instantaneous velocity at any time (in/ms)</td></tr><tr><td>$v_{b}$</td><td colspan="2">boundary velocity for primary fragments (ft/sec)</td></tr><tr><td>$v_{c}$</td><td colspan="2">ultimate shear stress permitted on an unreinforced web (psi)</td></tr><tr><td>$v_{f}$</td><td colspan="2">maximum post-failure fragment velocity (in/ms)</td></tr><tr><td>(avg) $v_{f}$</td><td colspan="2">average post-failure fragment velocity (in/ms)</td></tr><tr><td>$v_{i}$</td><td colspan="2">velocity at incipient failure deflection (in/ms)</td></tr><tr><td>$v_{o}$</td><td colspan="2">initial velocity of primary fragment (ft/sec)</td></tr><tr><td>$v_{r}$</td><td colspan="2">residual velocity of primary fragment after perforation (ft/sec)</td></tr><tr><td>$v_{s}$</td><td colspan="2">striking velocity of primary fragment (ft/sec)</td></tr><tr><td>$v_{t o}$</td><td colspan="2">maximum torsion capacity of an unreinforced web (psi)</td></tr><tr><td>$v_{t u}$</td><td colspan="2">nominal torsion stress in the direction of (psi) $v_{u}$</td></tr><tr><td>ultimate shear stress (psi) $v_{u}$</td><td colspan="2">ultimate shear stress at distance from the horizontal support (psi)* $d_{e}$</td></tr><tr><td>$v_{u H}$</td><td></td><td rowspan="2"></td></tr><tr><td>$v_{x}$ $v_{u V}$</td><td>ultimate shear stress at distance  from the vertical support (psi) velocity in x direction (in/ms) $d_{e}$</td></tr></tbody></table></body></html></div>


<!-- batch 10 | page 55 -->

$Vy$velocity in y direction (in/ms)

V (1) volume of partially vented chamber $(\mathsf{f t}^{3})$ 

(2) velocity of compression wave through concrete (in/sec)

(3) velocity of mass under shock load (in/sec)

$V_{d}$ ultimate direct shear capacity of the concrete of width b (Ilbs)

$V_{d H}$ shear at distance $d_{e}$ from the vertical support on a unit width (Ibs/in)

$V_{d V}$ shear at distance $d_{e}$ from the horizontal support on a unit width (Ibs/in)

$V_{f}$ free volume $(\mathsf{f t}^{3})$ 1

$V_{H}$ maximum horizontal velocity of the ground surface (in/sec)

$V_{o}$ volume of structure (ft3)

$V_{s}$ shear at the support (Ib/in for panels) (Ilbs for beam)

$V_{s H}$ shear at the vertical support on a unit width (lbs/in)*

$V_{s V}$ shear at the horizontal support on a unit width (Ibs/in)*

$V_{u}$ total shear on a width b (lbs)

$V_{V}$ maximum vertical velocity of the ground surface (in/sec)

$V_{x}$ unit shear along the long side of window frame (lb/in)

$V_{y}$ unit shear along the short side of window frame (Ibs/in)

W applied uniform load (lbs-in2)

$W_{c$(1) unit weight (psi for panels) (Ib/in for beam)

(2) weight density of concrete (lbs/ft3)

$W_{s}$weight density of sand (Ibs/ft³)

W (1) design charge weight (Ilbs)

(2) external work (in-lbs)

(3) width of wall (ft)

$W_{A}$ weight of fluid (Ibs)

$W_{A C T}$ actual quantity of explosives (lbs)

$W_{c}$ total weight of explosive containers (Ibs)



<!-- batch 10 | page 56 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>effective charge weight (lbs) $W_{E}$</td><td></td></tr><tr><td>$W_{E g}$</td><td>effective charge weight for gas pressure (Ib)</td></tr><tr><td>$W_{E X P}$</td><td>weight of explosive in question (Ibs)</td></tr><tr><td>$W_{f}$</td><td>weight of primary fragment (oz)</td></tr><tr><td>$\overline{{W_{f}}}$</td><td>average fragment weight (oz)</td></tr><tr><td>$W_{F}$</td><td>weight of frangible element $(\mathsf{I b}/\mathsf{I t}^{2})$</td></tr><tr><td>$W_{C I}$</td><td>weight of inner casing (Ibs)</td></tr><tr><td>$W_{c o}$</td><td></td></tr><tr><td>$W_{c o}$</td><td>total weight of steel core (lbs)</td></tr><tr><td>$W_{c2}$ $W_{c1}$</td><td>weight of outer casing (lbs) total weight of plates 1 and 2, respectively (Ibs)</td></tr><tr><td>1， $W_{s}$</td><td>width of structure (ft)</td></tr><tr><td>$W_{D}$</td><td>work done</td></tr><tr><td>X</td><td>yield line location in horizontal direction (in)*</td></tr><tr><td>X</td><td>(1) deflection (in)</td></tr><tr><td></td><td>(2) distance from front of object to location of largest cross section to</td></tr><tr><td></td><td>plane of shock front (ft)</td></tr><tr><td>$X_{c}$ $X_{a}$</td><td>any deflection (in)</td></tr><tr><td>$X_{D L}$</td><td>lateral deflection to which a masonry wall develops no resistance (in)</td></tr><tr><td></td><td>deflection due to dead load (in)</td></tr><tr><td>$X_{e}$</td><td>elastic deflection (in)</td></tr><tr><td>$X_{E}$</td><td>equivalent elastic deflection (in)</td></tr><tr><td>$X_{e p}$</td><td>elasto-plastic deflection (in)</td></tr><tr><td>$X_{t}$</td><td>maximum penetration into concrete of armor-piercing fragments (in)</td></tr><tr><td>(in) $X_{t}^{\prime}$</td><td>maximum penetration into concrete of fragments other than armor-piercing</td></tr><tr><td>$X_{m}$</td><td>maximum transient deflection (in)</td></tr></table></body></html></div>


<!-- batch 10 | page 57 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>$X_{p}$</td><td>plastic deflection (in)</td></tr><tr><td>$X_{s}$</td><td>(1) maximum penetration into sand of armor-piercing fragments (in)</td></tr><tr><td></td><td>(2) static deflection (in)</td></tr><tr><td>$X_{u}$</td><td>ultimate deflection (in)</td></tr><tr><td>$X_{1}$</td><td>(1) partial failure deflection (in)</td></tr><tr><td></td><td>(2) deflection at maximum ultimate resistance of masonry wall (in)</td></tr><tr><td>y</td><td>yield line location in vertical direction (in)*</td></tr><tr><td>yt</td><td>distance from the top of section to centroid (in)</td></tr><tr><td>Z</td><td>scaled slant distance (ft/Ib/{3)</td></tr><tr><td>$Z_{A}$</td><td>scaled normal distance $(\mathsf{f t}/\mathsf{I b}^{1/3})$</td></tr><tr><td>$Z_{G}$</td><td>scaled ground distance (ft/b/3)</td></tr><tr><td>α</td><td>angle formed by the plane of stirrups, lacing, or diagonal reinforcement and the plane of the longitudinal reinforcement (deg)</td></tr><tr><td></td><td>(2) angle of incidence of the pressure front (deg)</td></tr><tr><td></td><td></td></tr><tr><td></td><td>(3) acceptance coefficient</td></tr><tr><td>αec</td><td>(4) trajectory angle (deg)</td></tr><tr><td>αecH, αecL</td><td>ratio of flexural stiffness of exterior wall to flat slab ratio of flexural stiffness of exterior wall to slab in direction H and L</td></tr><tr><td></td><td>respectively</td></tr><tr><td>B</td><td>(1) coefficient for determining elastic and elasto-plastic resistances</td></tr><tr><td></td><td>(2) particular support rotation angle (deg)</td></tr><tr><td></td><td>(3) rejection coefficient</td></tr><tr><td></td><td>(4) target shape factor from Figure 2-212 (+/+)</td></tr><tr><td>$\beta_{1}$</td><td>factor equal to 0.85 for concrete strengths up to 4000 psi and is reduced by 0.05 for each 1000 psi in excess of 4000 psi</td></tr><tr><td>γ</td><td>coefficient for determining elastic and elasto-plastic deflections</td></tr></tbody></table></body></html></div>


<!-- batch 10 | page 58 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>$γp</td><td>factor for type of prestressing tendon</td></tr></thead><tbody><tr><td>δ</td><td>moment magnifier</td></tr><tr><td>$δ$</td><td>clearing factor</td></tr><tr><td>δ</td><td>deflection at sector's displacement (in)</td></tr><tr><td>$\varepsilon_{c}{'}$</td><td>average strain rate for concrete (in/in/ms)</td></tr><tr><td>εm$</td><td>unit strain in mortar (in/in)</td></tr><tr><td>$\varepsilon_{s}^{\prime}$</td><td>average strain rate for reinforcement (in/in/ms)</td></tr><tr><td>εu</td><td>rupture strain (in/in/ms)</td></tr><tr><td>日</td><td>(1) support rotation angle (deg)</td></tr><tr><td></td><td>(2) angular acceleration (rad/ms2)</td></tr><tr><td>Omax</td><td>maximum support rotation angle (deg)</td></tr><tr><td>OH</td><td>horizontal rotation angle (deg)*</td></tr><tr><td>θV</td><td>vertical rotation angle (deg)</td></tr><tr><td>μ</td><td>(1) ductility factor</td></tr><tr><td></td><td>(2) coefficient of friction</td></tr><tr><td>V</td><td>Poisson's ratio</td></tr><tr><td>ρ</td><td>(1) mass density (lbs-ms2/in4)</td></tr><tr><td></td><td>(2) density of air behind shock front (Ibs/ft³)</td></tr><tr><td>ρa</td><td>density of air (o/in3)</td></tr><tr><td>ρc</td><td>density of casing (oz/in3)</td></tr><tr><td>ρf</td><td>mass density of fragment (o/in3)</td></tr><tr><td>$\rho_{o}$</td><td>mass density of medium (Ib-ms2/in{4)</td></tr><tr><td>$\sigma_{u}$</td><td>fracture strength of concrete (psi)</td></tr><tr><td>$\Sigma_{0}$</td><td>effective perimeter of reinforcing bars (in)</td></tr></tbody></table></body></html></div>


<!-- batch 10 | page 59 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>∑M</td><td>summation of moments (in-lbs)</td></tr><tr><td>∑MN</td><td>sum of the ultimate unit resisting moments acting along the negative yield lines (in-lbs)</td></tr><tr><td>ΣMP</td><td>sum of the ultimate unit resisting moments acting along the positive yield lines (in-lbs)</td></tr><tr><td>φ</td><td>(1) capacity reduction factor</td></tr><tr><td></td><td>(2) bar diameter (in)</td></tr><tr><td></td><td>(3) TNT conversion factor</td></tr><tr><td>φr</td><td>assumed shape function for concentrated loads</td></tr><tr><td>φ(x)</td><td>assumed shape function for distributed loads free edge</td></tr><tr><td></td><td>simple support</td></tr><tr><td>77777777</td><td>fixed support</td></tr><tr><td>XXXXXXXX</td><td>either fixed, restrained, or simple support</td></tr></table></body></html></div>


Note. This symbol was developed for two-way elements which are used as walls. When roof slabs or other horizontal elements are under consideration, this symbol will also be applicable if the element is treated as being rotated into a vertical position.

<!-- batch 10 | page 60 -->

## APPENDIX 2C BIBLIOGRAPHY 

## BLAST LOADS 

1.Armendt, B.R., Hippensteel, R. G., Hoffman, A. J., and Keefer, J. H.,Project White Tribe: Air Blast From Simultaneously Detonated LargeScale Explosive Charges, BRL Report 1145, Aberdeen Proving Ground,Maryland, September 1961.
2.Armendt, B.R., Hippensteel, R.G., Hoffman, A. J., and Kingery, C.N.,
The Air Blast From Simultaneously Detonated Explosive Spheres, BRL Report 1294, Aberdeen Proving Ground, Maryland, August 1960.3.Armendt, B.R., Hippensteel, R. G., Hofman, A. J., and Schlueter, S.D.,
The Air Blast From Simultaneously Detonated Explosive Spheres: Part II Optimization, BRL Memorandum Report 1384, Department of the Army Project No. 503-04-002, Aberdeen Proving Ground, Maryland, January 1962.
4.Ayvazyan, H.E., Dobbs N., Computer Program Impres, special publication ARLCD-SP-84001, prepared by Ammann and Whitney, New York, New York, for U.S. Army Armament Research and Development Center, Large Caliber Weapon Systems Laboratory, Dover, New Jersey.5.Baker, W. E., Explosions in Air, University of Texas Press, Austin, Texas 1973.
6.Baker, W. E., Prediction and Scaling of Reflected Impulse From Strong Blast Waves, International Journal of Mechanical Science, 9, 1967, pp.
45-51.
7.Bleakney, W., The Diffraction of Shock Waves Around Obstacles and the Transient Loading of Structures, Princeton University, March 1950,
w1(Published and Distributed by the Armed Forces Special Weapons Project).
8.Coulter, G.A., Air Shock and Flow in Model Rooms, BRL Memorandum Report 1987, Aberdeen Proving Ground, Maryland, June 1969.9.Coulter, G. A., Air Shock Filling of Model Rooms, BRL Memorandum Report 1916, Aberdeen Proving Ground, Maryland, March 1968.10.Coulter, G. A. and Peterson, R.L., Blast Fill Time of a One-Room Structure, Operation Prairie Flat Project Officers Report, Project LN 111POR-2102, Ballistic Research Laboratory, Aberdeen Proving Ground,
Maryland, November 1964.


<!-- batch 10 | page 61 -->

11.Coulter, G. A., Bulmash G., and Kingery C., Feasibility Study of Shock Wave Modification in the BRL 2.44 m Blast Simulator, Memorandum Report ARBRL-MR-0339, prepared by U.S. Army Armament Research and Development Center, Ballistic Research Laboratory, Aberdeen Proving Ground, Maryland, March 1984.
12.Cranz, C., Lehrbuch der Ballistik, Springer-Verlag, Berlin, 1926.13.Dewey, J.M., Johnson, O.T., and Patterson, J.D. II, Mechanical Impulse Measurements Close to Explosive Charges, BRL Report 1182, Aberdeen Proving Ground, Maryland, November 1962.
14.Dobratz, B.M., LLNL Explosives Handbook, Properties of Chemical Explosives and Explosive Simulants, URCL-52997, Lawrence Livermore National Laboratory, Livermore, California, March 1981.15.Enqineering Design Handbook, Principles of Explosive Behavior, AMCP 706-180, Headquarters, U.S. Army Material Command, Washington, D.C.,
April 1972.
16.Goodman, H. J., Compiled Free Air Blast Data on Bar Spherical Pentolite,
BRL Report 1092, Aberdeen Proving Ground, Maryland, 1960.17.Granstorm, S. A., Loading Characteristics of Air Blasts From Detonating Charges, Transactions of the Royal Institute of Technology, Stockholm,
Sweden, Nr.100,1956.
18.Hokanson, J.C., Esparza, E. D., and Wenzel, A. B., Blast Effects of Simultaneous Multiple-Charge Detonations, Contractor Report ARLCDCR-78032, ARRADCOM, Dover, New Jersey, AD E400232, October 1978.
19.Hokanson, J.C., Esparza, E.D., Baker W.E., Sandoval, N.R. and Anderson, C.E., Determination of Blast Loads in the Damaged Weapons Facility, Vol 3, Final Report, Purchase Order F0913400, SwR1-6578,
prepared by Southwest Research Institute, San Antonio, Texas, for Mason and Hanger - Silas Mason Company, Inc., Pantex Plant, Amarillo, Texas,
July 1982.
20.Hokanson, J. C., Esparza, E. D., and Wenzel, A. B., Reflected Blast Measurements Around Multiple Detonating Charges, Minutes of the Eighteenth Explosives Safety Seminar, Volume I, September 1978, pp.
447-471.
21.Hokanson, J. C., Esparza, E. D., Wenzel, A. B. (Southwest Research Institute). Price, P. D. (ARRADCOM). Blast Effects of Simultaeous Multiple-Charge Detonations, Contractor Report ARLCD-CR-78032,
prepared by U.S. Army Armament Research and Development Command,

<!-- batch 10 | page 62 -->

Large Caliber Weapon Systems Laboratory, Dover, New Jersey, October 1978.
22.Hopkinson, B. British Ordnance Board Minutes, 13565, 1915.23.Iwanski, E. C., et al., Blast Effects on Buildings and Structures Operation of 6-Foot and 2-Foot Shock Tubes: High Pressure Tests on Simple Shapes, Report No. 54, Final Test Report No. 10, ARF Project No. D87,
Armour Research Foundation of Ilinois Institute of Technology.24.Jack, W. H., Jr., Measurements of Normally Reflected Shock Waves From Explosive Charges, BRL Memorandum Report 1499, Aberdeen Proving Ground, Maryland, AD 422886, July 1963.
25.Jack, W. H., Jr. and Armendt, B. F., Jr., Measurements of Normally Reflected Shock Parameters Under Simulated High Altitude Conditions,
BRL Report 1280, Aberdeen Proving Ground, Maryland, AD 469014, April 1965.
26.Johansson, C. H. and Persson, P.A., Detonics of High Explosives,
Academic Press, London, England, and New York, New York, 1970.27.Johnson, O.T., Patterson, J.D. II, and Olson, W.C., A Simple Mechanical Method for Measuring the Reflected Impulse of Air Blast Waves, BRL Report 1099, Aberdeen Proving Ground, Maryland, July 1957.28.Kaplan, K., Lewis, K. S., and Morris, P. J., Blast Loading and Response of Military Equipment, Draft Final Report URS 7339-6, URS Research Company, San Mateo, California, Prepared for Ballistic Research Laboratory, December 1973.
29.Kaplan, K. and Price, P.D., Accidental Explosions and Effects of Blast Leakage Into Structures, Contractor Report ARLCD-CR-79009, U.S. Army ARRADCOM, Dover, New Jersey, AD E400320, June 197.30.Keenan, W.A., and Tancreto, J. E., Blast Environment From Fully and Partially Vented Explosions in Cubicles, Technical Report R 828, prepared by Civil Engineering Laboratory, Naval Construction Batalion Center, Port Hueneme, California, sponsored by Department of the Army Picatinny Arsenal, November 1975.
31.Keenan, W., Tancreto, J., Meyers, G., Johnson, F., Hopkins, J.,
Nickerson, H., and Armstrong, W., NCEL Products Supporting DOD Revision of NAVFAC P-397, Program No. Y0995-01-003-201, Technical Memorandum 2591TM, sponsored by Naval Facilities Engineering Command, Alexandria, Virginia, and Naval Civil Engineering Laboratory,
Port Hueneme, California, March 1983.


<!-- batch 10 | page 63 -->

32.Kingery, C.N., and Bulmash G., Airblast Parameters from TNT Spherical Air Burst and Hemispherical Surface Burst, Technical Report ARBRL-TR02555, prepared by U.S. Army Armament Research and Development Center, Ballistic Research Laboratory, Aberdeen Proving Ground,Maryland, April 1984.
33.Kingery, C. N. and Coulter G. A., Reflected Overpressure Impulse on a Finite Structure, Technical Report ARBRL-TR-02537. prepared by U. S.
Army Armament Research and Development Center, Ballistic Research Laboratory, Aberdeen Proving Ground Maryland, December 193.34.Kingery, C. N. and Coulter G. A., Enhanced Blast as a Function of Multiple Detonations and Shape for Bare Pentolite Charges, Memorandum Report BRL-MR-3539, prepared by U.S. Army Ballistic Research Laboratory,
Aberdeen Proving Ground, Maryland, July 1986.
35.Kingery, C. N., Bulmash G., and Muller P., Blast Loading on Above Ground Barricaded Munition Storage Magazines, Technical Report ARBLTR-02557, prepared by U.S. Army Armament Research and Development Center, Ballistic Research Laboratory, Aberdeen Proving Ground,
Maryland, May 1984.
36.Kriebel, A.R., Air Blast in Tunnels and Chambers, Final Report DASA 1200-11, Supplement 1, Prepared for Defense Civil Preparednes Agency, URS Research Company, San Mateo, California, September 1972.
37.Makino, R. The Kirkwood-Brinkley Theory of the Propagation of Spherical Shock Waves and Its Comparison With Experiment, BRL Report 750,
Aberdeen Proving Ground, Maryland, April 1951.38.Mclntyre, F. L., TNT Equivalency Test Results of Selected High Explosives, Propellants, and Pyrotechnics in Surface Burst Configurations,
Contractor Report, Prepared by Technical Services Laboratory, National Space Technology Laboratories, NSTL MS 39529, for U.S. Army Research and Development Engineering Center, Dover, New Jersey,
Sponsored by U.S. Army - AMCCOM, July 1986.39.Melichar, J. F., The Propagation of Blast Waves Into Chambers, BRL Memorandum Report 1920, Aberdeen Proving Ground, Maryland, March 1968.
40.Olson, W.C., Patterson, J. D.II, and Williams, J. S., The Effect of Atmospheric Pressure on the Reflected Impulse From Blast Waves, BRL Memorandum Report 1241, Aberdeen Proving Ground, Maryland, January 1960.


<!-- batch 10 | page 64 -->

41.Reeves H., and Robinson W. T., Hastings Igloo Hazards Tests for Small Explosive Charges, Memorandum Report ARBL-MR-03356, prepared by U. S. Army Armament Research and Development Center, Ballistic Research Laboratory, Aberdeen Proving Ground, Maryland, May 1984.42.Reisler, R. E., Kennedy, L. W., and Keefer, J. H., High Explosive MultiBurst Air Blast Phenomena (Simultaneous and Non-Simultaneous Detonations), BRL Technical Report ARBRL-TR-02142, Aberdeen Proving Ground, Maryland, February 1979.
43.Sachs, R. G., The Dependence of Blast on Ambient Pressure and Temperature, BRL Report 466, Aberdeen Proving Ground, Maryland,
1944.
44.Shear, R. E., Incident and Reflected Blast Pressures for Pentolite, BRL Report 1262, Aberdeen Proving Ground, Maryland, September 1964.45.Shear, R. E. and McCane, P., Normally Reflected Shock Front Parameters, BRL Memorandum Report 1273, Aberdeen Proving Ground,
Maryland, May 1960.
46.Swisdak, M.M., Jr., Explosion Effects and Properties: Part I- Explosion Effects in Air, NSWC/WOL/TR 75-116, Naval Surface Weapons Center,
White Oak, Silver Spring, Maryland, October 1975.47.The Effects of Nuclear Weapons, S. Glastone, Editor, U. S. Atomic Energy Commission, Washington, D. C., (Revised Edition), 1964.48.Voltz, R. D., and Kiger, S. A., An Evaluation of the Separated Bay Concept for a Munition Assembly Complex; An Experimental Investigation of the Department of Energy Building 12-64 Complex, Technical Report SL-83-6, prepared by Structures Laboratory, U.S. Army Engineer Waterways Experiment Station, Vicksburg, Mississippi, for Department of Energy, Albuquerque Operations, Amarillo, Texas, September 1983.49.Ward, J. M. (DOD Explosives Safety Board), Swisdak, M. M., Jr.,
Peckham P. J., and Soper W. G. (NSWC), Lorenz R. A. (Boeing Military Air-craft Company), Modeling of Debris and Airblast Effects from Explosions inside Scaled Hardened Aircraft Shelters, Final Report NSWC TR 85-470, prepared by Naval Surface Weapons Center, Silver Spring,
Maryland, May 1985.
50.Warnecke, C. Data Report: Support Test Evaluation of a Pre-Engineered Building, TECOM Project No. 2-CO-PIC-004, U.S. Army Dugway Proving Ground, Dugway, Utah, June 1977.
51.Wenzel, A. B. and Esparza, E. D., Measurements of Pressures and Impulses at Close Distances From Explosive Charges Buried and in Air,

<!-- batch 10 | page 65 -->

Final Report on Contract No. DAAK02-71-C-0393 with U.S. Army MERDC, Fort Belvoir, Virginia, 1972.
52.Wilton, C. and Gabrielsen, B. L., Shock Tunnel Tests of Preloaded and Arched Wall Panels, Final Report URS 7030-10, prepared for Defense Civil Preparedness Agency, URS Research Company, San Mateo,
California, June 1973.
53.Wilton, C. and Gabrielsen, B. L., Shock Tunnel Tests of Wall Panels Technical Report, Volume I, Test Information and Analysis, URS 7030-7,
prepared for Defense Civil Preparedness Agency, URS Research Company, San Mateo, California, January 1972.
54.Wilton, C., Kaplan, K., and Gabrielsen, B.L., The Shock Tunnel: History and Results, Volume II - Loading Studies, Final Report SSI 7618-1,
prepared for Defense Civil Preparedness Agency, Scientific Service, Inc,
Redwood City, California, March 1978.
55.Zaker, T. A., Blast Pressures From Sequential Explosions, Phase Report II, Project J6166, IIT Research Institute, Chicago, Ilinois, March 25, 1969.PRIMARY AND SECONDARY FRAGMENTS 56.Amos, C. W., Fragment Resistance of Martensitic Steel Sheets (U), AMRA TR-64-01, (CONFIDENTIAL), U.S. Army Materials Research Agency,
Watertown, Massachusetts, January 1964.
57.Apgar, J. W., Reaction of Mild Steel Targets to Exploding Munitions (U),
U.S. Army Ballistic Research Laboratories, Aberdeen Proving Ground,
Maryland (CONFIDENTIAL), October 1967.
58.Baker, W. E., Non-Nuclear Weapons Effects on Protective Structures (U),
AFWL-TR-67-133 (SECRET), Mechanics Research, Inc., Houston, Texas,
for U.S. Air Force Weapons Laboratory, January 1969.59.Beth, R. A., Final Report on Concrete Penetration, Report No A-388,
National Defense Research Commitee, Office of Scientific Research and Development, March 1946.
60.Bulmash, G., Kingery C.N., and Coulter, G.A., Velocity Measurements of Acceptor Wall Fragments From the Mass Detonation of Neighboring Above-Ground Barricaded Munition Storage Magazine Model, Technical Report BRL-TR-2719, prepared by U.S. Army Ballistic Research Laboratory, Aberdeen Proving Ground, Maryland, March 1986.61.Cohen, E. and Dobbs N., Design Procedures and Details for Reinforced Concrete Structures Utilized in Explosive Storage and Manufacturing Facilities, Ammann and Whitney, Consulting Engineers, New York, New York, Annals of the New York Academy of Sciences, Conference on 
EM 

<!-- batch 10 | page 66 -->

Prevention of and Protection Against Accidental Explosion of Munitions,Fuels and Other Hazardous Mixtures, Vol. 152, Art. 1, 1968.62.Doyle, J.M., Klein, M.J. and Shah, H., Desiqn of Missile Resistant Concrete Panels, Preprints of the 2nd International Conference on Structural Mechanics in Reactor Technology, Vol. 4, Commission of the European Communities, Brussels, 1973, Paper No. J 3/3.63.Effects of Impact and Explosion, Volume 1, Office of Scientific Research and Development, National Defense Research Committee, Washington,D.C., 1946.
64.Fundamentals of Protective Design for Conventional Weapons, prepared by U.S. Army Engineer Waterways Experiment Station, Vicksburg,
Mississippi, for Office, Chief of Engineers, U.S. Army, Washington, D.C.,
July 1984.
65.Gewaltney, R. C., Missile Generation and Protection in Light-WaterCooled Power Reactor Plants, Nuclear Safety, 10(4): July-August 199.66.Giere, A. C., Calculating Fraqment Penetration and Velocity Data for Use in Vulnerability Studies, NAVORD Report 6621, U.S. Naval Nuclear Evaluation Unit, Albuquerque, New Mexico, October 1959.67.Gurney, R. W., The Initial Velocities of Fragments from Bombs, Shells and Grenades, Report No. 405, Ballistic Research Laboratories, Aberdeen Proving Ground, Maryland, September 1943.
68.Gurney, R. W., The Mass Distribution of Fragments from Bombs, Shells and Grenades, Report No. 448, Ballistic Research Laboratories, Aberdeen Proving Ground, Maryland, February 1944.
69.Healey, J. J., and Weissman, S., Primary Fragment Characteristics and Impact Effects in Protective Design, Minutes of the Sixteenth Explosive Safety Seminar, September 1974.
70.Hoffman, P.R., McMath, R.R., and Migotsky, E., Projectile Penetration Studies, AFWL Technical Report No. WL-TR-64-102, Avco Corporation for the Air Force Weapons Laboratory, Kirtland Air Force Base, December 1964.
71.Industrial Enqineering Study to Establish Safety Desiqn Criteria for Use in Enqineering of Explosive Facilities and Operations, Ammann and Whitney,
Consulting Engineers, New York, New York, Report for Picatinny Arsenal,
Dover, New Jersey, April 193.
72.Johnson, C. and Moseley, J.W., Preliminary Warhead Terminal Ballistic Handbook. Part 1: Terminal Ballistic Effects, NAVWEPS Report No. 773,
U.S. Naval Weapons Laboratory, Dahlgren, Virginia, March 1964.

<!-- batch 10 | page 67 -->

73.Kolsky, H., Stress Waves in Solids, Dover Publications, New York, New York, 1963.
74.Kymer, J.R., Penetration Performance of Arrow Type Projectiles, Report R-1814, U.S. Army Frankford Arsenal, Philadelphia, Pennsylvania, May 1966.
75.Mott, R.I., A Theoretical Formula for the Distribution of Weights of Fraqments, AC-3642 (British). March 1943.
76.Mott, R.I., A Theory of Fragmentation, Army Operational Research Group Memorandum, 113-AC-6427, Great Britain, 1943.77.Non-Nuclear Weapons Effects on Protective Structures (U), Technical Report No. AFWL-TR-69-57, Air Force Weapons Laboratory, Kirtland Air Force Base, December 1964.
78.Non-Nuclear Weapons Effects on Protective Structures (U), Technical Report No. AFWL-TR-69-57, (SECRET), Mechanics Research, Inc., for the Air Force Weapons Laboratory, Kirtland Air Force Base, September 1969.
79.Recht, R.,et al., Application of Ballistic Perforation Mechanics to Target Vulnerability and Weapons Effectiveness Analysis (U), NWC TR 4333(CONFIDENTIAL), Denver Research Institute for the Naval Weapons Center, China Lake, California, October 1967.
80.Reeves H., and Robinson W. T., Hastings Igloo Hazards Tests for Small Explosive Charges, Memorandum Report ARBL-MR-03356, prepared by U.S. Army Armament Research and Development Center, Ballistic Research Laboratory, Aberdeen Proving Ground, Maryland, May 1984.81.Rinehart, J. S. and Pearson, J., Behavior of Metals Under Impulsive Loads, The American Society of Metals, Cleveland, Ohio, 1954.82.Robertson, H. P., Terminal Ballistics, Preliminary Report, Committee on Passive Protection Against Bombing, National Research Council, January 1941.
83.Sterne, T. E., A Note on the Initial Velocities of Fragments from Warheads, Report No. 648, Ballistic Research Laboratories, Aberdeen Proving Ground, Maryland, September 1947.
84.Thomas, L. H., Computing the Effect of Distance on Damage by Fragments, Report No. 468, Ballistic Research Laboratories, Aberdeen Proving Ground, Maryland, May 1944.
85.Voltz, R.D., and Kiger, S.A., An Evaluation of the Separated Bay Concept for a Munition Assembly Complex; an Experimental Investigation of the 

<!-- batch 10 | page 68 -->

Department of Energy Building 12-64 Complex, Technical Report SL-83-6,prepared by Structures Laboratory, U. S. Army Engineer Waterways Experiment Station, Vicksburg, Mississippi, for Department of Energy,Albuquerque Operations, Amarillo, Texas .



Ward, J. M. (DOD Explosives Safety Board), Swisdak, M. M., Jr.,Peckham, P. J., and Soper, W.G.(NSWC), Lorenz, R. A.(Boeing Military Aircraft Company). Modeling of Debris and Airblast Effects from Explosions Inside Scaled Hardened Aircraft Shelters, Final Report NSWC TR 85-470, prepared by Naval Surface Weapons Center, Silver Spring,Maryland, May 1985.



## SHOCK LOADS 

87.American Society of Civil Engineers (ASCE), A Comparative Study of Structural Response to Explosion-Induced Ground Motions, ASCE, New York, New York, 1975.
88.Auld, H. E., A Study of Air-Blast-Induced Ground Motions, Ph.D. Thesis,
University of Ilinois, May 197.
89.Baladi, G.Y., and P. F. Hadala, Ground Shock Calculation Parameter Study Report I Effect of Various Nonlinear Elastic Plastic Model Formulations, Waterways Experiment Station Technical Report S-71-4,
April 1971.
90.Ballard, R. F., R. E. Leach, Middle North Series, Mixed Company Event,
Strong Motion Seismic Measurements, Defense Nuclear Agency Report POR-6746, July 25, 1973.
91.Barkan, D. D., Dynamics of Bases and Foundations, McGraw Hill Book Co., New York, New York 1962.
92.Baron, M. L., A Summary of Some Analytical Studies on Air Blast Induced Ground Motions, Defense Atomic Support Agency Report 2634, March 1971.
93.Baron, M. L., I. Nelson, and I. Sandler, Investigation of Air Induced Ground Shock Effect Resulting from Various Explosive Sources, Report 2Influence of Constitutive Models on Ground Motion Predictions,
Waterways Experiments Station Contract Report S-71-10, November 1971.
94.Batchelder, F. E., et al., Hardness Program - Non-EMP, Hardness Program Plan for Safeguard Ground Facilities, Vol. 1, Management and Technical Plan, U. S. Army Corps of Engineers, Huntsville Division,
HNDDSP-73-153-ED-R, August 16, 1974.


<!-- batch 10 | page 69 -->

95.Carder, D. S., and W.K. Cloud. Surface Motion from Large Underground Explosions, J. Geophys, Res., 64, 1471-1487, 1959.96.Carnes, B. L., and J.A. Conway. Mine Throw I: Cratering Effects of a Multiton Near Surface Detonation in Desert Alluvium, Waterways Experiment Station Technical Report N-73-3, May 1973.97.Christensen, W. J., Air Blast Induced Ground Shock, Navy Bureau of Yards and Decks Technical Study 27, September 1959.98.Cooper, H. Jr., and J.L. Braton, Calculation of Vertical Airblast-Induced Ground Motions from Nuclear Explosions in Frenchman Flat, Air Force Weapons Laboratory Report AFWL-TR-73-111, October 1973.99.Cooper, H. F., Jr., Empirical Studies of Ground Shock and Strong Motions in Rock, Defense Nuclear Agency Report 3245F, October 1973.100.Crandell, F. J., Ground Vibrations Due to Blastinq and Its Effect Upon Structures, Journal Boston Soc., Civil Engineers, Vol. 36, p. 245, 1949.101.Crandell, F. J., Transmission Coefficient for Ground Vibrations Due to Explosions, J. Boston Soc. Civil Engineering, 47, 152-168, 1960.102.Crawford, R. E., C. J. Higgins, and E. H. Bultmann. Air Force Manual for Design and Analysis of Hardened Structures, Air Force Weapons Laboratory Report AFWL-TR-74-102, October 1974.103.Day, J. D., H. J. Stout, and D. W. Murrell, Middle Gust Calibration Shots:Ground Motion Measurements, Waterways Experiment Station Technical Report N-75-1, February 1975.
104.Duvall, Wilbur I. and D.E.Fogelson, Review of Criteria for Estimating Damage to Residences from Blasting Vibrations, Bureau of Mines Report of Investigation 5968, 1962.
105.Dvorak, A., Seismic Effects of Blasting on Brick Houses, Proce Geofyrikeniha Ustance Ceskoslavenski Akademie, Vol. No. 169,
Geofyskialni Sbornik, pp. 189-202, 1962.
106.Edwards, A.T. and T. D. Northwood, Experimental Studies of the Effects of Blasting on Structures, The Engineer, V. 210, pp. 538-546, September 30,1960.
107.Eubanks, R. A. and B. R. Juskie, Shock Hardening of Equipment, Shock and Vibrations Bulletin, No. 32, Part II, December 1963.108.Galbraith, F.W., Operation Distant Plain Final Report Proj. 3.02b Shock Spectrum Measurements, TRW Systems Group Report 05318-6001R000, January 1968.


<!-- batch 10 | page 70 -->

109.Galbraith, F.W., Operation Prairie Flat, Proj. LN-306 Shock Spectrum Measurements, Defense Atomic Support Agency Report POR-2107,February 1970.
110.Grubaugh, R. E., and L. E. Elliot, Scaling of Ground Shock Spectra,
Defense Atomic Support Agency Report DASA-1921, February 1967.111.Habberjam, G. M. and J. T. Whetton, On the Relationship Between Seismic and Amplitude and Charge of Explosive Fired in Routine Blasting Operations, Geophysics 17. 116-128, January 1952.112.Hendron, A. J. Jr., Correlation of Operation Snowball Ground Motions with Dynamic Properties of Test Site Soils, Waterways Experiment Station Miscellaneous Paper l-745. October 1965.
113.Hoffman, H. V., F. M. Sauer, and B. Barclay, Operation Prairie Flat, Proj.
LN-308 Strong Ground Shock Measurements, Defense Atomic Support Agency Report POR-2108, April 1971.
114.Hudson, D. E., J. L. Alford, and W.D.Iwan, Ground Accelerations Caused by Large Quarry Blasts, Bull. Seismic Soc., A, 51, 191-202, 1961.115.Ichiro, I., On the Relationship Between Seismic Ground Amplitude and the Quantity of Explosives in Blasting, Reprint from Memoirs of the Faculty of Engineering, Kyoto University, 15, 579-587, 153.116.Ingram, J. K. Project Officer's Final Report Operation Distant Plain Events 1, 2A, 3, 4, and 5, Proj. 3.02A Earth Motion and Stress Measurements,
Waterways Experiment Station Technical Report N-71-3, May 1971.117.Ingram, L. F., Ground Motions from High Explosive Experiments,
Waterways Experiment Station Miscellaneous Paper N-72-10, December 1972.
118.Jaramillo, E. E., and R. E. Pozega, Middle Gust Free-Field Data Analysis,
Air Force Weapons Laboratory Report AFWL-TR-73-251, April 1974.119.Joachim, C. E., Mine Shaft Series, Events Mine Under and Mine Ore;
Ground Motion and Stress Measurements, Waterways Experiment Station Technical Report N-72-1, January 1972.
120.Kennedy, T. E., In-Structure Motion Measurements, Proj. LN-315Operation Prairie Flat, Waterways Experiment Station Technical Report N70-11, July 1970.
121.Kochly, J.A., and T.F. Stubbs, Mine Shaft Series, Mineral Rock Particle Velocity Measurements from a 100-ton TNT Detonation on Granite,
Defense Nuclear Agency Report POR-2162, May 24, 1971.

<!-- batch 10 | page 71 -->

122.Lamb, H., On the Propagation of Tremors Over the Surface of an Elastic Solid, Philosophical Transactions of Royal Society London, Series A,Volume 203, September 1904.
123.Langefors, Ulf, B. Kihlstron, and H. Westerberg, Ground Vibrations in Blasting, Water Power, pp. 335-338, 390-395, 421-424, February 198.124.Lockard, D. M., Crater Parameters and Material Properties, Air Force Weapons Laboratory Report AFWL-TR-74-200, October 1974.125.Meireis, E. C. and A. R. Wright, Hardness Program - No-EMP, Hardness Program Plan for Safeguard Ground Facilities, Vol. 2, Safeguard Structures and TSE Description, U.S. Army Corps of Engineers, Huntsville Division, HNDDSP-73-153-ED-R, November 1973.126.Morris, G., The Reduction of Ground Vibrations from Blasting Operations,
Engineering, pp. 460-465, April 1957.
127.Morris, W. E., and others, Operation Jangle Blast and Shock Measurements I, Armed Forces Special Weapons Project Report WT 366, June 1952.
128.Murphey, B. F., Particle Motions Near Explosions in Halite, Journal of Geophysical Research, Vo. 66, No. 3, March 1961, pp. 947-958.129.Murrell, D. W., Operation Mine Shaft, Mineral Rock Event, Far-out Ground Motions From a 100-ton Detonation on Granite, Waterways Experiment Station Technical Report N-72-6, April 1972.
130.Murrell, D. Operation SNOWBALL, Project 3.6 - Earth Motion Measurements, Waterways Experiment Station Technical Report TR 1759. March 1967.
131.Newmark, N. M., and others, Air Force Design Manual Principles and Practices for Design of Hardened Structures, Air Force Special Weapons Center Report AFSWC-TDR-62-138, December 192.132.Nicholls, H.R., C.F. Johnson, and W. I. Duvall, Blasting Vibrations and Their Effects on Structures, Bureau of Mines Bulletin 656, 1971.133.Odello, R. and P. Price, Ground Shock Effects from Accidental Explosions, Picatinny Arsenal Technical Report 4995, November 1976.134.Palaniswamy, K., and J. L. Merritt, Evaluation of Middle Gust Data:
Acoustic Path Length Scaling of Peak Velocities, Space and Missile Systems Organization Report 72-006-T4, November 1973.

<!-- batch 10 | page 72 -->

135.Parsons, R. M., and others, Guide for the Design of Shock Isolation Systems for Underground Protective Structures, Air Force Special Weapons Center Report AFSWC-TDR-62-64, October 1962.136.Phillips, B.R., and G.Y. Baladi, Results of Two Free-Field Code Calculations Versus Field Measurements for the Distant Plain 1A Event,Waterways Experiment Station Miscellaneous Paper S-73-21, April 1973.137.Proceedings of the Mixed Company/Middle Gust Results Meeting 13-15March 1973, Vol. II. Edited by General Electric-Tempo, Defense Nuclear Agency Report 3151-P2, May 1973.
138.Rausch, Maschinenfundamente Und Andere Dynamische Bauaufgaben,
Vertrieb VDE Verlag G.M.B.H. (Berlin), 1943.
139.Reiher, H. and F. J. Meister, Die Empfindlichkeit der Menschen gegen Erschutterungen, Forsch. Gebiete Ingenieur wesen, Vol. 2, No. 11, pp.
381-386, 1931.
140.Richart, F.E. Jr., J. R. Hall, and R. D. Woods, Vibration of Soils and Foundations, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1970.141.Ricker, N., The Form and Nature of Seismic Waves and the Structure of Seismograms, Geophysics, 5, 348-366, 1940.
142.Sachs, D. C., and C. M. Swift, Small Explosion Tests, Project Mole, Armed Forces Special Weapons Project Report 291, Vols. Iand II, December 1955.
143.Sager, R. A., Concrete Arch Studies, Proj. 3.2, Operation Snowbal,
Waterways Experiment Station Miscellaneous Paper I-736, August 1965.144.Sandler, I.S., J. P. Wright, and M. L. Baron, Ground Motion Circulations for Events Il and Il of the Middle Gust Series, Defense Nuclear Agency Report DNA 3290T, April 1974.
145.Steffens, R. J., The Assessment of Vibration Intensity and its Application to the Study of Building Vibrations, National Building Studies Special Report No. 19, Department of Scientific and Industrial Research, Building Research Station, London, England, 1952.
146.Sauer, F. M., and C. T. Vincent, Ferris Wheel Series - Flat Top Event Earth Motion and Pressure Histories, Defense Atomic Support Agency Report Ferris Wheel POR-3002, April 197.
147.Sauer, F. M., editor, Nuclear Geoplosics, A Sourcebook of Underground Phenomena and Effects of Nuclear Explosions, in 5 parts, Defense Atomic Support Agency Report DASA-1285, May 1964.


<!-- batch 10 | page 73 -->

148.Sauer, F. M., Summary Report on Distant Plain Events 6 and 1a Ground Motion Experiments, Defense Atomic Support Agency Report DASA-2587,October 1970.
149.Teichmann, G. A. and R. Westwater, Blasting and Associated Vibrations,
Engineering, pp. 460-465. April 1957.
150.Thoenen, J. R., and S. L. Windes, Seismic Effects of Quarry Blasting,
Bureau of Mines Bulletin, 442, 83, 1942.
151.URS/John A. Blume and Associates, Seismic Hazard and Building Structure Behavior at the Pantex Facility, April 1976.152.Vincent, C. T., Operation Prairie Flat, Proj. LN-304 Earth Pressure and Ground Shock Profile Measurements, Defense Atomic Support Agency Report POR-2113, May 1969.
153.Weidlinger, P., and A. Matthews, A Method for the Prediction of Ground Shock Phenomena in Soils, Air Force Special Weapons Center Report AFSWC-TDR-61-66, March 1962.
154.Westline, P. S., Esparza, E. D., and Wenzel, A. B., Analysis and Testing of Pipe Response to Buried Explosive Detonations, SwRI Final Report for American Gas Association, July 1978.
155.Willis, D. E. and J. T. Wilson, Maximum Vertical Ground Displacement of Seismic Waves Generated by Explosive Blasts, Bulletin Seismic Safety of America, 50, 455-459, 1960.
156.Zaccor, J. V., Procedures for Prediction of Ground Shock Phenomena Based on One-Dimensional Shock Propagation Considerations:
Procedures and Applications, Waterways Experiment Station Contract Report 3-171. April 1967.
157.Zolasko, J. S., and G. Y. Baladi, Free-Field Code Predictions Versus Field Measurements: A Comparative Analysis for the Prairie Flat Event,
Waterways Experiment Station Miscellaneous Paper S-71-6, March 191.