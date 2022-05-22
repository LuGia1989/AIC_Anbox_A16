FILE=./logs/gpu.log
if [ -f "$FILE" ]; then
	echo "$FILE exist.  Deleting...."
	rm "$FILE"
fi
echo "***********************************" >> ./logs/gpu.log
echo "Begin time ....." >> ./logs/gpu.log
echo "***********************************" >> ./logs/gpu.log
date +"%T" >> ./logs/gpu.log
echo "Begin time ....."
date +"%T"

for i in {1..60}; do nvidia-smi >> ./logs/gpu.log; sleep 1; done

echo "***********************************" >> ./logs/gpu.log
echo "End time ....." >> ./logs/gpu.log
echo "***********************************" >> ./logs/gpu.log
date +"%T" >> ./logs/gpu.log
echo "End time ....."
date +"%T"
echo "Calculating GPU memory ..."
python3 nvidia-smi_gpu.py ./logs/gpu.log

