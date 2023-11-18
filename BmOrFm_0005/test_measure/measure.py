"""
current project: BmOrFm_03          
current file: measure                     
current @author: ilmare                  
you are using PyCharm             
this file create at 21:29 2021/8/2       
"""
import numpy as np
import cmath

def draw_loss():

    # 1 - Ⅰ、2 - Ⅱ、3 - Ⅲ、4 - Ⅳ、5 - Ⅴ、6 - Ⅵ、7 - Ⅶ、8 - Ⅷ、9 - Ⅸ
    for i in range(9):
        result_file = "result.txt"
        testLog = open(file=result_file, mode='a', encoding='utf-8')

        file_name = "testLog0"
        file_input = file_name + str(i + 1) + ".log"
        print(file_input)
        print(file_input, file=testLog)

        conV_name = ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ"]
        label_name = "Configuration " + conV_name[i]
        print("label_name:", label_name)
        print("label_name:", label_name, file=testLog)
        # print("label_name:", label_name, file=result_file)
        # TP, 165, FP, 7, TN, 151, FN, 10
        (TP, FP, TN, FN) = np.loadtxt(fname=file_input, dtype=int, delimiter=',', usecols=(1, 3, 5, 7), unpack=True)
        print("TP:", TP)
        print("TN:", TN)
        print("FP:", FP)
        print("FN:", FN)

        print("TP:", TP, file=testLog)
        print("TN:", TN, file=testLog)
        print("FP:", FP, file=testLog)
        print("FN:", FN, file=testLog)

        Sen = []
        Spc = []
        Prc = []
        Acc = []
        F1 = []
        Mcc = []
        FMI = []
        for j in range(len(TP)):
            if TP[j] + FN[j] == 0:
                Sen = np.append(Sen, (TP[j] + 1 / (TP[j] + FN[j] + 1)))
            else:
                Sen = np.append(Sen, (TP[j] / (TP[j] + FN[j])))
            Spc = np.append(Spc, (TN[j] / (FP[j] + TN[j])))
            Prc = np.append(Prc, (TP[j] / (TP[j] + FP[j])))
            Acc = np.append(Acc, ((TP[j] + TN[j]) / (TP[j] + TN[j] + FP[j] + FN[j])))
            F1 = np.append(F1, (TP[j] * 2) / (2 * TP[j] + FN[j] + FP[j]))
            a = float((TP[j] * TN[j]) - (FP[j] * FN[j]))
            b1 = float(TP[j] + FP[j])
            b2 = float(TP[j] + FN[j])
            b3 = float(TN[j] + FP[j])
            b4 = float(TN[j] + FN[j])
            # print(a)
            c = (cmath.sqrt(b1 * b2 * b3 * b4))
            # print(b1, b2, b3, b4)
            if c == 0:
                Mcc = np.append(Mcc, ((a + 1) / (c + 1)))
            else:
                Mcc = np.append(Mcc, (a / c))
            FMI = np.append(FMI, cmath.sqrt((TP[j] / (TP[j] + FN[j])) * (TP[j] / (TP[j] + FP[j]))))

        print("Sen:", Sen, "Sen.mean:", np.mean(Sen))
        print("Spc:", Spc, "Spc.mean:", np.mean(Spc))
        print("Prc:", Prc, "Prc.mean:", np.mean(Prc))
        print("Acc:", Acc, "Acc.mean:", np.mean(Acc))
        print("F1:", F1, "F1.mean:", np.mean(F1))
        print("MCC:", Mcc, "Mcc.mean:", np.mean(Mcc))
        print("FMI:", FMI, "FMI.mean:", np.mean(FMI))

        print("Sen:", Sen, "Sen.mean:", np.mean(Sen), file=testLog)
        print("Spc:", Spc, "Spc.mean:", np.mean(Spc), file=testLog)
        print("Prc:", Prc, "Prc.mean:", np.mean(Prc), file=testLog)
        print("Acc:", Acc, "Acc.mean:", np.mean(Acc), file=testLog)
        print("F1:", F1, "F1.mean:", np.mean(F1), file=testLog)
        print("MCC:", Mcc, "Mcc.mean:", np.mean(Mcc), file=testLog)
        print("FMI:", FMI, "FMI.mean:", np.mean(FMI), file=testLog)

        print()
        print("\n--------------------------------------------\n", file=testLog)
        print()
        testLog.close()


if __name__ == '__main__':
    draw_loss()
