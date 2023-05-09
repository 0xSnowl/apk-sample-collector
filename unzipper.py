import subprocess
import os
import shutil

sample_count = 1
while sample_count <= 100:
    subprocess.call(["/usr/local/bin/7zz", "x", "-pinfected", f"zipped/sample{sample_count:03d}.zip"])
    for file in os.listdir("./"):
        if file.endswith('.apk'):
            src_file = os.path.join(file)
            dst_file = f"infected/sample{sample_count:03d}.apk"
            shutil.move(src_file, dst_file)
            sample_count += 1
            break