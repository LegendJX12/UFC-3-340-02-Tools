

<!-- batch 28 | page 1 -->

## DESIGN OF PLATES 

## 5 -27GENERAL

The emphasis in this section is on the dynamic plastic design of plates. As in the case for simply supported and continuous beams, design data have been derived from the static provisions of the AiSC Specification with necessary modifications and additions for blast design.



This section covers the dynamic flexural capacity of plates, as well as the necessary information for determining the equivalent bilinear resistance-deflection functions used in evaluating the flexural response of plates. Also presented is the supplementary consideration of adequate shear capacity at negative yield lines.

## 5 -28DYNAMIC FLEXURAL CAPACITY

As is the case for standard l-shaped sections, the ultimate dynamic moment-resisting capacity of a steel plate is a function of the elastic and plastic moduli and the dynamic design stress. For plates or rectangular cross section beams, the plastic section modulus is 1.5 times the elastic section modulus.



A representative moment-curvature relationship for a simply-supported steel plate is shown in Figure 5-10 (+). The behavior is elastic until a curvature corresponding to the yield moment $M_{v}$ is reached. With further increase in load, the curvature increases at a greater rate as the fully plastic moment value,$M_{2},$ is approached. Following the attainment of $M_{2}$ , the curvature increases while the moment remains constant.

For plates and rectangular cross section beams,$M_{2}$ is 50 percent greater than $M_{v},$ and the nature of the transition from yield to the fully plastic condition depends upon the plate geometry and end conditions. It is recommended that a capacity midway between $M_{v}$ and $M_{2}$ be used to define the plastic design moment,$M_{p}(M_{1}$ in Figure 5-11 (+)), for plates and rectangular cross section beams. Therefore, for plates with any ductility ratio,Equation 5-7 applies.



## 5 -29

## RESISTANCE AND STIFFNESS FUNCTIONS

Procedures for determining stiffness and resistance factors for one- and two-way plate elements are outlined in Chapter 3. These factors are based upon elastic deflection theory and the yield-line method, and are appropriate for defining the stiffness and ultimate load-carrying capacity of ductile structural steel plates. In applying these factors to steel plates, the modulus of elasticity should be taken equal to 29,000,000 psi. For two-way isotropic steel plates, the ultimate unit positive and negative moments are equal in all directions; i.e.



$$M_{v n}=M_{v o}=M_{h n}=M_{h o}=M_{o}$$

where $M_{P}$ is defined by Equation 5-7 and the remaining values are ultimate unit moment capacities as defined in Section 3-9.3 of Chapter 3. Since the stiffness factors were 

<!-- batch 28 | page 2 -->

derived for plates with equal stiffness properties in each direction, they are not applicable to the case of orthotropic steel plates, such as stffened plates, which have different stiffness properties in each direction.



## 5 -30DESIGN FOR FLEXURE

The procedure for the flexural design of a steel plate is essentially the same as the design of a beam. As for beams, it is suggested that preliminary dynamic load factors listed in Table 5-4 (+) be used for plate structures. With the stifness and resistance factors from Section 5-29 and taking into account the influence of shear on the available plate moment capacity as defined in Section 5-31, the dynamic response and rebound for a given blast loading may be determined from the response charts in Chapter 3. It should be noted that for $\mu\geq10$ , the dynamic design stress, incorporating the dynamic ultimate stress,$\pmb{f}_{d u}$ , may be used (see Equation 5-2).



## 5 -31DESIGN FOR SHEAR

In the design of rectangular plates, the effect of simultaneous high moment and high shear at negative yield lines upon the plastic strength of the plate may be significant. In such cases, the following interaction formula describes the effect of the support shear,V, upon the available moment capacity, M:

$$M/M_{p}=1-(V/V_{p})^{4}$$

where $M_{P}$ is the fully plastic moment capacity in the absence of shear calculated from Equation 5-7, and $\dot{V}_{p}$ is the ultimate shear capacity in the absence of bending determined from Equation 5-16 where the web area,$A_{w},$ is taken equal to the total cross sectional area at the support.



For two-way elements, values for the ultimate support shears which are applicable to steel plates are presented in Table 3-10 (+) of Chapter 3.



It should be noted that, due to the inter-relationship between the support shear, V, the unit ultimate flexural resistance,$r_{u},$ of the two-way element, and the fully plastic moment resistance,$M_{p},$ ,the determination of the resistance of steel plates considering Equation 5-23, is not a simple calculation. Fortunately, the number of instances when negative yield lines with support shears are encountered for steel plates will be limited. Moreover,in most applications, the $V/V_{p}$ ratio is such that the available moment capacity is at least equal to the plastic design moment for plates (Equation 5-7).



It is recommended that for a $V/V_{p}$ ratio on negative yield lines less than 0.67, the plastic design moment for plates, as determined from Equation 5-7, should be used in design.However, if $V/V_{p}$ is greater than 0.67, the influence of shear on the available moment capacity must be accounted for by means of Equation 5-23.



<!-- batch 28 | page 3 -->

<div style="text-align: center;">Figure 5-10Moment-Curvature Diagram for Dynamically Loaded Plates and Rectangular Cross-Section Bases </div>


$$M_{p}=M_{1}=f_{ds}\left(\frac{s+z}{2}\right)$$

<div style="text-align: center;">Table 5-4Preliminary Dynamic Load Factors for Plates </div>


## *Whichever governs 

## SPECIAL CONSIDERATIONS, BEAMS 

## UNSYMMETRICAL BENDING

### 5 -32.1General

In blast design, the number of situations where unsymmetrical bending occurs is limited and where encountered, it can be treated without serious economic penalty. Due to the fact that blast overpressure loads act normal to the surfaces of a structure, the use of doubly-symmetric cross sections for purlins and girts (e.g., hot-rolled S- and W-sections or cold-formed channels used back-to-back) is generally recommended. In such cases,the deformation criteria for flexural members in Section 5-22 apply.

<!-- batch 28 | page 4 -->

Unsymmetrical bending occurs when flexural members are subjected to transverse loads acting in a plane other than a principal plane. With this type of loading, the following are applicable:

(1)The member's neutral axis is not perpendicular to the plane of loading.

(2)Stresses cannot in general be calculated by means of the simple bending formula (Mc/1).



(3)The bending deflection does not coincide with the plane of loading but is perpendicular to the inclined neutral axis.



(4)If the plane of loads does not pass through the shear center of the cross section, bending is also accompanied by twisting.

Doubly-symmetric S, W, and box sections acting as individual beam elements and subjected to biaxial bending, i.e., unsymmetrical bending without torsion, can be treated using the procedures outlined in the following sections.



### 5 -32.2Elastic and Plastic Section Modulus

The inclination of the elastic and plastic neutral axis through the centroid of the section can be calculated directly from the following relationship (see Figure 5-11 (+)):

tan $\alpha=(I_{x}\Lambda_{y})$ tan φ

where 

α =angle between the horizontal principal plane and the neutral axis 

$\phi=a n g I$ 'e between the plane of the load and the vertical principal plane 

where and x and y refer to the horizontal and vertical principal axes of the cross section.The equivalent elastic section modulus may be evaluated from the following equation:

$$S=(S_{x}S_{y})/(S_{y}\cos\phi+S_{x}\sin\phi)$$

where 

$\begin{array}{r}{\mathcal{S}_{x}=}\\ {\mathcal{S}_{y}=}\end{array}$ elastic section modulus about the x-axis elastic section modulus about the y-axis 

<!-- batch 28 | page 5 -->

The plastic section modulus can be calculated using Equation 5-6. With these values of the elastic and plastic section moduli, the design plastic moment capacity can be determined from Equation 5-7.



### 5 -32.3Equivalent Elastic Stiffness

In order to define the stiffness and bilinear resistance function, it is necessary to determine the elastic deflection of the beam. This deflection may be calculated by resolving the load into components acting in the principal planes of the cross section.The elastic deflection,,$\delta,$ is calculated as the resultant of the deflections determined by simple bending calculations in each direction (see Figure 5-11 (+)). The equivalent elastic deflection on the bilinear resistance function $X_{E}$ , may then be determined by assuming that the elastic stiffness is valid up to the development of the design plastic moment capacity,$M_{p}$ 



### 5 -32.4Lateral Bracing and Recommended Design Criteria

The bracing requirements of Section 5-26 may not be totally adequate to permit a biaxially loaded section to deflect into the inelastic range without premature failure.However, for lack of data, the provisions of Section 5-26 on lateral bracing may be used if the total member end rotation corresponding to the total deflection due to the inclined load is limited to 2 degrees. In addition, the actual details of support conditions and/or bracing provided to such members by the other primary and secondary members of the frame must be carefully checked to ensure that the proper conditions exist to permit deflections in the inelastic range.



### 5 -32.5Torsion and Unsymmetrical Bending

The inelastic behavior of sections subjected to unsymmetrical bending, with twisting, is not totally known at present. Consequently, the use of sections with the resultant load not passing through the shear center is not recommended in plastic design of blastresistant structures, unless torsional constraints are provided for the elements. In actual installations, however, the torsional constraint offered to a purlin or girt by the flexural rigidity of attached floor, roof, or wall panels may force the purlin or girt to deflect in the plane of loading with litle or no torsional effects. Under such conditions or when some other means of bracing is provided to prevent torsional rotation in both the loading and rebound phases of the response, such unsymmetrically loaded members may be capable of performing well in the plastic range. However, because of the limited data presently available, there is insufficient basis for providing practical design guidelines in this area. Hence, if a case involving unsymmetrical bending with torsion cannot be prevented in design, the maximum ductility ratio should be limited to 1.0.

Furthermore, special precautions may have to be taken to restrict the torsional-flexural distortions that can develop under unsymmetrical loading, thereby reducing the flexural capacity of the member.



<!-- batch 28 | page 6 -->

## 5 -33

## STEEL JOISTS AND JOIST GIRDERS (OPEN-WEB STEEL JOISTS)

Open-web joists are commonly used as load-carrying members for the direct support of roof and floor deck in buildings. The design of joists for conventional loads is covered by the "Standard Specifica33tions, Load Tables and Weight Tables for Steel Joists and Joist Girders," adopted by the Steel Joist Institute. For blast design, all the provisions of this Specification are in force, except as modified herein.



These joists are manufactured using either hot-rolled or cold-formed steel. H Series joists are composed of 50-ksi steel in the chord members and either 36 ksi or 50-ksi steel for the web sections. LH Series, DLH Series and joist girders are composed of joist chords or web sections with a yield strength of at least 36 ksi, but not greater than 50 ksi.



Standard load tables are available for simply supported, uniformly loaded joists supporting a deck and so constructed that the top chord is braced against lateral buckling. These tables indicate that the capacity of a particular joist may be governed by either flexural or shear (maximum end reaction) considerations. As discussed previously, it is preferable in blast applications to select a member whose capacity is controlled by flexure rather than shear, which may cause abrupt failure.

The tabulated loads include a check on the bottom chord as an axially loaded tensile member and the design of the top chord as a column or beam column. The widththickness ratios of the unstiffened or stiffened elements of the cross section are also limited to values specified in the Standard Specifications.



The dynamic ultimate capacity of open-web joists may be taken equal to 1.7 x SIF x DIF times the allowable design load given in the joist tables. This value represents the safety factor of 1.7 multiplied by a dynamic increase factor, DIF, and the average strength increase factor, SIF (see Section 5-12).



