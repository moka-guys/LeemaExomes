import os

samples=[]

where_to_put_bash_script="/home/wook/Downloads/P635/processed/Reports/"#end with trailing /
folder_containing_fastqs="/home/wook/Downloads/P635/processed"
where_to_put_cat_files="/run/user/1000/gvfs/smb-share\:server\=159.92.115.69\,share\=myshare/170127_LEEMA_EXOMES/Data/Intensities/BaseCalls/"#end with trailing /

output_file=open(where_to_put_bash_script+"cat.sh",'w')

for file in os.listdir(folder_containing_fastqs):
	if file.endswith("fastq.gz"):
		if file.startswith("Undetermined"):
			pass
		else:
			samples.append(file.split("_L00")[0])
			print file.split("_L00")[0]

for sample in set(samples):
	output_file.write("cat "+sample+"*R1_001.fastq.gz >> "+where_to_put_cat_files+"NGSLEEMA_"+sample.split("_")[0]+"_WESLEEMA_"+ sample.split("_")[1] + "_R1_001.fastq.gz\ncat " +sample+ "*R2_001.fastq.gz >> "+where_to_put_cat_files+"NGSLEEMA_"+ sample.split("_")[0]+"_WESLEEMA_"+ sample.split("_")[1] + "_R2_001.fastq.gz\n")

#for sample in set(samples):
#	output_file.write("os.rename(/home/dnanexus/out/combined_fastq/"+sample+"_READ1_001.fastq.gz, /home/dnanexus/out/combined_fastq/"+sample+"_R1_001.fastq.gz)\nos.rename(/home/dnanexus/out/combined_fastq/"+sample+"_READ1_001.fastq.gz, /home/dnanexus/out/combined_fastq/"+sample+"_R1_001.fastq.gz)\n")

output_file.close()
