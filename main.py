from skillsData import candidateList

def getFrozenApplicants(myList) : # myList is a list of regular sets, where each set represents a group of applicants that possess a required skill
  finalCut = myList[0] 
  for skill in range(0, len(myList) - 1):
    finalCut.intersection_update(myList[skill + 1]) #intersection between the sets
  finalCut = frozenset(finalCut) #frozen set of final intersection of all sets
  return finalCut

print("Welcome Recruiter... you have 50 applicants to review today.")

print("Your candidates have been organized for you into overlapping sets.")
print("... Where each set corresponds to one of four desired skills.")

print("\nMost candidates will posess multiple skills and thus be listed in one or more of the four skill sets.")
print("You are looking for one or more candidates that have the following skills:\n Python, TensorFlow, SQL, C++")

pythonApplicants = set()
tensorFlowApplicants = set()
sqlApplicants = set()
cPlusPlusApplicants = set()

for candidate in candidateList:
  for i in range (0, len(candidate)): #parses through candidate's list of skills
    if candidate[i] == "Python":
      pythonApplicants.add(candidate[0]) #add candidates with that skill to the set for that skill
    if candidate[i] == "TensorFlow":
      tensorFlowApplicants.add(candidate[0])
    if candidate[i] == "SQL":
      sqlApplicants.add(candidate[0])
    if candidate[i] == "C++":
      cPlusPlusApplicants.add(candidate[0])

skillsList = [pythonApplicants, tensorFlowApplicants, sqlApplicants, cPlusPlusApplicants]
       
print("\nHere are the candidates that possess each skill:")
print("Python:", pythonApplicants)
print("TensorFlow:", tensorFlowApplicants)
print("SQL:", sqlApplicants)
print("C++:", cPlusPlusApplicants)

print("\nPlease find the candidates (by ID) that have all of the skills listed above")
finalSet = getFrozenApplicants(skillsList)
print( "\nThe length of your frozen set is", len(finalSet))
print("The applicants that posess all desired skills are:\n", finalSet)
