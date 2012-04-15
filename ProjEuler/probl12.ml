open Printf

let rec prod b = match b with
        [] -> 1
    |   a::ass -> a*(prod ass);;

let itoc b = (int_of_string (Char.escaped b));;

let divnum a =
    let res = ref 0 in
    for i = 1 to a do
        if ((a mod i) == 0) then
            res := !res + 1;
    done;
    !res;;

let main () =
    let factors = Array.make 1000000 0 in
    let it = ref 1 in
    let trig = ref 1 in
    let factn = ref 1 in
    let help = divnum 1024 in
    factors.(1) <- 1;
    factors.(2) <- 2;
    while ((!factn) <= 500) do
        it := !it + 1;
        factors.(!it + 1) <- divnum (!it + 1);
        if (!it mod 2 == 0) then
        begin
            factn := factors.(!it + 1) + (factors.(!it / 2) - 1) + (factors.(!it+1)-1)*(factors.(!it/2)-1);
        end
        else
            factn := factors.(!it) + (factors.((!it+1)/2) - 1) + (factors.((!it+1)/2)-1)*(factors.(!it)-1);
        trig := ((!it)*(!it + 1)) / 2;
        if (!factn > 500) then
        begin
            factn := divnum !trig;
        end;
        (*printf "num : %d | trig : %d | fact : %d | help : %d \n" !it !trig
         * !factn help;*)
    done;
    printf "result : %d \n" !trig;;

let _ = Printexc.print main ();;
