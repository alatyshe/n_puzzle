i=0
count=$1
file=$2
size=$([ "$3" != '' ] && echo "$3" || echo "3")
forces=$([ "$4" != '' ] && echo "$4" || echo "-s")


while [[ $i -lt $count ]]; do
	python ../../npuzzle/generator.py $size $forces > $file && python3 main.py $file | egrep -Eo "'Time_spend': .{1,50}"
	i=$[$i+1]
done