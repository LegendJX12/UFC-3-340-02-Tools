# UFC 3-340-02 Chapter 3: Principles of Dynamic Analysis (incl. Appendix 3)

<!-- Source: batch 11-18.pdf, PaddleOCR PP-StructureV3. Tables reliable; LaTeX equations NOT verified - check against the PDF / ocr_output/text before use. -->


<!-- batch 11 | page 1 -->

UFC 3-340-025 December 2008Change 2, 1 September 2014CHAPTER 3: PRINCIPLES OF DYNAMIC ANALYSIS 

<!-- batch 11 | page 2 -->

## CHAPTER 3 PRINCIPLES OF DYNAMIC ANALYSIS 

CHAPTER 3 PRINCIPLES OF DYNAMIC ANALYSIS .3-1  
INTRODUCTION..3-1  
3-1PURPOSE...3-1  
3-2OBJECTIVE..3-1  
3-3BACKGROUND..3-1  
3-4SCOPE..3-2  
3-5FORMAT..3-3  
3-6CHAPTER CONTENTS .3-4  
BASIC PRINCIPLES .3-4  
3-7GENERAL..3-4  
RESISTANCE—DEFLECTION FUNCTIONS .3-6  
3-8INTRODUCTION..3-6  
3-9ULTIMATE RESISTANCE...3-7  
3-9.1General..3-7  
3-9.2One-Way Elements...3-8  
3-9.3Two-Way Elements...3-8  
3-9.4Openings in Two-Way Elements..3-12  
3-10POST-ULTIMATERESISTANCE,.3-13  
3-11PARTIAL FAILURE AND ULTIMATEDEFLECTION..3-14  
3-12ELASTO-PLASTIC RESISTANCE..3-15  
3-13ELASTO-PLASTIC STIFFNESSES AND DEFLECTIONS..3-16  
3-14RESISTANCE-DEFLECTION FUNCTIONS FOR DESIGN ..3-18  
3-14.1General...3-18  
3-14.2Limited Deflections..3-18  
3-14.3Large Deflections....3-19  
3-15SUPPORT SHEARS OR REACTIONS...3-19  
DYNAMICALLY EQUIVALENT SYSTEMS ..3-73  
3-16INTRODUCTION...3-73

<!-- batch 11 | page 3 -->

3-17DYNAMIC DESIGN FACTORS..3-74  
3-17.1Introduction..3-74  
3-17.2Load, Mass, and Resistance Factors..3-75  
3-17.3Load-Mass Factor...3-78  
3-17.4Natural Period of Vibration...3-81  
DYNAMIC ANALYSIS ..3-86  
3-18INTRODUCTION...3-86  
3-19ELEMENTS WHICH RESPOND TO PRESSURE ONLY AND   
PRESSURE-TIMERELATIONSHIP ..3-86  
3-19.1General...3-86  
3-19.2Analysis By Numerical Methods..3-86  
3-19.3Design Charts for Idealized Loadings...3-92  
3-20ELEMENTS WHICH RESPOND TO IMPULSE .3-101  
3-20.1General..3-101  
3-20.2Determination of Time to Reach Maximum Deflection...3-104

<!-- batch 11 | page 4 -->

## CHAPTER 3 PRINCIPLES OF DYNAMIC ANALYSIS: FIGURES 

Figure 3-1Typical Resistance-Deflection Function for Two-Way   
Element..3-21  
Figure 3-2Idealized Yield Line Locations for Several Two-Way   
Elements .3-22  
Figure 3-3Determination of Ultimate Unit Resistance .3-23  
Figure 3-4Location of Yield Lines for A Two-Way Element with Two   
Adjacent Edges Supported and Two Edges Free (values of   
x).3-24  
Figure 3-5Location of Yield Lines for A Two-Way Element with Two   
Adjacent Edges Supported and Two Edges Free (values of   
y)3-25  
Figure 3-6Location of Symmetrical Yield Lines for Two-Way Element   
with Three Edges Supported and One Edge Free.3-26  
Figure 3-7Location of Unsymmetrical Yield Lines for A Two-Way   
Element with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=0.1)$ .3-27  
Figure 3-8Location of Unsymmetrical Yield Lines for Two-Way   
Element with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=0.3)$ .3-28  
Figure 3-9Location of Unsymmetrical Yield Lines for Two-Way   
Element with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=0.5)$ 3-29  
Figure 3-10Location of Unsymmetrical Yield Lines for Two-Way   
Element with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=0.75)$ .3-30  
Figure 3-11Location of Symmetrical Yield Lines for Two-Way Element   
with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=1.0)$ .3-31  
Figure 3-12Location of Unsymmetrical Yield Lines for Two-Way   
Element with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=1.25)$ .3-32  
Figure 3-13Location of Unsymmetrical Yield Lines for Two-Way   
Element with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=1.5)$ .3-33

<!-- batch 11 | page 5 -->

Figure 3-14Location of Unsymmetrical Yield Lines for Two-Way   
Element with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=1.75)$ 3-34  
Figure 3-15Location of Unsymmetrical Yield Lines for Two-Way   
Element with Three Edges Supported and One Edge Free   
$(X_{2}/X_{1}=2.0)$ .3-35  
Figure 3-16Location of Unsymmetrical Yield Lines for Two-Way   
Element with Three Edges Supported and One Edge Free   
(Values of y)..3-36  
Figure 3-17Location of Symmetrical Yield Lines for Two-Way Element   
with Four Edges Supported .3-37  
Figure 3-18Location of Unsymmetrical Yield Lines for Two-Way   
Element With Four Edges Supported (Values of $\pmb{x}_{1})$ (cd...3-38  
Figure 3-19Location of Unsymmetrical Yield Lines for Two-Way   
Element with Four Edges Supported (Values of y1)..3-39  
Figure 3-20Location of Unsymmetrical Yield Lines for Two-Way   
Element with Four Edges Supported (Values of x/L and y/H).3-40  
Figure 3-21Effects of Openings on Yield Line Locations .3-41  
Figure 3-22Deflection of Two-Way Element..3-42  
Figure 3-23Graphical Summary of Two-Way Elements.3-43  
Figure 3-24Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Two Adjacent Edges Fixed and Two   
Edges Free..3-44  
Figure 3-25Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with One Edge Fixed, an Adjacent Edge   
Simply-Supported and Two Edges Free..3-45  
Figure 3-26Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Two Adjacent Edges Simply  
Supported and Two Edges Fre..3-46  
Figure 3-27Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Three Edges Fixed and One Edge   
Free..3-47  
Figure 3-28Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Two Opposite Edges Fixed, One   
Edge Simply-Supported and One Edge Free ..3-48  
Figure 3-29Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Two Opposite Edges Simply  
Supported, One Edge Fixed, and One Edge Free.3-49

<!-- batch 11 | page 6 -->

Figure 3-30Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Three Edges Simply-Supported and   
One Edge Free.3-50  
Figure 3-31Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Two Adjacent Edges Fixed, One   
Edge Simply-Supported, and One Edge Free .3-51  
Figure 3-32Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Two Adjacent Edges Simply  
Supported, One Edge Fixed, and One Edge Free..3-52  
Figure 3-33Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with All Edges Fixed .3-53  
Figure 3-34Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Two Opposite Edges Fixed and Two   
Edges Simply-Supported.3-54  
Figure 3-35Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Three Edges Fixed and One Edge   
Simply-Supported..3-55  
Figure 3-36Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with All Edges Simply-Supported .3-56  
Figure 3-37Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Two Adjacent Edges Fixed, and   
Two Edges Simply-Supported .3-57  
Figure 3-38Moment and Deflection Coefficients for Uniformly-Loaded,  
Two-Way Element with Three Edges Simply-Supported and   
One Edge Fixed 3-58  
Figure 3-39Resistance-Deflection Functions for Limited Deflections..3-59  
Figure 3-40Resistance-Deflection Functions for Large Deflections ..3-60  
Figure 3-41Determination of Ultimate Support Shear...3-61  
Figure 3-42Typical Single-Degree-of-Freedom System .3-82  
Figure 3-43Determination of Load-Mass Factor in the Plastic Range..3-82  
Figure 3-44Load-Mass Factors in Plastic Range for Two-Way Elements..3-83  
Figure 3-45Acceleration Impulse Extrapolation Method .3-105  
Figure 3-46Discontinuities in the Acceleration Curve..3-105  
Figure 3-47Pressure-Time Function with Two Different Time Intervals ..3-106  
Figure 3-48A Two-Degrees-of-Freedom System..3-106

<!-- batch 11 | page 7 -->

Figure 3-49Maximum Response of Elastic, One-Degree-of-Freedom   
System for Triangular Load.3-107  
Figure 3-50Maximum Response of Elastic, One-Degree-of-Freedom   
System for Rectangular Load.3-108  
Figure 3-51Maximum Response of Elastic, One-Degree-of-Freedom   
System for Gradually Applied Load .3-109  
Figure 3-52Maximum Response of Elastic, One-Degree-of-Freedom   
System for Triangular Pulse Load ..3-110  
Figure 3-53Maximum Response of Elastic, One-Degree-of-Freedom   
System for Sinusoidal Pulse Loads..3-111  
Figure 3-54Maximum Deflection of Elasto-Plastic, One-Degree-of  
Freedom System for Triangular Load.3-112  
Figure 3-55Maximum Response Time of Elasto-Plastic, One-Degree-of  
Freedom System for Triangular Load .3-113  
Figure 3-56Maximum Deflection of Elasto-Plastic, One-Degree-of  
Freedom System for Rectangular Load.3-114  
Figure 3-57Maximum Response Time of Elasto-Plastic, One-Degree-of  
Freedom System for Rectangular Load.3-115  
Figure 3-58Maximum Deflection of Elasto-Plastic, One-Degree-of  
Freedom System for Gradually Applied Load..3-116  
Figure 3-59Maximum Response Time of Elasto-Plastic, One-Degree-of  
Freedom System for Gradually Applied Load.3-117  
Figure 3-60Maximum Deflection of Elasto-Plastic, One-Degree-of  
Freedom System for Triangular Pulse Load .3-118  
Figure 3-62Various Bilinear Triangular Loads 3-120  
Figure 3-63Regions of Figures 3-64 Through 3-26, Labeling of Axis   
and Curves 3-120  
Figure 3-64(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=1.000$   
$C_{2}=1.0)$ 3-121  
Figure 3-65(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.681$   
$C_{2}=1.7)$ 3-123  
Figure 3-66(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $(C_{1}0.464,C_{2}$   
$=1.7)$ 3-124

<!-- batch 11 | page 8 -->

Figure 3-67(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.316$ $C_{2}=1.7)$ 3-126Figure 3-68(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.215,$ $C_{2}=1.7)$ 3-127Figure 3-69(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.147$ $C_{2}=1.7)$ 3-129Figure 3-70(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.100$ $C_{2}=1.7)$ 3-130Figure 3-71(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.056$ $C_{2}=1.7)$ 3-132Figure 3-72(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.032$ $C_{2}=1.7)$ 3-133Figure 3-73(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.018$ $C_{2}=1.7)$ 3-135Figure 3-74(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.010,$ $C_{2}=1.7)$ 3-136Figure 3-75(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.681$ $C_{2}=3.0)$ 3-138Figure 3-76(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.464$ $C_{2}=3.0)$ 3-139Figure 3-77(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.316$ $C_{2}=3.0)$ 3-141Figure 3-78(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.215$ $C_{2}=3.0)$ 3-142Figure 3-79(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.147$ $C_{2}=3.0)$ 3-144

<!-- batch 11 | page 9 -->

Figure 3-80(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.100$ $C_{2}=3.0)$ 3-145Figure 3-81(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.056$ $C_{2}=3.0)$ 3-147Figure 3-82(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.032$ $C_{2}=3.0)$ 3-148Figure 3-83(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.018$ $C_{2}=3.0)$ 3-150Figure 3-84(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,$ $C_{2}=3.0)$ .3-151Figure 3-85(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.750$ $C_{2}=5.5)$ 3-153Figure 3-86(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.562$ $C_{2}=5.5)$ 3-154Figure 3-87(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.422,$ $C_{2}=5.5)$ 3-156Figure 3-88(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.316$ $C_{2}=5.5)$ 3-157Figure 3-89(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.237$ $C_{2}=5.5)$ 3-159Figure 3-90(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.178$ $C_{2}=5.5)$ 3-160Figure 3-91(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.133$ $C_{2}=5.5)$ 3-162Figure 3-92(a)Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.100$ $C_{2}=5.5)$ .3-163

<!-- batch 11 | page 10 -->

Figure 3-93(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.068$   
$C_{2}=5.5)$ 3-165  
Figure 3-94(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.046$   
$C_{2}=5.5)$ 3-166  
Figure 3-95(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032$   
$C_{2}=5.5)$ 3-168  
Figure 3-96(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.022$   
$C_{2}=5.5)$ 3-169  
Figure 3-97(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.015,$   
$C_{2}=6)$ 3-171  
Figure 3-98(a)Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010$   
$C_{2}=5.5)$ 3-172  
Figure 3-99(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.750$   
$C_{2}=10)$ 3-174  
Figure 3-100(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.648$   
$C_{2}=10)$ 3-175  
Figure 3-101(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.562,$   
$C_{2}=10)$ 3-177  
Figure 3-102(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.422,$   
$C_{2}=10)$ .3-178  
Figure 3-103(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.316$   
$C_{2}=10)$ 3-180  
Figure 3-104(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.237$   
$C_{2}=10)$ 3-181  
Figure 3-105(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.178$   
$C_{2}=10)$ .3-183

<!-- batch 11 | page 11 -->

Figure 3-106(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.133$   
$C_{2}=10)$ 3-184  
Figure 3-107(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.100$   
$C_{2}=10)$ 3-186  
Figure 3-108(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.068$   
$C_{2}=10)$ 3-187  
Figure 3-109(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.046$   
$C_{2}=10)$ 3-189  
Figure 3-110(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032$   
$C_{2}=10)$ .3-190  
Figure 3-11(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.022,$   
$C_{2}=10)$ 3-192  
Figure 3-112(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.015$   
$C_{2}=10)$ 3-193  
Figure 3-113(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010$   
$C_{2}=10)$ 3-195  
Figure 3-114(a) Maximum Response of Elasto-Plastic,$\mathrm{O n e-D e g r e e-o f-}$   
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.909$   
$C_{2}=30)$ 3-196  
Figure 3-115(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.866$   
$C_{2}=30)$ 3-198  
Figure 3-116(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.825$   
$C_{2}=30)$ 3-199  
Figure 3-117(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.750$   
$C_{2}=30)$ 3-201  
Figure 3-118(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.715$   
$C_{2}=30)$ .3-202

<!-- batch 11 | page 12 -->

Figure 3-119(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.681$   
$C_{2}=30)$ 3-204  
Figure 3-120(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.648$   
$C_{2}=30)$ .3-205  
Figure 3-121(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.619$   
$C_{2}=30)$ 3-207  
Figure 3-122(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.562$   
$C_{2}=30)$ .3-208  
Figure 3-123(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.511$   
$C_{2}=30)$ .3-210  
Figure 3-124(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.464$   
$C_{2}=30)$ 3-211  
Figure 3-125(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.383$   
$C_{2}=30)$ 3-213  
Figure 3-126(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.316,$   
$C_{2}=30)$ 3-214  
Figure 3-127(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.261$   
$C_{2}=30)$ 3-216  
Figure 3-128(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.215$   
$C_{2}=30)$ .3-217  
Figure 3-129(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.178$   
$C_{2}=30)$ 3-219  
Figure 3-130(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.147$ 7  
$C_{2}=30)$ 3-220  
Figure 3-131(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.121$   
$C_{2}=30)$ .3-222

<!-- batch 11 | page 13 -->

Figure 3-132(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.100$ $C_{2}=30)$ 3-223Figure 3-133(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.075$ $C_{2}=30)$ .3-225Figure 3-134(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.056$ $C_{2}=30)$ .3-226Figure 3-135(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.042$ $C_{2}=30)$ .3-228Figure 3-136(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.032$ $C_{2}=30)$ .3-229Figure 3-137(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.026$ $C_{2}=30)$ 3-231Figure 3-138(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.018$ $C_{2}=30)$ 3-232Figure 3-139(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.013$ $C_{2}=30)$ 3-234Figure 3-140(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.010$ $C_{2}=30)$ 3-235Figure 3-141(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.909$ $C_{2}=100)$ .3-237Figure 3-142(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.866$ 7$C_{2}=100)$ 3-238Figure 3-143(a)  Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.825$ $C_{2}=100)$ 3-240Figure 3-144(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.787$ $C_{2}=100)$ 3-241

<!-- batch 11 | page 14 -->

Figure 3-145(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.750$ $C_{2}=100)$ 3-243Figure 3-146(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.715$ $C_{2}=100)$ .3-244Figure 3-147(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.681$ $C_{2}=100)$ .3-246Figure 3-148(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.648$ $C_{2}=100)$ .3-247Figure 3-149(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.619,$ $C_{2}=100)$ .3-249Figure 3-150(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.590$ $C_{2}=100)$ .3-250Figure 3-151(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.562$ $C_{2}=100)$ .3-252Figure 3-152(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.511$ $C_{2}=100)$ 3-253Figure 3-153(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.464$ $C_{2}=100)$ 3-255Figure 3-154(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.422$ $C_{2}=100)$ .3-256Figure 3-155(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.365$ $C_{2}=100)$ 3-258Figure 3-156(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.316$ $C_{2}=100)$ .3-259Figure 3-157(a) Maximum Response of Elasto-Plastic,$\mathrm{O n e-D e g r e e-o f-}$ Freedom System for Bilinear-Triangular Pulse $C_{1}=0.274$ $C_{2}=100)$ 3-261

<!-- batch 11 | page 15 -->

Figure 3-158(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.261$ $C_{2}=100)$ 3-262Figure 3-159(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.237,$ $C_{2}=100)$ .3-264Figure 3-160(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.215$ $C_{2}=100)$ .3-265Figure 3-161(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.178$ $C_{2}=100)$ .3-267Figure 3-162(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.147,$ $C_{2}=100)$ 3-268Figure 3-163(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.121$ $C_{2}=100)$ 3-270Figure 3-164(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.100$ $C_{2}=100)$ 3-271Figure 3-165(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.075$ $C_{2}=100)$ 3-273Figure 3-166(a)  Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.056$ $C_{2}=100)$ 3-274Figure 3-167(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.042$ $C_{2}=100)$ .3-276Figure 3-168(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.032$ $C_{2}=100)$ 3-277Figure 3-169(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.026$ $C_{2}=100)$ .3-279Figure 3-170(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.018$ $C_{2}=100)$ 3-280

<!-- batch 11 | page 16 -->

Figure 3-171(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.013$ $C_{2}=100)$ 3-282Figure 3-172(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.010$ $C_{2}=100)$ .3-283Figure 3-173(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.909$ $C_{2}=300)$ .3-285Figure 3-174(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.866$ $C_{2}=300)$ .3-286Figure 3-175(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.825,$ $C_{2}=300)$ .3-288Figure 3-176(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.787$ $C_{2}=300)$ 3-289Figure 3-177(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.750$ $C_{2}=300)$ 3-291Figure 3-178(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.715,$ $C_{2}=300)$ 3-292Figure 3-179(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse.$C_{1}=0.681$ $C_{2}=300)$ 3-294Figure 3-180(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.648$ $C_{2}=300)$ 3-295Figure 3-181(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.619$ $C_{2}=300)$ 3-297Figure 3-182(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.590$ $C_{2}=300)$ .3-298Figure 3-183(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.562$ $C_{2}=300)$ .3-300

<!-- batch 11 | page 17 -->

Figure 3-184(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.536$ $C_{2}=300)$ 3-301Figure 3-185(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.511$ $C_{2}=300)$ .3-303Figure 3-186(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.487$ $C_{2}=300)$ 3-304Figure 3-187(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.464$ $C_{2}=300)$ .3-306Figure 3-188(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.422,$ $C_{2}=300)$ .3-307Figure 3-189(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.383$ $C_{2}=300)$ 3-309Figure 3-190(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.365$ $C_{2}=300)$ 3-310Figure 3-191(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.348$ $C_{2}=300)$ 3-312Figure 3-192(a)  Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.316$ $C_{2}=300)$ 3-313Figure 3-193(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.287$ $C_{2}=300)$ .3-315Figure 3-194(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.274$ $C_{2}=300$ .3-316Figure 3-195(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.261$ $C_{2}=300)$ .3-318Figure 3-196(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.237$ $C_{2}=300)$ .3-319

<!-- batch 11 | page 18 -->

Figure 3-197(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangle Pulse $\bar{C_{1}}=0.215,C_{2}$ $=300)$ 3-321Figure 3-198(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.198$ $C_{2}=300)$ .3-322Figure 3-199(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.178$ $C_{2}=300)$ 3-324Figure 3-200(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.162$ $C_{2}=300)$ .3-325Figure 3-201(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.147,$ $C_{2}=300)$ .3-327Figure 3-202(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.133,$ $C_{2}=300)$ 3-328Figure 3-203(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.121$ $C_{2}=300)$ 3-330Figure 3-204(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.110,$ $C_{2}=300)$ 3-331Figure 3-205(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.100$ $C_{2}=300)$ 3-333Figure 3-206(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.091$ $C_{2}=300)$ .3-334Figure 3-207(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.083$ $C_{2}=300)$ 3-336Figure 3-208(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.075$ $C_{2}=300)$ .3-337Figure 3-209(a) Maximum Response of Elasto-Plastic,$\mathrm{O n e-D e g r e e-o f-}$ Freedom System for Bilinear-Triangular Pulse $C_{1}=0.068$ $C_{2}=300)$ 3-339

<!-- batch 11 | page 19 -->

Figure 3-210(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.056$ $C_{2}=300)$ 3-340Figure 3-211(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.046$ $C_{2}=300)$ .3-342Figure 3-212(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.042$ $C_{2}=300)$ 3-343Figure 3-213(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.032$ $C_{2}=300)$ 3-345Figure 3-214(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.026$ $C_{2}=300)$ .3-346Figure 3-215(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.022$ $C_{2}=300)$ 3-348Figure 3-216(a) Maximum Response of Elasto-Plastic, One-Degree-of Freedom System for Bilinear-Triangular Pulse $C_{1}=0.018$ $C_{2}=300)$ 3-349Figure 3-217(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.015,$ $C_{2}=300)$ 3-351Figure 3-218(a)  Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $(C_{1}=0.013$ $C_{2}=300)$ 3-352Figure 3-219(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.010,$ $C_{2}=300)$ .3-354Figure 3-220Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.909$ $C_{2}=1000$ 3-356Figure 3-221Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.866$ $C_{2}=1000)$ 3-357Figure 3-222Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.825$ $C_{2}=1000)$ .3-358

<!-- batch 11 | page 20 -->

Figure 3-223Maximum Response of Elasto-Plastic, One-Degree-of

$Frecdom System for Bilinear-Triangular Pulse(C_1=0.787,$ $C_{2}=1000)$ 3-359Figure 3-224Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.750$ $C_{2}=1000)$ 3-360Figure 3-225(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.715$ $C_{2}=1000)$ 3-361Figure 3-226(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.681$ $C_{2}=1000)$ .3-362Figure 3-227(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.648$ $C_{2}=1000)$ .3-364Figure 3-228(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.619$ $C_{2}=1000)$ 3-365Figure 3-229(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.590$ $C_{2}=1000)$ 3-367Figure 3-230(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.562$ $C_{2}=1000)$ 3-368Figure 3-231(a)  Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.536$ $C_{2}=1000$ 3-370Figure 3-232(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.511$ $C_{2}=1000)$ 3-371Figure 3-233(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.487$ $C_{2}=1000$ 3-373Figure 3-234(a)  Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.464$ $C_{2}=1000)$ 3-374Figure 3-235(a) Maximum Response of Elasto-Plastic,$\mathrm{O n e-D e g r e e-o f-}$ Freedom System for Bilinear-Triangular Pulse $C_{1}=0.422$ $C_{2}=1000)$ 3-376

<!-- batch 11 | page 21 -->

Figure 3-236(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.383$ $C_{2}=1000)$ 3-377Figure 3-237(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.365$ $C_{2}=1000)$ .3-379Figure 3-238(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.348$ $C_{2}=1000)$ 3-380Figure 3-239(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.316$ $C_{2}=1000)$ .3-382Figure 3-240(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.287,$ $C_{2}=1000)$ 3-383Figure 3-241(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.274$ $C_{2}=1000)$ 3-385Figure 3-242(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.261$ $C_{2}=1000)$ 3-386Figure 3-243(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.237$ $C_{2}=1000)$ 3-388Figure 3-244(a)  Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.215,$ $C_{2}=1000)$ 3-389Figure 3-245(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.198$ $C_{2}=1000)$ 3-391Figure 3-246(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.178$ $C_{2}=1000$ 3-392Figure 3-247(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.162,$ $C_{2}=1000)$ 3-394Figure 3-248(a) Maximum Response of Elasto-Plastic,$\mathrm{O n e-D e g r e e-o f-}$ Freedom System for Bilinear-Triangular Pulse $C_{1}=0.147$ $C_{2}=1000)$ 3-395

<!-- batch 11 | page 22 -->

Figure 3-249(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.133$ $C_{2}=1000)$ 3-397Figure 3-250(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.121$ $C_{2}=1000)$ 3-398Figure 3-251(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.110$ $C_{2}=1000)$ 3-400Figure 3-252(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.100$ $C_{2}=1000)$ 3-401Figure 3-253(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.091$ $C_{2}=1000)$ .3-403Figure 3-254(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.083$ $C_{2}=1000)$ 3-404Figure 3-255(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.075$ $C_{2}=1000)$ .3-406Figure 3-256(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.068$ $C_{2}=1000)$ 3-407Figure 3-257(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.056$ $C_{2}=1000$ 3-409Figure 3-258(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.046$ $C_{2}=1000)$ 3-410Figure 3-259(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.042$ $C_{2}=1000$ 3-412Figure 3-260(a) Maximum Response of Elasto-Plastic, One-Degree-ofFreedom System for Bilinear-Triangular Pulse $C_{1}=0.032,$ $C_{2}=1000)$ 3-413Figure 3-261(a) Maximum Response of Elasto-Plastic,$\mathrm{O n e-D e g r e e-o f-}$ Freedom System for Bilinear-Triangular Pulse $C_{1}=0.026$ $C_{2}=1000)$ 3-415

<!-- batch 11 | page 23 -->

Figure 3-262(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.022$   
$C_{2}=1000)$ 3-416  
Figure 3-263(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.018,$   
$C_{2}=1000)$ .3-418  
Figure 3-264(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $C_{1}=0.015$   
$C_{2}=1000)$ 3-419  
Figure 3-265(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.013$   
$C_{2}=1000)$ 3-421  
Figure 3-266(a) Maximum Response of Elasto-Plastic, One-Degree-of  
Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,$   
$C_{2}=1000)$ 3-422  
Figure 3-267Graphical Interpolation 3-424  
Figure 3-268Elastic Rebound of Simple Spring-Mass System .3-425  
Figure 3-269Pressure-Time and Resistance Time Curves for Elements   
Which Respond To Impulse .3-426

<!-- batch 11 | page 24 -->

## CHAPTER 3 PRINCIPLES OF DYNAMIC ANALYSIS: TABLES 

Table 3-1Ultimate Unit Resistances for One-Way Elements ..3-62  
Table 3-2Ultimate Unit Resistances for Two-Way Elements   
(Symmetrical Yield Lines)..3-63  
Table 3-3Ultimate Unit Resistances for Two-Way Elements   
(Unsymmetrical Yield Lines)..3-64  
Table 3-4Post-Ultimate Unit Resistances for Two-Way Elements ...3-65  
Table 3-5General and Ultimate Deflections for One-Way Elements...3-66  
Table 3-6General, Partial Failure, and Ultimate Deflections for Two  
Way Elements .3-67  
Table 3-7Elastic and Elasto-Plastic Unit Resistances for One-Way   
Elements .3-68  
Table 3-8Elastic, Elasto-Plastic and Equivalent Elastic Stiffnesses for   
One-Way Elements .3-69  
Table 3-9Support Shears for One-Way Elements .3-70  
Table 3-10Ultimate Support Shears for Two-Way Elements   
(Symmetrical Yield Lines)3-71  
Table 3-11Ultimate Support Shears for Two Way Elements   
(Unsymmetrical Yield Lines).3-72  
Table 3-12Transformation Factors for One-Way Elements .3-84  
Table 3-13Load-Mass Factors in the Elastic and Elasto-Plastic Ranges   
for Two-Way Elements ..3-85  
Table 3-14Details of Computation By Acceleration Impulse   
Extrapolation Method..3-426  
Table 3-15Figure Numbers Corresponding To Various Combinations   
of $C_{1}$ and $C_{2}$ 3-427  
Table 3-16Response Chart Interpolation..3-428

<!-- batch 11 | page 25 -->

# CHAPTER 3 PRINCIPLES OF DYNAMIC ANALYSIS 

## INTRODUCTION 

## 3 -1PURPOSE

The purpose of this manual is to present methods of design for protective construction used in facilities for development, testing, production, storage, maintenance,modification, inspection, demilitarization, and disposal of explosive materials.

## 3 -2OBJECTIVE

The primary objectives are to establish design procedures and construction techniques whereby propagation of explosion (from one structure or part of a structure to another)or mass detonation can be prevented and to provide protection for personnel and valuable equipment.



The secondary objectives are to:

(1)Establish the blast load parameters required for design of protective structures.



(2)Provide methods for calculating the dynamic response of structural elements including reinforced concrete, and structural steel.



(3)Establish construction details and procedures necessary to afford the required strength to resist the applied blast loads.

(4)Establish guidelines for siting explosive facilities to obtain maximum cost effectiveness in both the planning and structural arrangements, providing closures, and preventing damage to interior portions of structures because of structural motion, shock, and fragment perforation.



## 3 -3BACKGROUND

For the first 60 years of the 20th century, criteria and methods based upon results of catastrophic events were used for the design of explosive facilities. The criteria and methods did not include a detailed or reliable quantitative basis for assessing the degree of protection afforded by the protective facility. In the late 1960's quantitative procedures were set forth in the first edition of the present manual, "Structures to Resist the Effects of Accidental Explosions". This manual was based on extensive research and development programs which permitted a more reliable approach to current and future design requirements. Since the original publication of this manual, more extensive testing and development programs have taken place. This additional research included work with materials other than reinforced concrete which was the principal construction material referenced in the initial version of the manual.

<!-- batch 11 | page 26 -->

