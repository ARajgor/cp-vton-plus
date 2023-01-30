import subprocess
import shutil
import time

t = time.time()
cmd_gmm = "python test.py --name GMM --stage GMM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/GMM/gmm_final.pth"
subprocess.call(cmd_gmm, shell=True)

warp_cloth = "result/GMM/test/warp-cloth"
warp_mask = "result/GMM/test/warp-mask"
shutil.copytree(warp_cloth, "data/test/warp-cloth", dirs_exist_ok=True)
shutil.copytree(warp_mask, "data/test/warp-mask", dirs_exist_ok=True)

cmd_tom = "python test.py --name TOM --stage TOM --workers 4 --datamode test --data_list test_pairs.txt --checkpoint checkpoints/TOM/tom_final.pth"
subprocess.call(cmd_tom, shell=True)

print("TOTAL TIME: ", time.time()-t)
print("ALL PROCESS FINISHED")