v 20130925 2
C 40000 40000 0 0 0 title-B.sym
C 47900 46600 1 270 0 voltage-3.sym
{
T 48600 46400 5 8 0 0 270 0 1
device=VOLTAGE_SOURCE
T 47600 46100 5 10 1 1 0 0 1
refdes=V1
T 47600 45800 5 10 1 1 0 0 1
value=13.9V
}
N 48100 45100 48100 45700 4
{
T 48100 45100 5 10 0 0 0 0 1
netname=0
}
N 49000 45100 49000 45300 4
{
T 49100 45100 5 10 1 1 0 0 1
netname=0
}
C 49100 46200 1 90 0 resistor-1.sym
{
T 48700 46500 5 10 0 0 90 0 1
device=RESISTOR
T 48800 46700 5 10 1 1 180 0 1
refdes=R1
T 49200 46600 5 10 1 1 0 0 1
value=4
}
C 49100 45300 1 90 0 resistor-1.sym
{
T 48700 45600 5 10 0 0 90 0 1
device=RESISTOR
T 48800 45800 5 10 1 1 180 0 1
refdes=R2
T 49200 45600 5 10 1 1 0 0 1
value=10
}
N 49000 46200 50000 46200 4
N 48100 46600 48100 47300 4
N 48100 47300 49000 47300 4
N 49000 47300 49000 47100 4