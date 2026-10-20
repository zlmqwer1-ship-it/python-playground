score1=float(input("请输入第一门课成绩:"))
score2=float(input("请输入第二门课成绩:"))
score3=float(input("请输入第三门课成绩:"))
print("\n");
print(f"总分: {score1 + score2 + score3:.2f}")
print(f"平均分: {(score1 + score2 + score3)/3:.2f}")
print(f"最高分: {max(score1, score2, score3):.2f}")
print(f"最低分: {min(score1, score2, score3):.2f}")