The adequacy of the section in rebound must be evaluated. Upon calculating the required resistance in rebound,$r/r_{u}$ ,using the rebound chart in Chapter 3 (Figure 3-268(+)), the lower chord must be checked as a column or beam column. If the bottom chord of a standard joist is not adequate in rebound, the chord must be strengthened either by reducing the unbraced length or by increasing the chord area. The top chord must be checked as an axial tensile member, but in most circumstances, it will be adequate.

The bridging members required by the joist specification should be checked for both the initial and rebound phase of the response to verify that they satisfy the required spacing of compression flange bracing for lateral buckling.



. In cases where the design of joists is governed by shear, the ductility ratio for the joist should not exceed unity. In addition, the joist members near the support should be investigated for the worst combination of slenderness ratio and axial load under load reversal.



<!-- batch 28 | page 7 -->

For hot-rolled members not limited by shear considerations, design ductility ratios up to the values specified in Section 5-35 can be used. The design ductility ratio of joists with light gauge chord members should be limited to 1.0.



The top and bottom chords should be symmetrical about a vertical axis. If double angles or bars are used as chord members, the components of each chord should be fastened together so as to act as a single member.



## SPECIAL CONSIDERATIONS, COLD-FORMED STEEL PANELS 

#### 5 -34BLAST RESISTANT DESIGN OF COLD-FORMED STEEL PANELS.5-34.1General

Studies on cold-formed panels have shown that the effective width relationships for cold-formed light gauge elements under dynamic loading do not differ significantly from the static relationships. Consequently, the recommendations presently contained in the American Iron and Steel Institute (AISl) Specifications are used as the basis for establishing the special provisions needed for the design of cold-formed panels subjected to blast loads. Some of the formulas of the Specification have been extended to comply with ultimate load conditions and to permit limited performance in the inelastic range.



Two main modes of failure can be recognized, one governed by bending and the other by shear. In the case of continuous members, the interaction of the two influences plays a major role in determining the behavior and the ultimate capacity. Due to the relatively thin webs encountered in cold-formed members, special attention must also be paid to crippling problems. Basically, the design will be dictated by the capacity in flexure but subject to the constraints imposed by shear resistance and local stability.

### 5 -34.2Resistance in Flexure

The material properties of the steel used in the production of cold-formed steel panels conforms to ASTM A446. This standard covers three grades (a, b, and c) depending on the yield point. Most commonly, panels are made of steel complying with the requirements of grade a, with a minimum yield point of 33 ksi and an elongation of rupture of 20 percent for a 2-inch gauge length. However, it is generally known that the yield stress of the material used in the manufacture of cold-formed panels generally exceeds the specified minimum yield stress by a significant margin; therefore, it is recommended that a design minimum yield stress of 40 ksi (corresponding to an average strength increase factor of $S I F=1.21)$ , be used unless the actual yield stress of the material is known. For grades b and c which exhibit higher minimum yield points, an average strength increase factor of 1.21 is also recommended.

In calculating the dynamic yield stress of cold-formed steel panels, it is recommended that a dynamic increase factor, DlF, of 1.1 be applied irrespective of actual strain rate and, consequently, the value of the dynamic design stress to be used is 

<!-- batch 28 | page 8 -->

$$f_{ds}=SIF\times DIF\times f_v=1.21\times1.1\times f_v=1.33f_v $$

and hence,$f_{d s}$ equals 44 ksi for the particular case of $f_{v}=33\;\mathrm{k s i}$ 

Ultimate design procedures, combined with the effective width concept, are used in evaluating the strength of cold-formed light gauge elements. Thus, a characteristic feature of cold-formed elements is the variation of their section properties with the intensity of the load. As the load increases beyond the level corresponding to the occurrence of local buckling, the effective area of the compression flange is reduced; as a result, the neutral axis moves toward the tension flange with the effective properties of the cross section such as A (area),  (moment of inertia) and S (section modulus)decreasing with load increase. The properties of the panels, as tabulated by the manufacturer, are related to different stress levels. The value of S referred to that of the effective section modulus at ultimate and the value of I related to a service stress level of 20 ksi. In the case of panels fabricated from hat sections and a flat sheet, two section moduli are tabulated,,$\mathcal{S}^{+}$ and S, referring to the effective section modulus for positive and negative moments, respectively. Consequently, the following ultimate moment capacities are obtained:

$$\begin{aligned}{M_{u p}}&{{}=f_{d s}S^{+}}\\ {M_{u n}}&{{}=f_{d s}S^{-}}\end{aligned}$$

where 

Mup = ultimate positive moment capacity for a 1-foot width of panel Mun = ultimate negative moment capacity for a 1-foot width of panel 

It should be noted that in cases where tabulated section properties are not available, the required properties may be calculated based upon the relationships in the AiSl Design Specification.



As for any single-span flexural element, the panel may be subjected to different end conditions, either simply supported or fixed. The fixed-fixed condition is seldom found in practice since this situation is difficult to achieve in actual installations. The simply fixed condition is found because of symmetry in each span of a two-span continuous panel.For multi-span members (three or more), the response is governed by that of the first span which is generally characterized by a simply supported condition at one support and a partial moment restraint at the other. Three typical cases can, therefore, be considerd:

