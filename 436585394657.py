import matplotlib.pyplot as plt
blood_sugar_men = [113, 86, 67, 160, 149, 88, 93, 116, 124, 80, 77, 81, 130]
blood_sugar_women = [121, 89, 62, 128, 149, 78, 73, 117, 124, 55, 77, 101, 120]

type = [blood_sugar_men, blood_sugar_women]
colors = ['g', 'r']
label = ['men','women']
bins = [80, 100, 125]
plt.xlabel ("Blood Surgar Range")
plt.ylabel ("Total no. of patients")
# bla bla bla bla
plt.hist(type, bins=bins, rwidth=0.96, color=colors, label=label, orientation="horizontal")
plt.title("Blood Sugar Level Chart")
plt.legend()
print (plt.show())