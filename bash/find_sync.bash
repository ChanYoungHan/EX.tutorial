#! bin/bash

path_to_find=$1
time_to_upload_start=$2
args_time_upload_end=""
if [ $# = 3 ]
then
    args_time_upload_end="-cmin $3"
fi

result_find_files=$(find $path_to_find -mindepth 3 -type f -cmin $time_to_upload_start $args_time_upload_end)
#echo "$result_find_files" | xargs -I{} rsync -e 'ssh -i /media/link/id_rsa -p 23456' -avzd --relative {} ops@1.229.180.178:/volume1/ops/test_db3/
echo "$result_find_files"
echo "$result_find_files" | xargs -I{} mc cp {} local/test

