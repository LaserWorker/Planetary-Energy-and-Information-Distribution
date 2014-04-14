Planetary-Energy-and-Information-Distribution
=============================================

For asteroid deflection, a basic model of energy distribution around a planet or asteroid is mathematically defined.


##Idea

Considering configurations of distributed craft orbiting a center of gravitational attraction in space. The craft are equipped for optical transmission synchronization and power distribution. Configurations are designed to obtain complete coverage of all space near and the surface of the gravitational attraction source, while minimizing the required distance. Orbital modeling using defined orbits on stationary planes are created to calculate phases for relative positioning of craft. Space craft are mathematically identified as having time dependent positions relative to craft in alternate orbital planes. These techniques are utilized for identifying specific orbital configurations. Computational models demonstrating geometrical satellite constellations are generated for optical power distribution and propulsion structures useful in space.

##Established Geometric positioning of satellites


$$


\text {All formulas are only valid given “n” and “N” are integers and 0<nN. “N” is the total number of satellites, “a” is the acceleration provided by gravity, “R” is the radius of orbit, “t” is the current time and “n” is the current satellite.}
\\ \space \\

S_1(t,n) = \left[
R \space , \space
{ \pi \over 2 } \space , \space
{ 2 \cdot n \cdot \pi \over N } + { \pi \over 2 } - t \cdot \sqrt { a \over R } \right]
\\ \space \\

C_1(t,n) = \left[
0 \space , \space
R \cdot \cos \left( t \cdot \sqrt{a \over R} + {2 \cdot n \cdot \pi \over N} \right) \space, \space
R \cdot \sin \left( t \cdot \sqrt{a \over R} + {2 \cdot n \cdot \pi \over N} \right) \right]
\\ \space \\

S_2(t,n)= \left\{ \begin{array}{11}
n<{N \over 2} &
\left[
R \space , \space
{\pi \over 2} \space, \space
t \cdot \sqrt{a \over R} + {\pi \cdot (4 \cdot n + 2) \over N} \right] \\
n>{N \over 2} &
\left[
R \space , \space
t \cdot \sqrt{a \over R} + {4 \cdot \pi \over N} \cdot \left( n - {N \over 2} \right) \space , \space
0 \right] \\
 \end{array} \right.
\\ \space \\

C_2(t,n)=\left\{ \begin{array}{11}
n<{N \over 2} &
\left[
0 \space , \space
R \cdot \cos \left( t \cdot \sqrt{a \over R} + {\pi \cdot (4 \cdot n + 2) \over N} \right) \space , \space
R \cdot \sin \left( t \cdot \sqrt{a \over R} + {\pi \cdot (4 \cdot n + 2) \over N} \right) \right] \\
n>{N \over 2} &
\left[
R \cdot \cos \left( t \cdot \sqrt{a \over R} + {4 \cdot \pi \over N} \cdot \left(n - {N \over 2} \right) \right) \space , \space
0 \space , \space
R \cdot \sin \left( t \cdot \sqrt{a \over R} + {4 \cdot \pi \over N} \cdot \left(n - {N \over 2} \right) \right) \right] \\
 \end{array} \right.
\\ \space \\

S_3(t,n)=\left\{ \begin{array}{11}
n<{N \over 3} &
\left[
R \space , \space
t \cdot \sqrt { a \over R } + {\pi \cdot \left( 6 \cdot n + 2 \right) \over N } \space , \space
{\pi \over 2} \right] \\
{2 \cdot N \over 3}>n>{N \over 3} &
\left[
R \space , \space
t \cdot \sqrt { a \over R } + {6 \cdot \pi \over N} \cdot \left( n - {N \over 3} \right) + \pi \space ,

\space
0
\right] \\
n>{2 \cdot N \over 3} &
\left[
R \space , \space
{\pi \over 2} \space , \space
t \cdot \sqrt { a \over R } + {6 \cdot \pi \over N} \cdot \left( n - {2 \cdot N \over 3} \right)
\right] \\
 \end{array} \right.
\\ \space \\

C_3(t,n)=\left\{ \begin{array}{11}
n<{N \over 3} &
\left[
0 \space , \space
R \cdot \cos \left( t \cdot \sqrt{ a \over R} + {\pi \cdot (6 \cdot n + 2) \over N} \right) \space , \space
R \cdot \sin \left( t \cdot \sqrt{ a \over R} + {\pi \cdot (6 \cdot n + 2) \over N} \right) \right] \\
{2 \cdot N \over 3}>n>{N \over 3} &
\left[
R \cdot \cos \left( t \cdot \sqrt{ a \over R} + {6 \cdot \pi \over N} \cdot \left( n - {N \over 3} \right) +

\pi \right) \space , \space
0 \space , \space
R \cdot \sin \left( t \cdot \sqrt{ a \over R} + {6 \cdot \pi \over N} \cdot \left( n - {N \over 3} \right) +

\pi \right) \right] \\
n>{2 \cdot N \over 3} &
\left[
R \cdot \cos \left( t \cdot \sqrt{ a \over R} + {6 \cdot \pi \over N} \cdot \left( n - {N \cdot 2 \over 3}

\right) \right) \space , \space
R \cdot \sin \left( t \cdot \sqrt{ a \over R} + {6 \cdot \pi \over N} \cdot \left( n - {N \cdot 2 \over 3}

\right) \right) \space , \space
0 \right] \\
 \end{array} \right.


$$