(1)Simply supported at both ends (single span.

(2)Simply supported at one end and fixed at the other (two equal span continuous member).



<!-- batch 28 | page 9 -->

(3)Simply supported at one end and partially fixed at the other (first span of an equally spaced multi-span element.



The resistance of the panel is a function of both the strength of the section and the maximum moment in the member.



The ability of the panel to sustain yielding of its cross section produces significant moment re-distribution in the continuous member which results in an increase of the resistance of the panel.



The behavior of cold-formed steel sections in flexure is nonlinear as shown in Figure 5-12 (+). To simulate the bilinear approximation to the resistance-deflection curve, a factor of 0.9 is applied to the peak resistance. Therefore, for design purposes, the recommended resistance formula for a simply supported, single-span panel is given by:

$$r_{u}=0.9\times8M_{u p}/L^{2}=7.2M_{u p}/L^{2}$$

where $r_{u}$ is the resistance per unit length of panel, and L is the clear or effective span length.



The recommended resistance formula for a simply-fixed, single-span panel or first span of an equally spaced continuous panel is given by:

$$r_{u}=0.9\times4(M_{u n}+2M_{u o})/L^{2}=3.6(M_{u n}+2M_{u o})/L^{2}$$

### 5 -34.3Equivalent Elastic Deflection

As previously mentioned, the behavior of cold-formed sections in flexure is nonlinear as shown in Figure 5-12 (+).A billinear approximation of the resistance-deflection curve is assumed for design. The equivalent elastic deflection $X_{E}$ is obtained by using the following equation:

$$X_{F}=(\beta r_{u}L^{4})/E I_{20}$$

where $\beta$ is a constant which depends on the support conditions and whose values are as follows:

$$\begin{array}{r l}{\beta=}&{{}~0.0130\:{f o r\:a\:s i m p l y\:s u p p o r t e d\:e l e m e n t}}\\ {\beta=}&{{}~0.0062\:{f o r\:s i m p l y\:f i x e d\:o r\:c o n t i n u o u s\:e l e m e n t s}}\end{array}$$

$I_{20}$ is defined as the effective moment of inertia of the section at a service stress of 20ksi. The value of $I_{20}$ is generally tabulated as a section property of the panel. The value of $r_{u}$ is obtained from Equation 5-29 or 5-30.



<!-- batch 28 | page 10 -->

### 5 -34.4Design for Flexure

When performing a one-degree-of-freedom analysis of the panel's behavior, the properties of the equivalent system can be evaluated by using a load-mass factor,$K_{L M}=$ 0.74, which is an average value applicable to all support conditions. The natural period of vibration for the equivalent single-degree system is thus obtained by substituting into Equation 5-15:

$$T_{N}=2\pi(0.74m L/K_{E})^{1/2}$$

where 

$$\begin{array}{r l}{m=}&{{}w/g i s t h e u n i t m a s s o f t h e p a n e I}\\ {K_{E}=}&{{}r_{u}L/X_{E}i s t h e e q u i v a l e n t e l a s t i c s t i f f n e s s o f t h e s y s t e m}\end{array}$$

### 5 -34.5Recommended Ductility Ratios

Figure 5-12 (+) illustrates the nonlinear character of the resistance-deflection curve and the recommended bilinear approximation. The initial slope of the actual curve is fairly linear until it enters a range of marked nonlinearity and, finally, a point of instabillity.However, excessive deflections cause the decking to act as a membrane in tension (solid curve) and, consequently, a certain level of stability sets in. It should be noted that, in order to use the procedure outlined in this section, care must be taken to adequately connect the ends of the decking so that it can achieve the desired level of tension-membrane action. A discussion of connectors at end panels is presented in Section 5-48.When tension-membrane action is not present, increased deflection will result in a significant drop off in resistance as illustrated by the dotted curve in Figure 5-12.



Two limits of deformation are assigned, depending on end-anchorage condition of the panel. For panels having nominal end anchorage, that is, where tension-membrane action is minimal, the maximum deflection of the panel is $\mathsf{X}_{\circ}$ , as illustrated in Figure 5-12(+), and is defined by:

$$X_{o}=1.75X_{F}一一$$

For panels with sufficient end anchorage to permit tension-membrane action, the maximum deflection of the panel is $X_{m}$ ,as illustrated in Figure 5-12 (+), and is defined by:

$$X_{m}=6.0X_{F}$$

<!-- batch 28 | page 11 -->

### 5 -34.6Recommended Support Rotations

In order to restrict the magnitude of rotation at the supports, limitations are placed on the maximum deflections $\mathsf{X}_{\circ}$ and $\mathsf{X}_{\mathsf{m}}$ as follows:

For elements where tension-membrane action is not present:

$$X_{o}=L/92\;o r\;\Theta_{m a x}=1.25\;d e g r e e s $$

For elements where tension-membrane action is present:

$$X_{m}=L/29\;o r\;\Theta_{m a x}=4\;d e g r e e s $$

### 5 -34.7Rebound

Appropriate dynamic response charts for one-degree-of-freedom systems in the elastic or elasto-plastic range under various dynamic loads are given in Chapter 3. The problem of rebound should be considered in the design of decking due to the different section properties of the panel, depending on whether the hat section or the flat sheet is in compression. Figure 5-13 (+) presents the maximum elastic resistance in rebound as a function of $T/T_{N}$ . While the behavior of the panel in rebound does not often control, the designer should be aware of the problem; in any event, there is a need for providing connections capable of resisting uplift or pull-out forces due to load reversal in rebound.

### 5 -34.8Resistance in Shear

Webs with h/t in excess of 60 are in common use among cold-formed members and the fabrication process makes it impractical to use stiffeners. The design web stresses must, therefore, be limited to ensure adequate stability without the aid of stiffeners,thereby preventing premature local web failure and the accompanying loss of loadcarrying capacity.



The possibility of web buckling due to bending stresses exists and the critical bending stress is given by Equation 5-37:

$$f_{c r}=640,000/(h/t)^{2}\leq f_{v}$$

By equating $f_{c r}$ to 32 ksi, which is a stress close to the yielding of the material, a value $h/t=141$ is obtained. Since it is known that webs do not actually fail at these theoretical buckling stresses due to the development of post-buckling strength, it can be safely assumed that webs with $h/t\leq150$ will not be susceptible to flexural buckling. Moreover,since the AISl recommendations prescribe a limit of $h/t=150$ for unstiffened webs, this type of web instability need not be considered in the design.



<!-- batch 28 | page 12 -->

Panels are generally manufactured in geometrical proportions which preclude webshear problems when used for recommended spans and minimum support-bearing lengths of 2 to 3 inches. In blast design, however, because of the greater intensity of the loading, the increase in required flexural resistance of the panels requires shorter spans.



In most cases, the shear capacity of a web is dictated by instability due to either 

(1)Simple shear stresses 

(2)Combined bending and shearing stresses 

For the case of simple shear stresses, as encountered at end supports, it is important to distinguish three ranges of behavior depending on the magnitude of h/t. For large values of h/t, the maximum shear stress is dictated by elastic buckling in shear and for intermediate hlt values, the inelastic buckling of the web governs; whereas for very small values of h/t, local buckling will not occur and failure will be caused by yielding produced by shear stresses. This point is illustrated in Figure 5-14 (+) for $f_{d s}=44$ ksi.The provisions of the AISl Specification in this area are based on a safety factor ranging from 1.44 to 1.67 depending upon h/t. For blast-resistant design, the recommended design stresses for simple shear are based on an extension of the AlSl provisions to comply with ultimate load conditions. The specific equations for use in design for $f_{d s}=$ 44,66 and 88 ksi are summarized in Table 5-5a (+), Table 5-6a (+), and Table 5-7a (+)respectively.



At the interior supports of continuous panels, high bending moments combined with large shear forces are present, and webs must be checked for buckling due to these forces. The interaction formula presented in the AISl Specification is given in terms of the allowable stresses rather than critical stresses which produce buckling. In order to adapt this interaction formula to ultimate load conditions, the problem of inelastic buckling under combined stresses has been considered in the development of the recommended design data.



In order to minimize the amount and complexity of design calculations, the allowable dynamic design shear stresses at the interior support of a continuous member have been computed for different depth-thickness ratios for $f_{d s}=44$ ,66, and 88 ksi, and tabulated in Table 5-5b (+), Table 5-6b (+), and Table 5-7b (+), respectively.

### 5 -34.9Web Crippling

In addition to shear problems, concentrated loads or reactions at panel supports,applied over relatively short lengths, can produce load intensities that can cripple unstiffened thin webs. The problem of web crippling is rather complicated for theoretical analysis because it involves the following:

(1)Nonuniform stress distribution under the applied load and the adjacent portions of the web 



<!-- batch 28 | page 13 -->

(2)Elastic and inelastic stability of the web element 

(3)Local yielding in the intermediate region of load application 

(4)The bending produced by the eccentric load (or reaction) when it is applied on the bearing flange at a distance beyond the curved transition of the web 

The AISl recommendations have been developed by relating extensive experimental data to service loads with a safety factor of 2.2, which was established taking into account the scatter in the data. For blast design of cold-formed panels, it is recommended that the AlSl values be multiplied by a factor of 1.50 in order to relate the crippling loads to ultimate conditions with sufficient provisions for scatter in test data.

For those sections that provide a high degree of restraint against rotation of their webs,the ultimate crippling loads are given as follows:

Allowable ultimate end support reaction 

$$Q_{u}=1.5f_{d s}t^{2}/4.44+0.558(N/t)^{1/2}J $$

Allowable ultimate interior support reaction 

$$Q_{u}=1.5f_{d s}t^{2}/6.66+1.446(N/t)^{1/2}J $$

where 

$\mathcal{Q}_{u}=$ ultimate support reaction per web 

$\begin{array}{r l}{f_{d s}=}&{{}d y n a m i c\;d e s i g n\;s t r e s s}\end{array}$ 

1

$N=\mathrm{b e a r i n g\;l e n g t h\;(i n)}$ 



The charts in Figure 5-15 (+) and Figure 5-16 (+) present the variation of $\mathcal{Q}_{u}$ asa function of the web thickness for bearing lengths from 1 to 5 inches for $f_{d}s=44$ ·ksi for end and interior supports, respectively. It should be noted that the values reported in the charts relate to one web only, the total ultimate reaction being obtained by multiplying $Q_{u}$ by the number of webs in the panel.



For design, the maximum shear forces and dynamic reactions are computed as a function of the maximum resistance in flexure. The ultimate load-carrying capacity of the webs of the panel must then be compared with these forces. As a general comment, the shear capacity is controlled by web crippling for simply supported elements and by the allowable design shear stresses at the interior supports for continuous panels.

In addition, it can be shown that the resistance in shear governs only in cases of relatively very short spans. If a design is controlled by shear resistance, it is 

<!-- batch 28 | page 14 -->

recommended that another panel be selected since a flexural failure mode is generally preferred.



## 5 -35

### SUMMARY OF DEFORMATION CRITERIA FOR STRUCTURAL ELEMENTS. 

Deformation criteria are summarized in Table 5-8 (+) for frames, beams and other structural elements including cold-formed steel panels, open-web joists and plates.

<div style="text-align: center;">Figure 5-11Biaxial Bending of a Doubly-Symmetric Section </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_296_553_913_1121.jpg" alt="Image" width="51%" /></div>


<!-- batch 28 | page 15 -->

<div style="text-align: center;">Figure 5-12Resistance-Deflection Curve for a Typical Cold-Formed Section </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_chart_box_201_323_1040_981.jpg" alt="Image" width="70%" /></div>


<!-- batch 28 | page 16 -->

<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_chart_box_193_330_824_1312.jpg" alt="Image" width="52%" /></div>


<!-- batch 28 | page 17 -->

<div style="text-align: center;">Figure 5-14Allowable Dynamic (Design) Shear Stresses for Webs of ColdFormed Members $(f_{d s}=44\mathrm{k s i})$  </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_chart_box_174_338_1054_1437.jpg" alt="Image" width="73%" /></div>


<!-- batch 28 | page 18 -->

<div style="text-align: center;">Figure 5-15 Maximum End Support Reaction for Cold-Formed Steel Sections  $(f_{d s}=44\mathrm{k s i})$  </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_chart_box_171_337_1062_1400.jpg" alt="Image" width="74%" /></div>


<!-- batch 28 | page 19 -->

<div style="text-align: center;">Figure 5-16Maximum Interior Support Reaction for Cold-Formed Steel Sections  $(f_{d s}=44\mathrm{k s i})$  </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_chart_box_172_337_1063_1400.jpg" alt="Image" width="74%" /></div>


<!-- batch 28 | page 20 -->

## Table 5-5Dynamic Design Shear Stress for Webs of Cold-Formed Members  $(f_{d s}=44\mathrm{k s i})$  

## (a) Simple Shear 


<div style="text-align: center;"><html><body><table border="1"><tr><td>hlt</td><td>$f_{d v}(\mathrm{{\sf{k s i}})}$</td></tr><tr><td>$(h/t)\leq57$</td><td>$0.50~f_{d s}\leq22.0$</td></tr><tr><td>$57\leq(h/t)\leq83$</td><td>$\overline{{1.26\times10^{3}/\left(h/t\right)}}$</td></tr><tr><td>$83\leq(h/t)\leq150$</td><td>$\overline{{1.07\times10^{5}/\left(h/t\right)}}$</td></tr></table></body></html></div>


(b) Combined Bending and Shear 


<div style="text-align: center;"><html><body><table border="1"><tr><td>hlt</td><td>$f_{dv}(\mathrm{\sf ksi})$</td></tr><tr><td>20</td><td>10.94</td></tr><tr><td>30</td><td>10.84</td></tr><tr><td>40</td><td>10.72</td></tr><tr><td>50</td><td>10.57</td></tr><tr><td>60</td><td>10.42</td></tr><tr><td>70</td><td>10.22</td></tr><tr><td>80</td><td>9.94</td></tr><tr><td>90</td><td>9.62</td></tr><tr><td>100</td><td>9.00</td></tr><tr><td>110</td><td>8.25</td></tr><tr><td>120</td><td>7.43</td></tr></tbody></table></body></html></div>


<!-- batch 28 | page 21 -->

## Table 5-6Dynamic Design Shear Stress for Webs of Cold-Formed Members  $(f_{d s}=66\mathrm{k s i})$  

## (a) Simple Shear 


<div style="text-align: center;"><html><body><table border="1"><tr><td>hlt</td><td>$f_{d v}(\mathrm{{\sf{k s i}})}$</td></tr><tr><td>$(h/t)\leq47$</td><td>0.50 $f_{\mathrm{d s}}\leq33.0$</td></tr><tr><td>$47<(h/t)\leq67$</td><td>$\overline{{1.54\times10^{3}/\left(h/t\right)}}$</td></tr><tr><td>$67\leq(h/t)\leq150$</td><td>$\overline{{1.07\times10^{5}/\left(h/t\right)}}$</td></tr></table></body></html></div>


(b) Combined Bending and Shear 


<div style="text-align: center;"><html><body><table border="1"><tr><td>hlt</td><td>$f_{dv}(\mathrm{\sf ksi})$</td></tr><tr><td>20</td><td>16.41</td></tr><tr><td>30</td><td>16.23</td></tr><tr><td>40</td><td>16.02</td></tr><tr><td>50</td><td>15.75</td></tr><tr><td>60</td><td>15.00</td></tr><tr><td>70</td><td>14.20</td></tr><tr><td>80</td><td>13.00</td></tr><tr><td>90</td><td>11.75</td></tr><tr><td>100</td><td>10.40</td></tr><tr><td>110</td><td>8.75</td></tr><tr><td>120</td><td>7.43</td></tr></tbody></table></body></html></div>


<!-- batch 28 | page 22 -->

## Table 5-7Dynamic Design Shear Stress for Webs of Cold-Formed Members  $(f_{d s}=88\mathrm{k s i})$  

## (a) Simple Shear 


<div style="text-align: center;"><html><body><table border="1"><tr><td>hlt</td><td>$f_{d v}(\mathrm{{\sf{k s i}})}$</td></tr><tr><td>$(h/t)\leq41$</td><td>0.50 $f_{d s}\leq44.0$</td></tr><tr><td>$41<(h/t)\leq58$</td><td>$1.78\times10^{3}/\left(h/t\right)$</td></tr><tr><td>$58\leq(h/t)\leq150$</td><td>$\overline{{1.07\times10^{5}/\left(h/t\right)}}$</td></tr></table></body></html></div>


(b) Combined Bending and Shear 


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>hlt</td><td>$f_{dv}(\mathrm{\sf ksi})$</td></tr><tr><td>20</td><td>21.60</td></tr><tr><td>30</td><td>21.00</td></tr><tr><td>40</td><td>20.00</td></tr><tr><td>50</td><td>18.80</td></tr><tr><td>60</td><td>17.50</td></tr><tr><td>70</td><td>16.00</td></tr><tr><td>80</td><td>14.30</td></tr><tr><td>90</td><td>12.50</td></tr><tr><td>100</td><td>10.75</td></tr><tr><td>110</td><td>8.84</td></tr><tr><td>120</td><td>7.43</td></tr></tbody></table></body></html></div>


<!-- batch 28 | page 23 -->

<div style="text-align: center;">Table 5-8Summary of Deformation Criteria </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Element</td><td>Highest level of Protection (Category No.))*</td><td>Additional Specifications</td><td>Deformation Type**</td><td>Maximum Deformation</td></tr><tr><td rowspan="2">Beams, purlins, spandrels or girts</td><td>1</td><td rowspan="2"></td><td>日 μ</td><td>2^\ 10</td></tr><tr><td>2</td><td>日 μ</td><td>12° 20</td></tr><tr><td>Frame structures</td><td>1</td><td></td><td>δ Θ†</td><td>H/25 2^\</td></tr><tr><td rowspan="2">Cold-formed steel floor and wall panels</td><td rowspan="2">1</td><td>Without tension- membrane action</td><td>日 μ</td><td>1.25° 1.75</td></tr><tr><td>With tension- membrane action</td><td>日 μ</td><td>4^° 6</td></tr><tr><td rowspan="2">Open-web joists</td><td rowspan="2">1</td><td></td><td>日 μ</td><td>24</td></tr><tr><td>Joists controlled by shear</td><td>日 μ</td><td>1° 1</td></tr><tr><td rowspan="2">Plates</td><td>1</td><td rowspan="2"></td><td>日 μ</td><td>2^\ 10</td></tr><tr><td>2</td><td>日 μ</td><td>12° 20</td></tr></tbody></table></body></html></div>


$\scriptstyle{\mathcal{O}}=$ maximum member end rotation (degrees) measured from the chord joining the member ends 



$\delta=$ relative sidesway deflection between stories 

$H=$ story height 

$\mu=$ ductility ratio $(X_{m}/X_{E})$ 

*As defined in Chapter 1.

**Whichever governs.

十Individual frame member.

<!-- batch 28 | page 24 -->

## SPECIAL CONSIDERATIONS, BLAST DOORS 

## BLAST DOOR DESIGN

## 5 -36

### 5 -36.1General

This section outlines procedures for the design of steel blast doors. Analytical procedures for the design of the individual elements of the blast door plate have been presented in earlier sections of this chapter. In addition to the door plate, door frames and anchorage, reversal bolts, gaskets and door operators are discussed. Blast doors are categorized by their functional requirements and method of opening.

### 5 -36.2Functions and Methods of Opening

#### 5 -36.2.1Functional Requirements

Blast doors may be designed to contain an accidental explosion from within a structure so as to prevent pressure and fireball leakage and fragment propagation. Blast doors may also be designed to protect personnel and/or equipment from the effects of external blast loads. In this case, a limited amount of blast pressures may be permited to leak into the protected area. In most cases, blast doors may be designed to protect the contents of a structure, thereby negating propagation when explosives are contained within the shelter.



#### 5 -36.2.2Method of Opening

Blast doors may be grouped based on their method of opening, such as: (a) single leaf (b) double leaf, (c) vertical lift, and (d) horizontal sliding.



### 5 -36.3Design Considerations

#### 5 -36.3.1General

The design of a blast door is intrinsically related to its function during and/or after an explosion. Design considerations include whether or not the door should sustain permanent deflections, whether rebound mechanisms or fragment protection is required, and whether pressure leakage be tolerated. Finally, the design pressure range may dictate the type of door construction that is to be used, including solid steel plate or built-up doors.



#### 5 -36.3.2Deflections

As stated in Section 5-16.7, plates can sustain a support rotation of 12 degrees without failing. This is applicable to blast doors providing that the resulting plate deflection does not collapse the door by pushing it through the opening. However, deflections may have to be limited if the mechanism used to open the door after an explosion is required to function. In addition, if a blast door is designed with a gasket so as to fully or nearly contain the pressure and fireball effects of an explosion, then deflections should be limited in order to ensure satisfactory performance of the gasket.

<!-- batch 28 | page 25 -->

#### 5 -36.3.3Rebound Mechanisms

Steel doors will be subjected to relatively large stress reversals caused by rebound.Blast doors may have to transfer these reversal loads by means of retracting pins or "reversal bolts." These heads can be mounted on any edge (sides, top, or bottom) of a doorplate. Reversal bolts can be designed as an integral part of the panic hardware assembly or, if tapered, they can be utilized in compressing the gasket around a periphery. The magnitude of the rebound force acting on the blast doors is discussed later.



#### 5 -36.3.4Fragment Protection

A plate-type blast door, or the plate(s) of a built-up blast door may be sized to prevent fragment penetration. However, when the blast door is subjected to large blast loads and fragments, a supplementary fragment shield may be necessary since the combined effects of the fragments and pressures may cause premature door failure due to the notching effects produced by the fragments. Procedures for predicting the characteristics of primary fragments such as impact, velocity, and size of fragment are presented in Chapter 2. Methods for determining the depth of penetration of fragments into steel are given in Section 5-49.



#### 5 -36.3.5Leakage Protection (Gaskets)

Blast doors may be designed to partly or fully contain the pressure and fireball effects of an explosion in which case gaskets may have to be utilized around the edge of a door or its opening. A sample of a gasket is illustrated in Figure 5-17 (+). This gasket will have to be compressed by means of a hydraulic operator which is capable of overcoming a force of 125 pounds per linear inch of the gasket. This gasket is made of neoprene conforming to the material callouts in Note 2 of Figure 5-17 for the current version of ASTM D 2000.



#### 5 -36.3.6Type of Construction

Blast doors are formed from either solid steel plate or built-up steel construction.

Solid steel plate doors are usually used for the high pressure ranges (50 psi or greater)and where the door span is relatively short. Depending on plate thicknesses, these doors may be used when fragment impact is critical. These plates can range in thickness of 1-inch or greater. For thick plates, connections using high strength bolts or socket head cap screws are recommended in lieu of welding. However, the use of bolts or screws must preclude the passage of leakage pressures into or out of the structure depending on its use.



Built-up doors are used usually for the low pressure range and where long spans are encountered. A typical built-up blast door may consist of a peripheral frame made from steel channels with horizontal channels serving as intermediate supports for the interior and/or exterior steel cover plates. The pressure loads must be transferred to the 

<!-- batch 28 | page 26 -->

channels via the plate. Concrete or some other material may be placed between the plates in order to add mass to the door or increase its fragment resistance capabilities.

### 5 -36.4Examples of Blast Door Designs

#### 5 -36.4.1General

In order to illustrate the relationship between the function of a blast door and its design considerations, four examples are presented in the following section. Table 5-9 (+) lists the design requirements of each of the above door examples.

#### 5 -36.4.2Door Type A (Figure 5-18 (+))

This blast door is designed to protect personnel and equipment from external blast pressures resulting from an accidental explosion. The door opening measures 8-feet high by 8-feet wide. It is a built-up double-leaf door consisting primarily of an exterior plate and a thinner interior plate both welded to a grid formed by steel tubes. Support rotations of each element (plate, channel, tube) have been limited to 2 degrees in order to assure successful operation of the panic hardware at the door interior. The direct blast load is transferred from the exterior plate to tubular members which form the door grid. The grid then transfers the loads to the door frame at the center of the opening through a set of pins attached to the top and bottom of the center mullions of the grid. At the exterior, the loads are transferred to the frame through the hinges which are attached to the exterior mullions and the frame. The reversal loads are also transferred by the pins and by the built-up door hinges. The center pins are also operated by the panic hardware assembly.



#### 5 -36.4.3Door Type B (Figure 5-19 (+))

This blast door is designed to prevent propagation from an accidental explosion into an explosives storage area. It is a built-up, sliding door protecting an opening 11-feet high by 16-feet wide, consisting of an exterior plate and a thinner interior plate. These plates are welded to vertical S-shapes which are spaced at 15-inch intervals. This door is designed to act as a one-way member, spanning vertically. Since flange buckling of the S-shapes is prohibited in the presence of the outer and inner plates acting as braces,the composite beam-plate arrangement is designed for a support rotation of 12 degrees.The yield capacity of the webs of the S-shapes in shear (Equation 5-16), as well as web crippling (Section 5-25), had to be considered in the design. This door has not been designed to resist reversal or rebound forces.



#### 5 -36.4.4Door Type C (Figure 5-20 (+))

This single-leaf blast door is designed as part of a containment cell which is used in the repeated testing of explosives. The door opening measures 4-feet 6-inches wide by 7feet 6-inches high. It is the only door, in these samples, designed elastically since it is subjected to repeated blast loads. It consists primarily of a thick steel door plate protected from test fragments by a mild steel fragment shield. It is designed as a simplysupported (four sides) plate for direct internal loads and as a one-way element spanning 

<!-- batch 28 | page 27 -->

the door width for rebound loads. It is equipped with a neoprene gasket around the periphery (Figure 5-17 (+)) as well as a series of six reversal bolts designed to transfer the rebound load into the door frame. The large thickness of the door plate warrants the use of high-strength, socket head cap screws in lieu of welding to connect the plate to the reversal bolt housing as well as to the fragment shield.



#### 5 -36.4.5Door Type D (Figure 5-21 (+))

This single-leaf blast door is designed as part of a containment structure which is used to protect nearby personnel and structures in the event of an accidental explosion. The door opening measures 4-feet wide by 7-feet high. It is designed as simply-supported on four sides for direct load and as a one-way element spanning the door width for rebound loads. It is equipped with a neoprene gasket around the periphery and a series of six reversal bolts which transfer the rebound load to the door frame. The reversal bolt housing and bearing blocks are welded to the door plate. Excessive deflections of the door plate under blast loading would hamper the sealing capacity of the gasket.Consequently, the door plate design rotation is limited to 2 degrees.

#### 5 -36.4.6Other Types of Doors

Another type of blast door design is a steel arch or "bow" door. The tension arch door requires compression ties to develop the compression reactions from the arch. The compression arch door requires tension members to develop the tension reactions from the arch. These doors are illustrated in Figure 5-42 (+)



### 5 -36.5Blast Door Rebound

Plate or element rebound can be determined for a single-degree-of-freedom system subjected to a triangular pulse (see Figure 5-13 (+)). However, when a system is subjected to a billinear load, only a rigorous, step-by-step dynamic analysis can determine the percentage of elastic rebound. In lieu of a rigorous analysis, a method of determining the upper bound on the rebound force is presented here.

Three possible rebound scenarios are discussed. Figure 5-22 (+) is helpful in describing each case.



(a)Case I- Gas load not present $(P_{g a s}=0)$ 1. In this case, the required rebound resistance is obtained from Figure 5-13 (+).



(b)Case $\mathrm{~I I~-~}t_{m}\leq t_{l}$ In this case, the required rebound resistance is again obtained from Figure 5-10 (+). This procedure, however, can overestimate the rebound load.



(c)Case Ill -$t_{m}>t_{i}$ Figure 5-22 (+) illustrates the case whereby the time to reach the peak response,$t_{m}$ is greater than the point where the gas load begins to act (tj). Assuming that the gas pressure can be considered constant over a period of time, it will act to lower the required rebound resistance since 

<!-- batch 28 | page 28 -->

the resistance time curve will oscillate about the gas pressure time curve. In this case, the upper bound for the required rebound resistance is:

$$\overline{{\boldsymbol{r}}}=\boldsymbol{r}_{u}-\boldsymbol{P}_{\mathrm{g a s}}$$

However, in all three cases, it is recommended that the required rebound resistance be at least equal to 50 percent of the peak positive door response.

### 5 -36.6Methods of Design

#### 5 -36.6.1General

Techniques used for the design of two types of blast doors will be demonstrated. The first technique is used for the door illustrated in Figure 5-18 (+) while the second is used for the door shown in Figure 5-21 (+). Detailed procedures for the design of plate and beam elements, as well as the related design criteria, are presented in earlier section of this chapter and numerical examples are presented in Appendix A.

#### 5 -36.6.2Built-up Door

The built-up steel door shown in Figure 5-18 (+) is constructed by welding the steel plates to the steel tubular grid (fillet welded to the exterior plate and plug-welded to the interior plate). The heavy exterior plate is designed as a continuous member supported by the tubes. The horizontal tubes, in turn, are designed as simply supported members,transferring load to the vertical tubes. The interior tubes are also designed as simply supported elements which transfer the direct and rebound loads to the pins while the side tubes transfer the direct load to the door frame proper and rebound loads to the hinges. The exterior tubes are also designed as simply supported elements with the supports located at the hinges.



#### 5 -36.6.3Solid Steel Plate Door

The steel plate of the blast door shown in Figure 5-21 (+) is initially sized for blast pressures since no high speed fragments will be generated in the facility. The plate is sized for blast loading, considering the plate to be simply supported on four edges. The direct load is transferred to the four sides of the door frame. In rebound, the plate acts as a simple beam spanning the width of the door opening. The rebound force is transferred to the six reversal bolts and then into the door frame. The door frame, as illustrated in Figure 5-19 (+), consists of two units; the first unit is imbedded into the concrete and the second unit is attached to the first one. This arrangement allows the first frame to be installed in the concrete wall prior to the fabrication of the door. After the door construction is completed, the subframe is attached to the embedded frame and, thus, the door installation is completed.



<!-- batch 28 | page 29 -->

<div style="text-align: center;">Figure 5-17Gasket Detail for Blast Door </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_142_322_1052_595.jpg" alt="Image" width="76%" /></div>


DETAIL (TYPICAL AROUND PERIPHERY OFDOOR)

<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_229_705_453_787.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">GASKET SPLICE </div>


## NOTES FOR GROOVE & GASKET 

1.ALL SURFACES OF DOOR GROOVE SHALL BEMACHINED TO I25 MICROINCHES AND SHALL NOT BE PAINTED.2.GASKETS FOR ALLDOORS SHALL MEET THE SPECIFICATIONREQUIREMENTSASPERASTMD2OOO-77a AND AS INDICATED IN THE FOLLOWING LINE CALL OUT;2BC520A14B14C12F17.



3. THE FORCE REQUIRED TO CLOSE DOOR IS APPROXIMATELYI25POUNDSPER LINEARINCHOF GASKET.

<!-- batch 28 | page 30 -->

<div style="text-align: center;">Figure 5-18Built-up Double-Leaf Blast Door with Frame Built into Concrete </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_162_333_1041_955.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">Figure 5-19Horizontal Sliding Blast Door </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_158_1034_1045_1431.jpg" alt="Image" width="74%" /></div>


<!-- batch 28 | page 31 -->

## Figure 5-20Single-Leaf Blast Door With Fragment Shield (Very High Pressure)

<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_195_319_1030_794.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">Figure 5-21Single Leaf Blast Door (High Pressure)</div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_547_910_1043_1145.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_239_933_499_1250.jpg" alt="Image" width="21%" /></div>


LEGEND:

-STEELFRAME EMBEDDED IN CONCRETE 

R CONTINUOUS GASKET 

-BEARING BLOCK 

-BLAST DOORPLATE 

E- DOOR HINGE 

F-REVERSAL BOLT HOUSING 

G -REVERSALBOLT 

-BARCONNECTED TO CLOSURE MECHANISM 

STEEL FRAME EQUIPPED WITH BLAST DOOR 

-LIGHT GAGECOVER PLATE 



<!-- batch 28 | page 32 -->

<div style="text-align: center;">Figure 5-22Bilinear Blast Load and Single-Degree-of-Freedom Response for Determining Rebound Resistance </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_chart_box_216_331_920_706.jpg" alt="Image" width="59%" /></div>




$\mathsf{P}=\mathsf{PEAK}\perp\mathsf{AD}$ 

$\mathsf{P}_{\mathsf{Q Q S}}=\mathsf{G A S}$ PRESSURE 

$r_{U}=\mathsf{P E A K}$ POSITIVE RESPONSE 

$\overline{r}=\mathsf{REQ}\cup\mathsf{IRED}$ REBOUND RESISTANCE 

$\mathsf{t}_{\mathsf{j}}\;=\;\mathsf{T I M E}$ AT WHICH SHOCK AND GAS LOADS INTERSECT 

$t_{m}=\top\mathrm{I M E}$ TO REACH MAXIMUM RESPONSE 



<!-- batch 28 | page 33 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td colspan="3" rowspan="2">Door Description</td><td colspan="9">Design Requirements</td></tr><tr><td colspan="3">Permanent Deflections</td><td colspan="2">Rebound Mechanisms</td><td colspan="2">Fragment Protection</td><td colspan="2">Level of Leakage Protection Required</td></tr><tr><td>Door</td><td>Figure</td><td>Method of Opening</td><td>None</td><td>Limited</td><td>Large</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Low</td><td>High</td></tr><tr><td>A</td><td>5-18(+)</td><td>Double-Leaf</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>B</td><td>(+)6-5</td><td>6uip!is</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td></tr><tr><td>O</td><td>)05</td><td>ee-e</td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>a</td><td>(+)-5</td><td>eeer</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td></tr></tbody></table></body></html></div>


