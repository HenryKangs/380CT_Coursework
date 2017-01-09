GRASP (runtotal, SEED)

Best_Solution = 0;

Read_Input ( );

for n = 1,2,3…, runtotal do

   GreedySolution = GreedyRandomizedConstruction (SEED);

   GRASPSolution = LocalSearch (GreedySolution);

   if(Solution better than Best_Solution) then

      UpdateSolution (GRASPSolution, Best_Solution);

   endif

endfor

return (Best_Solution);

end

—————————————————————————————————————————————————————————

LocalSearch (S)

while S not locally optimal do

   Find x′∈ N such that f(x′)≤f(S);

   Solution = x′;

endwhile

return (S);

end

—————————————————————————————————————————————————————————

GreedyRandomizedConstruction(SEED)

Sol = 0;

Sort elements based on incremental costs;

while Solution not complete do

   Build Restricted Candidate List (RCL);

   Choose an element x at random from RCL;

   Sol = Sol∪{x};

   Resort the elements based on incremental costs;

endwhile

return (Sol);

end
