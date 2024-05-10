library(tidyverse)
library(lme4)

result <- read_csv("results/cleaned_results/base_vs_ft_result.csv")
result$combined_unit = paste(result$given_unit, "_", result$answer_unit)

result_by_dimension <- result %>% group_by(same_unit) %>% 
  summarize(average_base=mean(base_accuracy), average_ft = mean(ft_accuracy), size=length(base_accuracy))


  
base_model <- glm(base_accuracy ~ combined_unit + correlation + same_unit, data=result, 
             family = "binomial")
summary(base_model)

ft_model <- glm(ft_accuracy ~ combined_unit + correlation + same_unit, data=result, 
             family = "binomial")
summary(ft_model)