<div style="text-align: center;"> ee ro e e   e </div>


ee neee e 

e ee 

12-220-020



<!-- batch 28 | page 34 -->

## COLUMNS AND BEAM COLUMNS 

## PLASTIC DESIGN CRITERIA

## 5 -37

### 5 -37.1General

The design criteria for columns and beam columns must account for their behavior not only as individual members but also as members of the overall frame structure.Depending on the nature of the loading, several design cases may be encountered.Listed below are the necessary equations for the dynamic design of steel columns and beam columns.



### 5 -37.2In-plane Loads

In the plane of bending of compression members which would develop a plastic hinge at ultimate loading, the slenderness ratio l/r shall not exceed the constant $(C_{c})$ defined as:

$$C_{c}=(2\pi^{2}E/f_{d s})^{1/2}$$

where,

$E=$ modulus of elasticity of steel (psi)$f_{d s}=$ dynamic design stress (see Section 5-13)

The ultimate strength of an axially loaded compression member shall be taken as:

$$P_{u}=1.7A F_{a}$$

where 

A= gross area of member,

$$\begin{array}{r l}{F_{a}=}&{{}\frac{\left(1-\left(K I/r\right)^{2}/2C_{c}^{2}\right)f_{d s}}{5/3+3\left(K I/r\right)/\left(8C_{c}\right)-\left(K I/r\right)^{3}/\left(8C_{c}^{3}\right)},\mathrm{a n d}}\end{array}$$

