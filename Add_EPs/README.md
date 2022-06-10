# Tutorial: OBTAINING A GROMACS TOPOLOGY WITH AN OFF-CENTER CHARGE

## 1.	Geometry optimization and single-point electrostatic potential calculation at B3LYP/6-311G(d,p) level;

## 2.	Generate mol2 file with RESP charge by antechamber and keep all temporary files;

## 3.	Determine the coordinates of extra points (EP) and generate the GROMACS Topology file with the CGenFF tool;

## 4.	Add the EP coordinates to the ESP file (a temporary file generated in step 2, normally named ANTECHAMBER.ESP);

## 5.	Modify the IN file (another temporary file generated in step 2, normally named ANTECHAMBER_RESP1.IN) of resp software;

## 6.	Refit RESP charges with modified temporary files by resp software;

## 7.	Replace the charges in the GROMACS Topology file (already generated in step 3) with new RESP charges generated in step 6.