Modern methods for the manufacture and storage of explosive materials, which include many exotic chemicals, fuels, and propellants, require less space for a given quantity of explosive material than was previously needed. Such concentration of explosives increases the possibility of the propagation of accidental explosions (one accidental explosion causing the detonation of other explosive materials). It is evident that a requirement for more accurate design techniques is essential. This manual describes rational design methods to provide the required structural protection.

These design methods account for the close-in effects of a detonation including the high pressures and the nonuniformity of blast loading on protective structures or barriers.These methods also account for intermediate and far-range effects for the design of structures located away from the explosion. The dynamic response of structures,constructed of various materials, or combination of materials, can be calculated, and details are given to provide the strength and ductility required by the design. The design approach is directed primarily toward protective structures subjected to the effects of a high explosive detonation. However, this approach is general, and it is applicable to the design of other explosive environments as well as other explosive materials as mentioned above.



The design techniques set forth in this manual are based upon the results of numerous full- and small-scale structural response and explosive effects tests of various materials conducted in conjunction with the development of this manual and/or related projects.

## 3 -4SCOPE

It is not the intent of this manual to establish safety criteria. Applicable documents should be consulted for this purpose. Response predictions for personnel and equipment are included for information.



In this manual an effort is made to cover the more probable design situations. However,sufficient general information on protective design techniques has been included in order that application of the basic theory can be made to situations other than those which were fully considered.



This manual is applicable to the design of protective structures subjected to the effects associated with high explosive detonations. For these design situations, the manual will apply for explosive quantities less than 25,000 pounds for close-in effects. However,this manual is also applicable to other situations such as far- or intermediate-range effects. For these latter cases the design procedures were originally developed for explosive quantities in the order of 500,000 pounds which is the maximum quantity of high explosive approved for aboveground storage facilities in the Department of Defense manual, "Ammunition and Explosives Safety Standards", DOD 6055.09-M. \1\However, DOD 6055.09-M currently addresses explosive quantities of up to 5,000,000Ibs, and the design procedures, in this document, have been extrapolated for designs to resist accidental explosions on ships of 5,000,000 lIbs or more. Although some disasters have involved very high explosive quantities (such as Port Chicago in 1944which involved around 10,000,000 pounds of explosives), limited testing has been completed at such high quantities (e.g. the Middle North Series used 1,000,000 Ibs 

<!-- batch 11 | page 27 -->

TNT, and the Minor Scale and Misty Picture used the equivalent of 8,000,000 Ibs TNT)./1/ Since tests were primarily directed toward the response of structural steel and reinforced concrete elements to blast overpressures, this manual concentrates on design procedures and techniques for these materials. However, this does not imply that concrete and steel are the only useful materials for protective construction. Tests to establish the response of wood, masonry blocks, and plastics, as well as the blast attenuating and mass effects of soil are contemplated. The results of these tests may require, at a later date, the supplementation of these design methods for these and other materials.



Other manuals are available to design protective structures against the effects of high explosive or nuclear detonations. The procedures in these manuals will quite often complement this manual and should be consulted for specific applications.

Computer programs, which are consistent with procedures and techniques contained in the manual, have been approved by the appropriate representative of the US Army, the US Navy, the US Air Force and the Department of Defense Explosives Safety Board (DDESB). These programs are available through the following repositories:

(1)Department of the Army 

Commander and Director 

U.S. Army Engineer Research and Development Center 

Post Office Box 631

Vicksburg, Mississippi 39180-0631

Attn:WESKA 



(2)Department of the Navy 

Commanding Officer 

Naval Facilities Engineering and Expeditionary Warfare Center 

1000 23rd Avenue 

Port Hueneme, California 93043

Attn:Code CI7



(3)Department of the Air Force Aerospace Structures Information and Analysis Center Wright Patterson Air Force Base Ohio 45433

Attn:AFFDL/FBR 

If any modifications to these programs are required, they will be submitted for review by DDESB and the above services. Upon concurrence of the revisions, the necessary changes will be made and notification of the changes will be made by the individual repositories.



## 3 -5FORMAT

This manual is subdivided into six specific chapters dealing with various aspects of design. The titles of these chapters are as follows:

<!-- batch 11 | page 28 -->

Chapter 1Introduction 

Chapter 2Blast, Fragment, and Shock Loads 

Chapter 3Principles of Dynamic Analysis 

Chapter 4Reinforced Concrete Design 

Chapter 5Structural Steel Design 

Chapter 6Special Considerations in Explosive Facility Design 

When applicable,illustrative examples are included in the Appendices.

Commonly accepted symbols are used as much as possible. However, protective design involves many different scientific and engineering fields, and, therefore, no attempt is made to standardize completely all the symbols used. Each symbol is defined where it is first used, and in the list of symbols at the end of each chapter.

## 3 -6CHAPTER CONTENTS

This chapter contains the procedures for analyzing structural elements subject to blast overpressures. These procedures are contained in the next eleven sections; Section 3-7deals with a simplified discussion of the basic principles of dynamics as well as the procedures for calculating the various components used to perform the dynamic analyses. Presented in Sections 3-8 through 3-15 are resistance-deflection functions for various elements including both one- and two-way panels as well as beam elements.These functions include the elastic, elasto-plastic, and plastic ranges of response. In addition, a discussion of dynamic equivalent systems is presented in Sections 3-16 and 3-17. These include single- and multi-degree-of-freedom systems. Presented in this Section also are methods for calculating load and mass factors required to perform the dynamic analyses.



Sections 3-18 through 3-20 include both a step-by-step numerical integration of an element's motion under dynamic loads utilizing the Acceleration-Impulse-Extrapolation Method or the Average Acceleration Method and design charts for idealized loads.Presented also in these Sections are methods for analyzing elements subjected to impulse type loadings; that is, loadings whose durations are short in comparison to the time to reach maximum response of the elements.



## BASIC PRINCIPLES 

## 3 -7GENERAL

The principles used in the analysis of structures under static load will be reviewed briefly, since the same principles are used in the analysis and design of structures subjected to dynamic loads. Two different methods are used either separately or concurrently in static analysis: one is based on the principle of equilibrium, and the other on work done and internal energy stored.



<!-- batch 11 | page 29 -->

Under the application of external loads, a given structure is deformed and internal forces developed in its members. In order to satisfy static equilibrium, the vector sum of all the external and internal forces acting on any free body portion of the structure must be equal to zero. For the equilibrium of the structure as a whole, the vector sum of the external forces and the reactions of the foundation must be equal to zero.

The method based on work done and energy considerations is sometimes used when it is necessary to determine the deformation of a structure. In this method, use is made of the fact that the deformation of the structure causes the point of application of the external load to be displaced. The force then does work on the structure. Meanwhile,because of the structural deformations, potential energy is stored in the structure in the form of strain energy. By the principle of energy conservation, the work done by the external force and the energy stored in the members must be equal. In static analysis,simplified methods such as the method of virtual work and the method of the unit load are derived from the general principle of energy conservation.

In the analysis of statically indeterminate structures, in addition to satisfying the equations of equilibrium, it is necessary to include a calculation of the deformation of the structure in order to arrive at a complete solution of the internal forces in the structure.The methods based on energy considerations such as the method of least work and the method based on Castigliano's theorems are generally used.



For the analysis of structures under dynamic loading, the same two methods are basically used; but the load changes rapidly with time and the acceleration velocity and,hence, the inertia force and kinetic energy are of magnitudes requiring consideration.Thus, in addition to the internal and external forces, the equation of equilibrium includes the inertia force and the equation of dynamic equilibrium takes the form of Newton's equation of motion:

$$F-R=M a $$

where 

$F=t o t a l$ external force as a function of time $R=t o t a l$ internal force as a function of time 

$M={t o t a l}{m a s s}$ 

$a=a c c e l e r a t i o n\;o f\;t h e\;m a s s$ 



As for the principle of conservation of energy, the work done must be equal to the sum of the kinetic energy and the strain energy:

$$W D=K E+S E $$

where 

<!-- batch 11 | page 30 -->

$$\begin{array}{l}{W D=w o r k\:d o n e}\\ {K E=k i n e t i c\:e n e r g y}\\ {S E=s t r a i n\:e n e r g y}\end{array}$$

and the strain energy includes both reversible elastic strain energy and the irreversible plastic strain energy. Thus, the difference between structures under static and dynamic loads is the presence of inertial force (Ma) in the equation of dynamic equilibrium, and of kinetic energy in the equation of energy conservation. Both terms are related to the mass of the structure; hence, the mass of the structure becomes an important consideration in dynamic analysis.



In the dynamic analysis of structures, both the energy balance equation and the force balance equation are applied with explicit description of the external forcing function F,and the internal resisting forcing function R. The difference between these forcing functions is the inertia force as described above. The following is a discussion of the details of how these forces are utilized in the design of structures which respond in the ductile mode.



In the design of a structure to resist the blast from an HE explosion, the total external force acting on the structure can be obtained by the principles discussed Chapter 2. The design method also consists of the determination of the total internal force, i.e. the resistance of the structure required to limit calculated deflections of the individual members and the structure as a whole under the external force (blast loading), to within prescribed maximum values. The determination of the resistance of the individual members of the structure is presented in Sections 3-8 through 3-17. Subsequent sections of this manual present the principles and methods of dynamic analysis and equations, charts, and procedures for design.



## RESISTANCE - DEFLECTION FUNCTIONS 

## 3 -8INTRODUCTION

Under the action of external loads, a structural element is deformed and internal forces set up. The sum of these internal forces tending to restore the element to its unloaded static position is defined as the resistance. The resistance of a structural element is a reactive force associated with the deflection of the element produced by the applied load. It is convenient to consider the resistance as an equivalent load in the same manner as the applied load, but opposite in direction. The variation of the resistance vs.displacement is expressed by a resistance-deflection function and may be represented graphically. An idealized resistance-deflection function for an element spanning in two directions and covering in the complete flexural range to incipient failure is shown in Figure 3-1 (+)



As load is applied to a structural element, the element deflects and, at any instant,exerts a resistance to further deformation, which is a function of its units stiffness K,until the ultimate unit resistance $r_{u}$ (total resistance is $r_{u}$ where A is the element area) of 

<!-- batch 11 | page 31 -->

the element is reached at deflection $X_{p}$ . The initial portion of the resistance-deflection diagram is composed of the elastic and elasto-plastic ranges, each with its corresponding stiffness, the transition from one range to another occurring as plastic hinges are formed at points of maximum stress (yield lines). The number of elastoplastic ranges required before the ultimate resistance of a particular element is reached depends upon the type and number of supports (and the placement of reinforcing steel in reinforced concrete elements). For example a beam with simple supports subjected to uniformly distributed loads needs only one plastic hinge to develop the ultimate resistance (or full plastic strength) of the element; whereas for the same beam fixed at both ends, more than one plastic hinge is required.



In subsequent paragraphs, various procedures, equations and illustrations are presented to enable the designer to determine the resistances of both one- and two-way elements. The procedures outlined apply mainly to reinforced concrete elements and so do the equations appearing in the text, unless the equations are given as part of an illustrative example. However, they can also be used for structural steel elements as well as other structural elements such as aluminum, plastics, etc. Equations have been derived for specific cases most often encountered in practice. These are applicable for structural steel and reinforced concrete elements of uniform thickness in both the horizontal and vertical directions. Before the equations and figures can be used for reinforced concrete element, however, the reinforcing steel across any yield line must have a uniform distribution in both the vertical and horizontal directions; however, the reinforcement across the positive yield lines can be different from that across the negative yield lines and the reinforcing pattern in the vertical direction different from that in the horizontal direction.



Regardless of whether it is a reinforced concrete or structural steel element, any opening in the element must be compact in shape and small in area, compared to the total area of the element.



## 3 -9ULTIMATE RESISTANCE

### 3 -9.1General

The ultimate resistance of an element depends upon:

(1)The distribution of the applied loads.

(2)The geometry of the element (length and width).

(3)The number and type of supports.

(4)The distribution of the moment capacity in the element.

The distribution of the loads depends upon the design range of the element; i.e., high,intermediate or low pressure. For intermediate and low pressure ranges, it can be assumed that the pressure is uniform across the surface of the element although it varies with time. At high pressure ranges, however, the blast loads are variable across the surface of the element. However, for structural steel elements and concrete 

<!-- batch 11 | page 32 -->

elements utilizing laced reinforcement, or for concrete elements with standard shear reinforcement which sustain relatively small deflections, a good estimate of the resulting deflections can be made using the resistance functions conforming to those of uniformly loaded elements.



The other factors that affect the ultimate resistance of an element are predetermined by the requirements of the protective structure (where the element is used) and the magnitude of the blast output.



### 3 -9.2One-Way Elements

The ultimate resistance of a. one-way reinforced concrete element with an elastic distribution of its reinforcing steel is based on the moment capacity at first yield since all critical sections yield simultaneously. For one-way reinforced concrete elements (such as beams or slabs) with non-elastic distribution of reinforcing steel and for structural steel elements, the ultimate resistance is a function of the moment capacity at the first yield plus the added moment capacity due to subsequent yielding at other critical sections.



Values of the ultimate resistance for one-way elements are shown in Table 3-1 (+)where the following symbols are used:

MN = ultimate negative unit moment capacity at the support.

Mp = ultimate positive unit moment capacity at midspan.

L = length 

r = ultimate unit resistance 

Ry = total ultimate resistance 

Table 3-1 (+) applies to both beams and slabs. However, special attention must be paid to the units used for the respective element. The moment capacity of a slab is expressed for a unit strip of the slab (inch-pounds per inch) whereas the total moment capacity (inch-pounds) is considered for a beam. Consequently, the resistance of a slab is expressed in load per unit area (psi) where the resistance of a beam is expressed in load per length along the beam (pounds per inch).



### 3 -9.3Two-Way Elements

The amount of data available on the limit analysis of rectangular steel plates is very limited. However, an elementary approach imagines a mechanism formed of straight yield lines, as is customary in reinforced concrete. This approach for reinforced concrete elements will be considered appropriate for structural steel elements.

In the design of two-way reinforced concrete elements, it is not necessary to define accurately the stress distribution during the initial and intermediate stages of loading since the ultimate load capacity can be readily determined by the use of yield line procedures. The yield line method assumes that after initial cracking of the concrete at points of maximum moment, yielding spreads until the full moment capacity is developed along the length of the cracks on which failure will take place. Several 

<!-- batch 11 | page 33 -->

illustrative examples of the simplified yield or crack lines for two-way elements are illustrated in Figure 3-2 (+).



In using the yield line solution, the initial step is to assume a yield line pattern (as shown in Figure 3-2 (+)) applying the following rules:

(1)The yield lines act as plastic hinges of a collapse mechanism made up of plane segments. They must be straight lines forming axes of rotation for the movements of the segments.



(2)The supports of the slabs will act as axes of rotation. A yield line may form along a fixed support and an axis of rotation will pass over a column.

(3)For compatibility of deformations, a yield line must pass through the intersection of the axes of rotation of the adjacent slab segments.

Tests indicate that the actual location and extent of these lines on reinforced concrete elements differ only slightly at failure from the theoretical ones. Use of the idealized yield lines results in little error in the determination of the ultimate resistance and the error is conservative for design.



The corner sections of two-way elements are stiff in comparison to the remainder of the member; therefore, the reinforcement strains associated with the reduced rotations at these sections will be less. To account for the corner effects, the design of any one particular section of a two-way element should consider a variation of the moment capacity along the yield lines rather than a uniform distribution.

This variation is approximated by taking the full moment capacity along the yield lines,except in the corners where two-thirds of the moment capacity over the lengths described in Figure 3-3 (+) are used. The variation applies to both the negative moment capacities along the supports and the positive moment capacities at the interior. The ultimate unit resistance can be determined from the yield line pattern using either the principle of virtual work or the equations of equilibrium. Each approach has its advantages; in general, the virtual work method is easier in principle, but difficult to manipulate algebraically since it involves differentiating a usually complex mathematical expression for a minimum value of resistance. The equilibrium method, which is used in this manual, also has its disadvantages. Since equilibrium requires that the shear forces acting on each side of a yield line have to be equal and opposite, correction forces (also known as nodal forces) have to be introduced around openings in two-way members and at free edges, and these correction forces may not be available from simple analysis. However, in three of the six cases shown in Figure 3-2 (+), (cases c, e, f),nodal forces exist; but their effects are negligible.



In order to calculate the ultimate unit resistance $r_{u}$ of a two-way element, the equation of equilibrium of each sector formed by the yield lines is expressed in terms of the moments produced by the internal and external forces. The sum of the resisting moments acting along the yield lines (both positive and negative) of each sector is 

<!-- batch 11 | page 34 -->

equated to the moment produced by the applied load about the axis of rotation (support of the sector), assuming that the shear forces are zero along the positive yield lines.

$$\Sigma M_{N}+\Sigma M_{o}=R c=r_{u}A c $$

where 

$M_{N}=\mathrm{~s u m~}$ 'of the ultimate unit resisting moments acting along the support (negative yield lines)



$M_{p}=$ sum of the ultimate unit resisting moments acting along the interior failure lines (positive yield lines)



$R=$ total ultimate resistance of the sector 

$c=$ distance from the centroid of the load to the line of rotation of the sector 

$r_{u}=$ ultimate unit resistance of the sector 

A=area of the sector 

Once the equations of equilibrium are known for all sectors, the ultimate resistance is obtained either by solving the equations simultaneously, or by a trial and error procedure noting that the unit resistance of all sectors must be equal.

To illustrate the above procedure (Equation 3-3), consider the two-way concrete element shown in Figure 3-3 (+) which is fixed on three edges and free on the fourth,and where the nomenclature is as follows:

L=length of element 

$H=$ height of element 

$x=$ yield line location in horizontal direction $\gamma=$ yield line location in vertical direction MyN = ultimate unit negative moment capacity in the vertical direction Mvp = ultimate unit positive moment capacity in the vertical direction MHN = ultimate unit negative moment capacity in the horizontal direction MHp = ultimate unit positive moment capacity in the horizontal direction 

The nomenclature as stated in the paragraph above is strictly applicable to two-way elements which are used as walls. However, when roof slabs or other horizontal elements are under consideration, the preceding nomenclature will also be applicable if the element is treated as being rotated into a vertical position.

The first step in the solution is to assume the location of the yield lines as defined by the coordinates x and y. It should be noted that in some cases, because of geometry, the value of x and y will be known and therefore need not be evaluated. In this example, the negative reinforcement in the horizontal direction at opposite supports is assumed to be equal; therefore, the vertical yield line is located at the center of the span and the value of x is numerically equal to L/2 (a, Figure 3-3 (+)). However, in other cases, neither the 

<!-- batch 11 | page 35 -->

location of x nor y will be known, and the solution will require the determination of both coordinates.



Once the yield lines have been assumed, the distribution of the resisting moments along the yield lines is determined. In the case at hand, the reduced moments, as a result of the increased stiffness at the corners, act over lengths equal to x/2 and y/2 in the horizontal and vertical directions, respectively (a, Figure 3-3 (+)). The equations of equilibrium are then written for each sector with the use of the free body diagrams (b,Figure 3-3). For the triangular sector I:

$$M_{V N}=(2/3)M_{V N}(L/4+L/4)+M_{V N}(L/2)=(5/6)M_{V N}L $$

$$M_{V P}=(2/3)M_{V P}(L/4+L/4)+M_{V P}(L/2)=(5/6)M_{V P}L $$

$$C_{I}=\gamma/3$$

$$R_{I}=(M_{V N}+M_{V P})/C_{I}=[5L(M_{V N}+M_{V P})]/(2y)$$

$$A_{I}=L y/2$$

$$r_{u}(S e c t o r I)=R_{I}/A_{I}=[5(M_{V N}+M_{V P})]/y^{2}$$

For the trapezoidal sector Il, a similar procedure gives 

$$M_{H N}=(2/3)M_{H N}(y/2)+M_{H N}(H-y/2)=M_{H N}(H-y/6)$$

$$M_{H P}=(2/3)M_{H P}(y/2)+M_{H P}(H-y/2)=M_{H P}(H-y/6)$$

$$C_{I I}=(1/3)(L/2)/2(H-y)+H//(H+H-y)=(L(3H-2y)//6(2H-y)$$

$$R_{I I}=(M_{H N}+M_{H P})/C_{I I}=[(6H-y)(2H-y)(M_{H N}+M_{H P})]/L(3H-2y)$$

$$A_{I I}=1/2)(L/2)(H+H-y)=[L(2H-y)]/4$$

$$r_{u}(S e c t o r\;I I)=R_{I I}/A_{I I}=[4(M_{H N}+M_{H P})(6H-y)]/L^{2}(3H-2y)$$

Equations 3-9 and 3-15 are the equations of equilibrium for the triangular (I) and the trapezoidal (Il) sectors, respectively. As mentioned previously, these equations can be solved simultaneously or by a trial and error procedure. In the latter method, values of y are substituted into both equations until $r_{u}$ (sector I) is equal to $r_{u}$ (sector Il)

If a numerical solution based on the above procedure (Equation 3-3) yields negative values for either $x,$ yor r then the assumed yield line location is wrong. In this example,the only other possible yield line pattern $(x\leq L/2)$ would be as shown in Figure 3-2c (+)The solution of Equation 3-3 is universally applicable for any two-way element. If the negative reinforcement in the horizontal direction had been unequal at the opposing supports, the value of $x=L/2$ would have changed, and all three sectors would have had to be considered to determine x, y and hence,had to be considered to determine x, y and hence,$r_{u}$ 



<!-- batch 11 | page 36 -->

Simultaneous solution of Equations 3-9 and 3-15 reveals that the locations of the yield lines are a function of the ratio of the spans L/H and the ratio of the sum of the unit vertical to horizontal moment capacities as follows:

$$\begin{aligned}&r_{u}(Settor I)=r_{u}(Settor II)\\&5(M_{DN}+M_{VP})/y^{2}=[4(M_{HN}+M_{HP})(6H-y)]/L^{2}(3H-2y)\\&L^{2}(M_{DN}+M_{VP})/H^{2}(M_{HN}+M_{HP})=[4y^{2}(6-y/H)]/[5H^{2}(3-2y/H)]\\&(L/H)[(M_{DN}+M_{NN})/(M_{HN}+M_{HP})]^{1/2}=(y/H)[(4(6-y/H)/(5(3-2y/H))]^{1/2}]\\ \end{aligned}$$

Equation 3-17c, which relates the location of the yield lines to the moment capacity of the element, is used to plot Figure 3-6 (+). Knowing the location of the yield lines, the resistance of the two-way element can be obtained from either Equation 3-9 or 3-15which are also presented in Table 3-2 (+)



Using the procedure outlined above, the values of the ultimate unit resistances for several two-way elements with various support conditions are given in Table 3-2 (+) and Table 3-3 (+), the nomenclature confirming to that previously listed. Table 3-2 covers the special cases where opposite supports provide the same degree of restraint thus resulting in symmetrical yield line patterns. Table 3-3 deals with the general cases when the yield line patterns are not symmetrical (that is, when opposite supports provide different restraints). Yield line location ratios x/L and ylH for the same elements are depicted in Figure 3-4 through Figure 3-20.



Figure 3-4 (+) and Figure 3-5 (+) show the location of the yield lines for two-way elements with two adjacent edges supported and the other two free. In each of these figures eight curves are shown which represent different ratios of the positive to the negative moment capacities in both the vertical and horizontal directions. Figure 3-6through Figure 3-16 illustrate the yield line location for two-way elements with three edges supported and one edge free. Figure 3-6 (+) and Figure 3-11 (+) covers the case when the yield line pattern is symmetrical (opposite supports provide the same degree of restraint). Figure 3-17 through Figure 3-20 show the yield line location for two-way elements with four sides supported.



Figure 3-17 (+) covers the special case when opposite supports provide the same degree of restraint, thus resulting in a symmetrical yield pattern. An example illustrating the use of some of these figures is provided in Appendix 3A.



### 3 -9.4Openings in Two-Way Elements

The use of openings in two-way elements, whether for access as a door opening or for visual communication as in the case of observation ports, is permissible with certain reservations. It is difficult to state exact rules concerning openings, but their effect on the design is generally a function of location, size and shape.

<!-- batch 11 | page 37 -->

Small compact openings with approximate areas of less than 5 percent of the panel area located away from regions of high stress can usually be ignored in the design.However, as in the case of conventional design, reinforcement at least equal to the amount interrupted should be placed adjacent to the opening. For example, in Figure 3-21 (+), the openings shown in (a) and (b) can be disregarded. If the opening in (b)were made more rectangular as in (c), then the design must be modified to account for the change in the yield lines and, hence, the change in the resistance. This change in resistance is a function of both the shape and the location of the opening.

Door openings invariably require special analysis because of their size. As depicted in (d), (e) and (f) of Figure 3-21 (+), the presence of door openings causes gross relocations of the yield lines which generally propagate from the corners of the openings. Since the door also sustains the blast loading, concentrated line loads are present around the periphery of such openings. These concentrated loads must be included in the analysis since they change the resistance. As previously outlined for solid elements and for this case also, the yield line locations are assumed and each sector is individually analyzed. The presence of line loads modifies Equation 3-3 to 

$$\Sigma M_{N}+\Sigma M_{n}=r_{u}A c+M_{c}产
$$

where $\mathsf{M}_{\mathsf{c}}$ is the moment of the concentrated loads about the line of rotation of the sector being considered. Solution of elements with openings is most easily accomplished through a trial and error procedure by setting up the simultaneous equations for each sector and assuming various values of x and y until the several values of $\mathsf{r}_{\mathsf{u}}$ agree to within a few percent.



## 3 -10POST-ULTIMATE RESISTANCE

In general, the two-way elements described in this manual exhibit a post-ultimate resistance after partial failure occurs, as indicated in Figure 3-1 (+). Prior to partial failure, the element is spanning in two directions with a resistance equal to the ultimate resistance $r_{u}$ . At a particular deflection, denoted as $X_{1}$ ,failure occurs along one side or two opposite sides, and the element then spans in one direction with the reduced postultimate unit resistance $r_{u p}$ until complete failure occurs at deflection $X_{u}$ . One-way elements do not exhibit this behavior.



The location of the yield lines determines the presence or absence of this range. If the yield lines emanating from the corners of the elements bisect the 90-degree corner angle, then all supports fail simultaneously and there is no post-ultimate range. As previously shown, the location of the yield lines for a particular element is a function of L/H and the ratio of the unit vertical to horizontal moment capacities. Post-ultimate resistances for two-way elements are shown in Table 3-4 (+).

<!-- batch 11 | page 38 -->

## 3 -11

## PARTIAL FAILURE AND ULTIMATE DEFLECTION

Partial failure deflection $X_{\tau}$ ,for two-way elements and ultimate deflections $X_{u}$ for both one-way and two-way elements are a function of the angle of rotation of the element at its supports and the geometry of the sectors formed by the position yield lines.

Once the ultimate resistance $r_{u}$ is reached (full moment capacity developed along the yield lines), the structural element becomes a mechanism which rotates with no further increase in either the moment or curvature between the hinges. For one-way elements,the rotation continues and the deflection increases until either the maximum deflection $X_{m}$ is reached, or failure occurs at $\varTheta_{m a x}$ .The equations for both the maximum deflection $X_{m}$ in the range $0\leq X<X_{\psi}$ and the ultimate deflection $X_{w}$ as a function of the rotation angle Θ are given in Table 3-5 (+) for several one-way elements.

The maximum support rotation at failure,$\varTheta_{m a x}$ , will vary with the material type and geometry of the element. The criteria for partial and incipient failure for concrete and structural steel elements can be found in Chapters 4 and 5 respectively.

For two-way elements, the rotations of all the sectors must be considered in order to define the deflections of partial and incipient failure. Prior to partial failure $(0\leq X_{m}\leq X_{1})$ the maximum deflection is a function of the larger angle of rotation formed along either the vertical or horizontal supports. At deflection $X_{\tau}$ , this larger angle equals $\varTheta_{m a x}$ and failure occurs along this support. Beyond this point, the element spans in one direction until the angle of rotation at the adjacent supports (in the direction opposite to that at which failure has already occurred) reaches $\varTheta_{m a x},$ ,at which time total collapse occurs 

$(X_{m}=X_{u})$ 



To illustrate the above, consider a two-way element (Figure 3-22 (+)) which is fully restrained on four edges and whose positive yield lines are defined by $H/2<x<L/2$ and $y=H/2$ :. The support rotation limit for this element is 12-degrees. Denoting $\Theta_{b}$ as the angle of rotation in the horizontal direction (along vertical supports) and $\Theta_{V}$ as the vertical angle of rotation (along horizontal supports), the maximum deflection $X_{m}$ at the center of the element prior to reaching the deflection $X_{1}$ is 

$$X_{m}=(H\tan\Theta_{v})/2$$

and partial failure occurs at deflection $X_{\tau}$ when $\Theta_{v}=\Theta_{m a x}$ (which is $12^{o}$ in Figure 3-22

$(\pm))$ 



$$X_{1}=(H\tan\Theta_{m a x})/2$$

Referring to Figure 3-22$(\pm)$ , the deflected shape at deflection $X_{1}$ is indicated by the solid line and $\Theta_{H}$ has value β which is defined as 



<!-- batch 11 | page 39 -->

$$\beta=\tan^{-1}(X_1/x)=\tan^{-1}(H\tan\Theta_{\max}/2x)$$

As the element continues to deflect the angle of rotation $\Theta_{H}$ increases, its magnitude becoming equal to 



$$\Theta_{H}=\lambda+\beta F 
$$

where λ is the angular rotation in excess of β. For a two-way element which undergoes partial failure but does reach incipient failure, the maximum deflection in the range $X_{1}\leq$ $X_{m}\leq X_{u}$ becomes 



$$X_{m}=x\tan\Theta_{H}+[(L/2)-x)]\tan(\Theta_{H}-\beta)$$

When $\Theta_{H}$ equal $\varTheta_{m a x},$ ,the ultimate deflection $X_{u}$ at incipient failure is 

$$X_{u}=x\tan\Theta_{m a x}+[(L/2-x)]\tan[\Theta_{m a x}-\tan^{-1}(H\tan\Theta_{m a x}/(2x))]$$

Equations 3-19 through 3-24 are specifically for two-way elements described in Figure 3-22 (+) and will vary for other two-way elements with different material properties and geometry.



The maximum deflection $X_{m}$ for two-way elements with differing edge conditions in the ranges $0\leq X_{m}\leq X_{1}$ _, and $X_{1}<X_{m}\leq X_{u}$ as a function of the rotation angles $\Theta_{H}$ and $\varTheta$ are given in Table 3-6 (+), along with the values of partial failure $(X_{i})$ and ultimate $(X_{u})$ deflections. The support which fails at partial deflection $X_{\tau}$ is also indicated.

