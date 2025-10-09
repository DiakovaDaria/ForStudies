# Assigning text to a string variable
text = "Before departure, all students leaving for exchange studies should fill in a specialized application form. An application should be submitted in 1 copy and not later than 2 weeks prior to departure for the exchange semester, provided that the students do not have any academic failure. The paper should be submitted to the International Academic Mobility Office (Volkhovsky per., 3, office 207, Tel.: +7 (812) 323 8447). A copy of the invitation letter from a host school - partner of GSOM SPbU has to be attached to the application."
# Finding the starting and ending indexes of the address
i_1 = text.find("(") + 1
i_2 = text.find(", Tel.")
# Outputting the adress by using string slicing
add = text[i_1:i_2]
print(add)