Kl/r = largest effective slenderness ratio listed in Table 5-10 (+) or Table 5-11 (+)

### 5 -37.3Combined Axial Loads and Biaxial Bending

Members subject to combined axial load and biaxial bending moment should be proportioned so as to satisfy the following set of interaction formulas:

$$\begin{aligned}&P/P_{u}+C_{mx}M_{x}/[(1-P/P_{ex})M_{mx}]+C_{my}M_{y}/[(1-P/P_{ey})M_{my}]\leq1.0\\&P/P_{p}+M_{x}/(1.18M_{px})+M_{y}/(1.18M_{py})\leq1.0for P/P_{p}\geq0.15\\ \end{aligned}$$

<!-- batch 28 | page 35 -->

or 

$$M_{x}/M_{px}+M_{y}/M_{py}\leq1.0\ forP/P_{p}<0.15$$

where 

$$\begin{array}{r l}&{M_{x},\;M_{y}=m a x i m u m\;a p p l i e d\;m o m e n t s\;a b o u t\;t h e\;x\mathrm{-}\;a n d\;y\mathrm{-}x a x e s}\\ &{P=\quad a p p l i e d\;a x i l\;l o a d}\\ &{P_{e x}=23/12(A F_{e x}^{\prime})}\\ &{P_{e y}=23/12(A F_{e x}^{\prime})}\\ &{F_{e x}^{\prime}=12\pi^{2}E[23(K l_{b}/r_{x})^{2}]}\\ &{F_{e y}^{\prime}=12\pi^{2}E[23(K l_{b}/r_{y})^{2}]}\\ &{J_{b}=\quad a c t a l\;u n b r a c e d\;l e g r i d y\;i n t h e\;p l a n e\;o f\;b e n d y}\\ &{r_{x},\;r_{y}=c o r e s p o n d i n g\;a r d i i\;o f\;g r a t i o n}\\ &{P_{p}=\quad A f_{d s}}\\ &{C_{m x},\;C_{m y}=c o e f i e d\;i n t e s\;a p p l i e d\;t o\;b e n d j e t r m\;i n t e r a c t i o n\;f r o m u l a\;a n d\;d e p e n d e n t}\\ &{\quad\;o u n\;c o u n c\;c o u n r e\;c o u n t r a c t r e\;c a u s e d\;b y\;a p p l i e d\;m o m e n t s\;(A I S C\;S p e c i c i a t i o n,}\\ &{\quad\;S e c t i o n\;1.6.1)}\\ &{M_{p x},\;M_{p y}=p l a s t i c\;b e n d i n g\;c a p a c i t i e s\;a b o u t\;x\;a n d\;y\;a x e s\;(M_{p x}=Z_{x}f_{d s},\;M_{p y}=Z_{y}f_{d s})}\\ &{M_{m x},\;M_{m y}=m o m e n t s\;t h a t\;c a n\;b e\;r e s i s t e d\;b y\;t h e\;m e n b e r\;i n t e\;o f\;a x i l\;l o a d}\end{array}$$

For columns braced in the weak direction,$M_{m x}=M_{p x}\mathrm{a n d}M_{m y}=M_{p y}$ 

When columns are unbraced in the weak direction:

$$\begin{aligned}&M_{mx}=[1.07-(1/r_y)(f_{ds})^{1/2}/3160]M_{px}<M_{px}\\ &M_{mv}=[1.07-(1/r_x)(f_{ds})^{1/2}/3160]M_{py}<M_{py}\\ \end{aligned}$$

Subscripts x and y indicate the axis of bending about which a particular design property applies. Also, columns may be considered braced in the weak direction when the provisions of Section 5-26 are satisfied. In addition, beam columns should also satisfy the requirements of Section 5-23.



## 5 -38

## EFFECTIVE LENGTH RATIOS FOR BEAM-COLUMNS

The basis for determining the effective lengths of beam columns for use in the calculation of $P_{u},P_{e x},M_{m x}$ ,and $M_{m y}$ , in plastic design is outlined below.

For plastically designed braced and unbraced planar frames which are supported against displacement normal to their planes, the effective length ratios in Table $5-10(+)$ and Table 5-11 (+) shall apply.



<!-- batch 28 | page 36 -->