## 3 -12ELASTO-PLASTIC RESISTANCE

As stated in Section 3-8,the initial portion of the resistance function (Figure 3-1 (+))generally is composed of an elastic and one or more elasto-plastic ranges. The elastic unit resistance $r_{e}$ is defined as the resistance at which first yield occurs; similarly, the elasto-plastic unit resistance $r_{e p}$ is the resistance at which second yields subsequently occur. Where all hinges form in a member at one time,$r_{e}$ will be equal to the ultimate unit resistance $r_{u};$ where two or more hinges are formed at separate times, the maximum value of $r_{e p}$ will be equal to $r_{u}$ (depending upon the hinges formed, one or more values of $r_{e p}$ may exist).



These resistances for one-way elements are listed in Table 3-7 (+). In those cases where the elasto-plastic resistance is equal to the ultimate resistance, the value can be determined from Table 3-1 (+)



<!-- batch 11 | page 40 -->

The determination of the elasto-plastic resistances of two-way elements is more complicated than that for one-way elements, since the resistance varies with the span ratio and, in the case of reinforced concrete elements, with the placement of the reinforcement. Data for calculating the resistances of two-way elements during the elasto-plastic ranges (graphically summarized in Figure 3-23 (+)) are presented in Figure 3-24 through Figure 3-38.



Figure 3-24 through Figure 3-26 are for a two-way element supported on two adjacent sides and free at the others. Figure 3-27 through Figure 3-32 are for a two-way element supported on three sides and free on the fourth, while Figure 3-33 through Figure 3-38are for elements fixed on four sides. The resistances in each range can readily be determined using the coefficients β, the subscript referring to the points listed in the accompanying illustration.



For example, in Figure 3-27$(\pm)$ ,for an element fixed on three sides and free on the fourth, if the ultimate unit resisting moments $M_{u}$ are known for points 1, 2 and 3, a resistance r for each point can be calculated from 

$$r=M_{u}/\beta H^{2}"$$

where the values of β are found in Figure 3-27 (+). The smallest value of resistance r (say at point 2), corresponds to the first yield and is equal to $r_{e}$ Next,the moments at the remaining two points are computed for this value of $r_{e},$ and the differences between these and the ultimate values are determined. These differences represent the remaining moment capacities available for additional load. At $r_{e}$ , the element's supports become free, fixed, and simply-supported on opposite sides. Using the moment differences and entering Figure 3-29 (+) two values of the change in resistance can be calculated as above, the smaller being Δr and therefore:

$$r_{e o}=r_{e}+\varDelta r -r 
$$

In similar fashion, the resistance at the end of each range can be determined until the ultimate unit resistance $r_{u}$ is reached.



## 3 -13ELASTO-PLASTIC STIFFNESSES AND DEFLECTIONS

The slopes of the elastic and elasto-plastic ranges of the resistance function are defined by the stiffness K of the element:

$$K=r/X $$

<!-- batch 11 | page 41 -->

where r is the unit resistance and X is the deflection corresponding to the value of r. The elastic range stiffness is denoted as $K_{e}$ , the elasto-plastic range as $K_{e p}$ ,while in the plastic range the stiffness is zero.



Typical resistance-deflection functions used for design are shown in Figure 3-39 (+).One- and two-step systems are generally used for one-way elements while two- and three-step systems are used for two-way elements. Two way elements fixed on all four sides will exhibit a four step system. As can be seen from the figure, the elastic range stiffness 



$$K_{e}=r_{e}/X_{e}$$

the elasto-plastic stiffness for a two-step system 

$$K_{e p}=(r_{u}-r_{e})/(X_{p}-X_{e})$$

and for a three-step system, the elasto-plastic stiffnesses 

$$K_{e p}=(r_{e p}-r_{e})/(X_{e p}-X_{e})$$

and 

$$K_{e p}^{\prime}=(r_{u}-r_{e p})/(X_{p}-X_{e p})$$

The elastic and elasto-plastic stiffnesses of one-way elements are given in Table 3-8 (+)as a function of the modulus of elasticity E, moment of inertia I, and span length.Knowing the resistances and stiffnesses, the corresponding elastic and elasto-plastic deflections can be computed from the above equations.



The determination of the elasto-plastic stiffnesses and deflections of two-way elements is more complicated than for one-way elements since another variable, namely, the aspect ratio $L/H,$ , must be considered. For two-way elements, the deflections at the end of each range of behavior is obtained from the γ coefficients presented in Figure 3-24(+) through Figure 3-38 (±). The deflection for each range of behavior is obtained from 

$$X D=\gamma r H^{4}$$

where $D,$ the flexural rigidity of the element is defined as 

$$D=E/(1-\nu^{2})$$

<!-- batch 11 | page 42 -->

E is the modulus of elasticity, I is the moment of inertia per unit width (where the width is perpendicular to span direction), and vis Poisson's ratio. It must be realized that except for the elastic range, the values of X (the displacement) and r in Equation 3-32represent change in deflection and resistance from one range of behavior to another.Therefore, for two-way members the change in deflection and resistance (as previously explained) is obtained from Figure 3-24 through Figure 3-38 and the stiffnesses are computed from Equations 3-28 through 3-33.



#### 3 -14RESISTANCE-DEFLECTION FUNCTIONS FOR DESIGN.3-14.1General

The resistance-deflection function used for design depends upon the maximum permitted deflection according to the design criteria of the element being considered.This maximum deflection $X_{m}$ can be categorized as either limited or large. In the limited deflection range, the maximum deflection of the system is limited to the elastic, elastoplastic and plastic ranges. When the maximum deflection falls in the large deflection range, the response of the system is mainly within the plastic range and the elastic and elasto-plastic ranges need not be considered. The error resulting from the omission of the elastic and elasto-plastic portions in this analysis is negligible.

The support rotation that corresponds to limited deflection varies for the different materials used in protection design. The response criteria for each material are obtained from the chapter that describes the design procedures for that material.

### 3 -14.2Limited Deflections

When designing for limited deflections, the maximum deflection $X_{m}$ of the element is kept within the elastic, elasto-plastic, and limited plastic ranges, and the resistancedeflection function for design takes the form shown in Figure 3-39 a, b, and c (+) for a one-step system, a two-step system, and a three-step system, respectively. The design charts presented in Section 3-19.3 were established for a one-step system; for two- and three-step systems, these charts can be used if the resistance-deflection functions are replaced with equivalent elastic resistance-deflection functions defined by $K_{E}$ and $X_{F}$ as indicated by the dotted lines in Figure 3-39. The equivalent elastic stiffness $K_{F}$ and the equivalent maximum elastic deflection $X_{E}$ are calculated such that the area under the dotted curve is equal to the area under the solid curve, thereby producing the same potential energy in each system. The equivalent maximum elastic deflection $X_{E}$ for the two-step and three-step systems shown is expressed by Equations 3-34 and 3-35,respectively.



$$\begin{aligned}X_{E}&=X_{e}+X_{p}(1-r_{e}/r_{u})\\X_{E}&=x_{e}(r_{ep}/r_{u})+X_{ep}(1-r_{e}/r_{u})+X_{p}(1-r_{ep}/r_{u})\end{aligned}$$

The equivalent elastic stiffness $K_{E}$ in each case is equal to 

<!-- batch 11 | page 43 -->

$$K_{E}=r_{u}X_{E}$$

UFC 3-340-025 December 2008Change 2,1 September 2014One-way elements exhibit one- and two-step resistance deflection curves depending on the type of supports. Consequently, the equivalent elastic stifness $K_{E}$ is given for oneway elements in Table 3-8 (+). The equivalent elastic deflection can then be calculated from Equation 3-36. Two-way elements generally exhibit two- and three-step resistancedeflection curves which are a function of not only the type of supports but also of the aspect ratio L/H of the element. The equivalent elastic deflection $X_{F}$ of the element under consideration must be calculated from Equations 3-34 and 3-35 for two- and three-step systems, respectively. The value of $K_{E}$ for the system can then be obtained from Equation 3-36.



### 3 -14.3Large Deflections

When designing for a large deflection, it can be assumed without significant error that the resistance rises instantaneously from zero to its ultimate value $r_{u}$ at the onset of the blast loading thus neglecting the elastic and elasto-plastic ranges. The design resistance function for one-way elements is approximated by a constant plastic range resistance as shown in Figure 3-40a (+), while for two-way elements, the resistance function becomes that shown in Figure 3-40b (+), where the maximum deflection $X_{m}$ can be either smaller or larger than the partial failure deflection $X_{1}$ 

## 3 -15SUPPORT SHEARS OR REACTIONS

Support shears or reactions are a function the applied load and the maximum resistance attained by an element, its geometry and yield line location. However, for short duration blast loads, the support shears can be reasonably estimated by neglecting the applied load. Therefore, the ultimate support shear can be assumed to be developed when the resistance reaches the ultimate value,$r_{u}$ 

Equations for the ultimate support shears $V_{s}$ for one-way elements are given in Table 3-9 (+). For those cases where an element does not reach its ultimate resistance, the support shears are obtained based upon elastic theory for the actual resistance r attained by the element.



For two-way elements, the ultimate shears acting at each section are calculated by use of the "yield line procedure" previously outlined for the determination of the ultimate resistance $r_{u}$ . The shear along the support is assumed to vary in the same manner as the moment varies (2/3 V at the corners and Velsewhere) to account for the higher stiffness of the corners (Figure 3-41$(\pm))$ ). Since the shear is assumed to be zero along the interior (usually positive) yield lines, the total shear at any section of a sector is equal to the resistance $r_{u}$ times the area between the section being considered and the positive yield lines. Referring to Figure 3-41, the support shear $V_{s V}$ for the triangular sector Iis 



$$(2/3)V_{s V}(L/4+L/4)+V_{s V}(L/2)=r_{u}(L y/2)$$

<!-- batch 11 | page 44 -->

$$V_{s V}=3r_{u}\gamma/5$$

and for the trapezoidal sector Il 

$$\begin{aligned}&(2/3)V_{sH}(y/2)+V_{sH}(H-y/2)=r_{u}(L/2)[(H-y+H)/2]\\ &V_{sH}=[3r_{u}L(2-y/H)]/[2(6-y/H)]\\ \end{aligned}$$

UFC 3-340-025 December 2008Change 2,1 September 2014Values of the ultimate support shears $V_{s H}$ and $V_{s v}$ for several two-way elements derived as above are presented in Table 3-10 (+) and Table 3-11 (+). Table 3-10 gives the ultimate support shears for the case where opposite supports provide the same degree of restraint resulting in symmetrical yield line patterns. Table 3-11 is for completely general situations where opposing supports provide different degrees of restraint and result in the formation of unsymmetrical yield lines. In these cases, the ultimate support shears are not equal at opposing supports. For the situations where the ultimate resistance of an element is not attained, the support shears are less than the ultimate value. The proportion of the total load along each support as well as the distribution of the shears along the support is assumed to be the same as previously cited for the ultimate support shear. Therefore, the support shears corresponding to the resistance r of the element is obtained from the equations presented in Table 3-10 (+) and Table 3-11 (+) by replacing $r_{u}$ with the actual resistance attained $(r_{e},r_{e p},\operatorname{\mathsf{e t c}.})$ 1.

<!-- batch 11 | page 45 -->

<div style="text-align: center;">Figure 3-1Typical Resistance-Deflection Function for Two-Way Element </div>


<div style="text-align: center;"><img src="../pages/batch 11/imgs/img_in_image_box_172_322_1009_767.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">DEFLECTION (X)</div>


<!-- batch 11 | page 46 -->

<div style="text-align: center;">Figure 3-2Idealized Yield Line Locations for Several Two-Way Elements </div>


<div style="text-align: center;"><img src="../pages/batch 11/imgs/img_in_image_box_296_316_891_896.jpg" alt="Image" width="49%" /></div>


<!-- batch 11 | page 47 -->

<div style="text-align: center;">Figure 3-3Determination of Ultimate Unit Resistance </div>


<div style="text-align: center;"><img src="../pages/batch 11/imgs/img_in_image_box_172_323_1004_673.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">b)FREE-BODY DIAGRAMS FOR INDIVIDUAL SECTORS </div>


<!-- batch 12 | page 1 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_191_220_1035_1496.jpg" alt="Image" width="70%" /></div>


<!-- batch 12 | page 2 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_270_227_1036_1494.jpg" alt="Image" width="64%" /></div>


<!-- batch 12 | page 3 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_191_213_1037_1502.jpg" alt="Image" width="71%" /></div>


<!-- batch 12 | page 4 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_269_243_995_1466.jpg" alt="Image" width="60%" /></div>


<!-- batch 12 | page 5 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_262_223_1037_1494.jpg" alt="Image" width="65%" /></div>


<!-- batch 12 | page 6 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_250_235_1010_1475.jpg" alt="Image" width="63%" /></div>


<!-- batch 12 | page 7 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_275_230_1026_1481.jpg" alt="Image" width="63%" /></div>


<!-- batch 12 | page 8 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_267_226_1017_1483.jpg" alt="Image" width="62%" /></div>


<!-- batch 12 | page 9 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_216_231_1005_1477.jpg" alt="Image" width="66%" /></div>


<!-- batch 12 | page 10 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_262_239_995_1469.jpg" alt="Image" width="61%" /></div>


<!-- batch 12 | page 11 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_267_239_995_1467.jpg" alt="Image" width="61%" /></div>


<!-- batch 12 | page 12 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_235_267_996_1488.jpg" alt="Image" width="63%" /></div>


<!-- batch 12 | page 13 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_272_223_1042_1491.jpg" alt="Image" width="64%" /></div>


<!-- batch 12 | page 14 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_194_213_956_1495.jpg" alt="Image" width="63%" /></div>


<!-- batch 12 | page 15 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_272_229_1033_1485.jpg" alt="Image" width="63%" /></div>


<!-- batch 12 | page 16 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_277_231_1033_1481.jpg" alt="Image" width="63%" /></div>


<!-- batch 12 | page 17 -->

<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_191_218_1036_1495.jpg" alt="Image" width="70%" /></div>


<!-- batch 12 | page 18 -->

<div style="text-align: center;">Figure 3-21Effects of Openings on Yield Line Locations </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_222_313_955_755.jpg" alt="Image" width="61%" /></div>


<!-- batch 12 | page 19 -->

<div style="text-align: center;">Figure 3-22 Deflection of Two-Way Element </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_227_322_894_1324.jpg" alt="Image" width="56%" /></div>


<!-- batch 12 | page 20 -->

<div style="text-align: center;">Figure 3-23 Graphical Summary of Two-Way Elements </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_183_327_975_1465.jpg" alt="Image" width="66%" /></div>


<!-- batch 12 | page 21 -->

<div style="text-align: center;">Figure 3-24Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Two Adjacent Edges Fixed and Two Edges Free </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_146_340_1026_1499.jpg" alt="Image" width="73%" /></div>


<!-- batch 12 | page 22 -->

<div style="text-align: center;">Figure 3-25Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with One Edge Fixed, an Adjacent Edge Simply-Supported and Two Edges Free. </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_147_367_1023_1473.jpg" alt="Image" width="73%" /></div>


<!-- batch 12 | page 23 -->

<div style="text-align: center;">Figure 3-26Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Two Adjacent Edges Simply-Supported and Two Edges Free </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_147_344_1024_1452.jpg" alt="Image" width="73%" /></div>


<!-- batch 12 | page 24 -->

<div style="text-align: center;">Figure 3-27 Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Three Edges Fixed and One Edge Free </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_147_340_1025_1432.jpg" alt="Image" width="73%" /></div>


<!-- batch 12 | page 25 -->

<div style="text-align: center;">Figure 3-28Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Two Opposite Edges Fixed, One Edge Simply-Supported and One Edge Free </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_146_369_1025_1465.jpg" alt="Image" width="73%" /></div>


<!-- batch 12 | page 26 -->

<div style="text-align: center;">Figure 3-29Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Two Opposite Edges Simply-Supported, One Edge Fixed, and One Edge Free </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_147_367_1026_1467.jpg" alt="Image" width="73%" /></div>


<!-- batch 12 | page 27 -->

<div style="text-align: center;">Figure 3-30 Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Three Edges Simply-Supported and One Edge Free </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_147_388_1026_1487.jpg" alt="Image" width="73%" /></div>


<!-- batch 12 | page 28 -->

<div style="text-align: center;">Figure 3-31Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Two Adjacent Edges Fixed, One Edge Simply-Supported, and One Edge Free </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_148_366_1048_1341.jpg" alt="Image" width="75%" /></div>


<!-- batch 12 | page 29 -->

<div style="text-align: center;">Figure 3-32Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Two Adjacent Edges Simply-Supported, One Edge Fixed, and One Edge Free </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_148_365_1047_1338.jpg" alt="Image" width="75%" /></div>


<!-- batch 12 | page 30 -->

<div style="text-align: center;">Figure 3-33Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with All Edges Fixed </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_148_338_1047_1310.jpg" alt="Image" width="75%" /></div>


<!-- batch 12 | page 31 -->

<div style="text-align: center;">Figure 3-34Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Two Opposite Edges Fixed and Two Edges Simply-Suported </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_148_338_1046_1310.jpg" alt="Image" width="75%" /></div>


<!-- batch 12 | page 32 -->

<div style="text-align: center;">Figure3-35N Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Three Edges Fixed and One Edge Simply-Supported </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_157_339_1022_1310.jpg" alt="Image" width="72%" /></div>


<!-- batch 12 | page 33 -->

<div style="text-align: center;">Figure 3-36Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with AlI Edges Simply-Supported </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_147_340_1049_1312.jpg" alt="Image" width="75%" /></div>


<!-- batch 12 | page 34 -->

<div style="text-align: center;">Figure 3-37Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Two Adjacent Edges Fixed, and Two Edges Simply-Supported </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_148_343_1045_1317.jpg" alt="Image" width="75%" /></div>


<!-- batch 12 | page 35 -->

<div style="text-align: center;">Figure 3-38Moment and Deflection Coefficients for Uniformly-Loaded, TwoWay Element with Three Edges Simply-Supported and One Edge Fixed </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_148_340_1049_1312.jpg" alt="Image" width="75%" /></div>


<!-- batch 12 | page 36 -->

<div style="text-align: center;">Figure 3-39Resistance-Deflection Functions for Limited Deflections </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_420_317_683_522.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">a)ONE STEP ELASTO-PLASTIC SYSTEM </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_261_589_526_791.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">DEFLECTION </div>


<div style="text-align: center;">b)TW STEP ELASTO-PLASTIC SYSTEM </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_566_591_841_807.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;">C)THREE STEP ELASTO-PLASTIC SYSTEM </div>


<!-- batch 12 | page 37 -->

<div style="text-align: center;">Figure 3-40Resistance-Deflection Functions for Large Deflections </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_341_316_816_547.jpg" alt="Image" width="39%" /></div>


<div style="text-align: center;">a)ONE-WAY ELEMENT </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_chart_box_341_598_848_832.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">b)TWO-WAY ELEMENT </div>


<!-- batch 12 | page 38 -->

<div style="text-align: center;">Figure 3-41Determination of Ultimate Support Shear </div>


<div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_259_321_932_808.jpg" alt="Image" width="56%" /></div>


<!-- batch 12 | page 39 -->

<div style="text-align: center;">Table 3-1Ultimate Unit Resistances for One-Way Elements </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Edge Condition and Loading Diagrams</td><td>Ultimate Resistance</td></tr><tr><td>L</td><td>$r_{u}=\frac{8M_{p}}{L^{2}}$</td></tr><tr><td>↓P L/2 + L/2 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_231_473_478_564.jpg" alt="Image" /></div></td><td>$R_{u}=\frac{4M_{p}}{L}$</td></tr><tr><td><div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_224_597_479_681.jpg" alt="Image" /></div></td><td>$r_{u}=\frac{4(M_{N}+2M_{p})}{L^{2}}$</td></tr><tr><td><div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_237_720_479_802.jpg" alt="Image" /></div></td><td>$R_{u}=\frac{2(M_{N}+2M_{p})}{L}$</td></tr><tr><td></td><td>$r_{u}=\frac{8(M_{N}+M_{p})}{L^{2}}$</td></tr><tr><td>↓P L12</td><td>$R_{u}=\frac{4\left(M_{N}+M_{p}\right)}{L}$</td></tr><tr><td><div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_225_1091_473_1165.jpg" alt="Image" /></div></td><td>$r_{u}=\frac{2M_{N}}{L^{2}}$</td></tr><tr><td>↓P L</td><td>$R_{u}=\frac{M_{N}}{L}$</td></tr><tr><td>P/2 P/2 ↓ ↓ L/3 L/3 L/3 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_227_1312_473_1428.jpg" alt="Image" /></div></td><td>$R_{u}=\frac{6M_{p}}{L}$</td></tr></table></body></html></div>


