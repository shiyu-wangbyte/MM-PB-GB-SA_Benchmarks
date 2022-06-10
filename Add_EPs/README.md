# Tutorial: OBTAINING A GROMACS TOPOLOGY WITH AN OFF-CENTER CHARGE

## 1.	Geometry optimization at B3LYP/6-311G(d,p) level;

   1.1 Generate the Gaussian input file.
   
   ```
   antechamber -i UNK.mol2 -fi mol2 -o UNK.gjf -fo gcrt -pf y -gn "%nproc=10" -gm "%mem=1500MB" -ch "UNK" -gk "# B3LYP/6-311G(d,p) em=GD3BJ scrf(solvent=water) opt freq" -gv 1 -nc 0 -rn UNK
   ```
   
   the usage of antechamber could be shown by "antechamber -h"
   
   1.2 Gaussian geometry optimization
   
   ```
   gauss UNK.gjf
   ```
   
## 2. Single-point electrostatic potential calculation at B3LYP/6-311G(d,p) level;

## 2.	Generate mol2 file with RESP charge by antechamber and keep all temporary files;

## 3.	Determine the coordinates of extra points (EP) and generate the GROMACS Topology file with the CGenFF tool;

## 4.	Add the EP coordinates to the ESP file (a temporary file generated in step 2, normally named ANTECHAMBER.ESP);

## 5.	Modify the IN file (another temporary file generated in step 2, normally named ANTECHAMBER_RESP1.IN) of resp software;

## 6.	Refit RESP charges with modified temporary files by resp software;

## 7.	Replace the charges in the GROMACS Topology file (already generated in step 3) with new RESP charges generated in step 6.