Table 5-10 (+) corresponds to bending about the strong axis of a member, while Table 5-11 (+) corresponds to bending about the weak axis. In each case,I is the distance between points of lateral support corresponding to $r_{x}\circ\Gamma r_{y},$ ,as applicable. The effective length factor, K, in the plane of bending shall be governed by the provisions of Section 5-39.



For columns subjected to biaxial bending, the effective lengths given in Table 5-10 (+)and Table 5-11 (+) apply for bending about the respective axes, except that $P_{u}$ for unbraced frames shall be based on the larger of the ratios $K//r_{x}\mathrm{o r}K//r_{y}$ . In addition, the larger of the slenderness ratios,$I/r_{x}$ or $I/r_{y}$ ,shall not exceed $C_{c}$ 

## 5 -39EFFECTIVE LENGTH FACTOR, K

In plastic design, it is usually sufficiently accurate to use the K factors from Table C1.8.1of the AISC Manual (reproduced here as Table $5-12\;(\pm))$ for the condition closest to that in question rather than to refer to the alignment chart (Chapter C of the AISC Manual). It is permissible to interpolate between different conditions in Table 5-12 using engineering judgment. In general, a design value of K equal to 1.5 is conservative for the columns of unbraced frames when the base of the column is assumed pinned, since conventional column base details will usually provide partial rotational restraint at the column base. For girders of unbraced frames, a design K value of 0.75 is recommended.



<div style="text-align: center;">Table 5-10Effective Length Ratios for Beam Columns (Webs of members in the plane of the frame; i.e., bending about the strong axis)</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>Braced Planar Frames*</td><td>One-and Two-Story Unbraced Planar Frames*</td></tr><tr><td>Use larger ratio, or $\overline{{P_{u}}}$ $I/r_{x}$ $I/r_{y}$</td><td>Use larger ratio, or $K//r_{x}$ $I/r_{y}$</td></tr><tr><td>Use $P_{e x}$ $I I r_{x}$</td><td>Use $K//r_{x}$</td></tr><tr><td>Use $\overline{{M_{m x}}}$ $I/r_{y}$</td><td>Use $I/r_{y}$</td></tr></table></body></html></div>


<div style="text-align: center;">*$I/r_{x}$ shall not exceed $C_{c}$ </div>


<div style="text-align: center;">Table 5-11Effective Length Ratios for Beam Columns (Flanges of members in the plane of the frame: i.e., bending about the weak axis)</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>Braced Planar Frames*</td><td>One- and Two-Story Unbraced Planar Frames*</td></tr><tr><td>Use larger ratio, or $P_{u}$ $I/r_{x}$ $l/r_{y}$</td><td>Use larger ratio, or $I/r_{x}$ $K//r_{y}$</td></tr><tr><td>Use $P_{e y}$ $I/r_{y}$</td><td>Use $K//r_{y}$</td></tr><tr><td>Use $I/r_{x}$ $M_{m y}$</td><td>Use $1/r_{x}$</td></tr></table></body></html></div>


<div style="text-align: center;">*$I/r_{y}$ shall not exceed $C_{c}$ </div>


<!-- batch 28 | page 37 -->

<div style="text-align: center;">Table 5-12Effective Length Factors for Columns and Beam-Columns </div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>Buckled shape of column is shown by dashed line.</td><td>(a)</td><td>(b)</td><td>(c)</td><td>(d)</td><td>(e)</td><td>(f)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Theoretical K value</td><td>0.5</td><td>0.7</td><td>1.0</td><td>1.0</td><td>2.0</td><td>2.0</td></tr><tr><td rowspan="4">Recommended design value when ideal conditions are approximated</td><td>0.65</td><td colspan="5">0.80</td></tr><tr><td></td><td colspan="5"></td></tr><tr><td>End condition code</td><td colspan="5">\</td></tr><tr><td>甲 o1</td><td colspan="5">Rotation fixed and translation free. Rotation free and translation free.</td></tr></table></body></html></div>


<!-- batch 28 | page 38 -->

## FRAME DESIGN 

## 5 -40GENERAL

The dynamic plastic design of frames for blast resistant structures is oriented toward industrial building applications common to ammunition manufacturing and storage facilities, i.e., relatively low, single-story, multi-bay structures. This treatment applies principally to acceptor structures subjected to relatively low blast overpressures.

The design of blast resistant frames is characterized by (a) simultaneous application of vertical and horizontal pressure-time loadings with peak pressures considerably in excess of conventional loads, (b) design criteria permitting inelastic local and overal dynamic structural deformations (deflections and rotations), and (c) design requirements dictated by the operational needs of the facility and the need for reusability with minor repair work after an incident must be considered.



Rigid frame construction is recommended in the design of blast resistant structures since this system provides open interior space combined with substantial resistance to lateral forces. In addition, this type of construction possesses inherent energy absorption capability due to the successive development of plastic hinges up to the ultimate capacity of the structure. However, where the interior space and wall opening requirements permit, it may be as effective to provide bracing.

The particular objective in this section is to provide rational procedures for efficiently performing the preliminary design of blast resistant frames. Rigid frames as well as frames with supplementary bracing and with rigid or nonrigid connections are considered. In both cases, preliminary dynamic load factors are provided for establishing equivalent static loads for both the local and overall frame mechanism.Based upon the mechanism method, as employed in static plastic design, estimates are made for the required plastic bending capacities as well as approximate values for the axial loads and shears in the frame members. The dynamic deflections and rotations in the sidesway and local beam mechanism modes are estimated based upon single degree-of-freedom analyses. The design criteria and the procedures established for the design of individual members previously discussed apply for this preliminary design procedure.



In order to confirm that a trial design meets the recommended deformation criteria of Table 5-8 (+) and to verify the adequacy of the member sizes established on the basis of estimated dynamic forces and moments, a rigorous frame analysis should be performed. This analysis should consider the moments produced by the axial load deflection P-delta effects in determining the sizes of individual elements. The use of computer programs for dynamic analysis of multi-degree-of-freedom, nonlinear dynamic analyses of steel frame structures is discussed in Section 5-10. These programs have the capability of performing a multi-degree-of-freedom, nonlinear, dynamic analysis of braced and unbraced, rigid and nonrigid frames of one or more story structures.

<!-- batch 28 | page 39 -->

#### 5 -41TRIAL DESIGN OF SINGLE-STORY RIGID FRAMES.5-41.1Collapse Mechanisms

General expressions for the possible collapse mechanism of single-story rigid frames are presented in Table 5-13 (+) for pinned and fixed base frames subjected to combined vertical and horizontal blast loads.



The objective of this trial design is to proportion the frame members such that the governing mechanism represents an economical solution. For a particular frame, the ratio of horizontal to vertical peak loading denoted by α is influenced by the horizontal frame plan of the structure and is determined as follows:

$$\alpha=q_{h}/q_{v}$$

where 

$q_{v}=p_{v}b_{v}=p e a k$ : vertical load on rigid frame $q_{h}=$ Phbn = peak horizontal load on rigid frame $p_{v}=$ blast overpressure on roof $p_{h}=$ reflected blast pressure on front wall $b_{v}=$ tributary width for vertical loading $b_{h}=$ tributary width for horizontal loading 

The orientation of the roof purlins with respect to the blast load directions are shown in 

Figure 5-23 (+).The value of α will usually lie in the range from about 1.8 to 2.5 when the direction of the blast load is perpendicular to the roof purlins. In this case, the roof purlins are supported by the frame and the tributary width is the same for the horizontal and vertical load. The value of α is much higher when the direction of the blast load is parallel to the roof purlins. In this case, the roof purlins are not supported by the girder of the frame and the tributary width of the vertical loading $(b_{v}=\operatorname{p u r l i n}\operatorname{s p a c i n g})$ Iis much smaller than the tributary width of the horizontal loading $(b_{h}={\mathrm{f r a m e~s p a c i n g}})$ 

It is assumed in this procedure that the plastic bending capacity of the roof girder,$M_{p},$ ,is constant for all bays. The capacity of the exterior and interior columns are taken as $\dot{C}M_{p}$ and $C_{1}M_{p}$ ,respectively. Since the exterior column is generally subjected to reflected pressures, it is recommended that a value of C greater than 1.0 be selected. In analyzing a given frame with certain member properties, the controlling mechanism is the one with the lowest resistance. In design, however, the load is fixed and the required design plastic moment is the largest $M_{P}$ value obtained from all possible mechanisms. For that purpose, C and $C_{1}$ should be selected so as to minimize the value of the maximum required $M_{P}$ from among all possible mechanisms. After a few trials, it will become obvious which choice of C and $C_{1}$ tends to minimize the largest value of $M_{p}$ .



<!-- batch 28 | page 40 -->

### 5 -41.2Dynamic Deflections and Rotations

It will normally be more economical to proportion the members so that the controlling failure mechanism is a combined mechanism rather than a beam mechanism. The mechanism having the least resistance constitutes an acceptable mode of failure provided that the magnitudes of the maximum deflections and rotations do not exceed the maximum values recommended in Table 5-8 (+).



### 5 -41.3Dynamic Load Factors

To obtain initial estimates of the required mechanism resistance, the dynamic load factors listed in this section may be used to obtain equivalent static loads for the indicated mechanisms. These load factors are necessarily approximate and make no distinction for different end conditions. However, they are expected to result in reasonable estimates of the required resistance for a trial design. Once the trial member sizes are established, then the natural period and deflection of the frame can be calculated.



It is recommended that the DLF for a beam collapse mechanism be equal to 1.25 while that for a panel or combined collapse mechanism be equal to 0.625. The DLF for a frame is lower than that for a beam mechanism, since the natural period of vibration in the sidesway mode will normally be much greater than the natural periods of vibration of the individual elements.



### 5 -41.4Loads in Frame Members

Estimates of the peak axial forces in the girders and the peak shears in the columns are obtained from Figure 5-24 (+). In applying the values of Figure 5-24, the equivalent horizontal static load shall be computed using the dynamic load factor for a panel or combined sidesway mechanism.



Preliminary values of the peak axial loads in the columns and the peak shears in the girders may be computed by multiplying the equivalent vertical static load by the roof tributary area. Since the axial loads in the columns are due to the reaction from the roof girders, the equivalent static vertical load should be computed using the dynamic load factor for the beam mechanism.



### 5 -41.5Sizing of Frame Members

Each member in a frame under the action of horizontal and vertical blast loads is subjected to combined bending moments and axial loads. However, the phasing between critical values of the axial force and bending moment cannot be established using a simplified analysis. Therefore, it is recommended that the peak axial loads and moments obtained from Figure 5-24 (+) be assumed to act concurrently for the purpose of trial beam-column design. The overall resistance of the frame depends upon the ultimate strength of the members acting as beam-columns.



<!-- batch 28 | page 41 -->

When an exterior frame of a building is positioned such that the shock front is parallel to frame, the loadings on each end of the building are equal and sidesway action will only occur in the direction of the shock wave propagation. Frame action will also be in one direction, in the direction of the sidesway. If the blast wave impinges on a building from a quartering direction, then the columns and girders in the exterior frames are subjected to biaxial bending due to the simultaneous loads acting on the various faces of the structure. This action will also cause sidesway in both directions of the structure. The interior girders will usually be subjected to bending in one direction only. However,interior columns may be subjected to either uniaxial or biaxial bending, depending upon the column connections to the girder system. In such cases, the moments and forces can be calculated by analyzing the response of the frame in each direction and superimposing the respective moments and forces acting on the individual elements.This approach is generally conservative since it assumes that the peak values of the forces in one direction occur simultaneously throughout the three-dimensional structure.Having estimated the maximum values of the forces and moments throughout the frame, the preliminary sizing of the members can be performed using the criteria previously presented for beams and columns.



