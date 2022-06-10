# Tutorial: OBTAINING A GROMACS TOPOLOGY WITH AN OFF-CENTER CHARGE

### 1.	Geometry optimization at B3LYP/6-311G(d,p) level;
   
   ```
   # Generate the Gaussian input file.
   antechamber -i UNK.mol2 -fi mol2 -o UNK.gjf -fo gcrt -pf y -gn "%nproc=10" -gm "%mem=1500MB" -ch "UNK" -gk "# B3LYP/6-311G(d,p) em=GD3BJ scrf(solvent=water) opt freq" -gv 1 -nc 0 -rn UNK
   #the usage of antechamber could be shown by "antechamber -h"
   
   # Gaussian geometry optimization
   gauss UNK.gjf
   ```
   where, gauss is Gaussian software. It meight be aliased to gauss, g09, g16 in your system.
   
### 2. Single-point electrostatic potential calculation at B3LYP/6-311G(d,p) level;

   ```
   # create Gaussian input file for single-point electrostatic potential calculation
   head -n 4 UNK.gjf > resp.gjf
   echo "# B3LYP/6-311G(d,p) em=GD3BJ scrf(solvent=water) pop=MK IOp(6/33=2,6/42=6) geom=allcheck guess=read" >> resp.gjf
   # B3LYP/6-311G(d,p) can be placed with other functional and basis sets
   head -n 9 UNK.gjf | tail -n 4 >> resp.gjf
   
   # Single-point electrostatic potential calculation
   gauss resp.gjf
   ```

### 3.	Generate mol2 file with RESP charge by antechamber and keep all temporary files;

   ```
   antechamber -i resp.log -fi gout -o lig.mol2 -fo mol2 -c resp -rn UNK -at gaff2
   ```

### 4.	Determine the coordinates of extra points (EP) and generate the GROMACS Topology file with the CGenFF tool;

   ```
   /your/cgenff/installion/path/cgenff_to_gmx.sh mol=NEW.mol2
   ```

### 5.	Add the EP coordinates to the ESP file (a temporary file generated in step 2, normally named ANTECHAMBER.ESP);

### 6.	Modify the IN file (another temporary file generated in step 2, normally named ANTECHAMBER_RESP1.IN) of resp software;

### 7.	Refit RESP charges with modified temporary files by resp software;

### 8.	Replace the charges in the GROMACS Topology file (already generated in step 3) with new RESP charges generated in step 6.
