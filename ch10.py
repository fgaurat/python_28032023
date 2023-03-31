import glob
import re


def main():
    log_dir = './logs'
    logs = glob.glob(f"{log_dir}/*.log")
    # logs = glob.glob(log_dir+"/*.log")

    # logs = sorted(logs)
    logs.sort()
    cpt=0
    for log in logs:
        with open(log) as f:
            for line in f:
                line = line.strip()
                # result = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                # result = re.findall(r'^(.+?)\s', line)
                # print(result)
                # if re.match(r"\"\b404\b\d+",line):
                # result = re.findall(r'\"\s404\s\d+', line)
                if re.search(r"\"\s404\s\d+",line):
                    # print(result)
                    cpt+=1
                    print(line)

    print(cpt)
if __name__=='__main__':
    main()
