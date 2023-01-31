read -p "请输入计算模式：1.粉末配置;2.buffer配置    " mode
echo "您选择的模式为 $mode"

if [ $mode = "1" ];then
	i=1
	while [ $i = "1" ]
	do
		python run.py
		i=0
		read -p "是否继续：1.是    " conti
		if [ $conti = "1" ];then
			i=1
		fi
	done
fi

if [ $mode = "2" ];then
	i=1
	while [ $i = "1" ]
	do
	
	done
fi