<!-- batch 12 | page 40 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Table 3-2 Ultimate Unit Resistances for Two-Way Elements (Symmetrical Yield Lines)</td><td colspan="4"></td></tr><tr><td>Edge Conditions</td><td>Yield Line Locations</td><td>Limits</td><td>Ultimate Unit Resistance</td><td></td></tr><tr><td>Two adjacent edges supported and two edges free</td><td>X H 7 L</td><td>×≤L y≤H</td><td>5(MHN+MHP)OR 6LMVN+(5MVP-MVN)X $x^{2}$ $H^{2}{3}}-2x) $5(MVN+MvP) 6HMHN+(5MHP-MHN)y OR $y^{2}$ $L{2}{3H-2y)</td><td></td></tr><tr><td>Three edges supported and one edge free</td><td>X X 2 3 X 1 2 3 L</td><td>×≤L/2 y≤H$</td><td>5(M{HN+MHP)OR 2M_n(3L-x)+10xMvP $x^{}$ $H_{2}{3 }-4x$ 5(Mv{n}+MvP)OR 4(MHN+MHP)(6H-y) $y^{2}$ $^²{2}{3H}-2y</td><td>Four edges supported</td></tr><tr><td>y ≤H/2$</td><td></td><td></td><td></td><td></td></tr></tbody></table></body></html></div>


Seee neeee e 

ee eeee 

12-200-02



<!-- batch 12 | page 41 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>Edge Conditions</td><td>Yield Line Locations</td><td>Limits</td><td>Ultimate Unit Resistance</td></tr></thead><tbody><tr><td>Two adjacent edges supported and two edges free</td><td>X L</td><td>×≤L y≤H</td><td>Same as in Table 3-2(+)</td></tr><tr><td>Three edges supported and one edge free</td><td>X X 2 3 1 x 1 2 H → 3 L</td><td>$x ≤\L2 y≤H$</td><td>5（MHN+MHP1)OR5MHN₃+MHPOR (5MP-MvN2）(x₁1+x₂2)+6MvN2L $x {\rac{}{2}$ $H{²2}{3L-2x₁}-2x2}$</td></tr><tr><td>Four edges supported</td><td>x1 x2 1 3 2 X . 2 H 3 4 2 L</td><td>x≤L2 y≤H/2$</td><td>(MVN1+MVP)(6L-x₁-x2) OR (MVN2+MVP)(6L-x₁1-x2)$ $y^{²}3L-2x_{1}-2x2$ (H-y){²(3L-2x{1}-2x2)$ 5(M_HN_{1+M_HP) OR 5(MHN2+M_HP) OR $x_{r{}{2}$ $x{22}$ 2 $5(M_N1}+MvP)OR $5(MV}N{2+MvP) $y_}{2}$ $y_{2}$ (MHN1+MHP)(6H-yY1-y2)ORMHN2+MHP)（6H-y1-Y2) OR $x^²2}（3H-2y_₁1-2y{2$ (L-x)²(3H-2y_₁-2y_2)</td></tr></tbody></table></body></html></div>


<div style="text-align: center;">ce  ree rae ee r  - e </div>


Seee neeee e 

ee eee 

12220-020



<!-- batch 12 | page 42 -->

<div style="text-align: center;">Table 3-4Post-Ultimate Unit Resistances for Two-Way Elements </div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>Edge Conditions</td><td>Yield Line Locations</td><td>Limits</td><td>Post-Ultimate Unit Resistance</td></tr><tr><td>Two adjacent edges supported and two edges free</td><td>L $\left|\begin{matrix}\frac{x}{2}\\ \end{matrix}\right|$ <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_404_554_617_684.jpg" alt="Image" /></div> <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_432_380_589_507.jpg" alt="Image" /></div></td><td>$y>L$ $y<L$ $x\geq H$ $x\leq H$</td><td>$2M_{V N}/H^{2}$ $2M_{H N}/L^{2}$ $2M_{H N}/L^{2}$ $2M_{V N}/H^{2}$</td></tr><tr><td>Three edges supported and one edge free</td><td>X X x H L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_432_722_597_852.jpg" alt="Image" /></div> <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_403_872_625_1026.jpg" alt="Image" /></div></td><td>$y>L/2$ $y<L/2$ $x\leq H$ $x\geq H$</td><td>$8(M_{H N}+M_{H P})/L^{2}$ $8(M_{H N}+M_{H P})/L^{2}$ $2M_{V N}/H^{2}$ $2M_{V N}/H^{2}$</td></tr><tr><td>Four edges supported</td><td>X X X H L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_433_1053_624_1190.jpg" alt="Image" /></div> <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_404_1206_627_1367.jpg" alt="Image" /></div></td><td>$y<L/2$ $y>L/2$ $x<H/2$ $x>H/2$</td><td>$8(M_{V N}+M_{V P})/H^{2}$ $8(M_{V N}+M_{V P})/L^{2}$ $8(M_{H N}+M_{H P})/L^{2}$ $8(M_{H N}+M_{H P})/H^{2}$</td></tr></table></body></html></div>


<!-- batch 12 | page 43 -->

<div style="text-align: center;">Table 3-5General and Ultimate Deflections for One-Way Elements </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Edge Conditions and Loading Diagrams</td><td>Maximum Deflection, $\pmb{X}_{m}$</td><td>Ultimate Deflection, $\pmb{X}_{u}$</td></tr><tr><td>L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_267_400_510_456.jpg" alt="Image" /></div></td><td>${\frac{L}{2}}{\tan\theta}$</td><td>$\frac{L}{2}\mathrm{t a n}\theta_{\mathrm{m a x}}$</td></tr><tr><td>↓P L/2 L/2 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_266_488_511_579.jpg" alt="Image" /></div></td><td>${\frac{L}{2}}{\tan\theta}$</td><td>$\frac{L}{2}\mathrm{t a n}\theta_{\mathrm{m a x}}$</td></tr><tr><td>8 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_259_615_511_697.jpg" alt="Image" /></div></td><td>${\frac{L}{2}}{\tan\theta}$</td><td>$\frac{L}{2}\mathrm{t a n}\theta_{\mathrm{m a x}}$</td></tr><tr><td>↓P <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_258_729_513_814.jpg" alt="Image" /></div></td><td>${\frac{L}{2}}{\tan\theta}$</td><td>$\frac{L}{2}\mathrm{t a n}\theta_{\mathrm{m a x}}$</td></tr><tr><td><div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_259_838_522_916.jpg" alt="Image" /></div></td><td>${\frac{L}{2}}{\tan\theta}$</td><td>$\frac{L}{2}\mathrm{t a n}\theta_{\mathrm{m a x}}$</td></tr><tr><td>2 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_258_945_524_1026.jpg" alt="Image" /></div></td><td>${\frac{L}{2}}{\tan\theta}$</td><td>$\frac{L}{2}\mathrm{t a n}\theta_{\mathrm{m a x}}$</td></tr><tr><td><div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_260_1067_506_1137.jpg" alt="Image" /></div></td><td>$L{\tan\theta}$</td><td>$L\mathrm{t a n}\theta_{\mathrm{m a x}}$</td></tr><tr><td>L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_259_1165_530_1246.jpg" alt="Image" /></div></td><td>$L{\tan\theta}$</td><td>$L\mathrm{t a n}\theta_{\mathrm{m a x}}$</td></tr><tr><td>$\frac{\frac{p/2}{\downarrow}}{\frac{\frac{p/2}{\downarrow}}{\frac{p/2}{\downarrow}}+\frac{\frac{p/2}{\downarrow}}{\frac{p/2}{\downarrow}}}$</td><td>${\frac{L}{3}}{\tan\theta}$</td><td>$\frac{L}{3}\mathrm{{t a n}}\theta_{\mathrm{{m a x}}}$</td></tr></tbody></table></body></html></div>


<!-- batch 12 | page 44 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td rowspan="3">Yield Line Location</td><td rowspan="3">Maximum Deflection,Xm</td><td rowspan="3">Partial Failure Deflection, X1</td><td colspan="2">Support Failing Deflection $X_{1$ H</td><td rowspan="3">Edge Conditio ns</td><td rowspan="3">Limits</td><td rowspan="3">Ultimate Deflection, Xu</td></tr><tr><td>(0<xm<x1)</td><td>(x{1}<xm<x$ Htanθ xtanθH+(L-x)tanθH-tan</td></tr><tr><td></td><td></td></tr><tr><td rowspan="4">x</td><td>xtan θmax$ Htan^θmax}$</td><td>Htanθmax$ xtanθmax+(L-x)tanθmax-tan</td><td>×≤H ×≥H</td><td>xtanθ_$ Htanθ ytanθ</td><td>tanθy$ x1H</td><td>tanθmax x/H</td><td>Two adjacent</td></tr><tr><td>edges supported and two edges free</td><td>Ltan^θmax$ ytanθmax+(H-y)tanθmax-tan</td><td>LtanθH ytanθ +(H-y)tan|θv −tan</td><td>ytanθmax$ Ltanθmax$</td><td>y≤L y≥L</td><td></td><td></td></tr><tr><td>H</td><td>Y L 1</td><td>tanθH 7 y/L</td><td>tanθmax 1 y/L</td><td>LtanθH xtanθ Htanθ</td><td>Htanθ 2 x tan θ_ + -x xtan θ-tan</td><td>xtan θmax$ Htan θm_ax$ ytanθmax$</td></tr><tr><td>x + x</td><td>×≤H ×≥H</td><td>H L</td><td>tanθ 7 x/H</td><td>xtan θmax + 2</td><td>tanθmax$ ×/H</td><td>Three edges supported and one edge free</td></tr><tr><td rowspan="4">x H</td><td>ytanθ</td><td>y≤L2$ y≥L2$</td><td>L H</td><td>LtanθH 2</td><td>tanθ_ 2y/L</td><td>Ltanθmax$ 2 x tan θ max$</td><td>tanθ_max 2y/L</td></tr><tr><td>L</td><td>Htanθ}$ 2 $x- e-θ e</td><td>Htanθmax}$ 2 tan θmax -tan-</td><td>4 -</td><td>Lx x ≤H/2 7 × ≥H/2</td><td>xtanθ_$ Htanθy}$ 2</td><td>H L</td></tr><tr><td>Htanθmax}$ 2</td><td>乙-7 +H_θue{x$</td><td>θu V 2x/H</td><td>2-7 xtanθmax +$ -x</td><td>xeθe 1 2x/H</td><td>Four edges supported</td><td></td></tr><tr><td>y≤L2$ y≥L2</td><td>LtanθH 2</td><td>ytanθmax$ Ltanθmax 2</td><td>Ltanθmax$ 2 □</td><td>X H</td><td>ytanθ LtanθH 2</td><td>L H</td></tr><tr><td>$H$ A- 2</td><td>Houe 2y/L</td><td>2H -y</td><td>xeθe 2y/L</td><td>+u</td><td>e-θe</td><td>ytan^θ_max +$</td><td>tan θmax -tan-</td></tr></tbody></table></body></html></div>


<div style="text-align: center;">ee rer  oe r  arerce - e </div>


Cee eee e 

e eeee 

12-220-020



<!-- batch 12 | page 45 -->

<div style="text-align: center;">Table 3-7Elastic and Elasto-Plastic Unit Resistances for One-Way Elements </div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>Edge Conditions and Loading Diagrams</td><td>Elastic Resistance, ■ $r_{e}$</td><td>Elasto-Plastic Resistance, $r_{e p}$</td></tr><tr><td>L</td><td>$r_{u}$</td><td></td></tr><tr><td>↓P L/2 中 L/2 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_228_495_475_586.jpg" alt="Image" /></div></td><td>$R_{u}$</td><td></td></tr><tr><td>L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_221_618_475_700.jpg" alt="Image" /></div></td><td>$\frac{8M_{_N}}{L^{2}}$</td><td>$r_{u}$</td></tr><tr><td>↓P L/2 L/2 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_219_743_476_827.jpg" alt="Image" /></div></td><td>$\frac{16M_{_N}}{3L}$</td><td>$R_{u}$</td></tr><tr><td><div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_220_863_485_943.jpg" alt="Image" /></div></td><td>$\frac{12M_{_N}}{L^{2}}$</td><td>$r_{u}$</td></tr><tr><td>↓P L/2 L/2</td><td>$\frac{8M_{_N}}{L}$</td><td>$R_{u}$</td></tr><tr><td>L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_222_1106_470_1178.jpg" alt="Image" /></div></td><td>$r_{u}$</td><td></td></tr><tr><td>↓P L</td><td>$R_{u}$</td><td></td></tr><tr><td>P/2 P/2 L/3 L/3 L/3 U <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_226_1298_470_1413.jpg" alt="Image" /></div></td><td>$R_{u}$</td><td></td></tr></table></body></html></div>


<!-- batch 12 | page 46 -->

<div style="text-align: center;">Table 3-8Elastic, Elasto-Plastic and Equivalent Elastic Stiffnesses for OneWay Elements </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Edge Conditions and Loading Diagrams</td><td>Elastic Stiffness, $K_{e}$</td><td>Elasto- Plastic Stiffness, 国 $K_{e p}$</td><td>Equivalent Elastic Stiffness, $K_{E}$</td></tr><tr><td>L</td><td>$\frac{384E I}{5L^{4}}$</td><td></td><td>384EI $\boxed{5L^{4}}$</td></tr><tr><td>↓P L/2 ↓ L/2</td><td>48EI $\overline{{L^{3}}}$</td><td></td><td>$\frac{48E I}{L^{3}}$</td></tr><tr><td>L</td><td>$\frac{185E I}{L^{4}}$</td><td>$\frac{384E I}{5L^{4}}$</td><td>$\frac{160E I}{L^{4}}^{\star}$</td></tr><tr><td>↓P L/2 + L/2</td><td>$\frac{107E I}{L^{3}}$</td><td>$\frac{48E I}{L^{3}}$</td><td>$\frac{106E I}{L^{3}}^{^{\star}}$</td></tr><tr><td>L</td><td>$\frac{384E I}{L^{4}}$</td><td>$\frac{384E I}{5L^{4}}$</td><td>$\frac{307E I}{L^{4}}^{\star}$</td></tr><tr><td>↓P L/2 中 L/2</td><td>$\frac{192E I}{L^{3}}$</td><td>$\frac{48E I}{L^{3}}^{\star\star}$</td><td>$\frac{192E I}{L^{3}}^{^{\star}}$</td></tr><tr><td>L</td><td>$\frac{8E I}{L^{4}}$</td><td></td><td>$\frac{8E I}{L^{4}}$</td></tr><tr><td>↓P L</td><td>$\frac{3E I}{L^{3}}$</td><td></td><td>$\frac{3E I}{L^{3}}$</td></tr><tr><td>$\frac{\frac{p/2}{\downarrow}\frac{p/2}{\downarrow}}{\frac{\frac{p}{p}}{\downarrow}\frac{p}{p}\frac{p/2}{\downarrow}\frac{p}{p}}$</td><td>$\frac{56.4E I}{L^{3}}$</td><td></td><td>$\frac{156.4E I}{L^{3}}$</td></tr></tbody></table></body></html></div>


<!-- batch 12 | page 47 -->

<div style="text-align: center;">Table 3-9Support Shears for One-Way Elements </div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>Edge Conditions and Loading Diagrams</td><td>Support Reactions, $v_{s}$</td></tr><tr><td>L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_289_421_533_477.jpg" alt="Image" /></div></td><td>$\frac{r_{u}L}{2}$</td></tr><tr><td>↓P L/2 十 L/2 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_287_517_533_610.jpg" alt="Image" /></div></td><td>$\frac{R_{u}}{2}$</td></tr><tr><td>∞ L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_278_650_532_735.jpg" alt="Image" /></div></td><td>L.Reaction R.Reaction $\frac{3r_{u}L}{8}$ $\frac{5r_{u}L}{8}$</td></tr><tr><td>↓P L/2 十 L/2 <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_283_800_532_884.jpg" alt="Image" /></div></td><td>L.Reaction R.Reaction $\frac{5R_{u}}{16}$ $\frac{11R_{u}}{16}$</td></tr><tr><td></td><td>$\frac{r_{u}L}{2}$</td></tr><tr><td>↓P L/2 L/2</td><td>$\frac{R_{u}}{2}$</td></tr><tr><td>L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_281_1162_527_1231.jpg" alt="Image" /></div></td><td>$r_{u}L$</td></tr><tr><td>⊥P L <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_280_1268_551_1350.jpg" alt="Image" /></div></td><td>$R_{u}$</td></tr><tr><td>P/2 ↓ $\frac{4}{10}\times\frac{1/3}{10}=\frac{1/3}{10}=\frac{1/3}{10}=\frac{4}{10}$ $\mathbb{P}/2$ <div style="text-align: center;"><img src="../pages/batch 12/imgs/img_in_image_box_284_1378_527_1490.jpg" alt="Image" /></div></td><td>$\frac{R_{u}}{2}$</td></tr></table></body></html></div>


<!-- batch 12 | page 48 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td colspan="2">Table 3-10 Ultimate Support Shears for Two-Way Elements (Symmetrical Yield Lines)</td><td colspan="4"></td></tr><tr><td>Edge Conditions</td><td colspan="2">Yield Line Locations</td><td>Limits</td><td>Horizontal shear, VsH</td><td>Vertical shear, VsV</td></tr><tr><td>Two adjacent edges supported and two edges free</td><td>x VsH| VsV L</td><td>x≤L y≤H</td><td></td><td></td><td></td></tr><tr><td>cee eee pue peuoddns e ee </td><td>X X X ' H 1 I</td><td>$H5$</td><td></td><td></td><td></td></tr><tr><td>supported</td><td>x X X 4 H \ L</td><td></td><td></td><td>i: −</td><td></td></tr></tbody></table></body></html></div>


Se ee e 

ee 

12-220-020



<!-- batch 12 | page 49 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>Edge Conditions</td><td colspan="2">Yield Line Locations</td><td>Limits</td><td>Horizontal shear, VsH</td><td>Vertical shear, Vs</td></tr></thead><tbody><tr><td>Two adjacent edges supported and two edges free</td><td colspan="2">x L</td><td>X≤L y≤H</td><td>Same as in Table 3-10 (+)</td><td>Same as in Table 3-10 (+)</td></tr><tr><td rowspan="2">Three edges supported and one edge free</td><td>x 1 $x2 T 1 2 3 X 1 2 心 3 L</td><td>L12 $x _{1$ 2 $X_{2$ y≤H</td><td rowspan="2">3x{1$ 5 $3x_{2$ 5 $3r{4x(2H-y) 6H-y 3ru(L-x)(2H-y) 6H-y</td><td rowspan="2">3r₄}H(2L-x_{1}-x2) 6L-X_{₁-_2$</td><td rowspan="2"></td></tr><tr><td></td><td></td></tr><tr><td>Four edges supported</td><td>x1 1x2 1 2 X H 3 4 2 可 L</td><td>L-2L-2 $ _{1$ $x{2 c H-2H-2 $y_{1}$ $y_{2$</td><td>3rux(2H-y_{1-y2) 6H-y_{₁1-y_2}$ 3rux(L-x)(2H-y₁1-y2) 6H-y_{₁-y_2}$</td><td>$3ru_1}$ 5 $3r{y_{2}$ 5</td><td></td></tr></tbody></table></body></html></div>


<div style="text-align: center;">c re re e r re ee e e 1 e </div>


Seees e 

e eeeee 

12-220-020



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

<!-- batch 14 | page 1 -->

<div style="text-align: center;">Figure 3-65(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.681,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_216_337_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-65(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.681,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_916_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 2 -->

<div style="text-align: center;">Figure 3-65(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.681,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_339_966_844.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-66(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}0.464,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_927_964_1433.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 3 -->

<div style="text-align: center;">Figure 3-66(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse (C1 0.464, C2 = 1.7)</div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_322_963_834.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-66(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse (C1 0.464,$C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_217_954_963_1456.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 4 -->

<div style="text-align: center;">Figure 3-67(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.316,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_340_958_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-67(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.316,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_918_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 5 -->

<div style="text-align: center;">Figure 3-67(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-68(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.215,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_231_926_980_1433.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 6 -->

<div style="text-align: center;">Figure 3 68(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.215,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_220_332_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-68(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.215,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_932_966_1439.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 7 -->

<div style="text-align: center;">Figure 3-69(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.147,\;C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_334_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-69(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.147,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_232_919_980_1434.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 8 -->

<div style="text-align: center;">Figure 3-69(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.147,C2=1.7)$ ,cont.</div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_334_967_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-70(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.100,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_920_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 9 -->

<div style="text-align: center;">Figure 3-70(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_220_332_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-70(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_922_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 10 -->

<div style="text-align: center;">Figure 3-71(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.056,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_334_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-71(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_918_961_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 11 -->

<div style="text-align: center;">Figure 3-71(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_334_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-72(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 12 -->

<div style="text-align: center;">Figure 3-72(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.032,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_332_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-72(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_922_970_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 13 -->

<div style="text-align: center;">Figure 3-73(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.018,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_335_962_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-73(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.018,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_918_961_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 14 -->

<div style="text-align: center;">Figure 3-73(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.018,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_333_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-74(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,C_{2}=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 15 -->

<div style="text-align: center;">Figure 3-74(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_332_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-74(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=1.7)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_210_919_972_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 16 -->

<div style="text-align: center;">Figure 3-75(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.681,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_333_965_841.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-75(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.681,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_217_915_966_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 17 -->

<div style="text-align: center;">Figure 3-75(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.681,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-76(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.464,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_227_925_984_1433.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 18 -->

<div style="text-align: center;">Figure 3-76(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.464,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_326_966_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-76(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.464,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 19 -->

<div style="text-align: center;">Figure 3-77(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.316,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_335_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-77(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_918_966_1435.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 20 -->

<div style="text-align: center;">Figure 3-77(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_335_967_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-78(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.215,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_919_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 21 -->

<div style="text-align: center;">Figure 3-78(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.215,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_329_967_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-78(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.215,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_922_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 22 -->

<div style="text-align: center;">Figure 3-79(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.147,\;C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_333_964_841.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-79(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.147,\;C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_217_918_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 23 -->

<div style="text-align: center;">Figure 3-79(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.147,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_335_967_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-80(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.100,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 24 -->

<div style="text-align: center;">Figure 3-80(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.100,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_216_329_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-80(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_922_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 25 -->

<div style="text-align: center;">Figure 3-81(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.056,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_333_964_841.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-81(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.056,\;C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_916_964_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 26 -->

<div style="text-align: center;">Figure 3-81(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.056,\;C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_333_971_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-82(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_924_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 27 -->

<div style="text-align: center;">Figure 3-82(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,\;C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_332_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-82(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_210_919_972_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 28 -->

<div style="text-align: center;">Figure 3-83(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.018,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_333_964_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-83(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.018,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_918_961_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 29 -->

<div style="text-align: center;">Figure 3-83(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.018,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_334_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-84(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,C_{2}=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 30 -->

<div style="text-align: center;">Figure 3-84(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.010,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_330_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-84(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=3.0)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_922_970_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 31 -->

<div style="text-align: center;">Figure 3-85(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.750,\;C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_334_966_841.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-85(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.750,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_217_918_966_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 32 -->

<div style="text-align: center;">Figure 3-85(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.750,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_332_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-86(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.562,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_919_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 33 -->

<div style="text-align: center;">Figure 3-86(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.562,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_329_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-86(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.562,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_211_920_970_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 34 -->

<div style="text-align: center;">Figure 3-87(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.422,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_333_964_841.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-87(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.422,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_917_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 35 -->

<div style="text-align: center;">Figure 3-87(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.422,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-88(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.316,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_925_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 36 -->

<div style="text-align: center;">Figure 3-88(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.316,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_216_329_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-88(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 37 -->

<div style="text-align: center;">Figure 3-89(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.237,\;C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_332_966_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-89(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.237,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_217_917_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 38 -->

<div style="text-align: center;">Figure 3-89(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.237,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_211_330_971_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-90(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.178,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 39 -->

<div style="text-align: center;">Figure 3-90(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.178,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_216_329_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-90(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.178,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_925_966_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 40 -->

<div style="text-align: center;">Figure 3-91(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.133,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_335_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-91(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.133,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_918_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 41 -->

<div style="text-align: center;">Figure 3-91(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.133,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-92(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.100,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_922_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 42 -->

<div style="text-align: center;">Figure 3-92(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=5.5)$ EMY $(C1=0.100,C2=5.5)$ Ta $(C1=0.100,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_322_963_834.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-92(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_925_968_1435.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 43 -->

<div style="text-align: center;">Figure 3-93(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.068,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_334_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-93(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.068,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_917_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 44 -->

<div style="text-align: center;">Figure 3-93(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.068,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_334_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-94(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.046,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 45 -->

<div style="text-align: center;">Figure 3-94(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.046,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_332_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-94(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.046,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_926_966_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 46 -->

<div style="text-align: center;">Figure 3-95(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_334_965_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-95(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.032,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_217_919_964_1433.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 47 -->

<div style="text-align: center;">Figure 3-95(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.032,C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_339_965_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-96(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.022,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_920_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 48 -->

<div style="text-align: center;">Figure 3-96(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.022,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_220_331_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-96(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.022,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_211_921_971_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 49 -->

<div style="text-align: center;">Figure 3-97(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.015,\bar{C}_{2}=6)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_335_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-97(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.015,C2=6)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_916_964_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 50 -->

<div style="text-align: center;">Figure 3-97(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.015,C2=6)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_335_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-98(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,C_{2}=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_217_924_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 51 -->

<div style="text-align: center;">Figure 3-98(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_331_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-98(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,\;C2=5.5)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_923_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 52 -->

<div style="text-align: center;">Figure 3-99(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.750,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_333_965_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-99(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.750,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_912_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 53 -->

<div style="text-align: center;">Figure 3-99(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.750,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_335_967_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-100(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.648,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_923_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 54 -->

<div style="text-align: center;">Figure 3-100(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.648,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_331_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-100(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.648,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_921_973_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 55 -->

<div style="text-align: center;">Figure 3-101(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.562,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_336_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-101(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.562,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_222_916_968_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 56 -->

<div style="text-align: center;">Figure 3-101(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.562,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_336_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-102  (a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.422,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 57 -->

<div style="text-align: center;">Figure 3-102(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.422,\;C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_216_327_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-102(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.422,\;C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_922_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 58 -->

<div style="text-align: center;">Figure 3-103(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.316,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_336_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-103(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_217_918_966_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 59 -->

<div style="text-align: center;">Figure 3-103(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.316,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_332_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-104(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.237,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 60 -->

<div style="text-align: center;">Figure 3-104(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.237,\;C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_330_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-104(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.237,\;C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_925_966_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 61 -->

<div style="text-align: center;">Figure 3-105(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.178,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_334_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-105(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.178,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_916_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 62 -->

<div style="text-align: center;">Figure 3-105(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.178,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_335_967_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-106(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.133,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_923_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 63 -->

<div style="text-align: center;">Figure 3-106(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.133,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_330_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-106(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.133,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_922_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 64 -->

<div style="text-align: center;">Figure 3-107(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.100,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_335_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-107(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_222_917_966_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 65 -->

<div style="text-align: center;">Figure 3-107(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.100,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_332_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-108(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.068,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_925_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 66 -->

<div style="text-align: center;">Figure 3-108(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.068,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_329_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-108(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.068,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_922_970_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 67 -->

<div style="text-align: center;">Figure 3-109(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.046,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_334_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-109(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.046,\;C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_917_961_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 68 -->

<div style="text-align: center;">Figure 3-109(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.046,\;C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-110(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_920_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 69 -->

<div style="text-align: center;">Figure 3-110(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_215_332_956_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-110(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_923_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 70 -->

<div style="text-align: center;">Figure 3-111(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.022,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_335_962_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-111(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.022,\;C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_917_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 71 -->

<div style="text-align: center;">Figure 3-111(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.022,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_335_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-112  (a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.015,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_921_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 72 -->

<div style="text-align: center;">Figure 3-112(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.015,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_331_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-112(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.015,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_212_921_970_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 14 | page 73 -->

<div style="text-align: center;">Figure 3-113(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,C_{2}=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_214_335_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-113(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_917_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 14 | page 74 -->

<div style="text-align: center;">Figure 3-113(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.010,C2=10)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_218_336_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-114  (a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.909,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 14/imgs/img_in_chart_box_213_920_961_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 1 -->

<div style="text-align: center;">Figure 3-114(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.909,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_222_328_957_842.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 3-114(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.909,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_211_921_958_1430.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 2 -->

<div style="text-align: center;">Figure 3-115(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.866,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-115(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.866,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_219_912_961_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 3 -->

<div style="text-align: center;">Figure 3-115(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.866,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_334_957_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-116(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.825,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_927_964_1430.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 4 -->

<div style="text-align: center;">Figure 3-116(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.825,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_330_960_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-116(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.825,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_923_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 5 -->

<div style="text-align: center;">Figure 3-117(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.750,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_964_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-117(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.750,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_221_914_967_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 6 -->

<div style="text-align: center;">Figure 3-117(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.750,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_334_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-118(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.715,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_922_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 7 -->

<div style="text-align: center;">Figure 3-118(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.715,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_223_328_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-118(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.715,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_919_970_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 8 -->

<div style="text-align: center;">Figure 3-119(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.681,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_335_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-119(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.681,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_914_966_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 9 -->

<div style="text-align: center;">Figure 3-119(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.681,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_323_968_833.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-120(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.648,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_923_966_1433.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 10 -->

<div style="text-align: center;">Figure 3-120(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.648,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_222_331_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-120(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.648,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_921_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 11 -->

<div style="text-align: center;">Figure 3-121(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.619,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_335_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-121(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.619,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_915_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 12 -->

<div style="text-align: center;">Figure 3-121(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.619,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-122(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.562,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_921_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 13 -->

<div style="text-align: center;">Figure 3-122(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.562,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_329_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-122(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.562,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_921_973_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 14 -->

<div style="text-align: center;">Figure 3-123(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.511,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_335_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-123(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.511,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_219_914_969_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 15 -->

<div style="text-align: center;">Figure 3-123(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.511,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-124(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.464,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_922_965_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 16 -->

<div style="text-align: center;">Figure 3-124(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.464,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_222_328_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-124(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.464,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_219_927_967_1430.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 17 -->

<div style="text-align: center;">Figure 3-125(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.383,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_336_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-125(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.383,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_921_965_1439.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 18 -->

<div style="text-align: center;">Figure 3-125(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.383,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-126(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.316,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_923_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 19 -->

<div style="text-align: center;">Figure 3-126(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_219_331_959_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-126(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_921_969_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 20 -->

<div style="text-align: center;">Figure 3-127(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.261,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_332_965_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-127(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.261,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_917_963_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 21 -->

<div style="text-align: center;">Figure 3-127(c)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.261,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_323_967_833.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-128  (a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.215,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_923_966_1433.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 22 -->

<div style="text-align: center;">Figure 3-128(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.215,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_219_331_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-128(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.215,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_926_965_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 23 -->

<div style="text-align: center;">Figure 3-129(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.178,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_334_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-129(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.178,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_916_963_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 24 -->

<div style="text-align: center;">Figure 3-129(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.178,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_337_966_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-130  (a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.147,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_920_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 25 -->

<div style="text-align: center;">Figure 3-130 (b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.147,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_219_331_959_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-130(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.147,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_925_966_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 26 -->

<div style="text-align: center;">Figure 3-131(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.121,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_335_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-131 (b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.121,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_916_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 27 -->

<div style="text-align: center;">Figure 3-131 (c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.121,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-132  (a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.100,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_921_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 28 -->

<div style="text-align: center;">Figure 3-132(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_331_960_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-132(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_921_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 29 -->

<div style="text-align: center;">Figure 3-133(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.075,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_332_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-133(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.075,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_917_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 30 -->

<div style="text-align: center;">Figure 3-133(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.075,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-134  (a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.056,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_923_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 31 -->

<div style="text-align: center;">Figure 3-134(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_322_958_834.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-134(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_925_970_1432.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 32 -->

<div style="text-align: center;">Figure 3-135(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.042,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_333_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-135(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.042,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_917_961_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 33 -->

<div style="text-align: center;">Figure 3-135(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.042,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_322_970_833.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-136(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_923_967_1433.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 34 -->

<div style="text-align: center;">Figure 3-136(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_331_957_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-136(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_924_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 35 -->

<div style="text-align: center;">Figure 3-137(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.026,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_336_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-137(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.026,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_917_962_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 36 -->

<div style="text-align: center;">Figure 3-137(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.026,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-138(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.018,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_920_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 37 -->

<div style="text-align: center;">Figure 3-138(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.018,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_331_957_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-138(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.018,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_211_921_971_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 38 -->

<div style="text-align: center;">Figure 3-139(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.013,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_334_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-139(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.013,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_918_961_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 39 -->

<div style="text-align: center;">Figure 3-139(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.013,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_333_971_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-140(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,C_{2}=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_919_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 40 -->

<div style="text-align: center;">Figure 3-140(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,\;C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_331_957_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-140(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=30)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_211_921_971_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 41 -->

<div style="text-align: center;">Figure 3-141(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.909,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-141(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.909,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_914_956_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 42 -->

<div style="text-align: center;">Figure 3-141(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.909,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_322_958_833.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-142  (a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.866,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_927_958_1434.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 43 -->

<div style="text-align: center;">Figure 3142(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.866,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_326_953_842.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 3-142(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.866,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_921_959_1430.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 44 -->

<div style="text-align: center;">Figure 3-143(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.825,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_333_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-143(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.825,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_913_955_1431.jpg" alt="Image" width="61%" /></div>


<!-- batch 15 | page 45 -->

<div style="text-align: center;">Figure 3-143(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.825,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_332_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-144(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.787,\;C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_921_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 46 -->

<div style="text-align: center;">Figure 3-144(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.787,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_328_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-144(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.787,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_926_966_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 47 -->

<div style="text-align: center;">Figure 3-145(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.750,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_332_966_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-145(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.750,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_913_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 48 -->

<div style="text-align: center;">Figure 3-145(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.750,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_332_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-146(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.715,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 49 -->

<div style="text-align: center;">Figure 3-146(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.715,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_326_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-146(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.715,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_925_966_1429.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 50 -->

<div style="text-align: center;">Figure 3-147(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.681,\;C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_334_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3 147(b) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.681,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_913_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 51 -->

<div style="text-align: center;">Figure 3-147(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.681,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_332_970_841.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-148(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.648,\;C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_227_923_984_1433.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 52 -->

<div style="text-align: center;">Figure 3-148(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.648,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_330_959_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-148(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.648,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_926_965_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 53 -->

<div style="text-align: center;">Figure 3-149(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.619,\;C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_333_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-149(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.619,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_915_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 54 -->

<div style="text-align: center;">Figure 3-149(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.619,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_325_967_833.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-150(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.590,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_925_965_1433.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 55 -->

<div style="text-align: center;">Figure 3-150(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.590,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_330_958_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-150(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.590,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_926_965_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 56 -->

<div style="text-align: center;">Figure 3-151(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.562,C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_337_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-151(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.562,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_915_963_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 57 -->

<div style="text-align: center;">Figure 3-151(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.562,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-152(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.511,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_923_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 58 -->

<div style="text-align: center;">Figure 3-152(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.511,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_329_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-152(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.511,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_921_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 59 -->

<div style="text-align: center;">Figure 3-153(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.464,\;C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_335_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-153(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.464,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_913_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 60 -->

<div style="text-align: center;">Figure 3-153(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.464,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-154(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.422,C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_921_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 61 -->

<div style="text-align: center;">Figure 3-154(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.422,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_328_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-154(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.422,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_921_969_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 62 -->

<div style="text-align: center;">Figure 3-155(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.365,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_333_964_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-155(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.365,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_914_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 63 -->

<div style="text-align: center;">Figure 3-155(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.365,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_211_330_971_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-156(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.316,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_183_923_995_1471.jpg" alt="Image" width="68%" /></div>


<!-- batch 15 | page 64 -->

<div style="text-align: center;">Figure 3-156(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.316,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_328_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-156(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_924_967_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 65 -->

<div style="text-align: center;">Figure 3-157(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.274,\;C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_332_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-157(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.274,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_914_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 66 -->

<div style="text-align: center;">Figure 3-157(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.274,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-158(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.261,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_920_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 67 -->

<div style="text-align: center;">Figure 3-158(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.261,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_327_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-158(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.261,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_922_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 68 -->

<div style="text-align: center;">Figure 3-159(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.237,\;C_{2}=100$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_338_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-159(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.237,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_914_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 69 -->

<div style="text-align: center;">Figure 3-159(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.237,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_332_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-160(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C_{1}=0.215,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_922_962_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 70 -->

<div style="text-align: center;">Figure 3-160(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.215,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_327_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-160(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.215,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_211_920_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 71 -->

<div style="text-align: center;">Figure 3-161(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.178,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_336_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-161(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.178,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_914_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 72 -->

<div style="text-align: center;">Figure 3-161(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.178,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-162(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.147,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_922_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 73 -->

<div style="text-align: center;">Figure 3-162(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.147,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_329_961_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-162(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.147,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_924_967_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 74 -->

<div style="text-align: center;">Figure 3-163(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.121,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_335_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-163(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.121,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_915_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 75 -->

<div style="text-align: center;">Figure 3-163(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.121,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_967_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-164(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.100,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_923_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 76 -->

<div style="text-align: center;">Figure 3-164(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_328_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-164(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_924_967_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 77 -->

<div style="text-align: center;">Figure 3-165(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.075,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_336_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-165(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.075,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_914_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 78 -->

<div style="text-align: center;">Figure 3-165(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.075,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_335_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-166(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.056,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_920_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 79 -->

<div style="text-align: center;">Figure 3-166(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_218_331_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-166(c)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_211_921_971_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 80 -->

<div style="text-align: center;">Figure 3-167(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.042,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_332_966_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-167(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.042,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_916_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 81 -->

<div style="text-align: center;">Figure 3-167(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.042,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_343_968_850.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-168(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_928_968_1440.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 82 -->

<div style="text-align: center;">Figure 3-168(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.032,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_328_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-168(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_926_966_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 83 -->

<div style="text-align: center;">Figure 3-169(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.026,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_335_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-169(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.026,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_217_918_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 84 -->

<div style="text-align: center;">Figure 3-169(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.026,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_338_966_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-170(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.018,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 85 -->

<div style="text-align: center;">Figure 3-170(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.018,\;C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_329_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-170(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.018,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_211_921_971_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 86 -->

<div style="text-align: center;">Figure 3-171(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.013,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_214_333_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-171(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.013,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_215_917_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 15 | page 87 -->

<div style="text-align: center;">Figure 3-171(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.013,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_334_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-172(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,C_{2}=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_213_920_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 15 | page 88 -->

<div style="text-align: center;">Figure 3-172(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_216_331_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-172(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=100)$ </div>


<div style="text-align: center;"><img src="../pages/batch 15/imgs/img_in_chart_box_212_924_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 1 -->

<div style="text-align: center;">Figure 3-173(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.909,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_334_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-173(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.909,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_914_956_1430.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 2 -->

<div style="text-align: center;">Figure 3-173(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.909,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-174(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.866,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_925_958_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 3 -->

<div style="text-align: center;">Figure 3-174(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.866,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_219_327_954_842.jpg" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 3-174(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.866,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_923_957_1430.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 4 -->

<div style="text-align: center;">Figure 3-175(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.825,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_335_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-175(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.825,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_914_955_1431.jpg" alt="Image" width="61%" /></div>


<!-- batch 16 | page 5 -->

<div style="text-align: center;">Figure 3-175(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.825,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_335_957_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-176(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.787,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_922_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 6 -->

<div style="text-align: center;">Figure 3-176(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.787,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_219_328_960_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-176(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.787,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 7 -->

<div style="text-align: center;">Figure 3-177(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.750,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_336_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-177(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.750,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_914_962_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 8 -->

<div style="text-align: center;">Figure 3-177(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.750,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-178(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.715,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_922_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 9 -->

<div style="text-align: center;">Figure 3-178(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.715,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_219_327_959_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-178(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.715,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 10 -->

<div style="text-align: center;">Figure 3-179(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$C_{1}=0.681,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_333_965_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-179(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.681,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_913_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 11 -->

<div style="text-align: center;">Figure 3-179(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.681,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_336_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-180(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.648,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_923_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 12 -->

<div style="text-align: center;">Figure 3-180(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.648,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_329_960_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-180(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.648,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 13 -->

<div style="text-align: center;">Figure 3-181(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.619,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_335_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-181(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.619,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_917_962_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 14 -->

<div style="text-align: center;">Figure 3-181(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.619,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_333_966_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-182(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.590,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_923_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 15 -->

<div style="text-align: center;">Figure 3-182(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.590,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_329_959_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-182(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.590,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_925_965_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 16 -->

<div style="text-align: center;">Figure 3-183(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.562,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_334_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-183(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.562,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_915_962_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 17 -->

<div style="text-align: center;">Figure 3-183(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.562,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_337_965_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-184(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.536,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_923_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 18 -->

<div style="text-align: center;">Figure 3-184(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.536,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_327_959_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-184(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.536,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 19 -->

<div style="text-align: center;">Figure 3-185(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.511,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_337_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-185(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.511,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_916_962_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 20 -->

<div style="text-align: center;">Figure 3-185(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.511,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_335_967_841.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-186(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.487,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 21 -->

<div style="text-align: center;">Figure 3-186(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.487,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_326_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-186(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.487,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_922_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 22 -->

<div style="text-align: center;">Figure 3-187(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.464,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_332_964_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-187(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.464,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_913_963_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 23 -->

<div style="text-align: center;">Figure 3-187(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.464,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_335_967_841.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-188(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.422,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_920_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 24 -->

<div style="text-align: center;">Figure 3-188(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.422,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_325_959_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-188(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.422,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_925_966_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 25 -->

<div style="text-align: center;">Figure 3-189(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.383,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_334_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-189(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.383,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_913_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 26 -->

<div style="text-align: center;">Figure 3-189(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.383,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-190(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.365,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_920_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 27 -->

<div style="text-align: center;">Figure 3-190(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.365,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_327_958_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-190(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.365,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 28 -->

<div style="text-align: center;">Figure 3-191(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.348,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_964_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-191(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.348,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_915_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 29 -->

<div style="text-align: center;">Figure 3-191(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.348,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-192(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.316,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_920_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 30 -->

<div style="text-align: center;">Figure 3-192(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.316,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_327_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-192(c) Maximum Response of Elasto-Plastic, One-Degree-of-Fredom System for Bilinear-Triangular Pulse $(C1=0.316,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_922_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 31 -->

<div style="text-align: center;">Figure 3-193(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.287,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_335_962_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-193(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.287,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_915_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 32 -->

<div style="text-align: center;">Figure 3-193(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.287,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-194(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.274,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_919_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 33 -->

<div style="text-align: center;">Figure 3-194(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.274,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_329_959_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-194(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.274,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_924_967_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 34 -->

<div style="text-align: center;">Figure 3-195(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.261,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_334_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-195(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.261,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_914_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 35 -->

<div style="text-align: center;">Figure 3-195(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.261,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-196(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.237,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_919_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 36 -->

<div style="text-align: center;">Figure 3-196(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.237,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_328_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-196(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.237,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_211_920_969_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 37 -->

<div style="text-align: center;">Figure 3-197(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangle Pulse $(C_{1}=0.215,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_334_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-197(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangle Pulse.$(C1=0.215,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_913_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 38 -->

<div style="text-align: center;">Figure 3-197(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangle Pulse $(C1=0.215,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-198(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.198,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_920_965_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 39 -->

<div style="text-align: center;">Figure 3-198(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.198,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_327_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-198(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.198,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 40 -->

<div style="text-align: center;">Figure 3-199(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.178,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_334_961_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-199(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.178,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_914_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 41 -->

<div style="text-align: center;">Figure 3-199(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.178,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_334_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-200(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.162,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 42 -->

<div style="text-align: center;">Figure 3-200(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.162,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_328_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-200(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.162,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_924_967_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 43 -->

<div style="text-align: center;">Figure 3-201(a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.147,\;C_{2}=300$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_332_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-201(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.147,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_914_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 44 -->

<div style="text-align: center;">Figure 3-201(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.147,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_335_967_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-202(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.133,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_921_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 45 -->

<div style="text-align: center;">Figure 3-202(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.133,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_328_959_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-202(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.133,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_925_966_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 46 -->

<div style="text-align: center;">Figure 3-203(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.121,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_335_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-203(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.121,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_915_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 47 -->

<div style="text-align: center;">Figure 3-203(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.121,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_335_967_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-204(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.110,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_920_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 48 -->

<div style="text-align: center;">Figure 3-204(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.110,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_325_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-204(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.110,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_211_920_970_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 49 -->

<div style="text-align: center;">Figure 3-205(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.100,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_334_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-205(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_915_964_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 50 -->

<div style="text-align: center;">Figure 3-205(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_333_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-206(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.091,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_920_966_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 51 -->

<div style="text-align: center;">Figure 3-206(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.091,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_327_960_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-206(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.091,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_924_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 52 -->

<div style="text-align: center;">Figure 3-207(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.083,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_333_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-207(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.083,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_914_965_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 53 -->

<div style="text-align: center;">Figure 3-207(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.083,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_335_968_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-208(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.075,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 54 -->

<div style="text-align: center;">Figure 3-208(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.075,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_330_958_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-208(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.075,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_922_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 55 -->

<div style="text-align: center;">Figure 3-209(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.068,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_332_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-209(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.068,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_915_966_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 56 -->

<div style="text-align: center;">Figure 3-209(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.068,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_333_971_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-210(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.056,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 57 -->

<div style="text-align: center;">Figure 3-210(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_329_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-210(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_210_920_972_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 58 -->

<div style="text-align: center;">Figure 3-211(a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.046,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_333_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-211(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.046,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_915_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 59 -->

<div style="text-align: center;">Figure 3-211(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.046,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_334_969_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-212(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse .$(C_{1}=0.042,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 60 -->

<div style="text-align: center;">Figure 3-212(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.042,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_329_963_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-212(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.042,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_211_921_971_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 61 -->

<div style="text-align: center;">Figure 3-213(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.032,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_333_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-213(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_216_917_966_1431.jpg" alt="Image" width="62%" /></div>


<!-- batch 16 | page 62 -->

<div style="text-align: center;">Figure 3-213(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.032,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_333_970_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-214(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.026,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_919_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 63 -->

<div style="text-align: center;">Figure 3-214(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.026,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_218_332_962_841.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-214(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.026,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_920_969_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 64 -->

<div style="text-align: center;">Figure 3-215(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.022,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_214_333_964_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-215(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.022,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_916_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 65 -->

<div style="text-align: center;">Figure 3-215(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.022,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_211_332_972_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-216(a) Maximum Response of Elasto-Plastic, One-Degree-of Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.018,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_921_967_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 66 -->

<div style="text-align: center;">Figure 3-216(b)Maximum Response of Elasto-Plastic, One-Degree-of Freedom System for Bilinear-Triangular Pulse $(C1=0.018,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_217_331_963_842.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-216(c)Maximum Response of Elasto-Plastic, One-Degree-of Freedom System for Bilinear-Triangular Pulse $(C1=0.018,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_212_923_968_1430.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 67 -->

<div style="text-align: center;">Figure 3-217(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.015,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_334_964_842.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-217(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.015,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_215_916_968_1431.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 68 -->

<div style="text-align: center;">Figure 3-217(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.015,\;C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_210_333_974_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-218(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.013,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_210_929_971_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 69 -->

<div style="text-align: center;">Figure 3-218(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.013,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_330_968_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-218(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.013,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_206_927_976_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 16 | page 70 -->

<div style="text-align: center;">Figure 3-219(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C_{1}=0.010,C_{2}=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_210_335_968_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-219(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_213_923_972_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 16 | page 71 -->

<div style="text-align: center;">Figure 3-219(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,C2=300)$ </div>


<div style="text-align: center;"><img src="../pages/batch 16/imgs/img_in_chart_box_208_334_974_849.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 1 -->

<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_260_405_1012_1309.jpg" alt="Image" width="63%" /></div>


(00)= 66.0=5)

eae rare re e rrrrr  e rre e 

Se eee 

e eeeee 

12-220-020



<!-- batch 17 | page 2 -->

<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_259_390_1022_1301.jpg" alt="Image" width="64%" /></div>


(00=90=)

eae rare re e rrrrr  e  re e 

<!-- batch 17 | page 3 -->

<div style="text-align: center;">ceee-e-ere-ecae-aeerceecaecare-rre </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_262_408_978_1304.jpg" alt="Image" width="60%" /></div>


(000=200.=0)

eae rare re e rrrrr  e re e 

See e e 

ee 

12-220-020



<!-- batch 17 | page 4 -->

(0=22.0=2） nd en-e ss woeeee-oe-eeeree-eeeeceee-ceerrereeeeeeecneiee 322-0200

<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_266_392_968_1300.jpg" alt="Image" width="58%" /></div>


(000=2.=)

eae rare re e rrrrr  e rre e 

ee eeee e 

eee 

12-120-020



<!-- batch 17 | page 5 -->

<div style="text-align: center;">$N_{\perp}/^{\infty}?$ AO ANAAAA A E E </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_260_389_1029_1301.jpg" alt="Image" width="64%" /></div>


(000=0.=)

eae rare re e rrrrr  e re e 

<!-- batch 17 | page 6 -->

<div style="text-align: center;">Figure 3-225(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.715,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_335_968_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-225(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.715,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_920_969_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 7 -->

<div style="text-align: center;">Figure 3-225(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.715,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_334_974_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-226(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.681,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_927_976_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 8 -->

<div style="text-align: center;">Figure 3-226(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.681,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_324_966_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-226(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.681,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_929_971_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 9 -->

<div style="text-align: center;">Figure 3-227(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.648,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_332_973_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-227(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.648,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_921_968_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 10 -->

<div style="text-align: center;">Figure 3-227(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.648,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_336_972_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-228(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.619,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_928_970_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 11 -->

<div style="text-align: center;">Figure 3-228(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.619,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_325_965_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-228(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.619,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_930_971_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 12 -->

<div style="text-align: center;">Figure 3-229(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.590,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_969_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-229(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.590,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_921_968_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 13 -->

<div style="text-align: center;">Figure 3-229(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.590,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_973_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-230(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.562,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_930_967_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 14 -->

<div style="text-align: center;">Figure 3-230(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.562,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_214_327_963_848.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-230(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.562,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_926_975_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 15 -->

<div style="text-align: center;">Figure 3-231(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.536,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_335_968_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-231(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.536,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_214_922_966_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 16 -->

<div style="text-align: center;">Figure 3-231(c)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.536,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_331_975_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-232(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.511,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_927_972_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 17 -->

<div style="text-align: center;">Figure 3-232(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.511,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_214_327_963_848.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-232(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.511,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_928_973_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 18 -->

<div style="text-align: center;">Figure 3-233(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.487,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_332_971_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-233(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.487,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_920_967_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 19 -->

<div style="text-align: center;">Figure 3-233(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.487,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_973_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-234(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.464,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_926_973_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 20 -->

<div style="text-align: center;">Figure 3-234(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.464,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_214_326_964_848.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-234(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.464,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_928_973_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 21 -->

<div style="text-align: center;">Figure 3-235(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.422,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_335_967_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-235(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.422,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_919_968_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 22 -->

<div style="text-align: center;">Figure 3-235(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.422,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_973_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-236(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.383,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_926_973_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 23 -->

<div style="text-align: center;">Figure 3-236(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.383,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_324_964_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-236(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.383,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_926_974_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 24 -->

<div style="text-align: center;">Figure 3-237(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.365,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_332_971_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-237(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.365,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_921_966_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 25 -->

<div style="text-align: center;">Figure 3-237(c)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.365,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_973_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-238(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.348,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_928_969_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 26 -->

<div style="text-align: center;">Figure 3-238(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.348,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_214_327_963_848.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-238(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.348,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_928_973_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 27 -->

<div style="text-align: center;">Figure 3-239(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.316,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_331_973_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-239(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.316,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_920_968_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 28 -->

<div style="text-align: center;">Figure 3-239(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.316,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_332_975_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-240(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.287,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_928_969_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 29 -->

<div style="text-align: center;">Figure 3-240(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.287,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_325_965_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-240(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.287,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_928_973_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 30 -->

<div style="text-align: center;">Figure 3-241(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.274,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_334_965_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-241(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.274,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_921_967_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 31 -->

<div style="text-align: center;">Figure 3-241(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.274,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_336_971_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-242(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.261,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_928_971_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 32 -->

<div style="text-align: center;">Figure 3-242(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.261,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_326_965_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-242(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.261,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_928_973_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 33 -->

<div style="text-align: center;">Figure 3-243(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.237,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_969_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-243(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.237,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_920_969_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 34 -->

<div style="text-align: center;">Figure 3-243(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.237,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_336_971_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-244(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.215,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_926_973_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 35 -->

<div style="text-align: center;">Figure 3-244(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.215,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_325_966_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-244(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.215,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_929_974_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 36 -->

<div style="text-align: center;">Figure 3-245(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.198,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_331_973_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-245(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.198,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_920_965_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 37 -->

<div style="text-align: center;">Figure 3-245(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.198,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_333_975_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-246(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.178,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_928_971_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 38 -->

<div style="text-align: center;">Figure 3-246(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.178,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_329_963_848.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">Figure 3-246(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.178,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_929_972_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 39 -->

<div style="text-align: center;">Figure 3-247(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.162,C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_332_971_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-247(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.162,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_920_966_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 40 -->

<div style="text-align: center;">Figure 3-247(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.162,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_333_974_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-248(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.147,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_926_974_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 41 -->

<div style="text-align: center;">Figure 3-248(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.147,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_324_967_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-248(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.147,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_930_972_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 42 -->

<div style="text-align: center;">Figure 3-249(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.133,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_336_964_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-249(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.133,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_920_969_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 43 -->

<div style="text-align: center;">Figure 3-249(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.133,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_335_972_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-250(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.121,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_925_974_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 44 -->

<div style="text-align: center;">Figure 3-250(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.121,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_324_966_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-250(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.121,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_206_927_975_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 45 -->

<div style="text-align: center;">Figure 3-251(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.110,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_969_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-251(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.110,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_921_966_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 46 -->

<div style="text-align: center;">Figure 3-251(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.110,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_206_331_975_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-252(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.100,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_925_974_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 47 -->

<div style="text-align: center;">Figure 3-252(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.100,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_213_326_965_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-252(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.100,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_928_973_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 48 -->

<div style="text-align: center;">Figure 3-253(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.091,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_969_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-253(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.091,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_921_965_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 49 -->

<div style="text-align: center;">Figure 3-253(c)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.091,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_333_976_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-254(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.083,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_925_976_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 50 -->

<div style="text-align: center;">Figure 3-254(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.083,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_325_965_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-254(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.083,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_928_975_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 51 -->

<div style="text-align: center;">Figure 3-255(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.075,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_332_971_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-255(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.075,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_921_965_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 52 -->

<div style="text-align: center;">Figure 3-255(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.075,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_335_974_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-256(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.068,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_928_971_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 53 -->

<div style="text-align: center;">Figure 3-256(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.068,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_328_964_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-256(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.068,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_206_926_976_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 54 -->

<div style="text-align: center;">Figure 3-257(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.056,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_332_971_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-257(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.056,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_922_965_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 55 -->

<div style="text-align: center;">Figure 3-257(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.056,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_332_975_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-258(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.046,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_928_968_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 56 -->

<div style="text-align: center;">Figure 3-258(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.046,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_328_964_849.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-258(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse.$(C1=0.046,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_206_926_976_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 57 -->

<div style="text-align: center;">Figure 3-259(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.042,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_208_332_971_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-259(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.042,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_923_971_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 58 -->

<div style="text-align: center;">Figure 3-259(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.042,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_975_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-260(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.032,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_928_972_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 59 -->

<div style="text-align: center;">Figure 3-260(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.032,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_330_964_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-260(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.032,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_206_927_976_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 60 -->

<div style="text-align: center;">Figure 3-261(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.026,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_335_968_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-261(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.026,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_924_967_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 61 -->

<div style="text-align: center;">Figure 3-261(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.026,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_975_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-262(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.022,\;C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_926_975_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 62 -->

<div style="text-align: center;">Figure 3-262(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.022,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_329_964_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-262(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.022,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_929_975_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 63 -->

<div style="text-align: center;">Figure 3-263(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.018,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_334_969_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-263(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.018,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_211_923_969_1445.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 64 -->

<div style="text-align: center;">Figure 3-263(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.018,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_205_330_978_849.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-264(a)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.015,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_925_976_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 65 -->

<div style="text-align: center;">Figure 3-264(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.015,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_330_964_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-264(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.015,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_206_927_976_1446.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 66 -->

<div style="text-align: center;">Figure 3-265(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.013,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_210_335_968_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-265(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.013,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_925_967_1446.jpg" alt="Image" width="63%" /></div>


<!-- batch 17 | page 67 -->

<div style="text-align: center;">Figure 3-265(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.013,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_207_333_975_848.jpg" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3-266(a) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $C_{1}=0.010,\ C_{2}=1000$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_209_928_972_1445.jpg" alt="Image" width="64%" /></div>


<!-- batch 17 | page 68 -->

<div style="text-align: center;">Figure 3-266(b)Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse,$(C1=0.010,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_212_330_964_848.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 3-266(c) Maximum Response of Elasto-Plastic, One-Degree-of-Freedom System for Bilinear-Triangular Pulse $(C1=0.010,\;C2=1000)$ </div>


<div style="text-align: center;"><img src="../pages/batch 17/imgs/img_in_chart_box_205_929_976_1447.jpg" alt="Image" width="64%" /></div>


<!-- batch 18 | page 1 -->

ee eeoe e 

ee eee 

12-220-020



<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_chart_box_193_423_844_1166.jpg" alt="Image" width="54%" /></div>


Z pe T sese 

<!-- batch 18 | page 2 -->

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_chart_box_197_196_1005_1481.jpg" alt="Image" width="67%" /></div>


ee ee 

e ee 

12-220-020



<!-- batch 18 | page 3 -->

<div style="text-align: center;">Figure 3-269 Pressure-Time and Resistance Time Curves for Elements Which Respond To Impulse </div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_chart_box_181_373_1006_861.jpg" alt="Image" width="69%" /></div>


<div style="text-align: center;">Table 3-14Details of Computation By Acceleration Impulse Extrapolation Method </div>



<div style="text-align: center;"><html><body><table border="1"><tr><td>n</td><td>t</td><td>${\pmb P}_{n}$</td><td>${\pmb R}_{n}$</td><td>$\pmb{P}_{n}-\pmb{R}_{n}$</td><td>$\boldsymbol{a}_{n}=(\boldsymbol{P}_{n}-\boldsymbol{R}_{n})/m$</td><td>$a_{n}(\Delta t)^{2}$</td><td>$2\pmb{X}_{n}$</td><td>$\pmb{X}_{n-1}$</td><td>$\pmb{X}_{n+1}$</td></tr><tr><td>0 1 2</td><td>0 2(Δt1} $\Delta t_{1}$</td><td>$P_{}$ $P_{2}$ $P_{0}$</td><td>$R_{1}$ $R_{2}$ $R_{0}$</td><td>$P_{1-}_{}$ $P_{}-} _}$ $P_{0}–R_{0}$</td><td>ao $a_{$ $a{$</td><td>$\pmb{a}_{0}(\pmb{\Delta t}_{1})^{2}$ $\pmb{a}_{1}(\pmb{\Delta t}_{1})^{2}$ $\pmb{a}_{2}(\pmb{\Delta t}_{1})^{2}$</td><td>0 2_{}$ $2X{}$</td><td>0 0 $X_{}$</td><td>$X_{}$ $X_{}$ $X_{1}$</td></tr><tr><td>j-1</td><td>(j-1)△t1$</td><td>Pj-1</td><td>$R_j-1</td><td>$P_j-1-_j-1$</td><td>aj-1</td><td>$aj_-1(△_1)}$</td><td>2X j-</td><td>$Xj-2$</td><td>_j</td></tr><tr><td>j</td><td>$j△__}$</td><td>Pj</td><td>Rj$</td><td>$P_{ }- }$</td><td>aj</td><td>$a(△_1){}$</td><td>2X_j$</td><td>$X_j}-1$</td><td>$ j1$</td></tr><tr><td>j+1</td><td>j(Δt₁)+△t2</td><td>$P_j}$</td><td>$R_j}$</td><td>$P_+1-+1$</td><td>$aj+1$</td><td>$a+1(_t{1^}</td><td>$2x 1$</td><td>Xj-1$</td><td>$X_}$</td></tr></table></body></html></div>


<!-- batch 18 | page 4 -->

<div style="text-align: center;">Table 3-15Figure Numbers Corresponding To Various Combinations of $c_{1}$ .and $c_{2}$  </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>C2 C1</td><td>1.00</td><td>1.70</td><td>3.00</td><td>5.50</td><td>10.0</td><td>30.0</td><td>100</td><td>300</td><td>1000</td></tr><tr><td>3-64 3-64 3-64 3-64 3-64 3-64 3-64 3-64 3-64 3-64 3-64</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.000 0.909 0.866 0.825</td><td rowspan="15">1.000 0.909 0.866 0.825 0.787 0.750 0.715 0.681 0.648 0.619 0.590 0.562 0.536 0.511 0.487 0.464 0.422 0.383 0.365 0.348 0.316 0.287 0.274 0.261 0.237 0.215 0.198 0.178 0.162 0.147 0.133 0.121 0.110 0.100 0.091 0.083 0.075 0.068 0.056 0.046 0.042 0.032 0.026 0.022 0.018 0.015 0.013</td><td rowspan="8">3-64</td><td rowspan="8">3-64</td><td rowspan="8">3-64</td><td rowspan="6">3-64</td><td>3-64</td><td>3-64</td><td>3-64</td><td>3-64 3-114 3-115 3-116</td></tr><tr><td>3-222</td><td></td><td></td><td></td></tr><tr><td>0.787 0.750 0.715 0.681 0.648 0.619 0.590</td><td>3-64</td><td>3-144</td><td>3-176</td></tr><tr><td>3-65</td><td>3-75</td><td>3-85</td><td>3-99</td></tr><tr><td>3-117 3-118</td><td>3-145 3-146</td><td>3-177 3-178</td><td>3-225</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>3-100</td><td>3-119 3-120 3-121</td><td>3-147</td></tr><tr><td>3-149</td><td></td><td></td><td></td></tr><tr><td>3-101</td><td>3-122</td><td>3-150</td><td>3-182</td><td>3-229</td><td></td><td></td></tr><tr><td>3-183 3-184</td><td>3-230 3-231</td><td>3-123</td><td>3-152</td><td>3-185</td><td>3-232</td><td>0.487 0.464 0.422 0.383</td><td>3-64</td></tr><tr><td>3-66</td><td>3-76</td><td>3-87</td><td>3-102</td><td>3-124 3-125</td><td>3-153 3-154</td><td>3-187</td><td>3-234</td></tr><tr><td>3-188</td><td>3-235</td><td>3-189</td><td>3-236</td><td>3-155</td><td>3-237</td><td></td><td></td></tr><tr><td>0.348 0.316 0.287 0.274</td><td>3-64</td><td>3-67</td><td>3-77</td><td>3-88</td><td>3-103</td><td>3-191</td><td>3-238</td></tr><tr><td>3-126</td><td>3-156</td><td>3-192 3-193</td><td>3-239 3-240</td><td>3-157</td><td>3-194</td><td>3-241</td><td>3-104</td></tr><tr><td>3-195</td><td>3-242</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.237</td><td>3-64</td><td>3-78</td><td>3-89</td><td>3-159</td><td>3-196</td><td>3-243</td><td>3-68</td></tr><tr><td>3-90</td><td>3-105</td><td>3-198</td><td>3-245</td><td>0.178</td><td>3-129</td><td>3-161</td><td>3-199</td><td>3-246</td></tr><tr><td>3-64</td><td>3-69</td><td>3-200</td><td>3-247</td><td>0.147</td><td>3-79</td><td>3-91</td><td>3-106</td><td>3-130</td></tr><tr><td>3-248</td><td>3-202</td><td>3-249</td><td>3-131</td><td>3-163</td><td>3-203</td><td>3-250</td><td></td><td></td></tr><tr><td>0.110 0.100 0.091 0.083</td><td>0.110</td><td>3-64</td><td>3-70</td><td>3-92</td><td>3-107</td><td>3-204</td><td>3-251</td><td>3-80</td></tr><tr><td>3-205</td><td>3-252</td><td>3-206</td><td>3-253</td><td></td><td>3-133</td><td>3-165</td><td>3-207</td><td>3-254</td></tr><tr><td>0.075</td><td>3-208</td><td>3-255</td><td>3-81</td><td>3-93</td><td>3-108</td><td>3-209</td><td>3-256</td><td></td></tr><tr><td>3-64</td><td>3-71</td><td>3-134</td><td>3-166</td><td>0.056</td><td>3-210</td><td>3-257</td><td></td><td></td></tr><tr><td>3-94</td><td>3-109</td><td>3-211</td><td>3-258</td><td>0.042</td><td>3-64</td><td>3-72</td><td>3-82</td><td>3-135</td></tr><tr><td>3-95</td><td>3-110</td><td>0.032</td><td>3-136</td><td>3-168</td><td>3-213</td><td>3-260</td><td></td><td></td></tr><tr><td>3-137</td><td>3-169</td><td>3-214</td><td>3-261</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.022</td><td>3-64</td><td>3-73</td><td>3-83</td><td>3-96</td><td>3-111</td><td>3-215</td><td>3-262</td><td>0.018</td></tr><tr><td>0.015</td><td>3-217</td><td>3-264</td><td>3-139</td><td>3-171</td><td>0.013</td><td>3-218</td><td>3-265</td><td></td></tr><tr><td>0.010</td><td>3-64</td><td>3-74</td><td>3-84</td><td>3-98</td><td>3-113</td><td>3-140</td><td>3-172</td><td>3-219</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></body></html></div>


<!-- batch 18 | page 5 -->

<div style="text-align: center;">Table 3-16Response Chart Interpolation </div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Number</td><td>$c_{1}$</td><td>$C_{2}$</td><td colspan="3">Desired Parameter</td></tr><tr><td rowspan="2">1</td><td>$C_{11}$</td><td>$C_{21}$</td><td rowspan="2">$\mathsf{Y}_{1}$</td><td rowspan="7">$\Upsilon_{a}$</td><td rowspan="7">Y</td></tr><tr><td>$C_{1}$</td><td>$C_{21}$</td></tr><tr><td rowspan="2">2</td><td>$C_{12}$</td><td>$C_{22}=C_{21}$</td><td rowspan="2">$\mathsf{Y}_{2}$</td><td rowspan="4"></td></tr><tr><td>$C_{1}$</td><td>$C_{2}$</td></tr><tr><td rowspan="2">3</td><td>$C_{13}$</td><td>$C_{23}$</td><td rowspan="2">$\mathsf{Y}_{3}$</td><td rowspan="2">$\Upsilon_{b}$</td></tr><tr><td>$C_{1}$</td><td>$C_{23}$</td></tr><tr><td>4</td><td>$C_{14}$</td><td>$C_{24}=C_{23}$</td><td>$\mathsf{Y}_{4}$</td><td></td></tr></tbody></table></body></html></div>


<!-- batch 18 | page 6 -->

UFC 3-340-025 December 2008Change 2, 1 September 2014APPENDIX 3: PRINCIPLES OF DYNAMIC ANALYSIS 

<!-- batch 18 | page 7 -->

## APPENDIX 3A ILLUSTRATIVE EXAMPLES PROBLEM 3A-1ULTIMATE UNIT RESISTANCE 

## Problem:Determine the ultimate unit resistance of a two-way structural element using (1) general solution and (2) charts

## Procedure: Part (a) - General Solution 

Step 1.Establish design parameters.

Step 2.Assume yield line locations in terms of x and/or y considering support conditions, presence of openings, etc.



Step 3.Determine negative and positive moment capacities of sections crossed by assumed yield lines.



Step 4.Establish distribution of moments across negative and assumed yield lines, considering corner effects and those of openings.

Step 5.Determine the ultimate unit resistance for each sector in terms of x and/or y considering free body diagram of the sectors (Figure 3-3 (+))Summation of the moments about the axis of rotation (support) of the sector yields Equation 3-3.



Step 6.Equate the ultimate unit resistance of the sectors and solve for the yield line location x and/or y.



Step 7.With known yield line location, solve for ultimate unit resistance of the element, using equations obtained in Step 6.

Note:For complex problems (three or more different sectors) the solution for the ultimate unit resistance is most easily accomplished through a trial-anderror procedure by determining $r_{u}$ for each sector for a given (assumed)yield line location and adjusting the yield lines until the several values of ru agree to within a few percent.



## Procedure: Part (b) - Chart Solution 

Step 1.Same as in Step 1 of Part (a).

Step 2.Same as in Step 2 of Part (a).

Step 3.Determine the negative and positive ultimate moment capacities in vertical and horizontal directions.



Step 4.For given support conditions (and value of $x_{2}/x_{1}$ in the case of an element with three edges supported and fourth free), use the appropriate chart (Figures 3-4 (+) through 3-20 (+)) to obtain yield line location ratios x/L or y/H for value of quantity obtained in Step 4. Then calculate x or y.

Step 5.Using the appropriate equation from Table 3-2 (+) determine the ultimate unit resistance of the element.



<!-- batch 18 | page 8 -->

## EXAMPLE 3A-1 (A)ULTIMATE RESISTANCE 

Required:Ultimate unit resistance of two-way structural steel element shown below using (1) general solution and (2) charts.

<div style="text-align: center;">Figure 3A-1</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_384_451_803_768.jpg" alt="Image" width="35%" /></div>


Solution:Part (a) - General Solution 

Step 1.Given:

(a)$L=240in\quad H=168in$ 

(b)Fixed on three sides and free at the fourth 

Step 2.Assume yield line location (Figure 3A-2 (+))

Step 3.The negative and positive moment capacities in both the horizontal and vertical directions are determined from the properties of the material. For this Example, it will be assumed that the moment capacities are equal to 

$M=20.000in\cdot lbs/in$ 



$$M_{HN}=M_{HP}=M_{VN}=M_{VP}=20,000\ in\ lbs/in $$

<!-- batch 18 | page 9 -->

<div style="text-align: center;">Figure 3A-2</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_94_313_911_1399.jpg" alt="Image" width="68%" /></div>


<!-- batch 18 | page 10 -->

Step 4.For distribution of moments across negative and assumed positive lines,see Figure 3A-2(a) (+).



Step 5.The ultimate unit resistance of each sector is obtained by taking the summation of the moments about its axis of rotation (supports) so that 

$\Sigma M_{N}+\Sigma M_{P}=R c=r_{u}A c$ 



a.Sector I (Figure 3A-2 (+))

$$\begin{aligned}\Sigma M_{VN}+\Sigma M_{VP}&=120(20,000)+2(2/3)(20,000)(60)+\\&\quad120(20,000)+2(2/3)(20,000)(60)\\&=8.0\times10^6in-lbs.\end{aligned}$$

$$r_{u}A\boldsymbol{c}=r_{u}\left[\frac{240(y)}{2}\right]\left[\frac{y}{3}\right]=40r_{u}y^{2}$$

therefore,

$$r_{u}=400(20,000)/40y^{2}=0.2\times10^{6}/y^{2}$$

b.Sector Il (Figure 3A-2 (+))

$$\begin{aligned}{\Sigma M_{H N}+\Sigma M_{H P}=}&{{}(168{-}y/2)(20{,}000)+(2/3)(20{,}000)(y/2)+}\\ {}&{{}(20{,}000)(168{-}y/2)+(2/3)(20{,}000)(y/2)}\\ {=}&{{}336(20{,}000)-(y/3)(20{,}000)}\end{aligned}$$

$$\begin{aligned}r_{u}A c=&r_{u}\left[\frac{120\left(168+168-y\right)}{2}\right]\left[\frac{120\left(168+2\left(168-y\right)\right)}{3}\right]/\left(168+168-y\right)\\=&4.800r_{u}\left(252-y\right)\end{aligned}$$

therefore,

$$r_{u}=\frac{336(20,000)-\frac{y}{3}(20,000)}{4800(252-y)}$$

Step 6.Equate the ultimate unit resistance of the sectors.

$$\frac{10(20,000)}{y^{2}}=\frac{336(20,000)-\frac{y}{3}(20,000)}{4800(252-y)}$$

<!-- batch 18 | page 11 -->

Simplifying:

$$y^{3}-1008y^{2}-144000y+36288000=0$$

and the desired root is:$y=137.6in$ 

Step 7.The ultimate unit resistance is obtained by substituting the value of y into either equation obtained in Step 5, both of which yield:

$$r_{u}=(20,000)/(137.6)^{2}=10.6\;\mathrm{p s i}$$

## Solution:Part (b) - Chart Solution 

Note:

Element conforms to the requirements of Section 3-8 since it is fixed on three sides and free on the remaining side and has uniform thickness in the horizontal and vertical directions.



Step 1.Same as Step 1 in Part (a).

Step 2.For illustrative purposes, a different yield pattern (Figure 3A-3 (+)) will be assumed.



<div style="text-align: center;">Figure 3A-3</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_384_831_795_1160.jpg" alt="Image" width="34%" /></div>


Step 3.For ultimate moment capacities, see Step 3 of Part (a).

Step 4.For three sides fixed and the fourth free, calculate the parameter.

$$X_{2}/X_{1}=[(M_{H N3}+M_{H P})/(M_{H N1}+M_{H P})]^{1/2}=[(20,000)(2)/(20,000)(2)]^{1/2}=1.0$$

From Figure 3-11 (+),$(X_{2}/X_{1}=1.0)$ calculate the parameters:

$$L/H[M_{V P}/(M_{H N1}+M_{H P})]=(240/168)[20,000/(2)(20,000)]^{1/2}=1.01$$

and 

<!-- batch 18 | page 12 -->

$$\frac{M_{V P}}{M_{V N2}}=\frac{20,000}{20,000}=1.0$$

Read yield line location:

$X_{1}/L$ . exceeds the maximum possible value of 0.5 therefore, assumed yield line pattern is wrong. Assume alternate yield line pattern as shown in Figure $3A-2\left(+\right)$ L:

From Figure 3-16 (+) calculate the following parameters:

$$\frac{L}{H}=\frac{\left(M_{vN3}+M_{vP}\right)^{1/2}}{\left(M_{HN2}+M_{HP}\right)^{1/2}+\left(M_{HN1}+M_{HP}\right)^{1/2}}\quad 与 \quad\frac{240}{168}\left[\frac{\left(20,000+20,000\right)^{1/2}}{\left(20,000+20,000\right)^{1/2}+\left(20,000+20,000\right)^{1/2}}\right]=0.71$$

and 

$$\begin{aligned}\frac{X}{L}=\frac{\left[\left(M_{H N1}+M_{H P}\right)/\left(M_{H N2}+M_{H P}\right)\right]^{1/2}}{1+\left[\left(M_{H N1}+M_{H P}\right)/\left(M_{H N2}+M_{H P}\right)\right]^{1/2}}\\=\frac{\left[40,000/40,000\right]^{1/2}}{1+\left[40,000/40,000\right]^{1/2}}=1/2\end{aligned}$$

From Figure 3-16 (+) read of yield line location:

$$\begin{aligned}&y/H=0.82;~y=0.8(168)=137.6\quad in\\&X/L=0.50;~X=0.5(240)=120.0\quad in\\ \end{aligned}$$

Step 5.From Table 3-2 (+):

NOTE:

Both equations given in the table for each edge condition and yield line location will provide identical values of $r_{u}$ 



$$r_{u}=\frac{5(M_{vN}+M_{VP})}{y^{2}}=\frac{5(20,000+20,000)}{137.6^{2}}=(0.00055)20,000=10.5\mathrm{~ps}i $$

<!-- batch 18 | page 13 -->

## EXAMPLE 3A-1 (B)ULTIMATE UNIT RESISTANCE 

Required:Ultimate unit resistance of the element considered in Example 3A1(A) except there is an opening as shown in Figure 3A-4 (+).

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_429_396_756_703.jpg" alt="Image" width="27%" /></div>


## Solution:

Step 1.Given: (a)$L=240\quad H=168$ Two additional free edges are formed due to the presence of the opening.



Step 2.Assumed yield line location is shown in Figure 3A-5 (+) (three different sectors are formed).



Step 3.Same as Step 3 of Example $3A{\scriptstyle-1(A)}$ , Part (a).

<!-- batch 18 | page 14 -->

<div style="text-align: center;">Figure 3A-5</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_197_320_973_862.jpg" alt="Image" width="65%" /></div>


Step 4.For distribution of moments across negative and assumed positive yield lines see Figure 3A-5 (+). (Since opening is located at lower right corner,there is no reduced moment capacity in this area.)

Step 5.The ultimate unit resistance is obtained from:

$$\Sigma M_{N}+\Sigma M_{o}=R c=r_{u}A c $$

a.Sector 1 (Figure 3A-5 (+))

$$\begin{aligned}\Sigma M_{HN}+\Sigma M_{HP}=&(20,000)(168-y/2)+(2/3)(20,000)(y/2)+\\&(20,000)(168-y/2)+(2/3)(20,000)(y/2)\\=&336(20,000)-(y/3)(20,000)\\=&(336-y/3)(20,000)\end{aligned}$$

$$\begin{aligned}{r_{u}A c}&{{}=r_{u}[x(168+168-y)/2][x(168+2(168-y))/3(168+168-y)]}\\ {}&{{}=r_{u}x^{2}(252-y)/3}\end{aligned}$$

therefore,

$$r_{u}=\frac{(1008-y)(20,000)}{x^{2}(252-y)}$$

<!-- batch 18 | page 15 -->

b.Sector Il (Figure 3A-5(+))

$$\begin{align*}\Sigma M_{HN}+\Sigma M_{HP}&=(20,000)(80)+(20,000)(80)\\&=160(20,000)\end{align*}$$

The sector is divided into Parts a, b, and c so that the centroid may be obtained (see table below).



Note:


<div style="text-align: center;"><html><body><table border="1"><tr><td>Portion of Sector</td><td>Area (A)</td><td>Distance from Centroid to axis of rotation (c)</td><td>$A^{\prime}C^{\prime}$</td></tr><tr><td>a</td><td>(y-88)(180-x) 2</td><td>$\frac{(180-x)}{2}+60=\frac{360-x}{3}$</td><td>$\frac{(y-88)(180-x)(360-x)}{6}$</td></tr><tr><td>b</td><td>(y-88)(60)</td><td>60 2</td><td>(y-88)(60){ 2</td></tr><tr><td>C</td><td>(168-y)(240-x)</td><td>(240-x) 2</td><td>(168-y)(240-x)^{2 2</td></tr></table></body></html></div>


$$\begin{aligned}{A c}&{{}=\sum{A^{*}c^{*}}=\frac{{\left({y-88}\right)}{\left({180-x}\right)}{\left({360-x}\right)}}{6}+\frac{{\left({y-88}\right)}{\left({60}\right)}^{2}}{2}+\frac{{\left({168-y}\right)}{\left({240-x}\right)}^{2}}{2}}\\ {}&{{}=\frac{1}{2}{\left[{\frac{{\left({y-88}\right)}}{3}{\left[{{{\left({180-x}\right)}{\left({360-x}\right)}+10800}\right]}+{{\left({168-y}\right)}{\left({240-x}\right)}^{2}}}\right]}}}\\ {}&{{}{{r}_{u}}=\frac{{\left({\sum{{M}_{{t i N}}}+\sum{{{M}_{{t i P}}}}}\right)}}{{A c}}}\\ {}&{{}=\frac{6,400,000}{\frac{{\left({y-88}\right)}}{3}{\left[{{{\left({180-x}\right)}{\left({360-x}\right)}+10,800}}\right]}+{{\left({168-y}\right)}{{\left({240-x}\right)}^{2}}}}}\\ \end{aligned}$$

C.Sector II  (Figure 3A-5 (+))

$$\begin{aligned}\Sigma M_{vn}+\Sigma M_{vp}&=(20,000)(180-x/2)+(2/3)(20,000)(x/2)+\\&\quad(20,000)(180-x/2)+(2/3)(20,000)(x/2)\\&=360(20,000)-(20,000)(x/3)\end{aligned}$$

<!-- batch 18 | page 16 -->

UFC 3-340-025 December 2008Change 2, 1 September 2014


<div style="text-align: center;"><html><body><table border="1"><tr><td>Portion of Sector</td><td>Area (A)</td><td>Distance from Centroid to axis of rotation (c')</td><td>$A^{\prime}C^{\prime}$</td></tr><tr><td>a</td><td>(108- x)(y-88) 2</td><td>$\frac{(y-88)}{3}+88=\frac{y+176}{3}$</td><td>(180- x)(y -88)(y+ 176) 6</td></tr><tr><td>b</td><td>(180− x)(88)</td><td>88 \f</td><td>(180-x)(88)^2 2</td></tr><tr><td>C</td><td>$\frac{x y}{2}$</td><td>y-3</td><td>$\frac{x y^{2}}{6}$</td></tr></table></body></html></div>


$$\begin{aligned}&A c=\Sigma A^{\prime}c^{\prime}=(y-88)(180-x)(y+176)/6+(180-x)(88)^{2}/2+x y^{2}/6\\&\quad=1/6(180-x)[(y-88)(y+176)+23,232]+x y^{2}\\&r_{u}=\frac{\sum M_{H N}+\sum M_{H P}}{A c}\\&\quad=\frac{(2160-2x)(20,000)}{(180-x)[(y-88)(y+176)+23,232]+x y^{2}}\\ \end{aligned}$$

<div style="text-align: center;">Step 6.Due to the complexity of obtaining a direct solution for ultimate unit resistance, a trial-and-error solution will be used (see table below):</div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>X</td><td>y</td><td>◼ $r_{l}$</td><td>■ $r_{I I}$</td><td>■ $r_{I I I}$</td></tr><tr><td>125</td><td>130</td><td>9.21</td><td>7.67</td><td>9.33</td></tr><tr><td>125</td><td>135</td><td>9.55</td><td>7.92</td><td>8.77</td></tr><tr><td>125</td><td>140</td><td>9.92</td><td>8.19</td><td>8.25</td></tr><tr><td>125</td><td>145</td><td>10.32</td><td>8.48</td><td>7.78</td></tr><tr><td>125</td><td>150</td><td>10.77</td><td>8.79</td><td>7.35</td></tr><tr><td>130</td><td>130</td><td>8.52</td><td>8.29</td><td>9.50</td></tr><tr><td>130</td><td>135</td><td>8.83</td><td>8.55</td><td>8.92</td></tr><tr><td>131</td><td>135</td><td>8.70</td><td>8.68</td><td>8.85</td></tr></tbody></table></body></html></div>


<!-- batch 18 | page 17 -->

Therefore:

$x=131in$ 

$y=135\mathrm{i n}$ 

$r_{u}=8.68\mathrm{p s i}$ 

UFC 3-340-025 December 2008Change 2, 1 September 2014

<!-- batch 18 | page 18 -->

## PROBLEM 3A-2 RESISTANCE-DEFLECTION FUNCTION 

## Problem:Determine the actual and equivalent resistance deflection function in the elasto-plastic region for a two-way structural element

## Procedure:

Step 1.Establish design parameters.

a.Geometry of element 

b.Support conditions 

Step 2.Determine ultimate positive and negative moment capacities.

Step 3.Determine static properties:

a.Modules of elasticity for the element 

b.Moment of inertia of the element 

Step 4.Establish points of interest and their ultimate moment capacities (Figure 3-23 (+))Step 5.Compute properties at first yield.

a.Location of first yield 

b.Resistance at first yield re 

C.Moments at remaining points consistent with re 

d.Maximum deflection at first yield 

Step 6.Compute properties at second yield.

a.Remaining moment capacity at other points 

b.Location of second yield 

C.Change in unit resistance Δr between first and second yield.

d.Unit resistance at second yield $r_{e p}$ 

e.Moment at remaining point consistent with $r_{e p}$ 

f.Change in maximum deflection 

g.Total maximum deflection 

Note: An element with unsymmetrical support conditions may exhibit three or four support yields. Therefore, repeat Step 6 as many times as necessary to obtain properties at the various yield points.

<!-- batch 18 | page 19 -->

Step 7.Compute properties at final yield (ultimate unit resistance):

a.Ultimate unit resistance 

b.Change in resistance between ultimate unit resistance and resistance at prior yield 



C.Change in maximum deflection (for elements supported on two,three, or four sides, use stiffness obtained from Figure 3-26 (+), 3-30 (+)and 3-36 (+), respectively)



d.Total maximum deflection 

Step 8.Draw the actual resistance-deflection curve.(Figure 3-39 (+))

Step 9.Calculate equivalent maximum elastic deflection of the element.

<!-- batch 18 | page 20 -->

## EXAMPLE 3A-2RESISTANCE-DEFLECTIONFUNCTION 

Required:The actual and equivalent resistance-deflection function (curve) in the elasto-plastic region for the two-way structural steel element.

## Solution:

Step 1.Given:

a.$L=240in\quad H=168in$ 

b.Fixed on three sides and free at the fourth 

Step 2.Same as Step 3 of Example 3A-1(A), Part a.

Step 3.Static properties:

a.Modulus of elasticity,$E_{s}$ for steel 

$$E_{s}=29\times10^{6}\mathrm{p s i}$$

b.Considering a 1-inch strip $(b=1inch)$ 

Assume $I=144\ln^{4}$ 

Step 4.For points of interest, see Figure 3A-6 (+)

Step 5.Properties at first yield.

<div style="text-align: center;">Figure 3A-6</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_418_984_789_1205.jpg" alt="Image" width="31%" /></div>


From Figure 3-27 (+) for $H/L=0.7$ 

$$\begin{aligned}&\beta_{1}=0.077\quad\beta_{2}=0.160\quad\beta_{3}=0.115\\&\gamma_{1}=0.012\quad\nu=0.3\\ \end{aligned}$$

a.

$$\begin{aligned}&M_{HP}=M_{HN}=M_{VP}=M_{NN}=20,000in-lbs/in\\&M_{P}=\beta rH^{2}\\&r=M/\beta H^{2}\\ \end{aligned}$$

<!-- batch 18 | page 21 -->

$$\begin{aligned}r_{1}=20,&000/[(0.077)(168)^{2}]=9.20\;\mathsf{psi}\\r_{2}=20,&000/[(0.160)(168)^{2}]=4.43\;\mathsf{psi}\\r_{3}=20,&000/[(0.115)(168)^{2}]=6.16\;\mathsf{psi}\\&\mathsf{First}\;\mathsf{yield}\;\mathsf{at}\;\mathsf{Point}\;2\;(\mathsf{small}\;\mathsf{s}\mathsf{mallest}\;r)\end{aligned}$$

$$\begin{aligned}&b.\quad&r_{e}=4.43\;psi\\&c.\quad&M_{P}\;(Point1)=(0.077)(4.43)(168)^2\;=\;9.627\;in-lbs/in\\&\quad&M_{N}\;(Point3)=(0.115)(4.43)(168)^2\;=\;14,379\;in-lbs/in\\&d.\quad&D\;=EII/(b(1-\nu^2))\\&\quad&=29\times10^6\times144/(1(1-(0.3)^2))=\;45.9\times10^8\;in-lbs\\&\quad&\mathsf{X_{e}}=\gamma_{1}r_{e}H^4/D=(0.0120)(4.43)(168)^4/(45.9*10^8)=0.0092\;in\end{aligned}$$

Step 6.Properties at second yield.

After first yield element assumes a simple-simple-fixed-free stiffness,therefore from Figure 3-29 (+) for $H/L=0.7;$ 



should be 0$\begin{aligned}&\begin{aligned}\\ &\beta_{1}&=0.120\quad\beta_{2}=0.220\\&0.03&\quad\gamma_{1}=0.945-\quad\nu=0.320\\&a.\quad M_{P}\quad(Point1)=M_{HP}-M_{P}\quad(at r_{e})=20,000-9627=10373in-lbs/in\\&M_{N}\quad(Point3)=M_{VN}-M_{P}\quad(at r_{e})=20,000-14,379=5621in-lbs/in\\&b.\quad M_{P}\quad(Point1)=10373in-lbs/in=\&_{1}\Delta\Gamma H^{2}\\&\quad\Delta r=10373/(0.120)(168)^{2}=3.06psi\\&\quad\Delta r=5.621in-lbs/in=\beta_{2}\Delta\Gamma H^{2}\\&\quad\Delta r=5.621/[0.220)(168)^{2}]=9.09psi\\&\quad Second yield at Point3(smaller\Delta r)\\&c.\quad\Delta r=0.90psi\\&d.\quad r_{ep}=r_{e}+\Delta r=4.43+0.90=5.33psi\\&e.\quad M_{P}\quad(Point1)=0.120(0.90)(168)^{2}=3.048in-lbs/in\\&f.\quad D=E//(1-n^{2})=(29)(10^{8})(144)/[14](-0.3)^{2}=45.9\times10^{8}in-lbs/in\\&\quad\Delta x=\gamma_{1}\Delta r H^{4}/D=0.000(0.90)(168)^{4}/45.9(10)^{8}=0.0047in\\&g.\quad X_{ep}=X_{e}+\Delta X=0.0092+0.0047=0.014in\\ &\end{aligned}\\ \end{aligned}$ 

$$\begin{aligned}&\begin{aligned}\\ &\beta_{1}&=0.120\quad\beta_{2}=0.220\\&0.03&\quad\gamma_{1}=0.945-\quad\nu=0.320\\&a.\quad M_{P}\quad(Point1)=M_{HP}-M_{P}\quad(at r_{e})=20,000-9627=10373in-lbs/in\\&M_{N}\quad(Point3)=M_{VN}-M_{P}\quad(at r_{e})=20,000-14,379=5621in-lbs/in\\&b.\quad M_{P}\quad(Point1)=10373in-lbs/in=\&_{1}\Delta\Gamma H^{2}\\&\quad\Delta r=10373/(0.120)(168)^{2}=3.06psi\\&\quad\Delta r=5.621in-lbs/in=\beta_{2}\Delta\Gamma H^{2}\\&\quad\Delta r=5.621/[0.220)(168)^{2}]=9.09psi\\&\quad Second yield at Point3(smaller\Delta r)\\&c.\quad\Delta r=0.90psi\\&d.\quad r_{ep}=r_{e}+\Delta r=4.43+0.90=5.33psi\\&e.\quad M_{P}\quad(Point1)=0.120(0.90)(168)^{2}=3.048in-lbs/in\\&f.\quad D=E//(1-n^{2})=(29)(10^{8})(144)/[14](-0.3)^{2}=45.9\times10^{8}in-lbs/in\\&\quad\Delta x=\gamma_{1}\Delta r H^{4}/D=0.000(0.90)(168)^{4}/45.9(10)^{8}=0.0047in\\&g.\quad X_{ep}=X_{e}+\Delta X=0.0092+0.0047=0.014in\\ &\end{aligned}\\ \end{aligned} 1$$

<!-- batch 18 | page 22 -->

Step 7.Properties at final yield (ultimate unit resistance). After second yield element assumes a simple-simple-simple-free stiffness, therefore from Figure 3-30(+) for $H/L=0.7;$ 



$$\begin{aligned}&r_{\gamma}=0.041\qquad\nu=0.3\\&a.\qquad r_{u}=10.6\;\mathrm{psi}\;(\mathrm{Part}\;(\mathrm{a}),\;\mathrm{Example}\;3\mathrm{A}-1(\mathrm{A}))\\&b.\qquad\Delta r=r_{u}-r_{ep}=10.6-5.33\;=5.23\;\mathrm{psi}\\&c.\qquad D=EII/(b(1-\nu^2))=29(10^8)(144)/(1(1-(0.3)^2))=45.9\times10^8\;\mathrm{in}-\mathrm{lbs}\\&\qquad\Delta x=\gamma_1rH^4/D=(0.045)(5.27)(168)^4/45.9\times10^8=0.037\;\mathrm{in}\\&d.\qquad X_{p}=X_{ep}+\Delta X\;=\;0.014+0.041=0.051\;\mathrm{in}\\ \end{aligned}$$

Step 8.

For actual resistance-deflection curve, see Figure 3A-7 (+)

Step 9.

$$\begin{aligned}X_{E}&=X_{e}(r_{ep}/r_{u})+X_{ep}[1-(r_{e}/r_{u})]+X_{p}[1-(r_{ep}/r_{u})]\quad&Equation3-35\\&X_{E}=0.0092(5.37/10.6)+0.014[1-(4.43/10.6)]+0.051[1-(5.37/10.6)]\\&=0.00466+0.0082+0.0252\\&=0.038in\\ \end{aligned}$$

The equivalent resistance-deflection curve is shown in Figure 3A-7 (+)

<div style="text-align: center;">Figure 3A-7</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_chart_box_344_947_841_1433.jpg" alt="Image" width="41%" /></div>


<!-- batch 18 | page 23 -->

## PROBLEM 3A-3DYNAMIC DESIGN FACTORS FOR A ONE-WAY ELEMENT 

### Problem:Determine the plastic load, mass and load-mass factors for a oneway element. 

## Procedure:

Step 1.Establish design parameters.

Step 2.Determine deflected shape:

a.geometry of element 

b.support conditions 

C.type of load and mass 

Step 3.Determine maximum deflection.

Step 4.Determine deflection function.

a.For distributed load and/or continuous mass determine the deflection at any point 



b.For concentrated loads and concentrated mass determine the deflection at the load 



Step 5.Calculate the shape function.

a.For distributed load and/or continuous mass calculate  (x),Equation 3-43



b.For concentrated load and concentrated mass calculate φr,Equation 3-46



Step 6.Calculate the load factor, K.

a.Use Equations 3-41 and 3-42 for a distributed load 

b.Use Equations 3-41 and 3-45 for a concentrated load 

Step 7.Calculate the mass factor, KM.

a.Use Equations 3-47 and 3-48 for a continuous mass 

b.Use Equations 3-44 and 3-49 for concentrated mass 

Step 8.Calculate the load-mass factor KLM, from Equation 3-53.

<!-- batch 18 | page 24 -->

EXAMPLE 3A-3 (A)DYNAMIC DESIGN FACTORS FOR A ONE-WAY ELEMENT 

Required:The load, mass and load-mass factors for a structural steel beam in the elastic range, with a distributed load.



Solution:

Step 1:Given structural steel beam shown in Figure 3A-8 (+)

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_397_484_789_685.jpg" alt="Image" width="32%" /></div>


a.$L=120\mathrm{i n}$ 

b.Simply supported on both edges 

C.$p(x)=2,000\ \mathrm{lb/in}$ 

$$m(x)=0.0055(\mathrm{lb}-\mathrm{s}^2/\mathrm{in})/\mathrm{in}$$

<div style="text-align: center;">Figure 3A-9</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_443_930_737_1017.jpg" alt="Image" width="24%" /></div>


Step 2:Assumed deflected shape for elastic range is shown in Figure 3A-9 (+)

Step 3:The maximum deflection at the center is;

$$\delta(\mathrm{m a x})=\frac{5p(\mathrm{m a x})L^{4}}{384E L}$$

Step 4:Determine deflection function 

$$\delta(x)=\frac{p(x)}{24E I}\left(L^{3}-2L x^{2}+x^{3}\right)$$

Step 5:Calculate the shape function using Equation 3-43

<!-- batch 18 | page 25 -->

$$\begin{aligned}\phi=&\frac{\delta(\boldsymbol{x})}{\delta_{\max}}=\frac{p(\boldsymbol{x})\boldsymbol{x}}{24EI}\left(L^{3}-2L\boldsymbol{x}^{2}+\boldsymbol{x}^{3}\right)\left(\frac{384EI}{5p(\boldsymbol{x})L^{4}}\right)\\=&\frac{16}{5L^{4}}\left(L^{3}\boldsymbol{x}-2L\boldsymbol{x}^{3}+\boldsymbol{x}^{4}\right)\end{aligned}$$

Step 6:a.Using Equation 3-42, determine equivalent force 

$$\begin{aligned}F_{E}=\int_{0}^{L}p(x)\phi(x)dx=\int_{0}^{L^{20}}\left(2,000\mathrm{lb}/\mathrm{in}\right)\frac{16}{5L^{4}}\left(L^{3}x-2L x^{3}+x^{4}\right)dx\\=\frac{6,400}{L^{4}}\left[\frac{L^{3}x^{2}}{2}-\frac{2L x^{4}}{4}+\frac{x^{5}}{5}\right]_{0}^{120}=1,280L\\=153.600\mathrm{lb}\end{aligned}$$

b.From Equation 3-41,find the load factor 

$$K_{L}=\frac{F_{E}}{F}=\frac{153.600\mathrm{~lb}}{(2.000\mathrm{~lb}/\mathrm{in}\times120\mathrm{~in})}$$

$K_{L}=0.64$ in the elastic range 

Step 7:

a.Find the equivalent mass from Equation 3-48:

$$\begin{aligned}M_{E}=&\int_{0}^{L}m(x)\varphi^{2}(x)dx=0.0055\left(\frac{256}{25L^{8}}\left(\int_{0}^{120}\left(L^{3}x-2L x^{3}+x^{4}\right)^{2}dx\right)\right)\\=&\frac{1.408}{25L^{8}}\left(\int_{0}^{120}\left(L^{6}x^{2}-4L^{4}x^{4}+2L^{3}x^{5}+4L^{2}x^{6}-4L x^{7}+x^{8}\right)dx\right)\\=&\frac{1.408}{25L^{8}}\left[\frac{L^{6}x^{3}}{3}-\frac{4L^{4}x^{5}}{5}+\frac{2L^{3}x^{6}}{6}+\frac{4L^{2}x^{7}}{7}-\frac{4L x^{8}}{8}+\frac{x^{9}}{9}\right]_{0}^{120}\\=&0.00277L\\=&0.3325\mathsf{lb}-\mathsf{s}^{2}/\mathsf{in}\end{aligned}$$

b.From Equation 3-47, calculate the mass factor:

$$K_{M}=\frac{M_{E}}{M}=\frac{0.3325\mathrm{~lb}-s^{2}/\mathrm{in}}{(0.0055\mathrm{~lb}-s^{2}/\mathrm{in}^{2}\times120\mathrm{~in})}$$

$K_{M}=0.50$ in the elastic range 

<!-- batch 18 | page 26 -->

UFC 3-340-025 December 2008Change 2,1 September 2014Step 8:Calculate the load-mass factor as defined by Equation 3-51:

$$\begin{aligned}K_{\mathrm{LM}}&=K_{\mathrm{M}}/K_{\mathrm{L}}\\&=0.50/0.64\end{aligned}$$

$K_{\mathrm{L M}}=0.78$ in the elastic range 

<!-- batch 18 | page 27 -->

## EXAMPLE 3A-3 (B)DYNAMIC DESIGN FACTORS FOR A ONE-WAY ELEMENT 

Required:The load, mass and load-mass factors for a structural steel beam in the plastic range with a distributed load.



## Solution:

Step 1.Given the structural steel beam shown in Figure 3A-8 (+):

a.$L=120\mathrm{i n}$ 

b.Simply-supported on both ends 

C.$p(x)=2,000\ \mathrm{lb/in}$ 

d.$m(x)=0.0055\ (\mathrm{lb}-\mathrm{s}^2/\mathrm{in})/\mathrm{in}$ 

Step 2.Assume deflected shape for the plastic range is shown in Figure 3A-10(+).



<div style="text-align: center;">Figure 3A-10</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_427_771_756_985.jpg" alt="Image" width="27%" /></div>


Step 3.Determine maximum deflection:

$$\delta_{\mathrm{m a x}}=(L/2)\mathrm{t a n}\Theta $$

Step 4.Determine the deflection at any point:

$$\delta(x)=x\tan\Theta\quad x<\mathsf{L}/2$$

Step 5.Calculate the shape function, Equation 3-43:

$$\phi(x)=\frac{\delta(x)}{\delta_{\mathrm{m a x}}}=\frac{x\tan\Theta}{(L/2)\tan\Theta}$$

<!-- batch 18 | page 28 -->

Step 6:

a.Find $F_{E}$ using Equation 3-42:

$$\begin{aligned}F_{E}&=\int_{0}^{L}p(x)\phi(x)dx=2\int_{0}^{60}(2,000\mathrm{lb}/\mathrm{in})(2x/L)dx\\&=4,000\mathrm{lb}/\mathrm{in}\left[x^{2}/L\right]_{0}^{60}\\&=120.000\mathrm{lb}\end{aligned}$$

b.From Equation 3-41:

$$K_{L}=\frac{F_{E}}{F}=\frac{120,000\mathrm{~lb}}{(2,000\mathrm{~lb}/\mathrm{in})(120\mathrm{~in})}$$

$$K_{L}=0.5\ in the plastic range $$

Step 7:

a.Use Equation 3-48 to find the equivalent mass:

$$\begin{aligned}M_{E}=\int_{0}^{L}m(x)\varphi^{2}(x)dx=2\int_{0}^{60}(0.0055)\left(4x^{2}/L^{2}\right)dx\\=0.044\left[\frac{x^{3}}{3L^{2}}\right]_{0}^{60}\\=0.22\left|b-s^{2}\right|\left|n\right|\end{aligned}$$

b.As defined by Equation 3-47

$$K_{M}=\frac{M_{E}}{M}=\frac{0.22\mathrm{~lb}-s^{2}/\mathrm{in}}{(0.0055\mathrm{~lb}-s^{2}/\mathrm{in}^{2})(120\mathrm{~in})}$$

$$K_{M}=0.33\ in the plastic range $$

Step 8.Calculate $K_{L M}$ using Equation 3-53

$$\begin{aligned}K_{LM}&=K_M/K_L\\&=0.33/0.5\end{aligned}$$

$K_{L M}=0.66$ in the plastic range 

<!-- batch 18 | page 29 -->

EXAMPLE 3A-3 (C)DYNAMIC DESIGN FACTORS FOR A ONE-WAY ELEMENT 

Required:The load, mass and load-mass factors for a structural steel beam in the elastic range, with a concentrated load.



Solution:

Step 1:Given structural steel beam shown in Figure 3A-11 (+):

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_475_484_707_684.jpg" alt="Image" width="19%" /></div>


a.$L=120in$ 

b.Simply supported on both sides 

C.$F=240kips$ 

$$m(x)=0.0055(\mathrm{lb}-\mathrm{s}^2/\mathrm{in})/\mathrm{in}$$

Step 2:Assume deflected shape for elastic range is shown in Figure 3A-12 (+):

## Figure 3A-12

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_452_966_737_1056.jpg" alt="Image" width="23%" /></div>


Step 3:Determine maximum deflection:

$$\delta_{\mathrm{m a x}}=\frac{P L^{3}}{48E L}$$

Step 4:Determine deflection functions:

a.for continuous mass 

$$\delta(x)=\frac{P_{X}}{48EI}\left(3L^{2}-4x^{2}\right)$$

b.for concentrated load 

$$\delta_{r}=\frac{P L^{3}}{48E L}$$

<!-- batch 18 | page 30 -->

Step 5:Calculate shape functions 

a.For continuous mass use Equation 3-43

$$\phi(x)=\frac{\delta(x)}{\delta_{\mathrm{m a x}}}=\left(\frac{P x\left(3L^{2}-4x^{2}\right)}{48E I}\right)\left(\frac{48E I}{P L^{3}}\right)$$

b.For concentrated load, use Equation 3-46

$$\begin{aligned}{\phi_{r}}&{{}=\left(\frac{P L^{3}}{48E I}\right)\left(\frac{48E I}{P L^{3}}\right)}\\ {}&{{}=1.0}\end{aligned}$$

Step 6:

a.Find equivalent force from Equation 3-45

$$F_{E}=\sum_{r=1}^{i}F_{r}\phi_{r}=P\times I=240\mathrm{kips}$$

b.Using Equation 3-41, calculate the load factor 

$$K_{L}=\frac{F_{E}}{F}=\frac{240\mathrm{kips}}{240\mathrm{kips}}$$

$K_{L}=1.0$ for the elastic range 

Step 7:a.Equation 3-48 gives the equivalent mass.

$$\begin{aligned}M_{E}&=\int_{0}^{L}m(x)\varphi^{2}(x)dx=0.0055\cdot\frac{256}{25L^{8}}\int_{0}^{120}\left(L^{3}x-2L x^{3}+x^{4}\right)^{2}dx\\&=0.0027L\\&=0.32\mathrm{~lb}\cdot s^{2}/\mathrm{in}\end{aligned}$$

b.From Equation 3-47, calculate the mass factor 

$$K_{M}=\frac{M_{E}}{M}=\frac{0.32\mathrm{~lb}-s^{2}/\mathrm{in}}{(0.0055\mathrm{~lb}-s^{2}/\mathrm{in}^{2}\times120\mathrm{~in})}$$

$$K_{M}=0.49\ in the elastic range $$

Step 8:Calculate the load-mass factor, from Equation 3-53

$$\begin{aligned}K_{LM}&=K_M/K_L\\&=0.49/1.0\end{aligned}$$

$K_{L M}=0.49$ for the elastic range 

<!-- batch 18 | page 31 -->

## EXAMPLE 3A-3 (D)DYNAMIC DESIGN FACTORS FOR A ONE-WAY ELEMENT 

Required:Determine the load, mass and the load-mass factors for a structural steel beam, in the plastic range, with a concentrated load.

Solution:

Step 1.Given structural steel beams shown in Figure 3A-11 (+)

a.$L=120\mathrm{i n}$ 

b.Simply-supported at both edges 

C.$F=240kips$ 

$$m(x)=0.0055\ (\mathrm{lb}-s^2/\mathrm{in})/\mathrm{in}$$

Step 2.Assumed deflected shape for the plastic range is shown in Figure 3A-13(+)



<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_429_734_761_946.jpg" alt="Image" width="27%" /></div>


Step 3:Determine maximum deflection 

$$\delta_{\mathrm{m a x}}=(L/2)\tan\Theta $$

Step 4:Determine deflection function.

a.for continuous mass 

$$\delta(x)=x\tan\Theta\qquad x<\mathsf{L}/2$$

b.for a concentrated load 

$$\delta_{r}=(L/2)\tan\theta $$

Step 5:Calculate shape factors using 

a.Equation 3-43 for continuous mass 

$$\begin{aligned}\phi(x)&=\frac{\delta(x)}{\delta_{max}}=\frac{x\tan\Theta}{(L/2)\tan\phi}\\&=2x/L\quad x<L/2\end{aligned}$$

3A-25

<!-- batch 18 | page 32 -->

b.Equation 3-46 for concentrated load 

$$\phi_{r}=\frac{\delta_{r}}{\delta_{\mathrm{m a x}}}=\frac{(L/2)\mathrm{t a n}\Theta}{(L/2)\mathrm{t a n}\Theta}$$

Step 6:

a.The equivalent force is found using Equation 3-45

$$F_{E}=\sum_{r=1}^{i}F_{r}\phi_{r}=Px_{1}=240\mathrm{kips}$$

b.Equation 3-41 gives the load factor 

$$K_{L}=\frac{F_{E}}{F}=\frac{240kips}{240kips}$$

$K_{L}=1.0$ for plastic range 

Step 7:

a.The equivalent mass is found using Equation 3-48

$$\begin{aligned}&M_{E}=\int_{0}^{L}m(x)\varphi^{2}(x)dx=2\int_{0}^{60}(0.0055)(4x^{2}/L^{2})dx\\ &=0.044\left[\frac{x^{3}}{3L^{2}}\right]_{0}^{60}=0.22lb-s^{2}/in\\ \end{aligned}$$

b.Solve for $K_{M}$ using Equation 3-47

$$K_{M}=\frac{M_{E}}{M}=\frac{0.22\mathrm{~lb}-s^{2}/\mathrm{in}}{\left(0.0055\mathrm{~lb}-s^{2}/\mathrm{in}^{2}\right)\left(120\mathrm{~in}\right)}$$

Step 8:From Equation 3-53, calculate $K_{L M}$ 

$$\begin{aligned}K_{LM}&=K_M/K_L\\&=0.33in the plastic range\end{aligned}$$

<!-- batch 18 | page 33 -->

## PROBLEM 3A-4PLASTIC LOAD-MASS FACTOR 

## Problem:Determine the plastic load-mass factor KLM for a two-way element using (1) general solution and (2) chart solution

Note:The determination of the plastic load-mass factor follows the calculations for the ultimate resistance, hence the structural configuration and the location of the plastic yield lines will be known.



## Procedure: Part (a) - General Solution 

Step 1.See Part (a), Problem 3A-1 for the structural configuration and location of plastic yield lines. Denote sectors formed by yield lines.

Step 2.Determine the load-mass factors properties I, c, and L'for all sectors.

Step 3.Determine the factor l/cL'for all sectors.

Step 4.Calculate the total area of the element.

Step 5.With values obtained above, calculate the plastic load-mass factor for the element using Equation 3-57.



Note:In the above problem, an element of uniform thickness was considered.For non-uniform elements, the load-mass factor is calculated using Equation 3-53 where the mass of the individual sectors must be considered.



## Procedure: Part (b) - Chart Solution 

Step 1.See Part (b), Problem 3A-1 for structural configuration and location of plastic yield lines in terms of x/L or y/H.



Step 2.For known value of X/L or ylH and support condition, determine the loadmass factor for the element from Figure 3-44 (+).

Note:Chart solution may be used only if the element conforms to the requirements listed in Section 3-17.3.



<!-- batch 18 | page 34 -->

## EXAMPLE 3A-4PLASTIC LOAD-MASS FACTOR 

Required:Plastic load-mass factor for the element considered in Example 3A1(A) using (1) general solution and (2) chart solution.

Solution:Part (a) - General Solution 

Step 1.Given structural configuration and location of yield lines shown below (see Part (a), Example 3A-1(A)) in Figure 3A-14 (+)



$$\begin{aligned}&L=240in\\&H=168in\\&X=120in\\&y=137.6in\\&T_c=constant\\ \end{aligned}$$

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_423_692_750_936.jpg" alt="Image" width="27%" /></div>


Step 2.Load-mass factor properties.

a.Sector I.

$$L^{\prime}=y=137.6\mathrm{i n}$$

$$c=y/3=137.6/3$$

$$I=L(L^{\prime3})/12=240(137.6)3/12.$$

b.Sector Il.

<!-- batch 18 | page 35 -->

Figure 3A-15

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_206_314_489_484.jpg" alt="Image" width="23%" /></div>


UFC 3-340-025 December 2008Change 2,1 September 2014

Figure 3A-16

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_734_315_941_579.jpg" alt="Image" width="17%" /></div>


$$\begin{aligned}&L'=x=120in\\&H-y=168-137.6=30.4in\\&c=\frac{L'[H+2(H-y)]}{3[H+(H-y)]}=\frac{120[168+2(30.4)]}{3(168+30.4)}\\&c=120(0.384)\quad retangle\\&I=\frac{(H-y)(L')^3}{3}+\frac{y(L')^3}{12}=\frac{30.4(120)^3}{3}+\frac{137.6(120)^3}{12}=21.60(120)^3\\ \end{aligned}$$

Step 3.Calculate factor l/cL'f or each sector:

Sector I.

$$\frac{I}{cL}=\frac{240(137.6)^{3}/12}{(133.4/3)(133.4)}=8.784m^{2}$$

Sector Il.

$$\frac{I}{cL}=\frac{21.60(120)^{3}}{(0.390\times120)(120)}=6.646\mathrm{in^{2}}$$

Sector IIl.$\frac{I}{cL}=6.646\mathrm{in^2}$ 

Step 4.Area of panel 

$$A=L H=240(168)=40,320\mathrm{i n}^{2}$$

Step 5.Load-mass factor 

$$\begin{aligned}K_{LM}=\frac{\sum I/cL'}{A}\\=\frac{8.256+2(6.646)}{40.320}=0.534\end{aligned}$$

typo, should be 8256133.4 should be 137.6

<!-- batch 18 | page 36 -->

## Solution:Part (b) - Chart Solution 

Step 1.Given: Panel fixed on 3 edges, 1 free and $y/H=0.803$ (see Part (b),Example 3A-1(A)).



Step 2.From Figure 3-44 (+), read load-mass factor 

$K_{L M}=0.543$ 



<!-- batch 18 | page 37 -->

## PROBLEM 3A-5RESPONSE OF A SINGLE-DEGREE-OF-FREEDOM SYSTEM SUBJECT TO DYNAMIC LOAD 

Problem:Determine the maximum response and the corresponding time it occurs of a single-degree-of-freedom system subjected to dynamic load using (a) numerical methods and (b) design charts.

## Procedure: Part (a) - Numerical Methods 

Step 1.Establish dimensional parameters of the system.

Step 2.Determine the natural period of vibration and integration time interval.

Step 3.Construct a table similar to Table 3-14 (+) of Section 3-19.2.

Note:For the first interval $n=1$ ,Equation 3-59 is used and subsequent intervals,the recurrence formula (Equation 3-56) is used.

## Procedure: Part (b) - Chart solution 

Step 1.Same as Step 1 of Example 3A-5, Part (a).

Step 2.Determine the non-dimensional parameters.

Step 3.Determine the ratio of the maximum displacement to the elastic displacement $X_{m}/X_{E}$ and the ratio of the time at which this maximum displacement occurs to the duration of the blast load.

<!-- batch 18 | page 38 -->

EXAMPLE 3A-5MAXIMUM RESPONSE OF SINGLE-DEGREE-OF-FREEDOM SYSTEM SUBJECTED TO A TRIANGULAR LOAD.

Required:The maximum response and the time it occurs, of a single-degree-offreedom system subjected to blast loads, using (a) numerical methods and (b) design charts.



Solution:Part (a) - Numerical Methods 

Step 1.Given:

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_263_596_353_848.jpg" alt="Image" width="7%" /></div>


<div style="text-align: center;">(a)Single-Degree-ofFreedom System </div>


<div style="text-align: center;">Figure 3A-17</div>


<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_520_610_707_855.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">TIME </div>


<div style="text-align: center;">(b) External Load </div>


$$\begin{aligned}&m=2.5\ Kips-sec^2/ft\\ &K=9,860\ Kips/ft\\ &r_u=750\ Kips\\ &X_E=0.076\ ft\\ &T=0.10\ sec\\ &P=1000\ Kips\\ \end{aligned}$$

<div style="text-align: center;"><img src="../pages/batch 18/imgs/img_in_image_box_781_609_965_887.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">(c) Resistance Function </div>


Step 2.Natural period of vibration and integration time interval:

$T_{N}=2\pi\left[m/K\right]^{1/2}=2\pi\left[2.5/9,860\right]^{1/2}=0.10\sec$ 

<!-- batch 18 | page 39 -->

<div style="text-align: center;">Step 3.Construct table as shown below.</div>



<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>n</td><td>t</td><td>$P_{n}$</td><td>$R_{n}$</td><td>！ $P_{n}–R_{n}$</td><td>$A_{n}=(P_{n}-R_{n})/m$</td><td>$\pmb{a}_{n}(\Delta t)^{2}$</td><td>$2X_{n}$</td><td>$X_{n-1}$</td><td>$X_{n+1}$</td></tr><tr><td></td><td>(sec)</td><td>(Kips)</td><td>(Kips)</td><td>(Kips)</td><td>(ft/sec2)</td><td>(ft)</td><td>(ft)</td><td>(ft)</td><td>(ft)</td></tr><tr><td>0</td><td>0</td><td>1000</td><td>0</td><td>1000</td><td>400</td><td>0.040</td><td>0.0</td><td>0.0</td><td>0.020</td></tr><tr><td>1</td><td>0.01</td><td>900</td><td>197.20</td><td>702.80</td><td>281.120</td><td>0.028112</td><td>0.0400</td><td>0.0</td><td>0.068112</td></tr><tr><td>2</td><td>0.02</td><td>800</td><td>671.68</td><td>128.43</td><td>51.366</td><td>0.05137</td><td>0.13622</td><td>0.020</td><td>0.121357</td></tr><tr><td>3</td><td>0.03</td><td>700</td><td>750</td><td>-50.0</td><td>-20.0</td><td>-0.00200</td><td>0.242714</td><td>0.06811</td><td>0.17261</td></tr><tr><td>4</td><td>0.04</td><td>600</td><td>750</td><td>-150.0</td><td>-60.0</td><td>-0.00600</td><td>0.34522</td><td>0.121357</td><td>0.21786</td></tr><tr><td>5</td><td>0.05</td><td>500</td><td>750</td><td>-250.0</td><td>-100.0</td><td>-0.0100</td><td>0.43673</td><td>0.17261</td><td>0.25312</td></tr><tr><td>6</td><td>0.06</td><td>400</td><td>750</td><td>-350.0</td><td>-140.0</td><td>-0.0140</td><td>0.050623</td><td>0.21786</td><td>0.27437</td></tr><tr><td>7</td><td>0.07</td><td>300</td><td>750</td><td>-450.0</td><td>-180.0</td><td>-0.0180</td><td>0.54874</td><td>0.25312</td><td>0.27762</td></tr><tr><td>8</td><td>0.08</td><td>200</td><td>750</td><td>-550.0</td><td>-220.0</td><td>-0.0220</td><td>0.55525</td><td>0.27437</td><td>0.25880</td></tr><tr><td>9</td><td>0.09</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table></body></html></div>


Note:

$$\begin{aligned}&P_{n}=f(t_{n})=1000\left[1-n(\Delta t/T)\right]\\&R_{n}=\frac{KX_{n}for X_{n}<X_{e}}{r_{u}=750for X_{n}>X_{e}}\\&X_{n+1}=2X_{n}-X_{n-1}+a_{n}(\Delta t)^{2}\\&Note:\\&For n=0,X_{n+1}(Column10)=X_{0+1}=X_{1}=(1/2)a_{0}(\Delta t)^{2}\\&\quad=(1/2)(0.040)\\&\quad=0.02ft\\ \end{aligned}$$

<!-- batch 18 | page 40 -->

$$\begin{aligned}For n=1,2X_n(Collun8)&=2X_1=2[(1/2)a_0(\Delta t)^2]\\&=2(0.02)=0.04ft\end{aligned}$$

$$X_{n-1}(\mathrm{Co}\mathrm{l}\mathrm{u}\mathrm{m}\mathrm{n}\mathrm{9})=X_{0}=0.0$$

$$\begin{aligned}X_{n+1}(Column10)&=X_2=2X_1-X_0+a_1(\Delta t)^2\\&=2(0.02)-0+0.02811\\&=0.06811ft\end{aligned}$$

$$\begin{aligned}For n=2,2X_n(Column8)&=2X_2=2(0.06811)\\&=0.13622ft\end{aligned}$$

$$X_{n-1}\left(\mathrm{Coulomb}9\right)=X_{1}=0.02\mathrm{ft}.$$

$$\begin{aligned}X_{n+1}(Collun10)&=X_3=2X_2-X_1+a_2(\Delta t)^2\\&=(2)(0.06811)-0.02+0.005137\\&=0.121357 産 \\ \end{aligned}$$

For $n=3,4,\ldots$ ,repeat the above procedure.

Solution:Part (b) - Design Charts 

Step 1.

Same as Step 1 of Example 3A-5, Part (a).

Step 2.

Non-dimensional parameters:

a.Natural period of vibration,$\mathsf{T}_{\mathsf{n}}$ .

$$T_{p}=2\pi[m/K]^{1/2}=2\pi[2.5/9,860]^{1/2}=0.10\sec $$

b.Ratio of duration of blast load Tto natural period $T_{N}$ 

$$T/T_{N}=0.10/0.10=1.0$$

C.Ratio of peak resistance $r_{u}$ to peak load P 

$$r_{u}/P=750/1000=0.75$$

Step 3.Using the ratios calculated in Step 2 and Figures 3-54 (+) and 3-55 (+)determine the value of $X_{m}/X_{E}\mathrm{a n d}t_{m}/T_{N}$ 



$$\mathrm{For}\ T/T_{N}=1\quad\mathrm{and}\quad r_{u}/P=0.75$$

$X_{m}/X_{E}=3.7$ from Figure 3-54

$t_{m}/T=0.77$ from Figure 3-55

<!-- batch 18 | page 41 -->

Step 4.Determine $X_{m}$ and $t_{m}$ .

$$\begin{aligned}&X_{m}/X_{E}=3.7\\&X_{m}=3.7X_{E}=3.7(.076)=0.28144\mathrm{~ft}\\&t_{m}/T=0.77\\&t_{m}=0.77T=0.77(0.10)=0.077\mathrm{~sec}\\ \end{aligned}$$

UFC 3-340-025 December 2008Change 2,1 September 2014

<!-- batch 18 | page 42 -->

# PROBLEM 3A-6MAXIMUM RESPONSE OF A SINGLE-DEGREE-OF-FREEDOM  SYSTEM TO BILINEAR BLAST LOADS 

Problem:Determine $\pmb{X}_{m}/\pmb{X}_{E},t_{m}/T_{N}$ and $t_{E}/T$ (when applicable) for a single-degreeof-freedom system subject to various bilinear blast loads.

## Procedure: Part (a) - Solution in Region D 

Step 1.Establish normalized parameters.

Step 2.Enter Table 3-15 (+) with the given C parameters and determine which figures have to be used.



Step 3.Enter each of the figures determined in Step 2, with the given values of the other two parameters and determine the region where the intersection points are located.



Step 4.Based on the region where the intersection points are located, enter the appropriate figure and find $X_{m}/X_{E},t_{m}/T_{N}$ and $t_{F}/T$ 

## Procedure: Part (b) - Solution in Region C - Graphical Interpolation

Step 1.Same as Step 1 in Part (a).

Step 2.Same as Step 2 in Part (a).

Step 3.Same as Step 3 in Part (a).

Step 4.Set up a table as shown in Table $3A-1(+)$ Post each figure number and the corresponding values of $C_{1}$ and $C_{2}$ , leaving a space between each line of information. Post in the spaces the appropriate values of $C_{1}$ and $C_{2}$ needed for interpolation. Enter each of the figures determined in Step 2with the given parameters and find the values of $X_{m}/X_{E}$ . Post these values in Table 3A-1.



Step 5.Use log-log graph paper to plot the points obtained in Step 4. Post these values in Table 3A-1 (+), using linear interpolation where necessary.

Step 6.Plot on log-log graph paper the points which represent $(X_{m}/X_{E},C_{2})$ for the given value of C. Use linear interpolation to find $X_{m}/X_{E}$ for given value of 

$C_{2}$ 



## Procedure: Part (c) - Solution in Region C - Mathematical Interpolation 

Step 1.Same as Step 1 in Part (a).

Step 2.Same as Step 2 in Part (a).

Step 3.Same as Step 3 in Part (a).

Step 4.Same as Step 4 in Part (b).

<!-- batch 18 | page 43 -->

UFC 3-340-025 December 2008Change 2, 1 September 2014Step 5.Solve for In $\Upsilon_{a}$ and In $\Upsilon_{b}$ using Equations 3-83 and 3-84.

Step 6.Solve for InY using Equation 3-85.

Step 7.Solve for Y using Equation 3-86.



<!-- batch 18 | page 44 -->

# EXAMPLE 3A-6MAXIMUM RESPONSE OF A SINGLE-DEGREE-OF-FREEDOM  SYSTEM TO BILINEAR BLAST LOADS 

Required:Determine $\pmb{X}_{m}/\pmb{X}_{E},t_{m}/T_{N}$ and $t_{E}/T$ (when applicable) for a single-degreeof-freedom system subject to various bilinear blast loads.

Solution:Part (a) - Solution in Region D 

Step 1.Given:$\begin{aligned}{P/r_{u}}&{{}=1.0}\\ {T/T_{N}}&{{}=3.0}\\ {C_{1}}&{{}=0.66}\\ {C_{2}}&{{}=50}\end{aligned}$ 

$$\begin{aligned}{P/r_{u}}&{{}=1.0}\\ {T/T_{N}}&{{}=3.0}\\ {C_{1}}&{{}=0.66}\\ {C_{2}}&{{}=50}\end{aligned}$$

Step 2.Enter Table 3-15 (+) with $C_{1}=0.66$ and $C_{2}=50$ . Note Figures 3-119$(\pm/\pm/\pm)$ ,3-120(+/+/+), 3-147$(\pm/\pm/\pm)$ ,and $3–148(\pm/\pm/\pm)$ apply.

Step 3.Enter each of the figures determined in Step 2, with $P/r_{u}=1.0$ and $T/T_{N}=$ 3.0. Note that the intersection point is located to the right of the line of solid squares, defined as Region D. In Region D, the maximum dynamic response depends only on the shock load described by $P/r_{u}$ and ${\dot{T}}/T_{N};$ the gas load described by $C_{1}P/r_{u}$ ,and $C_{2}T/T_{n}$ does not influence the maximum dynamic response. Consequently, Figures 3-64a (+) and 3-64b $(+)$ for a single triangular load pulse apply. Enter Figure 3-64a with $P/r_{u}=1.0$ and $T/\bar{T_{N}}=3.0$ and find $X_{m}/X_{E}=3.55,\;t_{m}/T_{N}=0.98,\;t_{E}/T=0.086$ 

Solution:Part (b) - Solution in Region C - Graphical Interpolation 

Step 1.Given:$\begin{aligned}&P/r_{u}=32\\&T/T_{N}=0.10\\&C_{1}=0.06\\&C_{2}=20\\ \end{aligned}$ 

$$\begin{aligned}&P/r_{u}=32\\&T/T_{N}=0.10\\&C_{1}=0.06\\&C_{2}=20\\ \end{aligned}$$

Step 2.Enter Table 3-15 (+) with $C_{1}=0.06$ and $C_{2}=20$ . Note Figures 3-108$(\pm/\pm/\pm)$ 1,3-109(+/+/+),3-133$(\pm/\pm/\pm)$ and 3-134$(\pm/\pm/\pm)$ apply.

Step 3.Enter each of these Figures with $P/r_{u}=32$ and $T/T_{n}=0.10$ . Note that the intersection point is not located in Regions A, B or D. Therefore the intersection points lie in region C and interpolation between charts is required to obtain a solution.



Step 4.Set up table as shown in Table 3A-1 (+) below. Post each chart number and the corresponding values of $C_{1}$ and $C_{2}$ leaving a space between each line of information. Post in the spaces the appropriate values of $C_{1}$ and $C_{2}$ needed for interpolation. Enter Figure 3-108$(\underline{{\pm}}/\underline{{\pm}}/\underline{{\pm}})$ with $P/r_{u}=32$ and 

<!-- batch 18 | page 45 -->

$T/T_{N}=0.10$ and find $X_{m}/X_{E}=112$ .Post this value in the table. Enter Figure 3-109$(\underline{{\pm}}/\underline{{\pm}}/\underline{{\pm}})$ with $P/r_{u}=32$ and $T/T_{N}=0.10$ Iand find $X_{m}/X_{E}=86$ Post this value in the table. Repeat this process for Figures $3-133(\pm/\pm/\pm)$ and 3-134$(\pm/\pm/\pm)$ , and post values for $X_{m}/X_{E}$ ·in the table.

Step 5.Use log-log graph paper to plot the points (112, 0.068) and (86, 0.046)which represent $(X_{m}/X_{E},C_{1})$ for $C_{2}=10$ as shown in Figure 3-267 (+). Use straight-line interpolation to find $X_{m}/X_{E}=103\mathrm{f o r}C_{1}=0.060$ 1. Post this value in the table. Repeat this process for $C_{2}=30$ ,and find $X_{m}/X_{E}=251$ for $C_{1}=0.06$ as shown in Figure 3-267.



Step 6.Plot on log-log graph paper the points (103, 10) and (251, 30) which represent $(X_{m}/X_{E},C_{2})$ for $C_{1}=0.060$ 1. Use straight-line interpolation for finding $X_{m}/X_{E}=182\mathrm{f o r}C_{2}=50$ as shown in Figure 3-267 (+). Thus the solution is $X_{m}/X_{E}=182$ 




<div style="text-align: center;"><html><body><table border="1"><tr><td>Figure No.</td></tr><tr><td>3-108 (±/+/±)</td></tr><tr><td>3-109 $(\underline{{\pm}}/\underline{{\pm}}/\underline{{\pm}})$</td></tr><tr><td>3-133 (+/+/+)</td></tr><tr><td>3-134 (±/+/±)</td></tr></table></body></html></div>


Solution:Part (c) - Solution in Region C - Mathematical Interpolation 

Step 1.Same as Step 1 of Part (b).

Step 2.Same as Step 2 of Part (b).

Step 3.Same as Step 3 of Part (b).

Step 4.Same as Step 4 of Part (b).

Step 5.Using Equations 3-83 and 3-84, find In $\Upsilon_{a}$ and ln $\Upsilon_{b}$ 

<!-- batch 18 | page 46 -->

$$\begin{aligned}\ln Y_{a}=&\ln Y_{1}+\frac{\ln\left[Y_{2}/Y_{1}\right]\ln\left[C_{1}/C_{11}\right]}{\ln\left[C_{12}/C_{11}\right]}\\=&\ln(112)+\frac{\ln(86/112)\ln(0.060/0.068)}{\ln(0.046/0.068)}\\\ln Y_{a}=&4.6339\\\ln Y_{b}=&\ln Y_{3}+\frac{\ln\left[Y_{4}/Y_{3}\right]\ln\left[C_{1}/C_{13}\right]}{\ln\left[C_{14}/C_{13}\right]}\\=&\ln(340)+\frac{\ln(230/340)\ln(0.06/0.075)}{\ln(0.056/0.075)}\\\ln Y_{b}=&5.5304\end{aligned}$$

Step 6.Find InY from Equation 3-85:

$$\begin{aligned}\ln Y&=\ln Y_{a}+\frac{\left(\ln Y_{b}-\ln Y_{a}\right)\ln\left(C_{2}/C_{21}\right)}{\ln\left(C_{23}/C_{21}\right)}\\&=4.6339+\frac{\left(5.5304-4.639\right)\ln\left(20/10\right)}{\ln\left(30/10\right)}\end{aligned}$$

Ir $Y=5.1995$ 

Step 7.Solve for Y using Equation 3-86:

$$\begin{aligned}\mathsf{Y}&=\mathsf{e}^{\ln\mathsf{Y}}\\&=\mathsf{e}^{5.1995}\\\mathsf{Y}&=181\end{aligned}$$

UFC 3-340-025 December 2008Change 2, 1 September 2014

<!-- batch 18 | page 47 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td colspan="2"></td><td>APPENDIX 3B LIST OF SYMBOLS</td></tr><tr><td>a</td><td>(1)</td><td>acceleration $(\mathsf{i n}/\mathsf{m s}^{2})$</td></tr><tr><td></td><td>(2)</td><td>depth of equivalent rectangular stress block (in)</td></tr><tr><td>A</td><td>area $({\mathsf{i n}}^{2})$</td><td></td></tr><tr><td>$A_{a}$</td><td></td><td>area of diagonal bars at the support within a width b $({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{o}$</td><td>area of openings</td><td>$(\mathsf{f t}^{2})$</td></tr><tr><td>$A_{s}^{\prime}$ $A_{s}$</td><td></td><td>area of tension reinforcement within a width $b\:({\mathsf{i n}}^{2})$</td></tr><tr><td>$A_{s H}$</td><td></td><td>area of compression reinforcement within a width area of flexural reinforcement within a width b in the horizontal direction on $b\:({\mathsf{i n}}^{2})$</td></tr><tr><td></td><td>each face</td><td>$\left(\mathsf{i n}^{2}\right)^{\star}$</td></tr><tr><td>$A_{s V}$</td><td>each face $(\mathsf{i n}^{2})^{\star}$</td><td>area of flexural reinforcement within a width b in the vertical direction on</td></tr><tr><td>$A_{v}$</td><td>or _ı and a width</td><td>total area of stirrups or lacing reinforcement in tension within a distance, $s_{s}$ $\dot{b}_{s}\mathrm{o r}b_{I}(\mathsf{i n}^{2})$</td></tr><tr><td>$A_{I I}$ $A_{I}$</td><td></td><td>area of sectorI and ll, respectively $({\mathsf{i n}}^{2})$</td></tr><tr><td>$b$</td><td>(1)</td><td>width of compression face of flexural member (in)</td></tr><tr><td></td><td>(2)</td><td>width of concrete strip in which the direct shear stresses at the supports are resisted by diagonal bars (in)</td></tr><tr><td>$b_{s}$</td><td></td><td>width of concrete strip in which the diagonal tension stresses are resisted</td></tr><tr><td>$b_{1}$</td><td>by stirrups of area . (in)</td><td>width of concrete strip in which the diagonal tension stresses are resisted $A_{v}$</td></tr><tr><td>B</td><td>by lacing of area constant defined in paragraph</td><td>$A_{v}\left(\mathsf{i n}\right)$</td></tr><tr><td>c</td><td>(1)</td><td>distance from the resultant applied load to the axis of rotation (in)</td></tr><tr><td></td><td>(2) damping coefficient</td><td></td></tr><tr><td>$c_{I},c_{I I}$</td><td></td><td>distance from the resultant applied load to the axis of rotation for sectors I</td></tr><tr><td></td><td>and Il, respectively (in)</td><td></td></tr><tr><td>$c_{s}$</td><td>dilatational velocity of concrete (ft/sec)</td><td></td></tr><tr><td>$c$</td><td>shear coefficient</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>$C_{c r}$</td><td>critical damping</td><td></td></tr></table></body></html></div>


<!-- batch 18 | page 48 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>$C_{r\alpha}$ $C_{d}$ $C_{f}$</td><td>shear coefficient for ultimate shear stress of one-way elements post-failure fragment coeficient peak reflected pressure coefficient at angle of incidence α $(\mathsf{I b}^{2}\mathrm{-}\mathsf{m s}^{4}/\mathsf{i n}^{8})$</td></tr><tr><td>$C_{s H}$ $C_{s}$</td><td>shear coefficient for ultimate support shear for one-way elements shear coefficient for ultimate support shear in horizontal direction for two-</td></tr><tr><td>$C_{s V}$</td><td>way elements * shear coefficient for ultimate support shear in vertical direction for two-way</td></tr><tr><td>$C_{D}$</td><td>elements*</td></tr><tr><td>$C_{D}q$</td><td>drag coefficient</td></tr><tr><td>$C_{D}q_{o}$</td><td>drag pressure (psi)</td></tr><tr><td>$C_{E}$</td><td>peak drag pressure (psi)</td></tr><tr><td>$C_{H}$</td><td>equivalent load factor shear coefficient for ultimate shear stress in horizontal direction for two-</td></tr><tr><td></td><td>way elements*</td></tr><tr><td>$C_{M}$ $C_{L}$</td><td>leakage pressure coefficient</td></tr><tr><td>$C_{u}$</td><td>maximum shear coefficient</td></tr><tr><td>$C_{u}{'}$</td><td>impulse coefficient at deflection $X_{u}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>$C_{v}$</td><td>impulse coefficient at deflection $X_{m}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td></td><td>shear coefficient for ultimate shear stress in vertical direction for two-way elements*</td></tr><tr><td>(1) $C_{1}$</td><td>impulse coefficient at deflection $X_{1}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>(2)</td><td>parameter defined in figure</td></tr><tr><td>(3)</td><td>ratio of gas load to shock load</td></tr><tr><td>$C_{1}$</td><td>impulse coefficient at deflection $X_{m}(\mathrm{p s i}-\mathrm{m s}^{2}/\mathrm{i n}^{2})$</td></tr><tr><td>$C_{2}$</td><td>ratio of gas load duration to shock load duration</td></tr><tr><td>$d$</td><td>distance from extreme compression fiber to centroid of tension</td></tr><tr><td></td><td>reinforcement (in)</td></tr><tr><td>reinforcement (in) $d^{\prime}$</td><td>distance from extreme compression fiber to centroid of compression</td></tr></table></body></html></div>


<!-- batch 18 | page 49 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td>$d_{c}$</td><td colspan="2">distance between the centroids of the compression and tension reinforcement (in)</td></tr></thead><tbody><tr><td>$d_{e}$</td><td>distance from support and equal to distance d or (in)</td><td>$d_{c}$</td></tr><tr><td>$d_{i}$</td><td>inside diameter of cylindrical explosive container (in)</td><td></td></tr><tr><td>$d{1$</td><td></td><td>distance between center lines of adjacent lacing bends measured normal</td></tr><tr><td>$d_{c o}$</td><td>to flexural reinforcement (in)</td><td></td></tr><tr><td>$d_{1}$</td><td>diameter of steel core (in)</td><td></td></tr><tr><td>D</td><td></td><td>diameter of cylindrical portion of primary fragment (in)</td></tr><tr><td></td><td>(1)</td><td>unit flexural rigidity (lb-in)</td></tr><tr><td></td><td>(2) (3)</td><td>location of shock front for maximum stress (ft)</td></tr><tr><td>$D_{o}$</td><td></td><td>minimum magazine separation distance (ft)</td></tr><tr><td>$D_{E}$</td><td></td><td>nominal diameter of reinforcing bar (in)</td></tr><tr><td>DIF</td><td></td><td>equivalent loaded width of structure for non-planar wave front (ft)</td></tr><tr><td></td><td>dynamic increase factor</td><td></td></tr><tr><td>DLF</td><td>dynamic load factor</td><td>base of natural logarithms and equal to 2.71828.….</td></tr><tr><td>e $(2E^{\prime})^{1/2}$</td><td></td><td></td></tr><tr><td>E</td><td></td><td>Gurney Energy Constant (ft/sec)</td></tr><tr><td>$E_{c}$</td><td>modulus of elasticity</td><td></td></tr><tr><td>$E_{s}$</td><td></td><td>modulus of elasticity of concrete (psi)</td></tr><tr><td>f</td><td></td><td>modulus of elasticity of reinforcement (psi)</td></tr><tr><td></td><td>unit external force (psi)</td><td></td></tr><tr><td>$f_{c}$</td><td></td><td>static ultimate compressive strength of concrete at 28 days (psi)</td></tr><tr><td>$\pmb{f}_{d c}$</td><td></td><td>dynamic ultimate compressive strength of concrete (psi)</td></tr><tr><td>$f_{d s}$</td><td>dynamic design stress for reinforcement (psi)</td><td></td></tr><tr><td>$f_{d u}$</td><td>dynamic ultimate stress of reinforcement (psi)</td><td></td></tr><tr><td>$f_{d y}$</td><td>dynamic yield stress of reinforcement (psi)</td><td></td></tr><tr><td>$f_{s}$</td><td>static design stress for reinforcement (a function of , and @) (psi)</td><td>$\pmb{f}_{y_{1}}$ $f_{u}$</td></tr><tr><td>$f_{u}$</td><td>static ultimate stress of reinforcement (psi)</td><td></td></tr><tr><td>$f_{y}$</td><td>static yield stress of reinforcement (psi)</td><td></td></tr></tbody></table></body></html></div>


<!-- batch 18 | page 50 -->

F (1)total external force (lbs)

(2)coefficient for moment of inertia of cracked section 

(3)function of $C_{2}$ and $C_{1}$ for bilinear triangular load 

F{$force in the reinforcing bars (lbs)

FE equivalent external force (Ibs)

g variable defined in Table 4-3 (+)

h charge location parameter (ft)

H (1)span height (in)

(2)distance between reflecting surface(s) and/or free edge(s) in 

vertical direction (ft)

Hc$height of charge above ground (ft)

Hc scaled height of charge above ground (ft/lb1/3)

Hs}$height of structure (ft)

HT scaled heigt oftriple point (ft/b/3)

i unit positive impulse (psi-ms)

i unit negative impulse (psi-ms)

$\ra{{}$sum of scaled unit blast impulse capacity of receiver panel and scaled unit 

blast impulse attenuated through concrete and sand in a composite 

element (psi-ms/lb /{3)

$ib$unit blast impulse (psi-ms)

$\fra{{ }$scaled unit blast impulse (psi-ms/|b/3)

$\overline{{\overline{{\boldsymbol{i}}}_{b t}}}$ totalscaled unit blast impulsecapacityofcompositelemnt(psi-ms/lb/)

$\overline{{i_{b a}}}$ scaled unit blast impulse capacity of receiver panel of composite element 

(psi-ms/lb1/³)

$\rac{{ b}$scaled unit blast impulse capacity of donor panel of composite element 

(psi-ms/lb1/³)

ie unit excess blast impulse (psi-ms)

$ir unit positive normal reflected impulse (psi-ms)

ir unit negative normal reflected impulse (psi-ms)

$is$unit positive incident impulse (psi-ms)



<!-- batch 18 | page 51 -->


<div style="text-align: center;"><html><body><table border="1"><thead><tr><td colspan="2">unit negative incident impulse (psi-ms)</td></tr></thead><tbody><tr><td>$j_{s}$</td><td>moment of inertia $(\mathsf{i n}^{4})$</td></tr><tr><td>$I_{a}$</td><td>average of gross and cracked moments of inertia of width $b(\mathsf{i n}^{4})$</td></tr><tr><td>$I_{c}$</td><td>moment of inertia of cracked concrete section of width $b(\mathsf{i n}^{4})$</td></tr><tr><td>$I_{g}$</td><td>moment of inertia of gross concrete section of width b $(\mathsf{i n}^{4})$</td></tr><tr><td>$I_{m}$</td><td>mass moment of inertia $(\mathsf{I b}{-}\mathsf{m s}^{2}{-}\mathsf{i n})$</td></tr><tr><td>$j$</td><td>ratio of distance between centroids of compression and tension forces to the depth d</td></tr><tr><td>$k$</td><td>constant defined in paragraph</td></tr><tr><td>K</td><td>(1） unit stiffness (psi-in for slabs) (Ib/in/in for beams)</td></tr><tr><td></td><td>(2) constant defined in paragraph</td></tr><tr><td>$K_{e}$</td><td>elastic unit stffness (psi/in for slabs) (Ib/in/in for beams)</td></tr><tr><td>$K_{e p}$</td><td>elasto-plastic unit stiffness (psi-in for slabs) (psi for beams)</td></tr><tr><td>$K_{E}$</td><td>equivalent elastic unit stiffness (psi-in for slabs) (psi for beams)</td></tr><tr><td>$K_{L}$</td><td>load factor</td></tr><tr><td>$K_{L M}$</td><td>load-mass factor</td></tr><tr><td>$(K_{L M})_{u}$</td><td>load-mass factor in the ultimate range</td></tr><tr><td>$(K_{L M})_{u p}$</td><td>load-mass factor in the post-ultimate range</td></tr><tr><td>$K_{M}$</td><td>mass factor</td></tr><tr><td>$K_{R}$</td><td>resistance factor</td></tr><tr><td>$K_{1}$</td><td>factor defined in paragraph</td></tr><tr><td>$K E$</td><td>kinetic energy</td></tr><tr><td></td><td>charge location parameter (ft)</td></tr><tr><td>$I_{p}$</td><td>spacing of same type of lacing bar (in)</td></tr><tr><td>L</td><td>(1) span length (in) except in chapter 4 $\left(\mathsf{f t}\right)^{\star}$</td></tr><tr><td></td><td>(2) distance between reflecting surface(s) and/or free edge(s) in</td></tr><tr><td>$L_{I}$</td><td>horizontal direction (ft) length of lacing bar required in distance s/ (in)</td></tr></tbody></table></body></html></div>


<!-- batch 18 | page 52 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>embedment length of reinforcing bars (in) $L_{o}$</td><td></td></tr><tr><td>$L_{w}$</td><td>wave length of positive pressure phase (ft)</td></tr><tr><td>$L_{w}$</td><td>wave length of negative pressure phase (ft)</td></tr><tr><td>$L_{w b},L_{w d}$</td><td>wave length of positive pressure phase at points b and d, respectively (ft)</td></tr><tr><td>$L_{1}$</td><td>total length of sector of element normal to axis of rotation (in)</td></tr><tr><td>$m$</td><td>unit mass $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$</td></tr><tr><td>$m_{a}$</td><td>average of the effective elastic and plastic unit masses $(\mathsf{p s i}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$m_{e}$</td><td>effective unit mass $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$</td></tr><tr><td>$m_{u}$</td><td>effective unit mass in the ultimate range $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$</td></tr><tr><td>$m_{u p}$ $M$</td><td>effective unit mass in the post-ultimate range $(\mathsf{p s i}{\scriptstyle-}\mathsf{m s}^{2}/\mathsf{i n})$</td></tr><tr><td>(1)</td><td>unit bending moment (in-lbs/in)</td></tr><tr><td>(2)</td><td>total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{e}$</td><td>effective total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{u}$</td><td>ultimate unit resisting moment (in-lbs/in)</td></tr><tr><td>$M_{c}$</td><td>moment of concentrated loads about line of rotation of sector $(\mathsf{i n-l b s})$</td></tr><tr><td>$M_{A}$</td><td>fragment distribution parameter</td></tr><tr><td>$M_{E}$</td><td>equivalent total mass $(\mathsf{I b}{\scriptstyle-\mathsf{m s}^{2}/\mathsf{i n}})$</td></tr><tr><td>$M_{H N}$</td><td>ultimate unit negative moment capacity in horizontal direction $\left(\mathsf{i n-l b s}/\mathsf{i n}\right)^{\star}$</td></tr><tr><td>$M_{H P}$</td><td>ultimate unit positive moment capacity in horizontal direction $(\mathsf{i n-l b s/i n})^{\star}$</td></tr><tr><td>$M_{N}$</td><td>ultimate unit negative moment capacity at supports (in-lbs/in)</td></tr><tr><td>$M_{P}$</td><td>ultimate unit positive moment capacity at midspan (in-lbs/in)</td></tr><tr><td>$M_{V N}$</td><td>ultimate unit negative moment capacity in vertical direction (in-bs/in)*</td></tr><tr><td>$M_{V P}$</td><td>ultimate unit positive moment capacity in vertical direction $(\mathsf{i n}{-}\mathsf{l b s}/\mathsf{i n})^{\star}$</td></tr><tr><td>n</td><td>(1) modular ratio</td></tr><tr><td></td><td>(2) number of time intervals</td></tr><tr><td>$N$</td><td>number of adjacent reflecting surfaces</td></tr><tr><td>$N_{f}$</td><td>number of primary fragments larger than $W_{f}$</td></tr></table></body></html></div>


<!-- batch 18 | page 53 -->

p reinforcement ratio equal to $\frac{A_{s}}{b d}\mathrm{o r}\frac{A_{s}}{b d_{c}}$ 

$p^{\prime}$ reinforcement ratio equal to $\frac{A_{s}^{\top}}{b d}\mathrm{o r}\frac{A_{s}^{\top}}{b d_{c}}$ 

$p_{b}$ reinforcement ratio producing balanced conditions at ultimate strength 

$p_{m}$ mean pressure in a partially vented chamber (psi)

$p_{m o}$ peak mean pressure in a partially vented chamber (psi)

$p_{H}$ reinforcement ratio in horizontal direction on each face *

$p_{T}$ reinforcement ratio equal to $p_{H}+p_{v}$ 

$p_{v}$ reinforcement ratio in vertical direction on each face*

$p(x)$ distributed load per unit length 

$P$ (1) pressure (psi)

(2)concentrated load (Ibs)

$P$ negative pressure (psi)

$P_{i}$ interior pressure within structure (psi).

$\Delta P_{i}$ interior pressure increment (psi)

$P_{f}$ fictitious peak pressure (psi)

$P_{o}$ peak pressure (psi)

$P_{r}$ peak positive normal reflected pressure (psi)

$P_{r}^{-}$ peak negative normal reflected pressure (psi)

$\bar{P}_{r\alpha}$ peak reflected pressure at angle of incidence α (psi)

$P_{s}$ positive incident pressure (psi)

$P_{s b},P_{s e}$ positive incident pressure at points b and e, respectively (psi)

$P_{s o}$ peak positive incident pressure (psi)

$P_{s o}$ peak negative incident pressure 

$P_{s o b},P_{s o d},P_{s o e}$ peak positive incident pressure at points b, d, and e, respectively (psi)

$q$ dynamic pressure (psi)



<!-- batch 18 | page 54 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>$q_{e}$ $q_{b}$</td><td>dynamic pressure at points b and e, respectively (psi)</td></tr><tr><td>$q_{o}$</td><td>peak dynamic pressure (psi)</td></tr><tr><td>$q_{0e}$ $q_{o b}$</td><td>peak dynamic pressure at points b and e, respectively (psi)</td></tr><tr><td>r</td><td>(1) unit resistance (psi)</td></tr><tr><td></td><td>(2) radius of spherical TNT (density equals 95 charge (ft)) $\mathsf{I b}/\mathsf{f t}^{3}$</td></tr><tr><td>r</td><td>unit rebound resistance (psi)</td></tr><tr><td>$\Delta r$</td><td>change in unit resistance (psi)</td></tr><tr><td>$r_{e}$</td><td>elastic unit resistance</td></tr><tr><td>$r_{e p}$</td><td>elasto-plastic unit resistance (psi)</td></tr><tr><td>$r_{u}$</td><td>ultimate unit resistance (psi, for slabs) (Ib/in for beams)</td></tr><tr><td>$r_{u p}$</td><td>post-ultimate unit resistant (psi)</td></tr><tr><td>$r_{1}$</td><td>radius of hemispherical portion of primary fragment (in)</td></tr><tr><td>R</td><td>(1) total internal resistance (Ibs)</td></tr><tr><td></td><td>(2) slant distance (ft)</td></tr><tr><td>$R_{f}$</td><td>distance traveled by primary fragment (ft)</td></tr><tr><td>$R_{I}$</td><td>radius of lacing bend (in)</td></tr><tr><td>$R_{A}$</td><td>normal distance (ft)</td></tr><tr><td>$R_{E}$</td><td>equivalent total internal resistance (Ibs)</td></tr><tr><td>$R_{G}$</td><td>ground distance (t)</td></tr><tr><td>$R_{u}$</td><td>total ultimate resistance</td></tr><tr><td>$R_{I},R_{I I}$</td><td>total internal resistance of sectors I and Il, respectively (Ilbs)</td></tr><tr><td>$s_{s}$</td><td>spacing of stirups in the direction parallel to the longitudinal reinforcement (in)</td></tr><tr><td>S_1</td><td>spacing of lacing in the direction parallel to the longitudinal reinforcement (in)</td></tr><tr><td>S</td><td>height of front wall or one-half its width, whichever is smaller (ft)</td></tr><tr><td>SE</td><td>strain energy</td></tr><tr><td>t</td><td>time (ms)</td></tr><tr><td>Δt</td><td>time increment (ms)</td></tr><tr><td>$t_{a}$</td><td>any time (ms)</td></tr></tbody></table></body></html></div>


<!-- batch 18 | page 55 -->


<div style="text-align: center;"><html><body><table border="1"><tr><td>$t_{c}$ $t_{f}$ $t_{e}$ $t_{b}$</td><td>time of arrival of blast wave at points b, e, and f, respectively (ms)</td></tr><tr><td>(1)</td><td>clearing time for reflected pressures (ms)</td></tr><tr><td>(2)</td><td>container thickness of explosive charges (in)</td></tr><tr><td>rise time (ms) $t_{d}$</td><td></td></tr><tr><td>$t_{E}$</td><td>time to reach maximum elastic deflection</td></tr><tr><td>$t_{m}$</td><td>time at which maximum deflection occurs (ms)</td></tr><tr><td>$t_{0}$</td><td>duration of positive phase of blast pressure (ms)</td></tr><tr><td>$t_{0}$</td><td>duration of negative phase of blast pressure (ms)</td></tr><tr><td>$t_{o f}$</td><td>fictitious positive phase pressure duration (ms)</td></tr><tr><td>$t_{0f}$</td><td>fictitious negative phase pressure duration (ms)</td></tr><tr><td>$t_{r}$</td><td>fictitious reflected pressure duration (ms)</td></tr><tr><td>$t_{u}$</td><td>time at which ultimate deflection occurs (ms)</td></tr><tr><td>$t_{y}$</td><td>time to reach yield (ms)</td></tr><tr><td>$t_{A}$</td><td>time of arrival of blast wave (ms)</td></tr><tr><td>$t_{1}$</td><td>time at which partial failure occurs (ms)</td></tr><tr><td>$T$</td><td>duration of equivalent triangular loading function (ms)</td></tr><tr><td>$T_{c}$</td><td>thickness of concrete section (in)</td></tr><tr><td>$T_{c}$</td><td>scaled thickness of concrete section $(\mathsf{f t}/\mathsf{I b}^{1/3})$</td></tr><tr><td>$T_{N}$</td><td>effective natural period of vibration (ms)</td></tr><tr><td>rise time (ms) $T_{r}$</td><td></td></tr><tr><td>thickness of sand fill (in) $T_{s}$</td><td></td></tr><tr><td>$T_{s}$</td><td>scaled thickness of sand fill (ft/Ib1/3)</td></tr><tr><td>particle velocity (ft/ms) $u$</td><td></td></tr><tr><td>$u_{u}$</td><td>ultimate flexural or anchorage bond stress (psi)</td></tr><tr><td>$U$</td><td>shock front velocity (ft/ms)</td></tr><tr><td>V</td><td>velocity (in/ms)</td></tr><tr><td>$v_{a}$</td><td>instantaneous velocity at any time (in/ms)</td></tr><tr><td>$v_{b}$</td><td>boundary velocity for primary fragments (ft/sec)</td></tr><tr><td>$v_{c}$</td><td>ultimate shear stress permitted on an unreinforced web (psi)</td></tr></table></body></html></div>


<!-- batch 18 | page 56 -->


<div style="text-align: center;"><html><body><table border="1"><tbody><tr><td>Vf$</td><td colspan="2">maximum post-failure fragment velocity (in/ms)</td></tr><tr><td>$f (avg.)</td><td colspan="2">average post-failure fragment velocity (in/ms)</td></tr><tr><td>$v_{i}$</td><td colspan="2">velocity at incipient failure deflection (in/ms)</td></tr><tr><td>$v_{o}$</td><td colspan="2">initial velocity of primary fragment (ft/sec)</td></tr><tr><td>$v_{r}$</td><td colspan="2">residual velocity of primary fragment after perforation (ft/sec)</td></tr><tr><td>$v_{s}$</td><td colspan="2">striking velocity of primary fragment (ft/sec) $\left(\mathsf{p s i}\right)^{\star}$</td></tr><tr><td>$v_{u}$</td><td colspan="2">ultimate shear stress (psi)</td></tr><tr><td>$v_{u H}$</td><td colspan="2">ultimate shear stress at distance  from the horizontal support $d_{e}$</td></tr><tr><td>$v_{u V}$</td><td colspan="2">ultimate shear stress at distancefrom the vertical support (psi)* $d_{e}$</td></tr><tr><td>V</td><td colspan="2">volume of partially vented chamber $(\mathsf{f t}^{3})$</td></tr><tr><td>$V_{d}$</td><td colspan="2">ultimate direct shear capacity of the concrete of width b (lbs)</td></tr><tr><td>$V_{d H}$</td><td colspan="2">shear at distance from the vertical support on a unit width (Ibs/in)* $d_{e}$</td></tr><tr><td>$V_{d V}$</td><td colspan="2">shear at distance from the horizontal support on a unit width (Ibs/in)* $d_{e}$</td></tr><tr><td>$V_{o}$</td><td colspan="2">volume of structure (f³)</td></tr><tr><td>$V_{s}$</td><td colspan="2">shear at the support on a unit width (Ibs/in)*</td></tr><tr><td>$V_{s H}$</td><td colspan="2">shear at the vertical support on a unit width (Ibs/in)*</td></tr><tr><td>$V_{s V}$</td><td colspan="2">shear at the horizontal support on a unit width (Ibs/in)*</td></tr><tr><td>$V_{u}$</td><td colspan="2">total shear on a width b (lbs)</td></tr><tr><td>$w$</td><td colspan="2">weight density of concrete (lbs/ft3)</td></tr><tr><td>$w_{s}$</td><td colspan="2">weight density of sand $(\mathsf{I b s}/\mathsf{f t}^{3})$</td></tr><tr><td>$W$</td><td colspan="2">charge weight (Ibs)</td></tr><tr><td>$W_{c}$</td><td colspan="2">total weight of explosive containers (Ibs)</td></tr><tr><td>$W_{f}$</td><td colspan="2">weight of primary fragment (o)</td></tr><tr><td>$W_{c o}$</td><td colspan="2">total weight of steel core (lbs)</td></tr><tr><td></td><td colspan="2">total weight of plates 1 and 2, respectively (lbs)</td></tr><tr><td>$W_{c1},W_{c2}$</td><td colspan="2"></td></tr><tr><td>$W_{s}$</td><td colspan="2">width of structure (ft)</td></tr><tr><td>$W D$</td><td colspan="2">work done</td></tr><tr><td>X</td><td colspan="2">yield line location in horizontal direction (in) *</td></tr></tbody></table></body></html></div>


<!-- batch 18 | page 57 -->

X deflection (in)

$X_{a$any deflection (in)

Xe elastic deflection (in)

Xep elasto-plastic deflection (in)

Xf$maximum penetration into concrete of armor-piercing fragments (in)

$X f'}$maximum penetration into concrete of fragments other than armor-piercing 

(in)

$X_m}$maximum transient deflection (in)

$X_}$plastic deflection (in)

$X_{s}$(1)maximum penetration into sand of armor-piercing fragments (in)

(2)static deflection (in)

Xu ultimate deflection (in)

XE equivalent elastic deflection (in)

$X_{}$partial failure deflection (in)

y yield line location in vertical direction (in)*

Z scaled slant distance (ft/lb1/3)

ZA scaled normal distance (ft/|b1/3)

$ZG$scaled ground distance (ft/lb1/3)

α(1)angle formed by the plane of stirrups, lacing, or diagonal 

reinforcement and the plane of the longitudinal reinforcement (deg)

(2)angle of incidence of the pressure front (deg)

B (1)coefficient for determining elastic and elasto-plastic resistances 

(2)particular support rotation angle (deg)

γ(1)coefficient for determining elastic and elasto-plastic deflections 

(2)deflection's increase in support rotation angle after partial failure 

(deg)

日(1)support rotation angle (deg)

(2)angular acceleration (rad/ms2)

Θmax maximum support rotation angle (deg)



<!-- batch 18 | page 58 -->

ΣMN sum of the ultimate unit resisting moments acting along the negative yield lines (in-lbs)



∑MP sum of the ultimate unit resisting moments acting along the positive yield lines (in-lbs)



77777// fixed support 

XXxXxxxx either fixed, restrained, or simple support 

<!-- batch 18 | page 59 -->

## APPENDIX 3C BIBLIOGRAPHY 

1. Blast Resistant Design, NAVFAC Design Manual 2.8, Department of the Navy,Naval Facilities Engineering Command, Alexandria, VA 22332, April 1982.2. Design of Structures to Resist Nuclear Weapons Effects, ASCE Manual of Engineering Practice, No. 42, American Society of Civil Engineers, New York, NY,1961. (1983 Edition under preparation)
3. Designing Facilities to Resist Nuclear Weapons Effects, Structures, TM5-858-3,Headquarters, Department of the Army, Washington, DC.
4. Structures to Resist the Effects of Accidental Explosions, Technical Manual TM51300, Navy Publication NAVFAC P-397, Air Force Manual AFM 88-22, Department of the Army, the Navy, and the Air Force, Washington, DC, June 1969.5. Crawford, R. E., et al, The Air Force Manual for Design and Analysis of Hardened Structures, AFWL-TR-74-102, Air Force Weapons Laboratory, Kirtland Air Force Base, New Mexico, 87117.
6. Healey, J., et al, Design of Steel Structures to Resist the Effects of HE Explosions,by Ammann and Whitney, Consulting Engineers, New York, NY, Technical Report 4837, Picatinny Arsenal, Dover, NJ, August 1975.
7. Hopkins, J., Charts for Predicting Response of a Simple Spring-Mass System to a Bilinear Blast Load, Technical Note N-1450, Naval Civil Engineering Laboratory, Port Hueneme, CA, April 1983.
8. Stea, W., et al, Nonlinear Analysis of Frame Structures Subjected to Blast Overpressures, by Ammann and Whitney, Consulting Engineers, New York, NY,Contractor report ARLCD-CR-77008, U.S. Army Armament Research and Development Command, Large Caliber Weapon Systems Laboratory, Dover, NJ,May 1977.
9. Stea, W., Weissman, S., and Dobbs, N., Overturning and Sliding Analysis of Reinforced Concrete Protective Structures, by Ammann and Whitney, Consulting Engineers, New York, NY, Technical Report 4921, Picatinny Arsenal, Dover, NJ,February 1976.
10. Javornicky, J. and Van Amerongen, C., Tables for the Analysis of Plates, Slabs and Diaphragms Based on the Elastic Theory, Bauverlag GmbH., Wiesbaden/Germany (2nd Edition 1971).
11.Roark, R.J. and Young, W. C., Formulas for Stress and Strain, McGraw Hll, New York (5th Edition 1975).
12.Cohen, E. and Dobbs, N., Design Procedures and Details for Reinforced Concrete Structures Utilized in Explosive Storage and Manufacturing Facilities, Ammann and Whitney, Consulting Engineers, New York, NY, Annals of the New York Academy of Sciences, Conference on Prevention of and Protection Against Accidental Explosion 

<!-- batch 18 | page 60 -->

UFC 3-340-025 December 2008Change 2,1 September 2014of Munitions, Fuels and Other Hazardous Mixtures, Volume 152, Art. 1, October 1968.

