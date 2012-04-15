open Printf

let main () =
    let numar = Array.make 3000000 0 in
    let numcl = ref 1 in
    let it = ref 0 in
    let res = ref 1 in
    let maxs = ref 1 in
    for i = 2 to 1000000 do
        numcl := 1;
        it := i;
        while (!it > 1) do
            if (!it mod 2 == 0) then
            begin
                it := !it / 2;
            end
            else
                it := 3*(!it) + 1;
            numcl := !numcl + 1;
        done;
        numar.(i) <- !numcl;
        if (maxs < numcl) then
        begin
            res := i;
            maxs := !numcl;
        end
    done;
    printf "result : %d maxs : %d\n" !res !maxs;;

let _ = Printexc.print main ();;
