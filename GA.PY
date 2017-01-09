GA
pick initial population pop
while termination condition not complete do 
   generate set pr of new candidate by recombination 
   generate set pm of new candidates from pop and pr by mutation 
   select new population pop from candidates in pop, pr, pm 
end while
end

-----------------------------------------------------------------

Selection
for all elements of population
   total += fitness of this individual
end for

for all elements of population
   probability = total of probabilities + (fitness / total)
   total of probabilities += probability
end for

while new population is complete
   do twice
      number = Random between 0 and 1
      for all elements of population
         if number > probability < next probability
            element selected
      end for
   end
   produce offspring
end loop
end