### 5 -41.6Stiffness and Deflection

The stiffness factor K for single-story rectangular frames subjected to uniform horizontal loading is defined in Table 5-14 (+). Considering an equivalent single degree-of-freedom system, the sidesway natural period of this frame is 

$$T_{N}=2\pi(m_{e}/K K_{L})^{1/2}一$$

where $K_{L}$ is a load factor that modifies K, the frame stiffness, due to a uniform load, so that the product $K K_{L}$ . is the equivalent stiffness due to a unit load applied at the equivalent lumped mass $m_{e}$ 



The load factor is given by 

$$K_{L}=0.55\left(1-0.25\beta\right)$$

where β is the base fixity factor and is equal to zero and one for pinned base and fixed base frames, respectively.



The equivalent mass $m_{e}$ to be used in calculating the period of a sidesway mode consists of the total roof mass plus one-third of the column and wall masses. Since all of these masses are considered to be concentrated at the roof level, the mass factor,$K_{M}$ is equal to one.



The limiting resistance $R_{u}$ is given by 

<!-- batch 28 | page 42 -->

$$R_{u}=\alpha w H $$

where w is equal to the equivalent static uniform load based on the dynamic load factor for a panel or combined sidesway mechanism.



The equivalent elastic deflection $X_{E}$ corresponding to $R_{u}$ is 

$$X_{F}=R_{u}/K_{F}一-一$$

Knowing the sidesway resistance $R_{u}$ and the sidesway natural period of vibration c $T_{n}$ , the ductility ratio $(\mu)$ for the sidesway deflection of the frame can be computed using the dynamic response charts (Chapter 3). The maximum deflection $X_{m}$ is then calculated from 



$$X_{m}=\mu X_{E}$$

where 

## $\mu=$ ductility ratio in sidesway 

## 5 -42

### TRIAL DESIGN OF SINGLE-STORY FRAMES WITH SUPPLEMENTARY BRACING. 

### 5 -42.1General

Frames with supplementary bracing can consist of (a) rigid frames in one direction and bracing in the other direction, (b) braced frames in two directions with rigid connections,and (c) braced frames in two directions with pinned connections. Most braced frames utilize pinned connections.



### 5 -42.2Collapse Mechanisms

The possible collapse mechanisms of single-story frames with diagonal tension bracing (X-bracing) are presented in Table 5-15 (+) and Table 5-16 (+) for pinned-base frames with rigid and nonrigid girder-to-column connections, respectively. In these tables, the cross sectional area of the tension brace is denoted by $A_{b}$ , the dynamic design stress for the bracing member is $f_{d s}$ , and the number of braced bays is denoted by the parameter m. In each case, the ultimate capacity of the frame is expressed in terms of the equivalent static load and the member ultimate strength (either $M_{p}\;\mathrm{o r}\;A_{b}f_{d s})$ 1.ln developing these expressions in the tables, the same assumptions were made as for rigid frames, ie.,$M_{P}$ for the roof girder is constant for all bays, the bay width L is constant, and the column moment capacity coefficient C is greater than 1.0.

<!-- batch 28 | page 43 -->

For rigid frames with tension bracing, it is necessary to vary C,$C_{1}$ ,and $A_{b}$ in order to achieve an economical design. When nonrigid girder to column connections are used, C and $C_{1}$ drop out of the resistance function for the sidesway mechanism and the area of the bracing can be calculated directly.



### 5 -42.3Bracing Ductility Ratio

Tension brace members are not expected to remain elastic under the blast loading.

Therefore, it is necessary to determine if this yielding will be excessive when the system 

is permitted to deflect to the limits of the design criteria previously given.



The ductility ratio associated with tension yielding of the bracing is defined as the maximum strain in the brace divided by its yield strain. Assuming small deflections and neglecting axial deformations in the girders and columns, the ductility ratio is given by 

$$\mu=\delta(\cos^{2}\gamma)E/L f_{d s}$$

where 

$\mu=$ ductility ratio 

$\delta=$ sidesway deflection, inches 

$\gamma=$ vertical angle between the bracing and a horizontal plane bay width, inches 



From the deflection criteria, the sidesway deflection is limited to H/25. The ductility ratio can be expressed further as 



$$\mu=(H/25L)(\cos^{2}\gamma)(E/f_{d s})$$

### 5 -42.4Dynamic Load Factor

The dynamic load factors listed in Section 5-41.3 may also be used as a rational starting point for a preliminary design of a braced frame. In general, the sidesway stiffness of braced frames is greater than unbraced frames and the corresponding panel or sidesway dynamic load factor may also be greater. However, since these dynamic load factors are necessarily approximate and serve only as a starting point for a preliminary design, refinements to these factors for frames with supplementary diagonal braces are not warranted.



### 5 -42.5Loads in Frame Members

Estimates of the peak axial loads in the girders and the peak shears in the columns of a braced rigid frame are obtained from Figure 5-25 (+).It should be noted that the shear in the blastward column and the axial load in the exterior girder are the same as the 

<!-- batch 28 | page 44 -->

rigid frame shown in Figure 5-24 (+). The shears in the interior columns V2 are not affected by the braces while the axial loads in the interior girders P are reduced by the horizontal components of the force in the brace $F_{H}$ . If a bay is not braced, then the value of $F_{H}$ must be set equal to zero when calculating the axial load in the girder of the next braced bay. To avoid an error, horizontal equilibrium should be checked using the formula:

$$R_{u}=V1+nV2+mF_{H}$$

where 

$$\begin{array}{l}{{R_{u},\;V1,\;V2\;a n d\;F_{H}\;a r e\;d e f i n e d\;i n\;F i g u r e\;5\scriptstyle-25\;\underline{{{+}}}}}\\ {{n=n u m b e r\;o f\;b a y s}}\\ {{m=n u m b e r\;o f\;b r a c e d\;b a y s}}\end{array}$$

In addition, the value of $M_{p}$ used in Figure 5-25 (+) is simply the design plastic moment obtained from the controlling panel or combined mechanism.

An estimate of the peak loads for braced frames with nonrigid girder to column connections may be obtained using Figure 5-25 (+). However, the value of $M_{p}$ must be set equal to zero. For such cases, the entire horizontal load is taken by the exterior column and bracing. There is no shear force in the interior columns.

Preliminary values of the peak axial loads in the columns and the peak shears in the girders are obtained in the same manner as rigid frames. However, in computing the axial loads in the columns, the vertical components of the forces in the tension braces must be added to the vertical shear in the roof girders. The vertical component of the force in the brace is given by 



$$F_{v}=A_{b}f_{d s}\sin\gamma $$

The reactions from the braces will also affect the load on the foundation of the frame;therefore, the design of the footings must include these loads.

### 5 -42.6Stiffness and Deflection

The equations for determining the sidesway natural period of vibration and the deflection at yield for braced frames are similar to that of rigid frames. The primary difference is the inclusion of the horizontal stiffness $(K_{b})$ provided by tension bracing.The equations for the natural period and elastic deflection are as follows:

Natural period of vibration is 

$$T_{N}=2\pi\mathrm{J m}_{e}/(K K_{L}+K_{b})\mathrm{J}^{1/2}$$

<!-- batch 28 | page 45 -->

and the equivalent elastic deflection is 

$$X_{F}=R_{u}/(K K_{L}+K_{b})~$$

The horizontal stiffness of the tension bracing is given by 

$$K_{b}=(n A_{b}E\cos^{3}\gamma)/L $$

and other values have been defined previously. It may be noted that for braced frames with nonrigid girder-to-column connections, the value of the frame stiffness (K) is equal to zero.



### 5 -42.7Slenderness Requirements for Diagonal Braces

The slenderness ratio of the bracing should be less than 300 to prevent vibration and "slapping." This design condition can be expressed as 

$$r_{b}\ge L_{b}/300~~
$$

where 

## $r_{b}=$ minimum radius of gyration of the bracing member $L_{b}=$ length between points of support 

Even though a compression brace is not considered effective in providing resistance,the tension and compression braces should be connected where they cross. In this manner,$L_{b}$ for each brace may be taken equal to half of its total length.

### 5 -42.8Sizing of Frame Members

Estimating the maximum forces and moments in frames with supplementary bracing is similar to the procedures described for rigid frames. However, the procedure is slightly more involved since it is necessary to assume a value for the brace area in addition to the assumptions for the coefficients C and $C_{1}$ . For frames with nonrigid connections, C and $C_{1}$ do not appear in the resistance formula for a sidesway mechanism and $A_{b}$ can be determined directly. In selecting a trial value of $A_{b}$ for frames with rigid connections,the minimum brace size is controlled by slenderness requirements. In addition, in each particular application, there will be a limiting value of $A_{b}$ beyond which there will be no substantial weight savings in the frame members since there are maximum slenderness requirements for the frame members. In general, values of $A_{b}$ of about 2 square inches will result in a substantial increase in the overall resistance for frames with rigid connections. Hence, an assumed brace area in this range is recommended as a starting 

<!-- batch 28 | page 46 -->

point. The design of the beams and columns of the frames follow the procedures previously presented.



<div style="text-align: center;">Figure 5-23Orientation of Roof Purlins with Respect to Blast Load Direction for Frame Blast Loading </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_182_534_1035_1143.jpg" alt="Image" width="71%" /></div>


<!-- batch 28 | page 47 -->

<div style="text-align: center;">Figure 5-24Estimate of Peak Shears and Axial Loads in Rigid Frames Due to Horizontal Loads </div>


<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_176_345_1003_669.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">n=NUMBER OF BAYS  Ry= aWH = EQUIVALENT HORIZONTAL STATIC LOAD </div>


<!-- batch 28 | page 48 -->

Figure 5-25Estimates of Peak Shears and Axial Loads in Braced Frames Due to Horizontal Loads 

<div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_254_348_845_530.jpg" alt="Image" width="49%" /></div>


$$\begin{array}{r l}&{\mathsf{R}_{\mathsf{U}}=\alpha\mathsf{w}\mathsf{H}}\\ &{\vee\mathsf{1}=\mathsf{R}_{\mathsf{U}}/\mathsf{2}+\mathsf{M}_{\mathsf{P}}/\mathsf{H}}\\ &{\mathsf{P1}=\mathsf{R}_{\mathsf{U}}/\mathsf{2}-\mathsf{M}_{\mathsf{P}}/\mathsf{H}}\\ &{\mathsf{P2}=\mathsf{P1}-\vee\mathsf{2}-\mathsf{F}_{\mathsf{H}}}\\ &{\mathsf{F}_{\mathsf{H}}=\mathsf{A}_{\mathsf{U}}\mathsf{F}_{\mathsf{U}\mathsf{S}}\subset\mathrel{\circ}\mathrel{\circ}\mathrel{\gamma}}\\ &{\mathsf{F}_{\mathsf{V}}=\mathsf{A}_{\mathsf{U}}\mathsf{F}_{\mathsf{U}\mathsf{S}}\mathrel{\circ}\mathrel{\circ}\mathrel{\gamma}}\\ &{\vee\mathsf{2}=\mathsf{R}_{\mathsf{U}}/\mathsf{2}\mathsf{n}-\mathsf{M}_{\mathsf{P}}/\mathsf{n}\mathsf{H}}\\ &{\mathsf{P3}=\mathsf{P2}-\vee\mathsf{2}-\mathsf{F}_{\mathsf{H}}}\\ &{\mathsf{P n}=\mathsf{P(n-1)}-\vee\mathsf{2}-\mathsf{F}_{\mathsf{H}}}\end{array}$$

