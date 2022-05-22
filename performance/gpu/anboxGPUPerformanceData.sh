#./nvidia-smi_gpu.sh 
./gpuResourceGeneration.sh $1 $2 $3 0 &
sleep 1
./gpuResourceGeneration.sh $1 $2 $3 1 &
sleep 1
./gpuResourceGeneration.sh $1 $2 $3 2 &
sleep 1
./gpuResourceGeneration.sh $1 $2 $3 3
sleep 3
./gpuResourceCalculation.sh
