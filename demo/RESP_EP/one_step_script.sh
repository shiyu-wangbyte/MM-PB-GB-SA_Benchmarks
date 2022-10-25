#make sure having right path
source $AMBERHOME/amber.sh
export SILCSBIODIR="FILL_IN"
path="./CL_BEBE.mol2"
cp $path UNK.mol2
charge=`python ../script/get_charge.py -p UNK.mol2`
$AMBERHOME/bin/antechamber -i UNK.mol2 -fi mol2 -o UNK.gjf -fo gcrt -pf y -gn "%nproc=12" -gm "%mem=1500MB" -ch "UNK" -gv 1 -nc ${charge}
${GAUSS_PATH}/g09 UNK.gjf
$AMBERHOME/bin/antechamber -i UNK.log -fi gout -o lig.mol2 -fo mol2 -c resp
bash ../ADD_EP_BY.sh