<!-- batch 28 | page 49 -->

<div style="text-align: center;">Table 5-13Collapse Mechanisms for Rigid Frames with Fixed and Pinned Bases </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td colspan="3" rowspan="2">PLASTIC MOMENT MP</td><td colspan="2"></td></tr><tr><td>COLLAPSEMECHANISM</td><td>FIXED BASES</td></tr><tr><td>1. BEAM MECHANISM</td><td>$\frac{w L^{2}}{16}$</td><td>$\frac{w L^{2}}{16}$</td><td></td><td></td></tr><tr><td>2.BEAM MECHANISM</td><td>$\frac{\omega w H^{2}}{4(2C+1)}$</td><td>$\frac{\alpha w H^{2}}{4(3C+1)}$</td><td>3a. PANEL MECHANISM</td><td>$\frac{\alpha wH^{2}}{2}\times\frac{1}{2+(n-1)C_{1}}\quad(C_{1}\overline{<}2)^{*}\quad\left[\quad\frac{\alpha wH^{2}}{4}\times\frac{1}{1+(n-1)C_{1}+C}\quad(C_{1}\overline{<}2)^{*}\right]$</td></tr><tr><td>3b. PANEL MECHANISM</td><td>$\frac{\alpha w H^{2}}{4n}\left(C_{1}>2\right)^{\star}$</td><td>$\frac{owH^{2}}{2}\times\frac{1}{2(n+C)+(n-1)C_{1}}\quad(C_{1}>2)^{\star}$</td><td>4.COMBINED MECHANISM</td><td>$\frac{w}{8n}\left(\alpha H^{2}+\frac{n}{2}L^{2}\right)$</td></tr><tr><td>5a. COMBINED MECHANISM</td><td>$\frac{\displaystyle\frac{3}{8}\omega w H^{2}}{\displaystyle\frac{1}{2}+\frac{1}{2}+\frac{C_{1}}{2}(n-1)}\quad(C_{1}<2)^{\star}.$</td><td>$\frac{\frac{3}{8}\omega wH^{2}}{\frac{5}{2}C+(n-1)C_{1}+\frac{1}{2}}\quad(C_{1}\bar{<}2)^{\star}$</td><td>5b. COMBINED MECHANISM</td><td>$\frac{\frac{3}{8}\omega wH^{2}}{C+\left(n-\frac{1}{2}\right)}\quad\left(C_{1}>2\right)^{\star}$</td></tr><tr><td>$\left(C_{1}>2\right)^{\star}$</td><td>$\frac{5}{2}C+(n-1)\frac{C_{1}}{2}+\left(n-\frac{1}{2}\right)$</td><td>6. COMBINED MECHANISM</td><td>$\frac{w}{8}\left[3\alpha H^{2}+(n-1)L^{2}\right]$</td><td>$\frac{w}{8}\left[3\alpha H^{2}+(n-1)L^{2}\right]$</td></tr><tr><td>$C+\left(2n-\frac{3}{2}\right)$</td><td>$\frac{5}{2}C+(n-1)\frac{C_{1}}{2}+\left(2n-\frac{3}{2}\right)$</td><td>W</td><td>$M{P</td><td></td></tr><tr><td>$\infty$</td><td>$n={\mathrm{n u m b e r~o f~b a y s}}=1,2,3,\ldots$</td><td>$\mathsf{C M}_{\mathsf{P}}$</td><td>$C_{}_{$</td><td>H</td></tr><tr><td>L</td><td>L</td><td>L</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></tbody></table></body></html></div>


<!-- batch 28 | page 50 -->

Table 5-14Stiffness Factors for Single Story, Multi-Bay Rigid Frames Subjected to Uniform Horizontal Loading 

$$\mathrm{STIFFNESFACTORK}=\frac{EI_{ca}}{H^3}\times C_2\times\left[1+(0.7-0.1\beta)(n-1)\right]$$

$$n=\mathrm{NUMBEROFBAYS}$$

$$\beta=\mathsf{BASE}\cdot\mathsf{FIXITY}\cdot\mathsf{FACTOR}^{\star\star}$$

$$\mathsf{I}_{\mathsf{g}}$$

$$D=\frac{I_{g}/L}{I_{c a}(0.75+0.25\beta)/H}$$

$$I_{c a}=A V E R A G E C O L U M N M O M E N T $$

$$OF\ INETIA=\sum I_c/(n+1)$$


<div style="text-align: center;"><html><body><table border="1"><tr><td rowspan="2">D</td><td colspan="3">$C_{2}$</td></tr><tr><td>$\beta=1.0$</td><td>$\beta=0.5^{\star}$</td><td>$\beta=0$</td></tr><tr><td>0.25</td><td>26.7</td><td>14.9</td><td>3.06</td></tr><tr><td>0.50</td><td>32.0</td><td>17.8</td><td>4.65</td></tr><tr><td>1.00</td><td>37.3</td><td>20.6</td><td>6.04</td></tr></table></body></html></div>


$$C_{2}$$

$$*\beta=1.0$$

$$=0.0 for hinged base $$

where:

E = modulus of elasticity (psi)

lca, lg, Ic = moment of inertia (in.4)

$H=h e i g h t(f e e t)$ 



$L=b a y l e n g t h(f e e t)$ 



<!-- batch 28 | page 51 -->

<div style="text-align: center;">Table 5-15Collapse Mechanisms for Rigid Frames with Supplementary Bracing and Pinned Bases </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>COLLAPSEMECHANISM</td><td colspan="2">PLASTIC MOMENT $M_{P}$</td></tr><tr><td>1. BEAM MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_183_388_418_444.jpg" alt="Image" /></div></td><td colspan="2">$\frac{w L^{2}}{16}$</td></tr><tr><td>2. BEAM MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_181_488_417_541.jpg" alt="Image" /></div></td><td colspan="2">$\frac{\alpha w H^{2}}{4(2C+1)}$</td></tr><tr><td>3a. PANEL MECHANISM 0 <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_181_585_430_640.jpg" alt="Image" /></div></td><td colspan="2">$\left(\frac{c w H^{2}}{2}-m A_{b}f_{d s}H\cos\gamma\right)\frac{1}{2+(n-1)C_{1}}\left(C_{1}<2\right)^{\star}$</td></tr><tr><td>3b.PANEL MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_182_681_432_736.jpg" alt="Image" /></div></td><td colspan="2">$\frac{\alpha w H^{2}}{4\eta}-\frac{m A_{b}f_{d s}H\cos\gamma}{2\eta}$ $\left(C_{1}\overline{{>}}2\right)^{\star}$</td></tr><tr><td>4.COMBINED MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_181_770_432_832.jpg" alt="Image" /></div></td><td colspan="2">$\frac{w}{8n}\left(\alpha H^{2}+\frac{n}{2}L^{2}\right)-\frac{mA_{b}f_{ds}H\cos\gamma}{4n}$</td></tr><tr><td>5a.COMBINED MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_182_874_425_929.jpg" alt="Image" /></div></td><td colspan="2">$\frac{\frac{3}{8}\alpha wH^{2}-\frac{m}{2}A_{b}f_{ds}H\cos\gamma}{C+\frac{1}{2}+\frac{C_{1}}{2}(n-1)}\quad(C_{1}\overline{<}2)^{\star}$</td></tr><tr><td>5b. COMBINED MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_181_985_426_1042.jpg" alt="Image" /></div></td><td colspan="2">$\frac{\frac{3}{8}\omega wH^{2}-\frac{m}{2}A_{b}f_{ds}H\cos\gamma}{C+\left(n-\frac{1}{2}\right)}\quad\left(C_{1}>2\right)^{\star}$</td></tr><tr><td>6.COMBINED MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_181_1096_432_1157.jpg" alt="Image" /></div></td><td>$\frac{w}{8}\left[3\alpha H+(n-1)L\right]-\frac{m}{2}A_{b}f_{ds}H\cos\gamma$ $C+\left(2n-\frac{3}{2}\right)$</td><td></td></tr><tr><td colspan="2">W $M{$ $A_{Fe$ $A_bf$ A{Fa H A L L -L $x w\prod\limits_{i=1}^{n}\frac{i}{i}$ <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_212_1235_488_1331.jpg" alt="Image" /></div></td><td>· of braced bays equivalent static load $n={\mathrm{n u m b e r~o f~b a y s}}=1,2,3,\ldots$ $w=\mathrm{u n i f o r m}$ $m=\mathrm{n u m b e r}$</td></tr></tbody></table></body></html></div>


<div style="text-align: center;">*For $C_{1}=2$ hinges form in the girders and columns at interior joints </div>


<!-- batch 28 | page 52 -->

<div style="text-align: center;">Table 5-16Collapse Mechanisms for Frames with Supplementary Bracing,Nonrigid Girder-to-Column Connections and Pinned Bases.</div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>COLLAPSEMECHANISM</td><td>ULTIMATE CAPACITY</td><td>FRAMING TYPE</td></tr><tr><td>1. BEAM MECHANISM EXTERIOR GIRDER <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_195_429_458_489.jpg" alt="Image" /></div></td><td>$M_{p}=w L^{2}/16$ $M_{p}=w L^{2}/8$ $M_{p}=w L^{2}/12$</td><td></td></tr><tr><td>2. BEAM MECHANISM INTERIOR GIRDER <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_195_559_458_619.jpg" alt="Image" /></div></td><td>$M_{p}=w L^{2}/16$ $M_{p}=w L^{2}/8$</td><td>① ②&③</td></tr><tr><td>3. BEAM MECHANISM BLASTWARD COLUMN <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_194_704_457_764.jpg" alt="Image" /></div></td><td>$M_{p}=\frac{\alpha WH^{2}}{4(2C+1)}$ $M_{p}=\alpha w H^{2}/8$</td><td>&② ③</td></tr><tr><td>4. PANEL MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_194_830_473_891.jpg" alt="Image" /></div></td><td>$A_{b}f_{ds}=\frac{\omega wH}{2m\cos\gamma}-\frac{2M_{p}}{mH\cos\gamma}$ $A_{b}f_{d s}=\alpha w H/2m\cos\gamma$</td><td>①& ② ③</td></tr><tr><td>5. COMBINED MECHANISM <div style="text-align: center;"><img src="../pages/batch 28/imgs/img_in_image_box_195_954_473_1014.jpg" alt="Image" /></div></td><td>$A_{b}f_{ds}=\frac{3\alpha wH}{4m\cos\gamma}-\frac{(2C+1)M_{p}}{mH\cos\gamma}$</td><td>③</td></tr></table></body></html></div>


Girder Framing Type:

①Girder simply supported between columns 

Girder continuous over columns 

Girder continuous over columns and rigidly connected to exterior columns only 

$$-A_{b}f_{\pm}$$

$$w=\mathrm{u n i f o r m} equivalent static load $$