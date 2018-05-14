library(party)
print(head(readingSkills))
dataset<-read.csv("Data_Final.csv")

high=ifelse(dataset$SEVERITY>=2,"MODERATE","HIGH")
check=ifelse(dataset$SEVERITY>=2,"HIGH","MODERATE")

dataset=data.frame(dataset,high)
dataset=data.frame(dataset,check)

input.dat <- dataset[c(1:10000),]
png(file = "decision_tree_example9.png")

#dataset = dataset[,-31]
names(dataset)
output.tree <- ctree(high ~ DAY_OF_WEEK + LIGHT_CONDITION, data = input.dat)
plot(output.tree)
dev.off()
