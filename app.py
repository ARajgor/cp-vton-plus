import subprocess
import shutil
import time

t = time.time()
gmm_train = "python train.py --name GMM --stage GMM --workers 4 --save_count 5000 --shuffle"
gmm_test = "python test.py --name GMM --stage GMM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/GMM/gmm_final.pth"
subprocess.call(gmm_test, shell=True)

warp_cloth = "result/GMM/test/warp-cloth"
warp_mask = "result/GMM/test/warp-mask"
shutil.copytree(warp_cloth, "data/test/warp-cloth", dirs_exist_ok=True)
shutil.copytree(warp_mask, "data/test/warp-mask", dirs_exist_ok=True)

tom_train = "python train.py --name TOM --stage TOM --workers 4 --save_count 5000 --shuffle"
tom_test = "python test.py --name TOM --stage TOM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/TOM/tom_final.pth"
subprocess.call(tom_test, shell=True)

print("TOTAL TIME: ", time.time()-t)
print("ALL PROCESS FINISHED")